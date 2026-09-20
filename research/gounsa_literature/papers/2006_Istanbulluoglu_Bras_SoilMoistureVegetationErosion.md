# 서지정보
Istanbulluoglu, E., & Bras, R. L. (2006). Soil moisture, vegetation, and erosion dynamics 관련 ecohydrologic landscape model. 정확한 서지 세부사항은 원문 재검증 필요.

# 이 논문을 찾은 이유
강우, 토양수분, 식생동역학, 침식이 하나의 수치모델에서 어떻게 연동되는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- ecohydrologic erosion model

# 공간 구조
- distributed landscape framework
- stochastic rainfall forcing

# 적용 환경
- 반건조 landscape

# 핵심 과정
- soil moisture
- vegetation dynamics
- runoff erosion
- sediment transport

# 식생 입력
- dynamic vegetation state
- vegetation cover

# 핵심 식
식생상태는 수분조건에 따라 변하고, 그 식생상태가 runoff 및 erosion resistance에 되먹임한다.

# 파라미터와 단위
원문 재검증 필요.

# 원 논문의 구현 범위
강우-토양수분-식생-침식의 동적 피드백을 포함한다.

# 고운사에 직접 사용할 수 있는 부분
- 식생과 수문을 분리된 고정 factor가 아니라 동적 상태로 다루는 구조

# 새로운 coupling이 필요한 부분
LPJ-GUESS PFT별 biomass와 직접 연결하는 식은 원 논문에 없다.

# 한계
고운사 산림 PFT 및 하층식생 구조를 그대로 표현하지 않는다.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
원문 재검증 필요.
