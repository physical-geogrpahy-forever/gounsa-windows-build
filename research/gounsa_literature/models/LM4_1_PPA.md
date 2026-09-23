# GFDL LM4.1 / LM3-PPA lineage

## 왜 검토했는가
고운사 5조건을 모두 만족할 수 있는 다른 demographic land-surface model이 LPJ-GUESS/FATES 외에 있는지 확인하기 위해 검토했다.

## 식생 구조
- PPA (Perfect Plasticity Approximation) cohort vegetation demography
- 한 tile 안에 여러 vegetation cohort와 여러 canopy layer
- cohort는 vegetation type, size, rooting depth, age 등을 공유하는 식물 집단
- tree와 C3/C4 grass를 명시적으로 모의
- recruitment, mortality, fire disturbance, tile succession

## 시간 구조
- land-surface energy/water/CO2: 30 min
- cohort biomass/growth/mortality: daily
- fire: daily
- 일부 land-use structural change: annual

## 뿌리/토양
- cohort-specific fine-root biomass and rooting depth
- soil layers와 연결된 root water uptake
- root, xylem, leaf hydraulic resistance
- 각 cohort가 물 경쟁
- hydrology/soil carbon vertically layered

## 지형수문
LM4.1은 sub-grid tile별 soil column과 characteristic hillslope 개념을 통해 groundwater lateral flow와 recharge/discharge를 표현하고 grid-scale river/lake routing도 갖는다.

하지만 이는 고운사에서 원하는 실제 LiDAR DEM의 10-50 m geographic hillslope cells와는 다르다. 실제 fine terrain topology가 아니라 ESM sub-grid parameterization이다.

## 하층식생/천이
장점:
- multi-layer canopy
- seedling/understory plants가 plant hydraulics와 경쟁의 영향을 받음
- tree/grass competition과 fire recovery 가능

한계:
- 기본 PFT set은 tree + C3/C4 grass 중심
- 독립 shrub layer가 약함
- 한국 산불 후 `초본 -> 관목 -> 교목` 천이를 species/PFT-rich하게 표현하려면 확장 필요

## 5조건
| 기준 | 판정 |
|---|---|
| 1 공간명시 cohort | STRONG cohort, but spatial tiles are sub-grid/statistical rather than fine GIS terrain cells |
| 2 하층식생과 천이 | PARTIAL-STRONG: grass + seedlings explicit, shrub diversity weak |
| 3 soil/terrain coupling | STRONG soil/root hydraulics, but external geomorph state interface not demonstrated |
| 4 유역/지형 | PARTIAL: characteristic hillslope groundwater + river routing, not fine mapped catchment precedent |
| 5 <=daily | VERY STRONG: 30 min land physics, daily cohort growth/fire |

## 현재 판정
**강한 demographic land-surface 비교모델이지만 고운사 최상위 후보는 아님.**

LPJ-GUESS spatial branches나 FATES에 비해 약한 부분은 시간해상도가 아니라 실제 fine terrain spatiality와 shrub-rich understory succession이다.

## 핵심 문헌
Shevliakova et al. (2024). The Land Component LM4.1 of the GFDL Earth System Model ESM4.1. Journal of Advances in Modeling Earth Systems. DOI: 10.1029/2023MS003922
Weng et al. (2015). Scaling from individual trees to forests in an Earth system modeling framework using a mathematically tractable model of height-structured competition. Biogeosciences, 12, 2655-2694.
