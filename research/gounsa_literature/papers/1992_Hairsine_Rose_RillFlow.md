# 서지정보
Hairsine, P. B., & Rose, C. W. (1992). *Modeling water erosion due to overland flow using physical principles: 2. Rill flow*. Water Resources Research, 28(1), 245-250. DOI: 10.1029/91WR02381.

# 이 논문을 찾은 이유
Hairsine-Rose 계열에서 concentrated-flow/rill erosion이 stream power, deposited-layer shielding, entrainment energy를 통해 어떻게 계산되는지 원 논문에서 확인하기 위해 검토했다.

# 연구 유형
- physically based rill erosion theory/model

# 공간 구조
- parallel trapezoidal rills on a slope
- triangular/rectangular special cases
- 1D rill-flow theory, not genuine 2D landscape hydrodynamics

# 적용 환경
- homogeneous soil with incised rills
- overland-flow/rill experiments

# 핵심 과정
- rill flow
- original-soil entrainment
- deposited-layer re-entrainment
- deposition
- transport-limited versus entrainment-limited behavior

# 식생 입력
없음.

# 핵심 식
Flow-driven entrainment is formulated using stream power distributed over the rill wetted perimeter.

Later implementations write the original-soil entrainment for size class i in the form:
```
r_i = (1-H) f_oi (F/J) (Omega - Omega_0)
```
where:
- H is deposited-layer protection
- F is the fraction of excess stream power used for entrainment
- J is specific energy of entrainment
- Omega_0 is critical stream power

The deposited layer changes the partitioning between erosion of original cohesive soil and re-entrainment of cohesionless deposited sediment.

# 파라미터와 단위
- J: J kg^-1 = m2 s^-2
- Omega: W m^-2
- Omega_0: W m^-2
- F: dimensionless
- H: dimensionless shielding fraction

# 원 논문의 구현 범위
Develops rill sediment continuity and analytical/numerical solutions for entrainment- and transport-limited states.

# 고운사에 직접 사용할 수 있는 부분
Provides a physically explicit concentrated-flow resistance variable `J` that can respond to changing soil strength.

Together with Misra & Rose (1995), this creates a defensible chain:
```
soil strength
 -> J
 -> flow-driven entrainment
```

# 새로운 coupling이 필요한 부분
Quantitative root/litter states are absent.
Any:
```
RLD/RMD -> soil strength -> J
```
implementation is a new coupling unless a direct quantitative relation is independently verified.

# 한계
- predefined parallel-rill theory
- vegetation absent
- use modern 2D implementation for Gounsa rather than this geometry directly

# 최종 판정
- **core concentrated-flow theoretical lineage**
- valuable for interpreting root effects through erosion-specific soil strength

# 참고 링크 / DOI
https://doi.org/10.1029/91WR02381
