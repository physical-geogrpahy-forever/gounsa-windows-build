# 서지정보
Peters, D. P. C. (2002). Plant species dominance at a grassland–shrubland ecotone: an individual-based gap dynamics model of herbaceous and woody species. Ecological Modelling, 152(1), 5–32. https://doi.org/10.1016/S0304-3800(01)00460-4

# 이 논문을 찾은 이유
고운사에서 초본과 목본을 동시에 개체 또는 집단 수준으로 계산하면서, 뿌리깊이와 토양수분을 명시적으로 연결하고 공간격자 사이 종자산포까지 포함하는 오래된 hybrid/gap model이 있는지 확인하기 위해 검토했다.

# 연구 유형
- mixed-lifeform individual-based gap dynamics model
- grassland–shrubland ecotone vegetation dynamics
- soil-water and vegetation competition coupling

# 모델명
ECOTONE

# 공간 구조
- 작은 plot에서 individual plants의 recruitment, growth, mortality를 계산
- herbaceous and woody lifeforms를 동시에 표현
- multiple plots를 grid로 배열하고 seed dispersal로 연결 가능
- individual root distribution과 resource availability by soil depth가 dynamic

# 적용 환경
- 미국 New Mexico Sevilleta National Wildlife Refuge
- shortgrass steppe–Chihuahuan desert transition
- perennial grasses와 shrub dominance 전이

# 핵심 과정
- recruitment
- growth
- mortality
- individual root distribution
- soil-water competition by depth
- species/life-form competition
- seed dispersal between plots in spatial runs
- soil and climate effects on dominance

# 시간 구조
매우 중요하게 세 과정의 시간해상도가 다르다.

- plant recruitment, growth, mortality: **annual timestep**
- soil water content: **daily timestep**
- nitrogen: **monthly timestep**

따라서 daily soil-water calculation이 있다는 이유로 vegetation demography가 daily라고 해석하면 안 된다.

# 토양 및 뿌리
ECOTONE의 강점이다.

- individual plant root distributions are dynamic
- soil water availability is represented by depth
- species can partition water spatially and temporally in soil profile
- soil texture and climate affect recruitment and competition through soil water

이는 단순 WHC scalar보다 훨씬 강한 belowground competition precedent다.

# 고운사에 사용할 수 있는 부분
1. herbaceous + woody mixed-lifeform competition을 한 gap model에서 구현한 선례
2. root distribution by depth + daily soil water의 직접 결합
3. seed dispersal로 여러 plots를 spatially 연결하는 구조
4. 고운사 초본-관목 경쟁의 아래지상부 수분경쟁 설계 참고

# 필요한 새로운 coupling
- annual plant demography를 daily/event-sensitive structure로 변경
- forest tree canopy strata and litter pools
- actual terrain cells and DEM routing
- external hydrology overwrite/state exchange
- dynamic soil geometry remapping
- temperate postfire herb–shrub–tree parameterization

# 한계
- primary system은 semiarid grassland–shrubland ecotone이며 forest succession model이 아님
- vegetation recruitment/growth/mortality는 annual
- actual hillslope/catchment routing이 아니라 plots connected by seed dispersal
- full forest canopy cohort architecture가 없음
- external terrain/hydrology coupler precedent가 확인되지 않음

# 다섯 기준 판정
1. spatial cohort/hybrid: **STRONG-PARTIAL**. individual mixed lifeforms and connected grid of plots, but not native terrain grid.
2. explicit understory succession: **STRONG for grass–shrub interaction**, but forest tree succession is outside original scope.
3. soil-state coupling: **STRONG local belowground biology; PARTIAL external coupling**. daily layered water exists but no published external state overwrite.
4. terrain/catchment precedent: **FAIL/PARTIAL**. spatial plots exist, routed terrain does not.
5. <=daily vegetation response: **FAIL for demography**. soil water daily, plant recruitment/growth/mortality annual.

# 최종 판정
- production shortlist 미진입
- FATE-HD보다 belowground water/root representation이 강한 **mixed-lifeform biology benchmark**
- daily storm-driven structural feedback requirement 때문에 최종 engine으로는 부적합

# 참고 링크 / DOI
- https://doi.org/10.1016/S0304-3800(01)00460-4
