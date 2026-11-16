#!/usr/bin/env python3
"""v1.6 EXPERIMENTAL landslide-scar vegetation/root overlay (separate, opt-in).

NOT part of original TREED or original LORICA. TREED is not modified: its raw
FPC/LAI/rootC output and its traits_restart.jld2 are untouched. The module
acts only on the LORICA side of the exchange, i.e. on the *effective* cover
and *effective* root carbon that LORICA uses for ET, the beta protection term
and Hwang et al. (2015) root cohesion. Disabled unless TREED_coupling.cfg has
`gounsa_experimental_landslide_recovery=on`; when disabled, or for a cell
without a recorded landslide scar, the original code path is executed and the
values are bit-identical.

Hypotheses (scenario parameters, NOT calibrated to Gounsa observations):
  H1  A cell eroded by the native LORICA landslide routine (ero_slid_m < 0)
      loses its standing vegetation; realised cover then recovers toward the
      TREED site potential by first-order (Newton-cooling type) recovery,
          R(a) = 1 - exp(-a / tau_cover),  a = years since the event.
      Remote-sensing studies report scar NDVI recovery over ~10-25 years
      (e.g. Remote Sensing 15:3994, 2023; Teshirogi et al., Geomorphology 398,
      2022: grass scars at Aso within ~12 years).
  H2  Live root carbon regrows with the same factor R(a) (simplification:
      roots track canopy recovery).
  H3  Roots of the removed stand that lie below the slip surface remain as
      dead roots whose reinforcement decays exponentially (Sidle 1991 JEQ
      20:43-52; Sidle 1992 WRR 28:1897-1910: D = exp(-k t^n), here n = 1).
      Coastal Douglas-fir roots lost ~80 % of strength 5 years after harvest
      (k ~ 0.32 /yr), Rocky Mountain Douglas-fir ~60 % (k ~ 0.18 /yr)
      (Burroughs & Thomas 1977, as summarised by Sidle & Terry 1992).
      The fraction of pre-event root carbon below the slip depth z (m) uses
      Jackson et al. (1996, Oecologia 108:389-411): 1 - Y = beta^(100 z),
      beta = 0.976 temperate coniferous forest.
  H4  Deposit-only cells are left unchanged (burial effects not modelled).
A cell with no soil keeps the existing zero_coupling rule (effective = 0).
"""
from pathlib import Path
import sys

ROOT = Path(sys.argv[1])
cp = ROOT / "LORICA/Functions/treed_coupling.cs"
text = cp.read_text(encoding="utf-8-sig")

anchor = "        bool treed_refresh_ks_each_year = false;"
if text.count(anchor) != 1:
    raise RuntimeError("field anchor missing")
fields = r'''
        // ---------------- v1.6 EXPERIMENTAL landslide-scar overlay ----------------
        bool gounsa_rec_enabled = false;
        double gounsa_rec_tau_cover_yr = 4.0;
        double gounsa_rec_dead_root_k_per_yr = 0.18;
        double gounsa_rec_root_beta = 0.976;
        int[,] gounsa_rec_event_t = null;          // LORICA t of the last scar event, -1 none
        double[,] gounsa_rec_slip_depth_m = null;  // eroded depth of that event
        double[,] gounsa_rec_rootC_at_event = null; // effective root C used in the event year
        double[,] gounsa_rec_last_effective_rootC = null;
        public int gounsa_rec_registered_cells = 0;

        void gounsa_rec_ensure()
        {
            if (gounsa_rec_event_t != null && gounsa_rec_event_t.GetLength(0) == nr && gounsa_rec_event_t.GetLength(1) == nc) return;
            gounsa_rec_event_t = new int[nr, nc];
            gounsa_rec_slip_depth_m = new double[nr, nc];
            gounsa_rec_rootC_at_event = new double[nr, nc];
            gounsa_rec_last_effective_rootC = new double[nr, nc];
            for (int r = 0; r < nr; r++) for (int c = 0; c < nc; c++) gounsa_rec_event_t[r, c] = -1;
        }

        // Called after the native slide (read ero_slid_m only).
        void gounsa_rec_register_slide()
        {
            if (!gounsa_rec_enabled) return;
            gounsa_rec_ensure();
            for (int r = 0; r < nr; r++)
                for (int c = 0; c < nc; c++)
                {
                    if (ero_slid_m == null || !(ero_slid_m[r, c] < -1e-12)) continue;
                    gounsa_rec_event_t[r, c] = t;
                    gounsa_rec_slip_depth_m[r, c] = -ero_slid_m[r, c];
                    gounsa_rec_rootC_at_event[r, c] = gounsa_rec_last_effective_rootC[r, c];
                    gounsa_rec_registered_cells++;
                }
        }

        double gounsa_rec_age(int r, int c)
        {
            if (!gounsa_rec_enabled || gounsa_rec_event_t == null || gounsa_rec_event_t[r, c] < 0) return -1.0;
            return (double)(t - gounsa_rec_event_t[r, c]);
        }

        double gounsa_rec_cover_factor(int r, int c)
        {
            double a = gounsa_rec_age(r, c);
            if (a < 1.0) return 1.0;
            return 1.0 - Math.Exp(-a / gounsa_rec_tau_cover_yr);
        }

        double gounsa_rec_dead_rootC(int r, int c)
        {
            double a = gounsa_rec_age(r, c);
            if (a < 1.0) return 0.0;
            double below = Math.Pow(gounsa_rec_root_beta, 100.0 * gounsa_rec_slip_depth_m[r, c]);
            return gounsa_rec_rootC_at_event[r, c] * below * Math.Exp(-gounsa_rec_dead_root_k_per_yr * a);
        }
'''
text = text.replace(anchor, anchor + fields, 1)

# configure from cfg at each TREED call
cfg_anchor = "            configure_treed_landslide_event(cfg);\n            string juliaExe"
if text.count(cfg_anchor) != 1:
    raise RuntimeError("cfg anchor missing")
text = text.replace(cfg_anchor, """            configure_treed_landslide_event(cfg);
            string recMode = cfg_string(cfg, "gounsa_experimental_landslide_recovery", "off");
            if (recMode != "off" && recMode != "on") throw new Exception("gounsa_experimental_landslide_recovery must be off|on");
            gounsa_rec_enabled = recMode == "on";
            gounsa_rec_tau_cover_yr = cfg_double(cfg, "gounsa_rec_tau_cover_yr", 4.0);
            gounsa_rec_dead_root_k_per_yr = cfg_double(cfg, "gounsa_rec_dead_root_k_per_yr", 0.18);
            gounsa_rec_root_beta = cfg_double(cfg, "gounsa_rec_root_beta", 0.976);
            if (gounsa_rec_enabled) gounsa_rec_ensure();
            string juliaExe""", 1)

cover_old = """                    double cover = bareBedrock ? 0.0 :
                        Math.Max(0.0, Math.Min(1.0, fpc[r, c]));"""
if text.count(cover_old) != 1:
    raise RuntimeError("cover anchor missing")
text = text.replace(cover_old, cover_old + """
                    if (gounsa_rec_enabled && !bareBedrock && gounsa_rec_age(r, c) >= 1.0)
                        cover = Math.Max(0.0, Math.Min(1.0, cover * gounsa_rec_cover_factor(r, c)));""", 1)

rc_old = """                    double rc = bareBedrock ? 0.0 : Math.Max(0.0, rootC[r, c]);"""
if text.count(rc_old) != 1:
    raise RuntimeError("rootC anchor missing")
text = text.replace(rc_old, rc_old + """
                    if (gounsa_rec_enabled && !bareBedrock && gounsa_rec_age(r, c) >= 1.0)
                        rc = Math.Max(0.0, rc * gounsa_rec_cover_factor(r, c) + gounsa_rec_dead_rootC(r, c));
                    if (gounsa_rec_enabled) gounsa_rec_last_effective_rootC[r, c] = rc;""", 1)

out_old = """            out_double(Path.Combine(outputDir, "treed_effective_fpc.asc"), effectiveFpc);"""
if text.count(out_old) != 1:
    raise RuntimeError("output anchor missing")
text = text.replace(out_old, out_old + """
            if (gounsa_rec_enabled)
            {
                double[,] recF = new double[nr, nc], recD = new double[nr, nc], recA = new double[nr, nc];
                for (int r = 0; r < nr; r++) for (int c = 0; c < nc; c++)
                {
                    recA[r, c] = gounsa_rec_age(r, c);
                    recF[r, c] = recA[r, c] >= 1.0 ? gounsa_rec_cover_factor(r, c) : 1.0;
                    recD[r, c] = gounsa_rec_dead_rootC(r, c);
                }
                out_double(Path.Combine(outputDir, "gounsa_rec_cover_factor.asc"), recF);
                out_double(Path.Combine(outputDir, "gounsa_rec_dead_rootC_gC_m2.asc"), recD);
                out_double(Path.Combine(outputDir, "gounsa_rec_years_since_scar.asc"), recA);
            }""", 1)
cp.write_text(text, encoding="utf-8")

main = ROOT / "LORICA/LORICA_main.cs"
src = main.read_text(encoding="utf-8-sig")
hook = """                gounsa_capture_landslide_stage("post_slide"); // v1.6 read-only audit"""
if src.count(hook) != 1:
    raise RuntimeError("run instrument_landslide_snapshots.py first")
src = src.replace(hook, hook + """
                gounsa_rec_register_slide(); // v1.6 EXPERIMENTAL overlay (no-op unless enabled)""", 1)
main.write_text(src, encoding="utf-8")
print("GOUNSA_V16_EXPERIMENTAL_LANDSLIDE_RECOVERY_MODULE_APPLIED_DEFAULT_OFF")
