# 서지정보
Zhao, J., Liu, Y., & Hu, Y. (2026). *MErSiM v1.0: resolving biases in global silicate weathering model with a data-driven surface erosion module*. Geoscientific Model Development, 19, 6857-6878. DOI: 10.5194/gmd-19-6857-2026.

# 이 논문을 찾은 이유
Gabet-Mudd 2009 계열의 최신 transient regolith model이 soil/regolith thickness, mineral abundance, exposure time and weathering flux를 어떻게 동시에 계산하는지 확인하고, Gounsa 100년 model에 사용할 수 있는 modern state equations가 있는지 검토했다.

# 연구 유형
- transient process-based silicate-weathering model
- modern evaluation/model-development paper
- global-scale erosion module coupled to regolith weathering

# 공간 구조
- 1D vertical regolith profile per grid cell
- surface erosion coupled externally

# 적용 환경
- global / Earth-system weathering
- modern and paleoclimate applications

# 핵심 상태변수
- `h`: regolith thickness [m]
- `x(z,t)`: fraction of weatherable primary minerals [-]
- `tau(z,t)`: mineral exposure/residence time [yr]
- `W`: regolith-integrated chemical weathering rate [m yr^-1]
- `P_r`: regolith production/front-advance rate [m yr^-1]
- `E`: physical erosion [m yr^-1]

# 핵심 식

Regolith thickness:
```
dh/dt
=
P_r
-
E
```

Primary-mineral fraction:
```
partial x / partial t
=
-P_r * partial x / partial z
-
K * tau^sigma * x
```

Exposure time:
```
partial tau / partial t
=
-P_r * partial tau / partial z
+
1
```

Integrated weathering:
```
W
=
integral_0^h
K * tau^sigma * x dz
```

Regolith production:
```
P_r
=
P_0 f(h)
```

with climate-dependent optimal production:
```
P_0
=
k_rp q
exp[
(E_a/R)(1/T_0 - 1/T)
]
```

and a soil-production function `f(h)`.

# 중요한 개념
Chemical dissolution `W` is **not subtracted directly from regolith thickness h** in the core thickness equation.

Instead:
- `h` tracks the position of the bedrock-regolith interface relative to the surface
- `W` tracks loss of weatherable minerals within the regolith column

This is exactly why:
```
regolith thickness
!= mobile soil mass
```

must be separated in Gounsa.

# erosion module
MErSiM replaces the earlier simplified SPIM erosion estimate with a Random-Forest model trained on about 4000 10Be-derived basin-average erosion rates.

This erosion module is unsuitable as the Gounsa local physical-erosion engine because SWEHR and explicit hillslope processes already provide that role.

# 고운사에 직접 사용할 수 있는 부분
Use the **transient state equations**, not the global RF erosion submodel.

A possible Gounsa interface:

```
LPJ-GUESS runoff + Tsoil
 + local lithology
 + regolith thickness
 + physical erosion from Gounsa modules
        |
        v
P_r, K
        |
        v
h_reg, x(z), tau(z), W
```

This would preserve supply limitation and residence-time effects.

# 시간척도
The equations are explicitly transient and use time in years.

The published global application is deep-time-oriented, so parameter calibration remains geologic/global.

A 1-year Gounsa numerical update is structurally possible but must be tested for:
- numerical stability
- parameter meaning over only 100 years
- detectability of change

# 새로운 coupling이 필요한 부분
- use LPJ-GUESS local hydrology instead of global climate forcing
- use SWEHR/hillslope modules instead of the RF erosion submodel
- define local lithology parameters
- connect Gounsa A/B mobile soil separately from the full regolith state

# 한계
- global weathering calibration
- no dynamic vegetation/root mechanics
- no event-scale erosion
- 1D vertical chemistry
- root-enhanced chemical reactions absent

# 최종 판정
**강한 modern candidate for transient C/Cr regolith-state equations, not a whole Gounsa model.**

Prefer it over a simple direct division of chemical flux by density.

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-19-6857-2026
