# 서지정보
Sato, H., & Sumida, A. (2025). Crown structure and competitive interactions in mixed forests: Insights from an individual-based model. Ecological Research, 40(5), e12562. https://doi.org/10.1111/1440-1703.12562

# 이 논문을 찾은 이유
SEIB-DGVM 최신 냉온대 계보의 virtual-forest 크기, 개체목 표현, LiDAR/수관구조 결합 가능성을 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- spatially explicit individual-based forest model

# 공간 구조
- simulation unit: 100 m x 100 m virtual forest
- individual trees establish, compete, die
- crown and trunk are geometrical
- fine roots are formless biomass state

# 적용 환경
- cold-temperate mixed conifer-hardwood forest
- East Asian PFT modifications inherited from Sato et al. 2023

# 핵심 과정
- individual-tree crown allometry
- light competition
- establishment
- growth
- mortality
- fine-root biomass

# 식생 입력
- individual-tree crown geometry
- DBH
- height
- fine-root biomass
- PFT state

# 핵심 식
Cold-temperate conifer and hardwood crown allometry is modified so that crown radius and leaf area depend on tree dimensions, allowing the different crown architectures of conifers and broadleaf trees to affect competition.

# 파라미터와 단위
- virtual forest: 100 m x 100 m in this study
- individual-tree spatial representation

# 원 논문의 구현 범위
혼효림의 crown architecture 차이가 경쟁과 stand structure에 주는 영향을 분석한다.

# 고운사에 직접 사용할 수 있는 부분
- LiDAR CHM/individual-tree crown geometry와 비교 가능한 상태변수
- 동아시아 침엽수/활엽수 수관 차이
- 100 m stand가 고정 모델해상도가 아니라 연구설정임을 확인하는 최신 사례

# 새로운 coupling이 필요한 부분
- LiDAR tree detection -> SEIB initial individual tree states
- root horizontal geometry
- geomorph grid로 root/litter rasterization

# 한계
fine roots는 biomass만 가지며 horizontal/vertical geometry가 없다. 수관은 세밀하지만 지하구조는 같은 수준으로 명시적이지 않다.

# 최종 판정
- 채택 후보의 구조 근거
- LiDAR 기반 고운사 초기화/검증에 특히 유용

# 참고 링크 / DOI
https://doi.org/10.1111/1440-1703.12562
