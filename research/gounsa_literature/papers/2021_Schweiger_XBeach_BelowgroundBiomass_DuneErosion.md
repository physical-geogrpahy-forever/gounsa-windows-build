# 서지정보
Schweiger, C., & Schüttrumpf, H. (2021). *Considering the effect of belowground biomass on dune erosion volumes in coastal numerical modelling*. Coastal Engineering, 168, 103927. DOI: 10.1016/j.coastaleng.2021.103927.

# 이 논문을 찾은 이유
quantitative belowground vegetation/root mechanics를 실제 morphodynamic erosion threshold에 직접 넣은 published numerical model이 있는지 확인하기 위해 검토했다.

# 연구 유형
- numerical model extension
- XBeach morphodynamic model
- 1D wave-flume validation

# 공간 구조
- 1D XBeach in the validation study
- process-based coastal morphodynamics
- genuine 2D mountain-hillslope model 아님

# 적용 환경
- vegetated coastal dunes
- sandy substrate
- storm erosion / waves

# 핵심 과정
- sediment erosion
- morphodynamic bed change
- root-enhanced critical erosion velocity
- erosion-depth-dependent loss of root protection

# 식생 입력
The model does not use generic vegetation cover as its root-resistance variable.

Root mechanics:
- root tensile strength
- root area ratio, RAR
- root cohesion C_r
- rooting depth
- root-cohesion calibration coefficient

A later large-scale XBeach implementation of the same root model gives:
```
C_r = t_R * RAR
```
and increases critical erosion velocity according to root cohesion while erosion remains within rooting depth.

The root effect can decrease dynamically as cumulative erosion approaches/exceeds rooting depth.

# 핵심 식
Conceptual root threshold pathway:
```
root tensile strength + RAR
 -> C_r
 -> increased critical erosion velocity U_cr
 -> reduced sediment erosion
```

The follow-up implementation expresses the increase approximately as:
```
U_cr,new = U_cr + rcc * sqrt(C_r / rho)
```
within the rooted zone.

Exact original-paper implementation should be checked before code adoption.

# 파라미터와 단위
- C_r: kN m^-2 / kPa scale
- RAR: dimensionless area ratio
- tensile strength: stress
- root depth: m
- U_cr: m s^-1

# 원 논문의 구현 범위
XBeach was extended with a literature-derived root model and tested against wave-flume dune erosion with and without belowground biomass. Including root effects improved predicted erosion volumes.

# 고운사에 직접 사용할 수 있는 부분
Important mechanistic precedent:
```
root amount/architecture/mechanics
 -> erosion initiation threshold
```

This suggests root effects need not be represented only through erodibility Kr; a critical-threshold term can have a separate root-mechanics basis.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC -> RAR/tensile strength/root cohesion and translating coastal critical velocity into hillslope critical shear stress are **new couplings**.

# 한계
- coastal sandy dune
- wave-driven, not rainfall hillslope erosion
- validation was 1D
- user-defined/calibrated root coefficient
- not a direct alternative to Iber+/Wu/SERGHEI-SE

# 최종 판정
- **채택: mechanistic root -> erosion-threshold precedent**
- final 2D engine candidate: no
- potentially important for deciding whether roots modify only Kd/Kr or also tau_c

# 참고 링크 / DOI
https://doi.org/10.1016/j.coastaleng.2021.103927
