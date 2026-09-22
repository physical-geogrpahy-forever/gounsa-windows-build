# 서지정보
Rouet, C., Davi, H., Druel, A., Fady, B., & Morin, X. (2025). PDG-Arena: an ecophysiological model for characterizing tree-tree interactions in heterogeneous and mixed stands. Annals of Forest Science, 82, 8. DOI: 10.1186/s13595-025-01277-8

# 이 논문을 찾은 이유
CASTANEA 기반의 최신 spatially explicit individual-tree process model이 HETEROFOR보다 고운사 LiDAR 결합에 유리한지 비교하기 위해 검토했다.

# 연구 유형
- 수치모델
- individual/process-based mixed forest model

# 공간 구조
- individual trees spatially explicit
- SamsaraLight 3D ray tracing
- stand 규모

# 적용 환경
- French Prealps
- beech-fir monospecific and mixed stands

# 핵심 과정
- photosynthesis
- transpiration
- carbon allocation
- light competition
- water competition
- growth
- PDG lineage의 survival/reproduction 가능성

# 식생 입력
- explicit tree inventory
- crown structure
- CASTANEA ecophysiological parameters

# 핵심 식
CASTANEA의 ecophysiology를 tree scale로 내려 individual crowns에 적용한다.

# 파라미터와 단위
- hourly transpiration
- daily precipitation forcing
- small stands, generally <1 ha in current evaluation

# 원 논문의 구현 범위
mixed-stand individual tree growth and ecological interactions.

# 고운사에 직접 사용할 수 있는 부분
- temperate beech/fir ecology
- explicit tree coordinates
- fine physiological time steps
- LiDAR crown initialization potential

# 새로운 coupling이 필요한 부분
- spatially differentiated soil water
- detailed root/litter/deadroot interface
- wildfire/postfire
- geomorphic soil changes

# 한계
현재 PDG-Arena의 물 경쟁은 나무 위치와 토심을 구분하지 않는 stand-wide common soil-water pool을 사용한다. 고운사 LiDAR 사면에서 slope position과 local soil moisture feedback을 모의하기에는 HETEROFOR individual-pedon option보다 불리하다.

# 최종 판정
- 보류/보조근거
- 주 식생엔진으로 HETEROFOR보다 우선하지 않음

# 참고 링크 / DOI
https://doi.org/10.1186/s13595-025-01277-8
