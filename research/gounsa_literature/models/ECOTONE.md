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

따라서 고운사의 핵심 요구인 `storm -> changed soil state -> vegetation structural response`에서 soil-water stress는 빠르게 계산할 수 있지만 actual demographic state 변화는 annual이다.

# 공간 구조
- small gap plots
- individual herbaceous and woody plants
- grid of plots can be linked by seed dispersal
- belowground resources resolved by soil depth

그러나 actual DEM-based terrain routing이나 catchment hydrology는 native feature가 아니다.

# criterion assessment
| criterion | 판정 |
|---|---|
| 1 spatial cohort/hybrid | STRONG-PARTIAL |
| 2 explicit understory succession | STRONG for grass–shrub, forest tree scope limited |
| 3 soil/terrain state coupling | STRONG local root-water process, external overwrite unproven |
| 4 terrain/catchment | FAIL/PARTIAL |
| 5 <=daily | FAIL structural demography; daily soil water only |

# 고운사에서 가치
- roots-by-depth와 mixed-lifeform soil-water competition benchmark
- herb/shrub belowground competition 설계 참고
- `daily hydro + slower demographic structure`라는 architecture의 한계 비교용

# 왜 production shortlist에 들지 않는가
1. recruitment/growth/mortality annual
2. semiarid grassland–shrubland target
3. forest canopy structure weak
4. no direct distributed hillslope/catchment hydro
5. no published external geomorphic state remapping

# 재검색 금지
다음이 새로 확인되지 않는 한 재검토하지 않는다.
- <=daily vegetation demographic extension
- forest tree canopy/understorey extension
- routed hillslope/catchment coupling
- external soil-state interface

# 관련 논문
- `papers/2002_Peters_ECOTONE.md`
