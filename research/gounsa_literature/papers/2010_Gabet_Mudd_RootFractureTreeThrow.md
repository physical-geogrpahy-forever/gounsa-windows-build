# 서지정보
Gabet, E. J., & Mudd, S. M. (2010). Bedrock erosion by root fracture and tree throw: A coupled biogeomorphic model to explore the humped soil production function and the persistence of hillslope soils. *Journal of Geophysical Research: Earth Surface, 115*, F04005. https://doi.org/10.1029/2009JF001526

# 이 논문을 찾은 이유
고운사에서 목본 뿌리 파쇄와 나무전도를 C/Cr에서 이동성 토양으로의 물리적 생산과정에 연결할 수 있는 published model을 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- biogeomorphic soil-production model

# 공간 구조
- hillslope soil-production framework

# 적용 환경
- 산림 사면
- 토양피복 기반암 사면

# 핵심 과정
- root fracture
- tree throw
- bedrock erosion
- soil production

# 식생 입력
- tree population dynamics
- tree size
- rootwad volume
- mortality and tree throw

# 핵심 식
뿌리 파쇄와 나무전도를 명시적인 기계적 과정으로 결합해 soil production을 계산하며 humped soil-production relation이 emergent하게 나타날 수 있음을 보인다.

# 파라미터와 단위
- tree density
- tree size
- rootwad volume
- mortality 또는 throw frequency
세부 계수와 단위는 구현 전 원문 재검증 필요.

# 원 논문의 구현 범위
목본의 성장과 사망이 암석 파쇄와 토양생산에 직접 영향을 주는 mechanistic framework.

# 고운사에 직접 사용할 수 있는 부분
C/Cr에서 AB 또는 PDZ로의 생물기계적 토양생산에 목본 뿌리와 tree throw를 넣는 구조적 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS cohort의 DBH, tree density, mortality, root state를 원 모델 변수에 연결하는 것은 새로운 coupling이다. FineRootC만으로 root fracture를 계산하는 것도 원 논문에 없는 새로운 coupling이다.

# 한계
- 목본 중심
- chemical weathering과 분리
- FineRootC와 기계적 root-fracture 변수는 동일하지 않음

# 최종 판정
- C/Cr에서 AB로의 생물기계적 토양생산에 채택 후보
- 기본모델에 강제하기보다 mechanistic sensitivity 후보로 유지

# 참고 링크 / DOI
https://doi.org/10.1029/2009JF001526
