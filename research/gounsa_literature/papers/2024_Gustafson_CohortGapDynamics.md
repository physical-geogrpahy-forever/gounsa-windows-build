# 서지정보
Gustafson, E. J., Sturtevant, B. R., Miranda, B. R., & Duveneck, M. J. (2024). Overcoming conceptual hurdles to accurately represent trees as cohorts in forest landscape models. Ecological Modelling, 490, 110657. https://doi.org/10.1016/j.ecolmodel.2024.110657

# 이 논문을 찾은 이유
고운사에서 개별목보다 계산량이 적으면서 일반적인 landscape cohort보다 실제 공간점유와 gap dynamics를 더 잘 표현하는 중간 구조가 가능한지 확인하기 위해 검토했다.

# 연구 유형
- 방법론
- cohort-based forest landscape model 개선
- LANDIS-II PnET-Succession 사례

# 공간 구조
- raster forest landscape cells
- species-age cohorts
- cohort별 proportional canopy occupancy
- open space/gap를 cell 내부 상태로 계산

# 적용 환경
- forest landscape modelling
- 예시 case는 northern Wisconsin forest site

# 핵심 과정
- cohort canopy occupancy
- gap formation after mortality/disturbance
- light attenuation
- dynamic canopy layers
- cohort biomass density
- PnET-Succession의 water/light competition

# 식생 입력
- species-age cohorts
- cohort LAI
- species MaxLAI
- cohort biomass/size
- canopy layer
- soil water and light availability

# 핵심 식
논문은 cohort canopy area를 cohort LAI와 MaxLAI의 비로 계산하는 proportional canopy occupancy 접근을 제안한다.

개념적으로:
```
PCanArea_i = LAI_i / MaxLAI_i
```

이를 이용해 cohort가 cell 전체를 항상 점유한다고 가정하지 않고, mortality/disturbance 뒤 생긴 gap을 보존한다.

# 파라미터와 단위
- LAI
- species-specific MaxLAI
- canopy-layer occupancy
- cohort biomass
- exact parameterization은 original PnET-Succession implementation을 재확인해야 함

# 원 논문의 구현 범위
- LANDIS-II PnET-Succession의 tree species-age cohorts
- cell 내부 cohort horizontal occupancy와 gap dynamics 개선
- light attenuation과 cell biomass 계산 개선

# 고운사에 직접 사용할 수 있는 부분
- 사용자가 원하는 "individual tree보다 단순하지만 ordinary cohort보다 공간적으로 나은" 구조의 좋은 방법론적 선례
- LPJ-GUESS SEC의 persistent gap 개념과 비교 가능
- geomorphic grid cell 내부에서 cohort occupancy를 어떻게 해석할지 참고 가능

# 새로운 coupling이 필요한 부분
- explicit herb/shrub demographic understory
- <=daily structural succession
- event-driven geomorphic soil-state feedback
- hillslope lateral hydrology

# 한계
- LANDIS-II/PnET-Succession의 기존 시간해상도 제약을 해결하지 않는다.
- tree cohort canopy 문제를 주로 다루며 postfire herb-shrub-tree full succession 문제를 해결하지 않는다.
- 실제 고운사 production engine 대안이 아니라 cohort representation benchmark다.

# 최종 판정
- 보조근거
- spatial cohort representation benchmark
- current top shortlist를 변경하지 않음

# 참고 링크 / DOI
- https://doi.org/10.1016/j.ecolmodel.2024.110657
