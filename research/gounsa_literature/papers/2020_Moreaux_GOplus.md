# 서지정보
Moreaux, V., Martel, S., Bosc, A., Picart, D., Achat, D., Moisy, C., Aussenac, R., Chipeaux, C., Bonnefond, J.-M., Figuères, S., Trichet, P., Vezy, R., Badeau, V., Longdoz, B., Granier, A., Roupsard, O., Nicolas, M., Pilegaard, K., Matteucci, G., Jolivet, C., Black, A. T., Picard, O., & Loustau, D. (2020). Energy, water and carbon exchanges in managed forest ecosystems: description, sensitivity analysis and evaluation of the INRAE GO+ model, version 3.0. Geoscientific Model Development, 13, 5973–6009. https://doi.org/10.5194/gmd-13-5973-2020

# 이 논문을 찾은 이유
hourly forest ecohydrology와 dynamic understorey biomass를 동시에 가지면서 individual-tree보다 단순한 고운사 vegetation engine 후보인지 확인하기 위해 검토했다.

# 연구 유형
- process-based forest ecosystem model
- model description, sensitivity analysis, evaluation

# 공간 구조
- typically 1 ha forest plot
- regional gridded upscaling 가능
- tree overstorey + understorey + soil
- actual lateral hillslope routing은 없음

# 적용 환경
- temperate managed forests
- Douglas fir, European beech, maritime pine 등

# 핵심 과정
- hourly radiation and energy balance
- evapotranspiration
- photosynthesis and respiration
- soil water
- tree growth and mortality
- understorey growth and mortality
- soil carbon
- management, regeneration, thinning, clearcut, coppicing

# 식생 입력과 상태
Tree layer:
- collection of individual trees
- foliage, branches, stem, bark, stump, taproot, coarse/small/fine roots

Understorey:
- homogeneous layer
- foliage
- roots
- perennial compartment, including rhizomes/seeds/woody understorey parts

# 시간해상도
- whole model core: hourly
- tree foliage growth: daily
- tree stem/branch/root structural growth: annual
- understorey biomass growth and mortality: daily

# 핵심 식
Understorey compartment growth is resolved daily as the minimum of demand and carbon-supply functions. The paper gives a sigmoid phenological demand formulation and separate foliage/root/perennial pools.

# 파라미터와 단위
- hourly meteorological forcing
- soil water-holding capacity and rooting-depth related parameters
- tree and understorey biomass pools
- exact parameters are species/site specific and must be checked in supplementary tables before use

# 원 논문의 구현 범위
- complete hourly soil-vegetation-atmosphere water/energy/C exchange
- dynamic understorey biomass
- tree regeneration and management
- forest rotations over decades
- gridded regional upscaling

# 고운사에 직접 사용할 수 있는 부분
- very strong fast-time-step benchmark
- understorey foliage/root/perennial biomass partition
- daily understorey root and biomass dynamics
- rapid water-stress feedback between soil and vegetation

# 새로운 coupling이 필요한 부분
- species-resolved herb/shrub demographic cohorts
- natural herb -> shrub -> tree postfire succession
- actual terrain-cell lateral hydrology
- event-driven erosion/deposition soil geometry remap

# 한계
- tree layer is an individual-tree collection rather than the desired cohort middle ground.
- understorey is one homogeneous layer rather than multiple demographic species/cohorts.
- version 3.0 is mainly monospecific even-aged forest; irregular mixed stands were future development.
- no direct hillslope/catchment lateral-water application identified.

# 최종 판정
- secondary process comparator
- fails strict criterion 2 and 4
- does not displace LPJ-GUESS SEC, FATES, or MEDFATE

# 참고 링크 / DOI
- https://doi.org/10.5194/gmd-13-5973-2020
- model code DOI: https://doi.org/10.15454/5K9HCS
