# FORMIND + mHM + GRASSMIND lineage

## 현재 판정
2026-09-23 재검토에서 FORMIND는 기존 예상보다 훨씬 강한 후보로 상승했다.

핵심 수정사항:
- FORMIND는 완전 개별목만 강제하는 모델이 아니다.
- 현재 문서의 `par.plantCohortsEnabled`는 cohort approach를 켜며 기본값이 true이다.
- 같은 patch 안에서 같은 type과 size인 tree들은 하나의 cohort로 요약될 수 있다.
- cohort는 type, 동일 tree 수 N, age, single-tree size/AGB로 정의된다.
- water logic는 model의 큰 time increment와 무관하게 daily로 실행된다.
- GPP도 daily 계산 경로를 갖는다.
- 2026 FORMIND-mHM은 실제 Selke catchment에서 FORMIND와 distributed hydrologic model mHM을 양방향 결합했다.

따라서 criteria 1, 3, 4, 5는 매우 강하다.

남은 결정적 약점은 criterion 2이다.
FORMIND의 woody recruitment/succession은 강하지만 native forest run 안의 herbaceous understory demography는 아직 확인되지 않았다. GRASSMIND v2.0은 현재 FORMIND codebase에 integrated되어 있으나, 공개 문헌은 이를 별도의 **grassland model**로 사용하며 tree canopy와 herbaceous individuals를 한 forest patch에서 동시에 돌린다는 증거는 아직 찾지 못했다.

## 고운사 5조건
| 기준 | 판정 | 근거 |
|---|---|---|
| 1. 공간명시 cohort | **STRONG** | 실제 quadratic patches + default cohort mode. 같은 patch의 same type/size trees를 type, N, age, size로 묶음. 필요하면 individual mode 가능 |
| 2. explicit understory + succession | **WOODY STRONG / HERB UNRESOLVED** | woody seed production, dispersal, seed pool, germination, seedlings, gap succession은 강함. GRASSMIND는 herbaceous demography가 강하나 forest understory로 동시 실행되는지는 미확인 |
| 3. soil-topography coupling readiness | **VERY STRONG** | native layered soil/water + soil depth/FC/PWP/root traits. 2026 mHM external hydrology coupling이 직접 구현됨 |
| 4. catchment/topography precedent | **VERY STRONG** | FORMIND-mHM 2026 Selke river catchment, Central Germany, mixed deciduous catchment, 약 40% forest |
| 5. <= daily | **STRONG** | `growth.calcDailyGpp()`; water logic는 timestep과 무관하게 매일 `calcDailyWaterForAllPatches` 실행. demographic/structural update는 더 느릴 수 있음 |

## 1. 공간구조와 cohort
FORMIND simulation area는 위치가 명시된 regular quadratic patches로 구성된다.
전형적인 forest-gap application에서는 약 20 m x 20 m patch가 사용된다.

현재 documentation의 cohort 정의:
- same patch
- same type
- same size
인 trees를 cohort로 묶는다.

cohort state:
- PFT/type
- number of identical trees N
- age
- size / aboveground biomass of one tree

`par.plantCohortsEnabled`:
- default = 1, cohort approach 활성
- 0이면 cohort 하나가 single plant

따라서 고운사의 요구인
```text
개별목 모델보다는 가볍고
landscape grid 안에서 size/age cohort를 유지
```
에 매우 잘 맞을 수 있다.

## 2. woody succession
FORMIND 3.x recruitment는 두 경로를 지원한다.
1. external/global seed influx
2. simulated mother plants의 seed production/dispersal

patch마다 seed pool이 존재한다.

현재 parameter/documentation에 확인되는 요소:
- maturity age
- mother-plant seed production
- dispersal kernel and max/mean distance
- seed mass
- seed survival/mortality
- germination rate
- germination time in days
- irradiance requirement for establishment
- seedling size/height
- maximum seedlings per patch
- density-dependent seedling mortality

즉 woody succession은 단순 age-class 교체가 아니라
```text
mother plants
 -> seeds
 -> spatial dispersal
 -> patch seed pools
 -> germination
 -> seedlings
 -> light/space competition
 -> cohorts
```
구조를 가진다.

산불, treefall, landslide, logging 등으로 gap이 생기면 환경이 달라지고 recruitment와 competition을 통해 forest succession이 진행된다.

## 3. criterion 2 핵심: GRASSMIND와 forest understory
### 확인된 사실
GRASSMIND는 species-rich herbaceous communities의 structure/dynamics를 계산하는 individual/process-based grassland model이다.

2026 Kantzenbach et al. 논문은 GRASSMIND v2.0이 **FORMIND forest model code에 integrated**되어 있다고 명시한다.

현재 FORMIND documentation에도 `grassmindEnabled` 관련 파라미터가 등장하며, process code는 `if (timer.isBeginOfYear() || par.grassmindEnabled)` 같은 분기를 가진다.

GRASSMIND 자체는 다음이 강하다.
- individual herbaceous plants
- species/PFT competition
- vertical light layers
- crowding mortality
- seed/recruitment dynamics
- daily process calculations
- litter transfer
- soil-water limitation

### 아직 확인되지 않은 사실
그러나 다음은 아직 published/native feature로 확인되지 않았다.

```text
FORMIND tree cohorts
+
GRASSMIND herbaceous individuals/cohorts
simultaneously in the same forest patch
```

LISA program description도 FORMIND를 forest component, GRASSMIND를 grassland component로 별도 표기하며 향후 LandTrans landscape에서 연결한다.

따라서 현재는 `grassmindEnabled` 또는 shared codebase를 근거로 **forest herbaceous understory가 이미 완전 구현되었다고 주장하지 않는다.**

현재 criterion 2 판정:
- woody understory/seedling succession: STRONG
- true herbaceous forest understory succession: UNRESOLVED / likely custom integration required

이 한 항목이 해결되면 FORMIND-mHM은 top-tier 후보가 될 가능성이 크다.

## 4. 시간구조
현재 FORMIND process-order documentation:
- recruitment/establishment
- mortality
- light competition
- `growth.calcDailyGpp()`

또한 `runIntermediateProcesses()`는 simulation time increment가 무엇이든 하루씩 loop하면서
`growth.calcDailyWaterForAllPatches(dayIndex)`를 실행한다.

따라서 environmental response는 daily이다.

고운사의 폭우/지형변화 문제에 대해:
```text
storm or geomorph update
 -> soil-water/state update
 -> next daily FORMIND water/GPP calculation
```
의 architecture가 가능하다.

완전 hourly physiology는 아니다.

## 5. soil / root / water
FORMIND current input parameters에는 다음이 있다.
- `Water_SD`: soil depth [m]
- `Water_LayerDepth`: layer thickness [m]
- `Water_SoilLayer`: layer count
- soil file by patch
- field-capacity / permanent-wilting-point related water states
- PFT-specific minimum soil water for unstressed uptake
- rainfall duration [hours]
- group-specific WUE
- rooting-depth parameters
- root lifespan [days]
- specific root length
- shoot-root ratio
- root biomass from stem biomass relationship

즉 기준 3은 native soilDepth 자체 때문이 아니라 **soil-water state와 roots가 physiology에 연결되어 있기 때문에** 강하다.

Dynamic erosion/deposition으로 soil geometry가 변하는 기능은 별개이며 고운사에서는 새로운 state-remapping coupling이 필요하다.

## 6. FORMIND-mHM 2026
Bruns et al. 2026은 FORMIND를 distributed hydrologic model mHM과 결합했다.

적용:
- Selke river catchment, Central Germany
- mixed deciduous catchment
- forest cover 약 40%
- catchment discharge + stand-scale forest GPP/ET feedback

결과의 핵심:
- coupled model의 discharge performance가 standalone mHM과 비슷
- ET partitioning은 크게 바뀜
- transpiration fraction Et/ET가 0.50에서 0.73으로 증가해 관측범위와 가까워짐
- seasonal GPP-discharge relationship이 여러 gauge에서 나타남

이 논문은 다음의 direct precedent이다.
```text
distributed catchment hydrology
 <->
 forest demographic model
```

따라서 criterion 3과 4는 더 이상 추정이 아니라 published implementation으로 볼 수 있다.

## 7. coupling infrastructure
UFZ FINAM framework는 FORMIND와 mHM을 step-wise component로 연결하는 데 사용된다.
FINAM 논의 문서에서는 soil-water variable 하나를 주고받는 FORMIND-mHM coupling의 overhead가 standalone 대비 약 5% 수준이었다고 보고한다.

이것은 고운사에서 외부 geomorphic/soil component를 연결할 때 구조적 장점이다.

다만 dynamic soil geometry, root exposure/burial, DEM connectivity를 FORMIND state에 반영하는 부분은 별도 구현이다.

## 8. fire / disturbance
현재 FORMIND parameter set에는 fire module이 존재한다.
- fire frequency
- severity
- fire size
- PFT fire tolerance

공식 FORMIND 소개는 treefall뿐 아니라 fire, landslide, logging, drought 등으로 gaps가 생기고 light-demanding species가 establish하는 forest succession을 설명한다.

따라서 고운사 postfire 100-year problem과 conceptual fit은 매우 좋다.

## 9. roots and geomorph interface
FORMIND current parameters provide:
- root biomass relationship
- rooting depth
- root lifespan
- specific root length
- shoot-root ratio

이는 다음 고운사 bridge에 유리하다.
```text
cohort/PFT root biomass
 + rooting-depth function
 + specific root length
 -> layer RLD / root mass
 -> erosion resistance / bioturbation interface
```

그러나 horizontal/3D root architecture는 native output이 아니며 별도 spatialization이 필요하다.

## 10. 고운사 soil-geometry event coupling
기준 3A는 매우 강하게 충족한다.

기준 3B는 새로운 coupling이다.
침식/퇴적으로 layer geometry가 바뀔 때 최소 다음을 remap해야 한다.
- soil water
- soil carbon/nutrient pools if activated
- root biomass/root length by layer
- litter/surface pools
- tree/seedling anchoring and exposure/burial state

FORMIND-mHM이 hydrology state exchange를 이미 구현했다는 것은 큰 장점이지만, geomorphic geometry remapping까지 기존 논문에 구현된 것은 아니다.

## 11. 현재 shortlist에서의 위치
criterion 2의 herbaceous forest understory를 제외하면 FORMIND-mHM은 현재 조사된 후보 중 구조적 적합성이 매우 높다.

비교:
- MEDFATE: 실제 spatial cells와 tree/shrub dynamics, coupling이 쉽지만 herb recruitment 불완전
- LPJ-GUESS hydrology lineages: tree/shrub/grass PFT demography가 강하고 catchment coupling precedent가 있으나 within-cell patches가 statistical
- FATES: demographic ecology가 가장 강하나 host stack이 무겁고 internal patches가 statistical
- FORMIND-mHM: actual patches + default cohort mode + woody seed demography + daily water/GPP + direct catchment coupling. 그러나 forest herbaceous understory 동시 실행 미확인

따라서 현재 FORMIND-mHM은 **조건부 top-tier**이다.

```text
IF concurrent tree + herbaceous understory demography is native or straightforward
 -> top-tier shortlist
ELSE
 -> very strong woody-forest comparator, criterion 2 때문에 최종 1순위 불가
```

## 다음 검증 우선순위
1. `grassmindEnabled`가 forest tree types와 동시에 실행 가능한지 source/config level에서 확인
2. FORMIND-mHM coupling의 exact exchange timestep과 soil-water variables 확인
3. mHM grid ↔ FORMIND patch scaling 확인
4. temperate German/Korean species parameterization 접근성 확인
5. restart/state injection과 dynamic soil-depth remapping 난이도 확인
6. 10–25 m vegetation patch 규모 계산비용 확인

## 핵심 문헌/문서
- Fischer et al. (2016), FORMIND model lineage/key description.
- FORMIND current documentation, 2026: general concept, recruitment, mortality, process order, input parameters.
- Bruns, N., Huth, A., Thober, S., & Fischer, S. M. (2026). Combining an individual-based dynamic vegetation model with a distributive hydrologic model to improve coupled water-carbon modelling. EGUsphere preprint. https://doi.org/10.5194/egusphere-2026-4918
- Kantzenbach, M., König, S., Reitz, T., Schädler, M., & Taubert, F. (2026). Synergizing grassland and soil system model expertise by coupling GRASSMIND (v2.0) and BODIUM (v1.2). EGUsphere preprint. https://doi.org/10.5194/egusphere-2026-1713
- UFZ LISA project documentation, 2026.
