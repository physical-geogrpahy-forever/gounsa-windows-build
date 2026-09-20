# Short-timescale weathering and hillslope-transport architecture for Gounsa

## 목적
고운사 산불 후 약 100년 simulation에서 Pelletier 2013을 soil production/weathering 및 hillslope diffusion의 주식으로 사용할지, 더 짧은 시간간격의 published process models로 대체할지를 통합 판단한다.

---

# 1. 핵심 결론

**Pelletier 2013을 100년 주식으로 사용하지 않는다.**

대신 과정별로 분리한다:

```
WEATHERING / SOIL PRODUCTION

chemical-weathering forcing
 = LPJ-GUESS-CNP 2025 [daily; not direct regolith production]

woody mechanical weathering
 = Gabet & Mudd 2010 [annual]

optional profile/physical-weathering benchmark
 = SSSPAM [annual/short-event capable]
 = SoilGen [daily hydrology, profile chemistry]


HILLSLOPE TRANSPORT

background continuous creep
 = residual diffusion term [annual outer step]

root growth/decay bioturbation
 = Gabet et al. 2003 [annual turnover]

tree throw
 = Doane 2021 [annual stochastic events]
   + CSDMS TreeThrow precedent

postfire dry ravel
 = Lamb 2011 [disturbance/event pathway]

shallow landslide
 = separate stability/mass-wasting module
```

---

# 2. 왜 Pelletier 2013이 주식이 아닌가

Pelletier 2013:
- explicitly targets geologic-time-scale eco-pedo-geomorphic coevolution
- separate runs prescribe EEMT states
- reported topography/soil states after 10 Myr
- small solver timestep is used only for numerical stability

Critical distinction:

```
small numerical timestep
!=
short ecological/process calibration timescale
```

Therefore:
```
annual LPJ-GUESS biomass(t)
 -> Pelletier Kd(t)
```
is not supported as an existing annual process law.

Keep Pelletier only for:
- long-term sign of feedback
- broad steady-state benchmark
- long-term eco-pedo-geomorphic consistency

---

# 3. chemical weathering: preferred core

## LPJ-GUESS-CNP 2025

Daily, patch-level weathering:

```
F_PW
=
F_CW,i
* F_T
* F_s,i
```

with:
```
F_CW,i
=
(b_carbonate + b_silicate)_i
* p_i
* q
```

and daily prognostic:
- soil temperature
- runoff

Vegetation affects runoff in LPJ-GUESS, so a vegetation-weathering feedback already exists.

### role
**Primary hydroclimatic chemical-weathering driver.**

### unresolved geomorphic conversion
The output is nutrient/mineral weathering flux, not direct soil/regolith thickness.

Need:
```
weathering mass/mineral flux
 -> solid-volume / density mass balance
 -> Delta H_chem
```

This is a new coupling and must be calibrated/validated.

---

# 4. chemical-weathering validation options

## REWTCrunch 2022
- vertically resolved Critical Zone reactive transport
- root biomass/exudation
- daily/short process forcing
- mineral dissolution

Role:
- deep-root chemical-weathering validation
- optional advanced module

Not first implementation because coupling/parameter burden is much larger.

## SoilGen 2022
- 1D soil profile
- daily precipitation/hydrology
- mineral weathering and solute transport
- no lateral flux

Role:
- independent profile-weathering benchmark
- not main spatial geomorphic engine

---

# 5. woody mechanical weathering: preferred core

## Gabet & Mudd 2010

**Annual timestep.**

Processes:
```
tree establishment/growth
 -> root fracture of bedrock
 -> mortality
 -> tree throw
 -> physical bedrock erosion / soil mantling
```

For Gounsa the simple original vegetation model is replaced by LPJ-GUESS cohort outputs.

Recommended interface:

```
LPJ-GUESS woody cohorts
 DBH
 density
 mortality
 root state
       |
       v
root-fracture / rootwad geometry
       |
       v
physical bedrock erosion
       |
       v
Delta H_mech
```

Do not copy Oregon weak-sandstone rates.

---

# 6. background hillslope transport

There are two defensible forms.

## A. conservative baseline: residual linear creep

Gabet & Mudd uses:

```
q_bg = -D_bg S
```

Advantages:
- easy annual integration
- does not artificially explode near critical slope
- cleaner when tree throw, root growth, dry ravel and landslides are explicitly represented

Disadvantage:
- may underestimate steep-slope continuous transport

## B. sensitivity/alternative: Roering nonlinear background

```
q_bg
=
-K_bg grad(z)
/
[1-(|grad(z)|/S_c)^2]
```

Advantages:
- better-known steep-slope nonlinearity

Critical caveat:
field-calibrated `K` can aggregate biological and other disturbance processes.

If Gounsa separately calculates:
- root growth
- tree throw
- dry ravel
- landslides

then using a natural-forest total `K` can double count them.

Also the strong increase near `S_c` can overlap with the explicit shallow-landslide module.

### current baseline judgment
Use **residual linear creep as first implementation**.

Use Roering nonlinear transport as:
- sensitivity test
- possible later replacement if field/topographic calibration shows linear residual is inadequate

If Roering is adopted, recalibrate `K_bg` as a residual coefficient after separately represented processes are removed.

---

# 7. root-growth / root-decay bioturbation

## Gabet et al. 2003

Annual root turnover gives a quantitative biogenic sediment-transport term.

Core lineage:

```
q_rootgrowth
~ x r tau / rho_r
```

where:
- `r`: root mass/area
- `tau`: annual root turnover
- `rho_r`: root tissue density
- `x`: geometry/displacement term

For Gounsa:
use LPJ-GUESS native root state and turnover rather than externally parameterized biomass trajectories.

Role:
**primary root-growth/decay hillslope-transport term.**

---

# 8. tree throw

## Doane 2021
**1-year timestep.**

Annual number of new pit-mound events is sampled stochastically.

Use:
```
LPJ-GUESS woody cohort mortality/disturbance
 -> tree-throw event probability
 -> displaced volume
 -> travel distance
 -> q_treethrow
```

## CSDMS TreeThrow
Independent annual event-model precedent:
- annual timestep
- individual tree growth/death/regeneration
- DBH controls soil-plate geometry and travel distance

The CSDMS source code is currently categorized as unavailable, so use conceptually rather than as a code base.

---

# 9. SSSPAM comparison

SSSPAM is important because it proves:
```
100-year coupled soilscape-landform evolution
```
is feasible.

It includes:
- physical weathering
- diffusion
- armouring
- erosion/deposition
- soil-profile grading

But:
- no dynamic forest/root model
- physical rather than chemical weathering
- overlaps heavily with SWEHR state and erosion
- later short 100-year applications can omit weathering because profile weathering is slow

Role:
**comparison and possible armour/coarse-fragment module source**, not main Gounsa framework.

---

# 10. HydroLorica comparison

Hydrology can run daily/monthly/yearly, but geomorphic/pedogenic changes are driven by annual aggregates.

However its vegetation module can flip forest/grass annually based on water balance and authors explicitly say it should not be used for annual-to-decadal ecological systems.

Therefore:
- useful architectural comparison
- not suitable as Gounsa succession engine

---

# 11. recommended temporal architecture

## daily
LPJ-GUESS:
- climate
- hydrology
- runoff
- soil temperature
- chemical weathering driver

SWEHR:
- only during erosive rainfall events, internal CFL timestep

## annual
After annual LPJ-GUESS state update:
- root-growth/decay bioturbation
- woody root-fracture/mechanical weathering
- stochastic tree throw
- residual background creep
- accumulated chemical-weathering mass balance
- update soil/regolith thickness and DEM

## event/disturbance
- wildfire
- dry ravel pulse
- shallow landslide
- major windthrow if explicitly forced
- SWEHR erosive storms

This multi-rate architecture matches the natural process timescales better than one Pelletier-style coefficient evaluated every year.

---

# 12. proposed total equations / bookkeeping

## hillslope transport
```
q_hill
=
q_bg
+
q_rootgrowth
+
q_treethrow
+
q_dryravel
```

Shallow landslides are discrete mass-wasting events and should not be hidden in `q_hill`.

## weathering/soil-production
```
Delta H_prod
=
Delta H_chem
+
Delta H_woody_mech
+
Delta H_other_phys
```

where:
- `Delta H_chem`: accumulated LPJ-GUESS-CNP chemical weathering converted by mass/volume balance
- `Delta H_woody_mech`: Gabet-Mudd root-fracture/tree-throw physical production
- `Delta H_other_phys`: only if separately justified, e.g. frost/thermal processes

Fire spall remains a separate supply process.

---

# 13. current judgment

### Pelletier 2013
**not selected as primary 100-year process engine.**

### weathering
**Primary forcing/process sources:**
- LPJ-GUESS-CNP daily chemical-weathering/P-release forcing
- Gabet & Mudd annual woody mechanical weathering

**Validation/comparison:**
- REWTCrunch
- SoilGen
- SSSPAM
- Pelletier long-term

### hillslope transport
**Primary modular structure:**
- residual background creep
- Gabet 2003 annual root-growth/decay transport
- Doane 2021 annual tree throw
- Lamb postfire dry ravel
- separate shallow landslide

This is the present preferred architecture for Gounsa.


---

# 14. second-pass source audit corrections

A second source-level audit corrected three important archive interpretations.

## Gabet et al. 2021
DOI `10.1029/2020JF005858` is:
```
Hilltop Curvature Increases With the Square Root of Erosion Rate
```

It is **not** a biomass-to-transport-efficiency paper.

Role:
- effective hillslope transport coefficient / erosion-rate constraint
- warning against treating `D` as a simple vegetation parameter

## Pelletier et al. 2018
DOI `10.1002/esp.4306` is:
```
Which way do you lean? Using slope aspect variations to understand Critical Zone processes and feedbacks
```

It is **not** a direct biomass-to-diffusivity numerical model.

Role:
- Critical Zone synthesis
- long-term conceptual consistency only

## Kirwan & Shugart 2008
```
A Biologically Based Model of Tree Throw on Hillslopes
```
is an AGU Fall Meeting abstract rather than a peer-reviewed full journal article.

Use only as an early annual forest-demography/tree-throw precedent.

Quantitative tree-throw support should instead prioritize:
- Constantine et al. 2012
- Doane et al. 2021
- Gabet & Mudd 2010

## strengthened postfire process separation
Roering & Gerber 2005 and Jackson & Roering 2009 strengthen:

```
background creep
!= postfire dry ravel
!= root-decay / landslide response
```

Therefore no universal postfire diffusivity multiplier is adopted.

## final evidence hierarchy

### production process sources
- Dantas de Paula et al. 2025: chemical-weathering forcing
- Gabet & Mudd 2010: annual woody mechanical weathering
- Gabet et al. 2003: root-growth/decay transport equations
- Doane et al. 2021: annual stochastic tree throw
- Constantine et al. 2012: cohort/storm windthrow support
- Lamb et al. 2011: postfire dry ravel

### validation / sensitivity
- REWTCrunch 2022
- SoilGen 2022
- Roering 2001
- Roering & Gerber 2005
- Jackson & Roering 2009

### comparison / long-term consistency
- SSSPAM 2019/2021
- HydroLorica 2020
- Pelletier 2013
- Pelletier et al. 2018
- Gabet et al. 2021
