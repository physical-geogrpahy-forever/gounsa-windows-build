#!/usr/bin/env python3
"""Apply the audited v0.9 LORICA landslide fixes to the extracted v0.5 source bundle."""
from pathlib import Path
import sys

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "work")


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8-sig")
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected exactly one match in {path}, found {n}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


# 1. Unconditionally unstable cells have Crain=0. They must initiate when event
# rainfall is positive; the previous >0 condition silently excluded them.
geomorph = ROOT / "LORICA/Functions/geomorph.cs"
replace_once(
    geomorph,
    "if (crrain_m_d[row, col] > 0.0 && rain_intensity_m_d > crrain_m_d[row, col])",
    "if (crrain_m_d[row, col] >= 0.0 && rain_intensity_m_d > crrain_m_d[row, col])",
    "zero-threshold landslide trigger",
)

# 2. Output diagnostics must not erase the root cohesion returned by TREED.
replace_once(
    geomorph,
    "            root_cohesion_kPa_new = new double[nr, nc];",
    """            if (root_cohesion_kPa_new == null ||
                root_cohesion_kPa_new.GetLength(0) != nr ||
                root_cohesion_kPa_new.GetLength(1) != nc)
                root_cohesion_kPa_new = new double[nr, nc];""",
    "preserve TREED root-cohesion raster",
)

# 3. Add explicit storm-event rainfall to the TREED coupling configuration.
coupling = ROOT / "LORICA/Functions/treed_coupling.cs"
text = coupling.read_text(encoding="utf-8-sig")
class_open = "    public partial class Mother_form\n    {"
if text.count(class_open) != 1:
    raise RuntimeError("could not uniquely locate Mother_form partial class")
text = text.replace(
    class_open,
    class_open + """
        // Optional event rainfall override for the existing LORICA steady-state
        // critical-rainfall landslide trigger. Units are converted to m/day.
        bool treed_landslide_event_override_enabled = false;
        double treed_landslide_event_intensity_m_d = 0.0;
""",
    1,
)
configure = """        void configure_treed_landslide_event(Dictionary<string, string> cfg)
        {
            treed_landslide_event_override_enabled = false;
            treed_landslide_event_intensity_m_d = 0.0;

            string mode = cfg_string(cfg, "landslide_event_mode", "legacy_fraction_annual");
            if (mode.Equals("legacy_fraction_annual", StringComparison.OrdinalIgnoreCase))
                return;

            if (!mode.Equals("explicit_event", StringComparison.OrdinalIgnoreCase))
                throw new Exception("Unknown landslide_event_mode: " + mode);

            double rainfallMm = cfg_double(cfg, "landslide_event_rainfall_mm", Double.NaN);
            double durationHours = cfg_double(cfg, "landslide_event_duration_h", Double.NaN);
            if (Double.IsNaN(rainfallMm) || Double.IsInfinity(rainfallMm) || rainfallMm <= 0.0)
                throw new Exception("landslide_event_rainfall_mm must be finite and > 0");
            if (Double.IsNaN(durationHours) || Double.IsInfinity(durationHours) ||
                durationHours <= 0.0 || durationHours > 24.0)
                throw new Exception("landslide_event_duration_h must be > 0 and <= 24");

            // Mean event intensity converted to m/day to match crrain_m_d.
            treed_landslide_event_intensity_m_d = (rainfallMm / 1000.0) / (durationHours / 24.0);
            if (Double.IsNaN(treed_landslide_event_intensity_m_d) ||
                Double.IsInfinity(treed_landslide_event_intensity_m_d) ||
                treed_landslide_event_intensity_m_d <= 0.0)
                throw new Exception("Invalid derived landslide event intensity");

            treed_landslide_event_override_enabled = true;
        }

"""
anchor = "        void run_treed_coupling()\n        {"
if text.count(anchor) != 1:
    raise RuntimeError("could not uniquely locate run_treed_coupling")
text = text.replace(anchor, configure + anchor, 1)
cfgline = "            var cfg = read_treed_cfg(cfgFile);"
if text.count(cfgline) != 1:
    raise RuntimeError("could not uniquely locate TREED cfg read")
text = text.replace(cfgline, cfgline + "\n            configure_treed_landslide_event(cfg);", 1)
coupling.write_text(text, encoding="utf-8")

# 4. Update annual rainfall forcing before TREED and water_balance, not after
# water_balance in the geomorphic erosion block.
initialise = ROOT / "LORICA/Functions/initialise_update.cs"
helper = """        void update_time_varying_rainfall_for_current_timestep()
        {
            if (!check_time_rain.Checked) return;
            if (rainfall_record == null || rainfall_record.Length == 0)
                throw new InvalidOperationException("Time-varying rainfall is enabled but rainfall_record is empty.");

            int recordIndex = t % rainfall_record.Length;
            rain_value_m = 0.001 * rainfall_record[recordIndex]; // rainfall record is mm/year -> m/year

            if (rain_m != null && dtm != null)
            {
                for (int r = 0; r < nr; r++)
                for (int c = 0; c < nc; c++)
                    if (dtm[r, c] != nodata_value)
                        rain_m[r, c] = rain_value_m;
            }
        }

"""
anchor = "        void initialise_every()       //fills the inputgrids with values"
text = initialise.read_text(encoding="utf-8-sig")
if text.count(anchor) != 1:
    raise RuntimeError("could not uniquely locate initialise_every")
text = text.replace(anchor, helper + anchor, 1)
old_rain = """                        if (check_time_rain.Checked)
                        {
                            corrected_t = t;
                            while (corrected_t > rainfall_record.Length) { corrected_t -= rainfall_record.Length; }

                            rain_value_m = 0.001 * rainfall_record[corrected_t]; //from mm (in record) to m (LORICA)   
                                                                                 // mvdm -1 weggehaald van corrected_t, leidde tot OutOfRange errors
                                                                                 // changed rain[row, col] to rain_value_m, due to errors, this is not spatial, but temporal variation
                                                                                 //this should be improved for when rainfall is not also spatially variable //ArT
                        }
"""
new_rain = """                        if (check_time_rain.Checked)
                        {
                            corrected_t = t % rainfall_record.Length;
                            rain_value_m = 0.001 * rainfall_record[corrected_t]; // mm/year -> m/year
                            rain_m[row, col] = rain_value_m;
                        }
"""
if text.count(old_rain) != 1:
    raise RuntimeError(f"annual rainfall update block expected once, found {text.count(old_rain)}")
text = text.replace(old_rain, new_rain, 1)
initialise.write_text(text, encoding="utf-8")

# 5. Prepare current-year rainfall before the daily climate series and hydrology.
main = ROOT / "LORICA/LORICA_main.cs"
replace_once(
    main,
    "        private void every_timestep()    //performs actions in every timestep\n        {",
    "        private void every_timestep()    //performs actions in every timestep\n        {\n            update_time_varying_rainfall_for_current_timestep();",
    "update annual rainfall before daily hydrology",
)

# 6. Explicit event rainfall override; retain the original fraction-of-annual
# rainfall behaviour when event mode is not enabled.
old_event = """                    rain_value_m = rain_m[row, col]; //AleG_neww
                    rain_intensity_m_d = daily_rain_as_frct_of_annual * rain_value_m;
                    rain_intensity_m_d *= n;"""
new_event = """                    rain_value_m = rain_m[row, col]; // annual precipitation [m/year]
                    if (treed_landslide_event_override_enabled)
                        rain_intensity_m_d = treed_landslide_event_intensity_m_d;
                    else
                        rain_intensity_m_d = daily_rain_as_frct_of_annual * rain_value_m;
                    rain_intensity_m_d *= n;"""
replace_once(geomorph, old_event, new_event, "explicit storm event intensity")

# 7. In situation C, deposit_slid_mass_mm1/mm2 has already subtracted the
# deposited fraction from the transport arrays. Multiplying the residual arrays
# by (1 - deposited_fraction) again loses that fraction a second time.
# This affects both fully mixed and layer-preserving transport.
geomorph_text = geomorph.read_text(encoding="utf-8-sig")
mass_replacements = [
    (
        "sediment_in_transport_kg[row + i, col + j, tex] += distribution_fraction * undeposited_landslide_fraction * sediment_in_transport_kg[row, col, tex];",
        "sediment_in_transport_kg[row + i, col + j, tex] += distribution_fraction * sediment_in_transport_kg[row, col, tex];",
        "mixed mineral residual routing",
    ),
    (
        "young_SOM_in_transport_kg[row + i, col + j] += distribution_fraction * undeposited_landslide_fraction * young_SOM_in_transport_kg[row, col];",
        "young_SOM_in_transport_kg[row + i, col + j] += distribution_fraction * young_SOM_in_transport_kg[row, col];",
        "mixed young SOM residual routing",
    ),
    (
        "old_SOM_in_transport_kg[row + i, col + j] += distribution_fraction * undeposited_landslide_fraction * old_SOM_in_transport_kg[row, col];",
        "old_SOM_in_transport_kg[row + i, col + j] += distribution_fraction * old_SOM_in_transport_kg[row, col];",
        "mixed old SOM residual routing",
    ),
    (
        """lay_sediment_in_transport_kg[row + i, col + j, lay, tex] +=
                                                                    distribution_fraction * undeposited_landslide_fraction *
                                                                    lay_sediment_in_transport_kg[row, col, lay, tex];""",
        """lay_sediment_in_transport_kg[row + i, col + j, lay, tex] +=
                                                                    distribution_fraction *
                                                                    lay_sediment_in_transport_kg[row, col, lay, tex];""",
        "layered mineral residual routing",
    ),
    (
        """lay_young_SOM_in_transport_kg[row + i, col + j, lay] +=
                                                                distribution_fraction * undeposited_landslide_fraction *
                                                                lay_young_SOM_in_transport_kg[row, col, lay];""",
        """lay_young_SOM_in_transport_kg[row + i, col + j, lay] +=
                                                                distribution_fraction *
                                                                lay_young_SOM_in_transport_kg[row, col, lay];""",
        "layered young SOM residual routing",
    ),
    (
        """lay_old_SOM_in_transport_kg[row + i, col + j, lay] +=
                                                                distribution_fraction * undeposited_landslide_fraction *
                                                                lay_old_SOM_in_transport_kg[row, col, lay];""",
        """lay_old_SOM_in_transport_kg[row + i, col + j, lay] +=
                                                                distribution_fraction *
                                                                lay_old_SOM_in_transport_kg[row, col, lay];""",
        "layered old SOM residual routing",
    ),
]
for old, new, label in mass_replacements:
    n = geomorph_text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {n}")
    geomorph_text = geomorph_text.replace(old, new, 1)

# Audit residual material before the existing cleanup block. The current LORICA
# path logs this condition but subsequently clears the transport arrays; expose
# the exact mass so the domain-edge accounting can be tested independently.
old_boundary = 'if (powered_slope_sum == 0) { Debug.WriteLine("there was vertical space to deposit, but no lower space to send sediment to. Sediment left in transport at " + row + " " + col); }'
new_boundary = """if (powered_slope_sum == 0)
                            {
                                double residual_transport_mass_kg = 0.0;
                                if (ls_mixingmode == 1)
                                {
                                    for (int tex = 0; tex < n_texture_classes; tex++)
                                        residual_transport_mass_kg += sediment_in_transport_kg[row, col, tex];
                                    residual_transport_mass_kg += young_SOM_in_transport_kg[row, col] + old_SOM_in_transport_kg[row, col];
                                }
                                else if (ls_mixingmode == 2)
                                {
                                    for (int lay = 0; lay < max_soil_layers; lay++)
                                    {
                                        for (int tex = 0; tex < n_texture_classes; tex++)
                                            residual_transport_mass_kg += lay_sediment_in_transport_kg[row, col, lay, tex];
                                        residual_transport_mass_kg += lay_young_SOM_in_transport_kg[row, col, lay];
                                        residual_transport_mass_kg += lay_old_SOM_in_transport_kg[row, col, lay];
                                    }
                                }
                                System.IO.File.AppendAllText(System.IO.Path.Combine(workdir, "landslide_mass_trace.log"),
                                    "C_NO_LOWER row=" + row + " col=" + col +
                                    " mode=" + ls_mixingmode +
                                    " mass_kg=" + residual_transport_mass_kg.ToString("R") +
                                    " deposited_fraction=" + deposited_landslide_fraction.ToString("R") +
                                    " max_deposition_m=" + maximum_allowed_deposition_m.ToString("R") +
                                    " available_material_m=" + available_landslide_material_m.ToString("R") + Environment.NewLine);
                                Debug.WriteLine("there was vertical space to deposit, but no lower space to send sediment to. Sediment left in transport at " + row + " " + col);
                            }"""
if geomorph_text.count(old_boundary) != 1:
    raise RuntimeError(f"boundary residual diagnostic anchor expected once, found {geomorph_text.count(old_boundary)}")
geomorph_text = geomorph_text.replace(old_boundary, new_boundary, 1)

# Record layered transport mass immediately before the initiation/continuation
# cleanup. This is the second cleanup site and can be reached without entering
# situation_C, so it must be audited separately.
ab_anchor = """                        //so, all cells under this cell have received the sediment in transport and OM in transport that they need.
                        //We will work on those cells when it's their turn but not now.
                        //for now, we are done with this cell, and it does no longer have sediment in transport:
"""
ab_diag = ab_anchor + """                        if (ls_mixingmode == 2)
                        {
                            double residualBeforeClear_kg = 0.0;
                            for (int auditLayer = 0; auditLayer < max_soil_layers; auditLayer++)
                            {
                                for (int auditTex = 0; auditTex < n_texture_classes; auditTex++)
                                    residualBeforeClear_kg += lay_sediment_in_transport_kg[row, col, auditLayer, auditTex];
                                residualBeforeClear_kg += lay_young_SOM_in_transport_kg[row, col, auditLayer];
                                residualBeforeClear_kg += lay_old_SOM_in_transport_kg[row, col, auditLayer];
                            }
                            if (residualBeforeClear_kg > 1e-8)
                            {
                                System.IO.File.AppendAllText(System.IO.Path.Combine(workdir, "landslide_mass_trace.log"),
                                    "AB_PRE_CLEAR row=" + row + " col=" + col +
                                    " situation_A=" + situation_A + " situation_B=" + situation_B +
                                    " slope_sum=" + powered_slope_sum.ToString("R") +
                                    " residual_kg=" + residualBeforeClear_kg.ToString("R") + Environment.NewLine);
                            }
                        }
"""
if geomorph_text.count(ab_anchor) != 1:
    raise RuntimeError(f"A/B cleanup anchor expected once, found {geomorph_text.count(ab_anchor)}")
geomorph_text = geomorph_text.replace(ab_anchor, ab_diag, 1)

# Also audit the situation-C cleanup path, after any downstream routing but
# immediately before the transport arrays are reset.
c_cleanup_anchor = """                        //clean up after we are done here:
                        if (ls_mixingmode == 1)
"""
c_cleanup_diag = """                        //clean up after we are done here:
                        if (ls_mixingmode == 2)
                        {
                            double residualBeforeClearC_kg = 0.0;
                            for (int auditLayer = 0; auditLayer < max_soil_layers; auditLayer++)
                            {
                                for (int auditTex = 0; auditTex < n_texture_classes; auditTex++)
                                    residualBeforeClearC_kg += lay_sediment_in_transport_kg[row, col, auditLayer, auditTex];
                                residualBeforeClearC_kg += lay_young_SOM_in_transport_kg[row, col, auditLayer];
                                residualBeforeClearC_kg += lay_old_SOM_in_transport_kg[row, col, auditLayer];
                            }
                            if (residualBeforeClearC_kg > 1e-8)
                            {
                                System.IO.File.AppendAllText(System.IO.Path.Combine(workdir, "landslide_mass_trace.log"),
                                    "C_PRE_CLEAR row=" + row + " col=" + col +
                                    " slope_sum=" + powered_slope_sum.ToString("R") +
                                    " residual_kg=" + residualBeforeClearC_kg.ToString("R") +
                                    Environment.NewLine);
                            }
                        }
                        if (ls_mixingmode == 1)
"""
if geomorph_text.count(c_cleanup_anchor) != 1:
    raise RuntimeError(f"situation-C cleanup anchor expected once, found {geomorph_text.count(c_cleanup_anchor)}")
geomorph_text = geomorph_text.replace(c_cleanup_anchor, c_cleanup_diag, 1)

# 7b. Layer-preserving deposition must use the actual mass-derived thickness
# of each transported source layer. The former implementation multiplied
# depofraction by segmentThickness/expected_lay_thick a second time. When a
# cell held less than one template layer of transport, this left material in
# transport even when depofraction == 1; the subsequent cleanup erased it.
method_start = geomorph_text.find("        double deposit_slid_mass_mm2(")
method_end = geomorph_text.find("        void BlockShiftDownWithBottomMerge_Strict", method_start)
if method_start < 0 or method_end < 0 or method_end <= method_start:
    raise RuntimeError("could not locate complete deposit_slid_mass_mm2 method")

new_method = r"""        double calc_layered_transport_thickness_m(int row, int col)
        {
            double totalThickness_m = 0.0;
            for (int layer = 0; layer < max_soil_layers; layer++)
            {
                double[] layerTextures_kg = new double[n_texture_classes];
                double fineMass_kg = 0.0;
                for (int tex = 0; tex < n_texture_classes; tex++)
                {
                    layerTextures_kg[tex] = lay_sediment_in_transport_kg[row, col, layer, tex];
                    if (tex >= 1) fineMass_kg += layerTextures_kg[tex];
                }

                double youngMass_kg = lay_young_SOM_in_transport_kg[row, col, layer];
                double oldMass_kg = lay_old_SOM_in_transport_kg[row, col, layer];
                fineMass_kg += youngMass_kg + oldMass_kg;

                if (fineMass_kg > 1e-12)
                {
                    double layerThickness_m = calc_thickness_from_mass(
                        layerTextures_kg, youngMass_kg, oldMass_kg);
                    if (!Double.IsNaN(layerThickness_m) &&
                        !Double.IsInfinity(layerThickness_m) &&
                        layerThickness_m > 0.0)
                        totalThickness_m += layerThickness_m;
                }
                else if (layerTextures_kg[0] > 1e-12)
                {
                    totalThickness_m += layerTextures_kg[0] / (dx * dx * 2700.0);
                }
            }
            return totalThickness_m;
        }

        double deposit_slid_mass_mm2(int deprow, int depcol, double dep_depth_m)
        {
            double locally_deposited_mass_kg = 0.0;
            const double Eps = 1e-12;
            const double ClampEps = 1e-12;

            double ClampNonNegative(double x)
            {
                if (x < 0.0 && x > -ClampEps) return 0.0;
                return (x < 0.0) ? 0.0 : x;
            }

            if (Double.IsNaN(dep_depth_m) || Double.IsInfinity(dep_depth_m) || dep_depth_m <= Eps)
                return 0.0;

            // Allocate the requested deposition depth from the transported
            // profile in source-layer order. Each fraction is based on the
            // actual thickness represented by that layer's transported mass,
            // not on the original template thickness.
            List<int> sourceLayerIndices = new List<int>();
            List<double> depositionSegmentThicknesses_m = new List<double>();
            List<double> layerWithdrawalFractions = new List<double>();

            double remainingDepositionDepth_m = dep_depth_m;
            for (int sourceLayer = 0;
                 sourceLayer < max_soil_layers && remainingDepositionDepth_m > Eps;
                 sourceLayer++)
            {
                double[] layerTextures_kg = new double[n_texture_classes];
                double fineMass_kg = 0.0;
                double totalMass_kg = 0.0;

                for (int textureClass = 0; textureClass < n_texture_classes; textureClass++)
                {
                    double value = lay_sediment_in_transport_kg[deprow, depcol, sourceLayer, textureClass];
                    layerTextures_kg[textureClass] = value;
                    totalMass_kg += value;
                    if (textureClass >= 1) fineMass_kg += value;
                }

                double youngMass_kg = lay_young_SOM_in_transport_kg[deprow, depcol, sourceLayer];
                double oldMass_kg = lay_old_SOM_in_transport_kg[deprow, depcol, sourceLayer];
                totalMass_kg += youngMass_kg + oldMass_kg;
                fineMass_kg += youngMass_kg + oldMass_kg;

                if (totalMass_kg <= Eps) continue;

                double availableLayerThickness_m;
                if (fineMass_kg > Eps)
                    availableLayerThickness_m = calc_thickness_from_mass(
                        layerTextures_kg, youngMass_kg, oldMass_kg);
                else
                    availableLayerThickness_m = layerTextures_kg[0] / (dx * dx * 2700.0);

                if (Double.IsNaN(availableLayerThickness_m) ||
                    Double.IsInfinity(availableLayerThickness_m) ||
                    availableLayerThickness_m <= Eps)
                    continue;

                double segmentThickness_m = Math.Min(
                    remainingDepositionDepth_m, availableLayerThickness_m);
                double withdrawalFraction = segmentThickness_m / availableLayerThickness_m;
                withdrawalFraction = Math.Max(0.0, Math.Min(1.0, withdrawalFraction));

                sourceLayerIndices.Add(sourceLayer);
                depositionSegmentThicknesses_m.Add(segmentThickness_m);
                layerWithdrawalFractions.Add(withdrawalFraction);
                remainingDepositionDepth_m -= segmentThickness_m;
            }

            int totalNumberOfSegments = depositionSegmentThicknesses_m.Count;
            if (totalNumberOfSegments == 0)
                return locally_deposited_mass_kg;

            // Keep one bottom layer for pre-existing material. Any overflow
            // segments are merged into that bottom layer without discarding mass.
            int numberOfTopSegments = Math.Min(totalNumberOfSegments, max_soil_layers - 1);
            BlockShiftDownWithBottomMerge_Strict(
                deprow, depcol, numberOfTopSegments, max_soil_layers);

            // Place the upper segments into newly opened top layers.
            for (int segmentIndex = 0; segmentIndex < numberOfTopSegments; segmentIndex++)
            {
                int sourceLayer = sourceLayerIndices[segmentIndex];
                double segmentThickness_m = depositionSegmentThicknesses_m[segmentIndex];
                double withdrawalFraction = layerWithdrawalFractions[segmentIndex];

                layerthickness_m[deprow, depcol, segmentIndex] = segmentThickness_m;
                for (int textureClass = 0; textureClass < n_texture_classes; textureClass++)
                    texture_kg[deprow, depcol, segmentIndex, textureClass] = 0.0;
                young_SOM_kg[deprow, depcol, segmentIndex] = 0.0;
                old_SOM_kg[deprow, depcol, segmentIndex] = 0.0;

                for (int textureClass = 0; textureClass < n_texture_classes; textureClass++)
                {
                    double availableMass_kg =
                        lay_sediment_in_transport_kg[deprow, depcol, sourceLayer, textureClass];
                    double withdrawnMass_kg = availableMass_kg * withdrawalFraction;
                    texture_kg[deprow, depcol, segmentIndex, textureClass] += withdrawnMass_kg;
                    lay_sediment_in_transport_kg[deprow, depcol, sourceLayer, textureClass] =
                        ClampNonNegative(availableMass_kg - withdrawnMass_kg);
                    locally_deposited_mass_kg += withdrawnMass_kg;
                }

                double availableYoung_kg =
                    lay_young_SOM_in_transport_kg[deprow, depcol, sourceLayer];
                double availableOld_kg =
                    lay_old_SOM_in_transport_kg[deprow, depcol, sourceLayer];
                double withdrawnYoung_kg = availableYoung_kg * withdrawalFraction;
                double withdrawnOld_kg = availableOld_kg * withdrawalFraction;

                young_SOM_kg[deprow, depcol, segmentIndex] += withdrawnYoung_kg;
                old_SOM_kg[deprow, depcol, segmentIndex] += withdrawnOld_kg;
                lay_young_SOM_in_transport_kg[deprow, depcol, sourceLayer] =
                    ClampNonNegative(availableYoung_kg - withdrawnYoung_kg);
                lay_old_SOM_in_transport_kg[deprow, depcol, sourceLayer] =
                    ClampNonNegative(availableOld_kg - withdrawnOld_kg);
                locally_deposited_mass_kg += withdrawnYoung_kg + withdrawnOld_kg;
            }

            // Merge remaining segments into the bottom layer when the profile
            // has fewer available slots than transported source layers.
            if (totalNumberOfSegments > numberOfTopSegments)
            {
                int bottomLayerIndex = max_soil_layers - 1;
                for (int segmentIndex = numberOfTopSegments;
                     segmentIndex < totalNumberOfSegments;
                     segmentIndex++)
                {
                    int sourceLayer = sourceLayerIndices[segmentIndex];
                    double segmentThickness_m = depositionSegmentThicknesses_m[segmentIndex];
                    double withdrawalFraction = layerWithdrawalFractions[segmentIndex];

                    layerthickness_m[deprow, depcol, bottomLayerIndex] += segmentThickness_m;

                    for (int textureClass = 0; textureClass < n_texture_classes; textureClass++)
                    {
                        double availableMass_kg =
                            lay_sediment_in_transport_kg[deprow, depcol, sourceLayer, textureClass];
                        double withdrawnMass_kg = availableMass_kg * withdrawalFraction;
                        texture_kg[deprow, depcol, bottomLayerIndex, textureClass] += withdrawnMass_kg;
                        lay_sediment_in_transport_kg[deprow, depcol, sourceLayer, textureClass] =
                            ClampNonNegative(availableMass_kg - withdrawnMass_kg);
                        locally_deposited_mass_kg += withdrawnMass_kg;
                    }

                    double availableYoung_kg =
                        lay_young_SOM_in_transport_kg[deprow, depcol, sourceLayer];
                    double availableOld_kg =
                        lay_old_SOM_in_transport_kg[deprow, depcol, sourceLayer];
                    double withdrawnYoung_kg = availableYoung_kg * withdrawalFraction;
                    double withdrawnOld_kg = availableOld_kg * withdrawalFraction;

                    young_SOM_kg[deprow, depcol, bottomLayerIndex] += withdrawnYoung_kg;
                    old_SOM_kg[deprow, depcol, bottomLayerIndex] += withdrawnOld_kg;
                    lay_young_SOM_in_transport_kg[deprow, depcol, sourceLayer] =
                        ClampNonNegative(availableYoung_kg - withdrawnYoung_kg);
                    lay_old_SOM_in_transport_kg[deprow, depcol, sourceLayer] =
                        ClampNonNegative(availableOld_kg - withdrawnOld_kg);
                    locally_deposited_mass_kg += withdrawnYoung_kg + withdrawnOld_kg;
                }
            }

            update_all_layer_thicknesses(deprow, depcol);
            return locally_deposited_mass_kg;
        }

"""
geomorph_text = geomorph_text[:method_start] + new_method + geomorph_text[method_end:]

old_available = "double available_landslide_material_m = calc_thickness_from_mass(available_mass_kg, available_youngsom, available_oldsom);"
new_available = """double available_landslide_material_m = (ls_mixingmode == 2)
                            ? calc_layered_transport_thickness_m(row, col)
                            : calc_thickness_from_mass(available_mass_kg, available_youngsom, available_oldsom);"""
if geomorph_text.count(old_available) != 1:
    raise RuntimeError(f"available material thickness anchor expected once, found {geomorph_text.count(old_available)}")
geomorph_text = geomorph_text.replace(old_available, new_available, 1)

old_call = "deposit_slid_mass_mm2(deposited_landslide_fraction, row, col, maximum_allowed_deposition_m)"
new_call = "deposit_slid_mass_mm2(row, col, maximum_allowed_deposition_m)"
if geomorph_text.count(old_call) != 1:
    raise RuntimeError(f"layer-preserving deposit call expected once, found {geomorph_text.count(old_call)}")
geomorph_text = geomorph_text.replace(old_call, new_call, 1)


# 7c. Preserve residual transport when a cell has no lower neighbour.
# The original cleanup unconditionally zeroed the transport arrays even when
# the routing routine had nowhere to send the material. In a closed internal
# sink this is temporary storage, not boundary export. Keep it in the arrays;
# a separate explicit outlet rule is required before material can be counted
# as exported from the model domain.
ab_cleanup_old = """                        if (ls_mixingmode == 1)
                        {
                            for (int tex = 0; tex < n_texture_classes; tex++)
                            {
                                sediment_in_transport_kg[row, col, tex] = 0;
                            }
                            young_SOM_in_transport_kg[row, col] = 0;
                            old_SOM_in_transport_kg[row, col] = 0;
                        }
                        if (ls_mixingmode == 2)
                        {

                            for (int layer = 0; layer < max_soil_layers; layer++)
                            {
                                for (int tex = 0; tex < n_texture_classes; tex++)
                                {
                                    lay_sediment_in_transport_kg[row, col, layer, tex] = 0;
                                }
                                lay_old_SOM_in_transport_kg[row, col, layer] = 0;
                                lay_young_SOM_in_transport_kg[row, col, layer] = 0;
                            }
                        }
"""
ab_cleanup_new = """                        if (powered_slope_sum > 0.0)
                        {
                            if (ls_mixingmode == 1)
                            {
                                for (int tex = 0; tex < n_texture_classes; tex++)
                                    sediment_in_transport_kg[row, col, tex] = 0;
                                young_SOM_in_transport_kg[row, col] = 0;
                                old_SOM_in_transport_kg[row, col] = 0;
                            }
                            if (ls_mixingmode == 2)
                            {
                                for (int layer = 0; layer < max_soil_layers; layer++)
                                {
                                    for (int tex = 0; tex < n_texture_classes; tex++)
                                        lay_sediment_in_transport_kg[row, col, layer, tex] = 0;
                                    lay_old_SOM_in_transport_kg[row, col, layer] = 0;
                                    lay_young_SOM_in_transport_kg[row, col, layer] = 0;
                                }
                            }
                        }
                        // If powered_slope_sum is zero, keep the residual in transport
                        // storage at this closed sink instead of deleting its mass.
"""
if geomorph_text.count(ab_cleanup_old) != 1:
    raise RuntimeError(f"A/B transport cleanup expected once, found {geomorph_text.count(ab_cleanup_old)}")
geomorph_text = geomorph_text.replace(ab_cleanup_old, ab_cleanup_new, 1)

c_cleanup_old = """                        if (ls_mixingmode == 1)
                        {
                            for (int tex = 0; tex < n_texture_classes; tex++)
                            {
                                sediment_in_transport_kg[row, col, tex] = 0;
                            }
                            young_SOM_in_transport_kg[row, col] = 0;
                            old_SOM_in_transport_kg[row, col] = 0;
                        }
                        if (ls_mixingmode == 2)
                        {
                            for (int lay = 0; lay < max_soil_layers; lay++)
                            {
                                for (int tex = 0; tex < n_texture_classes; tex++)
                                {
                                    lay_sediment_in_transport_kg[row, col, lay, tex] = 0;
                                }
                                lay_young_SOM_in_transport_kg[row, col, lay] = 0;
                                lay_old_SOM_in_transport_kg[row, col, lay] = 0;
                            }
                        }
"""
c_cleanup_new = """                        if (powered_slope_sum > 0.0)
                        {
                            if (ls_mixingmode == 1)
                            {
                                for (int tex = 0; tex < n_texture_classes; tex++)
                                    sediment_in_transport_kg[row, col, tex] = 0;
                                young_SOM_in_transport_kg[row, col] = 0;
                                old_SOM_in_transport_kg[row, col] = 0;
                            }
                            if (ls_mixingmode == 2)
                            {
                                for (int lay = 0; lay < max_soil_layers; lay++)
                                {
                                    for (int tex = 0; tex < n_texture_classes; tex++)
                                        lay_sediment_in_transport_kg[row, col, lay, tex] = 0;
                                    lay_young_SOM_in_transport_kg[row, col, lay] = 0;
                                    lay_old_SOM_in_transport_kg[row, col, lay] = 0;
                                }
                            }
                        }
                        // With no lower neighbour, retain the residual material in
                        // transport storage. It is not silently discarded or exported.
"""
if geomorph_text.count(c_cleanup_old) != 1:
    raise RuntimeError(f"situation-C transport cleanup expected once, found {geomorph_text.count(c_cleanup_old)}")
geomorph_text = geomorph_text.replace(c_cleanup_old, c_cleanup_new, 1)

# 7d. Carry residual landslide material across model timesteps in both mixing modes.
# The original per-event initializer clears the fully mixed transport arrays and
# resets remaining_vertical_size_m. Layer-resolved arrays survive by accident,
# but are not reactivated because their runout thickness is reset to zero.
# Use the layer arrays as persistent landslide-only storage for mode 1 as well;
# this keeps them separate from the mixed arrays shared with water erosion.
slide_method_start = geomorph_text.find("        void calculate_slide_new()")
reset_start = geomorph_text.find("                for (row = 0; row < nr; row++)", slide_method_start)
reset_end = geomorph_text.find('                //Debug.WriteLine("prepared");', reset_start)
if slide_method_start < 0 or reset_start < 0 or reset_end < 0 or reset_end <= reset_start:
    raise RuntimeError("could not locate calculate_slide_new initialization block")

new_reset = r"""                for (row = 0; row < nr; row++)
                {
                    for (col = 0; col < nc; col++)
                    {
                        if (dtm[row, col] != nodata_value)
                        {
                            ero_slid_m[row, col] = 0;
                            sed_slid_m[row, col] = 0;
                            slidestatus[row, col] = 0;
                            remaining_vertical_size_m[row, col] = 0;

                            // The mixed arrays are transient and can also be
                            // cleared by LORICA's water-erosion timestep setup.
                            for (int material = 0; material < 5; material++)
                                sediment_in_transport_kg[row, col, material] = 0;
                            young_SOM_in_transport_kg[row, col] = 0;
                            old_SOM_in_transport_kg[row, col] = 0;

                            if (ls_mixingmode == 1)
                            {
                                // Restore fully mixed residuals from layer 0
                                // of the landslide-only persistent store.
                                double[] storedMass = new double[n_texture_classes];
                                double storedYoung = 0.0;
                                double storedOld = 0.0;
                                for (int storedLayer = 0; storedLayer < max_soil_layers; storedLayer++)
                                {
                                    for (int tex = 0; tex < n_texture_classes; tex++)
                                    {
                                        storedMass[tex] += lay_sediment_in_transport_kg[row, col, storedLayer, tex];
                                        lay_sediment_in_transport_kg[row, col, storedLayer, tex] = 0.0;
                                    }
                                    storedYoung += lay_young_SOM_in_transport_kg[row, col, storedLayer];
                                    storedOld += lay_old_SOM_in_transport_kg[row, col, storedLayer];
                                    lay_young_SOM_in_transport_kg[row, col, storedLayer] = 0.0;
                                    lay_old_SOM_in_transport_kg[row, col, storedLayer] = 0.0;
                                }

                                double storedFineMass = storedYoung + storedOld;
                                for (int tex = 1; tex < n_texture_classes; tex++)
                                    storedFineMass += storedMass[tex];

                                for (int tex = 0; tex < n_texture_classes; tex++)
                                    sediment_in_transport_kg[row, col, tex] = storedMass[tex];
                                young_SOM_in_transport_kg[row, col] = storedYoung;
                                old_SOM_in_transport_kg[row, col] = storedOld;

                                double storedThickness_m = 0.0;
                                if (storedFineMass > 1e-12)
                                    storedThickness_m = calc_thickness_from_mass(storedMass, storedYoung, storedOld);
                                else if (storedMass[0] > 1e-12)
                                    storedThickness_m = storedMass[0] / (dx * dx * 2700.0);

                                if (!Double.IsNaN(storedThickness_m) &&
                                    !Double.IsInfinity(storedThickness_m) &&
                                    storedThickness_m > 0.0)
                                    remaining_vertical_size_m[row, col] = storedThickness_m;
                            }
                            else if (ls_mixingmode == 2)
                            {
                                // Layer-preserving transport already lives in
                                // the persistent layer arrays. Reconstruct the
                                // runout state from its actual mass-derived depth.
                                double storedThickness_m = calc_layered_transport_thickness_m(row, col);
                                if (!Double.IsNaN(storedThickness_m) &&
                                    !Double.IsInfinity(storedThickness_m) &&
                                    storedThickness_m > 0.0)
                                    remaining_vertical_size_m[row, col] = storedThickness_m;
                            }
                        }
                    }
                }
"""
geomorph_text = geomorph_text[:reset_start] + new_reset + geomorph_text[reset_end:]

# After the event has routed all cells, move any fully mixed residual back into
# the landslide-only persistent arrays. This prevents the next initialise_every()
# call from deleting it and avoids letting water erosion consume it as its own
# transient sediment load.
dtm_anchor = "                //now update the DTM:"
if geomorph_text.count(dtm_anchor) != 1:
    raise RuntimeError(f"DTM update anchor expected once, found {geomorph_text.count(dtm_anchor)}")
mixed_store = r"""                if (ls_mixingmode == 1)
                {
                    for (row = 0; row < nr; row++)
                    {
                        for (col = 0; col < nc; col++)
                        {
                            if (dtm[row, col] == nodata_value) continue;

                            for (int storedLayer = 0; storedLayer < max_soil_layers; storedLayer++)
                            {
                                for (int tex = 0; tex < n_texture_classes; tex++)
                                    lay_sediment_in_transport_kg[row, col, storedLayer, tex] = 0.0;
                                lay_young_SOM_in_transport_kg[row, col, storedLayer] = 0.0;
                                lay_old_SOM_in_transport_kg[row, col, storedLayer] = 0.0;
                            }

                            for (int tex = 0; tex < n_texture_classes; tex++)
                            {
                                lay_sediment_in_transport_kg[row, col, 0, tex] =
                                    sediment_in_transport_kg[row, col, tex];
                                sediment_in_transport_kg[row, col, tex] = 0.0;
                            }
                            lay_young_SOM_in_transport_kg[row, col, 0] =
                                young_SOM_in_transport_kg[row, col];
                            lay_old_SOM_in_transport_kg[row, col, 0] =
                                old_SOM_in_transport_kg[row, col];
                            young_SOM_in_transport_kg[row, col] = 0.0;
                            old_SOM_in_transport_kg[row, col] = 0.0;
                        }
                    }
                }

"""
geomorph_text = geomorph_text.replace(dtm_anchor, mixed_store + dtm_anchor, 1)

geomorph.write_text(geomorph_text, encoding="utf-8")
print("LORICA_V09_LANDSLIDE_MASS_ROUTING_PATCH_APPLIED")

# 7e. Correct the water-erosion outlet test: grid index 0 is a valid
# boundary cell, not an out-of-domain coordinate. The previous <= 0 test
# falsely exported sediment from valid cells one cell inside the domain.
replace_once(
    geomorph,
    "if ((row + i) >= nr | (row + i) <= 0 | (col + j) >= nc | (col + j) <= 0)",
    "if ((row + i) >= nr | (row + i) < 0 | (col + j) >= nc | (col + j) < 0)",
    "water-erosion outlet boundary off-by-one",
)

# 7f. Event counters are diagnostics, not cumulative simulation state.
# Start each landslide event with fresh counts, and count an initiation only
# when soil is physically removed. The original triggering, erosion, runout,
# deposition, and persistent-layer transport equations remain unchanged.
replace_once(
    geomorph,
    "nb_ok = 0; nb_check = 0; all_grids = 0.0;",
    "nb_ok = 0; nb_check = 0; all_grids = 0.0;\n"
    "                landslide_initiation_cells = 0;\n"
    "                landslide_continuation_cells = 0;\n"
    "                landslide_deposition_cells = 0;",
    "reset event-local landslide counters",
)
replace_once(
    geomorph,
    "landslide_initiation_cells += 1;",
    "if (actual_erosion_m > 0.0)\n"
    "                                landslide_initiation_cells += 1;",
    "count physical initiations rather than critical-rain exceedance alone",
)

# 7g. Optional coupling-side bare-bedrock sensitivity treatment.
# 'legacy' is the default and preserves TREED output transfer exactly.
# 'zero_coupling' removes *local* root reinforcement and FPC-based ET
# correction only where the current LORICA cell has no soil. It does NOT
# change TREED plant physiology, root carbon, trait optimization, or ecology.
replace_once(
    coupling,
    '            double etFull = cfg_double(cfg, "treed_et_factor_full_cover", 0.85);',
    '''            double etFull = cfg_double(cfg, "treed_et_factor_full_cover", 0.85);
            string bedrockMode = cfg_string(cfg, "treed_bare_bedrock_policy", "legacy");
            if (bedrockMode != "legacy" && bedrockMode != "zero_coupling")
                throw new Exception("Unknown treed_bare_bedrock_policy: " + bedrockMode);
            double[,] effectiveRootC = new double[nr, nc];
            double[,] effectiveFpc = new double[nr, nc];''',
    "optional bare-bedrock coupling policy",
)
replace_once(
    coupling,
    '''                    double cover = Math.Max(0.0, Math.Min(1.0, fpc[r, c]));
                    aridity_vegetation[r, c] = cover;''',
    '''                    // A no-soil grid cell may still have TREED biomass
                    // because TREED permits direct rainfall use at PAW=0.
                    // Do not interpret that biomass as a local soil-root bond
                    // in the explicitly selected sensitivity case.
                    bool bareBedrock = bedrockMode == "zero_coupling" &&
                                       soildepth_m[r, c] <= 0.0;
                    double cover = bareBedrock ? 0.0 :
                        Math.Max(0.0, Math.Min(1.0, fpc[r, c]));
                    effectiveFpc[r, c] = cover;
                    aridity_vegetation[r, c] = cover;''',
    "exclude zero-soil cover only for sensitivity mode",
)
replace_once(
    coupling,
    '                    double rc = Math.Max(0.0, rootC[r, c]);',
    '''                    double rc = bareBedrock ? 0.0 : Math.Max(0.0, rootC[r, c]);
                    effectiveRootC[r, c] = rc;''',
    "exclude zero-soil root reinforcement only for sensitivity mode",
)
replace_once(
    coupling,
    '            out_double(Path.Combine(outputDir, "treed_root_biomass_kgDM_m2.asc"), rootDryBiomass);',
    '''            out_double(Path.Combine(outputDir, "treed_effective_rootC_gC_m2.asc"), effectiveRootC);
            out_double(Path.Combine(outputDir, "treed_effective_fpc.asc"), effectiveFpc);
            out_double(Path.Combine(outputDir, "treed_root_biomass_kgDM_m2.asc"), rootDryBiomass);''',
    "write audit of effective coupling vegetation",
)
replace_once(
    coupling,
    '                "root_allocation_mode=" + cfg_string(cfg, "root_allocation_mode", "adaptive_experimental") + Environment.NewLine +',
    '''                "treed_bare_bedrock_policy=" + bedrockMode + Environment.NewLine +
                "root_allocation_mode=" + cfg_string(cfg, "root_allocation_mode", "adaptive_experimental") + Environment.NewLine +''',
    "audit bare bedrock treatment",
)

# 8. Add explicit defaults without changing the legacy model behaviour.
cfg_paths = [ROOT / "coupling/TREED_coupling.cfg"]
cfg_paths += sorted((ROOT / "coupling/scenarios").glob("*.cfg"))
for path in cfg_paths:
    cfg_text = path.read_text(encoding="utf-8-sig")
    if "landslide_event_mode=" not in cfg_text:
        cfg_text += (
            "\n# LORICA rainfall-triggered shallow-landslide forcing.\n"
            "# legacy_fraction_annual preserves the original interface.\n"
            "# explicit_event uses mean rainfall_mm over duration_h.\n"
            "landslide_event_mode=legacy_fraction_annual\n"
            "landslide_event_rainfall_mm=100.0\n"
            "landslide_event_duration_h=6.0\n"
        )
        path.write_text(cfg_text, encoding="utf-8")


# 9. Give each TREED ECA cell its own deterministic RNG stream. The ECA
# algorithm and objective function are unchanged; only its RNG is made explicit.
treed_model = ROOT / "TREED/src/TREED_model_functions.jl"
treed_physiology = ROOT / "TREED/src/TREED_physiological_functions.jl"
if not treed_model.is_file() or not treed_physiology.is_file():
    raise RuntimeError("TREED source files missing from the extracted v0.5 bundle")

model_text = treed_model.read_text(encoding="utf-8-sig")
model_anchor = "# Climate input struct"
seed_declaration = """# Per-cell ECA seed base supplied by treed_lorica_driver_seeded_wrapper.jl.
# The cell index is added in run_TREED_optimization, making the RNG independent
# of Julia's thread scheduling and thread count.
const TREED_ECA_BASE_SEED = parse(UInt64, get(ENV, "TREED_RANDOM_SEED", "20261113"))

"""
if model_text.count(model_anchor) != 1:
    raise RuntimeError("TREED climate-input anchor expected exactly once")
if "TREED_ECA_BASE_SEED" in model_text:
    raise RuntimeError("TREED per-cell ECA seed patch already present")
model_text = model_text.replace(model_anchor, seed_declaration + model_anchor, 1)

old_loop = """    # Run loop on multiple threads   
    Threads.@threads for i = 1:length(lookup(traits_start.H, X))
        for j = 1:length(lookup(traits_start.H, Y))"""
new_loop = """    # Run loop on multiple threads. Each cell has its own seeded ECA RNG.
    nY = length(lookup(traits_start.H, Y))
    Threads.@threads for i = 1:length(lookup(traits_start.H, X))
        for j = 1:nY"""
if model_text.count(old_loop) != 1:
    raise RuntimeError(f"TREED ECA threaded-loop anchor expected exactly once, found {model_text.count(old_loop)}")
model_text = model_text.replace(old_loop, new_loop, 1)

old_optimizer_call = """                optimized_traits = trait_optimizer(env = env, par = pars2, trait_optimization_function = trait_optimization_function, iters = 20)"""
new_optimizer_call = """                cell_seed = TREED_ECA_BASE_SEED + UInt64((i - 1) * nY + j)
                optimized_traits = trait_optimizer(env = env, par = pars2,
                    trait_optimization_function = trait_optimization_function,
                    iters = 20, seed = cell_seed)"""
if model_text.count(old_optimizer_call) != 1:
    raise RuntimeError(f"TREED trait-optimizer call expected exactly once, found {model_text.count(old_optimizer_call)}")
model_text = model_text.replace(old_optimizer_call, new_optimizer_call, 1)
treed_model.write_text(model_text, encoding="utf-8")

phys_text = treed_physiology.read_text(encoding="utf-8-sig")
old_signature = "trait_optimizer = function(; env, par,trait_optimization_function, iters)"
new_signature = "trait_optimizer = function(; env, par,trait_optimization_function, iters, seed=20261113)"
if phys_text.count(old_signature) != 1:
    raise RuntimeError(f"TREED trait_optimizer signature expected exactly once, found {phys_text.count(old_signature)}")
phys_text = phys_text.replace(old_signature, new_signature, 1)
old_solve = "Optimization.solve(prob, ECA(), maxiters = iters, abstol = 50)"
new_solve = "Optimization.solve(prob, ECA(options=Metaheuristics.Options(seed=seed)), maxiters = iters, abstol = 50)"
n_solve = phys_text.count(old_solve)
if n_solve != 2:
    raise RuntimeError(f"TREED ECA solve calls expected exactly twice (fixed_original and adaptive_experimental), found {n_solve}")
phys_text = phys_text.replace(old_solve, new_solve)
treed_physiology.write_text(phys_text, encoding="utf-8")

print("TREED_PER_CELL_ECA_RNG_PATCH_APPLIED")

print("LORICA_TREED_V09_PATCH_APPLIED")
