# v1.5 reference values for the v1.6 regression check

Extracted, unchanged, from the `lorica-v15-open30-beta2` artifact of GitHub Actions run
[#43725363487](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/43725363487)
(source commit `695526249487c8adaa19c8bd6dd099ffd6de628b`), as delivered in
`gounsa_v15_open30_beta2.zip` (sha256 `3257ad9ac11f7f3382bb5d4c78993cbd7ed8933785def4d549d1ac141e6dfd13`).

- `v15_open30_beta2_annual_state.csv`: the artifact's `annual_state.csv` (30 years).
- `v15_open30_beta2_cells_years01_13.csv`: per-cell values of years 1-13 read from the
  artifact's `year_XX/*.asc` rasters (TREED raw FPC/LAI/rootC, soil depth, DEM, root cohesion,
  water erosion).

The v1.6 regression job reruns the exact v1.5 `TestThirtyYearNormalTimestep()` (beta=2,
13 years, open hillslope) with the v1.6 read-only landslide snapshot hook compiled in, and
must reproduce these numbers. Year 13 is included because it is the first year in which
v1.5 beta0 and beta2 TREED states diverged.
