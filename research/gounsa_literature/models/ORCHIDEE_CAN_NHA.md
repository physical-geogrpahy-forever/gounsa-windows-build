# ORCHIDEE-CAN / ORCHIDEE-CAN-NHA

## 왜 검토했는가
수목 size cohort와 subdaily land-surface hydrology를 동시에 가진 모델이 고운사의 5조건에 맞는지 확인했다.

## 구조
- forest stand demography represented by up to ~20 tree cohorts/diameter classes
- cohort recruitment, allocation, self-thinning mortality
- vertically discretised canopy energy and radiation
- mechanistic plant hydraulics in CAN-NHA

## 시간해상도
- SECHIBA water/energy/photosynthesis: 30 min
- vegetation C allocation, mortality, recruitment, phenology, litter: daily

## 토양/뿌리
- dynamic root-water uptake
- soil-to-root-to-stem-to-leaf water potentials and hydraulic resistances
- drought/cavitation mortality extensions

## 하층식생
**주요 약점.**
ORCHIDEE-CAN의 multi-layer canopy가 sub-canopy microclimate를 계산한다고 해서 독립적인 understory succession model인 것은 아니다.

Published evaluation explicitly treated overstory and understory as the same species and noted that understory-specific phenology/traits were not represented and would require future different PFT/species treatment.

따라서:
- vertical canopy physics: strong
- independent herb/shrub population dynamics: weak
- postfire herb -> shrub -> tree succession: not adequate natively

## 공간/지형
주 적용은 site/grid scale land-surface simulation. Fine mapped catchment lateral hydrology precedent was not identified in this screening.

## 5조건
| 기준 | 판정 |
|---|---|
| 1 spatial cohort | PARTIAL: tree size cohorts but no fine actual terrain topology |
| 2 understory succession | WEAK |
| 3 soil coupling | STRONG local plant-soil hydraulics |
| 4 catchment/topography | WEAK-PARTIAL |
| 5 <=daily | VERY STRONG, 30 min + daily demography |

## 현재 판정
**탈락 from strict shortlist.**
시간해상도와 tree hydraulics는 매우 좋지만 criterion 2가 고운사 목적과 맞지 않는다.

## key references
- Naudts et al. 2015, GMD 8:2035-2065.
- Chen et al. 2016, GMD 9:2951-2972.
- Yao et al. 2022, GMD 15:7809-7839, ORCHIDEE-CAN-NHA r7236.
