# 서지정보
Saco, P. M., & Moreno-de las Heras, M. (2013). Ecogeomorphic coevolution of semiarid hillslopes: Emergence of banded and striped vegetation patterns through interaction of biotic and abiotic processes. *Water Resources Research, 49*(1), 115-126.

# 이 논문을 찾은 이유
SIBERIA erodibility에 식생 biomass를 직접 연결한 선례를 찾기 위해 검토했다.

# 연구 유형
- 수치모델

# 공간 구조
- distributed hillslope / landscape evolution

# 적용 환경
- 반건조 사면

# 핵심 과정
- 유수침식
- 지형-식생 공진화

# 식생 입력
- plant biomass density `P`

# 핵심 식
`q_s = beta q^m S^n`; `beta(P)`가 biomass 증가에 따라 감소하고 하한 `beta_min`을 둔다.

# 파라미터와 단위
`beta_b`, `beta_v`, `beta_min`, biomass density. 정확한 값은 원문 재검증 필요.

# 원 논문의 구현 범위
총 biomass가 SIBERIA erodibility를 수정한다.

# 고운사에 직접 사용할 수 있는 부분
biomass가 erodibility에 직접 들어가는 published coupling의 기본 골격.

# 새로운 coupling이 필요한 부분
LPJ-GUESS에서는 총 biomass 대신 PFT별 FineRootC/traits로 세분하려면 새로운 coupling 필요.

# 한계
교목, 관목, 초본 및 root trait을 구분하지 않는다.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1029/2012WR012001
