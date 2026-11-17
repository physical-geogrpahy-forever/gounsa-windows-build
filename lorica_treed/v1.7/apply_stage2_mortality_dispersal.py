#!/usr/bin/env python3
"""Gounsa v1.7 stage 2: install the EXPERIMENTAL landslide-mortality,
local-dispersal and stand-development module.

Run AFTER apply_root_depth_trait_module.py (the new code reuses the root-depth
state when it is on, and does nothing with it when it is off).

mortality_mode=off (default): every TREED and LORICA code path evaluates
exactly as before. LORICA gets one read-only accumulator of landslide erosion
(no landslide algorithm is changed); TREED gets guarded calls.

Usage: apply_stage2_mortality_dispersal.py <work_dir>
"""
import pathlib
import shutil
import sys

work = pathlib.Path(sys.argv[1])
here = pathlib.Path(__file__).resolve().parent
MARK = "GOUNSA_V17_STAGE2_MORTALITY"


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
if "GOUNSA_V17_ROOT_DEPTH_TRAIT" not in (src / "TREED.jl").read_text(encoding="utf-8"):
    raise SystemExit("apply_root_depth_trait_module.py must be applied first")
shutil.copyfile(here / "TREED_stage2.jl", src / "TREED_stage2.jl")

patch(src / "TREED.jl", [
    ('include("./TREED_rootdepth.jl")',
     'include("./TREED_rootdepth.jl")\n# ' + MARK + '\ninclude("./TREED_stage2.jl")', 1),
])

patch(src / "TREED_pars.jl", [
    ("    root_depth_search_step_m = 0.05,\n",
     "    root_depth_search_step_m = 0.05,\n\n"
     "    # " + MARK + " (experimental, opt-in)\n"
     "    mortality_mode = \"off\",\n"
     "    dispersal_m = 10.0,\n"
     "    growth_cap_m_yr = 0.3,\n"
     "    seed_source_min_phi = 1.0,\n", 1),
])

patch(src / "TREEDlocalstep.jl", [
    ("                          rain_alpha_mm=nothing, rain_lambda_per_day=nothing,\n",
     "                          rain_alpha_mm=nothing, rain_lambda_per_day=nothing,\n"
     "                          landslide_mask=nothing, cellsize_m=NaN,\n", 1),
    ("    rootdepth_begin!(pars2, climate, traitdir; alpha_mm=rain_alpha_mm, lambda_per_day=rain_lambda_per_day)\n",
     "    rootdepth_begin!(pars2, climate, traitdir; alpha_mm=rain_alpha_mm, lambda_per_day=rain_lambda_per_day)\n"
     "    stage2_begin!(pars2, climate, traitdir, landslide_mask) # " + MARK + "\n", 1),
    ("                                   traits_optimized, climate, dispersal, pars2)\n",
     "                                   traits_optimized, climate, dispersal, pars2)\n"
     "    stage2_recolonize!(traits_end, traits_evolved, traits_optimized, climate, pars2, cellsize_m)\n", 1),
    ("    rootdepth_save!(traitdir)\n",
     "    rootdepth_save!(traitdir)\n"
     "    stage2_save!(traitdir)\n", 1),
    ("    vegetation_output = run_TREED_final_distribution(traits_end, climate, pars2)\n",
     "    vegetation_output = run_TREED_final_distribution(traits_end, climate, pars2)\n"
     "    stage2_apply_outputs!(vegetation_output, traits_end, pars2)\n", 1),
])

# ---- coupling driver --------------------------------------------------------
patch(work / "coupling" / "treed_lorica_driver.jl", [
    ("rd_mode=lowercase(get(conf,\"root_depth_mode\",\"off\"))\n",
     "# " + MARK + "\n"
     "mort_mode=lowercase(get(conf,\"mortality_mode\",\"off\"))\n"
     "ls_mask=nothing\n"
     "if mort_mode != \"off\"\n"
     "    mfile = joinpath(input_dir, \"landslide_disturbed_mask.asc\")\n"
     "    isfile(mfile) || error(\"Missing $mfile\")\n"
     "    mraw,_ = read_esri_ascii(mfile)\n"
     "    size(mraw) == size(dtm) || error(\"landslide mask grid mismatch\")\n"
     "    ls_mask = permutedims(Array{Bool}(coalesce.(mraw .> 0.5, false)))\n"
     "end\n"
     "rd_mode=lowercase(get(conf,\"root_depth_mode\",\"off\"))\n", 1),
    ("    rain_alpha_mm=rd_alpha,rain_lambda_per_day=rd_lambda)\n",
     "    rain_alpha_mm=rd_alpha,rain_lambda_per_day=rd_lambda,\n"
     "    mortality_mode=mort_mode,\n"
     "    dispersal_m=parse(Float64,get(conf,\"dispersal_m\",\"10.0\")),\n"
     "    growth_cap_m_yr=parse(Float64,get(conf,\"growth_cap_m_yr\",\"0.3\")),\n"
     "    seed_source_min_phi=parse(Float64,get(conf,\"seed_source_min_phi\",\"1.0\")),\n"
     "    landslide_mask=ls_mask,cellsize_m=cs)\n", 1),
    ("println(\"TREED-LORICA coupling step complete for year $year\")",
     "if TREED.STAGE2[] !== nothing\n"
     "    s2 = TREED.STAGE2[]\n"
     "    write_esri_ascii(joinpath(output_dir,\"treed_stage2_occupied.asc\"), permutedims(Float64.(s2[:occ])), hdr)\n"
     "    write_esri_ascii(joinpath(output_dir,\"treed_stage2_phi.asc\"), permutedims(Float64.(s2[:phi])), hdr)\n"
     "    write_esri_ascii(joinpath(output_dir,\"treed_stage2_age_yr.asc\"), permutedims(Float64.(min.(s2[:age], 9999.0))), hdr)\n"
     "    open(joinpath(output_dir,\"treed_stage2_summary.csv\"),\"w\") do io\n"
     "        println(io,\"year,killed_cells,recolonised_cells,occupied_cells\")\n"
     "        println(io,\"$year,$(s2[:killed]),$(s2[:recolonised]),$(count(s2[:occ]))\")\n"
     "    end\n"
     "end\n"
     "println(\"TREED-LORICA coupling step complete for year $year\")", 1),
])

# ---- LORICA: read-only accumulator and mask export ---------------------------
patch(work / "LORICA" / "Functions" / "geomorph.cs", [
    ("                            dtm[row, col] += ero_slid_m[row, col] + sed_slid_m[row, col];\n"
     "                            dtmchange_m[row, col] += ero_slid_m[row, col] + sed_slid_m[row, col];\n",
     "                            dtm[row, col] += ero_slid_m[row, col] + sed_slid_m[row, col];\n"
     "                            dtmchange_m[row, col] += ero_slid_m[row, col] + sed_slid_m[row, col];\n"
     "                            if (ero_slid_m[row, col] < 0.0) gounsa_note_landslide_erosion(row, col, -ero_slid_m[row, col]); // " + MARK + " (read-only)\n", 1),
])

patch(work / "LORICA" / "Functions" / "treed_coupling.cs", [
    ("        public int gounsa_ls_capture_count = 0;\n",
     "        public int gounsa_ls_capture_count = 0;\n"
     "        // " + MARK + ": landslide erosion [m] summed since the last TREED step.\n"
     "        public double[,] gounsa_ls_pending_erosion_m = null;\n"
     "        void gounsa_note_landslide_erosion(int r, int c, double meters)\n"
     "        {\n"
     "            if (gounsa_ls_pending_erosion_m == null) gounsa_ls_pending_erosion_m = new double[nr, nc];\n"
     "            gounsa_ls_pending_erosion_m[r, c] += meters;\n"
     "        }\n", 1),
    ("        void configure_treed_landslide_event(Dictionary<string, string> cfg)\n",
     "        // " + MARK + ": 1 where this year's landslide removed soil (cell lost\n"
     "        // more than max(threshold, 1e-9) m), 0 elsewhere, nodata outside the DTM.\n"
     "        void write_treed_landslide_mask(string outputPath, Dictionary<string, string> cfg)\n"
     "        {\n"
     "            double thr = Math.Max(cfg_double(cfg, \"landslide_mortality_min_erosion_m\", 0.0), 1e-9);\n"
     "            double[,] mask = new double[nr, nc];\n"
     "            for (int r = 0; r < nr; r++)\n"
     "            {\n"
     "                for (int c = 0; c < nc; c++)\n"
     "                {\n"
     "                    if (dtm[r, c] == nodata_value) { mask[r, c] = nodata_value; continue; }\n"
     "                    mask[r, c] = (gounsa_ls_pending_erosion_m != null && gounsa_ls_pending_erosion_m[r, c] > thr) ? 1.0 : 0.0;\n"
     "                }\n"
     "            }\n"
     "            out_double(outputPath, mask);\n"
     "            gounsa_ls_pending_erosion_m = new double[nr, nc];\n"
     "        }\n\n"
     "        void configure_treed_landslide_event(Dictionary<string, string> cfg)\n", 1),
    ("            File.Copy(cfgFile, Path.Combine(exchangeRoot, \"TREED_coupling.cfg\"), true);\n",
     "            if (cfg_string(cfg, \"mortality_mode\", \"off\").ToLowerInvariant() != \"off\")\n"
     "                write_treed_landslide_mask(Path.Combine(inputDir, \"landslide_disturbed_mask.asc\"), cfg);\n"
     "            File.Copy(cfgFile, Path.Combine(exchangeRoot, \"TREED_coupling.cfg\"), true);\n", 1),
])
print(MARK + "_APPLIED_DEFAULT_OFF")
