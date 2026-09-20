# RillGrow lineage

## 핵심 문헌
Eltner et al. (2025), SOIL, DOI 10.5194/soil-11-413-2025, plus older RillGrow lineage.

## 고운사에서 검토한 이유
independent numerical lineage where rill initiation and network growth emerge from local flow/erosion rather than a prescribed rill mask.

## 공간구조
- cellular automaton
- raster microtopography
- steepest-direction/D8 local flow routing
- plot scale

## processes
- infiltration
- splash redistribution
- flow erosion/deposition
- rill initiation/growth
- sidewall slumping/toppling
- multi-grain clay/silt/sand

## vegetation
Current lineage is primarily bare-soil.
No dynamic root biomass/RLD vegetation module.

## 고운사에 쓸 수 있는 부분
- emergent-rill network benchmark
- independent comparison against McGuire and Wu

## 한계
- D8 local routing, not genuine 2D SWE
- plot scale
- bare-soil emphasis
- mountain-domain scaling uncertain

## 새로운 coupling
vegetation/root effects added to RillGrow erodibility are **new coupling**.

## 최종 판정
**rill-network comparison lineage, not final engine.**
