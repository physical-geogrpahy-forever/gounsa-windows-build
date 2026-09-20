# Postfire live/dead-root persistence and water-erosion interface

## 목적

산불 직후 LPJ-GUESS live fine-root state가 감소할 때 root erosion protection을 즉시 0으로 만들지 않고,
죽은 뿌리의 물리적 잔존효과와 수년 규모의 decay를 별도 상태로 보존하기 위한 구조를 정의한다.

핵심 원칙:

```
LiveRoot != DeadRoot != NoRoot
```

또한:

```
DeadRoot amount != DeadRoot mechanical integrity
```

이다.

---

## 1. 직접 유수침식 근거

### Ghidey & Alberts 1997

Dead roots alone reduced interrill erodibility.

```
K_i = 3.55 exp(-0.71 RTM)
```

- `RTM`: dead root mass [kg m^-2], 0-0.15 m

```
K_i = 3.62 exp(-0.029 RTL)
```

- `RTL`: dead root length [km m^-2], 0-0.15 m

Dead roots:
- increased soil shear strength
- increased aggregate stability
- reduced interrill erodibility
- did not significantly alter splash detachment itself

Therefore dead-root protection is mainly a **soil-resistance/binding** process, not rainfall shielding.

### Wang et al. 2014

Concentrated-flow experiments explicitly separated:
- dead roots
- live roots
- biocrust
- litter/stems

Total roots accounted for a major fraction of the reduction in soil detachment.

This confirms that live/dead root states can be treated independently.

### Wang & Zhang 2017

Root effect on concentrated-flow detachment was separated into:
- physical binding
- biological/chemical bonding

Across 10 grassland species:

```
total root reduction contribution = 53.6%
physical binding                 = 41.4 percentage points
bonding                          = 12.2 percentage points
```

The physical fraction of total root protection was therefore about:

```
41.4 / 53.6 ~= 0.77
```

Architecture-specific values were of similar order:
- tap-root: 33.2 / 41.6 ~= 0.80
- fibrous-root: 49.7 / 65.7 ~= 0.76

These ratios are **not universal coefficients**.
They are useful only as evidence that a newly dead but physically intact root network may retain a large fraction of the purely mechanical component while rapidly losing live-root bonding effects.

---

## 2. published numerical-model precedent: WEPP

WEPP independently adjusts rill erodibility for live and dead root mass:

```
CK_rdr = exp(-2.2 dr)
CK_rlr = exp(-3.5 lr)
```

where:
- `dr`: dead root mass [kg m^-2]
- `lr`: live root mass [kg m^-2]
- accounting zone: upper 0.15 m in the documented formulation

Thus an established numerical erosion model already treats:

```
live root effect > dead root effect > zero
```

on a mass basis.

This is a strong structural precedent for keeping two root pools.

Do not convert the coefficient ratio `2.2/3.5` directly into an RLD coefficient without calibration, because the state variable basis differs.

---

## 3. postfire fine-root state evidence

### Montagnoli et al. 2023

After wildfire in Fagus forest:
- shallow live fine roots declined
- dead root length and necromass increased immediately
- elevated dead-root signal persisted through the first spring
- effects were strongest at 0-10 cm
- later recovery included depth redistribution

Therefore:

```
fire
 -> live-root mortality
 -> dead-root pulse
 -> gradual decay
 -> new-root recovery
```

is directly observed.

### Ramirez et al. 2024, Uljin, Korea

At 1, 4 and 6 months postfire:
- root biomass deteriorated with burn severity
- burned-soil cohesion declined with time
- six-month cohesion intercept was about 1.80-2.30 times lower than unburned soil
- decaying roots later created macropore pathways and altered k_sat

This is the most important Korean postfire analogue in the current archive.

### Lei et al. 2022

Two years postfire:
- root number declined by about 46-58%
- tensile strength of roots <2 mm declined by about 36-47%
- soil-root-system shear strength declined by about 55-82%

Thus root **quantity** and root **mechanical quality** both decay.

### Vergani et al. 2017

Scots pine root reinforcement:
- down by factor ~3.6 after 4 years
- mechanical degradation dominated loss
- old-root protection projected close to zero by around 10 years

This is a slope-stability metric and is not transferable directly to water-erosion `J`.

### Sousa et al. 2026

Western Oregon postfire roots:
- minimum strength around 4 years
- recovery toward prefire condition extends over roughly decadal timescales

Again, use only as temporal/mechanical constraint.

---

## 4. required Gounsa state variables

For each PFT p and erosion-relevant layer i:

```
RLD_live,p,i(t)
RLD_dead,p,i(t)
I_dead,p,i(t)
```

where:
- `RLD_live`: living fine-root length density
- `RLD_dead`: dead-root length density still physically present
- `I_dead`: mechanical-integrity factor of the dead-root network

Define for bookkeeping:

```
RLD_dead,eff
=
RLD_dead * I_dead
```

This is a **state definition**, not yet a published erosion equation.

Why separate `I_dead`?

Because Lei 2022 and Vergani 2017 show that:
```
root abundance
and
root mechanical strength
```
both change after fire.

A constant-effect dead-root biomass pool would miss this.

---

## 5. fire mortality transfer

At a fire event, do not use:

```
LiveRoot -> 0
```

Instead the required conceptual transfer is:

```
LiveRoot
 -> surviving live root
 + newly dead root
 + thermally destroyed/combusted root
```

The fractions depend on:
- burn severity
- soil heating
- depth
- root diameter
- species/PFT

The exact mortality/combustion transfer function is still unresolved.

Montagnoli 2023 and Ramirez 2024 show that the shallowest roots are especially vulnerable.

---

## 6. recovery and decay

Total postfire root erosion resistance contains two opposing trajectories:

```
old-root legacy:
DeadRoot quantity/integrity -> declines

new vegetation:
LiveRoot growth -> recovers
```

Therefore a realistic postfire root-resistance curve can have:

```
initial legacy
 -> delayed minimum
 -> recovery
```

rather than a single monotonic exponential tied only to live biomass.

No universal `I_dead(t)` equation is yet adopted.

Do not insert Vergani's slope-stability decay coefficient directly into surface erosion.

---

## 7. candidate SWEHR coupling

The currently adopted live-root baseline is:

```
SEP_root = exp(-b RLD)
J_eff = J_bare / SEP_root
```

For postfire use, a general two-pool extension would have the form:

```
J_eff
=
J_bare
* exp(
    b_live * RLD_live
  + b_dead * RLD_dead,eff
)
```

This equation is **not yet production-approved**.

It is a transparent placeholder family showing where two states enter.

Unresolved:
- `b_live`
- `b_dead`
- `I_dead(t)`

Do not assign them from slope-stability studies.

### sensitivity information only

Two independent erosion lineages suggest dead roots retain less protection than live roots:
- WEPP rill mass coefficients: dead 2.2 vs live 3.5
- Wang & Zhang physical binding is roughly 0.76-0.80 of total root contribution in their grasslands

These should be used as **sensitivity brackets**, not averaged into a universal coefficient.

---

## 8. rainfall/interrill versus flow/rill separation

Dead-root evidence suggests:

### rainfall impact / splash
Do not use dead roots as a substitute for exposed litter cover.

Ghidey 1997 found no significant root effect on splash detachment.

### soil erodibility / flow resistance
Dead roots can continue to:
- bind aggregates
- raise soil shear strength
- reduce detachment

Therefore root state belongs mainly in the soil-resistance pathway.

This preserves:

```
SurfaceLitter -> rainfall shielding
Roots         -> soil binding / flow entrainment resistance
```

instead of collapsing them.

---

## 9. hydrologic side effect

Postfire root decay can also modify infiltration.

Ramirez 2024 and Lei 2022 show:

```
early postfire:
ash + hydrophobicity -> k_sat down

later:
root decay/macropores -> k_sat up
```

This effect must not be hidden inside `J`.

If included, it belongs in a separate hydrologic-state coupling.

---

## 10. current judgment

Resolved:
- dead roots retain nonzero erosion resistance
- live and dead roots must be separate states
- postfire root quantity and mechanical integrity both evolve
- immediate zero-root-resistance after fire is rejected

Not resolved:
- dead-root mechanical-integrity decay equation for Gounsa
- direct `b_dead` for SWEHR
- fire severity/depth -> fine-root mortality transfer
- coupling of root-decay macropores to infiltration

### implementation priority

1. export live `FineRootC` / RLD from LPJ-GUESS
2. create explicit dead-root pool after mortality/fire
3. preserve age or integrity information
4. calibrate live/dead erosion effect separately
5. only then hard-lock the postfire `JSMASK` equation

## 핵심 근거

- Ghidey & Alberts 1997
- Wang et al. 2014
- Wang & Zhang 2017
- WEPP Chapter 7
- Montagnoli et al. 2023
- Ramirez et al. 2024
- Lei et al. 2022
- Vergani et al. 2017
- Sousa et al. 2026
