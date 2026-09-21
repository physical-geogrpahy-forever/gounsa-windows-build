# 서지정보
Stolze, L., Dwivedi, D., Steefel, C., Molins, S., Dong, W., Beutler, C., et al. (2026). Model-Based Interpretation of Solute Exports and Carbon Partitioning During Shale Weathering in a Mountainous Hillslope. *Water Resources Research, 62*, e2025WR041597. DOI: 10.1029/2025WR041597.

# 이 논문을 찾은 이유
사면 topography, transient hydroclimate, soil respiration, unsaturated flow, gas exchange, 다광물 반응을 한 2D mountain-hillslope model에서 동시에 계산하는 최신 사례를 찾기 위해 검토했다.

# 연구 유형
- multidimensional multiphase reactive transport model
- field-constrained numerical modeling
- transient hydro-biogeochemical simulation

# 공간 구조
- 2D mountainous hillslope
- 92,880 active cells
- horizontal resolution 1 m
- vertical resolution 0.2 m
- variably saturated subsurface
- gas + aqueous phases

# 적용 환경
- snow-dominated Rocky Mountain hillslope, Colorado
- Cretaceous Mancos shale
- sedimentary-rock Critical Zone

# 핵심 과정
- variably saturated flow
- snowmelt infiltration
- lateral drainage
- soil CO2 dynamics
- gas-water exchange
- carbonate weathering
- silicate weathering
- pyrite oxidation
- petrogenic organic carbon oxidation
- aqueous solute export
- carbon partitioning

# 식생 입력
dynamic vegetation model은 없다.

하지만 model explicitly includes:
- transient soil respiration
- soil-derived CO2

따라서 vegetation/soil-biological forcing이 chemical weathering에 직접 들어가는 최신 hillslope precedent다.

고운사에서는 soil respiration source를 LPJ-GUESS belowground/root-litter states로 바꾸는 것이 새로운 coupling이다.

# 핵심 수치모델
PFLOTRAN 기반.

모델은:
- partially saturated water flow
- multicomponent reactive transport
- multiphase gas-water exchange
를 transient하게 계산한다.

Primary/secondary/gas species:
- 20 primary species
- 26 secondary aqueous species
- O2(g), CO2(g), N2(g), N2O(g)

# 핵심 결과

## hydroclimate
snowmelt:
```
CO2-rich water infiltration
 -> deeper delivery
 -> carbonate / silicate reactions
```

## topography
steeper slope:
```
enhanced lateral drainage
 -> lower near-surface saturation
 -> stronger O2 gas diffusion
 -> deeper reactant delivery
 -> localized higher weathering rates
```

sharp topographic features의 streamline divergence도 dissolved O2/CO2를 deeper reactive zones로 전달할 수 있다.

## biological forcing
transient soil respiration이 weathering driver로 포함된다.

따라서:
```
soil respiration
+ transient hydrology
+ slope geometry
 -> spatial mineral reaction pattern
```
이라는 직접 mountain-hillslope numerical precedent다.

# 파라미터와 단위
- grid: dx=1 m, dz=0.2 m
- variably saturated hydraulic parameters
- soil respiration forcing
- gas diffusion/transfer
- mineral kinetic/thermodynamic parameters
- transient temperature
- aqueous/gas species concentrations

# 원 논문의 구현 범위
full transient mountain-hillslope hydro-biogeochemical model.

공개:
- model inputs/results via ESS-DIVE
- augmented PFLOTRAN source code archived in Zenodo

따라서 reproducibility가 매우 높다.

# 고운사에 직접 사용할 수 있는 부분
**현재까지 발견한 가장 강한 spatial chemical-weathering engine precedent 중 하나.**

특히:
```
slope
 -> lateral drainage
 -> saturation
 -> gas transport
 -> CO2/O2 delivery
 -> W_chem
```
을 명시적으로 계산한다.

또:
```
soil respiration
 -> CO2
 -> weathering
```
을 transient forcing으로 넣는다.

고운사에서:
```
LPJ-GUESS respiration
+ terrain
+ subsurface hydrology
 -> PFLOTRAN/BioRT-style chemistry
```
구조를 만들 수 있다.

# 새로운 coupling이 필요한 부분
- LPJ-GUESS -> transient soil/root respiration
- LPJ-GUESS root uptake -> variably saturated flow
- Landlab topography -> PFLOTRAN geometry/update
- sandstone-specific mineral network
- W_chem -> mobile-soil/bedrock mass balance

모두 새로운 coupling이다.

# 한계
- shale, not sandstone
- vegetation succession explicit 없음
- geomorphic topography itself does not evolve in the RTM
- very high computational cost
- fire/postfire process 없음

# 최종 판정
- **핵심 채택: 2D transient mountain-hillslope reactive-transport benchmark**
- BioRT/Wen/Xiao보다 더 complete한 multiphase comparison candidate
- first production chemistry engine으로 채택할지는 계산비용 때문에 별도 판단
- spatial hillslope-weathering validation engine으로 매우 강함

# 참고 링크 / DOI
https://doi.org/10.1029/2025WR041597
