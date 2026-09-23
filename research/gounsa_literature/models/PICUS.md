# PICUS model lineage

업데이트: 2026-09-23

## 현재 판정
**강한 tree-spatial/process benchmark, strict shortlist에서는 탈락.**

PICUS는 10 x 10 m 실제 상호작용 patch, 개별 수목, 3-D 수관광, 종자산포와 수목 재생을 결합하며 v2.0에서는 다층 토양과 일별 생리까지 갖춘다. 산악 이질경관 적용 선례도 매우 강하다.

그러나 고운사에서 핵심인 독립적인 herb/shrub demographic understory가 확인되지 않는다.

## 구조
PICUS v1.2/v1.4/v1.5:
- 10 x 10 m horizontal patches
- vertical canopy cells
- individual trees
- interacting patches through light and seed dispersal
- germination, establishment, growth, mortality
- heterogeneous alpine landscape applications

PICUS v2.0:
- v1.x spatial structure retained/refined
- vertical canopy resolution refined to 1 m
- arbitrary number of soil layers
- layer depth, soil type, retention curve, hydraulic conductivity
- vertical layer exchange according to Darcy law
- daily carbon gain and climate forcing
- annual allocation
- juvenile-tree seed production/distribution/recruitment inherited from v1.4

## 시간 구조
- daily: climate forcing, plant water status, photosynthesis/carbon gain in v2.0
- annual: resource allocation and major tree structural update
- tree demographic/successional trajectory is long-term

Thus criterion 5 is strong for physiological response but not an hourly vegetation-demography model.

## soil / water
v2.0 soil is much stronger than classic gap models:
- multilayer soil
- water retention curves
- hydraulic conductivity
- vertical Darcy flow
- plant available water controls tree water status and photosynthesis

However native fine hillslope lateral groundwater/runon routing is not established as part of the PICUS core.

## spatial / mountain precedent
Lexer & Hönninger (2001):
- several hectares
- spatially explicit multi-species forest
- heterogeneous alpine landscapes
- topographic shielding incorporated in direct/diffuse radiation
- Eastern Alps test

Later PICUS applications include mountain/protection-forest and Eastern Alps management studies.

This is a strong terrain-aware forest-dynamics precedent, although not an explicit catchment lateral-hydrology solver.

## roots
The v2.0 water module is rooted in plant water availability from soil layers, but the public model description reviewed here does not expose the same explicit cohort fine-root biomass/RLD interface as LandscapeDNDC, FATES or MEDFATE.

Therefore root-to-geomorph coupling would require source-level audit before assigning a strong criterion-3 rating.

## understory
PICUS represents juvenile/suppressed trees and regeneration under an overstory.

But this must not be confused with independent forest-floor vegetation demography.

No native, dynamically recruiting:
- herb layer
- grass layer
- shrub population layer

was confirmed in the standard PICUS lineage reviewed here.

Thus postfire:
```text
herb -> shrub -> tree
```
cannot be represented natively as three demographic life forms.

## 고운사 5조건
| criterion | verdict |
|---|---|
| 1 spatial cohort/hybrid | STRONG spatial, but individual-tree rather than cohort |
| 2 explicit understory succession | FAIL-PARTIAL: tree regeneration yes, herb/shrub demography no |
| 3 soil/root coupling | STRONG soil hydrology / root-state interface requires audit |
| 4 hillslope/topography | STRONG mountain landscape; WEAK-PARTIAL lateral catchment hydrology |
| 5 <= daily | STRONG physiology; slower allocation/demography |

## Gounsa role
PICUS is useful for:
- 10 m forest-gap spatial scale benchmark
- tree regeneration and spatial seed dispersal
- mountain topographic radiation effects
- multilayer soil-water/tree physiology

It does not replace FATES, JULES-RED, MEDFATE or LPJ-GUESS under the strict herb/shrub/tree requirement.

## key references
- Lexer, M. J., & Hönninger, K. (2001). A modified 3D-patch model for spatially explicit simulation of vegetation composition in heterogeneous landscapes. Forest Ecology and Management, 144, 43–65. https://doi.org/10.1016/S0378-1127(00)00386-8
- BOKU PICUS v1.2 and v2.0 official model documentation, accessed 2026-09-23.
- Irauschek et al. (2017). Evaluating multifunctionality and adaptive capacity of mountain forest management alternatives under climate change in the Eastern Alps. European Journal of Forest Research.
