# New vegetation candidate screen without cycling

Date: 2026-09-23
Updated: 2026-09-23 after PREBAS, GO+ and aDGVM lineage audit

# 목적
기존 FATES, LPJ-GUESS, MEDFATE, FORMIND, ED2, HETEROFOR, SEIB-DGVM, LandscapeDNDC, JULES-RED 등 이미 검토된 모델을 반복 검색하지 않고, repository에 없던 새 계열만 조사한다.

# 이번에 실제로 새로 검토한 계열
1. ForSAFE-Veg + ForSAFE-2D
2. JSBACH4 forest-age tiles
3. LPJ-wsl v2.0 age classes
4. PREBAS
5. GO+ v3.0
6. aDGVM / aDGVM2 / 2D-aDGVM

추가 방법론 benchmark:
- Gustafson et al. (2024) cohort canopy occupancy and gap representation

CARAIB와 ORCHIDEE-MICT는 1차 검색에서 확인했으나 아직 기존 top shortlist를 바꿀 근거가 없어 이번 확정판에서는 보류한다.

# strict five-criteria result

| lineage | 1 spatial cohort/hybrid | 2 understory succession | 3 soil-state coupling | 4 terrain/catchment | 5 <= daily | 판정 |
|---|---|---|---|---|---|---|
| ForSAFE-Veg + ForSAFE-2D | **FAIL** | **STRONG-PARTIAL** | STRONG | **YES actual forest hillslope** | **YES daily** | process comparator |
| JSBACH4 forest-age | WEAK-PARTIAL | WEAK-PARTIAL | PARTIAL | FAIL for fine target | fast land physics | reject |
| LPJ-wsl v2.0 | PARTIAL | WEAK-PARTIAL | PARTIAL | WEAK | daily ecosystem processes available | reject |
| PREBAS | PARTIAL | **FAIL** | MODERATE | WEAK | daily fluxes, annual structure | reject |
| GO+ v3.0 | PARTIAL, individual stand | PARTIAL: dynamic homogeneous understorey | STRONG-PARTIAL | **FAIL lateral terrain** | **VERY STRONG hourly/daily** | process comparator |
| **aDGVM2 lineage** | **PARTIAL-STRONG but full individual** | **VERY STRONG** | STRONG local / MODERATE external | **YES-PARTIAL** via 2D-aDGVM topography | **YES daily** | **conditional candidate** |

# 가장 중요한 새 결론

## 1. 기능의 분산은 실제 문헌 구조임
ForSAFE family:
```
explicit ground vegetation
+ soil moisture/light/rooting-depth competition
+ actual forest hillslope
+ daily lateral hydrology
```
까지는 만족하지만 demographic cohort가 없다.

PREBAS와 GO+:
```
daily or hourly ecohydrology
+ tree structure
+ some ground vegetation
```
를 제공하지만 ground vegetation이 endogenous herb/shrub demographic succession이 아니다.

JSBACH4와 LPJ-wsl:
```
age-class demography
+ fast land-surface/ecosystem processes
```
는 있지만 actual fine terrain cohort와 explicit forest-floor succession이 약하다.

따라서 기존 shortlist가 우연히 좁아진 것이 아니라, 현재 문헌에서 필요한 기능들이 서로 다른 model families에 분산되어 있다는 결론이 더 강해졌다.

## 2. aDGVM2는 이번 batch의 유일한 신규 conditional candidate
aDGVM2는 다음을 실제 dynamic process로 가진다.
- grass
- tree
- shrub
- annual/perennial grass
- individual growth
- reproduction
- mortality
- trait-based competition
- root shape and depth
- water competition
- daily plant state/ecophysiology

또한 2D-aDGVM 2014는:
- spatially explicit landscape
- topographic heterogeneity
- seed dispersal
- fire spread
를 구현했다.

그러나 두 계열을 하나로 합쳐 말하면 안 된다.

```
2D-aDGVM 2014 spatial branch
!=
modern aDGVM2 hydraulic/trait branch
```

고운사에서 modern aDGVM2 ecology + 2D spatiality + external hydrology를 합치면 **새로운 coupling/code integration**이다.

aDGVM2의 현재 약점:
1. full individual-based computation
2. latest applications are representative 1 ha stands
3. direct lateral watershed hydrology 없음
4. published external soil-state overwrite interface 없음
5. tropical/savanna development history
6. Korean temperate calibration burden

따라서 top production shortlist를 교체하지 않고 바로 아래 conditional candidate로 둔다.

# broad VDM search saturation

Eckes-Shephard et al. (2025)의 vegetation-demography-model comparison이 다룬 주요 9개 계열은 다음과 같다.

- BiomeE
- BiomeEP
- CABLE-POP
- ED
- FATES
- JULES-RED
- LPJ-GUESS
- ORCHIDEE demographic lineage
- SEIB-DGVM

이 계열들은 모두 이미 고운사 repository에서 검토되었다.

따라서 이후 조사에서 generic "demographic vegetation model" 이름 수집의 우선순위를 낮춘다. 명백한 mainstream VDM을 빠뜨렸기 때문에 shortlist가 좁은 가능성은 현재 상당히 낮다.

# Gustafson et al. 2024의 의미
LANDIS-II PnET-Succession에서 cohort가 cell 전체를 채운다고 가정하지 않고 proportional canopy occupancy와 persistent gap을 표현하는 방법을 제안한다.

이는 사용자가 요구한:
```
full individual tree
보다 가볍고
ordinary nonspatial cohort
보다 공간적으로 명시적인
middle representation
```
의 좋은 방법론 benchmark다.

하지만:
- herb/shrub demographic understory
- <=daily structural succession
- lateral hillslope hydrology
를 해결하지 않으므로 새 production engine 후보는 아니다.

# shortlist 영향

현재 production top tier:
1. **LPJ-GUESS SEC/PPA + PF-style external hydrology**
2. **FATES + ELM/ParFlow host**
3. **MEDFATE + medfateland**

바로 아래:
4. **aDGVM2 lineage: conditional candidate / strongest biological benchmark**
5. FORMIND-mHM: same-patch demographic herb layer가 확인될 때 재승격

# 재검색 금지

다음 조건이 없는 한 아래 계열을 다시 broad-search하지 않는다.

## ForSAFE
- age/size cohort extension
- tree/shrub/herb demographic recruitment extension
- ForSAFE-2D와 cohort vegetation의 published direct integration

## JSBACH4
- actual fine-resolution terrain/catchment cohort implementation
- explicit understory herb/shrub demography

## LPJ-wsl
- fine catchment/hillslope application with explicit demographic understory
- PF-LPJG보다 직접적인 soil-terrain state exchange

## PREBAS
- endogenous herb/shrub demographic recruitment
- lateral hillslope hydrology extension

## GO+
- species/cohort-resolved herb/shrub understorey
- actual lateral hillslope/catchment implementation

## aDGVM2
- modern aDGVM2 spatially explicit 2D version
- distributed/catchment hydrology coupling
- cohort/super-individual computational mode
- temperate postfire herb-shrub-tree application

# 다음 조사 방향

이제 broad model-name search보다 다음 조합만 겨냥한다.

```
ground-vegetation demographic cohorts
+ woody cohorts or efficient hybrid
+ daily/subdaily ecophysiology
+ actual terrain cells
+ lateral hillslope/catchment hydrology
```

특히 published model coupling 또는 model family 내부 extension이 있는지 확인한다.

# 관련 파일
- `models/ForSAFE_Veg_2D.md`
- `models/JSBACH4_ForestAge.md`
- `models/LPJ_wsl_2_0.md`
- `models/PREBAS.md`
- `models/GOplus.md`
- `models/aDGVM_aDGVM2_2D.md`
- `papers/2019_Belyazid_ForSAFEVeg.md`
- `papers/2021_Zanchi_ForSAFE2D.md`
- `papers/2020_Nabel_JSBACH4_ForestAge.md`
- `papers/2021_Calle_LPJwsl_AgeClasses.md`
- `papers/2024_Gustafson_CohortGapDynamics.md`
- `papers/2023_Makela_PREBAS_ForestManagement.md`
- `papers/2020_Moreaux_GOplus.md`
- `papers/2009_Scheiter_aDGVM_Africa.md`
- `papers/2013_Scheiter_aDGVM2_CommunityEcology.md`
- `papers/2014_Blanco_2DaDGVM.md`
- `papers/2017_Langan_aDGVM2_SouthAmerica.md`
- `papers/2022_Pfeiffer_aDGVM2_LandscapeRangeland.md`
- `papers/2025_Langan_aDGVM2_HydraulicDiversity.md`
