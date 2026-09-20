# 결정: 고운사 sandstone soil production, chemical weathering, soil-thickness mass balance

날짜: 2026-09-21

## 핵심 전제
고운사 parent material은 현재 프로젝트 기준 **sandstone**으로 취급한다.

다음은 분리한다.

```
sandstone -> mobile soil production
!=
chemical dissolved mass loss
```

또한 current production baseline에서는:
```
tree throw / uprooting = excluded
shallow landslide      = excluded
```

---

## 1. A/B mobile soil mass balance

```
M_AB = rho_AB H_AB
```

Yoo 2007 / Brosens 2020 계열:

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
- `Phi_AB`: sandstone/saprolite에서 mobile soil로 공급되는 질량
- `D_phys`: physical deposition
- `E_phys`: SWEHR + hillslope transport에 의한 physical export
- `W_AB`: dissolved chemical mass loss

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

---

## 2. sandstone soil-production baseline

Production rate:

```
P_sand(h)
=
P0_sand exp(-h/gamma_sand)
```

where:
- `P_sand`: bedrock/saprolite -> mobile-soil production [m yr^-1]
- `P0_sand`: zero-soil-thickness production rate
- `h`: mobile-soil thickness
- `gamma_sand`: e-folding depth

Mass supply:

```
Phi_AB
=
rho_parent * P_sand
```

with density/porosity conversion treated explicitly.

### supporting sandstone data

Evans et al. 2019:
```
0.026-0.096 mm yr^-1
```
across two temperate sandstone sites.

Coniferous Comer Wood mean:
```
0.070 +/- 0.010 mm yr^-1
```

Evans et al. 2021 sandstone sites:

```
P0_sand
=
0.071-0.274 mm yr^-1
```

```
gamma_sand
=
0.80-4.50 m
```

The wide range is caused by sandstone matrix/cementation differences.

Heimsath et al. 2001 provides the forested Oregon sandstone soil-production-function lineage.

---

## 3. sandstone petrography is required

Do not assign one production coefficient to all sandstone.

Important controls:
- matrix abundance
- cement type
- quartz/feldspar overgrowth
- iron oxides
- permeability
- tensile strength
- fracture density
- degree of weathering

Marshall et al. 2014 and Evans et al. 2021 show that these properties can change soil-production susceptibility strongly.

Uiseong regional studies report lithic arkose and feldspathic wacke among common Cretaceous sandstones.

This is regional context only.

Exact Gounsa sandstone classification must be confirmed before final parameter selection.

---

## 4. chemical dissolved mass loss

Hartmann 2011/2014 + LPJ-GUESS-CNP remain the chemical-weathering forcing.

Keep separate:

```
F_bulk_chem
```

and:

```
F_P_release
```

Conceptually:

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

Do not infer geomorphic mass loss from the P pool if the parent bulk-weathering term can be evaluated directly.

---

## 5. postfire behavior

No arbitrary:

```
fire -> P_sand multiplier
```

is adopted.

Soil thinning already creates a published feedback:

```
fire / erosion
 -> H_AB down
 -> P_sand(H_AB) up
```

If sandstone is locally exposed, the production function naturally approaches `P0_sand`.

Fire spall remains a separate physical-fragment source.

---

## 6. root effect

Pawlik et al. 2023 shows living roots can:
- penetrate sandstone fractures
- wedge fragments
- contribute to soil formation

But no universal quantitative:
```
root biomass -> P_sand
```
law is available.

Therefore no LPJ-GUESS biomass multiplier is added to `P_sand` in the baseline.

---

## 7. DynSoil / MErSiM

Current role:
**optional advanced module, not production baseline.**

Use only if later required to track:
- primary-mineral fraction `x(z,t)`
- mineral exposure time `tau(z,t)`
- deeper transient regolith chemistry

The simple sandstone soil-production function is more directly constrained by relevant lithology.

---

## 8. Braun 2016

Retained as a groundwater-driven weathering-front alternative.

Not baseline because it requires:
- recharge/groundwater state
- fractured-bedrock permeability
- additional rock/mineral parameters

---

## 9. granite literature correction

Granite papers reviewed previously remain comparison-only.

They must not be used to infer the Gounsa production magnitude.

The earlier granite-based statement that production may be only sub-mm to a few mm per 100 yr is withdrawn.

Sandstone observations support a plausible production magnitude of:
```
several mm to roughly 1-3 cm per 100 yr
```
depending on soil thickness, matrix and cementation.

This is a sensitivity envelope, not a final Gounsa rate.

---

## 10. current annual bookkeeping

```
P_sand(t)
=
P0_sand exp[-H_AB(t)/gamma_sand]
```

```
Phi_AB(t)
=
rho_parent P_sand(t)
```

```
M_AB(t+1)
=
M_AB(t)
+
Phi_AB
+
D_phys
-
E_phys
-
W_AB
```

with consistent units and density conversion.

---

## unresolved

1. exact Gounsa sandstone formation/petrography
2. local `P0_sand`
3. local `gamma_sand`
4. parent and soil bulk densities / porosity
5. chemical-loss partition between A/B and deeper weathered material
6. fire-spall production
7. whether a root-dependent production modifier is necessary after validation

## 최종 판정
**Sandstone-specific annual soil-production function is the production baseline.**

DynSoil/MErSiM and Braun remain advanced alternatives.
