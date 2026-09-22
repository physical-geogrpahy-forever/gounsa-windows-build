# 서지정보
Maréchaux, I., Fischer, F. J., Schmitt, S., & Chave, J. (2025). TROLL 4.0: representing water and carbon fluxes, leaf phenology, and intraspecific trait variation in a mixed-species individual-based forest dynamics model - Part 1: Model description. Geoscientific Model Development, 18, 5143-5204. DOI: 10.5194/gmd-18-5143-2025

# 이 논문을 찾은 이유
LiDAR 기반 1 m급 공간구조와 root biomass를 동시에 가진 최신 개체목 모델이 고운사 주 식생모델 후보가 될 수 있는지 검토했다.

# 연구 유형
- 수치모델
- spatially explicit individual-based forest dynamics model

# 공간 구조
- individual trees in explicit 3D space
- aboveground virtual space at 1 m resolution
- configurable belowground voxels and soil layers
- explicit spatial seedling bank

# 적용 환경
- 현재 검증은 주로 열대림
- mixed-species forest dynamics

# 핵심 과정
- photosynthesis
- respiration
- carbon allocation
- leaf phenology
- water balance
- fine-root production
- vertical root distribution
- seed production/dispersal
- recruitment
- mortality

# 식생 입력
- individual trees
- leaf biomass
- wood biomass
- fine-root biomass
- root depth
- root biomass by soil layer
- NSC
- litterfall flux

# 핵심 식
Root depth:
RD = 0.35 * dbh^0.54

Fine-root biomass in soil layer l:
RB_l = RB_t [exp(-3 z_l/RD) - exp(-3 z_(l+1)/RD)]

Total fine-root biomass is currently assumed equal to leaf biomass.

# 파라미터와 단위
- aboveground horizontal resolution: 1 m
- root depth: m
- root biomass: g
- DBH-based individual allometry

# 원 논문의 구현 범위
forest structure, diversity, carbon/water flux, phenology and individual-tree dynamics.

# 고운사에 직접 사용할 수 있는 부분
- 1 m spatial structure
- explicit individual trees
- root depth and root biomass by soil layer
- direct comparison with airborne/terrestrial LiDAR
- spatial seedling bank
- high-frequency ecosystem water/carbon flux

# 새로운 coupling이 필요한 부분
- temperate Korean species calibration
- wildfire module
- dead-root pool after fire
- surface litter mass/decomposition
- horizontal root spread
- geomorph soil-depth updates

# 한계
- current validation primarily tropical
- total fine-root biomass is assumed equal to leaf biomass
- roots do not spread horizontally between belowground voxels
- litter decomposition, wood decay and nutrient mineralization are future developments
- mature wildfire disturbance module is not part of TROLL 4.0 as described

# 최종 판정
- 보조근거 / 강한 구조 비교후보
- LiDAR and root-profile representation are excellent
- whole-process Gounsa vegetation engine으로는 fire/litter limitations 때문에 SEIB보다 낮게 평가

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-18-5143-2025
