# 2D Hairsine-Rose / FEaST / SWEHR postfire lineage

## 목적
고운사 유수침식 본체 후보로 Hairsine-Rose 계열의 2D 구현을 통합 관리한다.

핵심 질문:
- genuine 2D인가?
- rainfall-driven과 flow-driven erosion을 동시에 계산하는가?
- original cohesive soil과 loose/deposited soil을 구분하는가?
- rill이 fixed mask 없이 발생 가능한가?
- multi-size sediment와 armoring/shielding을 표현하는가?
- LPJ-GUESS root/litter coupling을 코드 수준에서 넣기 쉬운가?

## 이론적 기반

### Hairsine & Rose 1991/1992
상태를 구분한다:
```
original cohesive soil
<-> suspended sediment
<-> deposited cohesionless layer
```

Deposited layer는 원토양을 shielding한다.

Flow entrainment later implementations:
```
r_i = (1-H) f_oi (F/J) (Omega - Omega_0)
```

- `H`: deposited-layer shielding fraction
- `F`: effective fraction of excess stream power
- `J`: specific energy of entrainment [J kg^-1 = m2 s^-2]
- `Omega_0`: critical stream power

## 2D implementations

### Kim et al. 2013, tRIBS-OFM/FEaST
- genuine 2D Saint-Venant
- unstructured finite volume
- rainfall detachment/redetachment
- flow entrainment/reentrainment
- multi-size sediment
- original/deposited layers
- hydrology coupling
- real catchment application

### McGuire et al. 2016, SWEHR
- genuine 2D postfire hillslope flow
- Hairsine-Rose sediment
- steep burned mountain catchment
- high-resolution topography and TLS topographic-change calibration
- emergent rills, no fixed rill mask
- multi-size sediment
- original/deposited-layer shielding
- vegetation represented as cover/throughfall in original paper

### Ouyang et al. 2023
- postfire mountain catchment
- SWE + Hairsine-Rose
- five sediment classes
- loose fire-disturbed topsoil layer
- deposition/shielding
- debris-flow transition

### Kim et al. 2016, tRIBS-VEGGIE-FEaST
- dynamic ecohydrology and 2D Hairsine-Rose exist in one modeling system
- erosion-state memory across events
- deposited layer/PSD evolve through event sequences
- direct root-biomass -> erodibility coupling is not implemented

## root/soil-strength bridge

### Misra & Rose 1995
Observed:
```
soil strength ↑
 -> rainfall detachability ↓
 -> J ↑
 -> runoff erodibility ↓
```

This supports using `J` as a soil-strength-sensitive flow-entrainment resistance variable.

However:
**no universal cohesion-to-J equation has been verified.**

### De Baets 2008/2020
EUROSEM/root mechanics lineage:
```
root density/RLD
 -> erosion-specific soil cohesion
 -> lower concentrated-flow detachment
```

2020 mechanistic formulation:
```
c_Max = c_Bare [1 + gamma(RLD_T) R]
c_Min = c_Bare [1 + gamma(RLD_T) r]
gamma(x) = M_max tanh(M1 x / M_max)
```

This gives the root-to-soil-strength side of the bridge, but not a universal numerical `cohesion -> J` transfer.

## litter bridge

### surface-exposed litter
Direct mass evidence:
- Li et al. 2014: 0-1 kg m^-2 litter
- Xia et al. 2019: 300/500/800 g m^-2 forest litter
- Zhu & Cheng 2022: litter mass + decomposition state

Effects:
- rainfall interception
- raindrop shielding
- flow slowing
- sediment trapping

No verified universal:
```
surface litter mass -> Hairsine-Rose original-soil detachability a
```
equation has yet been found.

### incorporated/buried litter
- Sun et al. 2016
- Liu et al. 2020
- Wang et al. 2022

Directly affects:
- `K_r`
- `tau_c`
- soil structural resistance

LSAD is a strong predictor of `K_r`.

Important:
```
SurfaceLitter != IncorporatedLitter
```
and undecomposed buried litter can even increase interrill erosion under some conditions.

## SWEHR 1.0 source-code audit

Public repository:
`csdms-contrib/swehr`

License:
GPL-2.0.

Language:
C.

Repository is extremely compact:
- `SWEHR.c` about 77 kB
- simple text inputs

### existing spatial parameter hooks

Source arrays include:
- `ASMASK[i][j]`: original-soil rainsplash detachability
- `ADSMASK[i][j]`: deposited-sediment rainsplash detachability
- `JSMASK[i][j]`: specific entrainment energy for original cohesive soil
- `UC[i][j]`: critical stream power for original soil
- `UC2[i][j]`: critical stream power for detached/deposited material
- `SMASK[i][j]`: explicitly described as a mask that can modify soil erodibility
- `H[i][j]`: deposited-layer shielding
- `M[k][i][j]`: deposited sediment mass by size class

### source equations

Original-soil rainsplash:
```
E1 = (1-H) * P_k * ASMASK * R
```

Runoff entrainment first computes excess stream power:
```
omega = rho_w g S_f q
E_sp = beta * (omega - UC),  if omega > UC
```

Then:
```
E3 = (1-H) * P_k * F / JSMASK * E_sp
```

Thus `JSMASK` is already a per-cell field and directly scales flow-driven entrainment resistance.

### example input
The bundled example sets:
- `F = 0.004`
- `h0 = 0.00099 m`
- `mtstar0 = 3 kg m^-2`
- `J = 30 m2 s^-2`
The example has zero original/deposited rainsplash detachability and therefore is only a minimal code example, not a forest calibration.

## implementation significance for Gounsa

SWEHR already exposes nearly all target coupling fields:
```
LPJ-GUESS / soil state
   ├─ root state -> JSMASK and/or UC
   ├─ surface litter -> ASMASK / interception / roughness
   ├─ loose surface sediment -> M, H
   └─ particle-size distribution -> P_k
```

Therefore code surgery is much smaller than building a new 2D erosion model.

But:
- root -> J or UC must use a defensible published/calibrated relation
- surface-litter mass -> ASMASK is still unresolved
- do not describe these mappings as existing SWEHR features

## comparison with Iber+

SWEHR advantages for Gounsa:
- actual steep postfire mountain validation
- emergent rills
- Hairsine-Rose original/deposited soil structure
- multiclass sediment
- published vegetation-recovery sensitivity
- public GPL C source
- very small, modifiable code
- cell-wise erodibility arrays already present

Iber+ advantages:
- newer GPU/CUDA framework
- finite-volume mature hydro-morphodynamics
- multiclass suspended + bedload
- Exner update
- higher-performance engineering architecture

Open question:
whether Iber+ full source is as directly modifiable/public as SWEHR and whether its loose-layer formulation offers enough benefit to outweigh SWEHR's postfire-specific structure.

## current judgment
**SWEHR / 2D Hairsine-Rose is now a top candidate, not merely a benchmark.**

It may be better suited to Gounsa than Iber+ because its published process structure maps directly onto:
- intact soil
- loose/deposited postfire layer
- rill emergence
- postfire event erosion
- multi-size sediment
- long-term event memory through the FEaST lineage

Final selection remains pending:
1. direct comparison of SWEHR vs Iber+ vs SERGHEI-SE source extensibility
2. final root-resistance mapping
3. final exposed-litter mapping
