# 서지정보
Hong, M., Chaney, N., Malyshev, S., Zorzetto, E., Preucil, A., & Shevliakova, E. (2025). LM4-SHARC v1.0: resolving the catchment-scale soil–hillslope aquifer–river continuum for the GFDL Earth system modeling framework. Geoscientific Model Development, 18, 2275–2301. https://doi.org/10.5194/gmd-18-2275-2025

# 이 논문을 찾은 이유
LM4.1의 PPA cohort vegetation을 실제 유역, 사면, 지하수, 하천 구조와 연결할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- model development and catchment evaluation
- LM4 hydrology extension

# 공간 구조
- HydroBlocks hierarchical multivariate clustering
- macroscale cell을 topography/soil 등 특성이 유사한 terrain tiles로 세분
- characteristic hillslope/height-band style spatial units
- hilltop, midslope, riparian, stream continuum
- regular 10 m vegetation raster가 아니라 지형을 압축한 spatial tiles

# 적용 환경
- Providence headwater catchment, Southern Sierra Nevada
- 약 1 km2 산지 headwater forest catchment
- 실제 topography, riparian convergence, streamflow observations 사용

# 핵심 과정
- unsaturated soil water
- hillslope groundwater/aquifer
- groundwater convergence/divergence
- two-way exchange between unsaturated soil and groundwater
- stream/river exchange
- surface energy and soil temperature

# 토양과 토심
- soil column and hillslope aquifer explicitly represented
- LM4 framework uses vertically discretized soil hydrology
- catchment application represents deep soil/bedrock water storage and groundwater-table dynamics

# 시간 구조
- LM4 physical land processes operate at subdaily time step, baseline LM4.1 atmospheric physics step 30 min
- SHARC is embedded in this hydrologic time integration

# 식생 구조와 연결
SHARC itself is a hydrologic extension. Vegetation demographic capability comes from LM4.1:
- PFT/size/age/rooting-depth cohorts
- PPA upper and lower canopy layers
- fine-root distributions
- tree/grass competition
- daily biomass/mortality

Therefore LM4-SHARC should be interpreted as LM4.1 cohort ecology plus catchment-scale hydrology, not as a separate succession model.

# 고운사에 직접 사용할 수 있는 부분
1. cohort land model and catchment soil-groundwater-stream continuum in one model family
2. topographic position controls on soil-water storage and riparian convergence
3. subdaily hydrology suitable for storm-event environmental feedback
4. explicit soil profile/rooting depth architecture

# 새로운 coupling이 필요한 부분
- hourly/subhourly erosion and DEM evolution
- erosion/deposition-driven soil-depth remapping
- fire-spall and coarse-fragment dynamics
- fine actual 10–25 m vegetation raster if terrain-tile compression is inadequate

# 한계
- geographic explicitness is HydroBlocks/terrain tiles, not preservation of every DEM cell.
- current LM4.1 PFT suite is less explicit for shrub understory than FATES.
- seedbank/seedling recruitment is simpler than FATES-TRS.

# 엄격 5조건 판정
1. 공간명시 cohort: 통과 with caveat. Real topographic terrain tiles, not regular fine raster.
2. 하층식생/천이: strong PPA layering and tree/grass demography, but shrub and recruitment detail weaker than FATES.
3. 토심/WHC: 매우 강함.
4. 유역/지형: 매우 강함. Direct headwater catchment application.
5. 시간간격: 통과. Subdaily/30-min physical hydrology with daily vegetation demography.

# 최종 판정
- 최상위 통합후보 중 하나
- 공간적으로 every-cell explicit하지 않은 점과 shrub understory weakness가 핵심 제약
