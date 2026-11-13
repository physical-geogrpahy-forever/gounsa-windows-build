# Deterministic wrapper for the LORICA-TREED local-grid driver.
# TREED's ECA optimizer is stochastic; seed it before loading/running TREED.
using Random

length(ARGS) >= 2 || error("Usage: julia treed_lorica_driver.jl YEAR_DIR TREED_DIR")
year_dir = abspath(ARGS[1])
year = parse(Int, basename(year_dir))
cfg_path = joinpath(dirname(year_dir), "TREED_coupling.cfg")

base_seed = 20261113
if isfile(cfg_path)
    for raw in eachline(cfg_path)
        line = strip(raw)
        if startswith(line, "treed_random_seed=")
            base_seed = parse(Int, strip(split(line, "=", limit=2)[2]))
            break
        end
    end
end

seed = base_seed + year
Random.seed!(seed)
println("TREED_RANDOM_SEED=", seed)

# The original, unchanged v0.5 driver is retained as the core.
include(joinpath(@__DIR__, "treed_lorica_driver_core.jl"))
