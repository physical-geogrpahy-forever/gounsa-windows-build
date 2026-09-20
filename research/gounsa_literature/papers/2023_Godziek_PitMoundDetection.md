# 서지정보
Godziek, J., & Pawlik, Ł. (2023). Indicators of wind-driven forest disturbances - pit-mound topography, its automatic detection and significance. CATENA, 221, 106757. https://doi.org/10.1016/j.catena.2022.106757

# 이 논문을 찾은 이유
tree-throw module의 공간적 산출물을 DEM/LiDAR로 검증할 방법을 찾기 위해 검토했다.

# 연구 유형
- 방법론
- geomorphometric detection

# 공간 구조
- hillslope DEM/LiDAR
- pit-mound objects

# 적용 환경
- forested hillslope

# 핵심 과정
- wind disturbance
- pit-mound topography
- tree throw legacy

# 식생 입력
- uprooting legacy, 직접 biomass 입력 아님

# 핵심 식
자동탐지 algorithm 세부식은 원문 재검증 필요.

# 파라미터와 단위
pit density, mound density, roughness metrics.

# 원 논문의 구현 범위
forest disturbance의 pit-mound signature를 자동 탐지한다.

# 고운사에 직접 사용할 수 있는 부분
tree-throw 모듈 검증지표로 pit/mound density와 roughness를 사용할 수 있다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS tree mortality에서 predicted pit-mound map을 생성하는 것은 새로운 coupling이다.

# 한계
수송량 계산식 자체는 아니다.

# 최종 판정
- 보조근거
- 검증 방법론
