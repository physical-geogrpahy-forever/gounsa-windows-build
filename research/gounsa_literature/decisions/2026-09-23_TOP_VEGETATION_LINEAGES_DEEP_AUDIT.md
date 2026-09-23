# 2026-09-23 상위 식생모델 계열 심층 감사

## 결정 내용
고운사 100년 산불 후 식생-지형 결합의 주 식생엔진 후보를 다음 4계열로 유지하되 역할을 분명히 구분한다.

1. LPJ-GUESS SEC/PPA + RE/PF-LPJG lineage
2. FATES + ELM/ParFlow lineage
3. MEDFATE + medfateland
4. JULES-RED

EDYS는 생산 식생엔진보다 ecogeomorphic coupling benchmark로 유지한다.

## 현재 우선순위
### 1. LPJ-GUESS lineage: primary R&D target
가장 중요한 이유는 사용자가 요구한 `완전 개별목보다 가볍지만 일반 cohort보다 공간구조가 좋은 중간 모델`에 SEC가 가장 직접적으로 부합하기 때문이다.

SEC/PPA:
- tree cohort age/size structure
- persistent canopy gaps
- woody understory/recruitment
- forest-floor light heterogeneity
- herbaceous understory light response

RE:
- 15-layer Richards hydrology
- configurable layer thickness / soil depth
- bedrock/aquifer lower boundary
- subdaily adaptive solver

PF-LPJG:
- hourly 3-D ParFlow
- daily direct soil-state overwrite into LPJ-GUESS
- two-way vegetation-hydrology exchange

이 기능들은 하나의 published branch에 모두 합쳐져 있지 않다. 따라서 SEC/PPA + RE/PF-LPJG 조합은 새로운 code merge/coupling이다.

현재 source/domain audit에서 SEC는 canopy/light/establishment 쪽, RE는 soil hydrology 쪽, PF-LPJG coupler는 framework/MPI 및 soil-state exchange 쪽을 주로 수정하므로 기능영역 충돌은 제한적일 가능성이 높다. 그러나 exact file-level merge conflict 수는 아직 검증하지 않았으므로 `쉽게 병합 가능`이라고 단정하지 않는다.

## 2. FATES: strongest ready biology + hydraulics
FATES는 현재 ready-made ecosystem-demography engine 중 생물학과 수리학의 조합이 가장 강하다.

확인된 현재 source 특징:
- tree / shrub / grass PFTs
- PFT-specific seed production/recruitment
- grass demographic application
- upper canopy / understory PPA
- fine-root biomass and root litter
- FATES-HYDRO 30-min plant hydraulics
- ELM-FATES + ParFlow hillslope precedent
- current parameter/source includes cross-grid seed-dispersal controls

공간 약점은 정확히 `internal disturbance-history patch가 x-y 좌표를 갖지 않는다`는 점이다. Host/grid geography 자체나 seed movement가 완전히 비공간적인 것은 아니다.

가장 큰 practical weakness:
- CTSM/ELM host dependency
- ParFlow까지 붙이면 매우 무거운 stack
- dynamic soil geometry remapping은 별도 개발

## 3. MEDFATE + medfateland: best implementation/coupling sandbox
고운사에서 빠르게 실제 prototype을 만들기에는 가장 유리할 수 있다.

강점:
- actual sf/terra GIS cells
- tree and shrub cohorts
- species-specific herbData
- daily growth/water calls
- state continuation
- lateral surface/subsurface/groundwater/channel routing
- TETIS/SERGHEI landscape hydrology options
- external bulk-soil hydrology delegation
- cohort x soil-layer fine-root proportion matrix
- root-layer matrix can be manually altered or supplied by another model

이 마지막 점은 geomorph engine과의 coupling에서 특히 중요하다.

결정적 약점:
- herb physiology/growth는 있으나 woody pathway와 같은 endogenous herb seed -> recruitment -> new cohort loop가 완결되지 않음

따라서 herb demographic extension의 개발량을 실제로 산정하면 최종후보 순위가 바뀔 수 있다.

## 4. JULES-RED: lightweight demographic fallback
강점:
- tree/shrub mass classes
- grass PFT
- idealized grass -> shrub -> tree succession
- 30-60 min land-surface physics
- daily vegetation update 가능
- layer-wise soil moisture state prescription/restart
- TOPMODEL/river-routing hydrology lineage

약점:
- competition is simplified gap/dominance hierarchy
- no SEC/PPA-like explicit canopy-understory geometry
- rootC is PFT-level and layer root mass must be inferred through parameterized root-depth weighting
- soil layer geometry is relatively rigid, so dynamic spatial soil-depth change is awkward

따라서 primary engine보다는 lightweight comparator/fallback으로 둔다.

## 평가축별 현재 판단
| 축 | LPJ-GUESS lineage | FATES | MEDFATE | JULES-RED |
|---|---|---|---|---|
| cohort middle-ground | 매우 강함, 특히 SEC | 강함 | 강함 | 강함 |
| herb-shrub-tree demography | 강함, herb는 woody보다 단순 | 매우 강함 | herb recruitment gap | 강하지만 단순 |
| canopy/understory | 매우 강함 SEC/PPA | 매우 강함 PPA | 중간 | 약함-중간 |
| root/soil physiology | RE 결합 시 강함 | 가장 강함 | 강함, coupling friendly | 중간 |
| actual GIS cells | external grid + legacy 50 m precedent | host grid explicit, internal patch implicit | 가장 직접적 | grid explicit |
| lateral hillslope hydrology | PF/LPJ-DH branch precedent | ParFlow precedent | native/optional landscape routing | TOPMODEL lineage |
| dynamic soil geometry | custom | custom | custom but state editing tractable | custom and relatively awkward |
| implementation burden | branch merge required | 매우 높음 | 가장 낮음 | 중간 |

## 실제 개발 전략
### scientific target
`LPJ-GUESS SEC + RE or PF-style hydrology`

### rapid prototype target
`MEDFATE + medfateland`

### high-fidelity biological/hydraulic benchmark
`FATES-HYDRO + ParFlow`

### lightweight comparator
`JULES-RED`

## 다음 검증 우선순위
1. LPJ SEC/RE/PF-LPJG 공개 source archives를 실제 diff하여 충돌 파일과 함수 목록 산정
2. LPJ-GUESS가 고운사 geomorph engine으로 내보낼 수 있는 root/litter/biomass state를 source-level로 확정
3. MEDFATE herb demographic extension에 필요한 최소 함수/상태 추가량 산정
4. FATES에서 grid-to-grid seed dispersal의 실제 실행경로와 host-grid constraints 확인
5. 네 모델 모두에 대해 erosion/deposition 후 soil/root/C/N/water conservative remapping specification 작성
6. 25 m vegetation grid, 1-5 m geomorph grid의 two-scale coupling benchmark 설계

## 현재 결론
추가 broad model search보다 네 계열의 source-level feasibility audit이 더 가치가 높다.

특히 LPJ-GUESS는 과학적 기능 부재보다 branch integration이 핵심 문제이며, MEDFATE는 반대로 software integration은 쉽고 herb demography가 핵심 문제다. FATES는 과학적으로 매우 완성도가 높지만 software stack complexity가 가장 큰 문제다.
