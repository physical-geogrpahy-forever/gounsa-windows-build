# 서지정보
Shevliakova, E., Malyshev, S., Martinez-Cano, I., Milly, P. C. D., Pacala, S. W., Ginoux, P., et al. (2024). The Land Component LM4.1 of the GFDL Earth System Model ESM4.1: Model Description and Characteristics of Land Surface Climate and Carbon Cycling in the Historical Simulation. Journal of Advances in Modeling Earth Systems, 16, e2023MS003922. https://doi.org/10.1029/2023MS003922

# 이 논문을 찾은 이유
고운사의 엄격 조건인 cohort demography, 상층/하층 구조, 뿌리와 토양수분, subdaily physiology를 동시에 만족하는 land model인지 확인하기 위해 검토했다.

# 연구 유형
- land/Earth-system model description
- second-generation vegetation demographic model

# 공간 구조
- LM4 grid cell 내부에 dynamic subgrid tiles
- tile 내부에 vegetation-type, size, rooting depth, age가 같은 식물을 cohort로 묶음
- PPA에 따라 cohort가 여러 canopy layers를 emergently 형성
- geographic raster cell 안의 subgrid demographic tiles이며 개별 tree x,y는 추적하지 않음

# 적용 환경
- global land-model applications
- LM4-SHARC와 결합될 경우 headwater catchment/hillslope hydrology로 확장 가능

# 핵심 과정
- PPA cohort competition for light and water
- dynamic canopy layering
- recruitment, growth, mortality
- daily fire disturbance
- plant hydraulics
- hydrology and soil carbon

# 식생 입력/상태
- leaves
- fine roots
- reproductive pool
- nonstructural carbohydrates
- sapwood
- heartwood
- cohort size/height
- cohort age
- cohort-specific rooting depth

# 하층식생과 천이
- tall cohorts form upper canopy, shorter cohorts form lower/understory layers by PPA
- cohorts are dynamically rearranged among canopy layers as vegetation changes
- tree and grass vegetation can coexist and compete for light and water in natural vegetation tiles
- current ESM4.1 PFT set includes C3/C4 grasses and multiple tree PFTs
- shrub PFT was not identified in the 2024 baseline paper
- recruitment is explicit but simpler than FATES-TRS seedbank/seedling ecology

# 토심/수문
- soil hydrology and thermodynamics use vertically discretized soil columns
- cohort-specific fine-root biomass follows an exponential vertical distribution
- water uptake is resolved for each cohort by soil layer
- rooting depth is a cohort property

# 시간 구조
- energy, water and CO2 exchange: 30 min
- biomass growth and mortality: daily
- fire: daily
- some land-use processes: daily to annual

# 고운사에 직접 사용할 수 있는 부분
1. PPA cohort architecture with emergent upper/understory layers
2. cohort-specific fine roots and rooting depth
3. 30-minute hydrology/physiology and daily demography
4. natural grass/tree competition
5. LM4-SHARC provides a published path to catchment/hillslope application

# 새로운 coupling이 필요한 부분
- fine-resolution GIS raster/hydrology if LM4-SHARC HydroBlocks are insufficient
- geomorphic DEM/soil-depth updates after storms
- Korean temperate shrub/herb parameterization
- erosion/deposition/root-exposure state remapping

# 한계
- baseline model has no verified shrub PFT in the 2024 paper.
- spatial representation is subgrid tile/cohort, not a 10 m actual vegetation raster.
- recruitment is less explicit than FATES Tree Recruitment Scheme.

# 엄격 5조건 판정
1. 공간명시 cohort: 중상. geographic grid + subgrid tiles, but not fine raster per cohort.
2. 하층식생/천이: 강함 for PPA tree/grass layers, weaker for shrub diversity and seedbank ecology.
3. 토심/WHC: 강함.
4. 유역/지형: LM4.1 alone moderate; LM4-SHARC makes it strong.
5. 시간간격: 통과. 30 min physics, daily demography.

# 최종 판정
- 채택 후보
- LM4-SHARC와 함께 볼 때 고운사의 cohort-hillslope architecture에 매우 가까운 통합 후보
