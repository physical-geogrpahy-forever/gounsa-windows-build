# Deterministic annual TREED wrapper for the 30-year LORICA-TREED run.
# The TREED model equations and ECA objective remain unchanged.
using Random

length(ARGS) >= 2 || error("Usage: treed_lorica_driver.jl YEAR_DIR TREED_DIR")
year_dir = abspath(ARGS[1])
year = parse(Int, basename(year_dir))
exchange_root = dirname(year_dir)
cfg_path = joinpath(exchange_root, "TREED_coupling.cfg")

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
ENV["TREED_RANDOM_SEED"] = string(seed)
Random.seed!(seed)
traitdir = joinpath(exchange_root, "traits")
restart_path = joinpath(traitdir, "traits_restart.jld2")
restart_before = isfile(restart_path)
println("TREED_RANDOM_SEED=", seed)
println("TREED_RESTART_PRESENT_BEFORE=", restart_before)

# Core is the original LORICA-to-TREED driver copied from the source bundle.
include(joinpath(@__DIR__, "treed_lorica_driver_core.jl"))

restart_after = isfile(restart_path)
restart_bytes = restart_after ? filesize(restart_path) : 0
audit_path = joinpath(exchange_root, "TREED_driver_audit.csv")
if !isfile(audit_path)
    open(audit_path, "w") do io
        println(io, "year,seed,restart_present_before,restart_present_after,restart_size_bytes")
    end
end
open(audit_path, "a") do io
    println(io, join((year, seed, lowercase(string(restart_before)),
                      lowercase(string(restart_after)), restart_bytes), ","))
end
println("TREED_RESTART_PRESENT_AFTER=", restart_after)
