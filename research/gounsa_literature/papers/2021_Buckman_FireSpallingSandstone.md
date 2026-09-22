# 서지정보
Buckman, S., Morris, R. H., & Bourman, R. P. (2021). Fire-induced rock spalling as a mechanism of weathering responsible for flared slope and inselberg development. *Nature Communications, 12*, 2150. https://doi.org/10.1038/s41467-021-22451-2

# 이 논문을 찾은 이유
고운사가 사암 기반 산림사면이라는 조건에서 wildfire가 sandstone 자체를 유의미하게 spalling하여 coarse-fragment supply를 만들 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- field geomorphic observations
- conceptual/quantitative fire-spalling weathering model

# 공간 구조
- rock outcrop
- cliff/inselberg margin
- landscape weathering

# 적용 환경
- fire-prone Australian landscapes
- quartz sandstone 사례 포함
- 2019-2020 Black Summer fires

# 핵심 과정
- wildfire heating
- rock spalling
- physical weathering
- sediment production
- long-term slope retreat

# 식생 입력
- fire regime 및 burning vegetation이 heating source의 배경조건
- quantitative vegetation biomass model은 아님

# 핵심 식
fire-spalling erosion rate를 spall thickness W, affected area A, fire recurrence interval t로 개념화하는 `E = W A / t` 계열 관계를 제시한다.
rock type/fire temperature는 spall thickness에, fire intensity/duration은 affected surface area에 영향을 준다.

# 파라미터와 단위
- spall thickness
- affected surface area
- fire recurrence interval
- rock type and fire severity
정확한 implementation unit은 원문 식을 재검증한다.

# 원 논문의 구현 범위
wildfire-induced rock spalling을 반복적 physical-weathering source로 보고 장기 geomorphic erosion에 연결한다. Sydney Basin quartz sandstone의 실제 wildfire spalling 사진과 현장관찰을 포함한다.

# 고운사에 직접 사용할 수 있는 부분
- **sandstone + wildfire -> spall production**의 직접 사례
- fire-spall production module에 burn/fire regime와 exposed rock area를 포함할 근거
- 고운사에서 fire spall을 단순 가정이 아닌 독립 geomorphic weathering process로 둘 강한 근거

# 새로운 coupling이 필요한 부분
LPJ-GUESS fire severity/fuel state 및 고운사 exposed sandstone geometry에서 W와 A를 계산하는 것은 **새로운 coupling**이다.

# 한계
고운사 사암의 물성 및 단일 산불 후 100년 단기 size-class dynamics를 직접 보정하지 않는다.

# 최종 판정
- 핵심 채택
- sandstone fire-spall production의 핵심 현장근거

# 참고 링크 / DOI
https://doi.org/10.1038/s41467-021-22451-2
