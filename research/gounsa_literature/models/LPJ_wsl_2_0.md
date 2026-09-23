# LPJ-wsl v2.0 age-class demography

업데이트: 2026-09-23

# 왜 검토했는가
LPJ 계열이면서 LPJ-GUESS SEC와 다른 계산효율 높은 age-class implementation이 고운사 vegetation engine이 될 수 있는지 확인했다.

# 핵심 구조
Calle & Poulter (2021):
- ecosystem age-class distributions
- fire
- land abandonment
- wood harvesting
- age-dependent stocks and fluxes
- global DGVM grid-cell framework

Age classes는 grid cell 내부의 subarea age distribution을 추적하는 방식이다.

# 고운사 5개 기준 판정
| 기준 | 판정 | 이유 |
|---|---|---|
| 1 spatial cohort | **PARTIAL** | demographic age classes는 있으나 actual fine x-y terrain cohort가 아님 |
| 2 understory succession | **WEAK-PARTIAL** | 고운사식 explicit herb/shrub/tree understory succession이 핵심이 아님 |
| 3 external soil-terrain coupling | PARTIAL | LPJ soil-water processes는 있으나 PF-LPJG 수준의 직접 state-exchange precedent가 아님 |
| 4 hillslope/catchment | **WEAK** | global grid-oriented, strict fine catchment precedent 없음 |
| 5 fast ecosystem processes | broadly compatible | 그러나 age-class framework 자체가 event-scale spatial coupling을 해결하지 않음 |

# LPJ-GUESS SEC와 비교
고운사 기준에서는 LPJ-wsl v2.0가 LPJ-GUESS SEC + PF-style coupling보다 유리하지 않다.

LPJ-GUESS lineage에는 이미:
- tree age/size cohorts
- shrub/grass PFT
- SEC canopy/gap structure
- recruitment layer
- 50 m catchment precedent
- ParFlow hourly + LPJ daily external hydrology coupling
이 존재한다.

따라서 LPJ-wsl의 age-class simplicity만으로 현재 후보를 교체할 이유가 없다.

# 새로운 coupling이 필요한 부분
- actual fine terrain representation
- explicit postfire herb/shrub/tree demographic succession
- lateral hydrology
- geomorphic state overwrite/remapping

# 관련 논문
- `papers/2021_Calle_LPJwsl_AgeClasses.md`

# 최종 판정
**탈락 / global age-class comparator**

LPJ-GUESS SEC/PF route보다 우선하지 않는다.
