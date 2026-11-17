###########################################################
# Gounsa v1.7 stage 2 (EXPERIMENTAL, opt-in): landslide mortality,
# local-grid recolonisation, stand-development ramp.
#
# mortality_mode = "off" (default): no function in this file changes anything.
# mortality_mode = "landslide_scar": cells listed in the LORICA landslide mask
#   (erosion > threshold) lose all vegetation. They are re-occupied only from
#   occupied, mature neighbours inside `dispersal_m` (local grid, no wrap).
#   Re-occupied cells ramp from 0 to the TREED equilibrium with
#   phi = min(1, growth_cap_m_yr * age / H_eq). phi scales ONLY the outputs
#   (FPC, LAI, fine/coarse root, NPP, GPP, H) and never the traits, because
#   TREED allometry would otherwise return dense crowns and very large
#   area-normalised root C for a short stand.
#
# Values of growth_cap_m_yr and seed_source_min_phi are scenarios taken from
# the literature time scales (STAGE2_LITERATURE.md), not field calibrations.
###########################################################

const STAGE2 = Ref{Any}(nothing)
const STAGE2_MATURE_AGE = 1.0e8   # age >= this means "never disturbed or fully grown"

stage2_mode(par) = hasproperty(par, :mortality_mode) ? lowercase(String(par.mortality_mode)) : "off"
stage2_on(par) = stage2_mode(par) != "off"

# Window of cell (i,j) with radius R cells, clipped at the grid edge (no wrap).
function stage2_window(i, j, R, nx, ny)
    return (max(1, i - R):min(nx, i + R), max(1, j - R):min(ny, j + R))
end

# Development fraction of an occupied cell.
function stage2_phi_value(occupied, age, H_eq, growth_cap)
    occupied || return 0.0
    (growth_cap > 0.0 && age < STAGE2_MATURE_AGE) || return 1.0
    return H_eq > 0.0 ? min(1.0, growth_cap * age / H_eq) : 1.0
end

function stage2_begin!(par, climate, traitdir, mask)
    if !stage2_on(par)
        STAGE2[] = nothing
        return nothing
    end
    stage2_mode(par) == "landslide_scar" || error("Unknown mortality_mode=$(par.mortality_mode)")
    nx, ny = size(climate.topo)
    f = joinpath(traitdir, "stage2_restart.jld2")
    if isfile(f)
        d = load(f)
        occ = Array{Bool}(d["occupied"]); age = Array{Float64}(d["age_yr"])
        (size(occ) == (nx, ny) && size(age) == (nx, ny)) || error("stage2_restart.jld2 grid mismatch")
    else
        occ = fill(true, nx, ny)
        age = fill(1.0e9, nx, ny)
    end
    # Cells that survived grow one more year.
    for idx in eachindex(age)
        if occ[idx] && age[idx] < STAGE2_MATURE_AGE
            age[idx] += 1.0
        end
    end
    killed = 0
    if mask !== nothing
        size(mask) == (nx, ny) || error("landslide mask grid mismatch")
        for idx in eachindex(mask)
            if mask[idx] && occ[idx]
                occ[idx] = false
                age[idx] = 0.0
                killed += 1
            end
        end
    end
    STAGE2[] = Dict{Symbol,Any}(:occ => occ, :age => age, :phi => fill(NaN, nx, ny),
                                :killed => killed, :recolonised => 0)
    return nothing
end

# Same feasibility test as run_TREED_ecology (find_H_new), reused for a
# recolonised cell. base_tr carries the eight traits that plant_allometry needs.
function stage2_height(env, base_tr, pars2)
    function feasible(h)
        tr_int = plant_allometry(tr = merge(base_tr, (H = h,)), par = pars2)
        GPP_out_int = GPP_function_for_optimization(env = env, tr = tr_int, par = pars2)
        R_maintenance_int = R_maintenance_function(env = env, tr = tr_int, par = pars2, GPP_out = GPP_out_int)
        C_turnover_total_int = C_turnover_function(env = env, tr = tr_int, par = pars2)
        NPP_int = calc_NPP(GPP_out = GPP_out_int, R_maintenance = R_maintenance_int, par = pars2)
        net = calc_net_C_gain(NPP = NPP_int, C_turnover_total = C_turnover_total_int, par = pars2)
        return net <= -80 ? 0 : 1
    end
    test_heights = collect(0:0.25:50)
    evaluations = feasible.(test_heights)
    sum(evaluations) == 0 && return 0.0
    index = findlast(Int8.([1, 0]), Int8.(evaluations))
    index === nothing && return 50.0
    return test_heights[index[1]]
end

# Re-occupy empty cells from occupied, mature neighbours inside dispersal_m.
# Trait choice follows TREED's own rule (per trait, the neighbour value closest
# to this cell's optimised value). dispersal_m <= 0 gives no recolonisation.
function stage2_recolonize!(traits_end, traits_evolved, traits_optimized, climate, pars2, cellsize_m)
    par = pars2
    st = STAGE2[]
    st === nothing && return nothing
    occ = st[:occ]; age = st[:age]
    nx, ny = size(occ)
    occ0 = copy(occ); age0 = copy(age)
    dispersal_m = Float64(par.dispersal_m)
    growth_cap = Float64(par.growth_cap_m_yr)
    seed_phi = Float64(par.seed_source_min_phi)
    R = (dispersal_m > 0.0 && isfinite(cellsize_m) && cellsize_m > 0.0) ? max(1, round(Int, dispersal_m / cellsize_m)) : 0
    rd = ROOTDEPTH[]
    nnew = 0
    if R > 0
        Tave_e = traits_evolved.Tave_optim[Ti=1]; Tmin_e = traits_evolved.Tmin_optim[Ti=1]
        Tmax_e = traits_evolved.Tmax_optim[Ti=1]; Pave_e = traits_evolved.Pave_optim[Ti=1]
        Tave_o = traits_optimized.Tave_optim[Ti=1]; Tmin_o = traits_optimized.Tmin_optim[Ti=1]
        Tmax_o = traits_optimized.Tmax_optim[Ti=1]; Pave_o = traits_optimized.Pave_optim[Ti=1]
        for i in 1:nx, j in 1:ny
            (climate.habitable[i, j] == 1 && !occ0[i, j]) || continue
            wi, wj = stage2_window(i, j, R, nx, ny)
            cand = Tuple{Int,Int}[]
            for ni in wi, nj in wj
                (ni == i && nj == j) && continue
                occ0[ni, nj] || continue
                (traits_end.H[ni, nj] > 0) || continue
                phi_n = stage2_phi_value(true, age0[ni, nj], Float64(traits_end.H[ni, nj]), growth_cap)
                phi_n >= seed_phi || continue
                push!(cand, (ni, nj))
            end
            isempty(cand) && continue
            dist(v, o) = (isfinite(v) && isfinite(o)) ? abs(v - o) : Inf
            pick(vals_e, val_o) = cand[argmin([dist(vals_e[c...], val_o) for c in cand])]
            c_all = pick(traits_evolved.a_ll, traits_optimized.a_ll[i, j])
            c_leaf = pick(traits_evolved.C_leaf, traits_optimized.C_leaf[i, j])
            c_tave = pick(Tave_e, Tave_o[i, j]); c_tmin = pick(Tmin_e, Tmin_o[i, j])
            c_tmax = pick(Tmax_e, Tmax_o[i, j]); c_pave = pick(Pave_e, Pave_o[i, j])
            a_ll_new = traits_evolved.a_ll[c_all...]
            seas_new = (a_ll_new <= 1.0 && traits_evolved.seasonality[c_all...] < 1.0) ? 0.0 : 1.0
            base_tr = (a_ll = a_ll_new, C_leaf = traits_evolved.C_leaf[c_leaf...],
                       seasonality = seas_new, r_s_r = traits_end.r_s_r[i, j],
                       Tave_optim = Tave_e[c_tave...], Tmax_optim = Tmax_e[c_tmax...],
                       Tmin_optim = Tmin_e[c_tmin...], Pave_optim = Pave_e[c_pave...])
            z_old = NaN
            if rd !== nothing
                z_old = rd[:z_r][i, j]
                zo = rd[:z_opt][i, j]
                zsrc = [rd[:z_r][c...] for c in cand]
                rd[:z_r][i, j] = isfinite(zo) ? zsrc[argmin(abs.(zsrc .- zo))] : zsrc[1]
            end
            env = (precip_monthly = parent(climate.precip[i, j, :]),
                   tair_monthly = parent(climate.tair[i, j, :]),
                   tair_annual = mean(parent(climate.tair[i, j, :])),
                   rsds_monthly = parent(climate.rsds[i, j, :]),
                   rss_monthly = parent(climate.rss[i, j, :]),
                   rls_monthly = parent(climate.rls[i, j, :]),
                   daylength = parent(climate.daylength[i, j, :]),
                   CO2_ppm = climate.CO2_ppm,
                   precip_annual = mean(parent(climate.precip[i, j, :])),
                   paw_mm = climate.paw_mm[i, j],
                   soildepth_m = climate.soildepth_m[i, j], rd = rootdepth_cell(i, j))
            H_new = stage2_height(env, base_tr, pars2)
            if !(H_new > 0.0)                # not productive: stays empty, retried next year
                rd !== nothing && (rd[:z_r][i, j] = z_old)
                continue
            end
            traits_end.a_ll[i, j] = base_tr.a_ll
            traits_end.seasonality[i, j] = base_tr.seasonality
            traits_end.C_leaf[i, j] = base_tr.C_leaf
            traits_end.Tave_optim[i, j] = base_tr.Tave_optim
            traits_end.Tmin_optim[i, j] = base_tr.Tmin_optim
            traits_end.Tmax_optim[i, j] = base_tr.Tmax_optim
            traits_end.Pave_optim[i, j] = base_tr.Pave_optim
            traits_end.H[i, j] = H_new
            occ[i, j] = true
            age[i, j] = 0.0
            nnew += 1
        end
    end
    # Empty cells report no vegetation height and are not seed sources.
    for i in 1:nx, j in 1:ny
        if climate.habitable[i, j] == 1 && !occ[i, j]
            traits_end.H[i, j] = 0.0
        end
    end
    st[:recolonised] = nnew
    return nothing
end

# Scale outputs by the development fraction. phi = 1 leaves a cell untouched,
# so mortality on with no disturbance is identical to mortality off.
function stage2_apply_outputs!(veg, traits_end, par)
    st = STAGE2[]
    st === nothing && return nothing
    occ = st[:occ]; age = st[:age]; phi_map = st[:phi]
    growth_cap = Float64(par.growth_cap_m_yr)
    nx, ny = size(occ)
    scaled = (:FPC, :LAI, :C_fineroot, :C_coarseroot, :C_sapwood, :C_heartwood,
              :NPP, :GPP, :R_maintenance, :Net_C_gain, :H)
    for i in 1:nx, j in 1:ny
        h = traits_end.H[i, j]
        isfinite(h) || continue
        phi = stage2_phi_value(occ[i, j], age[i, j], Float64(h), growth_cap)
        if phi >= 1.0 && h > 0 && occ[i, j] && age[i, j] < STAGE2_MATURE_AGE
            age[i, j] = 1.0e9          # fully grown: no later re-ramp if H_eq moves
        end
        phi_map[i, j] = phi
        phi >= 1.0 && continue
        for f in scaled
            hasproperty(veg, f) || continue
            A = getproperty(veg, f)
            v = A[i, j]
            isfinite(v) && (A[i, j] = v * phi)
        end
    end
    return nothing
end

function stage2_save!(traitdir)
    st = STAGE2[]
    st === nothing && return nothing
    occupied = st[:occ]; age_yr = st[:age]
    @save joinpath(traitdir, "stage2_restart.jld2") occupied age_yr
    return nothing
end
