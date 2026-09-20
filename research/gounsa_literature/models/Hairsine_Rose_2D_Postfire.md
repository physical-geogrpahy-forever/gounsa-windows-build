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

## comparison with Iber+ and SERGHEI-SE

### SWEHR advantages
- actual steep postfire mountain validation
- emergent rills
- Hairsine-Rose original/deposited soil structure
- multiclass sediment
- published vegetation-recovery sensitivity
- public GPL C source
- very small, modifiable code
- cell-wise erodibility arrays already inspected

### Iber+ advantages
- newer GPU/CUDA framework
- finite-volume mature hydro-morphodynamics
- multiclass suspended + bedload
- Exner update
- higher-performance engineering architecture

### Iber+ source-access disadvantage
2026-09-21 audit found that the public research-data deposit distributes Iber+ executables, while a 2024 NHESS code-availability statement says source access is limited to collaborators.

Therefore public independent modification cannot currently be treated as equivalent to SWEHR.

### SERGHEI-SE advantages
- public 3-clause BSD source
- modern C++/Kokkos/MPI HPC architecture
- CUDA/OpenMP plus newer HIP/SYCL portability work
- spatial arrays are a first-class architecture for parameters and forcing
- public test infrastructure
- recent soil-erosion and bed-update development

### SERGHEI-SE disadvantage relative to SWEHR
- no published quantitative root/litter erosion-resistance coupling
- no equally close steep-postfire TLS validation
- Hairsine-Rose intact/deposited-layer shielding memory is a closer conceptual fit to the observed postfire loose-layer problem

## current source-audit judgment

```
SWEHR
= best inspected postfire process match
+ easiest verified erosion-resistance hooks

SERGHEI-SE
= best open-source modern HPC architecture
+ legally/technically straightforward to fork and extend

Iber+
= excellent equations/HPC
- public source access blocker
```

Therefore the previous open question about Iber+ public source is now resolved negatively for the general public distribution.

Final engine selection remains pending:
1. final root-resistance mapping
2. final exposed-litter mapping
3. decide whether SWEHR's process match outweighs SERGHEI-SE's modern software architecture


---

## 2026-09-21 quantitative vegetation interface and long-term wrapper

### 1. roots: use J as the baseline quantitative resistance receiver

Direct literature review still did **not** verify a universal:

```
cohesion -> J
```

equation.

Hairsine-Rose literature treats `J` as an experimentally determined specific entrainment energy.

Gyssels et al. (2005), however, gives a published relative erosion response:

```
SEP_root = exp(-b RP)
```

For rill erosion, the review-average coefficients are:
- root density: `b = 0.5930`
- RLD: `b = 0.0460` when RLD is in km m^-3

Because SWEHR original-soil flow entrainment is, all else equal:

```
E3 ∝ 1 / JSMASK
```

the same published relative erosion multiplier can be embedded algebraically as:

```
J_eff
= J_bare / SEP_root
= J_bare * exp(b RP)
```

This is explicitly a **새로운 coupling**, not an existing Hairsine-Rose or Gyssels implementation.

Preferred baseline pathway:

```
LPJ-GUESS FineRootC
 -> PFT-specific RLD
 -> SEP_root
 -> JSMASK
```

Do **not** also apply the same root multiplier to `UC` in the baseline implementation. That would risk double counting unless an independent mechanism and calibration justify it.

### 2. alternative root pathway: RLD -> soil strength -> critical shear

De Baets + Léonard & Richard + Waldmann/PROMET establish a published structural pathway:

```
RLD
 -> erosion-specific cohesion / soil strength
 -> critical shear stress tau_c
```

Waldmann uses the Léonard & Richard lineage:

```
tau_c = beta * sigma_s
```

with `beta = 2.6e-4`, but subsequently requires a model-specific additional scaling. Therefore this is a strong structural precedent but not a transferable Gounsa coefficient.

This pathway is useful for:
- validation
- sensitivity analysis
- a `tau_c`-native alternative erosion closure

It does **not** directly close:

```
tau_c -> SWEHR UC
```

because critical stream power also depends on hydraulic velocity/state.

### 3. exposed surface litter: mass -> cover -> rainfall protection

The previous exposed-litter gap is substantially reduced.

Gregory (1982), WEPP residue documentation and Pannkuk & Robichaud (2003) support:

```
C_lit = 1 - exp(-b_m M_lit)
```

where:
- `M_lit`: exposed dry litter mass per unit area
- `C_lit`: fractional surface cover
- `b_m`: litter-type-specific mass-to-cover coefficient

Pannkuk & Robichaud (2003) is directly relevant to postfire steep forest and gives conifer needle mass-cover calibration plus exponential interrill and rill protection responses.

A defensible new SWEHR coupling is therefore:

```
f_lit,rain = exp(-k_lit C_lit)

ASMASK_eff
= ASMASK_bare * f_lit,rain
```

For their experiment:
- Douglas-fir interrill cover exponent: about `3.2`
- ponderosa pine: about `1.8`

These values are **not universal Gounsa parameters**. They demonstrate a published functional form and calibration scale.

### 4. surface litter, incorporated litter and loose sediment remain separate

```
SurfaceLitter
 -> dry mass
 -> surface cover
 -> rainfall shielding / interception / roughness

IncorporatedLitter
 -> soil structure
 -> Kr / tau_c type effects

DepositedLooseSediment
 -> M[k]
 -> H shielding / armoring
```

These states must not be collapsed into one litter or cover coefficient.

### 5. 100-year use is event driven, with hourly precipitation forcing

The available Gounsa precipitation forcing is hourly.

That is compatible with SWEHR.

The external forcing clock should use hourly precipitation:

```
P_1h(t)
```

For each hour, the observed hourly rainfall depth/intensity is held piecewise constant over that forcing interval.

SWEHR itself must **not** use a 1-hour numerical time step. Its internal hydraulic/sediment time step remains adaptive or sufficiently small to satisfy the Courant stability condition.

Therefore:

```
hourly rainfall data
 -> identify erosive storm events
 -> piecewise-constant hourly rainfall forcing within each event
 -> SWEHR sub-hourly internal integration
```

Between hydrologically separate events:
- surface water depth can reset/drain
- suspended sediment can clear according to the event boundary treatment
- topography persists
- `M[k]` deposited sediment persists
- `H` shielding persists
- particle-size/surface-state memory persists
- LPJ-GUESS updates vegetation/root/litter states on its own ecological time step

Long-term architecture:

```
LPJ-GUESS long-term ecological state
        |
        +-> FineRootC / litter / soil state
        |
hourly rainfall series
        |
        +-> storm-event segmentation
        |
        v
SWEHR event simulation
        |
        +-> updated topography
        +-> M[k]
        +-> H
        +-> surface PSD
        |
        v
persist state to next event
```

The exact dry-gap rule separating storm events must be defined from hydrologic response and tested as a sensitivity parameter rather than chosen arbitrarily.

This event-manager workflow is a **new coupling/workflow**, but it is consistent with:
- SWEHR's event-scale design
- FEaST event-to-event surface memory
- tRIBS long-term hydro-geomorphic precedents

### 6. present engine judgment

```
Primary process engine:
SWEHR / 2D Hairsine-Rose

Modern HPC fallback / possible later port:
SERGHEI-SE

Not primary implementation base under current public-source access:
Iber+

Long-term structural precedent:
tRIBS-FEaST / tRIBS-Erosion
```

SWEHR is preferred because it minimizes **conceptual coupling invention**, not because it is the newest or fastest code.

Before production lock:
1. benchmark SWEHR runtime on the actual Gounsa DEM
2. verify hourly forcing ingestion/event segmentation
3. calibrate `J_bare`, litter mass-cover/protection, and root-RLD conversion
4. compare a subset of events against SERGHEI-SE if feasible
