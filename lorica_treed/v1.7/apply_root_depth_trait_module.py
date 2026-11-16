#!/usr/bin/env python3
"""Gounsa v1.7: install the EXPERIMENTAL root-depth trait module.

Opt-in (root_depth_mode=off by default). With the default every TREED and
LORICA code path evaluates exactly as before. Upstream TREED physiology is not
removed; the module adds branches guarded by rootdepth_on(par).

Usage: apply_root_depth_trait_module.py <work_dir>
"""
import pathlib
import shutil
import sys

work = pathlib.Path(sys.argv[1])
here = pathlib.Path(__file__).resolve().parent
MARK = "GOUNSA_V17_ROOT_DEPTH_TRAIT"


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
shutil.copyfile(here / "TREED_rootdepth.jl", src / "TREED_rootdepth.jl")

patch(src / "TREED.jl", [
    ('include("./TREED_model_functions.jl")',
     '# ' + MARK + '\ninclude("./TREED_rootdepth.jl")\ninclude("./TREED_model_functions.jl")', 1),
])

patch(src / "TREED_pars.jl", [
    ("    paw_release_days = 365.0,\n",
     "    paw_release_days = 365.0,\n\n"
     "    # " + MARK + " (experimental, opt-in)\n"
     "    root_depth_mode = \"off\",\n"
     "    root_depth_initial_m = 0.5,\n"
     "    root_depth_min_m = 0.05,\n"
     "    root_depth_max_m = 3.0,\n"
     "    root_depth_cost_gC_m2_yr_per_m = 146.1,\n"
     "    root_depth_search_step_m = 0.05,\n", 1),
])

patch(src / "TREED_physiological_functions.jl", [
    # water supply
    ("  water_stressed = findall(Esupply .< Edemand)\n",
     "  # " + MARK + ": storage-limited supply replaces the line-198 supply\n"
     "  if rootdepth_on(par)\n"
     "    Esupply = rootdepth_esupply(env, par, Edemand, Emax)\n"
     "  end\n"
     "  water_stressed = findall(Esupply .< Edemand)\n", 1),
    # root-depth respiration cost (already per unit ground area)
    ("  C_turnover_total =  C_turnover_total ./ tr.CA\n",
     "  C_turnover_total =  C_turnover_total ./ tr.CA\n"
     "  if rootdepth_on(par)\n"
     "    C_turnover_total = C_turnover_total .+ rootdepth_cost(env, par)\n"
     "  end\n", 1),
    # optimum depth by deterministic search after the unchanged 3-D ECA
    ("    # Seasonality optimization \n    if (sum(env.tair_monthly .<= par.temp_threshold_growing_season) >= 3. && a_ll_optimized .< 1.)\n",
     "    z_r_optimized = rootdepth_on(par) ? rootdepth_grid_opt(env, par, a_ll_optimized, C_leaf_optimized, H_optimized) : NaN\n"
     "    # Seasonality optimization \n    if (sum(env.tair_monthly .<= par.temp_threshold_growing_season) >= 3. && a_ll_optimized .< 1.)\n", 1),
    ("      H_optimized = H_optimized, \n      seasonality_optimized = seasonality_optimized\n    )\n",
     "      H_optimized = H_optimized, \n      seasonality_optimized = seasonality_optimized,\n"
     "      z_r_optimized = z_r_optimized\n    )\n", 1),
])

patch(src / "TREED_model_functions.jl", [
    ("soildepth_m = climate.soildepth_m[i, j]",
     "soildepth_m = climate.soildepth_m[i, j], rd = rootdepth_cell(i, j)", 4),
    ("                traits_optimized.Pave_optim[i, j] = env.precip_annual\n",
     "                traits_optimized.Pave_optim[i, j] = env.precip_annual\n"
     "                rootdepth_store_opt!(i, j, optimized_traits) # " + MARK + "\n", 1),
])

patch(src / "TREEDlocalstep.jl", [
    ("                          evorate, dispersal, outputdir, traitdir, timestep,\n",
     "                          evorate, dispersal, outputdir, traitdir, timestep,\n"
     "                          rain_alpha_mm=nothing, rain_lambda_per_day=nothing,\n", 1),
    ("    traits_optimized = run_TREED_optimization(traits_start, climate, pars2)\n",
     "    # " + MARK + "\n"
     "    rootdepth_begin!(pars2, climate, traitdir; alpha_mm=rain_alpha_mm, lambda_per_day=rain_lambda_per_day)\n"
     "    traits_optimized = run_TREED_optimization(traits_start, climate, pars2)\n"
     "    rootdepth_evolve!(evorate)\n", 1),
    ("    @save joinpath(traitdir, \"traits_restart.jld2\") traits_end\n",
     "    @save joinpath(traitdir, \"traits_restart.jld2\") traits_end\n"
     "    rootdepth_save!(traitdir)\n", 1),
])

# ---- coupling driver --------------------------------------------------------
patch(work / "coupling" / "treed_lorica_driver.jl", [
    ("paw_days=parse(Float64,get(conf,\"paw_release_days\",\"365.0\"))\n",
     "paw_days=parse(Float64,get(conf,\"paw_release_days\",\"365.0\"))\n"
     "# " + MARK + "\n"
     "rd_mode=lowercase(get(conf,\"root_depth_mode\",\"off\"))\n"
     "rd_alpha=nothing; rd_lambda=nothing\n"
     "if rd_mode == \"milly_stochastic\"\n"
     "    statfile = joinpath(input_dir, \"rain_event_stats_monthly.csv\")\n"
     "    isfile(statfile) || error(\"Missing $statfile\")\n"
     "    st = readdlm(statfile, ',', skipstart=1)\n"
     "    size(st,1) == 12 || error(\"rain_event_stats_monthly.csv must contain 12 months\")\n"
     "    rd_alpha = Float64.(st[:,3]); rd_lambda = Float64.(st[:,4])\n"
     "end\n", 1),
    ("    paw_release_days=paw_days)\n",
     "    paw_release_days=paw_days,\n"
     "    root_depth_mode=rd_mode,\n"
     "    root_depth_initial_m=parse(Float64,get(conf,\"root_depth_initial_m\",\"0.5\")),\n"
     "    root_depth_min_m=parse(Float64,get(conf,\"root_depth_min_m\",\"0.05\")),\n"
     "    root_depth_max_m=parse(Float64,get(conf,\"root_depth_max_m\",\"3.0\")),\n"
     "    root_depth_cost_gC_m2_yr_per_m=parse(Float64,get(conf,\"root_depth_cost_gC_m2_yr_per_m\",\"146.1\")),\n"
     "    root_depth_search_step_m=parse(Float64,get(conf,\"root_depth_search_step_m\",\"0.05\")),\n"
     "    rain_alpha_mm=rd_alpha,rain_lambda_per_day=rd_lambda)\n", 1),
    ("println(\"TREED-LORICA coupling step complete for year $year\")",
     "if TREED.ROOTDEPTH[] !== nothing\n"
     "    rdst = TREED.ROOTDEPTH[]\n"
     "    zr = permutedims(rdst[:z_r]); zo = permutedims(rdst[:z_opt]); z0 = permutedims(rdst[:z_start])\n"
     "    write_esri_ascii(joinpath(output_dir,\"treed_root_depth_m.asc\"), zr, hdr)\n"
     "    write_esri_ascii(joinpath(output_dir,\"treed_root_depth_optimum_m.asc\"), zo, hdr)\n"
     "    write_esri_ascii(joinpath(output_dir,\"treed_root_depth_start_m.asc\"), z0, hdr)\n"
     "    write_esri_ascii(joinpath(output_dir,\"treed_root_depth_effective_m.asc\"), min.(zr, max.(soildepth, 0.0)), hdr)\n"
     "end\n"
     "println(\"TREED-LORICA coupling step complete for year $year\")", 1),
])

# ---- LORICA: export monthly wet-day statistics ------------------------------
cs = work / "LORICA" / "Functions" / "treed_coupling.cs"
patch(cs, [
    ("        void configure_treed_landslide_event(Dictionary<string, string> cfg)\n",
     "        // " + MARK + ": monthly wet-day statistics of the exact LORICA daily\n"
     "        // rainfall series (read-only). alpha = mean depth on wet days [mm],\n"
     "        // lambda = wet days per day. Wet day: P >= threshold (default 1 mm).\n"
     "        void write_treed_rain_event_stats(string outputPath, Dictionary<string, string> cfg)\n"
     "        {\n"
     "            double thr = cfg_double(cfg, \"root_depth_wet_day_threshold_mm\", 1.0);\n"
     "            using (StreamWriter sw = new StreamWriter(outputPath, false))\n"
     "            {\n"
     "                sw.WriteLine(\"month,wet_days,alpha_mm,lambda_per_day,precip_mm_month,wet_day_precip_mm\");\n"
     "                int day0 = 0;\n"
     "                for (int mo = 0; mo < 12; mo++)\n"
     "                {\n"
     "                    int wet = 0; double wetsum = 0.0, psum = 0.0;\n"
     "                    for (int d = 0; d < month[mo]; d++)\n"
     "                    {\n"
     "                        double pmm = Py[day0 + d] * 1000.0;\n"
     "                        psum += pmm;\n"
     "                        if (pmm >= thr) { wet++; wetsum += pmm; }\n"
     "                    }\n"
     "                    double alpha = wet > 0 ? wetsum / wet : 0.0;\n"
     "                    double lambda = (double)wet / month[mo];\n"
     "                    sw.WriteLine(String.Format(CultureInfo.InvariantCulture,\n"
     "                        \"{0},{1},{2:R},{3:R},{4:R},{5:R}\", mo + 1, wet, alpha, lambda, psum, wetsum));\n"
     "                    day0 += month[mo];\n"
     "                }\n"
     "            }\n"
     "        }\n\n"
     "        void configure_treed_landslide_event(Dictionary<string, string> cfg)\n", 1),
    ("            write_treed_same_year_monthly_climate(Path.Combine(inputDir, \"treed_climate_monthly.csv\"), cfg, couplingDir);\n",
     "            write_treed_same_year_monthly_climate(Path.Combine(inputDir, \"treed_climate_monthly.csv\"), cfg, couplingDir);\n"
     "            if (cfg_string(cfg, \"root_depth_mode\", \"off\").ToLowerInvariant() != \"off\")\n"
     "                write_treed_rain_event_stats(Path.Combine(inputDir, \"rain_event_stats_monthly.csv\"), cfg);\n", 1),
])
print(MARK + "_APPLIED_DEFAULT_OFF")
