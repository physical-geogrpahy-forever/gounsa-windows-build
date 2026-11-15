# v1.5 native open-hillslope validation — verified

Execution: [GitHub Actions #43723697839](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/43723697839), source SHA `4cc726c4ebd0728e9c4afb6234df341520c7ba2e`. Windows TREED+LORICA `every_timestep()` beta0, beta2, and independent comparison all **success**.

## Experimental configuration

- Synthetic 5×5 grid, 10 m resolution, 1 m starting soil depth. Not the observed Gounsa DEM.
- `GOUNSA_TOPO_MODE=open_hillslope`, z(r,c)=115−4r+2|c−2| m. All 25 cells route to one lower boundary outlet in a separately audited D8 preflight. No closed internal basin.
- `root_allocation_mode=fixed_original`, `soil_water_coupling_strength=1.0`, `K=0.0001` (unvalidated sensitivity setting), 3 annual native timesteps, β=0 or 2.
- Events: annually one 60 mm/6 h storm, annual rain 730/900/600 mm, temperatures 10/11/12°C. No landslides occurred.
- The archived `TREED_coupling.cfg` is copied **after** the runner restores its temporary `landslide_event_mode` overrides. The actual per-run mode was `explicit_event`, 60 mm/6 h; this follows the audited runner source. Do not infer effective event mode from the archived copy.

## Measured native outputs

| 3-year outcome | beta0 | beta2 |
|---|---:|---:|
| Gross water erosion, sum of cellwise thicknesses (m) | 0.000419235446 | 0.000151456221 |
| In-domain deposition, sum of cellwise thicknesses (m) | 0.000198778186 | ≈0 |
| Sediment exported outside computational domain (kg) | 35.64180904 | 24.48223128 |
| Maximum yearly relative mass-closure error | 1.276e-15 | 9.279e-16 |
| Initiated landslides | 0 | 0 |

- 3-year gross erosion reduction under beta2: **63.87%**.
- 3-year **exported sediment** reduction under beta2: **31.31%**. These different reductions are real because beta0 deposits material inside the catchment (3 depositional cells each year), whereas beta2 has no measurable deposition.
- Native model outputs and an independent Python audit confirmed that annual soil mass loss matches the separately measured exported sediment mass within 1e-5 kg for years 2–3.
- Beta0 and beta2 have identical TREED FPC, LAI, and root-carbon trajectories in all three years, despite different eroded/depitted soil and DEM rasters. Thus active soil-water coupling alone does **not** establish detectable reverse Geo→Eco effects in this particular 3-year mild-erosion test.

## Important scientific limits

The source-audited TREED `traits_restart.jld2` holds community-representative functional traits, **not demographic cohorts, individual mortality or landslide recolonization histories**. The unmodified TREED model and this experiment do not implement post-landslide vegetation mortality or recovery. See `audits/v1.5/TREED_RESTART_SOURCE_AUDIT.md` and Rogger et al. (2026, GMD, DOI 10.5194/gmd-19-4931-2026).

Result is **numerical integration and sediment-routing validation**, not observed erosion calibration or a Gounsa field prediction.
