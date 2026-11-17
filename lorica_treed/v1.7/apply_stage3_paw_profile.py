#!/usr/bin/env python3
"""Gounsa v1.7 stage 3: layered plant-available-water profile from LORICA to TREED.

Opt-in (root_depth_paw_profile=uniform by default). Needs the root-depth module
and the stage-2 patch applied first. With the default every code path evaluates
exactly as before. LORICA only gains a read-only export; no hydrology, landslide,
critical-rainfall or erosion algorithm changes.

LORICA has no soil-water state (monthly Turc/Budyko ET, no store), so the legacy
PAW/365 term has nothing to be replaced by there. What LORICA does have is the
layer-resolved Saxton and Rawls available water. This patch hands that profile to
the root-depth module in place of the uniform-PAW assumption.

Usage: apply_stage3_paw_profile.py <work_dir>
"""
import pathlib
import shutil
import sys

work = pathlib.Path(sys.argv[1])
here = pathlib.Path(__file__).resolve().parent
MARK = "GOUNSA_V17_STAGE3_PAW_PROFILE"


def patch(path, edits):
    s = path.read_text(encoding="utf-8")
    if MARK in s:
        raise SystemExit("already patched: %s" % path)
    for old, new, count in edits:
        n = s.count(old)
        if n != count:
            raise SystemExit("anchor count %d != %d in %s: %r" % (n, count, path, old[:70]))
        s = s.replace(old, new)
    path.write_text(s, encoding="utf-8", newline="")


src = work / "TREED" / "src"
if "GOUNSA_V17_STAGE2_MORTALITY" not in (src / "TREED.jl").read_text(encoding="utf-8"):
    raise SystemExit("apply_stage2_mortality_dispersal.py must be applied first")
# TREED_rootdepth.jl carries the profile support (inactive without a profile). Refresh it.
shutil.copyfile(here / "TREED_rootdepth.jl", src / "TREED_rootdepth.jl")

patch(src / "TREEDlocalstep.jl", [
    ("                          landslide_mask=nothing, cellsize_m=NaN,\n",
     "                          landslide_mask=nothing, cellsize_m=NaN,\n"
     "                          paw_profile=nothing, paw_profile_step_m=NaN, # " + MARK + "\n", 1),
    ("    rootdepth_begin!(pars2, climate, traitdir; alpha_mm=rain_alpha_mm, lambda_per_day=rain_lambda_per_day)\n",
     "    rootdepth_begin!(pars2, climate, traitdir; alpha_mm=rain_alpha_mm, lambda_per_day=rain_lambda_per_day,\n"
     "                     paw_profile=paw_profile, paw_profile_step_m=paw_profile_step_m)\n", 1),
])

patch(work / "coupling" / "treed_lorica_driver.jl", [
    ("    rd_alpha = Float64.(st[:,3]); rd_lambda = Float64.(st[:,4])\nend\n",
     "    rd_alpha = Float64.(st[:,3]); rd_lambda = Float64.(st[:,4])\nend\n"
     "# " + MARK + "\n"
     "pawprof=nothing; pawstep=NaN\n"
     "paw_mode=lowercase(get(conf,\"root_depth_paw_profile\",\"uniform\"))\n"
     "paw_mode in (\"uniform\",\"layered\") || error(\"root_depth_paw_profile must be uniform or layered\")\n"
     "if paw_mode == \"layered\"\n"
     "    rd_mode != \"off\" || error(\"root_depth_paw_profile=layered needs root_depth_mode != off\")\n"
     "    pfile = joinpath(input_dir, \"paw_profile_mm.csv\")\n"
     "    isfile(pfile) || error(\"Missing $pfile\")\n"
     "    plines = readlines(pfile)\n"
     "    hdr1 = plines[1]\n"
     "    startswith(hdr1, \"# step_m=\") || error(\"paw_profile_mm.csv header missing\")\n"
     "    hparts = split(strip(hdr1[3:end]))\n"
     "    pawstep = parse(Float64, split(hparts[1], '=')[2])\n"
     "    nnodes = parse(Int, split(hparts[2], '=')[2])\n"
     "    pawprof = zeros(Float64, nc, nr, nnodes)\n"
     "    for ln in plines[2:end]\n"
     "        isempty(strip(ln)) && continue\n"
     "        f = split(ln, ',')\n"
     "        length(f) == nnodes + 2 || error(\"paw_profile_mm.csv row has $(length(f)) fields, expected $(nnodes+2)\")\n"
     "        pawprof[parse(Int, f[2]) + 1, parse(Int, f[1]) + 1, :] = parse.(Float64, f[3:end])\n"
     "    end\n"
     "end\n", 1),
    ("    landslide_mask=ls_mask,cellsize_m=cs)\n",
     "    landslide_mask=ls_mask,cellsize_m=cs,\n"
     "    paw_profile=pawprof,paw_profile_step_m=pawstep)\n", 1),
])

patch(work / "LORICA" / "Functions" / "treed_coupling.cs", [
    ("        void configure_treed_landslide_event(Dictionary<string, string> cfg)\n",
     "        // " + MARK + ": available water per metre of soil [mm m-1] for one layer\n"
     "        // (same Saxton and Rawls theta33 - theta1500 as treed_paw_mm).\n"
     "        double treed_paw_density_mm_per_m(int r, int c, int lay)\n"
     "        {\n"
     "            double sand = texture_kg[r, c, lay, 1];\n"
     "            double silt = texture_kg[r, c, lay, 2];\n"
     "            double clay = texture_kg[r, c, lay, 3] + texture_kg[r, c, lay, 4];\n"
     "            double om = old_SOM_kg[r, c, lay] + young_SOM_kg[r, c, lay];\n"
     "            double fine = sand + silt + clay;\n"
     "            if (fine <= 0) return 0.0;\n"
     "            double S = sand / fine;\n"
     "            double C = clay / fine;\n"
     "            double OM = (fine + om > 0) ? 100.0 * om / (fine + om) : 0.0;\n"
     "            double theta33t = -0.251 * S + 0.195 * C + 0.011 * OM\n"
     "                            + 0.006 * S * OM - 0.027 * C * OM\n"
     "                            + 0.452 * S * C + 0.299;\n"
     "            double theta33 = theta33t + (1.283 * theta33t * theta33t - 0.374 * theta33t - 0.015);\n"
     "            double theta1500t = -0.024 * S + 0.487 * C + 0.006 * OM\n"
     "                              + 0.005 * S * OM - 0.013 * C * OM\n"
     "                              + 0.068 * S * C + 0.031;\n"
     "            double theta1500 = theta1500t + (0.14 * theta1500t - 0.02);\n"
     "            return Math.Max(0.0, theta33 - theta1500) * 1000.0;\n"
     "        }\n\n"
     "        // Cumulative plant-available water [mm] at depths 0, step, 2 step ... root_depth_max_m,\n"
     "        // layers taken top (index 0) to bottom. Below the soil the value stays constant.\n"
     "        void write_treed_paw_profile(string outputPath, Dictionary<string, string> cfg)\n"
     "        {\n"
     "            double step = cfg_double(cfg, \"root_depth_search_step_m\", 0.05);\n"
     "            double zmax = cfg_double(cfg, \"root_depth_max_m\", 3.0);\n"
     "            int K = (int)Math.Round(zmax / step);\n"
     "            using (StreamWriter sw = new StreamWriter(outputPath, false))\n"
     "            {\n"
     "                sw.WriteLine(\"# step_m=\" + step.ToString(\"R\", CultureInfo.InvariantCulture) + \" nodes=\" + (K + 1));\n"
     "                for (int r = 0; r < nr; r++)\n"
     "                {\n"
     "                    for (int c = 0; c < nc; c++)\n"
     "                    {\n"
     "                        if (dtm[r, c] == nodata_value) continue;\n"
     "                        double[] cum = new double[K + 1];\n"
     "                        int k = 1; double top = 0.0, accum = 0.0;\n"
     "                        for (int lay = 0; lay < max_soil_layers; lay++)\n"
     "                        {\n"
     "                            double h = layerthickness_m[r, c, lay];\n"
     "                            if (h <= 0) continue;\n"
     "                            double dens = treed_paw_density_mm_per_m(r, c, lay);\n"
     "                            double bottom = top + h;\n"
     "                            while (k <= K && k * step <= bottom + 1e-12)\n"
     "                            {\n"
     "                                cum[k] = accum + dens * (k * step - top);\n"
     "                                k++;\n"
     "                            }\n"
     "                            accum += dens * h; top = bottom;\n"
     "                        }\n"
     "                        while (k <= K) { cum[k] = accum; k++; }\n"
     "                        System.Text.StringBuilder line = new System.Text.StringBuilder();\n"
     "                        line.Append(r.ToString(CultureInfo.InvariantCulture)).Append(',').Append(c.ToString(CultureInfo.InvariantCulture));\n"
     "                        for (int j = 0; j <= K; j++) line.Append(',').Append(cum[j].ToString(\"R\", CultureInfo.InvariantCulture));\n"
     "                        sw.WriteLine(line.ToString());\n"
     "                    }\n"
     "                }\n"
     "            }\n"
     "        }\n\n"
     "        void configure_treed_landslide_event(Dictionary<string, string> cfg)\n", 1),
    ("                write_treed_rain_event_stats(Path.Combine(inputDir, \"rain_event_stats_monthly.csv\"), cfg);\n",
     "                write_treed_rain_event_stats(Path.Combine(inputDir, \"rain_event_stats_monthly.csv\"), cfg);\n"
     "            if (cfg_string(cfg, \"root_depth_paw_profile\", \"uniform\").ToLowerInvariant() == \"layered\")\n"
     "                write_treed_paw_profile(Path.Combine(inputDir, \"paw_profile_mm.csv\"), cfg);\n", 1),
])
print(MARK + "_APPLIED_DEFAULT_UNIFORM")
