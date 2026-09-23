# 서지정보
Haga, C. et al. (2022). Modeling tree recovery in wind-disturbed forests with dense understory species under climate change. Ecological Modelling. DOI and full bibliographic details to be completed from the canonical paper record.

# 이 논문을 찾은 이유
10 m actual-grid LANDIS-II application where dense understory is represented as a true cohort/species rather than an empirical cover modifier.

# 연구 유형
- forest landscape simulation
- disturbance-recovery and understory competition

# 공간 구조
- LANDIS-II landscape grid
- study area approximately 136 km²
- 10 m x 10 m spatial analysis/application reported
- species-age cohorts in each geographic cell

# 적용 환경
- Japanese temperate forest
- wind-disturbed forest recovery
- dense Sasa understory

# 핵심 과정
- tree cohort succession
- Sasa understory competition
- establishment, dispersal, vegetative reproduction and resprouting
- NECN carbon, nitrogen, water and biomass processes

# 하층식생 구현 확인
The public Project-LANDIS-Understory repository confirms that `sasa_spp` is treated as a normal LANDIS species/cohort rather than a simple LAI modifier.

Species-level attributes include:
- longevity = 1000 yr
- maturity = 1 yr
- shade tolerance
- fire tolerance
- effective and maximum seed dispersal distance
- vegetative reproduction probability
- sprout age limits
- post-fire regeneration = resprout

Initial communities contain entries such as `sasa_spp 11 (1870)`, confirming an explicit age cohort with biomass.

# NECN root/litter/CN participation
The modified NECN parameter file gives `sasa_spp` the same physiological/biogeochemical parameter structure as tree species, including:
- leaf lignin
- fine-root lignin
- wood lignin
- coarse-root lignin
- leaf C:N
- fine-root C:N
- wood C:N
- coarse-root C:N
- litter C:N
- fine-root fraction
- coarse-root fraction
- monthly maximum NPP
- maximum biomass

Therefore Sasa enters the actual NECN biomass, root, litter and C/N pathways.

# 토양/수문
- spatial SoilDepthMap
- drainage, baseflow, stormflow, field capacity, wilting point maps
- sand/clay fractions
- initial SOM C/N pools
- dead coarse roots and surface deadwood pools

# 시간해상도
- NECN ecosystem calculations include monthly physiology/biogeochemistry
- LANDIS succession timestep in the project = 1 yr
- therefore fails the Gounsa criterion requiring <=1 day event-aware vegetation/environment updates

# 고운사에 직접 사용할 수 있는 부분
- strongest precedent identified for 10 m actual geographic grid + East Asian temperate forest + explicit dense understory cohort + tree cohorts + root/litter/CN + dispersal/regeneration
- demonstrates that understory species can be represented as full LANDIS/NECN cohorts rather than generic grass cover

# 새로운 coupling이 필요한 부분
- hourly/daily geomorph-event state updating
- immediate soil-depth change after erosion/deposition
- short-timescale root exposure/burial and mortality

# 한계
- ecosystem timestep too coarse for Gounsa storm-event coupling
- landscape scale computational setup is much larger than local stand models
- Sasa-specific biology is not equivalent to Korean postfire herb/shrub community, though the structural precedent is highly relevant

# 최종 판정
- critical structural precedent, not final Gounsa engine
- passes criteria 1,2,3,4 strongly
- fails criterion 5

# 코드 근거
- https://github.com/hagachi/Project-LANDIS-Understory
