# 서지정보
Maréchaux, I., Fischer, F. J., Schmitt, S., & Chave, J. (2025). TROLL 4.0: representing water and carbon fluxes, leaf phenology, and intraspecific trait variation in a mixed-species individual-based forest dynamics model - Part 1: Model description. Geoscientific Model Development, 18, 5143-5204. https://doi.org/10.5194/gmd-18-5143-2025

# 이 논문을 찾은 이유
LiDAR를 이용해 수 m 이하의 식생-지형 피드백을 구성할 수 있다는 조건에서, 개별목과 뿌리 및 토양수분을 매우 세밀하게 공간화한 공개 산림모델 후보인지 검토했다.

# 연구 유형
- 수치모델
- individual-based forest dynamics model

# 공간 구조
- typical stand: 1-100 ha
- aboveground: 1 m x 1 m x 1 m voxels
- belowground: configurable coarser horizontal grid and finer vertical layers
- spatially explicit seedling bank at 1 m ground sites
- within-stand topography is assumed flat

# 적용 환경
- tropical forest
- evaluated at Amazonian sites
- future temperate/boreal transfer discussed but not implemented as a validated standard use

# 핵심 과정
- individual-tree growth and mortality
- light transfer
- carbon balance
- soil water balance
- root water uptake
- leaf phenology
- seed production/dispersal/recruitment

# 식생 입력
- individual-tree traits
- leaf biomass
- fine-root biomass
- rooting depth
- root biomass by soil layer
- seed bank
- crown/3D structure

# 핵심 식
Rooting depth:
RD = 0.35 * dbh^0.54

Fine-root biomass in soil layer l:
RB_l = RB_t * [exp(-3 z_l / RD) - exp(-3 z_(l+1) / RD)]

이 식에서는 약 95%의 fine-root biomass가 지표에서 RD 사이에 위치하도록 한다.

# 파라미터와 단위
- aboveground voxel: 1 m3
- seed bank: 1 m x 1 m ground cells
- RD: m
- RB: g
- root length density is derivable in the water-uptake module

# 원 논문의 구현 범위
fine-scale tropical forest structure, carbon, water, roots and recruitment.

# 고운사에 직접 사용할 수 있는 부분
- LiDAR/remote-sensing 3D structure와 직접 비교 가능한 1 m canopy representation
- fine-root biomass와 vertical distribution을 명시적으로 제공
- root length density 계산 계보
- spatial seedling bank
- belowground soil-water voxels

# 새로운 coupling이 필요한 부분
- temperate East Asian species/PFT parameterization
- slope/topography
- wildfire disturbance
- litter/deadwood decomposition
- geomorphic erosion and soil-depth feedback

# 한계
- 현재 모델은 tropical forest 중심
- stand topography flat
- root horizontal spread는 belowground voxel 사이에 표현하지 않음
- total fine-root biomass를 leaf biomass와 같다고 가정
- litter decomposition, wood decay, nutrient mineralization은 future development로 명시
- fire regime/disturbance module도 현재 완성 기능으로 제시되지 않음

# 최종 판정
- 강한 비교후보
- LiDAR/뿌리 공간구조만 보면 매우 우수
- 고운사 주모델로는 fire, litter/deadwood, temperate parameterization, topography 부재 때문에 보류

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-18-5143-2025
