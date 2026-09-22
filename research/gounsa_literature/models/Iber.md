# Iber+ multiclass erosion lineage

## 핵심 문헌
Cea, García-Feal, Nord, Piton & Legoût (2024). Environmental Modelling & Software 179, 106098. DOI 10.1016/j.envsoft.2024.106098.

## 고운사에서 검토한 이유
modern GPU finite-volume genuine 2D erosion engine that separates rainfall-driven and flow-driven detachment.

## 공간구조
- 2D shallow-water equations
- fully distributed finite volume
- GPU/HPC
- plot to meso-scale catchment

## erosion structure
```
∂(h C_k)/∂t + ∂(q_x C_k)/∂x + ∂(q_y C_k)/∂y
= D_rdd,k + D_rdrd,k + D_fdd,k + D_fdrd,k + D_dep,k
```

Rainfall-driven:
```
D_rdd,k = α_d,k r (1-ε) f_d g_k
```

Flow-driven:
```
D_fdd,k = K_d,k max(τ-τ_s,0)(1-ε)g_k
```

## vegetation
No dynamic root biomass/RLD erosion-resistance formulation was found in this chat.

## critical connection
`K_d` has units kg s^-1 N^-1 and a Foster-style shear-excess form closely comparable to WEPP `K_r`.

This makes Iber+ a mathematically clean target for a root-dependent flow-erodibility coupling, but that coupling is **not already implemented in the 2024 paper**.

## 고운사에 쓸 수 있는 부분
- modern genuine 2D hydraulics
- rainfall vs flow detachment separation
- multiclass sediment
- loose-layer shielding
- Exner morphology

## 새로운 coupling
WEPP/Mao/PROMET/LPJ-GUESS vegetation-state effects supplied to `K_d` or `α_d` are **새로운 coupling**.

## 최종 판정
**현재 핵심 2D-engine 후보 중 하나.**


---

## 2026-09-22 exact state interface review

### persistent event states
Iber+ 2024는 각 particle class에 대해 다음을 분리한다.

Original soil:
```
g_k
D_rdd,k
D_fdd,k
```

Loose layer:
```
M_s,k [kg m^-2]
f_k = M_s,k / M_s
D_rdrd,k
D_fdrd,k
D_dep,k
```

따라서 장기 soil-profile model로 넘길 때 `total detachment`를 사용하면 안 된다.

### persistent original-soil depletion
cell area를 A_i라 하면 event 중 original soil에서 실제 새로 제거된 class-k mass:

```
E_orig,i,k
=
A_i ∫(D_rdd,i,k + D_fdd,i,k) dt
```

이 값만 embedded soil profile depletion에 해당한다.

### loose-layer recycling
```
E_redet,i,k
=
A_i ∫(D_rdrd,i,k + D_fdrd,i,k) dt
```

이는 이미 surface loose layer에 존재하던 material의 재이동이므로 deep profile에서 다시 제거하면 안 된다.

### event-end surface state
Iber+가 계산한:
```
M_s,k(end) [kg m^-2]
```
와
```
f_k(end)=M_s,k/M_s
```
를 다음 event의 surface loose/armour state로 보존한다.

Iber equation 자체에서 equivalent loose-layer thickness:
```
l_d,k = M_s,k / (rho_s phi)
```
이므로 mass-to-thickness에 새로운 식이 필요하지 않다.

### topography
Iber+는 event 안에서 Exner mass conservation으로 z_b를 이미 갱신한다.
따라서 외부 long-term model에서 동일 event erosion/deposition으로 DEM을 다시 갱신하면 이중계산이다.

역할분담 원칙:
- Iber+: event 동안 topography/hydrodynamics coupling
- SSSPAM/mARM: inter-event weathering, depth-resolved PSD/profile restructuring
- event-end DEM은 Iber+ result를 authoritative state로 유지
- SSSPAM은 event erosion depth를 다시 더하지 않고 profile bookkeeping만 일치시킨다.

### 중요한 limitation
Iber+ original-soil grading g_k는 multilayer depth profile로 자동 진화하지 않는다.
따라서 erosion으로 새로운 subsurface layer가 노출되면 next-event g_k를 SSSPAM/mARM profile의 새 surface layer에서 다시 공급해야 한다.

이 전달은 particle-class mass fraction이라는 동일 물리량의 전달이며 새로운 empirical equation은 아니다.

### shielding parameter
```
epsilon = min(M_s/M_s,cr,1)
```
에서 `M_s,cr`는 published model input이지만 고운사 site parameter가 필요하다.

자의성 방지:
- soil-loss fit로 보정 금지
- 현장 armour mass per area 또는 armour thickness + rho_s + phi로 독립 결정
- 독립자료가 없으면 uncertainty range로 남기고 결과에 명시

### 현재 판정
event-scale 2D multiclass erosion과 surface loose-layer state는 OpenLISEM보다 Iber+가 더 적합하다.
이유는 OpenLISEM current code에서 multiclass controls/material-depth evolution 일부가 비활성인 반면 Iber+ 2024는 class별 mass conservation이 published active feature이기 때문이다.


---

## 2026-09-22 기존모델 사용가능성 재감사

### 실제 구현이 강한 부분
2024 Iber+ soil-erosion module 자체에 구현됨:
- 2D shallow-water finite-volume hydrodynamics
- rainfall-driven detachment
- runoff/flow-driven detachment
- loose-layer redetachment
- multiclass suspended load
- multiclass bed load
- class-specific deposition
- class-specific mass conservation
- dynamic loose-layer grading
- shielding by loose sediment mass
- GPU implementation
- laboratory to meso-scale applications
- public software and test cases

### vertical soil structure
2024 erosion module의 vertical structure:
```
loose sediment layer
original soil matrix
non-erodible rock
```

즉:
- loose-layer mass/PSD는 동적
- original-soil grading g_k는 input
- SSSPAM/mARM처럼 여러 깊이 layer의 embedded PSD를 자체적으로 진화시키는 model은 아님
- physical weathering module 없음

### hydrology
Iber+ 자체에는 여러 hydrology/infiltration options가 존재하지만,
2024 erosion paper의 검증사례에서는 일부 test가 simple loss/infiltration parameterization을 사용한다.
따라서 고운사의 stony-soil theta-h-K dynamics가 2024 erosion module 안에서 자동 해결된다고 주장하지 않는다.

### vegetation
2024 soil-erosion module 자체에는:
- root biomass
- RLD
- live/dead root state
- litter biomass
- PFT
를 erosion resistance state로 사용하는 published dynamic module이 없음.

따라서 LPJ-GUESS vegetation state를 Iber erodibility에 연결하면 새로운 coupling이다.

### 판정
**고운사 event-scale 2D water-erosion engine 후보로 매우 강함.**
하지만 단독으로:
- depth-resolved embedded gravel profile
- physical weathering
- quantitative vegetation/root effect
를 해결하지 못함.

### standalone verdict
- event 2D hydrodynamics: 강함
- rainfall/flow erosion separation: 강함
- multiclass surface sediment: 강함
- dynamic loose armour: 강함
- deep embedded PSD: 부족
- weathering: 없음
- quantitative vegetation: 없음

따라서 **전체 production model이 아니라 water-erosion engine 후보**로 분류한다.

## 2026-09-22 적용범위 재감사

### 확인된 적용 범위
Cea et al. (2024)는 다음 규모에서 Iber+ soil-erosion module을 제시/검증했다.
- laboratory multiclass experiment
- 60 x 2.2 m vineyard hillslope plot, 4 rainfall events
- **20 km² French Alps headwater mountain catchment**
- river reach debris-flood morphology case

따라서 `산지 적용성이 없다`고 볼 수는 없다. 산지 유역에서 event-scale 적용 선례가 있다.

### 그러나 확인되지 않은 것
2024 erosion paper 자체에서 다음은 dynamic erosion state로 구현되지 않았다.
- root biomass
- RLD
- dead/live roots
- litter mass
- PFT
- postfire vegetation recovery
- embedded rock-fragment-specific soil hydraulics

따라서 stony forest/postfire physics가 자체적으로 해결된다고 주장하지 않는다.

### 재판정
**event-scale 2D water erosion에는 현재 가장 강한 기존 후보로 유지.**
단, quantitative vegetation과 deep stony profile은 별도 문제다.
