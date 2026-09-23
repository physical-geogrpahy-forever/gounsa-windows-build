# 서지정보
Blanco, C. C., Scheiter, S., Sosinski, E., Fidelis, A., Anand, M., & Pillar, V. D. (2014). Feedbacks between vegetation and disturbance processes promote long-term persistence of forest-grassland mosaics in south Brazil. Ecological Modelling, 291, 224–232. https://doi.org/10.1016/j.ecolmodel.2014.07.024

# 이 논문을 찾은 이유
aDGVM 계열에 실제 geographic spatialization, topographic heterogeneity, seed dispersal 및 disturbance spread가 구현된 선례가 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- spatially explicit extension of aDGVM

# 공간 구조
- 2D spatially explicit landscape
- vegetation patches/cells
- seed dispersal between spatial units
- fire spread and spatial connectivity

# 적용 환경
- South Brazil forest-grassland mosaics
- topographically heterogeneous landscape

# 핵심 과정
- grass-tree competition
- topographic heterogeneity
- seed dispersal
- fire spread
- patch connectivity
- forest expansion and grassland persistence

# 식생 입력
- aDGVM vegetation states
- grass biomass
- forest/woody state
- topography
- spatial seed dispersal and fire parameters

# 핵심 식
본 검토의 핵심은 공간 구조이다. 기존 aDGVM을 spatially explicit 2D approach에 넣어 topography, seed dispersal, fire spread의 상호작용을 계산한다.

# 파라미터와 단위
- landscape spatial configuration
- topography
- seed dispersal
- fire spread
- exact cell size와 transition parameter는 production 적용 전 원문 재확인 필요

# 원 논문의 구현 범위
- spatially explicit vegetation-disturbance feedback
- topographic heterogeneity
- long-term forest-grassland mosaic dynamics

# 고운사에 직접 사용할 수 있는 부분
- criterion 4의 분명한 topographic distributed-landscape precedent
- seed dispersal and disturbance spread를 actual space에 넣은 선례
- geomorphic cells와 vegetation geography를 연결하는 개념적 참고

# 새로운 coupling이 필요한 부분
- aDGVM2의 더 발전한 shrub/trait/hydraulic ecology를 이 2D branch에 통합
- lateral hillslope hydrology
- external soil-moisture/state exchange
- erosion/deposition soil-layer remapping

# 한계
- 이 논문은 aDGVM2의 최신 생리/수리학 branch가 아니라 기존 aDGVM의 spatial extension이다.
- topography는 vegetation-fire heterogeneity에 쓰이지만 watershed lateral hydrology를 계산하지 않는다.
- 따라서 2D-aDGVM과 최신 aDGVM2 기능을 하나의 published ready-made model로 간주하면 안 된다.

# 최종 판정
- 채택: spatial precedent
- production engine 자체가 아니라 aDGVM lineage의 criterion-4 근거

# 참고 링크 / DOI
- https://doi.org/10.1016/j.ecolmodel.2014.07.024
