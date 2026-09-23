# 서지정보
Hudjetz, S., Lennartz, G., Krämer, K., Roß-Nickoll, M., Gergs, A., & Preuss, T. G. (2014). Modeling Wood Encroachment in Abandoned Grasslands in the Eifel National Park – Model Description and Testing. PLOS ONE, 9(12), e113827. https://doi.org/10.1371/journal.pone.0113827

# 이 논문을 찾은 이유
고운사에서 full individual-tree model보다 단순하면서도 초본, 관목, 교목의 초기 천이를 공간적으로 명시하고 하루 이하 시간간격으로 계산하는 forest/landscape hybrid가 기존 문헌에 있는지 확인하기 위해 검토했다.

# 연구 유형
- 공간명시적 식생천이 모델 개발 및 검증
- herbaceous compartment model + woody individual-based model의 multimodel coupling

# 공간 구조
- raster-based landscape
- published application에서 최대 약 1,500 ha, 150,000 cells
- 이는 약 100 m2/cell, 즉 대략 10 x 10 m cell에 해당
- 각 cell에서 초본 식생과 개별 관목/교목이 함께 계산됨
- 목본은 height, crown diameter, cover, age와 위치를 갖는 개체로 표현

# 적용 환경
- 독일 Eifel National Park의 abandoned semi-natural grassland와 wood encroachment
- 산림 내부보다는 초지에서 관목 및 교목으로 진행되는 초기 천이에 초점

# 핵심 과정
- herbaceous species cover dynamics
- woody seed production and dispersal
- seed decay
- germination
- individual woody growth
- self-thinning
- browsing
- mowing, grazing, trampling
- wild-boar disturbance
- herbaceous layer에 의한 woody seed/recruitment inhibition
- woody canopy/cover 확대에 따른 herbaceous space 감소

# 식생 입력
- herbaceous species 또는 species groups의 cover
- woody species-specific growth and life-history parameters
- 개별 목본의 height, crown diameter, cover, age
- land-use and browsing settings
- initial vegetation and neighborhood seed sources

# 핵심 시간구조
논문은 simulation balance를 daily increments로 반복하며 100년 규모 simulation을 수행한다.

그러나 중요한 제한이 있다.

- daily meteorological forcing으로 구동되지 않는다.
- landscape state의 핵심 갱신은 yearly scale이다.
- seasonal variability를 명시적으로 계산하지 않는다.
- space가 light, nutrient, water 등의 여러 resource를 묶은 proxy로 사용된다.

따라서 단순히 `daily timestep`이라는 이유만으로 FATES나 LPJ-GUESS의 daily ecophysiology와 동급으로 해석하면 안 된다.

# 파라미터와 단위
- herbaceous cover: 면적 또는 % cover
- woody height: m
- crown diameter 및 crown area
- age: yr
- cell area: application 기준 약 100 m2
- daily iteration, yearly landscape-development interpretation

# 고운사에 사용할 수 있는 부분
1. **초기 천이 구조의 매우 좋은 방법론적 선례**
   - 초본 layer와 관목/교목을 하나의 spatial raster에서 직접 상호작용시킨다.
   - 특히 초본 litter/cover가 woody recruitment를 억제하고, woody expansion이 herbaceous area를 줄이는 양방향 interaction이 명시적이다.
2. 10 m 규모 raster와 100년 simulation이 이미 실제 구현되었다.
3. full forest individual-tree physiology보다 훨씬 단순한 hybrid 구조이므로 계산비용 관점에서 참고 가치가 크다.

# 필요한 새로운 coupling
고운사 생산모델로 사용하려면 다음이 새로 필요하다.

- external soil water content/potential 또는 water table state 입력
- soil-layer/root-depth representation
- storm-driven terrain/soil change와의 state exchange
- meteorology-driven photosynthesis/transpiration/water stress
- 산림 상층 canopy light와 하층 microclimate의 보다 기작적인 계산

# 한계
- soil water balance 또는 lateral hydrology가 없다.
- water, nutrient, light가 상당 부분 `space` proxy로 압축된다.
- daily weather forcing이 없다.
- herbaceous layer는 cover-based compartment이며 age/size demographic cohort는 아니다.
- forest-understorey model보다는 grassland-to-woodland succession model이다.
- 최신 LandS 배포는 source code가 아니라 executable 중심이라 coupling 확장성이 제한된다.

# 다섯 기준 판정
1. spatial cohort/hybrid: **STRONG-PARTIAL**. 실제 raster + woody individuals, herb cover populations.
2. explicit understory succession: **STRONG**. herb, shrub, tree interaction과 recruitment가 직접 표현됨.
3. external soil/terrain state coupling: **FAIL in published implementation**. mechanistic soil-water state interface 없음.
4. terrain/catchment precedent: **PARTIAL**. 실제 landscape GIS는 강하지만 routed hillslope/catchment hydrology는 아님.
5. <= daily response: **PARTIAL**. daily iteration은 존재하나 daily meteorological/ecophysiological response가 아님.

# 최종 판정
- **새로운 biological/spatial succession benchmark**
- current production top tier를 대체하지 않음
- 특히 MEDFATE의 herb recruitment extension 또는 LPJ/FATES의 초기 herb-woody interaction 설계에 참고할 가치가 큼

# 참고 링크 / DOI
- https://doi.org/10.1371/journal.pone.0113827
