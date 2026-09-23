# 고운사 식생엔진 폭우 직후 시간응답 감사

업데이트: 2026-09-23

## 목적
고운사에서는 6시간 규모 폭우가 지형과 토심을 바꾼 뒤 그 변화가 식생과 수문에 빠르게 되먹임되어야 한다.

따라서 단순히 `모델이 daily climate를 사용한다`가 아니라 다음 네 항목의 실제 갱신 주기를 구분한다.

1. 외부 지형사건 직후 root/biomass loss를 상태에 반영할 수 있는가
2. 손실된 root biomass를 언제 다시 생산하는가
3. recruitment / mortality / cohort structure를 언제 갱신하는가
4. soil-water stress는 언제 반응하는가

---

# 1. LPJ-GUESS

## 빠른 부분
- photosynthesis / respiration / hydrology / water stress는 daily
- external coupling 또는 event hook이 `Individual` 상태를 직접 수정하면 같은 해 중에도 상태를 즉시 바꿀 수 있음
- 공개 LPJ source의 기존 biomass-loss routine은 `remaining = 1 - mortality`로
  - `densindiv`
  - `cmass_leaf`
  - `cmass_root`
  - `cmass_sap`
  - `cmass_heart`
  - C/N storage
  등을 즉시 줄임
- 따라서 storm erosion에 의한 root loss를 같은 패턴으로 구현하는 것은 구조적으로 가능
- Vegetation / Patch / Soil / Individual state가 dump/restart에 serialize됨

## 느린 부분
일반 자연식생에서 핵심 구조 갱신은 연말이다.

공개 source `framework.cpp`:
```text
if (date.islastday && date.islastmonth) {
    // Tissue turnover, allocation to new biomass and reproduction,
    // updated allometry
    growth(stand, patch);
}
```

따라서 storm 직후 root biomass를 줄이면:
```text
즉시: root pool 감소, water uptake/stress 변화 가능
연말: 본격적인 tissue turnover / new biomass allocation / reproduction / allometry
```

## 고운사 의미
LPJ-GUESS는 event damage를 못 받는 모델이 아니다.
문제는 **회복 구조의 native cadence가 연간이라는 것**이다.

고운사에서 폭우 뒤 수주~수개월의 fine-root 재생 자체가 핵심 상태변수라면 별도 subannual allocation extension 없이 LPJ는 거칠다.

판정:
**storm damage injection = 가능**
**native root structural recovery = annual limitation**

---

# 2. FATES

## 빠른 생리
- host land-surface/plant hydraulics: subdaily, 보통 half-hourly class
- FATES-HYDRO: leaf -> stem -> transporting root -> absorbing root -> rhizosphere continuum
- soil/root water state는 빠른 land-surface loop에서 반응

## daily allocation / turnover
현재 public FATES source의 PARTEH generic allocation code는 명시적으로:
```text
This subroutine is called each day in FATES,
which is the control interval that we conserve carbon
from the allocation and turnover process.
```
라고 설명한다.

따라서 LPJ와 달리:
```text
storm damage
 -> next daily allocation/turnover cycle
 -> root/leaf/wood allocation response
```
가 native time structure에 맞는다.

## daily demography/disturbance
FATES patch dynamics source는 disturbance rates를 daily timestep 기준으로 처리한다.
Recruitment, mortality, cohort dynamics 역시 daily demographic framework에 연결된다.

## root-loss caveat
FATES는 soil/rhizosphere layer와 cohort fine-root state가 강하지만:
- soil profile이 얕아지면 root fraction/profile을 surviving layers에 다시 맞출 수 있음
- 그러나 침식된 토층에 있던 live root C를 자동으로 물리적으로 제거하는 geomorphic routine은 없음

따라서 필요:
```text
erosion root fraction
 -> FineRootC physical loss
 -> C/N fate
 -> surviving profile remap
```

판정:
**native fast physiology = 매우 강함**
**native daily allocation/demography = 매우 강함**
**physical erosion-root truncation = new coupling**

---

# 3. MEDFATE + medfateland

## daily distributed loop
`growth_land_day`는 한 날짜 단위로:
- local carbon balance
- growth
- mortality
- overland runoff
- subsurface flow
- groundwater flow
을 spatial cells에서 계산한다.

## daily fine-root growth
`growth_day_c.cpp`는 현재 fine-root biomass와 target fine-root biomass의 차이를 계산하고, 각 soil layer/root sink에 대해 fine-root growth를 당일 계산한다.

source pattern:
```text
deltaFRBpheno = max(targetFineRootBiomass - currentFineRootBiomass, 0)
deltaFRBsink = layerRootBiomass * RGRfinerootmax * resource limitation
```

따라서 외부 geomorphic event가 root biomass를 줄였다면 다음 daily growth call부터 root regrowth가 반응할 수 있다.

## woody recruitment
Daily recruitment mode에서는 woody seedling:
- root depth Z95 daily increment
- Z50 update
- current soil layer psi 사용
- root distribution 사용
- drought mortality
- ground PAR light mortality
을 계산한다.

## herb limitation
현재 herb cohorts는 physiological/root state는 있으나:
- native seed-to-herb cohort recruitment loop 없음
- tree/shrub과 같은 dynamic mortality branch에서 herb가 제외됨

따라서 early postfire herb population turnover는 native daily demographic process로 완결되지 않는다.

## soil geometry
cell별 layer widths / total soil depth를 가질 수 있다.
`soil_redefineLayers()`는 geometry를 쉽게 바꾸지만 initialized state는 보존하지 않으므로 conservative remapper가 필요하다.

판정:
**daily woody/root response = 매우 강함**
**actual GIS daily event loop = 네 후보 중 가장 다루기 쉬움**
**herb lifecycle = custom extension 필요**

---

# 4. JULES-RED

## fast land-surface
- energy / water / photosynthesis: subdaily, 일반적으로 30-60 min class
- layer soil wetness `sthuf`는 외부 prescribed state로 timestep 시작 시 overwrite 가능

## daily RED demography
current public source `veg3_red_dynamic_mod.F90`는 demographic state를 실제 `dt`로 적분한다.

계산:
- assimilate -> reproductive allocation `alpha_recrt`
- seedling influx into first mass class
- growth flux across mass classes
- mortality
- plant number density update
- demographic litter

current next-generation JULES path는 RED dynamics를 one-day interval로 호출하는 source evidence가 있다.

따라서 RED의 daily demography는 실제 구현이다.

## roots
약점:
- root biomass/interface가 PFT aggregate 중심
- `rootd_ft`는 PFT prescribed e-folding depth
- RED mass class별 dynamic rooting-depth demography가 아님

## soil geometry
표준 JULES는 soil layer thickness와 total soil depth를 domain 전체에서 공통으로 사용한다.
따라서 cell-specific shallow soil 및 erosion-driven dynamic depth는 구조적으로 불리하다.

판정:
**daily mass-class demography = 강함**
**external soil-water state injection = 강함**
**dynamic shallow-soil/root geometry = 네 후보 중 약한 편**

---

# 5. storm-response 비교

| 항목 | LPJ-GUESS SEC | FATES | MEDFATE | JULES-RED |
|---|---|---|---|---|
| fast soil-water response | daily, PF coupling 시 hourly hydrology | subdaily | daily, external hydrology 가능 | subdaily |
| immediate external biomass/root loss hook | 가능, custom | 가능, custom | 상태 직접 수정 쉬움, custom | 가능하나 root state 단순 |
| native new root allocation | **annual natural vegetation** | **daily** | **daily** | daily vegetation path, root architecture는 PFT aggregate |
| native woody recruitment/demography | mainly annual | daily | daily/annual configurable | daily |
| native herb demography | PFT physiology/competition 있으나 tree cohort보다 단순 | strongest among candidates | incomplete | grass single class, simplified |
| layer root structure | moderate/static profile | **very strong cohort hydraulics** | **strong cohort Z50/Z95** | weak-moderate PFT profile |
| cell-specific soil depth | branch-dependent/custom | host-dependent/custom dynamic event | **native per-cell soil object** | weak, standard domain-common geometry |
| conservative erosion layer remap | new coupling | new coupling | new coupling but easiest insertion | new coupling, most invasive |

---

# 6. 결정 변화

이 감사로 단순 우선순위가 조금 바뀐다.

## 생태생리와 storm recovery가 가장 중요한 경우
**FATES가 가장 강함.**

이유:
- subdaily hydraulics
- daily allocation/turnover
- daily demographic dynamics
- tree/shrub/grass
- cohort roots
- existing ParFlow hillslope coupling

## canopy-gap cohort architecture가 가장 중요한 경우
**LPJ-GUESS SEC는 여전히 가장 매력적이지만 annual allocation이 실제 약점.**

EarthShape/Landlab 및 PF-LPJG 선례 때문에 geomorph/hydrology coupling 자체의 불확실성은 낮아졌으나, storm 후 root structural recovery를 subannual로 만들려면 추가 코드가 필요하다.

## 빠르게 고운사 prototype을 만드는 경우
**MEDFATE가 가장 현실적.**

- actual GIS cells
- daily root growth
- daily woody dynamics
- state objects transparent
- layer widths cell-specific

대신 herb demographic lifecycle을 새로 완성해야 한다.

## 경량 대안
**JULES-RED.**

시간구조는 예상보다 강하지만 root/soil geometry가 고운사 목적과 덜 맞는다.

---

# 7. 현재 구현 후보 경로

현재 세 개만 실제 prototype 대상으로 남긴다.

### Path F
```text
FATES + ELM/ParFlow
+ geomorph root-loss/layer-remap coupler
```

### Path L
```text
LPJ-GUESS SEC/PPA
+ PF-style external hydrology
+ EarthShape-style external orchestration
+ event root-loss hook
+ optional subannual root-allocation extension
```

### Path M
```text
MEDFATE + medfateland
+ conservative soil/root remapper
+ herb demographic lifecycle extension
```

JULES-RED는 comparator/fallback으로 유지한다.

# 최종 판정
폭우 직후 식생 회복의 시간해상도를 엄격히 적용하면:

```text
FATES > MEDFATE > JULES-RED > LPJ-GUESS
```

단, 이것은 **storm-response cadence 한 축의 순서**이며 전체 모델의 종합 순위가 아니다.

전체 구조에서는:
- LPJ-GUESS SEC: canopy-gap cohort 장점
- FATES: ready biology/hydraulics 장점
- MEDFATE: implementation/GIS coupling 장점
이 서로 다른 강점을 유지한다.
