# 서지정보
Landuyt, D., Blondeel, H., Lorer, E., Perring, M. P., Steppe, K., & Verheyen, K. (2024). A trait-based modelling approach towards dynamic predictions of understorey communities in temperate forests. Ecological Modelling, 498, 110873. https://doi.org/10.1016/j.ecolmodel.2024.110873

# 이 논문을 찾은 이유
고운사에서 기존 forest models의 약점인 온대림 하층 초본의 동적 경쟁과 천이를 명시적으로 계산하는 별도 process-based understorey model이 있는지 확인하기 위해 검토했다.

# 연구 유형
- 새로운 process-based understorey community model 개발
- trait-based, cover-based, cohort-inspired approach
- temperate forest mesocosm validation

# 모델명
DynaFORb

# 공간 구조
- 개별 식물 대신 species-specific cover를 상태량으로 사용
- 한 simulation plot 내부 식물이 같은 resources를 경쟁한다는 가정
- 논문에서 권장하는 plot scale은 약 0.01–1 m2
- plant organ x species x height layer를 3-D arrays로 계산
- landscape x-y routing model은 아님

# 적용 환경
- 벨기에 Aelmoeseneie deciduous forest understorey mesocosm
- grasses, herbs, ferns, dwarf shrubs and tree saplings가 존재하는 temperate forest floor를 대상으로 개발

# 핵심 과정
- species-specific phenology
- daily aboveground biomass reconstruction from cover and height
- vertical light partitioning among understorey layers
- daily gross photosynthesis
- growth and maintenance respiration demand
- species performance from assimilation/demand ratio
- interspecific competition
- annual relative cover response

# 시간 구조
중요한 이중 시간구조가 있다.

- 내부 light, temperature, photosynthesis, biomass/performance calculations: **daily**
- main state variable인 species cover update/output: **yearly**

따라서 daily ecophysiological calculation은 존재하지만 post-storm 이후 실제 community cover가 즉시 구조적으로 갱신되는 모델은 아니다.

# 수분 및 토양 관련 판정
현재 버전은 경쟁과 performance에서 light를 주 자원으로 사용하고 temperature를 보조적으로 사용한다.
논문은 **water and nutrient competition are not accounted for yet**라고 명시한다.

따라서 다음 고운사 핵심 interface가 없다.
- soil moisture/potential by layer
- water table
- root-zone uptake
- lateral flow
- dynamic soil depth

논문 자체도 belowground processes가 주요 향후 개발 필요사항이라고 판단한다.

# 식생 입력 및 상태량
- species cover
- maximum height and phenology curve
- SLA
- leaf fraction
- shoot:root ratio
- leaf N
- photosynthetic parameters
- daily temperature and light forcing

# 고운사에 사용할 수 있는 부분
- 온대림 하층식생을 개체목이 아닌 **cover-based cohort-inspired community**로 계산하는 최신 방법론
- full individual herb model보다 계산량이 적으면서 species-specific competition을 유지하는 설계
- MEDFATE의 부족한 endogenous herb recruitment/succession을 보완할 때 참고할 수 있는 understorey competition structure
- LPJ/FATES에서 herbaceous PFT를 더 세밀한 temperate forest herbs로 확장할 때 참고 가능

# 필요한 새로운 coupling
- soil-water and nutrient competition module
- external geomorphic/hydrologic state exchange
- overstorey forest dynamics와의 양방향 coupling
- annual cover update를 daily/event-sensitive structural response로 세분화하려면 새 개발 필요
- recruitment, seed bank, dispersal을 landscape-scale로 명시화하려면 추가 개발 필요

# 한계
- standalone understorey model이며 tree overstorey demography engine이 아님
- main community state update가 annual
- water/nutrient competition absent
- landscape/catchment topology absent
- current validation은 full long-term succession prediction이 아니라 one-year performance vs observed cover change 중심

# 다섯 기준 판정
1. spatial cohort/hybrid: **WEAK-PARTIAL**. cohort-inspired cover structure는 있으나 geographic x-y vegetation cohorts가 아님.
2. explicit understory succession: **STRONG-PARTIAL**. species-level understorey competition은 매우 강하지만 seed/recruitment landscape demography는 제한적.
3. external soil/terrain state coupling: **FAIL currently**. water and nutrient competition 자체가 아직 없음.
4. terrain/catchment precedent: **FAIL**.
5. <= daily: **PARTIAL**. internal calculations daily, main cover state yearly.

# 최종 판정
- production engine 후보는 아님
- **temperate understorey biology benchmark**로 가치가 큼
- MEDFATE herb module 또는 다른 top-tier forest engine의 understorey extension 설계 참고문헌으로 보존

# 참고 링크 / DOI
- https://doi.org/10.1016/j.ecolmodel.2024.110873
- code reported by paper: https://github.com/DriesLanduyt/DynaForB
