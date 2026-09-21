# Gounsa current production handoff

날짜: 2026-09-21 09:42 KST
브랜치: `gounsa-water-erosion-deep-review-2026-09-21`

## authoritative scope

현재 고운사 100년 production baseline은 다음 과정만 포함한다.

```
water erosion
+ residual background creep
+ root-growth/decay transport
+ postfire dry ravel
+ shallow-sandstone soil production
+ chemical dissolved weathering
+ fire spall / coarse-fragment supply
```

현재 제외:

```
tree throw / uprooting
shallow landslide
```

관련 tree-throw decision/model files는 archive-only로 보존한다.

---

## water erosion

Baseline:
`SWEHR / McGuire 2016`

External precipitation:
- 1-hour forcing

Internal SWEHR integration:
- sub-hourly
- CFL-constrained

LPJ-GUESS:
- native root state
- litter state
- vegetation recovery

feeds the published SWEHR state through documented new couplings.

---

## hillslope transport

Current production equation:

```
q_hill
=
q_bg
+
q_root
+
q_dryravel
```

### residual creep

Final baseline:

```
q_bg
=
-K_bg H_* [1-exp(-H/H_*)] grad(z)
```

Source:
- Johnstone & Hilley 2015
- Landlab `DepthDependentDiffuser`
- Furbish 2009 for depth-limited local-creep interpretation

Shallow-soil limit:

```
H << H_*
```

```
q_bg
approx
-K_bg H grad(z)
```

Thus the formerly used:
```
-D*_bg H grad(z)
```
is only the shallow approximation, not the full production equation.

### root transport

Gabet et al. 2003:

```
q_root
=
x r tau / rho_r
```

Use LPJ-GUESS native:
- root state
- turnover
- root vertical distribution

Do not modify `K_bg` again with vegetation.

### dry ravel

Separate postfire process:
- Lamb lineage
- Roering & Gerber
- Jackson & Roering

No universal fire multiplier on residual creep.

---

## shallow-sandstone soil production

Project condition:

```
sandstone + shallow mobile soil
```

Therefore two mandatory production modes remain.

### Mode A: exponential

```
P_A(H)
=
P0 exp(-H/gamma)
```

Main analogue source:
- Evans et al. 2021 sandstone sites

### Mode B: shallow finite-depth peak / zero-depth suppression

Requirement:
- very thin/exposed sandstone may produce less than the finite-depth peak
- potential high-production zone around roughly 0.15-0.30 m in the Oregon sandstone lineage

Do **not** invent the final hump equation or coefficients before local/regional evidence.

---

## 100-year analogue magnitude

Using Evans et al. 2021 site-specific `P0,gamma` pairs and:
```
H = 0.05-0.30 m
```

Mode A sensitivity gives approximately:

- Comer: 7.2-7.6 mm / 100 yr
- Hilton: 15.7-17.2 mm / 100 yr
- Rufford: 6.2-6.9 mm / 100 yr
- Woburn: 18.8-25.7 mm / 100 yr

These are analogue sensitivity values, not Gounsa predictions.

Oregon thin-soil sandstone evidence suggests a broader sensitivity envelope of roughly:
```
15-35 mm / 100 yr
```
in some shallow regimes.

Therefore soil production is not dropped simply because the simulation is 100 years.

---

## chemical weathering

Keep separate:

```
P_sand
!=
W_chem
```

Use:
- `P_sand(H)`: slow parent-material to mobile-soil production
- LPJ-GUESS/Hartmann: daily climate/hydrology-sensitive dissolved chemical-weathering forcing

Do not add:
- arbitrary biomass multiplier
- arbitrary annual climate multiplier
- arbitrary fire multiplier

to `P_sand`.

---

## mobile-soil mass balance

```
M_AB
=
rho_AB H_AB
```

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

All modules must obey:

```
total exported mobile soil
<=
available mobile soil
```

No negative soil depth.

---

## numerical framework

Preferred scaffold:
`Landlab`

Current structure:

```
LPJ-GUESS
│
├─ root state + turnover
│    └─ Gabet root-growth/decay flux
│
├─ runoff + soil T
│    └─ Hartmann chemical dissolved weathering
│
└─ vegetation recovery

Landlab grid
│
├─ soil__depth
├─ bedrock__elevation
├─ topographic__elevation
│
├─ custom sandstone production
│    ├─ Mode A exponential
│    └─ Mode B shallow-hump sensitivity
│
├─ DepthDependentDiffuser
│    └─ q_bg
│
├─ Gabet root flux
│
└─ dry-ravel coupling

SWEHR
└─ event-scale water erosion
```

Optional sensitivity only:
`DepthDependentTaylorDiffuser`

Reason:
nonlinear near-critical transport may overlap with dry-ravel/nonlocal steep-slope motion.

---

## Pelletier status

```
Pelletier 2013
= long-term consistency/comparison only
!= production engine
```

Reason:
- geologic-time constitutive calibration
- small internal dt is numerical stability, not annual ecological calibration
- process attribution is less transparent than the current modular design

---

## tree throw / uprooting status

All of the following are archive-only:
- `decisions/2026-09-21_TREE_THROW_COUPLING.md`
- `models/LPJ_GUESS_TreeThrow.md`
- `models/ForestGALES_fgr.md`
- `models/TreeThrow_Annual.md`
- `models/Doane_TreeThrow_Roughness.md`

They must not drive current production implementation.

---

## shallow landslide status

Archive only.

No current:
- factor-of-safety module
- landslide root cohesion
- failure probability
- landslide routing

---

## authoritative decisions

- `decisions/2026-09-21_GEOMORPH_SCOPE_CORRECTION.md`
- `decisions/2026-09-21_BACKGROUND_CREEP.md`
- `decisions/2026-09-21_SANDSTONE_WEATHERING_BASELINE.md`
- `decisions/2026-09-21_SHALLOW_SANDSTONE_PRODUCTION.md`
- `decisions/2026-09-21_WEATHERING_CREEP_IMPLEMENTATION_FRAMEWORK.md`
- `decisions/2026-09-21_WATER_EROSION_ENGINE_REASSESSMENT.md`

## authoritative models

- `models/Landlab_ShallowSoil_Weathering_Creep.md`
- `models/Sandstone_Soil_Production.md`
- `models/Residual_Background_Creep.md`
- `models/Short_Timestep_Weathering_HillslopeTransport.md`
- `models/Hairsine_Rose_2D_Postfire.md`

## next priority

Do not return to tree throw/uprooting or shallow landslide.

Next research/implementation priorities:
1. exact Gounsa sandstone petrography / formation
2. defensible `P0`, `gamma` sensitivity set
3. Mode B shallow-soil production constraints
4. fire-spall production on sandstone
5. coarse-fragment supply versus armour
6. implementation integration in Landlab + SWEHR + LPJ-GUESS
