# 서지정보
Pelak, N. F., Parolari, A. J., & Porporato, A. (2016). Bistable plant-soil dynamics and biogenic controls on the soil production function. *Earth Surface Processes and Landforms, 41*(8), 1011-1017.

# 이 논문을 찾은 이유
plant biomass가 soil production function에 직접 들어가는 모델을 찾기 위해 검토했다.

# 연구 유형
- 수치 / 이론모델

# 공간 구조
- hillslope soil-production conceptual model

# 적용 환경
- 일반 사면

# 핵심 과정
- soil production
- plant-soil feedback

# 식생 입력
- plant biomass density `b`

# 핵심 식
후속 비교연구에서 `P(h,b)=[P0+Pv b(h)] exp(-ks h)` 형태로 재현됨. 정확한 원 논문 식번호는 원문 재확인 필요.

# 파라미터와 단위
`P0`, `Pv`, `ks`, soil depth `h`, biomass `b`.

# 원 논문의 구현 범위
biomass가 soil production potential을 직접 증가시키는 최소모델.

# 고운사에 직접 사용할 수 있는 부분
biomass-driven soil production의 구조적 선례.

# 새로운 coupling이 필요한 부분
목본/초본 분리 및 LPJ-GUESS PFT별 효과를 넣는 것은 새로운 coupling.

# 한계
물리풍화, 화학풍화, tree throw를 분리하지 않는다.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1002/esp.3878
