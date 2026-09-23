# GO+ v3.0

업데이트: 2026-09-23

# 왜 검토했는가
고운사 vegetation engine에서 중요한 두 조건인 fast ecohydrology와 explicit understorey biomass를 동시에 가지는 새 계열인지 확인했다.

# 모델 구조
```
hourly atmosphere
      |
      v
tree overstorey
+ dynamic understorey
+ soil water / soil carbon
```

GO+ v3.0는 보통 1 ha forest plot을 계산하며 gridded regional upscaling이 가능하다.

# 식생 표현
## Tree layer
- individual trees
- foliage, branch, stem, bark, stump
- taproot, coarse root, small root, fine root
- regeneration, mortality, thinning and harvesting

## Understorey layer
- spatially homogeneous layer
- foliage biomass
- root biomass
- perennial biomass
- perennial pool includes rhizomes, seeds or woody understorey parts
- daily growth and mortality

따라서 understorey는 정적 cover가 아니다.

그러나:
```
dynamic homogeneous understorey biomass
!=
species/cohort-resolved herb-shrub succession
```

# 시간해상도
- core energy/water/C flux: hourly
- understorey growth/mortality: daily
- tree foliage growth: daily
- most woody structural growth: annual

# 공간/수문
- local plot, typically 1 ha
- regional grid upscaling possible
- soil water and groundwater state validation
- lateral hillslope/catchment routing is not the core model

# 고운사 5개 기준 판정
| 기준 | 판정 | 이유 |
|---|---|---|
| 1 spatial cohort | PARTIAL | tree individuals are explicit in stand state but not a geographic cohort-grid architecture |
| 2 explicit understory succession | **PARTIAL** | daily dynamic biomass and roots, but one homogeneous layer without species/cohort herb-shrub succession |
| 3 soil-topography coupling | STRONG-PARTIAL | fast soil-water feedback is strong; external geomorphic state replacement not demonstrated |
| 4 hillslope/catchment | **FAIL** | plot/regional grid model, no lateral hillslope routing precedent identified |
| 5 <= daily | **VERY STRONG** | hourly core, daily understorey |

# 강점
- fast timestep
- dynamic roots and understorey biomass
- vegetation-soil feedback
- open Python code
- long-term forest rotations

# 고운사에서 탈락하는 이유
초기 postfire succession을 여러 herb/shrub/tree demographic populations의 recruitment/competition으로 나타내지 않는다.
또한 storm-driven topographic redistribution과 lateral water flow가 없다.

# 관련 논문
- `papers/2020_Moreaux_GOplus.md`

# 최종 판정
**secondary process comparator**

fast-time-step understorey benchmark로 유지하되 strict shortlist에는 넣지 않는다.
