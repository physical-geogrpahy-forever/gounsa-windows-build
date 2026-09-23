# Haverd et al. (2018) — CABLE-POP

## 서지정보
Haverd, V., Smith, B., Nieradzik, L. P., et al. (2018). A new version of the CABLE land surface model (Subversion revision r4601) incorporating land use and land cover change, woody vegetation demography, and a novel optimisation-based approach to plant coordination of photosynthesis. *Geoscientific Model Development*, 11, 2995–3026. https://doi.org/10.5194/gmd-11-2995-2018

## 이 논문을 검색한 이유
subdaily land-surface physics와 woody cohort demography를 함께 가지므로 고운사 5조건의 잠재 후보인지 확인하기 위해 검토했다.

## 연구 유형
land-surface model + woody demographic module development.

## 공간구조
CABLE grid/tile 안에서 POP가:
- disturbance-age patches
- age/size tree cohorts
를 사용한다.

POP patch는 면적분율이며 x-y가 지정된 실제 patch가 아니다.

## 핵심과정
CABLE:
- sub-diurnal radiation, energy, photosynthesis, transpiration
- six-layer soil heat/water
- daily CASA-CNP biogeochemistry

POP:
- cohort establishment
- age/size structure
- light/resource competition among tree cohorts
- mortality
- disturbance-mediated landscape heterogeneity

## 시간
결정적 한계:
**POP demographic timestep = 1 year.**

따라서 CABLE의 water/energy process가 subdaily여도 vegetation cohort structure가 폭우 이후 하루 내 갱신되는 모델은 아니다.

## 하층식생/천이
CABLE 자체에는 woody와 herbaceous PFT가 있으나 POP는 woody demography module이다.

Published CABLE-POP configurations에서는:
- tree demography는 explicit
- natural grass/shrub/tree PFT replacement는 FATES/RED 수준의 endogenous succession으로 구현되지 않음
- 일부 global applications은 PFT 분포를 prescribed하고 natural dynamic vegetation을 계산하지 않음

## 토양/지형
CABLE soil water physics는 강하지만 criterion 5와 2의 부족을 상쇄하지 못한다.

## 고운사 5조건 판정
- spatial cohort: PARTIAL
- explicit understory succession: WEAK
- soil coupling: STRONG
- watershed/topography: secondary
- <=daily demographic timestep: **NO**

## 최종 판정
**production vegetation engine 후보에서 제외.**
Efficient woody-demography comparator로만 유지.
