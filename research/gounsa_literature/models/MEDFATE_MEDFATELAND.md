# MEDFATE + medfateland

## 현재 판정
BiomeE/BiomeEP와 유사한 cohort process model을 **실제 GIS 공간단위로 확장한 가장 직접적인 공개 구현 사례 중 하나**.

## 식생 표현
MEDFATE:
- tree cohorts
- shrub cohorts
- optional species-specific herb cohorts (`herbData`)
- seed bank / seedling bank
- cohort-specific fine-root depth distribution
- daily water/carbon/growth
- annual woody recruitment and forest dynamics

개별목 x,y는 추적하지 않는다.

## 공간 확장
medfateland v3.0.0:
- sf point/cell based spatial units
- terra raster topology for connected grid cells
- forest, soil, topography, weather state per spatial unit
- parallel execution
- explicit seed dispersal among stands
- lateral surface flow
- lateral subsurface flow
- groundwater/baseflow
- channel routing
- optional SERGHEI coupling

핵심 함수:
- spwb_spatial / growth_spatial / fordyn_spatial
- spwb_land / growth_land / fordyn_land
- spwb_land_day / growth_land_day

`fordyn_land` adds management, seed dispersal, recruitment and resprouting to daily distributed ecohydrology/growth.

## 실제 published spatial application
Balaguer-Romano et al. 2025:
- medfate 4.8.0 + medfateland 2.5.2
- Barcelona Metropolitan Region
- 313,000 ha
- 200 m raster grid
- daily weather forcing
- tree + understory shrub species in forest cells
- growth, mortality and forest succession simulated 2015–2050
- 200 m resolution was chosen because of computational limitations, not because of a hard model cell-size limit

2026 package documentation:
- medfateland v3.0.0 uses user-defined `terra::SpatRaster` topology
- connected watershed example uses 100 m cells
- no hard-coded minimum cell dimension was found

Therefore 10–25 m cells are structurally allowed, but **no published validation at 10–25 m was identified**. Fine resolution must be benchmarked for computational cost and scale validity.

## 중요한 장점 for Gounsa
1. cohort-based, not individual-tree
2. actual geographic cells rather than statistical disturbance patches
3. dynamic tree and shrub understory
4. existing herb cohorts can participate in growth simulations
5. daily water/carbon/growth
6. vertical fine-root distribution by cohort
7. seed dispersal among spatial units
8. lateral water transfer among cells
9. one-day simulation functions allow external event loop control
10. state objects can be continued into subsequent calls
11. R ecosystem: sf, terra and parallelization align with current workflow

## Herb cohort code audit, 2026-09-23
Current medfate source/tests show:
- `forest` objects can contain `herbData` with species, height, cover, Z50 and Z95.
- `growthInput()` explicitly incorporates tree, shrub and herb root-depth parameters.
- package tests run both `growth()` and `fordyn()` successfully with `herbData` present.

However, the natural-regeneration code is not symmetric across growth forms:
- seed production/recruitment is separated into trees and shrubs.
- `.seedlings2recruits()` creates only tree and shrub recruit cohorts.
- `herbData` is explicitly removed from the newly generated recruit forest object.
- resprouting likewise handles tree and shrub cohorts, not herb recruitment.

Therefore the correct statement is:

```
existing herb cohorts
 -> water / carbon / growth simulation: YES

herb seed production -> herb recruitment -> new herb cohorts
 -> native fordyn demographic succession: NO / not implemented in the same way as trees and shrubs
```

Hence MEDFATE has **dynamic herb physiology/growth**, but not yet a complete endogenous herbaceous succession module comparable to woody recruitment.

## Event coupling audit
medfateland outputs a `state` object for every spatial unit and officially supports continuation via `update_landscape()`. This makes interrupted daily/event-loop execution practical.

For Gounsa:
```
geomorph event
 -> DEM / soil-depth / moisture change
 -> edit landscape soil/state
 -> resume growth_land_day / growth_land
```
is architecturally possible.

However, dynamic geomorphic soil-depth change is not plug-and-play:
- MEDFATE stores soil as layer widths plus hydraulic state.
- `soil_redefineLayers()` can change layer widths, but documentation states that initialized hydraulic state variables are lost when layers are redefined.
- `growthInput` also contains root fractions by layer, rhizosphere water state, internal carbon, litter and soil-carbon state.

Therefore an erosion/deposition event that changes soil thickness requires an explicit **state remapping algorithm**:
1. change soil layer widths/depth,
2. conservatively remap soil water and C/N pools,
3. recompute cohort root fractions from Z50/Z95/Z100,
4. preserve internal plant carbon/biomass state,
5. then resume the daily simulation.

This remains a **new coupling**, but the package state architecture makes it substantially more tractable than in LANDIS-II.

## 10–25 m resolution assessment
There is no code-level minimum cell-size restriction identified. Raster cell size is supplied by the user through the `terra` topology.

Computational scaling is the main issue:
- 200 m = 25 cells per km²
- 100 m = 100 cells per km²
- 25 m = 1,600 cells per km²
- 10 m = 10,000 cells per km²

Thus, relative to the 200 m published application, a 25 m grid has 64 times more cells per unit area and a 10 m grid has 400 times more cells per unit area.

medfate 5.0 introduced major speedups and multi-site/watershed C++ runners, and medfateland supports parallel execution, so fine grids are more plausible than in the 2025 application. Nevertheless, 10 m over a large landscape and 100 years of daily growth remains computationally demanding.

Practical Gounsa test order:
1. 25 m vegetation grid first,
2. benchmark 10 m on a small subcatchment,
3. retain 1–5 m geomorph grid separately,
4. only adopt 10 m vegetation if outputs materially differ from 25 m.

## 중요한 한계
1. standard parameterization is Mediterranean
2. tree/shrub demographic succession is complete, but herb recruitment succession is not
3. published applications are much coarser than desired Gounsa cells
4. storm-scale geomorphology remains external
5. erosion/deposition-driven soil-depth changes require new state remapping coupling
6. dynamic root exposure or burial is not native

## current role
**Top-tier candidate for direct technical testing.**
Potentially a better architecture match than BiomeE because the spatial wrapper, seed dispersal, daily state continuation and lateral hydrology already exist.

However, if explicit grass/herb recruitment and replacement through the first postfire decades is mandatory without custom extension, BiomeE/FATES remains stronger biologically.

## key references
- De Cáceres et al. 2023, GMD 16:3165–3201. DOI 10.5194/gmd-16-3165-2023
- Balaguer-Romano et al. 2025, Journal of Environmental Management 395:127844. DOI 10.1016/j.jenvman.2025.127844
- medfate v5.1.0 documentation/source, 2026
- medfateland v3.0.0 documentation, 2026
