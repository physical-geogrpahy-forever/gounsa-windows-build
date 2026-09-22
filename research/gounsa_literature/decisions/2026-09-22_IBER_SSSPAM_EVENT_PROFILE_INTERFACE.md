# 결정: event erosion은 Iber+, long-term profile은 SSSPAM/mARM으로 분리

날짜: 2026-09-22

## 상태
이 결정은 같은 날짜의 `2026-09-22_DYNAMIC_ARMOUR_MODEL_SELECTION.md` 중
`OpenLISEM+SWATRE for event hydro-erosion` 부분을 **수정/대체**한다.

SSSPAM/mARM의 long-term armour/profile 선택 자체는 유지한다.

## 왜 event engine 선택이 바뀌었는가
OpenLISEM source inspection 결과:
- 총 detachment/deposition은 kg/cell로 명확하게 보존
- SWATRE soil water는 강점
- 그러나 current source에서 material-depth evolution은 disabled
- grain-size-distribution controls와 일부 UI가 inactive/commented
- therefore class-by-class persistent sediment-state handoff가 production path로 불확실

반면 Iber+ 2024:
- genuine 2D SWE
- original soil vs loose sediment layer 분리
- class별 suspended/bed load
- class별 detachment/redetachment/deposition
- M_s,k [kg m^-2] mass conservation
- dynamic loose-layer grading f_k
- shielding
- Exner topographic update
가 published active model로 검증됨.

따라서 **입도별 armour와 장기 profile coupling을 생각하면 Iber+가 event erosion engine으로 더 방어적**이다.

## 최종 역할분담

### 1. event soil hydrology
고운사 매립 석력의 hydraulic properties는 independent measurements를 우선한다.

Iber+ Green-Ampt inputs:
- Ksat: measured effective stony-soil Ksat
- porosity / theta_s: measured
- initial saturation: measured pre-event water state
- soil depth: measured/modelled current depth
- wetting-front suction: Neuman 1976 published relation from effective hydraulic curve
- initial abstraction: only independently measured/represented interception/depression storage; output-fit calibration 금지

GEM/Naseri는 field measurement가 없는 cell/property의 physically based estimator/benchmark로 유지한다.

### 2. event 2D runoff + erosion
**Iber+ 2024**

Persistent source terms by class:

```
E_orig,k
=
A_cell ∫(D_rdd,k + D_fdd,k) dt
```

이는 original soil matrix에서 새로 제거된 질량.

```
E_redet,k
=
A_cell ∫(D_rdrd,k + D_fdrd,k) dt
```

이는 loose layer 재이동이며 deep profile loss로 다시 계산하지 않는다.

event-end surface state:
```
M_s,k(end)
f_k(end)
z_b(end)
```

### 3. long-term embedded PSD / weathering
**SSSPAM / mARM3D/mARM5D**

사용:
- depth-resolved particle-size profile
- weathering transition matrices
- subsurface resupply
- profile restructuring
- soil depth bookkeeping

사용하지 않음:
- SSSPAM 자체 calibrated fluvial erosion equation
- SSSPAM의 event erosion/deposition을 Iber+ 결과 위에 다시 계산

### 4. exact handoff
Event after Iber+:

```
Iber+ E_orig,k
 -> SSSPAM top profile depletion / vertical resupply

Iber+ M_s,k(end), f_k(end)
 -> persistent surface loose/armour state

Iber+ z_b(end)
 -> authoritative next-event DEM

SSSPAM inter-event weathering
 -> updated surface/subsurface PSD

SSSPAM newly exposed top-layer grading
 -> next Iber+ g_k

persistent loose/armour mass
 -> next Iber+ M_s,k(initial)
```

## double-counting 금지
다음은 하지 않는다.

1. Iber+ redetachment를 SSSPAM deep-profile erosion으로 다시 제거
2. Iber+ Exner elevation change 뒤 SSSPAM에서 같은 event mass로 DEM을 다시 변화
3. Iber+ class-selective deposition 뒤 SSSPAM deposition matrix로 같은 sediment를 다시 sorting
4. Iber+ shielding과 별도 custom armour factor를 동시에 곱함

## 아직 완전히 닫히지 않은 interface
Iber+의 variable-thickness loose layer와 SSSPAM의 armour/profile layer discretisation은 동일하지 않다.

따라서 두 state를 단순 동일시하지 않는다.

최소자의성 방침:
- surface state의 authoritative mass는 Iber+의 M_s,k [kg m^-2]
- SSSPAM은 deeper profile and weathering state를 관리
- surface/deep exchange가 발생할 때는 mass conservation + existing SSSPAM vertical-resupply rule만 사용
- 별도 fitted exchange coefficient를 만들지 않는다

이 layer-boundary 구현은 software engineering 문제이며, 새로운 empirical process equation으로 만들지 않는다.

## shielding parameter M_s,cr
Iber+:
```
epsilon = min(M_s/M_s,cr,1)
```

M_s,cr는 free calibration parameter로 사용하지 않는다.

우선순위:
1. field-measured armour mass per area
2. measured armour thickness + measured rho_s + porosity
3. independent experiment
4. 불가하면 literature-constrained uncertainty range

soil-loss output에 맞춰 tuning하는 것은 금지.

## OpenLISEM의 위치
OpenLISEM+SWATRE는 탈락시키지 않는다.

용도:
- stony-soil Richards hydrology benchmark
- postfire-event comparison
- measured theta-h-K sensitivity test

하지만 **primary event erosion engine은 Iber+로 변경**한다.

## 현재 production architecture

```
LPJ-GUESS
    |
    v
measured stony-soil hydraulic state
(+ GEM/Naseri benchmark where needed)
    |
    v
Iber+ 2024
2D runoff
multiclass detachment/redetachment/deposition
dynamic loose-layer mass
Exner event topography
    |
    | E_orig,k ; M_s,k(end) ; z_b(end)
    v
SSSPAM / mARM
depth-resolved embedded PSD
vertical resupply
physical weathering
inter-event profile evolution
    |
    v
next-event g_k, soil depth, surface/subsurface grading
```

## 자의성 원칙
새로 만드는 것은 process equation이 아니라 state transfer/interface이다.

각 parameter는:
- 측정값
- published model parameterisation
- 독립 실험
중 하나로 제약한다.

erosion-output fitting으로 임의 보정하는 parameter는 production model에서 허용하지 않는다.
