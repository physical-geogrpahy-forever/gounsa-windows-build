# 서지정보
Gabet, E. J., & Mudd, S. M. (2010). Bedrock erosion by root fracture and tree throw: A coupled biogeomorphic model to explore the humped soil production function and the persistence of hillslope soils. *Journal of Geophysical Research: Earth Surface, 115*, F04005.

# 이 논문을 찾은 이유
목본 뿌리에 의한 물리풍화와 tree throw를 토양생산에 직접 연결한 모델을 찾기 위해 검토했다.

# 연구 유형
- 수치모델

# 공간 구조
- hillslope soil-production model

# 적용 환경
- 산림 사면

# 핵심 과정
- root fracture
- tree throw
- bedrock erosion
- soil production

# 식생 입력
- conifer population dynamics
- rootwad volume
- tree-throw frequency

# 핵심 식
root fracture + tree throw로 bedrock erosion을 계산하며 humped soil-production relation이 emergent하게 나타날 수 있다.

# 파라미터와 단위
tree population, rootwad volume, throw frequency 등. 세부 단위 원문 재검증 필요.

# 원 논문의 구현 범위
목본 고유의 물리적 soil production mechanism을 명시한다.

# 고운사에 직접 사용할 수 있는 부분
고운사 woody mechanical weathering 항의 핵심 모델 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS DBH/density/root state를 원 모델 변수로 연결하면 새로운 coupling.

# 한계
초본/관목의 화학풍화와 별도.

# 최종 판정
- 채택 후보

# 참고 링크 / DOI
https://doi.org/10.1029/2009JF001526
