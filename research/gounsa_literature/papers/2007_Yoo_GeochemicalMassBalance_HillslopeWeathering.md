# 서지정보
Yoo, K., Amundson, R., Heimsath, A. M., Dietrich, W. E., & Brimhall, G. H. (2007). *Integration of geochemical mass balance with sediment transport to calculate rates of soil chemical weathering and transport on hillslopes*. Journal of Geophysical Research: Earth Surface, 112, F02013. DOI: 10.1029/2005JF000402.

# 이 논문을 찾은 이유
LPJ-GUESS chemical-weathering flux를 실제 mobile-soil mass/thickness 변화와 연결할 때, soil production, physical sediment transport, chemical mass loss를 동시에 보존하는 published mass-balance formulation이 필요한지 확인하기 위해 검토했다.

# 연구 유형
- process-oriented hillslope soil mass-balance model
- geochemical inverse model
- field-constrained numerical framework

# 공간 구조
- hillslope soil boxes
- vertical parent-to-soil input
- lateral soil transport
- lateral solute transport

# 적용 환경
- semiarid granodiorite hillslope
- southeastern Australian highlands

# 핵심 과정
- soil production from saprolite
- physical soil transport
- chemical weathering mass loss/gain
- immobile-element conservation
- residence time

# 핵심 질량수지
Bulk soil mass is controlled by:
```
soil production
- physical export
- chemical solute export
```

The paper defines:
- `rho`: soil bulk density [M L^-3]
- `h`: soil thickness [L]
- `Phi`: soil mass production [M L^-2 T^-1]
- `div(q_s)`: physical erosion/deposition [M L^-2 T^-1]
- `div(q_w)`: chemical solute loss/gain [M L^-2 T^-1]

Thus the non-steady-state bookkeeping basis is:

```
d(rho h)/dt
=
Phi
- div(q_s)
- div(q_w)
```

with sign convention adjusted consistently for deposition/gain.

At steady state:
```
Phi = E + W
```
for production, physical erosion and chemical weathering mass loss.

# immobile-element constraint
For a chemically immobile element i:
```
C_i,p * Phi
=
C_i,s * E
```

This gives a rigorous way to separate chemical loss from physical transport when elemental data are available.

# 중요한 개념
Chemical weathering is a **mass-loss term from mobile soil/regolith material**.

It is not automatically identical to:
```
bedrock -> regolith front advance
```

The paper distinguishes material supply from underlying parent material and chemical removal after that material enters the mobile/weathering system.

# 고운사에 직접 사용할 수 있는 부분
For an A/B mobile-soil state:

```
M_AB = rho_AB * H_AB
```

a defensible update is:

```
dM_AB/dt
=
M_prod_from_C
+ deposition
- physical_erosion
- chemical_mass_loss
```

This is the preferred bookkeeping framework for combining:
- regolith/soil production
- SWEHR physical erosion/deposition
- chemical weathering loss

# 새로운 coupling이 필요한 부분
LPJ-GUESS/Hartmann chemical-weathering flux must be mapped to the same spatial cell and mass basis.

If chemical precipitation produces net mass gain locally, the sign convention must permit negative weathering loss / positive chemical gain.

# 한계
- original analysis assumes hillslope morphology approximately fixed over the residence-time problem
- field application is semiarid granodiorite
- not a vegetation model
- does not calculate the weathering-front advance rate dynamically

# 최종 판정
**핵심 채택: mobile-soil chemical/physical mass-balance framework.**

Use this lineage to update A/B soil mass and thickness. Do not use chemical-weathering flux alone as a regolith-production velocity.

# 참고 링크 / DOI
https://doi.org/10.1029/2005JF000402
