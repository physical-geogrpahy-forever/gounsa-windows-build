# 서지정보
Moustakas, A., Sakkos, K., Wiegand, K., Ward, D., Meyer, K. M., & Eisinger, D. (2009). Are savannas patch-dynamic systems? A landscape model. Ecological Modelling, 220(24), 3576–3588. https://doi.org/10.1016/j.ecolmodel.2009.06.036

# 이 논문을 찾은 이유
교목, 관목, 초본을 동시에 공간격자에서 계산하고 soil depth/soil moisture와 daily vegetation response를 결합한 간단한 spatial model이 존재하는지 확인하기 위해 검토했다.

# 연구 유형
- spatially explicit individual/grid-based savanna vegetation model
- conceptual/process model

# 공간 구조
- 100 x 100 cells
- published simulation에서 한 cell은 약 3 km x 3 km
- tree와 bush는 individual basis
- grass는 biomass state
- 각 cell마다 soil depth, porosity, soil moisture 및 life-form biomass/state를 계산

# 적용 환경
- arid savanna
- mesic savanna
- shallow vs deeper soil parameterizations
- landscape-scale patch dynamics

# 핵심 과정
- precipitation and soil-moisture dynamics
- germination
- growth
- mortality
- tree/bush/grass competition for soil moisture
- fire
- grazing/browsing
- woodcutting
- seasonal restrictions
- heterogeneous soil depth and porosity

# 식생 및 토양 상태
- individual tree/bush size and age
- grass biomass
- cell soil depth
- cell soil porosity
- soil moisture
- precipitation

# 시간 구조
- vegetation cells updated daily
- tree, bush and grass growth can respond daily to soil moisture and season
- simulations extended to more than 2000 years

# 핵심 식 또는 규칙
life-form별 maximum biomass는 precipitation과 soil depth에 의해 제한된다.

개념적으로 tree의 경우:
```
max_tree_mass <= C_t * Z * R
```

여기서
- C_t: water-biomass conversion efficiency factor
- Z: soil depth
- R: average annual precipitation

유사한 구조가 bush와 grass에도 적용된다.

# 고운사에 사용할 수 있는 부분
- `tree + shrub + grass + soil moisture + soil depth + daily update`라는 최소 구조가 2009년에도 spatial vegetation model로 구현 가능했음을 보여주는 benchmark
- full individual-tree forest physiology가 없어도 life-form succession/competition을 daily soil water와 연결하는 간단한 구조의 선례

# 필요한 새로운 coupling
- 10–50 m terrain cells로 공간규모 축소
- actual DEM routing and lateral water flow
- forest canopy/light structure
- litter/root biomass pools
- external soil-water overwrite and dynamic soil-geometry remapping
- temperate postfire parameterization
- seed dispersal implementation

# 한계
- cell size가 약 3 km로 고운사 target보다 매우 큼
- savanna ecology를 위한 모델
- seed dispersal and seed longevity를 명시적으로 포함하지 않음
- soil depth/porosity는 simulation 동안 고정
- hillslope/catchment routing을 모의하지 않음
- woody vegetation은 full forest canopy cohorts가 아니라 individual life-form representation

# 다섯 기준 판정
1. spatial cohort/hybrid: **STRONG-PARTIAL**. real grid + woody individuals + grass biomass이지만 cohort-light forest architecture는 아님.
2. explicit understory succession: **STRONG life-form level**. tree, bush, grass가 명시적으로 경쟁하나 species-rich temperate understorey는 아님.
3. soil-state coupling: **MODERATE locally**. soil moisture/depth가 직접 성장에 영향을 주지만 external state-exchange precedent는 없음.
4. terrain/catchment precedent: **FAIL/PARTIAL**. heterogeneous landscape는 있으나 DEM/routed catchment가 아님.
5. <= daily: **YES**.

# 최종 판정
- production shortlist를 바꾸지 않음
- aDGVM2보다 단순하고 오래된 savanna benchmark
- `daily soil water -> tree/shrub/grass dynamics` 구조를 입증하는 보조근거

# 참고 링크 / DOI
- https://doi.org/10.1016/j.ecolmodel.2009.06.036
