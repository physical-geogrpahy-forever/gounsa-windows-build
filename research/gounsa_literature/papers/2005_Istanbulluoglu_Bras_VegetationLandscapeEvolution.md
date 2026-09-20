# 서지정보
Istanbulluoglu, E., & Bras, R. L. (2005). Vegetation-modulated landscape evolution 관련 CHILD 계열 연구. 정확한 서지 세부사항은 원문 재검증 필요.

# 이 논문을 찾은 이유
식생이 사면확산과 유수침식 모두에 영향을 주는 published LEM이 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- landscape evolution model

# 공간 구조
- CHILD 계열
- distributed landscape evolution
- 유수 및 사면과정 결합

# 적용 환경
- 식생이 존재하는 산지 및 반건조 landscape

# 핵심 과정
- fluvial erosion
- hillslope diffusion
- disturbance
- vegetation growth and loss

# 식생 입력
- vegetation cover state
- vegetation-dependent roughness
- vegetation-dependent erosion resistance
- root cohesion 관련 상태

# 핵심 식
검토 과정에서 vegetation cover가 hillslope transport coefficient 또는 관련 resistance를 조절하는 구조가 확인되었다. 다만 고운사에서는 이 cover를 LPJ-GUESS canopy cover와 동일시하지 않는다.

# 파라미터와 단위
원문 재검증 필요.

# 원 논문의 구현 범위
식생-지형 피드백을 LEM 내부에서 동적으로 표현한다.

# 고운사에 직접 사용할 수 있는 부분
- 식생이 fluvial process와 hillslope process에 서로 다른 경로로 작동할 수 있다는 구조적 근거
- disturbance에 따른 transport efficiency 변화 개념

# 새로운 coupling이 필요한 부분
LPJ-GUESS의 상층 canopy 상태에서 실제 geomorphically effective ground cover를 만드는 연결은 원 논문에 없다. 이를 고운사에 적용하려면 `새로운 coupling`이 필요하다.

# 한계
- vegetation cover를 직접 상태변수로 사용
- 고운사에서 필요한 하층식생/지표피복과 LPJ-GUESS canopy state가 동일하지 않음

# 최종 판정
- 보류
- 사면확산 식생 modifier의 직접 근거로는 현재 미채택

# 참고 링크 / DOI
원문 재검증 필요.
