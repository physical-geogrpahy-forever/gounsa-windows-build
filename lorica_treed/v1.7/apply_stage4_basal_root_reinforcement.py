#!/usr/bin/env python3
"""Gounsa v1.7 stage 4: root reinforcement resolved to the slip plane (opt-in).

root_reinforcement_mode = hwang_mean (default) | basal_profile

hwang_mean keeps the existing conversion: Cr = multiplier * K * Tr * Br / rho_r, a
column-mean cohesion that LORICA then uses as the cohesion at the slip plane.

basal_profile replaces K (= 1.2 per metre, read here as Wu's k' = 1.2 over a 1 m
reference column) by the root volume density at the slip plane,

    c_r = k'' * k' * Tr * (Br / rho_r) * f(z_slip)            [Wu and Waldron form]

f(z) [1/m] is the Jackson et al. (1996) profile Y(z) = 1 - beta^(100 z), with beta set by
the cell's rooting depth z_r as the depth of 95 percent of the roots, normalised over the
rooted depth so that the integral of f is 1. Because the integral of f is 1, the depth
integral of c_r equals Hwang's total for any rooted depth up to 1 m. z_slip is the LORICA soil
depth (the infinite-slope failure plane). k'' is the fibre-bundle reduction and is required
explicitly (no default); hwang_root_cohesion_multiplier must be 1 in this mode.

root_profile_truncation = module (default) | soil_bottom
  module       roots end at min(z_r, soil depth), as in the stage-1 root-depth module, so a soil
               deeper than z_r has no root at its base
  soil_bottom  roots end at the soil depth only; z_r only sets the shape (D95)

Needs the stage-3 patch applied first (C# side). LORICA's landslide, critical-rainfall,
hydrology and erosion algorithms are not touched. Default behaviour is byte-identical.

Usage: apply_stage4_basal_root_reinforcement.py <work_dir>
"""
import pathlib
import sys

work = pathlib.Path(sys.argv[1])
MARK = "GOUNSA_V17_STAGE4_BASAL_ROOT"
cs = work / "LORICA" / "Functions" / "treed_coupling.cs"
s = cs.read_text(encoding="utf-8")
if MARK in s:
    raise SystemExit("already patched: %s" % cs)
if "GOUNSA_V17_STAGE3_PAW_PROFILE" not in s:
    raise SystemExit("apply_stage3_paw_profile.py must be applied first")


def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count:
        raise SystemExit("anchor count %d != %d: %r" % (n, count, old[:80]))
    s = s.replace(old, new)


helpers = r'''        // ---- ''' + MARK + r''' ----
        // Jackson et al. (1996) cumulative root fraction Y(z) = 1 - beta^(100 z), z in m.
        // beta is chosen so that the depth of 95 percent of the roots equals d95_m.
        // Returns the root volume density f(z) [1/m] at the slip plane depth zSlip, with the
        // distribution normalised over the rooted depth (integral of f = 1).
        double root_profile_density_at_slip(double zSlip, double d95_m, double soilDepth_m, string truncation)
        {
            if (zSlip <= 0.0 || d95_m <= 1e-6 || soilDepth_m <= 1e-6) return 0.0;
            double lnb = Math.Log(0.05) / (100.0 * d95_m); // ln(beta) < 0
            double zEnd = (truncation == "soil_bottom") ? soilDepth_m : Math.Min(d95_m, soilDepth_m);
            if (zSlip > zEnd + 1e-12) return 0.0;
            double yEnd = 1.0 - Math.Exp(100.0 * zEnd * lnb);
            if (yEnd <= 1e-12) return 0.0;
            double g = -100.0 * lnb * Math.Exp(100.0 * zSlip * lnb);
            return g / yEnd;
        }

        // Wu and Waldron form at the slip plane. rootC in g C m-2.
        // Returns kPa; density is returned through the out argument for the audit raster.
        double basal_root_cohesion_kPa(double rootC_gC_m2, double zSlip, double d95_m, double soilDepth_m,
                                       double kPrime, double kDoublePrime, string truncation,
                                       Dictionary<string, string> cfg, bool applyKdp, out double density)
        {
            density = root_profile_density_at_slip(zSlip, d95_m, soilDepth_m, truncation);
            double fC = cfg_double(cfg, "hwang_root_carbon_fraction", 0.47);
            double rhoRoot = cfg_double(cfg, "hwang_root_density_kg_m3", 435.3);
            double Tr_MPa = hwang_root_tensile_strength_MPa(cfg);
            if (rootC_gC_m2 <= 0.0 || fC <= 0.0 || rhoRoot <= 0.0 || Tr_MPa <= 0.0) return 0.0;
            double V_m = rootC_gC_m2 / (1000.0 * fC) / rhoRoot;   // root volume per ground area [m3 m-2 = m]
            double kdp = applyKdp ? kDoublePrime : 1.0;
            return Math.Max(0.0, kdp * kPrime * (Tr_MPa * 1000.0) * V_m * density);
        }

'''
rep("        string cfg_path(Dictionary<string, string> cfg, string key, string fallback, string baseDir)",
    helpers + "        string cfg_path(Dictionary<string, string> cfg, string key, string fallback, string baseDir)")

setup = r'''            double TrUsed_MPa = hwang_root_tensile_strength_MPa(cfg);
            // ''' + MARK + r'''
            string reinfMode = cfg_string(cfg, "root_reinforcement_mode", "hwang_mean");
            if (reinfMode != "hwang_mean" && reinfMode != "basal_profile")
                throw new Exception("Unknown root_reinforcement_mode: " + reinfMode);
            string profTrunc = cfg_string(cfg, "root_profile_truncation", "module");
            if (profTrunc != "module" && profTrunc != "soil_bottom")
                throw new Exception("Unknown root_profile_truncation: " + profTrunc);
            double kPrime = cfg_double(cfg, "root_k_prime", 1.2);
            double kDoublePrime = Double.NaN;
            double[,] zrRaster = null;
            double[,] slipDensity = null;
            if (reinfMode == "basal_profile")
            {
                string kdpText;
                if (!cfg.TryGetValue("root_k_double_prime", out kdpText))
                    throw new Exception("root_reinforcement_mode=basal_profile needs an explicit root_k_double_prime (no default).");
                kDoublePrime = cfg_double(cfg, "root_k_double_prime", Double.NaN);
                if (Double.IsNaN(kDoublePrime) || kDoublePrime <= 0.0 || kDoublePrime > 1.0)
                    throw new Exception("root_k_double_prime must be in (0, 1].");
                if (Math.Abs(cfg_double(cfg, "hwang_root_cohesion_multiplier", 1.0) - 1.0) > 1e-12)
                    throw new Exception("hwang_root_cohesion_multiplier must be 1 in basal_profile mode; use root_k_double_prime.");
                zrRaster = new double[nr, nc];
                slipDensity = new double[nr, nc];
                string zrFile = Path.Combine(outputDir, "treed_root_depth_m.asc");
                if (File.Exists(zrFile)) read_double(zrFile, zrRaster);
                else
                {
                    double d95 = cfg_double(cfg, "root_profile_d95_m", Double.NaN);
                    if (Double.IsNaN(d95) || d95 <= 0.0)
                        throw new Exception("basal_profile without the root-depth module needs root_profile_d95_m.");
                    for (int r0 = 0; r0 < nr; r0++) for (int c0 = 0; c0 < nc; c0++) zrRaster[r0, c0] = d95;
                }
            }
'''
rep("            double TrUsed_MPa = hwang_root_tensile_strength_MPa(cfg);\n", setup)

rep("                    rootCohesionRaw[r, c] = hwang_root_cohesion_raw_kPa(rc, cfg);\n"
    "                    rootCohesion[r, c] = hwang_root_cohesion_kPa(rc, cfg);\n",
    "                    if (reinfMode == \"basal_profile\")\n"
    "                    {\n"
    "                        double dens0, dens1;\n"
    "                        double zr0 = Math.Max(0.0, zrRaster[r, c]);\n"
    "                        // raw: Wu-level (k'' = 1) at the slip plane; corrected: with k'' and the legacy reduction factor\n"
    "                        rootCohesionRaw[r, c] = basal_root_cohesion_kPa(rc, soildepth_m[r, c], zr0, soildepth_m[r, c], kPrime, kDoublePrime, profTrunc, cfg, false, out dens0);\n"
    "                        rootCohesion[r, c] = cfg_double(cfg, \"hwang_root_cohesion_reduction_factor\", 1.0) *\n"
    "                            basal_root_cohesion_kPa(rc, soildepth_m[r, c], zr0, soildepth_m[r, c], kPrime, kDoublePrime, profTrunc, cfg, true, out dens1);\n"
    "                        slipDensity[r, c] = dens1;\n"
    "                    }\n"
    "                    else\n"
    "                    {\n"
    "                        rootCohesionRaw[r, c] = hwang_root_cohesion_raw_kPa(rc, cfg);\n"
    "                        rootCohesion[r, c] = hwang_root_cohesion_kPa(rc, cfg);\n"
    "                    }\n")

rep("            write_treed_root_cohesion_summary(outputDir, exchangeRoot, rootC, rootCohesionRaw, rootCohesion, cfg, TrUsed_MPa);\n",
    "            if (reinfMode == \"basal_profile\")\n"
    "            {\n"
    "                out_double(Path.Combine(outputDir, \"treed_rootprofile_density_slip_per_m.asc\"), slipDensity);\n"
    "                File.AppendAllText(Path.Combine(outputDir, \"treed_rootcohesion_parameters.txt\"),\n"
    "                    \"root_reinforcement_mode=basal_profile\" + Environment.NewLine +\n"
    "                    \"root_k_prime=\" + kPrime.ToString(\"R\", CultureInfo.InvariantCulture) + Environment.NewLine +\n"
    "                    \"root_k_double_prime=\" + kDoublePrime.ToString(\"R\", CultureInfo.InvariantCulture) + Environment.NewLine +\n"
    "                    \"root_profile_truncation=\" + profTrunc + Environment.NewLine);\n"
    "            }\n"
    "            write_treed_root_cohesion_summary(outputDir, exchangeRoot, rootC, rootCohesionRaw, rootCohesion, cfg, TrUsed_MPa);\n")

cs.write_text(s, encoding="utf-8", newline="")
print("stage 4 patch applied to", cs)
