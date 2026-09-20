# 결정: 고운사 chemical weathering, regolith production, soil-thickness mass balance

날짜: 2026-09-21

## 질문
LPJ-GUESS-CNP/Hartmann weathering flux를 실제 토양/레골리스 두께변화로 어떻게 변환할 것인가?

## 핵심 결정
다음 두 과정을 절대 동일시하지 않는다.

```
chemical dissolved mass loss
!=
bedrock-to-regolith front advance
```

따라서 A/B mobile soil과 C/Cr regolith를 별도 상태로 계산한다.

---

## 1. A/B mobile soil

상태:
```
M_AB = rho_AB H_AB
```

Yoo 2007, Brosens et al. 2020 계열:

```
dM_AB/dt
=
Phi_AB
+
D_phys
-
E_phys
-
W_AB
```

approximately constant `rho_AB`이면:

```
dH_AB/dt
=
(
Phi_AB
+
D_phys
-
E_phys
-
W_AB
)
/ rho_AB
```

여기서:
- `Phi_AB`: underlying C/Cr에서 mobile soil로 공급되는 질량
- `D_phys`: 물리적 퇴적
- `E_phys`: SWEHR 및 사면과정에 의한 물리적 제거
- `W_AB`: chemical dissolved mass loss

이 식을 A/B soil-thickness bookkeeping의 기본으로 채택한다.

---

## 2. bulk chemical weathering

LPJ-GUESS-CNP의 P-weathering 계보를 재검토했다.

Hartmann & Moosdorf 2011 부모모델은 먼저:
```
bulk chemical silicate-rock weathering
```
을 major cations + dissolved silica flux로 계산한 뒤, lithology-specific P content를 사용해 P liberation을 계산한다.

따라서 고운사에서는:

```
F_bulk_chem
```
과:
```
F_P_release
```
를 별도 변수로 둔다.

개념적으로:

```
F_bulk_chem
=
f(lithology, runoff)
* F_T
* F_shield
```

```
F_P_release
=
F_bulk_chem
* p_rel
```

LPJ-GUESS P-pool flux를 geomorphic mass flux로 역산하는 방식은 기본안으로 쓰지 않는다.

---

## 3. C/Cr regolith thickness

Regolith thickness는 chemical dissolved mass flux를 density로 나눈 값으로 직접 갱신하지 않는다.

DynSoil/MErSiM lineage:

```
dh_reg/dt
=
P_r
-
E_boundary
```

Primary-mineral depletion:

```
partial x/partial t
=
-P_r partial x/partial z
-
K tau^sigma x
```

Chemical weathering:

```
W
=
integral K tau^sigma x dz
```

즉:
- `P_r` controls bedrock-to-regolith production
- `W` controls mineral dissolution within regolith
- `E_boundary` removes regolith physically

를 별도로 둔다.

---

## 4. front-production 후보

### DynSoil / MErSiM
장점:
- transient state equations
- `h_reg`, `x(z)`, `tau(z)` explicit
- climate and physical erosion coupling
- annual outer bookkeeping에 이식하기 쉬움

단점:
- global/geologic parameterization
- vegetation/root effects absent

### Braun 2016
장점:
- pore-fluid velocity and groundwater gradient로 weathering-front advance를 물리적으로 계산
- rock/mineral properties explicit

단점:
- recharge, groundwater geometry, fractured-bedrock permeability 필요
- parameter burden 큼

현재:
**DynSoil/MErSiM state architecture를 우선 후보, Braun 2016을 hydrologic-mechanism alternative로 둔다.**

production hard-lock은 아직 하지 않는다.

---

## 5. woody mechanical production

Gabet & Mudd 2010:

```
LPJ-GUESS woody cohort/root state
 -> root fracture/tree throw
 -> P_woody_mech
```

Chemical front production과 별도 항으로 취급한다.

그러나 selected `P_r`가 자연조건의 total regolith production에 이미 biological mechanical effects를 포함하도록 calibration되었다면 중복 가능성이 있다.

따라서 Gounsa에서는:

```
P_total
=
P_chem_front,residual
+
P_woody_mech
+
P_other_phys
```

처럼 process attribution을 유지하는 방향을 선호한다.

---

## 6. current full state architecture

```
LPJ-GUESS
  |
  +-- runoff/Tsoil
  |     -> Hartmann bulk chemical-loss forcing
  |     -> W_chem
  |
  +-- hydrologic/climate state
  |     -> chemical front production P_chem
  |
  +-- woody cohorts/root state
        -> Gabet-Mudd P_woody_mech

SWEHR/hillslope modules
  -> E_phys / D_phys

A/B balance
  -> H_AB

C/Cr regolith balance
  -> H_reg

H_AB + H_reg
  -> surface/subsurface geometry
```

---

## 7. resolved
- chemical dissolved mass loss and regolith production are now separated
- A/B mobile-soil mass-balance form is selected
- Hartmann parent bulk weathering is separated from P release
- transient regolith state candidate is identified

## 8. unresolved
1. Gounsa 100-year magnitude of `P_chem_front`, `W_chem`, `P_woody_mech`
2. local lithology parameters and rock density
3. exact C/Cr initial thickness/state
4. recharge/subsurface hydrology if Braun is used
5. residual calibration of chemical front production after explicit woody mechanical weathering
6. how much chemical mass loss occurs in A/B versus deeper C/Cr

## 최종 판정
다음 단계는 **100년 order-of-magnitude test**다.

If chemical/front production over 100 years is negligible relative to water erosion, dry ravel, tree throw and landslide, use the simplest mass-balance implementation.

If it is material, implement DynSoil/MErSiM-style transient regolith states.
