# 서지정보
Ouyang, C., et al. (2023). *Mechanistic Analysis and Numerical Simulation of the 2021 Post-Fire Debris Flow in Xiangjiao Catchment, China*. Journal of Geophysical Research: Earth Surface, 128, e2022JF006846. DOI: 10.1029/2022JF006846.

# 이 논문을 찾은 이유
실제 산불 산지에서 2D shallow-water hydraulics와 rainfall/flow-driven erosion, deposited-layer shielding, multi-size sediment를 함께 사용하는 model이 Iber+/Wu보다 더 적합한지 확인하기 위해 검토했다.

# 연구 유형
- coupled numerical model
- postfire runoff erosion to debris-flow transition
- event-scale catchment simulation

# 공간 구조
- shallow-water equations for surface flow
- DEM resolution 10 m in application
- catchment-scale spatial model
- multi-process coupled framework

# 적용 환경
- Xiangjiao catchment, China
- steep mountain landscape
- coniferous forest/shrub
- postfire debris-flow event

# 핵심 과정
- rainfall
- infiltration
- raindrop detachment
- flow entrainment
- re-detachment/re-entrainment
- deposition
- deposited-layer shielding
- five sediment-size classes
- surface-flow dynamics
- transition toward debris flow

# 식생 입력
- vegetation cover C_v
- throughfall coefficient
- LAI distribution
- fire severity maps affect hydrologic/soil initial conditions
- root biomass/RLD direct input 없음

# 핵심 식
The erosion component adopts Hairsine-Rose.

For each particle class, it distinguishes:
- rainfall detachment from original soil
- rainfall redetachment from deposited layer
- runoff entrainment from original soil
- runoff re-entrainment from deposited layer
- deposition

Shielding:
a deposited-layer state H limits access to original soil as deposited sediment mass accumulates.

The application initializes a 4 cm fire-disturbed topsoil as a deposited/loose surface layer.

Surface flow uses shallow-water equations based on mass and momentum conservation.

# 파라미터와 단위
- deposited-layer sediment mass: kg m^-2
- particle classes: five
- detachability coefficients
- excess stream-power entrainment fraction
- vegetation cover
- throughfall coefficient
- infiltration/soil parameters by burn severity

# 원 논문의 구현 범위
Postfire runoff, erosion, sediment entrainment and debris-flow initiation are modeled mechanistically at catchment scale.

# 고운사에 직접 사용할 수 있는 부분
Very important postfire structural precedent:
```
fire-disturbed loose surface layer
+ raindrop detachment
+ flow entrainment
+ deposited-layer shielding
+ size-selective sediment
+ SWE
```

This may be particularly relevant to Gounsa because fire can create/leave a loose surface layer and exposed coarse material.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root/litter quantities replacing C_v/LAI or controlling Hairsine-Rose detachability would be **new coupling**.

# 한계
- vegetation effect remains cover/LAI-based
- no dynamic root biomass/RLD erosion resistance
- model focus extends to debris-flow formation, beyond ordinary hillslope erosion
- event-scale rather than 100-year eco-geomorphic recovery

# 최종 판정
- **strong postfire engine benchmark**
- not a complete quantitative-vegetation solution
- Hairsine-Rose deposited-layer structure should be directly compared against Iber+ loose-layer formulation before final engine selection

# 참고 링크 / DOI
https://doi.org/10.1029/2022JF006846
