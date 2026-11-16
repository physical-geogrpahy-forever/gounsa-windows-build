# v1.7 root-depth module, single-cell tests. SYNTHETIC Korea-like climate, not field data.
using Optimization, OptimizationMetaheuristics, Metaheuristics, Statistics, JLD2, Printf
src = ARGS[1]; what = ARGS[2]
isfile(joinpath(src, "TREED_rootdepth.jl")) && include(joinpath(src, "TREED_rootdepth.jl"))
include(joinpath(src, "TREED_physiological_functions.jl"))
include(joinpath(src, "TREED_pars.jl"))
T = [-2.5,0,5.5,12.5,18,22,25,25.5,20,13,6,-0.5]
Pmm = [20,25,40,70,80,130,250,230,130,40,35,18.0]
wet0 = [4,4,6,7,8,9,14,12,8,5,6,4.0]
days = [31,28,31,30,31,30,31,31,30,31,30,31.0]
rsds = [95,125,160,200,220,210,180,185,160,135,100,85.0]
doy = [15,46,73,104,134,166,196,227,259,288,319,349]
dl = [24/pi*acos(clamp(-tand(36.4)*tand(23.44*sind(360/365*(d-81))), -1, 1)) for d in doy]
rss = rsds .* 0.85 .* 86400e-6
rls = (0.2 .+ 0.8*0.5) .* (107 .- T) .* 86400e-6 .* -1
mkenv(zs; rd=nothing) = (precip_monthly = Pmm ./ 1000 ./ days, tair_monthly = T, tair_annual = mean(T),
    rsds_monthly = rsds .* 86400e-6, rss_monthly = rss, rls_monthly = rls, daylength = dl, CO2_ppm = 420.0,
    precip_annual = mean(Pmm ./ 1000 ./ days), paw_mm = 0.12*zs*1000, soildepth_m = zs, rd = rd)
base = merge(pars, (root_allocation_mode = "fixed_original", soil_water_coupling_strength = 1.0))
opt(par, env, seed) = trait_optimizer(env=env, par=par, trait_optimization_function=trait_optimization_function, iters=20, seed=seed)
if what == "off"
    for zs in (0.0, 0.3, 1.0), seed in (1, 2)
        o = opt(base, mkenv(zs), seed)
        println(zs, " ", seed, " ", repr(o.H_optimized), " ", repr(o.a_ll_optimized), " ", repr(o.C_leaf_optimized))
    end
elseif what == "unit"
    # Guswa (2008) Eq. 12 limits
    @assert rootdepth_milly_T(0.0, 10.0, 0.3, 4.0) == 0.0
    @assert isapprox(rootdepth_milly_T(1e6, 10.0, 0.3, 4.0), 3.0; rtol=1e-9)      # W<1, huge storage: all rain
    @assert isapprox(rootdepth_milly_T(1e6, 10.0, 0.6, 4.0), 4.0; rtol=1e-9)      # W>1, huge storage: Tpot
    @assert isapprox(rootdepth_milly_T(5.0, 10.0, 0.001, 1000.0), 10*0.001*(1-exp(-0.5)); rtol=1e-3) # W->0
    @assert isapprox(rootdepth_milly_T(36.0, 10.0, 8/31, 3.5)/3.5, 0.63; atol=0.01)   # design-doc table
    zs = [rootdepth_milly_T(s, 10.0, 0.26, 3.5) for s in 0:5:300]; @assert all(diff(zs) .>= -1e-12)
    # Nylsvley check of Guswa Table 1: W = 0.36 with lambda = 0.167*exp(-5/15), alpha 15, Tpot 5.7*? -> printed only
    println("Guswa Table 1 lambda_eff*alpha = ", 0.167*exp(-5/15)*15, " mm/d")
    println("UNIT_OK")
else
    cost = parse(Float64, ARGS[3]); conc = ARGS[4] == "concentrated"
    wet = conc ? max.(1.0, round.(wet0 ./ 3)) : wet0
    par = merge(base, (root_depth_mode = what, root_depth_cost_gC_m2_yr_per_m = cost))
    @printf("mode=%s cost=%.1f rain=%s\n", what, cost, ARGS[4])
    for zs in (0.0, 0.05, 0.1, 0.2, 0.3, 0.6, 1.0, 2.0)
        z = 0.5; hist = Float64[]; H = Float64[]; zo = Float64[]
        for yr in 1:30
            env = mkenv(zs; rd = (z_r = z, alpha_mm = Pmm ./ wet, lambda_per_day = wet ./ days))
            o = opt(par, env, yr)
            z += 0.1 * (o.z_r_optimized - z); push!(hist, z); push!(H, o.H_optimized); push!(zo, o.z_r_optimized)
        end
        @printf("soil %.2f | z_opt mean %.2f sd %.2f | z_r yr1 %.2f yr10 %.2f yr30 %.2f | H mean(yr21-30) %.1f\n",
            zs, mean(zo[11:30]), std(zo[11:30]), hist[1], hist[10], hist[30], mean(H[21:30]))
    end
end
