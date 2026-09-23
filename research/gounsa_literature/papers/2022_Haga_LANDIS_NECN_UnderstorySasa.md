# 서지정보
Haga, C., Hotta, W., Inoue, T., Matsui, T., et al. (2022). Modeling Tree Recovery in Wind-Disturbed Forests with Dense Understory Species under Climate Change. Ecological Modelling, 472, 110072. https://doi.org/10.1016/j.ecolmodel.2022.110072

# 이 논문을 찾은 이유
동아시아 온대림에서 실제 fine raster에 하층식생 cohort와 tree cohort를 동시에 배치하고 장기 천이를 계산한 선례가 있는지 확인하기 위해 검토했다.

# 연구 유형
- spatial forest landscape simulation
- LANDIS-II NECN v6.3 extension application

# 공간 구조
- southern Hokkaido, Japan
- actual 10 m x 10 m grid
- landscape-scale raster cells
- tree species and understory Sasa represented as species-age cohorts
- cell-to-cell seed dispersal

# 적용 환경
- wind-disturbed temperate forest
- Oshima-Hiyama National Forest, southern Hokkaido
- dense Sasa kurilensis understory
- post-disturbance recovery under climate change

# 핵심 과정
- tree establishment and succession
- understory-tree competition
- seed dispersal
- vegetative reproduction
- resprouting
- biomass production
- C/N and litter pools through NECN

# 하층식생 구현
Sasa kurilensis is not a prescribed cover modifier. Public project inputs show `sasa_spp` as a normal LANDIS species with:
- longevity 1000 yr
- maturity 1 yr
- shade tolerance
- fire tolerance
- effective/max seed dispersal distance
- vegetative reproduction probability
- post-fire resprouting
- age/biomass cohorts in initial communities
- biomass-by-age outputs

NECN species/functional-group parameters for Sasa additionally include:
- fine-root lignin
- coarse-root lignin
- fine-root C:N
- coarse-root C:N
- fine-root fraction
- coarse-root fraction
- LAI/NPP parameters

Thus understory Sasa enters real biomass, root, litter and C/N pathways.

# 토양 요소
- raster soil depth map
- field capacity
- wilting point
- sand/clay fractions
- drainage/baseflow/stormflow parameters
- SOM pools

# 시간 구조
- NECN uses monthly ecosystem-process calculations within LANDIS-II succession framework
- this is the decisive mismatch to the Gounsa strict criterion of <=1 day

# 고운사에 직접 사용할 수 있는 부분
1. 10 m actual grid precedent
2. East Asian temperate forest understory-tree competition
3. understory species as full age/biomass/root/litter cohort
4. seed dispersal, resprouting and post-disturbance regeneration architecture
5. soil-depth/field-capacity/wilting-point spatial inputs

# 새로운 coupling이 필요한 부분
To use this ecological structure with Gounsa hourly geomorphology, a faster ecohydrology/physiology engine or extensive modification would be needed. Directly updating NECN soil state after each storm would be a new coupling and is not supported by this published setup.

# 한계
- monthly ecosystem timestep fails strict time criterion.
- landscape architecture is heavier than a local stand model.
- Sasa biology is not directly transferable to Korean postfire grasses/shrubs but provides a structural precedent.

# 엄격 5조건 판정
1. 공간명시 cohort: 매우 강함, 10 m actual raster.
2. 하층식생/천이: 매우 강함, full Sasa species-age cohort plus tree regeneration.
3. 토심/WHC: 강함, soil depth, FC, WP and other soil maps.
4. 유역/지형: spatial landscape and disturbance context, but not a fully coupled hillslope hydrology model.
5. 시간간격: 실패, monthly.

# 최종 판정
- 직접 생산모델 후보에서는 시간간격 때문에 보류
- 그러나 공간해상도, 동아시아 하층 cohort, tree-understory succession 설계의 핵심 선례로 채택
