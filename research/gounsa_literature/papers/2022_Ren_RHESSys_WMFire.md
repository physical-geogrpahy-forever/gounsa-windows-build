# Ren et al. (2022) — RHESSys-WMFire watershed application

## 서지정보
Ren, J., et al. (2022). Projecting Future Fire Regimes in a Semiarid Watershed of the Inland Northwestern United States: Interactions Among Climate Change, Vegetation Productivity, and Fuel Dynamics. *Earth's Future*. https://doi.org/10.1029/2021EF002518

## 이 논문을 검색한 이유
actual mountain watershed, distributed vegetation, topography, lateral water flow and fire dynamics를 함께 계산하는 모델이 고운사의 criterion 4/5와 얼마나 가까운지 확인하기 위해 검토했다.

## 적용환경
Trail Creek watershed, inland northwestern US.

## 공간구조
- 10 m DEM aggregated to 100 m
- 72 sub-basins
- 16,705 patches
- evergreen, shrub, grass, deciduous and nonvegetated types
- explicit elevation, slope, aspect and watershed hierarchy

## 핵심과정
- daily ecohydrology
- soil moisture and ET
- vegetation productivity
- C/N
- lateral downslope water redistribution
- fire spread and fire effects

## 고운사 의미
criterion 3, 4, 5의 excellent precedent.
산지 유역에서 distributed vegetation-water-fire interaction은 충분히 현실적인 architecture임을 보여준다.

## 결정적 한계
Vegetation types are spatially initialized strata/classes.
Natural recruitment and dynamic creation/replacement of herb/shrub/tree demographic cohorts is not the core mechanism.

## 최종 판정
**spatial ecohydrology benchmark로 유지. Primary succession engine은 아님.**
