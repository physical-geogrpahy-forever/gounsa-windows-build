# Saco & Moreno-de las Heras (2013)

# 서지정보
Saco, P. M., & Moreno-de las Heras, M. (2013). Ecogeomorphic coevolution of semiarid hillslopes: Emergence of banded and striped vegetation patterns through interaction of biotic and abiotic processes. *Water Resources Research, 49*(1), 115-126. https://doi.org/10.1029/2012WR012001

# 이 논문을 찾은 이유
SIBERIA 유수침식 erodibility를 피복률이 아니라 식생량으로 수정한 published precedent 확인.

# 연구 유형
- 수치모델

# 공간 구조
- distributed hillslope ecogeomorphic model coupled to SIBERIA
- 세부 routing은 원문 재검증 필요

# 적용 환경
- 반건조 사면

# 핵심 과정
- runoff/run-on
- fluvial sediment transport
- vegetation-pattern feedback

# 식생 입력
- plant biomass density P

# 핵심 식
기본은 `q_s = beta q^m S^n`. 채팅에서 erodibility를 biomass의 감소함수 `beta(P)=max[beta_min, beta_b(1-beta_v P)]` 형태로 복구했으나 exact notation은 원문 재검증 필요.

# 파라미터와 단위
- P: biomass density
- beta_b, beta_v, beta_min
- exact units: 원문 재검증 필요

# 원 논문의 구현 범위
동적 식생, runoff/run-on, erosion/deposition feedback 결합.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS의 quantitative biomass가 SIBERIA-type erodibility를 직접 바꿀 수 있다는 핵심 선례.

# 새로운 coupling이 필요한 부분
목본/관목/초본 또는 PFT별 계수, FineRootC→RLD/RSAD 변환은 새로운 coupling.

# 한계
총 biomass를 사용하며 목본/초본 구분 없음. genuine 2D 최종 엔진을 단독으로 충족하는 모델은 아님.

# 최종 판정
- 채택 후보
- biomass-erodibility 연결의 핵심 근거

# 참고 링크 / DOI
- https://doi.org/10.1029/2012WR012001
