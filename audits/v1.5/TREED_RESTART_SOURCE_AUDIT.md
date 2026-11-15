# TREED–LORICA v1.5: landslide restart and population-state source audit

Source: exact v0.5 bundle `lorica_treed/v0.5/LORICA_TREED_v0.5_source.tar.xz` extracted without modifications by GitHub Actions [source audit](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/43724148989).

## Verified original code findings

- `TREED/src/TREED_model_functions.jl`, lines 26–39: the `traits` object has nine attributes, `H`, `a_ll`, `C_leaf`, `seasonality`, `r_s_r`, and four environmental optima. There is no stand-level population density, mortality event, landslide scar age or separate dead-biomass storage.
- `TREED/src/TREEDlocalstep.jl`, lines 71–86: restart loads `traits_end`, executes optimization/evolution/ecology, then saves `traits_end` before computing `FPC`, `LAI` and root carbon. The saved traits are not a demographic cohort or mortality ledger.
- `TREED/src/TREEDlocalstep.jl`, lines 50–58: the `habitable` mask checks valid topography and temperature, but does not mask `soildepth_m <= 0`. Hence soil-free cells can retain positive native TREED FPC, even when the separate LORICA coupling sets effective FPC and effective root cohesion to zero.
- `TREED/src/TREED_model_functions.jl`, lines 462–475: low-production sites may retain traits as an implicit refuge and regain height when favorable conditions return. This is not explicit loss and long-term recolonization after a landslide.
- `LORICA/LORICA_main.cs`, lines 7179–7186 and 7212–7221: in one LORICA annual timestep, TREED is called before `water_balance`; `calculate_water_ero_sed_daily` is called once after the water balance. Thus the existing `treed_water_sediment_export_kg` field represents sediment export from that annual routine, not just the last calendar day's export.

## Scientific decisions

1. Preserve the verified original TREED and existing LORICA physics. Do not assert that the model simulates forest stand mortality or succession when the saved state does not represent them.
2. Never interpret a zero-soil-depth synthetic pixel as proof that all real trees or roots have died; gounsa observations (rock fissures, C-horizon roots) matter.
3. Validate the open-outlet sediment balance separately with identical forcing under beta0 and beta2; the new optional `GOUNSA_TOPO_MODE=open_hillslope` changes initial DEM only. The existing default remains `closed_convergent`.
4. Treat an explicit landslide mortality/regrowth module as a distinct, reference-based model addition, not a silent fix to original TREED.

Unresolved: real Gounsa DEM and hydrologic boundary data; measured erosion/landslide patterns; calibrated root survival and recovery times.
