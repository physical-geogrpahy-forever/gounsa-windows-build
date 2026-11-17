# v1.7 stage 2 unit tests: landslide mortality, local-grid recolonisation, development ramp.
# SYNTHETIC climate (Korea-like monsoon shape), not Gounsa field data.
# usage: julia --project=<TREED dir> stage2_unit_test.jl <TREED dir>
using Test, Statistics, Printf, JLD2, Rasters
treed = ARGS[1]
include(joinpath(treed, "src", "TREED.jl"))
using .TREED
const T2 = TREED

nx = ny = 5
par_on(; disp = 10.0, g = 0.3, seed = 1.0) = merge(T2.pars, (root_allocation_mode = "fixed_original",
    soil_water_coupling_strength = 1.0, mortality_mode = "landslide_scar",
    dispersal_m = disp, growth_cap_m_yr = g, seed_source_min_phi = seed))

# ---------------------------------------------------------------- pure helpers
@testset "window and phi" begin
    @test T2.stage2_window(3, 3, 1, 5, 5) == (2:4, 2:4)
    @test T2.stage2_window(1, 1, 2, 5, 5) == (1:3, 1:3)     # clipped, no wrap-around
    @test T2.stage2_window(5, 5, 2, 5, 5) == (3:5, 3:5)
    @test T2.stage2_phi_value(false, 1.0e9, 10.0, 0.3) == 0.0
    @test T2.stage2_phi_value(true, 1.0e9, 10.0, 0.3) == 1.0
    @test T2.stage2_phi_value(true, 10.0, 9.9, 0.3) ≈ 0.3 * 10 / 9.9
    @test T2.stage2_phi_value(true, 100.0, 9.9, 0.3) == 1.0  # capped at 1
    @test T2.stage2_phi_value(true, 5.0, 9.9, 0.0) == 1.0    # growth_cap 0: no ramp
    @test T2.stage2_phi_value(true, 0.0, 9.9, 0.3) == 0.0
end

# ---------------------------------------------------------------- off mode
@testset "off mode does nothing" begin
    climate = (topo = zeros(nx, ny),)
    T2.stage2_begin!(merge(T2.pars, (mortality_mode = "off",)), climate, mktempdir(), nothing)
    @test T2.STAGE2[] === nothing
    veg = (FPC = fill(0.6, nx, ny), H = fill(10.0, nx, ny))
    before = copy(veg.FPC)
    T2.stage2_apply_outputs!(veg, (H = fill(10.0, nx, ny),), merge(T2.pars, (mortality_mode = "off",)))
    @test veg.FPC == before
    # default parameter set has the module off
    @test T2.stage2_on(T2.pars) == false
end

# ---------------------------------------------------------------- state, mask, restart
@testset "mask, ageing and restart" begin
    dir = mktempdir()
    climate = (topo = zeros(nx, ny),)
    mask = falses(nx, ny); mask[3, 3] = true; mask[1, 5] = true
    T2.stage2_begin!(par_on(), climate, dir, mask)
    st = T2.STAGE2[]
    @test st[:killed] == 2
    @test !st[:occ][3, 3] && !st[:occ][1, 5] && count(st[:occ]) == nx * ny - 2
    @test st[:age][3, 3] == 0.0 && st[:age][2, 2] == 1.0e9
    T2.stage2_save!(dir)
    # next year, no new mask: dead cells stay empty (no ageing), living cells unchanged
    T2.stage2_begin!(par_on(), climate, dir, falses(nx, ny))
    st = T2.STAGE2[]
    @test st[:killed] == 0 && !st[:occ][3, 3] && st[:age][3, 3] == 0.0
    @test st[:age][2, 2] == 1.0e9
    # an occupied young cell ages by one year
    st[:occ][3, 3] = true; st[:age][3, 3] = 4.0
    T2.stage2_save!(dir)
    T2.stage2_begin!(par_on(), climate, dir, nothing)
    @test T2.STAGE2[][:age][3, 3] == 5.0
    # a mask that kills an already-empty cell does not count it twice
    T2.stage2_begin!(par_on(), climate, mktempdir(), trues(nx, ny))
    @test T2.STAGE2[][:killed] == nx * ny
    @test_throws ErrorException T2.stage2_begin!(par_on(), climate, mktempdir(), falses(3, 3))
end

# ---------------------------------------------------------------- output scaling
@testset "development factor scales outputs only where phi < 1" begin
    climate = (topo = zeros(nx, ny),)
    T2.stage2_begin!(par_on(), climate, mktempdir(), nothing)
    st = T2.STAGE2[]
    st[:age][2, 2] = 10.0                # young, H_eq = 10 -> phi = 0.3
    st[:occ][4, 4] = false; st[:age][4, 4] = 0.0   # empty
    st[:age][5, 5] = 100.0               # young by age but ramp already complete
    veg = (FPC = fill(0.6, nx, ny), LAI = fill(3.0, nx, ny), C_fineroot = fill(50.0, nx, ny),
           C_coarseroot = fill(80.0, nx, ny), CA = fill(12.0, nx, ny), NPP = fill(400.0, nx, ny),
           H = fill(10.0, nx, ny))
    traits_end = (H = fill(10.0, nx, ny),)
    T2.stage2_apply_outputs!(veg, traits_end, par_on(g = 0.3))
    @test veg.FPC[1, 1] == 0.6 && veg.LAI[1, 1] == 3.0           # mature: untouched
    @test veg.FPC[2, 2] ≈ 0.18 && veg.LAI[2, 2] ≈ 0.9 && veg.H[2, 2] ≈ 3.0
    @test veg.C_fineroot[2, 2] ≈ 15.0 && veg.C_coarseroot[2, 2] ≈ 24.0
    @test veg.CA[2, 2] == 12.0                                   # crown area is not scaled
    @test veg.FPC[4, 4] == 0.0 && veg.NPP[4, 4] == 0.0           # empty cell
    @test veg.FPC[5, 5] == 0.6                                   # ramp complete
    @test st[:age][5, 5] == 1.0e9                                # marked grown
    @test st[:phi][2, 2] ≈ 0.3 && st[:phi][1, 1] == 1.0 && st[:phi][4, 4] == 0.0
    # area-normalised root carbon (coupling quantity) scales with phi
    rootC = (veg.C_fineroot .+ veg.C_coarseroot) ./ veg.CA
    @test rootC[2, 2] ≈ 0.3 * rootC[1, 1]
end

# ---------------------------------------------------------------- recolonisation with real physiology
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.0]
Tc = [-2.5, 0, 5.5, 12.5, 18, 22, 25, 25.5, 20, 13, 6, -0.5]
Pmm = [20, 25, 40, 70, 80, 130, 250, 230, 130, 40, 35, 18.0]
xs = 1.0:nx; ys = Float64.(ny:-1:1)
mk3(f) = Raster(Float32[f(m) for i in 1:nx, j in 1:ny, m in 1:12], (X(xs), Y(ys), Ti(1:12)))
mk2(v) = Raster(fill(Float32(v), nx, ny), (X(xs), Y(ys)))
climate = T2.create_TREED_local_climate_input(mk3(m -> Tc[m] + 273.15),
    mk3(m -> Pmm[m] / 1000 / (days[m] * 86400)), mk3(m -> 0.5), mk3(m -> 150.0),
    mk2(100.0), mk2(100.0), mk2(1.0), 420.0, 36.4)

function env_at(i, j)
    return (precip_monthly = parent(climate.precip[i, j, :]), tair_monthly = parent(climate.tair[i, j, :]),
            tair_annual = mean(parent(climate.tair[i, j, :])), rsds_monthly = parent(climate.rsds[i, j, :]),
            rss_monthly = parent(climate.rss[i, j, :]), rls_monthly = parent(climate.rls[i, j, :]),
            daylength = parent(climate.daylength[i, j, :]), CO2_ppm = climate.CO2_ppm,
            precip_annual = mean(parent(climate.precip[i, j, :])), paw_mm = climate.paw_mm[i, j],
            soildepth_m = climate.soildepth_m[i, j], rd = nothing)
end

# find a trait set that is productive in this climate (the real model optimises it)
pars_t = par_on()
best = (H = 0.0, a_ll = 1.0, C_leaf = 500.0)
for a in (0.5, 1.0, 2.0, 5.0), c in (150.0, 300.0, 500.0, 800.0)
    tc = parent(climate.tair[3, 3, :]); pc = parent(climate.precip[3, 3, :])
    bt = (a_ll = a, C_leaf = c, seasonality = 1.0, r_s_r = 1.0, Tave_optim = mean(tc), Tmax_optim = maximum(tc),
          Tmin_optim = minimum(tc), Pave_optim = mean(pc))
    h = T2.stage2_height(env_at(3, 3), bt, pars_t)
    h > best.H && (global best = (H = h, a_ll = a, C_leaf = c))
end
@printf("productive trait set for the synthetic climate: H=%.2f a_ll=%.1f C_leaf=%.0f\n", best.H, best.a_ll, best.C_leaf)
@test best.H > 1.0

function make_traits()
    tr = T2.initialize_TREED_traits(climate)
    tr.a_ll .= best.a_ll; tr.C_leaf .= best.C_leaf; tr.seasonality .= 1.0
    tr.r_s_r .= 1.0; tr.H .= best.H
    return tr
end

# 2-D view for counting
occ_count() = count(T2.STAGE2[][:occ])

@testset "recolonisation only from occupied mature neighbours in the local window" begin
    tr_end = make_traits(); tr_ev = deepcopy(tr_end); tr_op = deepcopy(tr_end)
    # (a) two scars inside a living stand -> both are re-occupied from neighbours
    mask = falses(nx, ny); mask[3, 3] = true; mask[1, 5] = true
    T2.stage2_begin!(par_on(), climate, mktempdir(), mask)
    T2.stage2_recolonize!(tr_end, tr_ev, tr_op, climate, par_on(), 10.0)
    st = T2.STAGE2[]
    @test st[:recolonised] == 2 && occ_count() == nx * ny
    @test st[:age][3, 3] == 0.0 && tr_end.H[3, 3] ≈ best.H
    @test tr_end.a_ll[3, 3] == best.a_ll && tr_end.C_leaf[3, 3] == best.C_leaf

    # (b) only column 1 alive, radius 1: exactly one column is gained per pass, and a
    # freshly recolonised cell (phi < 1) is no seed source while seed_source_min_phi = 1
    dir = mktempdir()
    tr_end = make_traits(); tr_ev = deepcopy(tr_end); tr_op = deepcopy(tr_end)
    mask = trues(nx, ny); mask[1, :] .= false
    T2.stage2_begin!(par_on(), climate, dir, mask)
    T2.stage2_recolonize!(tr_end, tr_ev, tr_op, climate, par_on(), 10.0)
    st = T2.STAGE2[]
    @test all(st[:occ][1:2, :]) && !any(st[:occ][3:5, :])
    @test all(tr_end.H[3:5, :] .== 0) && all(tr_end.H[1:2, :] .> 0)  # empty cells report no height
    T2.stage2_apply_outputs!((FPC = fill(0.6, nx, ny),), tr_end, par_on())
    T2.stage2_save!(dir)
    T2.stage2_begin!(par_on(), climate, dir, nothing)
    tr_ev = deepcopy(tr_end); tr_op = deepcopy(tr_end)
    T2.stage2_recolonize!(tr_end, tr_ev, tr_op, climate, par_on(), 10.0)
    @test !any(T2.STAGE2[][:occ][3:5, :])                            # young cells are not sources
    # (c) same state, but young cells may seed (seed_source_min_phi = 0): column 3 follows
    T2.stage2_begin!(par_on(seed = 0.0), climate, dir, nothing)
    tr_ev = deepcopy(tr_end); tr_op = deepcopy(tr_end)
    T2.stage2_recolonize!(tr_end, tr_ev, tr_op, climate, par_on(seed = 0.0), 10.0)
    @test all(T2.STAGE2[][:occ][1:3, :]) && !any(T2.STAGE2[][:occ][4:5, :])

    # (d) dispersal_m = 0 -> no recolonisation at all
    tr_end = make_traits(); tr_ev = deepcopy(tr_end); tr_op = deepcopy(tr_end)
    mask = falses(nx, ny); mask[3, 3] = true
    T2.stage2_begin!(par_on(disp = 0.0), climate, mktempdir(), mask)
    T2.stage2_recolonize!(tr_end, tr_ev, tr_op, climate, par_on(disp = 0.0), 10.0)
    @test !T2.STAGE2[][:occ][3, 3] && T2.STAGE2[][:recolonised] == 0 && tr_end.H[3, 3] == 0

    # (e) radius 2 (dispersal 20 m on 10 m cells): two columns in one pass
    tr_end = make_traits(); tr_ev = deepcopy(tr_end); tr_op = deepcopy(tr_end)
    mask = trues(nx, ny); mask[1, :] .= false
    T2.stage2_begin!(par_on(disp = 20.0), climate, mktempdir(), mask)
    T2.stage2_recolonize!(tr_end, tr_ev, tr_op, climate, par_on(disp = 20.0), 10.0)
    @test all(T2.STAGE2[][:occ][1:3, :]) && !any(T2.STAGE2[][:occ][4:5, :])
end
println("STAGE2_UNIT_TESTS_DONE")
