# 서지정보
Braun, J., Mercier, J., Guillocheau, F., & Robin, C. (2016). *A simple model for regolith formation by chemical weathering*. Journal of Geophysical Research: Earth Surface, 121(11), 2140-2171. DOI: 10.1002/2016JF003914.

# 이 논문을 찾은 이유
LPJ-GUESS/Hartmann chemical mass-loss flux와 별개로, fresh bedrock가 실제 regolith로 전환되며 weathering front가 이동하는 속도를 계산할 published model이 필요한지 확인하기 위해 검토했다.

# 연구 유형
- process-based numerical regolith model
- subsurface hydrology + weathering-front propagation + surface erosion/transport

# 공간 구조
- 2D hillslope cross section
- permeable regolith above impermeable bedrock
- groundwater/water-table geometry

# 적용 환경
- orogenic and anorogenic settings
- generic rock types including granite/basalt examples

# 핵심 과정
- groundwater flow
- solute export
- mineral dissolution
- weathering-front advance
- regolith-thickness evolution
- surface erosion

# 핵심 식

Weathering-front propagation is linked to pore-fluid velocity:

```
front advance rate
proportional to
fluid velocity
```

The proportionality follows a simple dissolution/transport mass balance involving:
- mineral equilibrium concentration `C_eq`
- mineral molar volume `V_m`
- mineral fraction in protolith `M_p`

The model then links pore-fluid velocity to the groundwater gradient and fractured-bedrock permeability.

A compact form of the front relation is:
```
B_dot
proportional to
F * hydraulic-gradient
```
where `F` is a rock-dependent weathering constant assembled from mineral solubility/volume/fraction and hydraulic properties.

The paper also proposes high-flow kinetic limitation and an Arrhenius temperature dependence as extensions.

# 중요한 개념
This model calculates:
```
bedrock -> regolith interface motion
```

This is **not the same quantity** as the dissolved chemical mass loss from existing soil/regolith.

That distinction directly solves a key ambiguity in the Gounsa weathering architecture.

# 고운사에 직접 사용할 수 있는 부분
Candidate process source for:
```
P_front,chem [m yr^-1]
```

If local/subsurface hydrology is available:
```
water flux / groundwater gradient
+ rock properties
 -> weathering-front advance
```

This front advance can supply new C/Cr material independently of chemical mass loss within existing regolith.

# LPJ-GUESS relation
LPJ-GUESS can supply:
- water balance
- soil temperature
- possibly recharge-related forcing

But Braun uses subsurface groundwater geometry and hydraulic conductivity, not simply surface runoff.

Therefore:
```
LPJ-GUESS runoff
 -> Braun front advance
```
must not be done directly.

A recharge/subsurface-flow interface is required.

# 한계
- designed for geological regolith evolution
- simplified hydrogeology
- no dynamic vegetation/root system
- parameters such as fractured-bedrock permeability and controlling-mineral properties are required
- 2D cross-section, not the final Gounsa raster implementation

# 최종 판정
**강한 후보: chemical weathering-front production law.**

Use only if Gounsa explicitly models C/Cr weathering-front advance. Do not confuse it with Hartmann/LPJ dissolved weathering flux.

# 참고 링크 / DOI
https://doi.org/10.1002/2016JF003914
