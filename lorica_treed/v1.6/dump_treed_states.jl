# Dump the per-year TREED restart traits (traits_restart.jld2 = traits_end)
# and the per-year TREED NetCDF output to flat CSV tables, cell by cell.
# Read-only: nothing is written back to the model state.
#
# Usage: julia --project=TREED_DIR dump_treed_states.jl RUN_ROOT TREED_DIR
#   RUN_ROOT contains year_XX/ folders written by LoricaTreedLandslideRecovery.
# Row/col use the LORICA/ESRI orientation (row 0 = north), identical to the
# driver's to_esri() = permutedims(Array(layer)).

length(ARGS) >= 2 || error("Usage: dump_treed_states.jl RUN_ROOT TREED_DIR")
run_root = abspath(ARGS[1])
treed_dir = abspath(ARGS[2])
include(joinpath(treed_dir, "src", "TREED.jl"))
using .TREED
using JLD2, Rasters, NCDatasets, DimensionalData

fields = collect(fieldnames(TREED.traits))
years = sort(filter(d -> startswith(d, "year_") && isdir(joinpath(run_root, d)), readdir(run_root)))
isempty(years) && error("No year_XX folders in $run_root")

function esri(A)
    M = Array(A)
    # Trait optima are stored as mean/max/min over Ti => trailing Ti axis of length 1.
    if ndims(M) == 3
        size(M, 3) == 1 || error("unexpected 3-D trait raster with Ti length $(size(M, 3))")
        M = M[:, :, 1]
    end
    ndims(M) == 2 || error("unexpected raster rank $(ndims(M))")
    return permutedims(M)
end
fmt(x) = (x === missing || !(x isa Real) || !isfinite(x)) ? "NaN" : string(Float64(x))

open(joinpath(run_root, "treed_restart_traits_by_cell.csv"), "w") do io
    println(io, join(vcat(["year", "row", "col"], string.(fields)), ","))
    for yd in years
        y = parse(Int, yd[6:end])
        p = joinpath(run_root, yd, "traits_restart.jld2")
        isfile(p) || error("missing $p")
        tr = JLD2.load(p)["traits_end"]
        mats = [esri(getfield(tr, f)) for f in fields]
        nr, nc = size(mats[1])
        for r in 1:nr, c in 1:nc
            println(io, join(vcat([string(y), string(r - 1), string(c - 1)], [fmt(m[r, c]) for m in mats]), ","))
        end
    end
end
println("TREED_RESTART_TRAITS_DUMPED years=", length(years), " fields=", join(string.(fields), "|"))

layer_names = nothing
open(joinpath(run_root, "treed_output_by_cell.csv"), "w") do io
    for yd in years
        y = parse(Int, yd[6:end])
        p = joinpath(run_root, yd, "TREED_output_timestep_$(y).nc")
        isfile(p) || (println("WARN missing ", p); continue)
        st = RasterStack(p)
        names2d = sort([string(k) for k in keys(st) if ndims(st[k]) == 2])
        if layer_names === nothing
            global layer_names = names2d
            println(io, join(vcat(["year", "row", "col"], layer_names), ","))
        end
        mats = [esri(st[Symbol(k)]) for k in layer_names]
        nr, nc = size(mats[1])
        for r in 1:nr, c in 1:nc
            println(io, join(vcat([string(y), string(r - 1), string(c - 1)], [fmt(m[r, c]) for m in mats]), ","))
        end
    end
end
println("TREED_OUTPUT_DUMPED layers=", layer_names === nothing ? "none" : join(layer_names, "|"))
