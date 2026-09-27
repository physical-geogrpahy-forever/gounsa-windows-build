# 고운사 표면 입도분포 모델 후보 재검토 — 2026-09-28

## 검토 목적
고운사 100년 산불 후 식생-지형 모델에서 사용할 `표면 입도분포(surface grain-size distribution)` 및 수문-침식 연결을 최신 published numerical model과 현재 유지되는 software 중심으로 다시 검토한다.

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

`solver internal timestep`과 `외부 forcing/coupling interval`은 구분한다. 2D shallow-water solver는 안정성 때문에 초 또는 분 단위 내부 substep이 필요할 수 있다. 이것은 고운사의 1시간 forcing/state-exchange 조건과 모순되지 않는다. 반면 published configuration이 1분 강우 forcing 자체를 연구의 핵심 입력으로 요구한다면 이를 그대로 `1-hour model`이라고 부르지 않는다.

---

## 1. Iber+ multiclass soil erosion — Cea-Gómez et al. 2024
DOI: 10.1016/j.envsoft.2024.106098

### 확인된 기능
- genuine 2D finite-volume shallow-water equations
- rainfall + infiltration terms
- rainfall-driven와 flow-driven erosion을 별도 계산
- `N_p` sediment classes
- loose surface sediment layer와 original soil matrix 분리
- loose-layer class mass `M_s,k`와 mass fraction `f_k`를 **시간 및 공간적으로 동적 갱신**
- suspended load + bed load
- class-specific deposition
- Exner topographic update
- plot, hillslope, meso-catchment, river reach 규모 test
- GPU acceleration, software/data 공개

### 표면입도 상태

```text
M_s = Σ M_s,k
f_k = M_s,k / M_s
```

각 size class의 질량수지를 풀기 때문에 loose surface layer의 입도조성이 erosion/deposition에 따라 실제로 변한다.

### 핵심 제한
- coarse parent fragment의 **physical weathering/fragmentation 없음**
- surface GSD/rock cover가 infiltration parameter를 자동 변경하지 않음
- shield factor는 loose-layer total mass 기반으로, large rock-fragment geometry/cover/embeddedness를 직접 표현하지 않음
- published multiclass validation은 주로 soil-size particles 중심

### 판정
**현재 고운사의 genuine 2D rainfall-runoff + multiclass hillslope erosion 본체로 가장 직접적인 최신 published 후보.**
RiverBedDynamics 2025보다 hillslope rainfall erosion과 infiltration 구조가 직접적이고, rainfall-driven/flow-driven detachment 분리가 고운사 설계와 잘 맞는다. 단, surface coarse-fragment weathering과 GSD→infiltration feedback은 별도 coupling 필요.

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
- flowing-water physics는 channelized와 unchannelized overland-flow areas에 적용 가능

### 핵심 제한
- 주 검증대상은 gravel-bed river
- forest mountain hillslope 검증은 없음
- **infiltration 없음**
- **weathering/fragmentation 없음**
- Manning roughness가 GSD에 따라 동적으로 갱신되지 않으며 저자도 future enhancement로 제시
- large boulder/vegetation macro-roughness 미구현

### 판정
**2025년 기준 가장 강한 genuine 2D dynamic GSD sorting/transport engine 후보.**
고운사에서는 Iber+보다 coarse-gravel active-layer sorting에 강하지만 rainfall-infiltration-hillslope erosion 본체로는 덜 직접적이다.

---

## 3. OpenLISEM current 2026 software
현재 공개 line: 7.4.9 및 7.5.0 beta

### 확인된 기능
- actively maintained 2026 software
- full catchment water balance
- Green-Ampt 및 SWATRE infiltration
- interception, ET, subsurface-water options
- kinematic/diffusive/dynamic 2D flow
- splash/runoff/channel/flood sediment dynamics
- suspended + bedload options
- median grain size 또는 multiple sediment classes
- user-defined/estimated GSD
- detachable material depth 및 dynamic soil-property options
- recent versions include dynamic crusting updates
- external rainfall time series 사용

### 시간구조
Rainfall time series 및 simulation time은 minute-based clock으로 입력되지만 1시간 자료는 60-min interval로 표현 가능하다. 내부 solver timestep은 별개이다.

### 핵심 제한
- **surface coarse-fragment physical weathering/fragmentation 없음**
- dynamic GSD가 Green-Ampt/SWATRE `Ks`, suction, porosity를 자동 갱신하는 기능 확인되지 않음
- fire-spall large fragment/dry-ravel routing 없음
- 2026 최신 기능 일부는 software release 기능이며 각각 peer-reviewed model paper로 검증된 것은 아님

### 판정
**현재 유지관리되는 통합 hydrology + 2D flow + multiclass sediment software로 매우 강한 production-framework 후보.**
그러나 surface-rock weathering 자체의 해결책은 아니다.

---

## 4. CAESAR-Lisflood
주요 model lineage: Coulthard et al.; 공개 구현 지속 사용

### 확인된 기능
- 2D Lisflood-FP hydrodynamics
- catchment mode에서 **hourly rainfall input 사용 선례가 명확함**
- 최대 9 grain-size fractions
- active layers와 dynamic D50/armouring
- Wilcock-Crowe 또는 Einstein-Brown 계열 입도별 sediment transport
- slope processes 포함
- mountainous/post-earthquake catchment 적용 선례
- internal adaptive timestep은 저유량 시 최대 1 h, 홍수 시 훨씬 짧아질 수 있음

### 핵심 제한
- 표준 기능에 **particle weathering/fragmentation 없음**
- 과거 적용에서 weathering effect를 수동 PSD 수정으로 처리한 사례가 있음
- surface PSD/rock cover가 infiltration hydraulic parameters를 동적으로 바꾸는 기능은 확인되지 않음

### 판정
`hourly rainfall + 2D + multi-grain transport` 조건의 실제 선례로 매우 강하다. 다만 고운사에 필요한 표면암편 풍화와 infiltration feedback은 해결하지 못한다.

---

## 5. tRIBS-FEaST / Hairsine-Rose lineage — Kim et al. 2013; Kim et al. 2023
2013 DOI: 10.1002/wrcr.20373
2023 DOI: 10.1029/2022WR033879

### 확인된 기능
- genuine 2D Saint-Venant flow on unstructured triangular grid
- tRIBS hydrology framework: interception, ET, infiltration, runoff production, groundwater dynamics
- Hairsine-Rose multiple particle-size sediment transport
- rainfall/flow detachment separation
- class-specific deposition
- dynamic deposited layer and mechanistic surface shield/armouring
- 2023 hillslope-basin application

### 핵심 제한
- 2023 microtopography application에서는 infiltration loss를 **0**으로 두고 rainfall excess를 사용
- particle size가 Manning roughness 또는 infiltration parameters를 동적으로 갱신하지 않음
- **weathering/fragmentation 없음**
- 최신 core-model development라기보다 검증된 기존 integrated lineage

### 판정
2D hydrology + multiclass Hairsine-Rose shield의 강한 선행모델. 최신 production 후보라기보다는 process precedent로 유지한다.

---

## 6. Shmilovitz et al. 2024
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
**weathering/fragmentation + runoff transport + dry ravel을 한 모델에서 연결한 최신 핵심 선례**이나 고운사의 최종 surface-GSD engine으로 그대로 채택하지 않는다.

---

## 7. mARM3D / mARM5D
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
weathering/fragmentation 및 PSD 질량보존의 핵심 선행 계보로 유지한다.

---

## 8. Li, Sklar & Gasparini 2025
DOI: 10.1002/esp.70111

### 확인된 기능
- fracture-controlled latent initial GSD
- climate, lithology, erosion rate, residence time에 따른 hillslope weathering/size reduction
- landscape-scale spatial grain-size production
- code/data 공개

### 핵심 제한
- landscape evolution timestep 50 yr
- event hydrology, infiltration, surface armour transport 없음
- surface movement engine이 아니라 grain-size production/weathering model

### 판정
fire-spall/bedrock-derived initial PSD와 장기 weathering parameterization의 보조 근거. 표면 transport engine 후보는 아니다.

---

## 9. 기타 최신/인접 후보

### CIDRE v2.0 (2023)
- grain tracking은 가능하지만 grains are passive tracers이며 GSD가 erosion/hydraulics를 되먹임하지 않음
- geological-timescale LEM, infiltration 없음
- 직접 후보에서 제외

### goSPL 2026 preprint
- hydrology, regolith, weathering geochemistry가 크게 확장됨
- 현재 확인 범위에서 dynamic surface coarse-fragment GSD + size-selective hillslope transport + infiltration feedback model은 아님
- 2026-09 현재 preprint
- 직접 후보에서 제외

---

# 엄격 비교 요약

| 모델 | 1h forcing/coupling | genuine 2D | dynamic surface GSD | fragmentation/weathering | size-selective transport | infiltration | runoff | hillslope/mountain | 현재 역할 |
|---|---|---|---|---|---|---|---|---|---|
| Iber+ 2024 | O coupling 가능 | O | O loose layer | X | O | O | O | O hillslope/catchment | **2D runoff-erosion 본체 최우선** |
| RiverBedDynamics 2025 | O coupling 가능 | O | O active layer | X | O | X | O | △ river-focused | **coarse-GSD transport 보조/대안** |
| OpenLISEM 2026 | O rainfall series | O | O multiclass sediment | X | O | O | O | O catchment | **통합 production framework 강력 후보** |
| CAESAR-Lisflood | O hourly precedent | O | O active layers | X | O | △ no GSD-controlled infiltration | O | O mountain/catchment | hourly multi-grain precedent |
| tRIBS-FEaST | O framework coupling | O | O deposited shield | X | O | O base framework; 2023 test X | O | O hillslope | integrated process precedent |
| Shmilovitz 2024 | X published forcing 1-min | X effectively 1D | O | O | O | O | O | O rocky dryland | **fragmentation/dry-ravel precedent** |
| mARM5D 2015 | X | O spatial grid + depth | O | O | O | X | △ | O hillslope | weathering/PSD lineage |
| Li et al. 2025 | X 50-yr LEM step | O landscape grid | △ produced GSD | O | X event transport | X | X | O landscape | production/weathering control |

---

# 현재 결론

## 1. 단일 published model
**현재 확인한 published/current models 중 고운사의 모든 조건을 동시에 만족하는 단일 모델은 없다.**

특히 아직 한 모델에서 닫히지 않는 조합은:

```text
1-hour forcing/coupling
+ genuine 2D
+ dynamic surface GSD
+ particle weathering/fragmentation
+ size-selective hillslope transport
+ infiltration/runoff
+ surface GSD -> infiltration feedback
```

이다.

## 2. 현재 가장 합리적인 production architecture

### 2D rainfall-runoff/erosion 본체
**Iber+ 2024**를 1순위로 재검토한다.

이유:
- genuine 2D
- rainfall + infiltration
- rainfall-driven / flow-driven erosion 분리
- multiple size classes
- dynamic loose-surface-layer GSD
- hillslope/catchment validation
- GPU 구현

### surface coarse-fragment weathering
**Shmilovitz 2024 / mARM transition-matrix lineage**에서 physical fragmentation 구조를 가져오는 것이 가장 직접적이다.

### coarse active-layer sorting이 중요한 경우
**RiverBedDynamics 2025**의 grain-size-specific Exner/active-layer formulation을 비교대안으로 검토한다.

### 전체 software framework 대안
**OpenLISEM 2026**은 수문, infiltration, 2D flow, multiclass sediment를 한 software에서 운용할 수 있다는 장점 때문에 별도 production-framework 후보로 유지한다.

이 결합은 기존 단일 published model이 아니라 **고운사의 새로운 coupling**으로 명시해야 한다.

## 3. 핵심 미해결 공백
가장 큰 남은 문제는 여전히 다음이다.

```text
surface GSD / rock-fragment state
        ↓
Ks, suction, porosity, roughness 또는 infiltration capacity
        ↓
infiltration / runoff
```

Iber+, RiverBedDynamics, OpenLISEM, CAESAR-Lisflood, tRIBS-FEaST 모두 이 feedback을 `dynamic surface coarse-fragment GSD`에서 자동 계산하는 검증된 구조를 제공하지 않는다.

따라서 다음 문헌조사는 일반적 rock-fragment hydrology가 아니라 아래 질문에 한정한다.

> `dynamic surface grain-size/rock-cover state`로부터 `Ks, infiltration capacity, Green-Ampt/vG parameters, roughness`를 계산하고 그 값을 runoff solver에 되먹임하는 published process model이 있는가?

이것이 발견되지 않으면 해당 부분은 고운사의 명시적 새로운 coupling으로 남긴다.
