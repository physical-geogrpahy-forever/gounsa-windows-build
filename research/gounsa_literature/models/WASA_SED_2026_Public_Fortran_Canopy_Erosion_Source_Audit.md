# WASA-SED Fortran native source-audit 2026-10-27

## Strict goal
Search newly other-than-OpenLISEM fully publicly distributed model able to resolve **5–10cm same original rainfall event** with canopy LAI, genuine 2D XY hydrodynamics, splash/runoff erosion, local sediment deposition and optional morphological effects.

## Published origin
Mueller et al. (2010), *Geoscientific Model Development* 3:275–291 DOI 10.5194/gmd-3-275-2010. Upstream https://github.com/TillF/WASA-SED, docs version rev_281 (2025-01-28), source is 90% Fortran90 style and sample inputs/tutorial distributed, Makefile to compile; license text CC BY 4-style customized wording `license.txt` read. Do not claim GPL from repo; repo metadata says NOASSERTION.

## Actual source read
1. `src/Hillslope/soilwat.f90` SHA `536d2392c441988f43899fbbf25fcb9c9191a767`: function signature includes `tclai`, `tcintc`, `lai_act(nveg)`, `prec_in`; internal `! (11) INTERCEPTION` and `q_surf_in`, `q_surf_out`. SVC/TC indexing `i_ce,i_lu,tcid_instance2` and runoff redistribution to lower terrain components. **No PDE XY SWE solver**.
2. `src/Hillslope/sedi_yield.f90` SHA `43af5642e1879ad7794f47299dbf5b7234256ad8`: L25–29 `q_in`, `q_out` [m3] and hourly timestep; L80-90 computes area-fraction weighted `K_fac C_fac P_fac` across soil-vegetation components; L181–195 `SELECT CASE(erosion_equation)`: USLE, Onstad–Foster, MUSLE, MUST. These are **not finite-volume bidirectional local raindrop & sheet detachment**.
3. `docs/index.md` manual explicitly describes semi-distributed sub-basin / LU / TC / SVC, hourly/daily hillslope hydrology, downstream sediment routing and reservoir deposition. GMD 2010 shows 445km2 Isábena experimental application. Raster GIS input/mapping should not be confused with native 5cm 2D flow.

## Decision matrix
- Complete public native source: **YES**
- Canopy LAI and intercepted water native: **YES**
- Runoff and erosion same source: **YES at hillslope conceptual TC and USLE-family equations**
- Genuine XY 2D SWE / independent grid-face fluxes: **NO**
- Published 0.05–0.1m computational rainfall erosion: **NO evidence**
- Native splash/drop impact, 2D suspended load advection + local deposit/DoD: **NO**
- Native source compiled/benchmark executed in this audit: **NO (not needed after spatial criterion fails)**

## Final
**Reject as original free 2D centimeter Gounsa engine**; keep as actually code-inspected non-LISEM literature. Adding grid/SWE is unwanted new coupling.

## Links
https://github.com/TillF/WASA-SED/blob/master/src/Hillslope/soilwat.f90
https://github.com/TillF/WASA-SED/blob/master/src/Hillslope/sedi_yield.f90
https://github.com/TillF/WASA-SED/blob/master/docs/index.md
https://doi.org/10.5194/gmd-3-275-2010
