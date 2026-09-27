# 고운사 표면 입도분포 모델 후보 재검토 — 2026-09-28

## 검토 목적
고운사 100년 산불 후 식생-지형 모델에서 사용할 `표면 입도분포(surface grain-size distribution)` 엔진을 최신 published numerical model 중심으로 다시 검토한다.

## 고정 기준
후보는 다음 항목을 분리해서 평가한다.

1. 고운사 외부 forcing/coupling interval인 **1시간 자료와 직접 결합 가능한가**
2. genuine 2D 공간구조인가
3. 표면 PSD/GSD를 동적 상태변수로 추적하는가
4. 암편 weathering/fragmentation이 PSD를 갱신하는가
5. 입도별 이동/침식/퇴적을 계산하는가
6. infiltration을 계산하는가
7. runoff/overland flow를 계산하는가
8. hillslope/mountain 환경에 실제 적용 또는 명시적 설계가 되었는가
9. 코드 또는 재현 가능한 구현이 공개되어 있는가

`solver internal timestep`과 `외부 forcing/coupling interval`은 구분한다. 내부 안정성 때문에 초/분 단위 substep을 쓰는 것은 허용되지만, 1분 강우 forcing을 필수로 요구하는 published configuration을 그대로 `1-hour model`이라고 부르지 않는다.

---

## 1. Shmilovitz et al. 2024
DOI: 10.1029/2023JF007478

### 확인된 기능
- 표면 debris를 여러 grain-size class로 유지
- particle-size-dependent runoff transport
- physical fragmentation: mARM 계열 transition matrix
- dry ravel
- Green-Ampt infiltration
- Landlab OverlandFlow
- code 공개

### 핵심 제한
- 실제 논문 계산격자는 `80–200 × 3`이며 경계조건상 **effectively 1D**
- rainfall forcing은 **1-min resolution**, storm duration 약 15–95 min
- debris-layer `Ks`, `psi_f` 등은 외생 parameter이며 현재 PSD에서 동적으로 계산되지 않음
- 건조지 cliff/talus 대상, 식생 없음

### 판정
과정 결합의 중요한 최신 선례지만 고운사 production surface-GSD engine으로 그대로 채택하지 않는다.

---

## 2. RiverBedDynamics v1.0 — Monsalve et al. 2025
DOI: 10.5194/gmd-18-3427-2025

### 확인된 기능
- genuine 2D raster
- OverlandFlow와 동적 결합
- non-steady hydraulics
- surface + substrate GSD
- grain-size-specific Exner mass balance
- 입도별 erosion/deposition/transport
- active-layer sorting 및 stratigraphy
- hours-to-years 적용을 명시
- code 공개

### 핵심 제한
- 주 검증대상은 gravel-bed river
- hillslope overland flow에도 같은 formulation을 사용할 수 있다고 설명하지만 forest mountain hillslope 검증은 없음
- **infiltration 없음**
- **weathering/fragmentation 없음**
- Manning roughness가 GSD에 따라 동적으로 갱신되지 않으며 저자도 future enhancement로 제시
- large boulder/vegetation macro-roughness 미구현

### 판정
현재 검토한 최신 published model 중 **2D dynamic surface-GSD transport engine으로 가장 강한 후보**. 단독으로는 고운사 표면암편 모델 완성 불가.

---

## 3. CAESAR-Lisflood
주요 model lineage: Coulthard et al.; 현재 공개 구현/매뉴얼 지속 사용

### 확인된 기능
- 2D Lisflood-FP hydrodynamics
- catchment mode에서 **hourly rainfall input 사용 선례가 명확함**
- 최대 9 grain-size fractions
- active layers와 dynamic D50/armouring
- Wilcock-Crowe 또는 Einstein-Brown 계열 입도별 sediment transport
- slope processes 포함
- mountainous/post-earthquake catchment 적용 선례

### 핵심 제한
- 현 공개 model의 표준 기능에는 **particle weathering/fragmentation function이 없음**
- 과거 적용에서 weathering effect를 수동 PSD 수정으로 처리한 사례가 있음
- hydrology는 rainfall-runoff model + 2D routing 구조이며 표면 PSD/rock cover가 infiltration hydraulic parameters를 동적으로 바꾸는 기능은 확인되지 않음

### 판정
`1-hour forcing + 2D + multi-grain transport` 조건에는 매우 강하지만 `surface particle weathering`과 `PSD -> infiltration` 때문에 단독 채택 불가.

---

## 4. mARM3D / mARM5D
Cohen et al. 2010; Cohen et al. 2015

### 확인된 기능
- profile layers + spatial grid
- PSD state vector
- physical weathering/fragmentation
- size-selective fluvial erosion/armouring
- mARM5D: diffusive transport, fluvial transport, soil depth/PSD evolution

### 핵심 제한
- 장기 soil/landscape evolution 목적
- 1-hour hydrology model 아님
- explicit event infiltration/2D overland flow engine이 아님

### 판정
weathering/fragmentation 및 PSD 질량보존의 선행 핵심 계보로 유지하되 production hydrology/transport engine으로는 부적합.

---

## 5. Li, Sklar & Gasparini 2025
DOI: 10.1002/esp.70111

### 확인된 기능
- fracture-controlled latent initial GSD
- climate, lithology, erosion rate, residence time에 따른 hillslope weathering/size reduction
- landscape-scale spatial grain-size production
- code/data 공개

### 핵심 제한
- landscape evolution timestep 50 yr
- event hydrology, infiltration, surface armour transport 없음
- surface grain-size movement engine이 아니라 **grain-size production/weathering model**

### 판정
fire-spall/bedrock-derived initial PSD와 장기 weathering parameterization의 보조 근거. 표면 transport engine 후보가 아님.

---

## 6. RiverBedDynamics 외 최신/인접 후보

### CIDRE v2.0 (2023)
- grain tracking은 가능하지만 grains are passive tracers이며 GSD가 erosion/hydraulics를 되먹임하지 않음
- geological-timescale LEM, infiltration 없음
- 탈락

### goSPL 2026 preprint
- hydrology, regolith, weathering geochemistry가 크게 확장됨
- 그러나 현재 확인 범위에서 고운사에 필요한 dynamic surface coarse-fragment GSD + size-selective hillslope transport + infiltration feedback model은 아님
- 또한 2026-09 현재 preprint 상태
- 직접 후보에서 제외

---

# 엄격 비교 요약

| 모델 | 1h coupling | genuine 2D | dynamic surface GSD | fragmentation/weathering | size-selective transport | infiltration | runoff | hillslope/mountain | code |
|---|---|---|---|---|---|---|---|---|---|
| Shmilovitz 2024 | △ published forcing 1-min | X effectively 1D | O | O | O | O | O | O rocky dryland | O |
| RiverBedDynamics 2025 | O external coupling 가능, internal substep | O | O | X | O | X | O via OverlandFlow | △ hillslope equations 가능, river-focused validation | O |
| CAESAR-Lisflood | O hourly rainfall precedent | O | O | X | O | △ rainfall-runoff, no PSD-controlled infiltration | O | O catchment/mountain applications | O |
| mARM5D 2015 | X | O spatial grid + depth | O | O | O | X | △ prescribed runoff/discharge framework | O hillslope | △ |
| Li et al. 2025 | X 50-yr LEM step | O landscape grid | △ produced GSD | O weathering production | X event transport | X | X | O landscape | O |

---

# 현재 결론

## 1. 단일 published model
**현재 확인한 published models 중 고운사의 모든 조건을 동시에 만족하는 단일 모델은 없다.**

특히 동시에 만족되지 않는 조합은:

```text
1-hour forcing/coupling
+ genuine 2D
+ dynamic surface GSD
+ particle weathering/fragmentation
+ size-selective hillslope transport
+ infiltration/runoff
+ PSD -> infiltration feedback
```

이다.

## 2. 최신 핵심 후보의 역할 구분
- **RiverBedDynamics 2025**: genuine 2D dynamic GSD transport/erosion/deposition
- **Shmilovitz 2024 / mARM lineage**: fragmentation/weathering transition
- **CAESAR-Lisflood**: hourly rainfall + 2D catchment multi-grain precedent
- **Li et al. 2025**: hillslope grain-size production/weathering control

이들을 하나의 기존 published model이라고 부르면 안 된다. 고운사에서 결합하면 **새로운 coupling**이다.

## 3. 가장 큰 남은 공백
`surface GSD / rock cover -> infiltration parameters`를 동적으로 계산하는 검증된 최신 hillslope model이 현재 가장 큰 공백이다.

따라서 다음 문헌조사는 일반적인 표면암편 실험이 아니라 다음 질문 하나로 좁힌다.

> `dynamic surface grain-size/rock-cover state`로부터 `Ks, infiltration capacity, Green-Ampt/vG parameters, roughness`를 계산하여 runoff solver에 되먹임하는 published process model이 있는가?

이 질문이 해결되지 않으면 표면입도와 수문을 연결하는 부분은 고운사의 새로운 coupling으로 명시한다.
