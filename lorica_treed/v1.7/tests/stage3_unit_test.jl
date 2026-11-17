# v1.7 stage 3 unit tests: layered plant-available-water profile in the root-depth module.
# usage: julia --project=<TREED dir> stage3_unit_test.jl <TREED dir>
using Test, Statistics
treed = abspath(ARGS[1])
include(joinpath(treed, "src", "TREED.jl"))
using .TREED
const T2 = TREED

@testset "profile interpolation" begin
    cum = [0.0, 10.0, 30.0, 35.0]            # nodes at 0, 0.1, 0.2, 0.3 m
    @test T2.rootdepth_profile_storage_mm(cum, 0.1, 0.0) == 0.0
    @test T2.rootdepth_profile_storage_mm(cum, 0.1, 0.05) ≈ 5.0
    @test T2.rootdepth_profile_storage_mm(cum, 0.1, 0.15) ≈ 20.0
    @test T2.rootdepth_profile_storage_mm(cum, 0.1, 0.3) ≈ 35.0
    @test T2.rootdepth_profile_storage_mm(cum, 0.1, 5.0) ≈ 35.0   # constant below the last node
    @test T2.rootdepth_profile_storage_mm([0.0], 0.1, 0.2) == 0.0  # degenerate profile
end

@testset "storage: uniform fallback and layered" begin
    base = (soildepth_m = 1.0, paw_mm = 100.0)
    env_u = merge(base, (rd = (z_r = 0.5, alpha_mm = zeros(12), lambda_per_day = zeros(12)),))
    @test T2.rootdepth_storage_mm(0.5, env_u) ≈ 50.0                 # legacy uniform formula
    @test T2.rootdepth_storage_mm(2.0, env_u) ≈ 100.0                # clipped at the soil depth
    cum_uniform = [100.0 * 0.05 * k for k in 0:20]                    # 100 mm per m, 1 m deep
    env_l = merge(base, (rd = (z_r = 0.5, alpha_mm = zeros(12), lambda_per_day = zeros(12),
                               paw_cum = cum_uniform, paw_step_m = 0.05),))
    for z in (0.05, 0.2, 0.5, 0.77, 1.0, 1.7)
        @test T2.rootdepth_storage_mm(z, env_l) ≈ T2.rootdepth_storage_mm(z, env_u) atol = 1e-9
    end
    # top-heavy profile: 60 mm in the first 0.2 m, 40 mm in the remaining 0.8 m
    cum_top = [k <= 4 ? 300.0 * 0.05 * k : 60.0 + 50.0 * 0.05 * (k - 4) for k in 0:20]
    env_t = merge(base, (rd = (z_r = 0.5, alpha_mm = zeros(12), lambda_per_day = zeros(12),
                               paw_cum = cum_top, paw_step_m = 0.05),))
    @test T2.rootdepth_storage_mm(0.2, env_t) ≈ 60.0
    @test T2.rootdepth_storage_mm(0.2, env_t) > T2.rootdepth_storage_mm(0.2, env_u)
    @test T2.rootdepth_storage_mm(1.0, env_t) ≈ 100.0 atol = 1e-9     # same total capacity
    # soil depth clips z_eff before the profile is read
    env_c = merge((soildepth_m = 0.3, paw_mm = 60.0), (rd = (z_r = 1.0, alpha_mm = zeros(12), lambda_per_day = zeros(12),
                               paw_cum = cum_top, paw_step_m = 0.05),))
    @test T2.rootdepth_storage_mm(1.0, env_c) ≈ T2.rootdepth_profile_storage_mm(cum_top, 0.05, 0.3)
    # no soil: no storage, whichever source
    env_0 = merge((soildepth_m = 0.0, paw_mm = 0.0), (rd = env_t.rd,))
    @test T2.rootdepth_storage_mm(0.5, env_0) == 0.0
end

@testset "state: profile handed to the cell tuple" begin
    nx = ny = 3
    par = merge(T2.pars, (root_depth_mode = "bucket_monthly", root_allocation_mode = "fixed_original"))
    climate = (topo = zeros(nx, ny),)
    prof = [10.0 * k + i + j for i in 1:nx, j in 1:ny, k in 0:4]
    T2.rootdepth_begin!(par, climate, mktempdir(); paw_profile = prof, paw_profile_step_m = 0.1)
    c = T2.rootdepth_cell(2, 3)
    @test c.paw_cum == prof[2, 3, :] && c.paw_step_m == 0.1
    @test_throws ErrorException T2.rootdepth_begin!(par, climate, mktempdir(); paw_profile = zeros(2, 2, 5), paw_profile_step_m = 0.1)
    @test_throws ErrorException T2.rootdepth_begin!(par, climate, mktempdir(); paw_profile = prof, paw_profile_step_m = 0.0)
    T2.rootdepth_begin!(par, climate, mktempdir())
    @test T2.rootdepth_cell(1, 1).paw_cum === nothing
end
println("STAGE3_UNIT_TESTS_DONE")
