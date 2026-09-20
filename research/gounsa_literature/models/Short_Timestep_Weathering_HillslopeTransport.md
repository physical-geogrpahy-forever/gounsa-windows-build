# Short-timescale weathering and hillslope-transport architecture for Gounsa

## 목적
고운사 산불 후 약 100년 simulation에서 Pelletier 2013을 풍화/토양생산 및 사면확산의 주 모델로 쓸지, 더 짧은 시간간격의 published process models로 대체할지를 통합 정리한다.

## 현재 production scope

포함:
- water erosion
- residual background creep
- root-growth/decay biogenic transport
- postfire dry ravel
- chemical weathering / regolith-front production
- fire spall / coarse-fragment supply

제외:
- tree throw / uprooting
- shallow landslide

제외 항목 문헌은 archive-only로 유지한다.

---

# 1. 핵심 결론

**Pelletier 2013을 100년 production engine으로 사용하지 않는다.**

현재 baseline:

```
WEATHERING

chemical-weathering forcing
 = Hartmann + LPJ-GUESS-CNP [daily forcing]

sandstone soil production
 = P_sand(h) = P0_sand exp(-h/gamma_sand) [annual]

advanced deeper-regolith option
 = DynSoil/MErSiM or Braun [optional]

mobile A/B soil mass balance
 = Yoo 2007 + Brosens 2020

fire spall
 = separate physical supply process


HILLSLOPE TRANSPORT

q_hill
 =
 q_bg
 + q_rootgrowth
 + q_dryravel
```

---

# 2. 왜 Pelletier 2013을 주식으로 쓰지 않는가

Pelletier 2013:
- geologic-time-scale eco-pedo-geomorphic coevolution
- prescribed EEMT states
- reported landscape states after about 10 Myr
- small internal dt is numerical-stability requirement

따라서:

```
small numerical dt
!=
annual ecological/process calibration
```

직접:

```
LPJ-GUESS biomass(t)
 -> Pelletier diffusivity(t)
```

를 existing published annual coupling으로 취급하지 않는다.

Pelletier의 현재 역할:
- long-term sign check
- steady-state consistency benchmark
- comparison only

---

# 3. chemical weathering

## 3.1 Hartmann + LPJ-GUESS-CNP

부모 Hartmann 계보는 먼저 bulk chemical-weathering flux를 계산하고, lithology-specific P content를 사용해 P release를 계산한다.

따라서 고운사에서는:

```
F_bulk_chem
F_P_release
```

를 분리한다.

LPJ-GUESS-CNP는 daily:
- soil temperature
- runoff
- patch state

를 제공하므로 short-timescale chemical-weathering forcing에 적합하다.

그러나:

```
chemical dissolved mass loss
!=
bedrock-to-regolith production
```

이다.

## 3.2 A/B mobile-soil mass balance

```
M_AB = rho_AB H_AB
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

Yoo 2007 / Brosens 2020 계보를 사용한다.

## 3.3 sandstone soil production

Production baseline:

```
P_sand(h)
=
P0_sand exp(-h/gamma_sand)
```

Sandstone evidence:
- Heimsath et al. 2001
- Evans et al. 2019
- Evans et al. 2021

Observed sandstone analogue envelope:

```
P0_sand = 0.071-0.274 mm yr^-1
gamma_sand = 0.80-4.50 m
```

These are sensitivity bounds only.

DynSoil/MErSiM and Braun 2016 are optional advanced deeper-regolith models, not the first production baseline.

## 3.4 uprooting 기반 mechanical weathering

현재 production baseline에서 제외한다.

Gabet & Mudd 2010의 rootwad/tree-throw physical production은 archive/reference only이다.

현재 물리적 공급에서 핵심은:
- fire spall
- 별도로 검증되는 other physical weathering

이다.

---

# 4. residual background creep

Production baseline:

```
q_bg
=
-D*_bg H_active grad(z)
```

근거:
- Furbish et al. 2009
- Furbish & Haff 2010

장점:
- active mobile-soil thickness가 줄면 flux도 줄어듦
- A/B soil이 거의 없는데도 constant D가 계속 토사를 운반하는 문제 방지

`D*_bg`는:
- natural-landscape total diffusivity가 아님
- biomass multiplier가 아님
- residual local-creep coefficient임

포함 가능한 미해상 과정:
- wetting-drying
- weak freeze-thaw
- fauna
- micro-scale granular rearrangement
- unresolved shallow bioturbation

Sonoda & Kurashige 2017의 일본 풍화화강암 산림 관측은 wet-dry residual creep의 중요한 지역적 근거다.

---

# 5. root-growth / root-decay biogenic transport

Gabet et al. 2003을 사용한다.

General:

```
q_sx
=
x r tau / rho_r
```

```
x
=
z_c sin(theta) cos(theta)
```

Final form:

```
q_sx
=
-[0.003 r tau / (rho_r log(beta))]
sin(theta) cos(theta)
```

where:
- `r`: root mass per area
- `tau`: root turnover [yr^-1]
- `rho_r`: root tissue density
- `beta`: vertical root-distribution parameter
- `theta`: slope angle

For production, do not use Gabet's broad vegetation-class example parameters if LPJ-GUESS native root state is available.

Preferred interface:

```
LPJ-GUESS
 fine-root state
 root turnover
 layer root distribution
       |
       v
root center-of-mass depth
       |
       v
Gabet q_rootgrowth
```

LPJ-GUESS already contains PFT-specific fine-root turnover parameterization, so an external turnover model is not required.

The Gabet derivation represents an upper-bound-style displacement because some real root-growth strain can be absorbed by local soil-density change.

---

# 6. postfire dry ravel

Dry ravel remains a separate disturbance transport process.

Key lineages:
- Lamb et al. 2011
- Roering & Gerber 2005
- Jackson & Roering 2009

Do not convert fire effects into a generic multiplier on `D*_bg`.

Current separation:

```
background creep
!=
root-growth transport
!=
postfire dry ravel
```

---

# 7. excluded processes

## tree throw / uprooting
Not in current production baseline.

Doane, Gallaway, Constantine, Gabet & Mudd tree-throw literature remains archived only.

## shallow landslide
Not in current production baseline.

No factor-of-safety/root-cohesion implementation is currently required.

---

# 8. temporal architecture

## daily
LPJ-GUESS:
- hydrology
- runoff
- soil temperature
- vegetation/root state
- chemical-weathering forcing

SWEHR:
- erosive rainfall events only
- internal sub-hourly CFL-constrained timestep

## annual geomorphic update
- accumulated chemical-weathering mass balance
- sandstone soil production
- Gabet root-growth/decay transport
- residual depth-dependent creep
- soil/regolith thickness update
- DEM update

## disturbance events
- wildfire
- dry-ravel release
- fire spall
- SWEHR erosive storms

---

# 9. current production equations

## hillslope transport

```
q_hill
=
q_bg
+
q_rootgrowth
+
q_dryravel
```

with:

```
q_bg
=
-D*_bg H_active grad(z)
```

and Gabet root-growth/decay flux as above.

## weathering / regolith

```
A/B:
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

```
C/Cr:
dh_reg/dt
=
P_r
-
E_boundary
```

Chemical dissolution is tracked separately from front advance.

---

# 10. comparison models

## REWTCrunch
daily root-exudation/reactive-transport validation.

## SoilGen
daily hydrology + 1D chemical-profile weathering benchmark.

## SSSPAM
100-year soilscape/armour/profile benchmark, but no dynamic forest roots and overlaps SWEHR erosion states.

## HydroLorica
architecture reference only; its vegetation representation is not suitable for annual-decadal succession.

## Roering nonlinear transport
steep-slope sensitivity comparison only, not the baseline residual flux.

---

# 11. final current judgment

### weathering
Primary:
- sandstone-specific annual soil-production function
- Hartmann/LPJ-GUESS-CNP bulk chemical-weathering forcing
- Yoo/Brosens mobile-soil mass balance

Advanced optional:
- DynSoil/MErSiM transient mineral/regolith state
- Braun 2016 hydrologic front model

### hillslope diffusion/transport
Primary:
- Furbish depth-dependent residual creep
- Gabet 2003 root-growth/decay transport
- Lamb postfire dry ravel

### excluded
- uprooting/tree throw
- shallow landslide

### Pelletier
Long-term reference only.

## remaining implementation questions
1. exact Gounsa sandstone petrography and production parameters
2. 100-year magnitude of sandstone soil production and chemical mass loss
3. `D*_bg` residual calibration
4. exact LPJ-GUESS root-variable/unit mapping into Gabet equation
5. fire-spall production equation


---

# 12. sandstone correction

고운사 parent material은 sandstone으로 취급한다.

따라서 granite-based production magnitude는 local constraint가 아니다.

Sandstone production baseline:

```
P_sand(h)
=
P0_sand exp(-h/gamma_sand)
```

Evans et al. 2021:
```
P0_sand = 0.071-0.274 mm yr^-1
gamma_sand = 0.80-4.50 m
```

Evans et al. 2019 temperate conifer woodland mean:
```
0.070 +/- 0.010 mm yr^-1
```

Postfire soil thinning can therefore alter production naturally through `h`, without an arbitrary fire multiplier.

Sandstone matrix/cementation controls are critical, so final values require site petrography.

DynSoil/MErSiM is now optional sensitivity/advanced chemistry only.
