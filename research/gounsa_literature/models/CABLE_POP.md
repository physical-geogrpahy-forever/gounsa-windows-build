# CABLE-POP

업데이트: 2026-09-23

## 검토 이유
Subdaily land-surface physics와 demographic cohort를 함께 가진 후보로서 고운사 5조건을 적용했다.

## 구조
- CABLE biophysics: sub-diurnal radiation, photosynthesis, transpiration, energy balance, 6-layer soil water/heat
- CASA-CNP: daily C/N/P biogeochemistry, leaf/stem/fine-root allocation and litter
- POP: woody stand-age/size cohorts, establishment, mortality and disturbance
- POP demographic timestep: 1 year

## 5조건
1. spatial cohort: PARTIAL. Grid/patch 내부 woody cohorts이며 식물 x-y 위치는 없다.
2. understory succession: WEAK. POP는 woody demography용이며 최근 비교문헌에서도 vegetation type 간 competition을 모의하지 않는 것으로 정리된다. 초본-관목-교목의 명시적 postfire succession이 없다.
3. soil/geomorph coupling: local layered soil physics는 강하나 현재 shortlist보다 특별히 유리하지 않다.
4. catchment/topography: land-surface 적용 전례는 많지만 criterion 2와 5의 약점을 상쇄할 fine mountain demographic precedent는 확인하지 못했다.
5. fast timestep: biophysics subdaily, CASA-CNP daily이지만 POP demography는 annual.

## 최종 판정
**Production vegetation-engine 후보에서 제외.**

Subdaily physiology가 있더라도 woody-only annual demography이면 사용자의 하층식생/천이 기준을 충족하지 못한다는 비교사례로 유지한다.

## 핵심 참고
- Haverd et al. 2014, Biogeosciences 11:4039-4055, POP demographic model.
- Haverd et al. 2018, GMD 11:2995-3026, CABLE + POP integration.
- Tschumi et al. 2023, JGR Biogeosciences model comparison.
