# 서지정보
Schumacher, S., Bugmann, H., & Mladenoff, D. J. (2004). Improving the formulation of tree growth and succession in a spatially explicit landscape model. Ecological Modelling, 180(1), 175–194. https://doi.org/10.1016/j.ecolmodel.2003.12.055

# 이 논문을 찾은 이유
BiomeE/BiomeEP와 같은 cohort vegetation concept이 실제 fine raster landscape cells에서 spatially linked succession으로 구현된 선례를 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- spatial forest landscape model

# 공간 구조
- spatially explicit raster landscape
- standard LandClim stand cells: 25 m x 25 m
- cell 간 seed dispersal and disturbance linkage

# 적용 환경
- European Alps mountain forests
- climate/topography/soil gradients

# 핵심 과정
- recruitment
- growth
- mortality
- competition among species-age cohorts
- climate and edaphic limitation
- seed dispersal
- fire/wind/management extensions

# 식생 입력
- species-age cohorts
- cohort mean individual biomass
- stem number
- derived DBH and stand structure

# 핵심 식
FORCLIM/gap-model concepts를 단순화하여 cohort growth, competition and succession을 25 m cells에 적용한다.

# 파라미터와 단위
- stand process: annual
- climate includes monthly temperature/drought inputs
- standard cell: 25 m x 25 m

# 원 논문의 구현 범위
각 geographic raster cell이 실제 forest stand state를 가지며 cohorts가 cell 내부에서 성장하고, cells are linked by dispersal/disturbances.

# 고운사에 직접 사용할 수 있는 부분
- genuine geographic cohort cells
- mountain topography precedent
- 25 m fine landscape scale
- explicit seed dispersal between cells

# 새로운 coupling이 필요한 부분
- daily/event water and geomorphic feedback
- roots/litter quantitative state
- understory herbs/shrubs

# 한계
- tree-focused
- annual vegetation dynamics too coarse for direct storm coupling
- root/litter/understory state insufficient for Gounsa geomorphic feedback

# 최종 판정
- 보조근거
- spatial cohort architecture precedent, not final vegetation engine

# 참고 링크 / DOI
https://doi.org/10.1016/j.ecolmodel.2003.12.055
