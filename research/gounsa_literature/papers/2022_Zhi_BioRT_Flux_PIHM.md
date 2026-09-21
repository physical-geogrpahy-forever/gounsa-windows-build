# 서지정보
Zhi, W., Shi, Y., Wen, H., Saberi, L., Ng, G.-H. C., Sadayappan, K., Kerins, D., Stewart, B., & Li, L. (2022). BioRT-Flux-PIHM v1.0: a biogeochemical reactive transport model at the watershed scale. *Geoscientific Model Development, 15*, 315-333. DOI: 10.5194/gmd-15-315-2022.

# 이 논문을 찾은 이유
WITCH/PROFILE처럼 column/catchment chemistry에 강한 모델 외에, 지형과 수문에 더 직접적으로 연결되는 watershed-scale reactive transport model이 있는지 확인하기 위해 검토했다.

# 연구 유형
- watershed-scale hydro-biogeochemical numerical model
- coupled land-surface + hydrology + reactive transport

# 공간 구조
- distributed watershed
- shallow and deep subsurface zones
- surface runoff, subsurface lateral flow, deep flow
- spatially explicit watershed hydrology

# 적용 환경
- watershed / Critical Zone
- hydro-biogeochemical simulations

# 핵심 과정
Flux:
- surface energy balance
- evapotranspiration

PIHM:
- precipitation
- interception
- infiltration
- recharge
- surface runoff
- shallow lateral flow
- deep flow

BioRT:
- mineral dissolution / precipitation
- aqueous complexation
- surface complexation
- ion exchange
- plant nutrient uptake
- soil respiration
- microbial redox
- solute transport

# 식생 입력
- evapotranspiration and land-surface state
- plant nutrient uptake
- soil respiration terms
- land-surface forcing affecting soil temperature and water storage

정량 root biomass 또는 dynamic forest succession을 직접 제공하는 DGVM은 아니다.

# 핵심 식
BioRT는 hydrology가 계산한:
- soil temperature
- water storage
- water fluxes
를 받아 reactive transport를 계산한다.

Mineral reactions:
- kinetic mineral dissolution / precipitation
- equilibrium complexation and sorption

식생 및 생물학 관련:
```
plant nutrient uptake
+ soil respiration
+ microbial redox
 -> solute state
 -> mineral reaction environment
```

# 파라미터와 단위
- mineral kinetic rate constants
- reactive surface area
- soil temperature
- water content
- surface/subsurface flow
- plant uptake rates
- respiration parameters
- aqueous/solid species concentrations

# 원 논문의 구현 범위
watershed-scale reaction and transport를 land-surface/hydrology와 결합한다.

# 고운사에 직접 사용할 수 있는 부분
중요한 대안 계보다.

현재 고운사는:
- LPJ-GUESS
- SWEHR
- Landlab
을 2D 공간구조로 결합하려 한다.

BioRT-Flux-PIHM은:
```
topography / hydrology
 -> reactive transport
 -> plant uptake / respiration / weathering
```
을 watershed scale에서 이미 구현한 선례다.

따라서 WITCH를 grid cell별로 독립 적용하는 것보다 lateral hydrologic transport가 중요해질 경우 강한 대안/검증모델이 된다.

# 새로운 coupling이 필요한 부분
- PIHM vegetation representation을 LPJ-GUESS로 대체
- SWEHR/Landlab hydrologic/geometric state를 BioRT chemistry와 연결
- sandstone mineral assemblage 적용

모두 새로운 coupling이다.

# 한계
- LPJ-GUESS 같은 dynamic forest succession 없음
- direct root biomass/exudation detail은 REWTCrunch보다 약함
- geomorphic soil production thickness를 직접 계산하지 않음

# 최종 판정
- **채택 후보: watershed-scale spatial chemical-weathering engine / comparison model**
- B-WITCH보다 공간수문 coupling이 강하고, REWTCrunch보다 root chemistry는 단순함
- production core 대체 여부는 구현 난이도와 code integration 검토 후 결정

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-15-315-2022
