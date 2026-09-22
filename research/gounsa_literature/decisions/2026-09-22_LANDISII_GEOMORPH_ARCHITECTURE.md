# LANDIS-II + NECN 기반 고운사 지형모델 아키텍처

날짜: 2026-09-22

## 식생축
- LANDIS-II Core v8
- NECN Succession v8.x
- fire extension as needed

## LANDIS-II와 지형상태 연결 선례
Hotta et al. 2026:
```
slope / soil depth / soil moisture
 -> LANDIS-II establishment and recovery
```
단, dynamic erosion으로 soil depth를 갱신하는 양방향 지형모델은 아님.

## 과정별 existing geomorphic model 우선후보

### Water erosion
Iber+ 2024
- genuine 2D hydrodynamics
- rainfall detachment
- runoff detachment
- multiclass sediment
- loose layer/shielding

### Armour / embedded PSD / weathering
SSSPAM/mARM
- dynamic armour
- multilayer PSD
- subsurface resupply
- physical weathering
- soil profile
- SSSPAM own D8 empirical fluvial engine은 primary event erosion으로 사용하지 않음

### Tree throw / root-fracture soil production
Gabet & Mudd 2010
- tree population
- rootwad volume
- tree throw frequency
- root fracture
- soil creep

### Postfire dry ravel
Lamb et al. 2011
- vegetation sediment storage
- wildfire storage collapse
- vegetation recovery
- dry-ravel pulse

### Shallow landslide
Schwarz et al. 2010 Root Bundle Model
- root diameter classes
- root number
- root mechanics
- progressive pullout/failure

### Root vertical distribution helper
DyRoot 2019
- fine/coarse roots
- dynamic depth distribution
- multiple forest ecosystems
- no published LANDIS-II coupling

## excluded as production basis
- COPLAS
- WEPP cropland root multipliers
- DANSAT agricultural dynamics
- PROMET crop-oriented coupling
- ELM-Erosion global calibrated engine

## unresolved interfaces
1. NECN fine-root biomass -> forest RLD / architecture
2. NECN coarse-root biomass -> root diameter/rootwad distribution
3. NECN surface litter -> cover/contact area/roughness
4. root/litter states -> Iber+ erodibility
5. geomorphic soil-depth change -> NECN soil C/N pool remapping
6. fire severity -> sandstone spall production and PSD

## 원칙
Generic vegetation factor 금지.
각 LANDIS-II state는 기존 published relation/model 또는 독립 현장측정으로 물리량에 매핑한다.
