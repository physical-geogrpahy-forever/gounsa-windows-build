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
세 과정의 시간해상도가 다르다.

- plant recruitment, growth, mortality: **annual timestep**
- soil water content: **daily timestep**
- nitrogen: **monthly timestep**

중요한 재판정:
고운사 criterion 5는 모든 demographic process가 daily일 것을 요구하는 것이 아니라, environmental/physiological/ecohydrological response가 최소 daily scale에서 가능해야 하며 demographic scheduling은 별도로 평가한다.

따라서 ECOTONE의 annual recruitment/growth/mortality는 **자동 탈락 사유가 아니다.**

고운사에 적용할 경우 다음 operator splitting이 가능하다.

```text
subdaily/hourly geomorphic-hydrologic event
 -> updated soil depth / moisture / erosion-deposition state
 -> immediate disturbance operator for direct damage
 -> daily soil-water and root competition
 -> accumulated stress
 -> annual background recruitment/growth/mortality
```

이렇게 하면 woody background dynamics는 연 1회 유지하면서도 폭우, 침식, 매몰, 뿌리노출처럼 즉시 구조를 바꾸는 사건만 event-driven으로 처리할 수 있다.

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
5. fast hydrology + slow demography를 분리한 coupling architecture

# 필요한 새로운 coupling
- actual terrain cells and DEM routing
- external hydrology overwrite/state exchange
- dynamic soil geometry remapping
- event-driven direct disturbance operator
- forest tree canopy strata and litter pools
- temperate postfire herb–shrub–tree parameterization

annual plant demography 전체를 daily로 재작성하는 것은 필수사항이 아니다.

# 한계
- primary system은 semiarid grassland–shrubland ecotone이며 forest succession model이 아님
- vegetation recruitment/growth/mortality는 annual
- actual hillslope/catchment routing이 아니라 plots connected by seed dispersal
- full forest canopy cohort architecture가 없음
- external terrain/hydrology coupler precedent가 확인되지 않음

# 다섯 기준 판정
1. spatial cohort/hybrid: **STRONG-PARTIAL**. individual mixed lifeforms and connected grid of plots, but not native terrain grid.
2. explicit understory succession: **STRONG for herb–woody interaction**, but forest-tree scope is limited in original application.
3. soil-state coupling: **STRONG local belowground biology; PARTIAL external coupling**. daily layered water exists but no published external state overwrite.
4. terrain/catchment precedent: **FAIL/PARTIAL**. spatial plots exist, routed terrain does not.
5. <=daily vegetation response: **PARTIAL-ACCEPTABLE**. daily soil-water/resource response, annual background demography.

# 최종 판정
- **conditional candidate / mixed-lifeform biology benchmark**
- 이전의 “annual demography이므로 최종 engine 부적합” 판정은 너무 엄격하여 철회
- 핵심 병목은 timestep보다 actual terrain hydrology, forest canopy generalization, external state exchange임

# 참고 링크 / DOI
- https://doi.org/10.1016/S0304-3800(01)00460-4
