# 고운사 식생 엔진 심층 감사 결정

업데이트: 2026-09-23

## 목적
광범위 후보 탐색 후 남은 상위 계열을 코드와 상태변수 수준에서 재검토하여, 고운사 산불 후 100년 식생-지형 결합모델의 실제 구현 경로를 좁힌다.

고정 기준:
1. 개별목보다 가벼운 spatial cohort/hybrid 구조
2. 초본-관목-교목 및 하층식생 천이
3. 얕은 토심/토양수분과 외부 지형모델 coupling
4. 실제 사면/유역/지형 선례
5. 일 이하, 가급적 시간 이하의 빠른 생태수문 반응

---

# 1. 가장 중요한 새 결정

## LPJ-GUESS에서 RE와 ParFlow를 동시에 토양수문 solver로 사용하지 않는다

두 branch는 서로 보완적인 독립 과정이 아니라 토양수문 계산에서 상당 부분 역할이 중복된다.

- LPJ-GUESS-RE: LPJ 내부 1-D Richards equation, 사용자 정의 soil-layer thickness, bedrock/aquifer/free-drainage lower boundary
- PF-LPJG: LPJ 내부 soil-moisture/runoff 계산을 ParFlow 3-D surface-subsurface hydrology로 교체하고 ParFlow soil moisture가 LPJ state를 overwrite

따라서 production path는 다음 둘 중 하나다.

### 경로 A
```text
LPJ-GUESS SEC/PPA
+ LPJ-GUESS-RE
+ 별도 측방 routing 또는 단순 외부 유역수문
```

장점: LPJ 내부에서 비교적 단순하게 끝남.
단점: 고운사 폭우/측방 지하수/실제 terrain routing을 별도 개발해야 함.

### 경로 B, 현재 우선 검토
```text
LPJ-GUESS SEC/PPA
+ PF-LPJG style ParFlow coupling
```

ParFlow가 담당:
- 3-D Richards flow
- surface/subsurface lateral redistribution
- groundwater
- storm/hourly soil-water state

LPJ-GUESS SEC/PPA가 담당:
- tree age/size cohort
- persistent canopy gap / canopy-understory light competition
- shrub/herbaceous PFT
- recruitment/growth/mortality
- vegetation C pools

**현재 고운사에는 경로 B가 더 직접적이다.**

LPJ-GUESS-RE는 이 경로에서 동시에 solver로 돌리기보다 다음 설계 참고로 사용한다.
- custom layer thickness
- shallow soil/bedrock boundary
- variable soil depth treatment

---

# 2. LPJ-GUESS SEC/PPA + PF-LPJG 병합 난이도

## 확인된 기본 code architecture
공개 LPJ-GUESS 계열 코드에서 주요 모듈은 다음처럼 분리된다.

```text
framework/framework.cpp   main temporal loop
modules/soil.cpp          layered soil state
modules/soilwater.cpp     soil-water process
modules/canexch.cpp       canopy exchange + layer soil-water uptake
modules/growth.cpp        allocation/growth/establishment flux
modules/vegdynam.cpp      establishment/mortality/disturbance
framework/guess.h         shared state/classes
```

PF-LPJG 논문은 MPI coupler를 `framework.cpp`에 삽입했다고 명시하며, ParFlow soil moisture로 LPJ internal soil moisture를 overwrite한다.

SEC/PPA 논문은 주로 다음 생태기능을 수정한다.
- crown/canopy organization
- cohort spatial centroid or canopy-layer sorting
- light availability
- forest-floor gap
- recruitment placement
- self-thinning/competition

따라서 **SEC/PPA와 PF coupler의 주요 관심영역은 상당 부분 분리되어 있다.**

정확한 branch-to-branch diff를 완료하지 않은 상태에서 `충돌이 없다`고 단정하지 않는다. 특히 다음 공유영역은 수동 병합 가능성이 높다.
- `framework/guess.h` shared state
- `canexch.cpp` water/light exchange
- input/output definitions
- revision 간 API/state changes

현재 판정:
**merge difficulty = MEDIUM, not prohibitive**

`SEC + RE + PF` 3중 병합보다 `SEC + PF` 2중 병합이 훨씬 합리적이다.

---

# 3. LPJ-GUESS의 얕은 토양 root 문제

LPJ-GUESS-RE 논문은 root architecture가 정적임을 명시한다.

기본 구조:
```text
RD_cumul = 1 - beta_root^z
```

PFT-specific vertical profile을 각 soil layer로 배분한다.

중요한 shallow-soil 문제:
- 계산된 누적 root fraction이 soil column bottom에서 1에 도달하지 않으면
- 누락된 root fraction을 bottom layer에 몰아넣음
- RE 논문은 1 m보다 얕은 soil에서 bottom layer가 tree root biomass의 가장 큰 비율을 갖게 될 수 있음을 직접 지적

고운사에서는 postfire soil depth가 매우 얕을 가능성이 있으므로 이 동작을 그대로 사용하지 않는다.

필요한 새 coupling:
```text
erosion reduces active soil depth
 -> calculate root mass in removed volume
 -> remove live/dead root mass physically
 -> allocate removed root to exported sediment / dead litter as appropriate
 -> retain surviving root mass
 -> recalculate surviving vertical fractions
 -> update plant C balance / stress / mortality
```

---

# 4. FATES 심층 감사

## 식생 demographic coverage
현재 공개 FATES parameter file은 다음 PFT를 정식으로 포함한다.
- multiple extratropical trees
- multiple extratropical/arctic shrubs
- C3 grasses
- C4 grass

소스에는 다음이 확인된다.
- seed production
- seed germination pools
- recruitment
- PFT-specific seed dispersal fraction
- maximum inter-grid-cell dispersal distance

따라서 FATES의 공간 약점은 `종자 이동이 없음`이 아니다.
정확한 약점은 **internal disturbance patch가 geographic x-y를 갖지 않는다는 것**이다.

## ecohydrology
ELM-FATES-ParFlow published precedent:
- ELM/FATES biophysical exchange: half-hourly
- ParFlow hydrology: 3-D explicit surface/subsurface
- soil moisture -> FATES physiology: same fast coupling loop
- vegetation structural/demographic update: daily

이는 현재 후보 중 가장 강한 ready-made hillslope-demography coupling precedent다.

## root geometry
FATES source stores:
- `zi_soil`: soil layer interfaces
- `dz_soil`: layer thickness
- `rootfrac_scr`: root fraction by soil layer

`set_root_fraction()` recalculates root fractions from actual soil-layer interfaces and can limit the maximum active rooting layer.

따라서 host model이 얕은 soil column을 제공하면 root profile geometry는 그 soil column에 맞출 수 있다.

그러나 함수는 남은 root fractions를 다시 합계 1로 normalize한다.
즉:
```text
soil layer removed
 != automatic root biomass death/removal
```

따라서 FATES도 고운사에서 erosion-root truncation coupling이 필요하다.

FATES-HYDRO는 leaf-stem-transporting root-absorbing root-rhizosphere hydraulic continuum까지 갖지만 현재 source comment상 experimental option이라는 점을 기록한다.

## 현재 판정
**ready ecology + hydrology precedent로는 가장 강함.**

단점:
- CTSM/ELM + FATES + ParFlow stack이 무거움
- internal patches are non-geographic
- geomorphic soil-layer removal/root loss는 custom

---

# 5. MEDFATE + medfateland 심층 감사

## 식생과 공간
- actual GIS cells
- tree cohorts
- shrub cohorts
- herb cohorts can exist and run physiology/growth
- seed bank / seedling bank
- spatial seed dispersal
- daily growth/water
- lateral water flow / groundwater / routing
- one-day state-continuation functions

## root structure
각 cohort는 `Z50`, `Z95`, optional `Z100`을 가질 수 있다.
Fine-root fractions are calculated by soil layer.

### woody seedling root growth
`regeneration.R`에서 seedling bank의 `Z95`가 daily 증가하고 `Z50`도 함께 갱신된다.

따라서 산불 후 woody recruitment의 초기 root-depth development는 LPJ-GUESS의 static PFT root profile보다 직접적이다.

### root truncation
`ldrRS_one_c()`는 `Z100`보다 깊은 층을 0으로 만들 수 있지만 마지막에 root fractions를 합계 1로 rescale한다.

따라서 MEDFATE도 soil erosion이 기존 root biomass를 자동 제거하지 않는다.

## soil layer change
`soil_redefineLayers()`가 공개 함수로 존재한다.
하지만 source documentation은 initialized `soil`에 사용할 경우:
- hydraulic parameters are recalculated
- **state variables are lost**
라고 명시한다.

따라서 geomorphic event 후 soil layer remap은 사용자가 직접 질량보존 방식으로 구현해야 한다.

필요 remap:
- liquid soil water
- soil C/N if used
- root fractions and root mass
- rhizosphere water state
- litter/interface pools

## herbaceous limitation
existing herb cohorts의 physiology/growth는 가능하지만 native regeneration pathway는 tree/shrub 위주다.
`seed -> new herb cohort`의 완전한 demographic loop는 확인되지 않았다.

## 현재 판정
**구현 난이도는 네 후보 중 가장 낮음.**

특히 R/terra/sf 기반 고운사 workflow와 잘 맞는다.
결정적 추가개발은:
1. herb recruitment
2. erosion-root truncation
3. soil-state conservative remap

---

# 6. JULES-RED 심층 감사 및 버전 정정

기존 기록의 `JULES v8.1` 표현은 현재 공개 문서에서 재검증하지 못했다.
2026-09-23 현재 public JULES documentation의 `Latest` user guide는 **v7.9**로 표시된다.
따라서 이후 고운사 기록은 별도 source가 없는 한 v7.9 public documentation 기준으로 한다.

## RED demography
public v7.9 guide에서 정식 확인:
- `mclass`: PFT mass-class number
- `mass0`, `massi`
- `height0`
- `crwn_area0`
- `alpha_recrt`
- `mort_base`
- `dom_order`

`dom_order`:
```text
3 tree
2 shrub
1 grass
```

따라서 RED woody size-class demography와 tree-shrub-grass hierarchy는 확실하다.

## hydrology/state injection
JULES prescribed-data interface can prescribe `sthuf` for each soil layer at the beginning of every timestep.
즉 external hydrology state injection은 강하다.

## soil geometry limitation
public v7.9 documentation:
- `sm_levels` user configurable
- `dzsoil_io` layer thicknesses configurable
- 그러나 `dzsoil_io`와 total soil depth는 **constant across domain**

따라서 고운사의 공간적으로 매우 이질적인 shallow soil depth에 불리하다.

## roots
`rootd_ft_io` is a PFT root-depth parameter.
Recommended mode uses an exponential root distribution weighted across soil layers.
Root depth is therefore much more prescribed/static than MEDFATE seedling root development or FATES hydraulic structure.

Outputs include:
- `rootC`
- `root_litC`

하지만 root state is primarily PFT-level rather than rich cohort-by-soil-layer root demography.

## current verdict
**top-tier comparator but downgraded for Gounsa shallow-soil implementation.**

장점:
- parsimonious/light mass-class demography
- grass-shrub-tree succession
- half-hourly land-surface physics and daily RED application evidence
- prescribed soil-water state

약점:
- soil depth spatially fixed by standard domain setup
- root architecture simple/static
- canopy/understory competition simpler than SEC/FATES

---

# 7. 공통적으로 새로 필요한 geomorph-root module

LPJ-GUESS, FATES, MEDFATE 모두 `얕아진 soil profile에 root fractions를 맞추는 것`과 `침식으로 실제 root biomass가 소실되는 것`을 자동으로 같은 과정으로 처리하지 않는다.

따라서 고운사에는 model-independent coupling layer를 둔다.

```text
Geomorph event
  -> old/new DEM and soil interfaces
  -> overlap volume by old/new soil layer
  -> conservative remap of soil water/C/N
  -> calculate live/dead root mass physically removed
  -> removed roots: sediment-export or dead organic pool
  -> surviving root mass by new layers
  -> root exposure/burial stress
  -> pass remapped soil/root state to vegetation engine
```

이 모듈은 반드시 **새로운 coupling**으로 명시한다.

---

# 8. 현재 순위의 의미

단순 총점 순위가 아니라 구현 목적별 판정이다.

## 과학구조 최우선
**LPJ-GUESS SEC/PPA + ParFlow-style coupling**
- desired middle ground between individual-tree and ordinary cohort
- persistent gap/canopy structure
- shrub/herb PFT lineage
- actual external 3-D hydrology precedent

주요 새 개발:
- branch merge
- shallow-soil root rule
- geomorph event state remap

## ready ecohydrological demography 최우선
**FATES + ELM/ParFlow**
- strongest existing demographic + hillslope coupling precedent
- tree/shrub/grass + seed dynamics
- half-hourly physiology / daily vegetation

주요 단점:
- heavy stack
- implicit internal patches

## 구현 및 실험 속도 최우선
**MEDFATE + medfateland**
- actual GIS cells
- easy day-by-day external loop
- root-layer state and woody seedling root growth
- R/C++ ecosystem

주요 새 개발:
- herb recruitment
- conservative soil/root remap

## 경량 demographic comparator
**JULES-RED**
- simple mass classes and tree-shrub-grass hierarchy
- external soil moisture forcing possible

고운사에서는 shallow variable soil geometry 때문에 우선순위가 낮아짐.

---

# 9. 다음 구현 감사 우선순위

1. **LPJ SEC/PPA + PF-LPJG**
   - exact revision/file diff 확보
   - SEC state additions and PF MPI coupling collision audit
   - 10-25 m or 25-50 m runtime feasibility

2. **FATES persistent single-patch GIS-cell setup**
   - 최소 ELM/FATES/ParFlow test configuration
   - root/litter outputs by layer
   - restart soil-geometry edit feasibility

3. **MEDFATE prototype**
   - 1 cell/day loop
   - externally change soil layers
   - conservative water/root remap helper
   - simple herb recruitment extension size estimate

4. JULES-RED는 위 세 경로가 과도할 경우 경량 fallback으로 유지

---

# 최종 결정
현재 production-engine 선택은 아직 확정하지 않는다.

그러나 broad model search 단계는 사실상 종료하고, 다음 세 구현경로를 실제 prototype/branch audit 대상으로 좁힌다.

```text
A. LPJ-GUESS SEC/PPA + ParFlow-style external hydrology
B. FATES + ELM/ParFlow
C. MEDFATE + medfateland + herb recruitment extension
```

JULES-RED는 comparator/fallback.
EDYS는 ecogeomorphic architecture precedent.

모든 경로에서 erosion/deposition-driven root biomass truncation 및 conservative soil-state remapping은 고운사 **새로운 coupling**이다.

## 핵심 근거
- Stoebke et al. (2026), GMD 19:3595-3615. DOI 10.5194/gmd-19-3595-2026.
- Jia et al. (2026), GMD 19:1727-1747. DOI 10.5194/gmd-19-1727-2026.
- Verbruggen et al. (2025), GMD 18:6623-. DOI 10.5194/gmd-18-6623-2025.
- Fang et al. (2022), ELM-FATES-ParFlow topographic forest hydrology coupling.
- NGEET/fates current public source audit, 2026-09-23.
- emf-creaf/medfate current public source audit, 2026-09-23.
- JULES public v7.9 User Guide, accessed 2026-09-23.
