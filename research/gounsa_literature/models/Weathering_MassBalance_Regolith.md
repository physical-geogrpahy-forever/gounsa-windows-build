# Gounsa weathering mass-balance and regolith bookkeeping

## 목적
고운사에서 풍화를 하나의 단일 `weathering rate`로 처리하지 않고 다음을 분리한다:

1. sandstone parent-material to mobile-soil production
2. chemical dissolution within existing soil/regolith
3. mobile A/B soil production/loss
4. deeper regolith/front state when needed
5. physical erosion/deposition

---

# 1. state separation

Recommended states:

```
Z_surf
H_AB
H_CCr_or_reg
M_AB
x_primary(z)
tau_weathering(z)
```

where:
- `Z_surf`: surface elevation
- `H_AB`: mobile A/B soil thickness
- `H_CCr_or_reg`: underlying regolith/saprolite thickness
- `M_AB = rho_AB H_AB`
- `x_primary`: weatherable primary-mineral fraction
- `tau_weathering`: mineral exposure time

---

# 2. chemical mass-loss forcing

The LPJ-GUESS-CNP lineage derives from Hartmann-Moosdorf.

Important correction:

The parent Hartmann 2011/2014 framework first estimates **bulk chemical weathering**, then derives P release from lithology-specific P content.

Therefore Gounsa should calculate separately:

```
F_bulk_chem
```

and:

```
F_P_release
```

Do not infer geomorphic mass loss solely from the LPJ-GUESS P pool if the parent bulk-weathering term can be evaluated directly.

A generic implementation is:

```
F_bulk_chem
=
f_bulk(lithology, runoff)
* F_T(T)
* F_shield
```

and then:

```
F_P_release
=
F_bulk_chem
* p_rel,lithology
```

with exact units and lithology coefficients taken from the Hartmann model tables.

---

# 3. mobile A/B soil mass balance

Yoo 2007 and Be2D/Brosens 2020 provide the core structure.

```
M_AB
=
rho_AB H_AB
```

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

where:
- `Phi_AB`: mass supplied into mobile A/B soil
- `D_phys`: physical deposition
- `E_phys`: physical erosion/export
- `W_AB`: net chemical mass loss

Equivalent thickness update for approximately constant bulk density:

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

This is the correct location for:
- SWEHR physical erosion/deposition
- chemical mass loss from mobile soil
- conversion/supply from underlying C/Cr

---

# 4. regolith/weathering-front state

Do not update full regolith thickness with:

```
F_bulk_chem / rho
```

alone.

That would confuse dissolved mass loss with bedrock-to-regolith conversion.

Use a separate front-production state:

```
dh_reg/dt
=
P_front
-
E_boundary
```

or the transient DynSoil/MErSiM system:

```
dh_reg/dt
=
P_r
-
E_phys
```

with mineral depletion:
```
partial x/partial t
=
-P_r partial x/partial z
-
K tau^sigma x
```

and:
```
W_chem
=
integral K tau^sigma x dz
```

---

# 5. candidate weathering-front production models

## sandstone-specific empirical production baseline

Current production baseline:

```
P_sand(h)
=
P0_sand exp(-h/gamma_sand)
```

Sandstone evidence:
- Heimsath et al. 2001
- Evans et al. 2019
- Evans et al. 2021

Evans 2021 reports sandstone-specific zero-thickness production and e-folding depths spanning roughly:

```
P0_sand = 0.071-0.274 mm yr^-1
gamma_sand = 0.80-4.50 m
```

These are sensitivity/analogue bounds, not direct Gounsa coefficients.

## DynSoil / MErSiM
Retained as optional advanced deeper-regolith/mineral-state module, not the initial production baseline.

## Braun 2016
Weathering-front advance is tied to:
- subsurface pore-fluid velocity
- groundwater gradient
- fractured-bedrock permeability
- mineral solubility and abundance

Advantages:
- stronger hydrologic mechanism

Limit:
- more subsurface parameters
- needs recharge/groundwater state

## woody uprooting/rootwad production
Current production baseline excludes tree throw/uprooting.

Gabet & Mudd 2010 remains archive/reference only.

---

# 6. double-counting rule

This is critical.

Possible sources of new material:
- sandstone soil production at the soil-parent interface
- deeper chemical/front weathering where explicitly represented
- frost/thermal physical weathering if supported
- fire spall

If a published empirical `P_r` already represents total natural regolith production, adding all explicit physical terms would double count.

Therefore production must be defined either as:

### option A: residual decomposition
```
P_total
=
P_chem_residual
+
P_woody
+
P_other
```

with `P_chem_residual` calibrated after explicit physical processes are removed.

### option B: one integrated production model
use a total empirical `P_r` and do not separately add physical production.

For Gounsa's research question, **option A is preferred** because vegetation feedbacks need explicit process attribution.

---

# 7. present preferred architecture

```
LPJ-GUESS
 runoff / Tsoil
      |
      +--> Hartmann bulk chemical-loss forcing
      |       -> W_AB / W_reg
      |
annual sandstone production
      +--> P_sand(h)

SWEHR / hillslope modules
      -> E_phys / D_phys

Mass balance
      -> H_AB
      -> H_CCr_or_reg
      -> surface elevation
```

---

# 8. current judgment

The previous unresolved statement:
```
chemical-weathering flux
 -> regolith thickness
```
was too compressed.

It is now resolved conceptually into two different conversions:

```
chemical dissolved mass loss
 -> mobile-soil/regolith mass loss
```

and:

```
weathering-front advance
 -> new regolith production
```

The first is closed by Yoo/Brosens-style mass balance.

For the current sandstone baseline, the second is represented first by a sandstone-specific empirical soil-production function. DynSoil/MErSiM and Braun 2016 are advanced alternatives if a deeper regolith-front state is later required.

## next quantitative task
Calibrate:
- `P0_sand`
- `gamma_sand`
- `W_chem`

and compare them with event erosion and dry-ravel magnitudes over 100 years.


---

## 2026-09-21 sandstone correction

고운사 parent material은 sandstone으로 취급한다.

따라서 granite-based century-scale magnitude reasoning is withdrawn for local parameterization.

Current production interface:

```
P_sand(h)
=
P0_sand exp(-h/gamma_sand)
```

Sandstone observations show several-fold variation in `P0` and `gamma` caused by:
- matrix content
- cementation
- permeability
- tensile strength
- fracture density

Thus exact Gounsa sandstone petrography is now a parameterization prerequisite.

Chemical dissolved loss remains separate:

```
W_chem
```

and the mobile-soil mass balance remains:

```
dM_AB/dt
=
rho_parent P_sand
+
D_phys
-
E_phys
-
W_AB
```

with consistent density conversion.

DynSoil/MErSiM is demoted to optional advanced mineral/regolith-state sensitivity.
