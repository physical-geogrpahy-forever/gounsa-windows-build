# 서지정보
Welivitiya, W. D. D. P., Willgoose, G. R., & Hancock, G. R. (2019). A coupled soilscape–landform evolution model: Model formulation and initial results. *Earth Surface Dynamics, 7*, 591–607. https://doi.org/10.5194/esurf-7-591-2019

# 이 논문을 찾은 이유
토양 프로파일의 수직 입도구조와 지형이 함께 변화하는 기존 수치모델을 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- soilscape-landform evolution model

# 공간 구조
- SSSPAM과 landform evolution model 결합
- 초기 결과는 이상화된 선형 사면

# 적용 환경
- 장기 soilscape evolution

# 핵심 과정
- depth-dependent weathering
- particle-size evolution
- erosion
- deposition
- elevation change

# 식생 입력
- 이 세션에서 확인한 범위에서는 상세 PFT 또는 cohort 동태가 핵심이 아님

# 핵심 식
이 세션에서는 원문 방정식 전체를 구현수준으로 복구하지 않았다. 핵심은 토양 프로파일의 입도조성을 상태변수로 추적하고 지형변화와 결합한다는 구조다.

# 파라미터와 단위
- particle-size fractions
- soil layer state
- weathering depth dependence
- sediment load
세부 단위와 계수는 원문 재검증 필요.

# 원 논문의 구현 범위
토양 프로파일과 landform을 동시에 진화시킨다.

# 고운사에 직접 사용할 수 있는 부분
- fine과 coarse를 수직적으로 분리해 추적하는 구조
- 단일 토심값 대신 profile composition을 상태변수로 두는 구조
- erosion/deposition에 따라 profile composition이 변하는 구조

# 새로운 coupling이 필요한 부분
고운사에서 SSSPAM 전체를 이식하지 않고 CF_surface, CF_AB, CF_C와 fine/coarse mass pools만 차용하는 것은 새로운 coupling이다.

# 한계
- 고운사 산림사면에 직접 보정된 모델이 아님
- 다른 수문과 침식모듈과 중복될 수 있음

# 최종 판정
- 수직 coarse/fine profile 구조의 보조근거
- 전체 모델 이식은 미채택

# 참고 링크 / DOI
https://doi.org/10.5194/esurf-7-591-2019
