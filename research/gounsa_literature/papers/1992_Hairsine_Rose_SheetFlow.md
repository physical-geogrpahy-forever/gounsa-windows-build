# 서지정보
Hairsine, P. B., & Rose, C. W. (1992). *Modeling water erosion due to overland flow using physical principles: 1. Sheet flow*. Water Resources Research, 28(1), 237-243. DOI: 10.1029/91WR02380.

# 이 논문을 찾은 이유
고운사 유수침식 후보인 Hairsine-Rose 계열의 원래 물리구조를 확인하고, original cohesive soil과 deposited cohesionless layer의 구분이 postfire loose surface layer에 적합한지 검토했다.

# 연구 유형
- physically based erosion theory/model
- analytical/numerical process model

# 공간 구조
- plane slope
- original formulation is not a modern genuine 2D hydrodynamic catchment solver

# 적용 환경
- cohesive soil surface under overland flow

# 핵심 과정
- erosion of original cohesive soil
- deposition
- cohesionless deposited-layer formation
- deposited-layer shielding
- entrainment-limited and transport-limited regimes

# 식생 입력
없음.

# 핵심 식
The theory explicitly separates three sediment states:
```
original cohesive soil
<-> sediment in flow
<-> deposited cohesionless layer
```

As deposited sediment accumulates it shields the original cohesive soil, so erosion agents increasingly act on the deposited layer rather than intact soil.

Two equilibrium regimes are distinguished:
- complete shielding, analogous to transport-limited behavior
- incomplete shielding, where sediment concentration still depends on cohesive soil strength

# 파라미터와 단위
Original Hairsine-Rose parameters include sediment-size fractions, settling velocities, detachment/entrainment parameters, stream power and deposited-layer shielding variables.

Exact equations/units should be taken from the original article and later corrections before implementation.

# 원 논문의 구현 범위
Provides the physical base for later rainfall/flow Hairsine-Rose formulations and modern 2D implementations.

# 고운사에 직접 사용할 수 있는 부분
The original/deposited distinction is highly relevant to:
- intact postfire soil
- fire-disturbed loose mineral material
- freshly deposited sediment
- evolving armour/shield layer

It avoids forcing all surface sediment into one transport-capacity state.

# 새로운 coupling이 필요한 부분
Root/litter control of original-soil strength/detachability is not included and would be a new coupling.

# 한계
- vegetation absent
- not itself a 2D catchment solver
- later papers corrected/generalized some equations

# 최종 판정
- **core theoretical lineage**
- use through a verified later 2D implementation rather than coding the 1992 formulation alone

# 참고 링크 / DOI
https://doi.org/10.1029/91WR02380
