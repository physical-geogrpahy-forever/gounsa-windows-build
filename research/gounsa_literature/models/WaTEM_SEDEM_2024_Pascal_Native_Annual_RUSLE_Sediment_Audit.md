# WaTEM/SEDEM 2024+ official source original scope audit: annual soil loss versus free XY storm

## Program publication/source pedigree
- Original model scientific reference Van Rompaey et al. 2001 *ESPL* DOI10.1002/esp.275. [Canonical paper](../papers/2001_VanRompaey_Verstraeten_VanOost_WaTEM_SEDEM_AnnualSediment.md).
- KU Leuven official developer description https://ees.kuleuven.be/en/geography/modelling/erosion/watem-sedem directly links https://github.com/watem-sedem/watem-sedem; official MIT? **NO** source license expressly LGPL3. Original language Delphi later Free Pascal since 2017. Source + Windows/Linux binaries releases fully available.
- Latest cited preserved 5.0.1 (2024) Zenodo DOI https://doi.org/10.5281/zenodo.10997288 ; don't equate this with 2001 original numerical results.

## Actual public code and mathematical execution trace
- GitHub repository `watem-sedem/watem-sedem` official original. `common/runmodel.pas` calls `Topo_Calculations` and sorts DTM/routing/upstream area/LS before RUSLE-annual erosion logic. Code `common/lateralredistribution.pas` calculates ktc by landuse; `common/write_output.pas` exports sediment masses/erosion/deposition per raster.
- `docs/watem-sedem.rst`: **adapted RUSLE mean annual E=R K LS C P**, soil erosion net/deposition by transport capacity. Physical same-time water depth/hydraulic velocity and canopy water storage are **not part of the standard governing equations**.
- `docs/routing.rst`: DEM-based multi-direction routing/flux decomposition, sediment outgoing from one pixel to one or two target pixels; grid2D representation not 2D shallow-water PDE momentum.
- `docs/formulas-units.rst`: outgoing S_o = min(S_i+E,TC) after normalization, converts rate and flux to per-cell m³. Annual tonnage and spatial net E/D not subhourly sediment concentration.
- Search in default repo `interception` only `docs/cn-ws.rst` CN initial abstraction `I_a` mention interception by name; `canopy` only crop canopy **C-subfactor**. No active `LAI` canopy tank/leaf drip and kinetic energy native functions found. Crop protective C factor should not be laundered as canopy process.
- Actual `docs/tutorials/Total sediment 1.txt` contains annual net erosion/deposition (negative erosion positive deposition), but these outputs prove annual mass delivery not physically resolved 6h run.

## Exact hard gate
| Gate | Published/source result |
|---|---|
| Original full source + binary | YES, official Pascal LGPL v3 |
| Cellwise erosion/deposition sediment connectivity | YES, annual RUSLE/TC |
| One short storm rainfall input mm/h + water depth h(t) | NO standard native basis |
| LAI canopy water storage/drainage/drop energy | NO native |
| Four edge unrestricted 2D hydraulic advection | NO, direction/flux decomposition |
| Published 5cm 6h, numerical CFL mass | NO |

**User Gounsa engine NO-GO**. Better at long-term annual catchment C-factor landscape analysis, not event forest hillslope rain canopy comparison. Do not conflate 2D grid output with 2D flow.

## Links
https://github.com/watem-sedem/watem-sedem
https://github.com/watem-sedem/watem-sedem/blob/master/common/runmodel.pas
https://github.com/watem-sedem/watem-sedem/blob/master/docs/watem-sedem.rst
https://github.com/watem-sedem/watem-sedem/blob/master/docs/routing.rst
https://watem-sedem.github.io/watem-sedem/
https://doi.org/10.5281/zenodo.10997288
