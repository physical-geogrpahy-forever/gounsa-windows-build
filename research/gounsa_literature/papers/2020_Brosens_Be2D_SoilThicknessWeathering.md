# 서지정보
Brosens, L., Campforts, B., Robinet, J., Vanacker, V., Opfergelt, S., Ameijeiras-Mariño, Y., Minella, J. P. G., & Govers, G. (2020). *Slope Gradient Controls Soil Thickness and Chemical Weathering in Subtropical Brazil: Understanding Rates and Timescales of Regional Soilscape Evolution Through a Combination of Field Data and Modeling*. Journal of Geophysical Research: Earth Surface, 125(6), e2019JF005321. DOI: 10.1029/2019JF005321.

# 이 논문을 찾은 이유
soil production, physical erosion/deposition and chemical weathering을 soil-thickness equation에서 실제로 어떻게 결합하는지, 그리고 chemical weathering을 L/T 단위로 처리하는 landscape model 선례를 확인하기 위해 검토했다.

# 연구 유형
- field-calibrated soil-landscape evolution model
- Be2D

# 공간 구조
- 1D hillslope transects / soil boxes
- lateral sediment transport
- local soil thickness

# 적용 환경
- subtropical southern Brazil
- basalt and dacite-rhyolite parent materials

# 핵심 과정
- soil production from saprolite
- chemical weathering
- diffusive transport
- physical erosion/deposition
- soil residence time

# 핵심 thickness balance
The paper defines soil thickness `d` as the balance among:
- soil production `phi` [L T^-1]
- chemical weathering `W` [L T^-1]
- physical erosion/deposition `E_tot` [L T^-1]

Conceptually:

```
dd/dt
=
phi
- W
- E_tot
```

with the physical term obtained from the difference between lateral mass influx and outflux divided by:
```
rho_s * Delta x
```

Sign convention for deposition is handled consistently through the flux divergence.

# chemical-weathering parameterization
In Be2D:
```
W(d)
=
W0 * exp(-beta d)
```

where:
- `W0`: weathering rate at zero soil thickness [L T^-1]
- `beta`: depth-scaling factor [L^-1]

This is a long-term effective weathering relation, not a daily LPJ-GUESS climate forcing.

# 중요한 개념
The model demonstrates a practical route:

```
mass flux
 -> divide by bulk density
 -> equivalent thickness rate
```

for a **mobile-soil layer**.

However it does not imply that chemical dissolved loss equals bedrock-to-regolith production.

# 고운사에 직접 사용할 수 있는 부분
Strong support for the A/B-layer bookkeeping:

```
dH_AB/dt
=
P_AB
+ deposition/rho_AB
- physical_erosion/rho_AB
- W_AB_mass/rho_AB
```

This can receive:
- SWEHR physical erosion/deposition
- Yoo/Hartmann chemical mass loss
- production from underlying C/Cr

# 한계
- long-term calibration
- original weathering law is depth-only effective parameterization
- no dynamic LPJ-GUESS vegetation
- no explicit postfire event processes

# 최종 판정
**핵심 채택: soil-thickness mass-balance implementation precedent.**

Use the balance structure, not the original exponential weathering coefficient as the Gounsa daily/annual chemical-weathering law.

# 참고 링크 / DOI
https://doi.org/10.1029/2019JF005321
