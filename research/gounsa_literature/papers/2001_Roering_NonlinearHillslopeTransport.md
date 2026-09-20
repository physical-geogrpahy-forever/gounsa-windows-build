# 서지정보
Roering, J. J., Kirchner, J. W., & Dietrich, W. E. (2001). *Hillslope evolution by nonlinear, slope-dependent transport: Steady state morphology and equilibrium adjustment timescales*. Journal of Geophysical Research: Solid Earth, 106, 16499-16513. DOI: 10.1029/2001JB000323.

# 이 논문을 찾은 이유
고운사처럼 급경사 산지에서 Pelletier 2013의 장기 vegetation-modified diffusivity 대신, 100년 simulation에 연 단위로 적분할 수 있는 physically established background hillslope-transport law가 있는지 확인하기 위해 검토했다.

# 연구 유형
- 이론/수치모델
- nonlinear hillslope transport
- field-topography constrained landscape evolution

# 공간 구조
- continuous hillslope / raster 또는 profile에 구현 가능
- local slope-dependent flux

# 적용 환경
- soil-mantled hillslopes
- steep slopes approaching a critical gradient

# 핵심 과정
- background hillslope sediment transport
- creep-like disturbance transport
- slope-dependent nonlinearity
- near-critical-slope transport acceleration

# 식생 입력
직접 vegetation state 없음.

따라서 이 식은 고운사에서 **background physical creep/continuous transport** 항으로만 사용하고:
- root-growth bioturbation
- tree throw
- postfire dry ravel
을 별도 과정으로 둔다.

# 핵심 식

Vector form commonly used for the Roering nonlinear flux law:
```
q_creep
=
-K_nl * grad(z)
/
[1 - (|grad(z)| / S_c)^2]
```

1D magnitude form:
```
q_s
=
K S
/
[1 - (S/S_c)^2]
```

where:
- `K_nl`: nonlinear hillslope diffusivity [m^2 yr^-1 for volumetric flux per contour length convention]
- `S`: slope gradient
- `S_c`: critical slope gradient

For:
```
S << S_c
```
the equation approaches linear diffusion.

As:
```
S -> S_c
```
transport rises strongly.

# 파라미터와 단위
- `K_nl`: L^2 T^-1 in standard geomorphic volumetric-flux implementation
- `S_c`: dimensionless critical gradient
- `q_s`: volumetric sediment flux per contour width [L^2 T^-1]

Site-specific calibration is required.

# 원 논문의 구현 범위
The model describes continuous background hillslope transport as a nonlinear function of slope.

It does **not** dynamically calculate:
- root biomass
- tree-throw rate
- litter
- wildfire disturbance

# 고운사에 직접 사용할 수 있는 부분
For steep mountain terrain, this is a more defensible background transport law than applying a constant linear diffusivity everywhere.

Recommended role:
```
q_hill
=
q_creep,Roering
+
q_rootgrowth,Gabet
+
q_treethrow,Doane
+
q_dryravel,Lamb
```

The Roering term supplies only the continuous background component.

# 시간간격
The constitutive equation is continuous in time and can be numerically integrated at annual or shorter geomorphic steps subject to stability.

Its parameters are not inherently a 10^4-10^6 yr forcing state in the way Pelletier 2013's eco-pedo-geomorphic calibration is.

Thus using a 1-year outer timestep over a 100-year Gounsa simulation is numerically/process-wise plausible, provided stability is checked.

# 새로운 coupling이 필요한 부분
LPJ-GUESS vegetation should **not** be multiplied directly into `K_nl` without a separate published relation.

Vegetation effects enter instead through separate process terms:
- Gabet root growth/decay
- Doane/tree throw
- Lamb dry ravel/storage
- possibly frost/wet-dry terms if independently parameterized

# 한계
- no vegetation dynamics
- near `S_c` numerical behavior requires care
- background creep remains an effective parameterization aggregating multiple small disturbances

# 최종 판정
**채택 후보: 고운사 continuous/background hillslope transport law.**

Preferred over Pelletier 2013's biomass-dependent diffusivity for the 100-year main model.

# 참고 링크 / DOI
https://doi.org/10.1029/2001JB000323
