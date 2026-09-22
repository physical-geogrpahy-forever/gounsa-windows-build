# 서지정보
Sato, H., Shibuya, M., & Hiura, T. (2023). Reconstructing spatiotemporal dynamics of mixed conifer and broad-leaved forests with a spatially explicit individual-based dynamic vegetation model. Ecological Research, 38(3), 465-478. https://doi.org/10.1111/1440-1703.12385

# 이 논문을 찾은 이유
SEIB-DGVM이 고운사와 가까운 동아시아 냉온대 침엽수-활엽수 혼효림, 산지 수분구배, 교란 후 천이에 실제 적용된 적이 있는지 확인했다.

# 연구 유형
- 수치모델
- spatially explicit individual-based vegetation model calibration/validation

# 공간 구조
- SEIB-DGVM virtual forest
- 개별목 경쟁 및 spatial niche segregation
- elevation과 terrestrial wetness index를 환경구배로 사용

# 적용 환경
- 일본 홋카이도
- deciduous broad-leaved + evergreen conifer mixed forest
- cool-temperate to sub-boreal transition

# 핵심 과정
- 정착
- 생장
- 경쟁
- 사망
- drought/excess moisture limitation
- catastrophic disturbance 이후 succession

# 식생 입력
- 개별목/PFT biomass
- crown/tree structure
- fine-root biomass 계보
- soil-water response
- litter pool 계보

# 핵심 식
논문의 핵심은 특정 지형식보다 PFT별 drought 및 excessive-soil-moisture tolerance, establishment rate, background mortality를 보정하여 elevation/wetness gradient에 따른 혼효림 구조를 재현한 것이다.

# 파라미터와 단위
- cold-temperate PFTs introduced/calibrated for East Asia
- drought and excessive moisture tolerance: PFT-specific
- establishment and background mortality: calibrated
- 75-year simulated forest가 교란 후 관측 forest와 가장 유사한 결과

# 원 논문의 구현 범위
홋카이도 혼효림의 교란 후 succession과 공간적 환경구배에 따른 침엽수 비율과 biomass를 재현한다.

# 고운사에 직접 사용할 수 있는 부분
- 동아시아 냉온대 PFT 계보
- 지형성 습윤도와 토양수분이 종조성/biomass에 영향을 주는 구조
- 약 100년 post-disturbance succession과 직접적으로 유사한 시간범위
- 한국 온대 산림로의 지역적 전이가 열대/북방림 전용 모델보다 방어적

# 새로운 coupling이 필요한 부분
- 고운사 수종/PFT parameterization
- LiDAR-derived terrain/CHM initialization
- dynamic geomorphic soil depth and water state
- plot 사이 fine-scale seed dispersal

# 한계
독립 validation plots의 교란 이전 broadleaf/conifer 비율은 충분히 재현하지 못했다. 지형수문은 full 2D lateral hydrology가 아니라 stand/grid environmental control이다.

# 최종 판정
- 채택 후보의 핵심 지역 적용 근거
- SEIB-DGVM을 고운사 식생축 최우선 기술검증 후보로 올리는 중요한 근거

# 참고 링크 / DOI
https://doi.org/10.1111/1440-1703.12385
