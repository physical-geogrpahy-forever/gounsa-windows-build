# 서지정보
Clason, A. J., Farnell, I., & Lilles, E. B. (2022). Carbon 5-60 Years After Fire: Planting Trees Does Not Compensate for Losses in Dead Wood Stores. Frontiers in Forests and Global Change, 5, 868024. DOI: 10.3389/ffgc.2022.868024

# 이 논문을 찾은 이유
SORTIE-ND가 실제로 산불 이후 수십-100년 산림회복 모의에 사용된 선례가 있는지 확인하기 위해 검토했다.

# 연구 유형
- 산불 후 현장 chronosequence + forest simulation
- spatially explicit individual-based forest dynamics

# 공간 구조
- SORTIE-ND individual trees
- 각 나무의 위치와 life stage를 명시
- 4 ha simulated stand에서 중앙 1 ha 분석

# 적용 환경
- British Columbia sub-boreal forests
- 5-60 years since wildfire
- lodgepole pine, spruce, subalpine fir, trembling aspen 등

# 핵심 과정
- seedling/sapling/adult initialization
- establishment
- growth
- mortality
- neighbourhood competition
- 100 years since fire까지 stand projection

# 식생 입력
- stems per hectare by DBH class
- seedling height classes
- species-specific establishment/growth/mortality parameters

# 핵심 식
SORTIE-ND의 species- and size-specific neighbourhood growth, establishment and mortality equations을 이용한다.

# 고운사에 직접 사용할 수 있는 부분
- 산불 후 100년 forest recovery를 SORTIE-ND로 모의한 실제 선례
- 개별목 기반 postfire regeneration trajectory
- LiDAR tree-map 초기조건과 구조적으로 호환 가능

# 새로운 coupling이 필요한 부분
- fire severity를 개별목/seedling mortality로 초기화
- root biomass and turnover
- soil-water/soil-depth feedback
- litter/dead-root geomorphic interface

# 한계
이 연구는 fire-spread model을 SORTIE-ND 내부에서 돌린 것이 아니라 산불 이후 관측된 stand를 초기화해 회복을 모의했다. 따라서 native wildfire process의 근거가 아니다.

# 최종 판정
- 보조근거
- postfire forest succession 선례는 강함
- root/hydrology interface 부족 때문에 HETEROFOR보다 우선하지 않음

# 참고 링크 / DOI
https://doi.org/10.3389/ffgc.2022.868024
