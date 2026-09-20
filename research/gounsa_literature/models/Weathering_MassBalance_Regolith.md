# Gounsa weathering mass-balance and regolith bookkeeping

## 목적
고운사에서 풍화를 하나의 단일 `weathering rate`로 처리하지 않고 다음을 분리한다:

1. bedrock/regolith interface advance
2. chemical dissolution within existing regolith
3. mobile A/B soil production/loss
4. woody mechanical bedrock production
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

## DynSoil / MErSiM
```
P_r
=
P_0 f(h)
```

```
P_0
=
k_rp q
exp[
(E_a/R)(1/T_0 - 1/T)
]
```

Advantages:
- transient
- explicit regolith state
- mineral residence-time and supply limitation
- easy annual bookkeeping

Limit:
- global/geologic calibration

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

## Gabet & Mudd 2010 woody mechanical
Separate from chemical front advance:

```
P_woody_mech
```

from root fracture/tree throw.

Do not add it blindly to a chemical `P_r` if the selected `P_r` was calibrated to total natural regolith production that already includes biological mechanical effects.

---

# 6. double-counting rule

This is critical.

Possible sources of new regolith:
- chemical front advance
- root fracture
- tree throw bedrock detachment
- frost/thermal physical weathering
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
 runoff / Tsoil / vegetation
      |
      +--> Hartmann bulk chemical-loss forcing
      |       -> W_AB / W_reg
      |
      +--> chemical front model
      |       -> P_chem_front
      |
      +--> woody cohorts/root state
              -> Gabet-Mudd P_woody_mech

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

The second requires selecting/calibrating a front-production model, with DynSoil/MErSiM and Braun 2016 as the strongest current candidates.

## next quantitative task
Estimate the order of magnitude of:
- `P_chem_front`
- `W_chem`
- `P_woody_mech`

for Gounsa over 100 years before choosing the more complex front model.
