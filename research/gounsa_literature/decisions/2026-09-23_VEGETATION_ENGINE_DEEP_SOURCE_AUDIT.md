# 고운사 식생엔진 심층 소스 감사 결정

업데이트: 2026-09-23

## 결정 목적
고운사 산불 후 약 100년 식생-수문-지형 상호작용 모델의 식생엔진 후보를 광범위하게 탐색한 뒤, 최상위 계열을 실제 소스 수준에서 비교했다.

고정 기준은 다음과 같다.
1. 개별목보다 가볍되 cohort/size/stage 구조가 있을 것
2. 초본-관목-교목 및 하층식생 천이를 명시적으로 다룰 것
3. 외부 토양/수문/지형 상태와 연결 가능할 것
4. 실제 지형/유역/측방수문 선례가 있을 것
5. 식생 반응이 적어도 일 단위, 생리/수문은 가능하면 시간 이하일 것

추가로 고운사에서는 침식/퇴적으로 토심과 DEM이 변한 뒤 root biomass, soil water, C/N state를 질량보존적으로 재매핑해야 한다.

---

# 1. 최상위 후보군
현재 생산후보는 다음 네 계열로 압축한다.

1. LPJ-GUESS SEC/PPA + external hydrology + selected LPJ-GUESS-RE soil-geometry ideas
2. FATES + ELM/ParFlow 또는 동등한 host hydrology
3. MEDFATE + medfateland + herb demographic extension
4. JULES-RED: 경량 fallback/comparator

EDYS는 native erosion/deposition-soil-depth feedback의 매우 중요한 설계 precedent이나, woody DBH/age cohort 부재, 약한 canopy structure, 월 단위 핵심 식물생산, 현대 공개소스 문제 때문에 생산엔진 최상위에서는 제외한다.

---

# 2. LPJ-GUESS: 현재 권장 조합
서로 다른 published branch 기능을 하나의 기존 모델로 부르면 안 된다.

Published components:
- SEC/PPA revision 13221: persistent canopy gaps / cohort canopy structure
- PF-LPJG: ParFlow hourly + LPJ daily soil-water state exchange
- LPJ-GUESS-RE: variable soil layers + Richards vertical hydrology
- LPJ-DH: 50 m fine-catchment lateral routing precedent

## 권장 architecture
두 water solver를 동시에 쓰지 않는다.

```text
LPJ-GUESS SEC canopy/demography
+ PF-LPJG-style external hydrology ownership
+ selected RE soil-layer / shallow-bedrock bookkeeping
- RE Richards solver itself
```

SEC와 PF/RE는 주요 수정영역이 비교적 분리되어 있어 병합은 현실적인 후보이지만, revision mismatch와 회귀검증이 필요하므로 trivial merge라고 부르지 않는다.

## 뿌리의 결정적 새 확인
LPJ-GUESS는 cohort/individual 수준의 total fine-root C(`cmass_root`)를 가지지만, native layer-specific live-root C pool은 아니다.
Layer root mass는 root distribution을 이용해 재구성해야 한다.

침식 후 단순히 더 얕은 토층에 전체 root C를 재정규화하면 안 된다.

필요한 새 coupling:
```text
removed soil thickness
 -> root fraction in removed volume
 -> frac_loss
 -> reduce live cmass_root and N consistently
 -> route lost root C/N to local dead-root litter and/or sediment export
 -> renormalize surviving root distribution
```

현재 코드의 management pathway가 `cmass_root`를 비율만큼 줄이고 root litter로 라우팅하는 기존 패턴을 가지므로, root-loss accounting의 구현 template로 활용할 수 있다.

## 판정
LPJ-GUESS SEC는 사용자가 원한 `개별목보다 가볍고 일반 cohort보다 공간적으로 명시적인 canopy-gap 구조`에 가장 잘 맞는다.
그러나 dynamic soil-depth/root-remapping은 명확한 새 coupling이다.

---

# 3. FATES: 생물학적으로 가장 완결된 ready candidate
Current source audit confirms:
- size/PFT cohorts
- upper canopy + understory PPA
- native tree, multiple shrub, C3/C4 grass PFTs
- PFT seed production/bank/germination/recruitment
- inter-grid seed dispersal parameters
- half-hourly biophysics / plant hydraulics
- daily demographics
- FATES-HYDRO rhizosphere -> absorbing root -> transporting root -> stem -> leaf
- ELM-FATES-ParFlow actual hillslope coupling precedent

## spatial limitation의 정확한 의미
Host grid-cell 간 seed dispersal은 존재한다.
문제는 internal disturbance patch/cohort에 geographic x-y가 없다는 점이다.
Postfire recovery-only experiment에서는 patch creation을 최소화하여 `1 GIS cell -> approximately 1 persistent FATES patch` 구성을 검토할 수 있다.

## 뿌리/토심의 강점
`max_rooting_depth_index_col`은 source comment상 bedrock/permafrost에 의해 허용되는 deepest rooting layer를 host가 FATES에 전달하는 interface다.
공통 `set_root_fraction()`이 physiology, hydrology, mortality, soil BGC, cohort dynamics 등에서 재사용된다.

따라서 soil-depth/root-access constraint는 비교적 일관되게 전달된다.

## erosion root severing에 대한 매우 중요한 기존 hook
PARTEH의
```text
PRTDamageLosses(prt, organ_id, mass_fraction)
```
은 살아남는 식물의 특정 organ에 대해 C/N/P 등 해당 organ state를 지정 비율만큼 실제로 차감하고 damage-loss flux로 기록한다.
함수 자체는 손실 biomass의 최종 목적지를 외부 damage model이 결정하도록 설계되어 있다.

따라서 고운사에서는 개념적으로:
```text
organ_id = fine-root organ
mass_fraction = fraction of root biomass in eroded volume
```
으로 partial root loss를 구현하고, 외부 geomorph coupler가 손실분을 local litter와 sediment export로 나누는 방식을 검토할 수 있다.

이는 published erosion coupling은 아니며 반드시 새로운 coupling으로 기록한다. 그러나 FATES 내부 C/N/P accounting을 재사용할 수 있어 구현부담을 낮춘다.

## 판정
과학적으로 가장 완결된 ready demographic candidate.
단점은 ELM/CTSM/ParFlow host stack과 event soil-geometry remapping의 복잡성이다.

---

# 4. MEDFATE + medfateland: 가장 구현 친화적인 후보
강점:
- actual sf/terra GIS cells
- tree/shrub cohorts
- species-specific `herbData`
- daily water/carbon/growth
- cohort root depth Z50/Z95/Z100
- fine/coarse root utilities
- lateral surface/subsurface/groundwater/channel flow
- seed dispersal among geographic units
- one-day simulation functions
- `soilDomains="none"`으로 external bulk hydrology 위임 가능
- `soil_redefineLayers()`라는 명확한 layer-geometry insertion point

## woody regeneration은 강함
Source audit confirms tree/shrub seedling bank에서 daily root-depth growth와 daily light/drought hydraulic filtering을 수행할 수 있다.
즉 woody recruitment는 단순 연간 확률만이 아니다.

## herb의 정확한 상태
`herbData`는 단순 cover-only 입력이 아니다.
- 같은 integrated plant cohort arrays에 들어간다.
- root profile이 생성된다.
- internal water/carbon machinery에 참여한다.
- mergeHerbs 등 cohort helper가 있다.

그러나 source가 명시적으로:
- woody regeneration path에서 herbData를 제외하고
- daily dynamic mortality branch에서 `ctype == "herb"`를 제외한다.

따라서 현재 빠진 것은 새 herb physiology가 아니라 다음 demographic wrapper다.
```text
herb seed production
 -> seed bank / dispersal
 -> germination
 -> create/merge herbData cohort
 -> demographic mortality/disappearance
 -> turnover/seed return
```

이는 처음 생각한 것보다 작은 수정이지만, 생태학적 검증이 필요한 중간 규모 확장이다.

## soil remap
`soil_redefineLayers()`는 layer geometry를 바꿀 수 있으나 initialized state를 보존하는 conservative remapper는 아니다.
따라서 erosion/deposition마다 water/C/N/root state를 별도로 overlap-remap해야 한다.

## 판정
가장 빠르게 고운사 prototype을 만들기 좋은 후보.
단, early postfire herb succession을 핵심 연구결과로 삼는다면 herb demographic extension을 먼저 구현/검증해야 한다.

---

# 5. JULES-RED
2026년 현재 `MetOffice/jules` public GitHub source에 RED가 정식 science component로 존재한다.

장점:
- tree/shrub mass classes
- grass
- daily current-source demography
- subdaily land-surface physics
- tree > shrub > grass recruitment hierarchy
- broad grass -> shrub -> tree succession
- layer-wise `sthuf` soil wetness prescription 가능
- catchment/TOPMODEL/routing lineage

약점:
- root biomass가 RED mass-class-by-layer가 아니라 PFT aggregate `rootC` + prescribed exponential root-depth profile 중심
- standard soil-layer geometry가 fine-cell별 동적으로 바뀌는 구조가 아님
- canopy competition이 SEC/FATES보다 단순

판정:
경량 demographic fallback/comparator. 고운사 생산엔진 우선순위는 상위 3개보다 낮다.

---

# 6. 모든 상위 후보에 공통으로 필요한 Gounsa remapper
현재 top 4 중 어느 것도 `erosion/deposition -> soil geometry + live-root C/N + water/C/N state`를 완전 native하게 보존하면서 처리하지 않는다.
따라서 공통 새 모듈을 설계한다.

## 입력
- old/new soil layer interfaces
- erosion/deposition thickness
- old/new DEM
- soil water or water potential by layer
- soil C/N/mineral N
- texture/coarse fragments if material changes
- vegetation root pool and root distribution

## 핵심 알고리즘
```text
1. old-new layer overlap matrix 계산
2. soil water mass 보존 remap
3. soil C/N/mineral N 보존 remap
4. eroded volume 속 live-root mass 계산
5. plant live-root C/N pool에서 해당 질량 제거
6. removed root를 local dead-root/litter vs sediment export로 분할
7. deposition 시 buried-root 상태를 별도 처리
8. surviving soil profile에서 root fractions 재계산
9. plant hydraulic/water-stress state 재초기화 또는 일관화
10. 다음 daily vegetation step 재개
```

중요:
- `root profile truncation`과 `root biomass physical loss`를 구분한다.
- soil depth가 줄었다고 전체 root biomass를 남은 토층에 압축하지 않는다.
- root loss와 shallow-landslide root cohesion 감소는 같은 event state를 공유할 수 있지만 동일 parameter로 합치지 않는다.

---

# 7. 현재 우선순위의 의미
단일 숫자순위로 완전히 고정하지 않는다. 목적별 우선순위가 다르다.

## canopy-gap cohort 구조 최우선
LPJ-GUESS SEC

## ready herb/shrub/tree demography + hydraulics 최우선
FATES

## 실제 GIS/일별 geomorph coupling 구현편의 최우선
MEDFATE

## 계산적으로 단순한 mass-class fallback
JULES-RED

현재 다음 구현감사는 LPJ-GUESS SEC, FATES, MEDFATE 세 후보에 집중한다.
JULES-RED는 비교대상으로 유지한다.

---

# 8. 다음 검증
1. LPJ-GUESS SEC branch를 current release/PF path에 이식할 때 실제 충돌 파일 목록 확보
2. FATES fine-root partial damage를 `PRTDamageLosses(fnrt_organ, frac_loss)`로 적용할 때 litter/damage flux accounting 연결부 확인
3. MEDFATE herbData가 유지하는 biomass/cover 상태와 seed/mortality extension 최소 코드 경로 작성
4. 세 후보 공통 soil/root conservative remapper prototype 설계
5. 25 m vegetation grid + 1-5 m geomorph grid benchmark architecture 확정
6. 고운사 국내 수종/관목/초본 parameterization 가능성 비교

## 관련 모델 파일
- `models/LPJ_GUESS_SPATIAL_COHORT_SYNTHESIS.md`
- `models/FATES.md`
- `models/MEDFATE_MEDFATELAND.md`
- `models/JULES_RED.md`
- `models/EDYS_TerreSIM.md`
