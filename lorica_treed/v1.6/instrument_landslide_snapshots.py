#!/usr/bin/env python3
"""v1.6 landslide state instrumentation for LORICA-TREED (NO PHYSICS CHANGE).

Run after apply_v11_formula_patch.py, instrument_water_export.py and
fix_downstream_sediment_accumulation.py.

Inside the native LORICA `every_timestep()` the landslide block is

    soil_update_split_and_combine_layers();
    comb_sort();
    ini_slope();
    calculate_critical_rain();
    calculate_slide_new();
    soil_update_split_and_combine_layers();

TREED is called earlier in the same timestep, so the TREED raster written for
year t describes vegetation BEFORE the year-t landslide.  To separate the
pre-slide and post-slide states this patch inserts two read-only capture calls:

    calculate_critical_rain();
    gounsa_capture_landslide_stage("pre_slide");      # after threshold, before slide
    calculate_slide_new();
    soil_update_split_and_combine_layers();
    gounsa_capture_landslide_stage("post_slide");     # after slide + layer update

The capture method only clones existing arrays and sums existing mass arrays.
It never writes to any LORICA state variable, so all physics, routing and
TREED exchange are unchanged.  The annual runner reads the captured copies via
reflection after `every_timestep()` returns.
"""
from pathlib import Path
import sys

ROOT = Path(sys.argv[1])

main = ROOT / "LORICA/LORICA_main.cs"
src = main.read_text(encoding="utf-8-sig")
old_block = """                ini_slope();
                calculate_critical_rain();
                calculate_slide_new();
                soil_update_split_and_combine_layers();
            }"""
if src.count(old_block) != 1:
    raise RuntimeError("Cannot uniquely locate the native every_timestep landslide block")
new_block = """                ini_slope();
                calculate_critical_rain();
                gounsa_capture_landslide_stage("pre_slide"); // v1.6 read-only audit
                calculate_slide_new();
                soil_update_split_and_combine_layers();
                gounsa_capture_landslide_stage("post_slide"); // v1.6 read-only audit
            }"""
src = src.replace(old_block, new_block, 1)
main.write_text(src, encoding="utf-8")

cp = ROOT / "LORICA/Functions/treed_coupling.cs"
text = cp.read_text(encoding="utf-8-sig")
anchor = "        bool treed_refresh_ks_each_year = false;"
if text.count(anchor) != 1:
    raise RuntimeError("Cannot uniquely locate TREED annual field anchor")
hook = r'''
        // ------------------------------------------------------------------
        // v1.6 read-only landslide state capture (no physics change).
        // Keys: "<stage>.<variable>", stage = pre_slide | post_slide.
        // ------------------------------------------------------------------
        public Dictionary<string, double[,]> gounsa_ls_grids = new Dictionary<string, double[,]>();
        public Dictionary<string, double> gounsa_ls_scalars = new Dictionary<string, double>();
        public int gounsa_ls_capture_count = 0;

        double[,] gounsa_clone_or_nan(double[,] a)
        {
            double[,] o = new double[nr, nc];
            for (int r = 0; r < nr; r++)
                for (int c = 0; c < nc; c++)
                    o[r, c] = (a == null || a.GetLength(0) != nr || a.GetLength(1) != nc) ? Double.NaN : a[r, c];
            return o;
        }

        void gounsa_capture_landslide_stage(string stage)
        {
            gounsa_ls_capture_count++;
            string p = stage + ".";
            gounsa_ls_grids[p + "dtm_m"] = gounsa_clone_or_nan(dtm);
            gounsa_ls_grids[p + "soildepth_m"] = gounsa_clone_or_nan(soildepth_m);
            gounsa_ls_grids[p + "crrain_m_d"] = gounsa_clone_or_nan(crrain_m_d);
            gounsa_ls_grids[p + "root_cohesion_kPa"] = gounsa_clone_or_nan(root_cohesion_kPa_new);
            gounsa_ls_grids[p + "effective_fpc_lorica"] = gounsa_clone_or_nan(aridity_vegetation);
            gounsa_ls_grids[p + "cohesion_factor"] = gounsa_clone_or_nan(Cohesion_factor);
            gounsa_ls_grids[p + "stslope_radians"] = gounsa_clone_or_nan(stslope_radians);
            gounsa_ls_grids[p + "contributing_cells"] = gounsa_clone_or_nan(contributing_cells);
            gounsa_ls_grids[p + "transmissivity_m2_d"] = gounsa_clone_or_nan(transmissiv_m2_d);
            gounsa_ls_grids[p + "sat_bd_kg_m3"] = gounsa_clone_or_nan(sat_bd_kg_m3);
            gounsa_ls_grids[p + "peak_friction_angle_radians"] = gounsa_clone_or_nan(peak_friction_angle_radians);
            gounsa_ls_grids[p + "ero_slid_m"] = gounsa_clone_or_nan(ero_slid_m);
            gounsa_ls_grids[p + "sed_slid_m"] = gounsa_clone_or_nan(sed_slid_m);
            gounsa_ls_grids[p + "Ks_topsoil_m_h"] = gounsa_clone_or_nan(Ks_topsoil_m_h);

            double[,] soilMass = new double[nr, nc];
            double[,] persistentMass = new double[nr, nc];
            double[,] transientMass = new double[nr, nc];
            double[,] paw = new double[nr, nc];
            double totalSoil = 0.0, totalPersistent = 0.0, totalTransient = 0.0;
            for (int r = 0; r < nr; r++)
            {
                for (int c = 0; c < nc; c++)
                {
                    double s = 0.0, pm = 0.0, tm = 0.0;
                    for (int l = 0; l < max_soil_layers; l++)
                    {
                        for (int k = 0; k < n_texture_classes; k++)
                        {
                            s += texture_kg[r, c, l, k];
                            pm += lay_sediment_in_transport_kg[r, c, l, k];
                        }
                        s += young_SOM_kg[r, c, l] + old_SOM_kg[r, c, l];
                        pm += lay_young_SOM_in_transport_kg[r, c, l] + lay_old_SOM_in_transport_kg[r, c, l];
                    }
                    for (int k = 0; k < n_texture_classes; k++) tm += sediment_in_transport_kg[r, c, k];
                    tm += young_SOM_in_transport_kg[r, c] + old_SOM_in_transport_kg[r, c];
                    soilMass[r, c] = s; persistentMass[r, c] = pm; transientMass[r, c] = tm;
                    totalSoil += s; totalPersistent += pm; totalTransient += tm;
                    paw[r, c] = (dtm[r, c] == nodata_value) ? Double.NaN : treed_paw_mm(r, c);
                }
            }
            gounsa_ls_grids[p + "soil_mass_kg"] = soilMass;
            gounsa_ls_grids[p + "persistent_landslide_mass_kg"] = persistentMass;
            gounsa_ls_grids[p + "transient_transport_mass_kg"] = transientMass;
            gounsa_ls_grids[p + "paw_mm"] = paw;
            gounsa_ls_scalars[p + "total_soil_mass_kg"] = totalSoil;
            gounsa_ls_scalars[p + "total_persistent_landslide_mass_kg"] = totalPersistent;
            gounsa_ls_scalars[p + "total_transient_transport_mass_kg"] = totalTransient;
            gounsa_ls_scalars[p + "landslide_initiation_cells"] = landslide_initiation_cells;
            gounsa_ls_scalars[p + "landslide_continuation_cells"] = landslide_continuation_cells;
            gounsa_ls_scalars[p + "landslide_deposition_cells"] = landslide_deposition_cells;
            gounsa_ls_scalars[p + "treed_water_sediment_export_kg"] = treed_water_sediment_export_kg;
            gounsa_ls_scalars[p + "event_intensity_m_d"] = treed_landslide_event_override_enabled ? treed_landslide_event_intensity_m_d : Double.NaN;
            gounsa_ls_scalars[p + "t"] = t;
        }'''
text = text.replace(anchor, anchor + hook, 1)
cp.write_text(text, encoding="utf-8")
print("LORICA_V16_LANDSLIDE_SNAPSHOT_INSTRUMENTED_NO_PHYSICS_CHANGE")
