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
                                Console.WriteLine("LS_UNROUTED_RESIDUAL row=" + row +
                                    " col=" + col +
                                    " mode=" + ls_mixingmode +
                                    " mass_kg=" + residual_transport_mass_kg.ToString("R") +
                                    " deposited_fraction=" + deposited_landslide_fraction.ToString("R") +
                                    " max_deposition_m=" + maximum_allowed_deposition_m.ToString("R") +
                                    " available_material_m=" + available_landslide_material_m.ToString("R"));
                                Debug.WriteLine("there was vertical space to deposit, but no lower space to send sediment to. Sediment left in transport at " + row + " " + col);
                            }"""
if geomorph_text.count(old_boundary) != 1:
    raise RuntimeError(f"boundary residual diagnostic anchor expected once, found {geomorph_text.count(old_boundary)}")
geomorph_text = geomorph_text.replace(old_boundary, new_boundary, 1)
geomorph.write_text(geomorph_text, encoding="utf-8")
print("LORICA_V09_LANDSLIDE_MASS_ROUTING_PATCH_APPLIED")

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

print("LORICA_TREED_V09_PATCH_APPLIED")
