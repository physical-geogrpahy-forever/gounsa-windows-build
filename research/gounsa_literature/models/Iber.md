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
