# 고운사 식생엔진 구현범위 감사

업데이트: 2026-09-23

## 목적
상위 식생엔진 후보를 단순 기능표가 아니라 실제 production prototype에 필요한 최소 코드변경 범위로 비교한다.

현재 production path 후보:
- FATES + ELM/ParFlow
- LPJ-GUESS SEC/PPA + PF-style coupling + EarthShape-style orchestration
- MEDFATE + medfateland

JULES-RED는 경량 comparator/fallback으로 유지한다.

---

# 1. FATES path

## 그대로 쓸 수 있는 것
- tree / shrub / grass PFT
- PFT-specific seed production, germination, recruitment
- inter-grid seed dispersal
- daily allocation / turnover / demographic dynamics
- PPA canopy / understory
- cohort fine-root C
- FATES-HYDRO absorbing root / transporting root / stem / leaf hydraulic continuum
- host-model soil water coupling
- published ELM-FATES-ParFlow hillslope coupling
- restart infrastructure
- patch/cohort fusion / sparse cohort removal

## 고운사에서 반드시 새로 넣을 것
### A. geomorphic root truncation
침식으로 토층 일부가 제거될 때:
```text
old root profile
 -> removed soil overlap
 -> physically removed root mass
 -> reduce FineRootC / associated C-N state
 -> decide exported-vs-litter fate
 -> recompute surviving root distribution
```

현재 FATES는 얕아진 soil profile 안에 root distribution을 재계산할 수 있지만, removed soil volume의 root biomass를 geomorphic loss로 자동 제거하지 않는다.

### B. conservative soil-layer remapping
host soil geometry가 event 중 바뀌면 water / C / N / hydraulic state의 보존 remap이 필요하다.

### C. fine-grid seed-neighbor optimization
현재 `DetermineGridCellNeighbors`는 모든 grid-cell pair를 검사한다.

```text
for gi = 1..N-1
  for gj = gi+1..N
      compute distance
```

따라서 fine grid에서 초기 neighbor discovery는 O(N^2)이다.

고운사 10-25 m 격자에서는 다음 중 하나가 필요할 가능성이 높다.
- spatial window search
- KD-tree / spatial index
- precomputed GIS neighbor list
- seed dispersal off 또는 local-only sensitivity run

## 계산복잡도 완화 전략
- observed 2025 wildfire를 initial condition으로 두고 future patch-creating fire 비활성
- `mortality_disturbance_fraction = 0` 등으로 ordinary mortality-driven patch fission 최소화
- existing patch fusion / cohort fusion 유지
- 1 host GIS cell ≈ 1 persistent FATES patch configuration

## 예상 수정 성격
FATES core ecology를 새로 만드는 일은 적다.
주요 부담은:
1. ELM/ParFlow/FATES build and run infrastructure
2. geomorphic soil/root state remapper
3. fine-grid performance engineering

## 구현 난이도
**과학 코드 수정: 중간**
**소프트웨어/HPC 스택: 높음**

---

# 2. LPJ-GUESS SEC/PPA path

## 공개 precedent를 그대로 쓸 수 있는 것
### SEC/PPA
- tree age/size cohorts
- persistent canopy gaps
- explicit canopy-understory light structure
- shrub/herbaceous PFT competition lineage

### PF-LPJG
published LPJ modifications:
1. LPJ soil discretization을 ParFlow column과 맞춤
2. layer-specific sand/clay/silt inputs
3. ParFlow soil moisture로 LPJ internal soil-water state overwrite
4. MPI coupler를 main `framework.cpp`에 삽입

published coupled experiment는 grid cell당 LPJ patch 하나를 사용하고 patch-destroying disturbance를 끈 configuration을 사용했다.

### EarthShape / Landlab
- Python external orchestration
- segmented LPJ execution
- dump / restart transfer
- terrain -> LPJ site/landform input generation
- elevation / slope / aspect / soil-depth bridge
- LPJ vegetation -> geomorph field bridge
- vegetation state에 따라 geomorphic erodibility / diffusivity를 매 coupling step 갱신한 공개 code precedent

## 고운사에서 반드시 새로 넣을 것
### A. modern branch integration
PF-LPJG base = LPJ-GUESS 4.0.1 era
SEC/PPA = revision 13221

따라서 old PF branch 전체 merge가 아니라 modern SEC source에 다음 개념을 port해야 한다.
- external hydrology state interface
- soil layer mapping
- MPI or alternative coupler
- layer-specific hydraulic properties

SEC code archive는 현재 public record는 보이지만 files가 restricted 상태이므로 exact branch diff 감사에는 접근 제한이 있다.

### B. storm/root-loss event hook
LPJ existing mortality code처럼:
```text
cmass_root *= remaining
cmass_leaf *= remaining
cmass_sap *= remaining
...
```
하는 event hook은 구조적으로 가능하다.

필요한 추가 결정:
- removed root C/N -> exported sediment / litter / soil organic pool
- exposed-but-surviving root stress
- partial cohort mortality rule

### C. subannual recovery limitation
일반 자연식생의 `growth()`는 연말 실행:
- tissue turnover
- new biomass allocation
- reproduction
- updated allometry

따라서 root-loss state를 즉시 적용할 수 있어도 native structural recovery는 annual이다.

고운사에서 필요한 경우 추가:
```text
subannual fine-root recovery routine
```
또는 annual recovery를 허용하는 sensitivity comparison.

### D. soil/root conservative remapper
RE / EarthShape precedent가 soil-depth representation을 돕지만 erosion root truncation과 state mass conservation은 새 coupling이다.

## 구현 난이도
**branch/code integration: 높음**
**external orchestration: 기존 precedent가 있어 중간**
**scientific canopy architecture fit: 매우 높음**

---

# 3. MEDFATE + medfateland path

## 그대로 쓸 수 있는 것
- actual GIS cells
- tree cohorts
- shrub cohorts
- `herbData` physiological cohorts
- cohort Z50 / Z95 / optional Z100 roots
- daily water / carbon / woody growth
- daily fine-root biomass growth
- spatial seed dispersal for woody recruitment
- daily woody seedling environmental filtering
- surface / subsurface / groundwater / channel routing
- one-day execution functions
- ordinary R/Rcpp state objects
- cell-specific soil-layer widths / soil depth
- external hydrology delegation option

## 고운사에서 반드시 새로 넣을 것
### A. herb demographic lifecycle
현재 source limitation:
`growth_day_c.cpp`:
```text
else if(ctype[j] == "herb") dynamicCohort = false;
```

`regeneration.R`:
- seed production / seedling bank / recruit generation이 tree/shrub 중심
- recruit forest 생성 시 `herbData` 제거

따라서 필요한 extension:
```text
herb seed production
 -> seed bank / dispersal
 -> germination filter
 -> herb recruit cohort / herbData
 -> daily physiological growth
 -> demographic mortality / disappearance
 -> cohort merge / turnover
```

기존 woody seedling code에서 재사용 가능한 환경필터:
- soil-layer water potential
- root depth Z50/Z95
- drought mortality
- ground PAR light mortality
- temperature filtering

### B. conservative soil remapper
`soil_redefineLayers()`는 geometry 변경은 가능하지만 initialized state를 보존하지 않는다.

새 함수 필요:
```text
old layers + state
 -> overlap-based remap
 -> new widths
 -> water / C/N / rhizosphere state conservation
```

### C. physical root truncation
new soil geometry 안에서 root fractions를 재정규화하는 것과 실제 eroded root mass loss를 구분해야 한다.

## 구현 난이도
**geomorphic coupling: 낮음-중간**
**herb biology extension: 중간**
**software stack: 낮음**

---

# 4. JULES-RED fallback

## 그대로 쓸 수 있는 것
- tree/shrub woody mass classes
- grass class
- daily RED demographic integration
- subdaily land-surface water/energy
- external layer-wise `sthuf` prescription
- restart `plantNumDensity`

## 새로 필요한 것
- spatially variable/dynamic soil geometry extension
- richer root-by-layer state
- erosion root truncation
- fine catchment implementation

표준 JULES의 domain-common soil layer geometry 때문에 고운사 shallow-soil heterogeneity에는 코드침습성이 크다.

## 구현 난이도
**demography: 낮음**
**고운사 soil-geometry extension: 높음**

---

# 5. 최소 수정범위 비교

| 항목 | FATES | LPJ-GUESS SEC | MEDFATE | JULES-RED |
|---|---|---|---|---|
| 기존 biology 완성도 | 매우 높음 | 높음 | 중상 | 중상 |
| daily structural recovery | O | X, 자연식생 annual | O | O |
| herb lifecycle | O/강함 | 부분적 | **새 개발 필요** | 단순 grass class |
| actual GIS unit | host grid O | external grid/coupler | **native O** | grid O |
| cell-specific soil depth | host dependent | branch/custom | **native O** | 표준 X |
| geomorph root truncation | 새 coupling | 새 coupling | 새 coupling | 새 coupling |
| dynamic soil-state remap | 새 coupling | 새 coupling | 새 coupling, 구조 명확 | 새 coupling, 침습적 |
| branch merge 필요 | X | **O** | X | X |
| external heavy stack | **매우 큼** | 중-큼 | 작음 | 중간 |
| fine-grid performance risk | 큼 | 미확인/중간 | 셀수 scaling | 중-큼 |

---

# 6. 현재 production prototype 우선순위

## Scientific reference implementation
**FATES + ELM/ParFlow**

목적:
- 가장 완전한 daily demography/root hydraulics
- Gounsa 최종 결과의 생태적 benchmark

## Engineering prototype
**MEDFATE + medfateland**

목적:
- 실제 GIS/day-by-day loop를 가장 빠르게 구성
- geomorph soil/root remapper 개발과 검증
- herb lifecycle extension 규모 측정

## Canopy-structure alternative
**LPJ-GUESS SEC/PPA + PF/EarthShape lineage**

목적:
- persistent-gap cohort structure가 결과에 중요한지 비교
- annual allocation limitation의 효과 평가

현재 즉시 하나만 채택하는 대신 이 세 경로의 작은 subcatchment prototype 비용을 비교한 뒤 final engine을 정하는 것이 가장 타당하다.

---

# 7. 다음 구현 전 확인
1. FATES fine-grid seed neighbor builder를 대체하지 않고 어느 크기까지 실행 가능한지 작은 synthetic benchmark 설계
2. MEDFATE herb lifecycle extension에 필요한 exact function list와 최소 parameter set 정의
3. LPJ SEC source access 여부 재확인 및 PF coupler port 대상 interface 목록 작성
4. 공통 geomorphic conservative remapper의 model-independent state specification 작성

# 판정
현재 병목은 더 이상 `적절한 식생모델을 못 찾았다`가 아니다.

병목은 세 후보의 서로 다른 부족부분이다.

```text
FATES   : software/HPC complexity
LPJ     : branch integration + annual recovery cadence
MEDFATE : herb demographic lifecycle
```

공통 새 개발은:
```text
geomorphic soil-layer remap
+ physical root truncation
```
이다.
