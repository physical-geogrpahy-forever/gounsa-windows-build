# 서지정보
Lehmann et al. (2019). STEP-TRAMM 계열 root decay/regrowth와 landslide 모델. 정확한 전체 서지정보는 원문 재검증 필요.

# 이 논문을 찾은 이유
교란 뒤 root strength decay와 forest regrowth를 shallow landslide에 동적으로 반영하는 수치모델을 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- landslide model

# 공간 구조
- spatially distributed slope-stability framework

# 적용 환경
- 산림
- 교란 후

# 핵심 과정
- root-strength decay
- regrowth
- landslide initiation

# 식생 입력
- empirical root-strength state
- forest recovery state

# 핵심 식
root strength가 disturbance 후 decay하고 regrowth에 따라 회복되어 slope stability를 바꾼다. 정확한 식은 원문 재검증 필요.

# 파라미터와 단위
원문 재검증 필요.

# 원 논문의 구현 범위
dynamic root-strength state를 landslide susceptibility와 연결한다.

# 고운사에 직접 사용할 수 있는 부분
root-related effect의 지연감소와 회복을 별도 시간함수로 두는 비교근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root biomass와 STEP-TRAMM root-strength state 연결은 새로운 coupling이다.

# 한계
root biomass 자체를 동적으로 계산하는 모델은 아니다.

# 최종 판정
- 보조근거
- 원문 재검증 필요

# 참고 링크 / DOI
미복구, 원문 재검증 필요.
