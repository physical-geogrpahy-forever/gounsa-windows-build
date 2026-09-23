# FORMIND + mHM + GRASSMIND lineage

업데이트: 2026-09-23

## 현재 판정
FORMIND는 고운사 5조건 가운데 **1, 3, 4, 5가 매우 강한 조건부 상위 후보**이다.

핵심 장점:
- 완전 개별목만 강제하지 않으며 default cohort mode를 지원
- actual quadratic forest patches
- woody seed production, dispersal, germination, recruitment, mortality
- daily GPP와 daily water process
- fire/disturbance succession
- 2026 FORMIND-mHM에서 distributed catchment hydrology와 직접 결합

그러나 criterion 2의 herbaceous forest understory에 대해 source-level audit을 마쳤고, 현재 GRASSMIND integration을 **동일 forest patch 내 tree + herb 동시 실행의 증거로 사용할 수 없다고 확정**한다.

---

## 고운사 5조건
| 기준 | 판정 | 근거 |
|---|---|---|
| 1. 공간명시 cohort | **STRONG** | actual quadratic patches + default cohort mode. same patch/type/size trees를 cohort로 묶음 |
| 2. explicit understory + succession | **WOODY STRONG / HERB FAIL-PARTIAL** | woody recruitment/gap succession은 강함. GRASSMIND herb demography는 강하지만 current code path가 grass vs non-grass로 분기되어 same forest patch 동시 실행 근거가 없음 |
| 3. soil-topography coupling readiness | **VERY STRONG** | native soil/water state + 2026 mHM external hydrology coupling |
| 4. catchment/topography precedent | **VERY STRONG** | FORMIND-mHM Selke catchment |
| 5. <= daily | **STRONG** | daily GPP and daily water loop; structural demography slower |

---

## 1. 공간구조와 cohort
FORMIND simulation area는 위치가 명시된 regular quadratic patches로 구성된다. 전형적인 gap-model application은 약 20 m x 20 m patch를 사용한다.

현재 documentation의 cohort approach는 같은 patch 안의
- same plant type
- same size
인 나무들을 하나의 cohort로 묶는다.

cohort state에는 type, 동일 tree 수 N, age, size/AGB 등이 포함된다.

`par.plantCohortsEnabled`는 기본적으로 cohort approach를 활성화하며, 필요하면 individual mode도 가능하다.

따라서
```text
full individual tree보다 계산량을 줄이면서
실제 spatial forest patches 안에서 size/age structure 유지
```
라는 고운사 요구와 잘 맞는다.

---

## 2. woody succession
FORMIND recruitment는 global/external seed influx와 simulated mother plants의 seed production/dispersal을 지원한다.

확인되는 과정:
- maturity
- seed production
- dispersal kernel
- patch seed pool
- seed survival
- germination
- light requirement
- seedling state
- density-dependent seedling mortality
- growth and competition

즉 woody succession은
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
의 명시적 구조를 갖는다.

산불, treefall, landslide, logging 등으로 gap이 생긴 뒤 recruitment와 경쟁을 통해 woody succession이 진행될 수 있다.

---

## 3. GRASSMIND source-level audit: criterion 2 확정
### 확인된 사실
GRASSMIND는 species-rich herbaceous communities를 계산하는 process-based grassland model이며, 최신 버전은 FORMIND software/code infrastructure 안으로 통합되었다.

GRASSMIND 자체에는 다음이 있다.
- herbaceous plants
- species/PFT competition
- vertical light structure
- crowding mortality
- seed/recruitment processes
- daily processes
- litter transfer
- soil-water limitation

FORMIND documentation에도 `grassmindEnabled` 관련 parameter가 존재한다.

### 결정적인 source evidence
최신 FORMIND process-order source/documentation은 plant type에 따라 대략 다음과 같은 compile-time 분기 구조를 사용한다.

```cpp
if constexpr (isGrass<PlantWithTraitsType>) {
    // GRASSMIND/grass-specific process path
} else {
    // forest/non-grass FORMIND process path
}
```

즉 current implementation은 `grass type`과 `non-grass/tree type`을 같은 generic plant container 안에서 동시에 섞어 한 forest patch의 상층-하층으로 처리한다는 증거가 아니다. 오히려 **서로 다른 plant-type execution path를 공유 codebase에서 선택**하는 구조로 읽는 것이 타당하다.

또한 LISA/LandTrans 설명도 FORMIND를 forest component, GRASSMIND를 grassland component로 구분한다.

### 따라서 현재 판정
다음 주장은 금지한다.

```text
GRASSMIND is integrated into FORMIND code
therefore
FORMIND forest run already contains explicit herbaceous understory succession
```

현재 확인 가능한 정확한 표현은:

```text
FORMIND:
  explicit woody forest demography and succession = YES

GRASSMIND:
  explicit herbaceous demography = YES

simultaneous FORMIND tree cohorts + GRASSMIND herbaceous population
within the same forest patch = NOT demonstrated as native current mode
```

따라서 고운사 criterion 2는 **부분 충족**이며, forest herb layer를 반드시 요구한다면 custom integration이 필요하다.

---

## 4. 시간구조
FORMIND current process-order documentation은 daily GPP 계산 경로를 포함한다.

또한 intermediate-process loop는 simulation의 큰 structural timestep과 별개로 매일 water process를 수행한다.

따라서 고운사의 event architecture는 원칙적으로:
```text
storm / geomorphic event
 -> soil/hydrologic state update
 -> next daily FORMIND water/GPP response
```
로 만들 수 있다.

다만 완전 hourly plant physiology model은 아니다.

---

## 5. soil / root / water
현재 FORMIND input/state에는 다음 계열의 정보가 있다.
- soil depth
- layer thickness / layer count
- spatial soil files
- field-capacity / wilting-point related state
- rooting-depth traits
- root lifespan
- specific root length
- shoot-root ratio
- root biomass relationships

따라서 criterion 3은 `soil depth native`라서가 아니라 **soil-water/root state가 physiology에 직접 연결되고 외부 hydrology coupling이 이미 존재하기 때문**에 강하다.

침식/퇴적으로 soil geometry가 바뀌는 경우에는 water, roots, C/N, litter 등을 새 layer 구조로 보존적으로 remap해야 하며 이는 고운사의 **새로운 coupling**이다.

---

## 6. FORMIND-mHM 2026
Bruns et al. (2026)은 FORMIND와 distributed hydrologic model mHM을 coupling했다.

적용:
- Selke river catchment, Central Germany
- mixed deciduous forest catchment
- discharge와 forest GPP/ET feedback 동시 평가

이 연구는 다음의 direct precedent이다.
```text
distributed catchment hydrology
 <->
 demographic forest model
```

따라서 criterion 3과 4는 추정이 아니라 existing coupling precedent로 볼 수 있다.

FINAM component framework를 통한 step-wise data exchange도 외부 geomorphic component와 연결할 때 장점이다.

---

## 7. fire / disturbance
FORMIND 계열은 fire, treefall, landslide, logging, drought 등으로 gap이 생성되고 이후 recruitment/competition을 통해 forest structure가 변화하는 architecture를 갖는다.

따라서 postfire woody recovery에는 매우 적합하다.

문제는 초기 postfire herbaceous stage가 native forest run 안에 완전히 들어와 있지 않다는 점이다.

---

## 8. roots and geomorph interface
FORMIND state/parameters의 root biomass, rooting depth, root lifespan, specific root length를 사용하면 다음과 같은 bridge를 설계할 수 있다.

```text
cohort/PFT root biomass
 + rooting-depth distribution
 + specific root length
 -> layer RLD / root mass
 -> erosion resistance / bioturbation interface
```

그러나 explicit horizontal/3-D root architecture는 native state가 아니므로 별도 spatialization이 필요하다.

---

## 9. 현재 shortlist에서의 위치
FORMIND-mHM은 criterion 2를 제외하면 가장 이상적인 구조 중 하나다.

장점:
- actual patches
- default cohort option
- woody seed demography
- daily water/GPP
- direct catchment coupling
- fire/disturbance succession

결정적 약점:
- forest run에서 tree + explicit herbaceous demographic understory 동시 실행이 native feature로 입증되지 않음

따라서 현재 판정은:

```text
strong secondary / conditional top-tier
```

이며, **LPJ-GUESS spatial-hydrology lineage, MEDFATE, FATES보다 criterion 2에서 한 단계 아래**에 둔다.

---

## 다음 검증 우선순위
1. forest-herb concurrent mode가 향후 FORMIND release/LandTrans에서 실제 구현되는지 추적
2. FORMIND-mHM exact exchange timestep과 exchanged state variables 확인
3. mHM grid ↔ FORMIND patch scaling 확인
4. Korean temperate species parameterization 가능성 확인
5. restart/state injection과 dynamic soil-depth remapping 난이도 확인
6. 10–25 m patch에서 100년 계산비용 확인

## 핵심 문헌/문서
- Fischer et al. (2016), FORMIND model lineage.
- FORMIND current documentation/source, 2026.
- Bruns, N., Huth, A., Thober, S., & Fischer, S. M. (2026). Combining an individual-based dynamic vegetation model with a distributive hydrologic model to improve coupled water-carbon modelling. EGUsphere preprint. https://doi.org/10.5194/egusphere-2026-4918
- Kantzenbach, M., König, S., Reitz, T., Schädler, M., & Taubert, F. (2026). Synergizing grassland and soil system model expertise by coupling GRASSMIND (v2.0) and BODIUM (v1.2). EGUsphere preprint. https://doi.org/10.5194/egusphere-2026-1713
- UFZ LISA/LandTrans documentation, 2026.
