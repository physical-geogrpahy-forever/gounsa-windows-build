# Landlab implementation path for shallow sandstone weathering and creep

## 목적
고운사 100년 model에서 Pelletier 장기모델 대신:
- shallow sandstone soil production
- mobile-soil mass balance
- depth-limited residual creep

를 짧은 numerical timestep으로 안정적으로 구현할 framework를 정리한다.

## recommended components

### 1. soil/regolith state
Landlab grid fields:
```
topographic__elevation
bedrock__elevation
soil__depth
```

These provide the minimum explicit state required for a shallow-soil model.

### 2. production
Landlab default:
```
ExponentialWeatherer
```

```
P
=
P0 exp(-H/Hd)
```

For Gounsa:
- use this as sandstone mode A
- implement custom mode B for shallow finite-depth production peak / zero-depth suppression

Do not hard-lock the default exponential weatherer.

### 3. residual creep

Preferred Landlab component:
```
DepthDependentDiffuser
```

Flux:

```
q_bg
=
-K H_* (1-exp(-H/H_*)) grad(z)
```

For:
```
H << H_*
```

this becomes:

```
q_bg
approx
-K H grad(z)
```

which matches the Furbish-style shallow-soil residual form already selected.

This is particularly suitable because Gounsa mobile soil is shallow.

### 4. steep-slope optional component
If linear slope dependence is inadequate:

```
DepthDependentTaylorDiffuser
```

adds nonlinear slope dependence with a critical slope and supports dynamic internal timestepping.

Do not enable it by default because:
- Gounsa already separates dry ravel
- nonlinear near-critical flux can double count nonlocal steep-slope processes

Use only as sensitivity.

## numerical timestep
The outer geomorphic state can still be updated annually.

Landlab diffusion components may internally require shorter stable substeps.

Recommended:

```
annual forcing/state
 -> internally stable diffusion substeps
 -> annual conserved output
```

This is directly analogous to:
```
hourly rain
 -> sub-hourly SWEHR integration
```

## coupling with LPJ-GUESS

### root-growth transport
Do not encode LPJ-GUESS vegetation by changing residual diffusivity.

Instead:

```
LPJ-GUESS root state/turnover
 -> Gabet q_rootgrowth
 -> add explicit link/node flux
```

### chemical weathering
Use LPJ-GUESS/Hartmann as a separate chemical dissolved-loss forcing in the mobile-soil mass balance.

### production
Sandstone `P(h)` remains a parent-material production law, not a direct biomass multiplier.

## current total hillslope transport

```
q_hill
=
q_bg,Landlab
+
q_rootgrowth,Gabet
+
q_dryravel
```

Tree throw/uprooting and shallow landslide are outside current scope.

## mass conservation
Every process must update the same mobile-soil state.

Required constraint:

```
total exported mobile soil
<=
available mobile soil
```

No component may create negative soil depth.

## why this is preferable to Pelletier
Pelletier 2013:
- geologic-time calibration
- bundled eco-pedo-geomorphic feedback
- harder to isolate current processes

Landlab:
- modular
- depth-dependent mobile soil state
- arbitrary numerical timestep
- published current implementation
- easy separation of process equations
- easier coupling to SWEHR/LPJ-GUESS states

## final judgment
**Preferred numerical scaffold: Landlab DepthDependentDiffuser + custom shallow-sandstone weatherer.**

Pelletier remains long-term comparison only.
