# MEDFATE + medfateland

## 현재 판정
BiomeE/BiomeEP와 유사한 cohort process model을 **실제 GIS 공간단위로 확장한 가장 직접적인 공개 구현 사례 중 하나**.

## 식생 표현
MEDFATE:
- tree cohorts
- shrub cohorts
- optional herbaceous layer
- seed bank / seedling bank
- cohort-specific fine-root depth distribution
- daily water/carbon/growth
- annual recruitment and forest dynamics

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

2026 MEDFATELAND catchment preprint:
- distributed vegetation-hydrology interactions
- two Spanish catchments
- 500 m grid in that application
- confirms spatial distributed ecohydrological use

Package documentation examples include 100 m and 200 m watershed grids. Cell size is a user-defined raster topology choice, not a hard-coded 200/500 m limit, although fine resolution causes computational cost.

## 중요한 장점 for Gounsa
1. cohort-based, not individual-tree
2. actual geographic cells rather than statistical disturbance patches
3. dynamic tree and shrub understory
4. daily water/carbon/growth
5. vertical fine-root distribution by cohort
6. seed dispersal among spatial units
7. lateral water transfer among cells
8. one-day simulation functions allow external event loop control
9. state objects can be continued into subsequent calls
10. R ecosystem: sf, terra and parallelization align with current workflow

## 중요한 한계
1. standard parameterization is Mediterranean
2. woody cohorts are the main forest-dynamics state; herbs are supported in stand description/water balance but not demonstrated as equally complete long-term demographic cohorts
3. published applications are 200–500 m, much coarser than the desired Gounsa geomorph grid
4. storm-scale geomorphology remains external
5. erosion/deposition-driven soil-depth changes need new coupling/state remapping
6. no evidence yet that dynamic root exposure or burial is native

## event coupling potential
medfateland provides one-day functions:
```
geomorph event
 -> update DEM / soil depth / moisture
 -> update sf/soil/forest state
 -> growth_land_day / spwb_land_day
 -> next event/day
```
This is much closer to the required Gounsa control structure than monthly LANDIS-II NECN.

For sub-day storms, geomorphology remains hourly/subhourly while vegetation state can be updated after the event and resumed at daily steps.

## understory caution
Tree and shrub understory are dynamic in MEDFATE forest dynamics.
The herbaceous layer exists and can include species-specific herb cohorts, but current `fordyn` state-variable documentation identifies woody cohorts (trees/shrubs) as the main dynamic forest state. Therefore **full herbaceous succession should not yet be claimed as solved**.

## current role
**Top-tier candidate for direct technical testing.**
Potentially a better architecture match than BiomeE because the spatial wrapper, seed dispersal and lateral hydrology already exist.

## key references
- De Cáceres et al. 2023, GMD 16:3165–3201. DOI 10.5194/gmd-16-3165-2023
- Balaguer-Romano et al. 2025, Journal of Environmental Management 395:127844. DOI 10.1016/j.jenvman.2025.127844
- medfateland v3.0.0 documentation, 2026
