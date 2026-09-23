# JSBACH4 forest-age tiles

업데이트: 2026-09-23

# 왜 검토했는가
individual-tree보다 가볍고 ordinary DGVM보다 demographic structure가 풍부한 새 middle-complexity model인지 확인했다.

# 핵심 구조
Nabel et al. (2020)은 JSBACH4의 hierarchical tile structure 아래 forest age classes를 추가했다.

- forest PFT
- age-class subtiles
- age-dependent photosynthesis/respiration 등
- exact forest age tracking
- management/disturbance에 따른 age-class transfer

# 고운사 5개 기준 판정
| 기준 | 판정 | 이유 |
|---|---|---|
| 1 spatial cohort | **WEAK-PARTIAL** | age classes는 subgrid tile fractions이며 실제 geomorphic x-y cohort가 아님 |
| 2 understory succession | **PARTIAL/WEAK** | PFT dynamics는 있으나 forest-floor herb/shrub demographic strata가 핵심 구조가 아님 |
| 3 soil-topography coupling | PARTIAL | land-surface soil state는 있으나 고운사식 external fine-terrain state exchange 선례가 약함 |
| 4 hillslope/catchment | **NO for target** | fine forest hillslope demographic application을 확인하지 못함 |
| 5 fast physiology | YES at land-surface level | 단, demographic age-class structure가 고운사 event coupling을 해결하지 않음 |

# 핵심 해석
JSBACH4의 forest-age scheme은 계산효율이 좋은 age bookkeeping이다. 그러나 사용자가 요구한 spatial cohort는 단순히 "나이가 여러 개 존재"하는 것이 아니라 실제 terrain cell과 연결되어 식생-지형 피드백을 받는 cohort이다.

따라서 이 모델은 그 의미의 criterion 1을 충족하지 않는다.

# 고운사에서의 가치
- efficient age-class transfer benchmark
- management/disturbance age bookkeeping 참고

# 새로운 coupling이 필요한 부분
- actual fine terrain cells
- explicit forest-floor herb/shrub demography
- lateral hillslope water redistribution
- erosion/deposition soil remap

# 관련 논문
- `papers/2020_Nabel_JSBACH4_ForestAge.md`

# 최종 판정
**탈락**

새 top-tier 후보로 다시 조사하지 않는다. 새로운 fine-scale cohort/hillslope extension이 발견될 때만 재검토한다.
