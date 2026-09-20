# DynSoil / GM09 / MErSiM transient regolith lineage

## 핵심 문헌
- Gabet & Mudd 2009, Geology, DOI 10.1130/G25270A.1
- Park et al. 2020 / GEOCLIM steady-state application
- Maffre et al. DynSoil transient implementation lineage
- Maffre et al. 2025 GEOCLIM7
- Zhao et al. 2026 MErSiM v1.0, DOI 10.5194/gmd-19-6857-2026

## 고운사에서 검토한 이유
100년 model에서:
- fresh bedrock to regolith production
- regolith thickness
- primary-mineral depletion
- chemical weathering
- physical erosion

을 하나의 mass-consistent transient state system으로 처리할 수 있는지 확인하기 위해 관리한다.

## 핵심 states

```
h_reg(t)
x(z,t)
tau(z,t)
```

where:
- `h_reg`: regolith thickness
- `x`: weatherable primary-mineral fraction
- `tau`: exposure/residence time

## governing equations

```
dh_reg/dt
=
P_r
-
E_phys
```

```
partial x/partial t
=
-P_r partial x/partial z
-
K tau^sigma x
```

```
partial tau/partial t
=
-P_r partial tau/partial z
+
1
```

```
W_chem
=
integral K tau^sigma x dz
```

## production law

```
P_r
=
P_0 f(h_reg)
```

with:
```
P_0
=
k_rp q
exp[
(E_a/R)(1/T_0 - 1/T)
]
```

and a thickness-dependent soil/regolith production function.

## critical distinction

```
regolith-thickness evolution
!=
mobile-soil thickness evolution
```

DynSoil/MErSiM:
```
dh_reg/dt = P_r - E_phys
```

Chemical dissolution changes mineral abundance and weathering flux within the regolith.

For the Gounsa mobile A/B layer, Yoo/Brosens-style mass balance should separately include chemical mass loss.

## preferred Gounsa two-layer bookkeeping

### C/Cr or total regolith
```
h_reg
x(z)
tau(z)
```
from the transient regolith lineage.

### mobile A/B soil
```
M_AB = rho_AB H_AB
```

```
dM_AB/dt
=
parent_to_soil_mass
+ physical_deposition
- physical_erosion
- chemical_mass_loss_AB
```

This avoids forcing one state variable to represent both:
- bedrock weathering-front advance
- mobile-soil mass loss

## LPJ-GUESS interface
Potential climate inputs:
- runoff or recharge-related water flux
- soil/regolith temperature

But the exact relation depends on the chosen production formulation.

Do not substitute surface runoff directly for subsurface recharge without checking the selected equation.

## physical erosion interface
Do **not** use MErSiM's global RF erosion model in Gounsa.

Provide `E_phys` from:
- SWEHR event erosion
- background hillslope transport
- tree throw/dry ravel if they export material from the regolith cell
- shallow landslide when applicable

Avoid double counting lateral redistribution that remains within the local regolith system.

## relation to Braun 2016
Braun provides a more explicitly groundwater-driven weathering-front model.

DynSoil/MErSiM provides a more convenient transient state system with climate/erosion/mineral residence-time coupling.

Current comparison:
- Braun: stronger subsurface-hydrology process basis
- DynSoil/MErSiM: easier transient regolith bookkeeping

## current judgment
**Optional advanced transient regolith/mineral-state architecture.**

Before hard-lock:
1. quantify expected 100-year magnitude
2. define local lithology parameters
3. determine whether LPJ-GUESS runoff or a recharge/subsurface-water variable should drive `P_0`
4. ensure no double counting with Gabet-Mudd woody mechanical production


---

## 2026-09-21 exact production-law audit

MErSiM/GM09 transient framework gives:

```
dh_reg/dt = P_r - E
```

with:

```
P_r = P_0 f(h)
```

```
f(h) = exp(-h/d_0)
```

and climate-responsive optimal production:

```
P_0
=
k_rp q
exp[
(E_a/R)
(1/T_0 - 1/T)
]
```

where:
- `q`: runoff/water-flux forcing in the published formulation
- `T`: temperature
- `d_0`: characteristic regolith-thickness scale
- `k_rp`: proportionality parameter

Chemical dissolution rate constant is separately:

```
K
=
k_d
(1-exp(-k_w q))
exp[
(E_a/R)
(1/T_0 - 1/T)
]
```

Thus the model already separates:
- regolith-front production `P_r`
- chemical dissolution `K` / `W`
- physical erosion `E`

### important application caveat
The 2026 paper explicitly notes that current MErSiM applications primarily use a steady-state regolith-thickness assumption for efficient global/deep-time weathering calculations.

Therefore the full `x(z,t)` and `tau(z,t)` transient profile is **not automatically the best 100-year Gounsa production baseline**.

### simplified Gounsa option
Because East Asian granite production/erosion constraints suggest century-scale front motion is often sub-mm to several-mm, a first implementation may use only:

```
P_r(t)
=
P_0(t)
exp[-h_reg(t)/d_0]
```

on an annual geomorphic step.

LPJ-GUESS supplies the climate/hydrologic forcing used to compute or scale `P_0(t)`.

The full transient mineral-age equations are then reserved for sensitivity/advanced validation if weathering proves dynamically important.

This retains a published process equation while avoiding unnecessary state complexity.


---

## 2026-09-21 sandstone scope correction

고운사 parent material은 sandstone으로 취급한다.

Sandstone-specific soil-production measurements now provide a more direct first-order production law:

```
P_sand(h)
=
P0_sand exp(-h/gamma_sand)
```

with analogue sandstone bounds from Evans et al. 2021 approximately:

```
P0_sand = 0.071-0.274 mm yr^-1
gamma_sand = 0.80-4.50 m
```

Therefore this model lineage is **demoted from preferred production baseline to optional advanced module**.

Current role:
- transient primary-mineral depletion
- mineral exposure/residence age
- deeper regolith chemistry
- sensitivity analysis

Do not use its global/deep-time `k_rp`, `d_0` parameters instead of sandstone-specific local calibration unless a specific reason is demonstrated.

The earlier granite-based justification for simplifying MErSiM is also withdrawn. The simplification is now justified by **availability of more directly relevant sandstone soil-production functions**, not by assuming sandstone production is negligible.
