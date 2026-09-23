# ECOTONE

업데이트: 2026-09-23

# 모델 성격
Peters (2002)의 ECOTONE은 herbaceous and woody lifeforms를 하나의 individual-based gap dynamics framework에서 계산하는 mixed-lifeform model이다.

고운사 관점에서 특별한 점은 단순 grass cover와 shrub cover를 경쟁시키는 것이 아니라:
- individual recruitment, growth, mortality
- dynamic root distributions
- soil-water availability by depth
- daily soil-water balance
- plots linked by seed dispersal
를 함께 가진다는 점이다.

# 시간 구조
```text
daily    : soil water
monthly  : nitrogen
annual   : plant recruitment, growth, mortality
```

이 시간구조는 **자동 탈락 사유가 아니다.**
고운사 criterion 5의 핵심은 environmental / physiological / ecohydrological response가 적어도 daily scale에서 가능하느냐이며, demographic scheduling이 annual인 경우에는 별도로 표시한다.

따라서 ECOTONE은 다음처럼 해석하는 것이 타당하다.

```text
fast state
 daily soil water
 root-zone water competition
 external terrain/hydrology state

slow state
 annual background recruitment
 annual background growth
 annual background mortality
```

100년 규모 succession에서는 woody growth와 background recruitment를 연 1회 갱신하는 것이 반드시 문제는 아니다. 특히 나무 줄기크기, 수관 크기, 장기 population structure 같은 변수는 일별 구조 갱신의 필요성이 낮다.

# 고운사에서 필요한 event-driven 예외
문제가 되는 것은 6시간 폭우, 산사태, 침식/퇴적처럼 **구조를 즉시 바꾸는 사건까지 다음 연말까지 기다리는 경우**다.

따라서 production coupling에서는 background demography와 disturbance update를 분리하는 것이 가장 자연스럽다.

```text
hourly/subdaily geomorphic event
 -> erosion/deposition/landslide/root exposure/burial
 -> immediate disturbance operator
      plant removal or damage
      root-zone truncation
      cover reduction
      soil-layer remapping
 -> daily soil-water/root competition resumes
 -> annual background recruitment/growth/mortality
```

즉 annual demography를 전부 daily로 재작성할 필요는 없다.

## immediate event operator가 필요한 변수
- erosion depth
- deposition depth
- active soil depth
- exposed/buried root fraction
- uprooted or removed individuals
- canopy/ground-cover loss from direct disturbance
- root-accessible soil volume

## annual update에 남겨도 되는 변수
- background woody diameter/height increment
- background seed production and recruitment
- density-dependent mortality
- slow root-distribution adjustment
- long-term competitive replacement

# 공간 구조
- small gap plots
- individual herbaceous and woody plants
- grid of plots can be linked by seed dispersal
- belowground resources resolved by soil depth

그러나 actual DEM-based terrain routing이나 catchment hydrology는 native feature가 아니다.

# criterion assessment
| criterion | 판정 |
|---|---|
| 1 spatial cohort/hybrid | **STRONG-PARTIAL**: mixed-lifeform individuals and connected plots, but not native terrain grid |
| 2 explicit understory succession | **STRONG for herb–woody transition**; original forest-tree canopy scope is limited |
| 3 soil/terrain state coupling | **STRONG local root-water process, PARTIAL external coupling** |
| 4 terrain/catchment | **FAIL/PARTIAL**: spatial plots but no routed terrain |
| 5 <=daily | **PARTIAL-ACCEPTABLE**: daily soil water and resource response, annual background demography |

# criterion 5에 대한 수정 판정
이전 기록의 `FAIL because demography is annual`은 지나치게 엄격했다.

고운사에서 필요한 것은 모든 population process를 하루마다 실행하는 것이 아니라:
1. storm 이후 바뀐 soil/water state가 빠르게 vegetation stress에 전달되고
2. 직접적인 geomorphic disturbance는 event-driven으로 즉시 반영되며
3. 느린 background succession은 annual update로 계산되는 구조다.

이 구조라면 ECOTONE의 annual demography는 충분히 사용할 수 있다.

# 고운사에서 가치
- roots-by-depth와 mixed-lifeform soil-water competition benchmark
- herb/shrub belowground competition 설계 참고
- fast hydrology + slow demography operator splitting의 직접적인 선례
- event-driven geomorphic disturbance를 추가하기 쉬운 conceptual architecture

# production candidate로 남는 문제
1. original target은 semiarid grassland–shrubland ecotone이고 temperate forest canopy model이 아님
2. actual terrain/catchment hydrology가 없음
3. external soil-water overwrite/state exchange implementation이 확인되지 않음
4. forest tree canopy strata, litter, woody debris가 top-tier forest models보다 약함
5. individual-based representation의 계산비용을 고운사 grid 규모에서 확인해야 함

# 현재 판정
**benchmark-only에서 conditional candidate로 한 단계 상향한다.**

단, LPJ-GUESS, FATES, MEDFATE를 곧바로 대체하지는 않는다. 다음을 확인해야 한다.
- woody functional types가 temperate shrub/tree까지 얼마나 일반화 가능한가
- external hydrology state를 얼마나 쉽게 overwrite할 수 있는가
- gap plots를 actual terrain cells로 대응시킬 수 있는가
- event-driven erosion/deposition/root-damage operator를 삽입할 수 있는가

# 재검색 조건
앞으로 broad model-name search는 하지 않고 다음 항목만 targeted audit한다.
- ECOTONE source/code availability
- exact woody species/generalization structure
- soil-water state variables and restart/update interface
- descendants or forest applications

# 관련 논문
- `papers/2002_Peters_ECOTONE.md`
