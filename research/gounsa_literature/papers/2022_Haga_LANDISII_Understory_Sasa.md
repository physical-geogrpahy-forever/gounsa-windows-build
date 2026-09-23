# 서지정보
Haga, C., Hotta, W., Inoue, T., Matsui, T., Aiba, M., Owari, T., Suzuki, S. N., Shibata, H., & Morimoto, J. (2022). Modeling Tree Recovery in Wind-Disturbed Forests with Dense Understory Species under Climate Change. Ecological Modelling, 472, 110072. https://doi.org/10.1016/j.ecolmodel.2022.110072

# 이 논문을 찾은 이유
동아시아 온대림에서 실제 공간격자와 species-age cohorts를 사용하면서 하층식생이 수목 재생과 장기천이에 직접 경쟁하는 선례를 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- forest landscape succession
- post-disturbance recovery

# 공간 구조
- LANDIS-II raster landscape
- 10 m x 10 m grid cells
- cohorts are spatially explicit at cell level
- stems within a cell are assumed uniformly distributed and not individually located

# 적용 환경
- Oshima-Hiyama National Forest, southern Hokkaido, Japan
- 2016 typhoon windthrow-disturbed temperate/hemiboreal forest
- dense understory dwarf bamboo Sasa kurilensis

# 핵심 과정
- seed dispersal
- cohort establishment
- biomass growth and mortality
- understory competition
- post-disturbance forest recovery
- postfire/vegetative resprouting parameters also exist in species definition

# 식생 입력
Sasa was implemented as a real LANDIS-II/NECN species-age cohort rather than a cover multiplier.
Repository source files confirm that `sasa_spp` has:
- age and biomass in initial communities
- longevity and maturity
- shade tolerance
- fire tolerance
- effective and maximum seed dispersal distance
- vegetative reproduction probability
- sprout ages
- post-fire resprouting
- FRoot lignin
- CRoot lignin
- FRoot C:N
- CRoot C:N
- fine-root fraction
- coarse-root fraction

Thus Sasa participates in NECN biomass/root/litter/C/N pathways.

# 토양/수문
NECN input includes spatial maps for:
- SoilDepth
- drainage
- baseflow
- stormflow
- field capacity
- wilting point
- sand/clay
- surface and soil SOM C/N pools
- dead wood and dead coarse roots

# 시간 구조
- LANDIS-II succession timestep in this implementation: 1 year
- NECN ecosystem physiology/hydrology is monthly internally
- therefore this model does not satisfy the desired daily/hourly event-coupling criterion.

# 고운사에 직접 사용할 수 있는 부분
- unusually direct East Asian precedent for 10 m actual geographic cells
- dense understory species can be modeled as full age-biomass cohort
- understory can have roots, litter and C/N properties
- explicit tree establishment and long-term competition with understory
- soil depth and WHC-related maps exist spatially

# 새로운 coupling이 필요한 부분
- subdaily/hourly geomorphic storm feedback
- erosion/deposition-driven soil depth update between storms
- conservative remapping of soil/root pools after geomorphic change

# 한계
- monthly ecosystem processes are too coarse for the user's strict criterion 5
- Sasa is one dominant understory life form rather than a diverse herb/shrub community
- landscape model architecture is comparatively heavy

# 최종 판정
- strong structural precedent and serious fallback candidate
- strongest evidence identified for criteria 1–4 in an East Asian forest
- fails strict criterion 5 because ecosystem calculations are monthly rather than daily/hourly

# 참고 링크 / DOI
- https://doi.org/10.1016/j.ecolmodel.2022.110072
- source project: https://github.com/hagachi/Project-LANDIS-Understory
