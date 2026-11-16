###########################################################
# Gounsa v1.7 EXPERIMENTAL root-depth trait module for TREED
#
# NOT part of upstream TREED (Rogger et al. 2026). Opt-in through
# `root_depth_mode`; the default "off" leaves every TREED code path and every
# output byte unchanged.
#
# Trait  z_r [m]: potential rooting depth (depth holding 95 % of roots, D95).
# Realised depth   z_eff = min(z_r, soil depth).
# Benefit          plant-accessible storage S_r = PAW * z_eff / soil depth,
#                  entering the monthly water supply.
# Cost             Guswa (2008) Eq. 1: C = gamma_r * RLD / SRL * z_eff, a root
#                  respiration cost proportional to realised depth. Default
#                  146.1 g C m-2 yr-1 per m from Guswa Table 2 (gamma_r = 0.5
#                  mmol C g-1 d-1, RLD = 0.10 cm cm-3, SRL = 1500 cm g-1);
#                  Guswa Table 1 (Nylsvley savanna) gives 14.0. Neither is a
#                  Korean measurement.
# Optimum          z_r is NOT an ECA dimension (the 20-iteration ECA cannot
#                  resolve it). After the unchanged 3-D ECA, z_r_opt is found
#                  by a deterministic grid search maximising net carbon gain
#                  with the other traits fixed (Guswa's marginal cost = marginal
#                  benefit condition), bounded above by soil depth.
#
# Water supply modes
#   "milly_stochastic": Guswa (2008, WRR 44, W02427) Eq. 12 / A1-A2, after
#       Milly (1993):  <T> = Tpot * W * (exp(B) - 1) / (exp(B) - W),
#       B = S_r (1 - W) / alpha,  W = alpha * lambda / Tpot.
#       alpha = mean rain depth on wet days [mm], lambda = wet-day frequency
#       [1/day]; each month is treated as statistically stationary (no
#       carry-over of storage between months).
#   "bucket_monthly": deterministic monthly bucket with carry-over, cyclic
#       steady state (two passes over the 12 months).
#
# Root profile: Jackson et al. (1996) Y(d) = 1 - beta^d, truncated and
# renormalised at z_eff as in LPJmL4.0-VR (Sakschewski et al. 2021, Eq. A2).
###########################################################

# Per-run state. `nothing` when the module is off.
const ROOTDEPTH = Ref{Any}(nothing)

rootdepth_mode(par) = hasproperty(par, :root_depth_mode) ? lowercase(String(par.root_depth_mode)) : "off"
rootdepth_on(par) = rootdepth_mode(par) != "off"

function rootdepth_cell(i, j)
    st = ROOTDEPTH[]
    st === nothing && return nothing
    return (z_r = st[:z_r][i, j], alpha_mm = st[:alpha_mm], lambda_per_day = st[:lambda_per_day])
end

# Trial value during optimisation, otherwise the cell's current trait.
function rootdepth_zr(env)
    hasproperty(env, :z_r_trial) && return Float64(env.z_r_trial)
    return Float64(env.rd.z_r)
end

function rootdepth_zeff(z_r, env)
    zs = (hasproperty(env, :soildepth_m) && isfinite(env.soildepth_m)) ? max(0.0, Float64(env.soildepth_m)) : 0.0
    return max(0.0, min(Float64(z_r), zs))
end

# Plant-accessible storage [mm]; PAW assumed uniform over the soil column.
function rootdepth_storage_mm(z_r, env)
    zs = (hasproperty(env, :soildepth_m) && isfinite(env.soildepth_m)) ? max(0.0, Float64(env.soildepth_m)) : 0.0
    paw = (hasproperty(env, :paw_mm) && isfinite(env.paw_mm)) ? max(0.0, Float64(env.paw_mm)) : 0.0
    zs <= 0.0 && return 0.0
    return paw * rootdepth_zeff(z_r, env) / zs
end

# Guswa (2008) Eq. 12. All rates in mm/day, storage in mm.
function rootdepth_milly_T(S_mm, alpha_mm, lambda_per_day, Tpot)
    (Tpot > 0.0 && alpha_mm > 0.0 && lambda_per_day > 0.0 && S_mm > 0.0) || return 0.0
    W = alpha_mm * lambda_per_day / Tpot
    B = S_mm * (1.0 - W) / alpha_mm
    if abs(1.0 - W) < 1e-9
        g = S_mm / alpha_mm
        ratio = g / (1.0 + g)
    elseif B > 50.0
        ratio = 1.0
    elseif B < -50.0
        ratio = 1.0 / W
    else
        eB = exp(B)
        ratio = (eB - 1.0) / (eB - W)
    end
    return min(Tpot, Tpot * W * ratio)
end

# Monthly water supply [mm/day] replacing min(Emax, P) (+ Gounsa PAW term).
function rootdepth_esupply(env, par, Edemand, Emax)
    mode = rootdepth_mode(par)
    z_r = rootdepth_zr(env)
    S = rootdepth_storage_mm(z_r, env)
    P = Float64.(env.precip_monthly) .* 1000.0   # mm/day
    Ed = Float64.(Edemand)
    Es = zeros(Float64, 12)
    if mode == "milly_stochastic"
        lam = env.rd.lambda_per_day
        for m in 1:12
            if Ed[m] <= 0.0
                Es[m] = min(Emax, P[m])
                continue
            end
            # alpha is rescaled so that alpha*lambda equals the month's mean
            # rainfall rate used everywhere else in TREED.
            a = lam[m] > 0.0 ? P[m] / lam[m] : 0.0
            T = rootdepth_milly_T(S, a, lam[m], Ed[m])
            # Avoid flagging numerically-saturated months as water stressed.
            Es[m] = T >= 0.995 * Ed[m] ? Ed[m] : T
            Es[m] = min(Emax, Es[m])
        end
    elseif mode == "bucket_monthly"
        days = Float64.(par.month_days)
        Wst = S
        for pass in 1:2, m in 1:12
            Es[m] = min(Emax, P[m] + Wst / days[m])
            aet = min(Es[m], max(0.0, Ed[m]))
            Wst = min(S, max(0.0, Wst + (P[m] - aet) * days[m]))
        end
    else
        error("Unknown root_depth_mode=$(par.root_depth_mode). Use off, milly_stochastic or bucket_monthly.")
    end
    return Es
end

# Annual root-depth carbon cost [g C m-2 yr-1], Guswa (2008) Eq. 1.
function rootdepth_cost(env, par)
    return par.root_depth_cost_gC_m2_yr_per_m * rootdepth_zeff(rootdepth_zr(env), env)
end

# Deterministic search for the depth that maximises net carbon gain with the
# ECA-optimised traits held fixed. Ties resolve to the shallowest depth.
function rootdepth_grid_opt(env, par, a_ll, C_leaf, H)
    zs = (hasproperty(env, :soildepth_m) && isfinite(env.soildepth_m)) ? max(0.0, Float64(env.soildepth_m)) : 0.0
    zmin = Float64(par.root_depth_min_m)
    ub = min(Float64(par.root_depth_max_m), zs)
    ub <= zmin && return zmin
    seasonality = sum(env.tair_monthly .<= par.temp_threshold_growing_season) >= 3. ? 0 : 1
    grid = collect(zmin:Float64(par.root_depth_search_step_m):ub)
    grid[end] < ub && push!(grid, ub)
    best_z = zmin; best = -Inf
    for z in grid
        e = merge(env, (z_r_trial = z,))
        tr = plant_allometry(tr = (a_ll = a_ll, C_leaf = C_leaf, H = H, r_s_r = par.r_s_r_initial,
            seasonality = seasonality, Tave_optim = mean(env.tair_monthly), Tmax_optim = maximum(env.tair_monthly),
            Tmin_optim = minimum(env.tair_monthly), Pave_optim = mean(env.precip_monthly)), par = par)
        G = GPP_function_for_optimization(env = e, tr = tr, par = par)
        R = R_maintenance_function(env = e, tr = tr, par = par, GPP_out = G)
        N = calc_NPP(GPP_out = G, R_maintenance = R, par = par)
        C = C_turnover_function(env = e, tr = tr, par = par)
        net = calc_net_C_gain(NPP = N, C_turnover_total = C, par = par)
        if net > best + 1e-9
            best = net; best_z = z
        end
    end
    return best_z
end

function rootdepth_begin!(par, climate, traitdir; alpha_mm = nothing, lambda_per_day = nothing)
    if !rootdepth_on(par)
        ROOTDEPTH[] = nothing
        return nothing
    end
    lowercase(String(par.root_allocation_mode)) == "fixed_original" ||
        error("root_depth_mode requires root_allocation_mode=fixed_original")
    mode = rootdepth_mode(par)
    mode in ("milly_stochastic", "bucket_monthly") ||
        error("Unknown root_depth_mode=$(par.root_depth_mode)")
    if mode == "milly_stochastic"
        (lambda_per_day !== nothing && length(lambda_per_day) == 12) ||
            error("milly_stochastic needs 12 monthly wet-day frequencies (rain_event_stats_monthly.csv)")
    end
    nx, ny = size(climate.topo)
    f = joinpath(traitdir, "rootdepth_restart.jld2")
    if isfile(f)
        z = load(f)["z_r"]
        size(z) == (nx, ny) || error("rootdepth_restart.jld2 grid mismatch")
    else
        z = fill(Float64(par.root_depth_initial_m), nx, ny)
    end
    ROOTDEPTH[] = Dict{Symbol,Any}(
        :z_r => z,
        :z_start => copy(z),
        :z_opt => fill(NaN, nx, ny),
        :alpha_mm => alpha_mm === nothing ? fill(NaN, 12) : Float64.(alpha_mm),
        :lambda_per_day => lambda_per_day === nothing ? fill(NaN, 12) : Float64.(lambda_per_day))
    return nothing
end

function rootdepth_store_opt!(i, j, optimized_traits)
    st = ROOTDEPTH[]
    st === nothing && return nothing
    st[:z_opt][i, j] = optimized_traits.z_r_optimized
    return nothing
end

# Same lagged-adaptation rule as every other TREED trait.
function rootdepth_evolve!(evorate)
    st = ROOTDEPTH[]
    st === nothing && return nothing
    z = st[:z_r]; zo = st[:z_opt]
    for idx in eachindex(z)
        if isfinite(zo[idx])
            z[idx] = z[idx] + evorate * (zo[idx] - z[idx])
        end
    end
    return nothing
end

function rootdepth_save!(traitdir)
    st = ROOTDEPTH[]
    st === nothing && return nothing
    z_r = st[:z_r]
    @save joinpath(traitdir, "rootdepth_restart.jld2") z_r
    return nothing
end
