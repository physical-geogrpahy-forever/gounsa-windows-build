# 서지정보
Lischke, H., Zimmermann, N. E., Bolliger, J., Rickebusch, S., & Löffler, T. J. (2006). TreeMig: A forest-landscape model for simulating spatio-temporal patterns from stand to landscape scale. Ecological Modelling, 199(4), 409–420. https://doi.org/10.1016/j.ecolmodel.2005.11.046

# 이 논문을 찾은 이유
spatially explicit cohort/size-class vegetation dynamics with intercell dispersal precedent를 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- spatially explicit forest landscape model

# 공간 구조
- rectangular geographic grid
- each cell contains species-specific height-class distributions
- cells linked by seed dispersal
- flexible cell side length from about 25 m to 1 km in later WSL documentation

# 적용 환경
- Alpine forests
- stand-to-landscape and regional migration simulations

# 핵심 과정
- reproduction
- seed production
- seed-bank dynamics
- germination
- growth
- competition
- mortality
- intercell seed dispersal

# 식생 입력
- species
- height classes
- number/density distribution by height class
- environment-dependent demographic parameters

# 핵심 식
개별목 위치 대신 height-class frequency distributions와 Poisson-distributed within-cell tree density/light를 사용한다.

# 파라미터와 단위
- yearly demographic processes
- published example: 100 m x 100 m cells for local pattern simulation
- regional Alpine example: 1 km x 1 km cells

# 원 논문의 구현 범위
각 geographic cell의 height-structured forest state가 seed dispersal로 연결되어 spatial migration and succession을 만든다.

# 고운사에 직접 사용할 수 있는 부분
- explicit geographic grid with non-individual vegetation classes
- seed bank and seed dispersal
- mountain forest spatial precedent

# 새로운 coupling이 필요한 부분
- root/litter state
- daily/subdaily ecohydrology
- shrub/herb understory
- geomorphic event state update

# 한계
- tree-focused height classes rather than full tree/shrub/grass cohort ecology
- yearly time step
- belowground variables too weak for Gounsa

# 최종 판정
- 보조근거
- spatial cohort architecture precedent, not final Gounsa engine

# 참고 링크 / DOI
https://doi.org/10.1016/j.ecolmodel.2005.11.046
