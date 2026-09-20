# 2차 감사: 100년 고운사 풍화 및 사면수송 문헌 재정리

날짜: 2026-09-21

## 감사 목적
직전 결론을 다시 원문과 정확한 서지정보 기준으로 확인하고, 잘못 연결된 논문과 역할을 정정한다.

## 핵심 결론
기존 결정:
```
Pelletier 2013을 주식으로 쓰지 않고
daily/annual process-specific modules를 쓴다
```
는 유지한다.

다만 문헌 역할을 더 엄밀하게 정리한다.

---

## A. 1차 채택 계보

### chemical-weathering forcing
**Dantas de Paula et al. 2025, LPJ-GUESS-CNP**
- actual LPJ-GUESS implementation
- daily patch weathering
- prognostic runoff and soil temperature
- vegetation affects runoff
- output is P/chemical-weathering flux, not geomorphic soil-production thickness

판정:
```
chemical-weathering forcing = 채택
soil-production engine = 아님
```

### mechanistic chemical validation
**Roque-Malo et al. 2022 REWTCrunch**
- daily timescale
- root biomass/exudation
- reactive transport
- mineral dissolution
- public software archive

판정:
advanced validation / sensitivity module.

### woody mechanical weathering
**Gabet & Mudd 2010**
- annual timestep confirmed
- annual seed recruitment, mortality, tree throw, physical clast weathering and bedrock-erosion bookkeeping
- root fracture + tree throw
- actual numerical biogeomorphic model

판정:
primary annual woody-mechanical-weathering lineage.

### root-growth/decay transport
**Gabet, Reichman & Seabloom 2003**
- quantitative review
- derives process-specific sediment-flux equations for root growth/decay and tree throw
- not a complete numerical landscape model

판정:
primary root-bioturbation process equation source.

### tree throw
**Doane et al. 2021**
- numerical test uses one-year timestep
- stochastic annual pit-mound production
- tree-throw vs creep flux theory
- field/LiDAR validation

판정:
primary spatial/theoretical tree-throw flux source.

**Constantine et al. 2012**
- ForGEM forest-gap dynamics + windthrow sediment flux
- tree-size distribution and storm forcing
- centennial-scale forest disturbance response

판정:
primary cohort/storm tree-throw supporting source.

---

## B. postfire process separation

### Roering & Gerber 2005
Exact citation recovered:
Geology 33(5), 349-352, DOI 10.1130/G21260.1.

Key:
- postfire dry-ravel flux nonlinear with slope
- postfire critical gradient 1.03 vs long-term 1.27
- immediate/first-year postfire state
- not annual vegetation-recovery model

Role:
postfire dry-ravel state, not background creep.

### Jackson & Roering 2009
New canonical paper file added.

Key:
- three steep burned forest sites
- dry ravel important
- hydrophobicity did not automatically yield runoff erosion
- root-strength decay and landslide susceptibility distinct
- supports separating dry ravel, root decay and landslide from background diffusion

---

## C. background creep

### baseline
Use a residual background term:
```
q_bg = -D_bg S
```

This is a bookkeeping/process-separation choice, not a claim that all natural creep is intrinsically linear.

Reason:
tree throw, root growth, dry ravel and landslide are represented separately.

### Roering nonlinear law
Roering 2001 remains the steep-slope sensitivity/alternative.

Do not use a natural-landscape total calibrated `K` unchanged because it may already aggregate:
- bioturbation
- tree throw
- dry ravel
- other disturbance processes

Near-critical nonlinearity may also overlap with separately modeled shallow landslides.

---

## D. comparison models

### SSSPAM
- explicit 100-year simulations
- physical weathering, soil profile, armouring
- no dynamic forest/root model
- overlaps SWEHR sediment/armour states

Role:
comparison and coarse-fragment/armour source.

### HydroLorica
- daily/monthly/yearly hydrologic timestep
- annual geomorphic aggregation
- authors explicitly warn vegetation implementation should not be used for annual-decadal systems

Role:
architecture reference only.

### SoilGen
- daily hydrology/profile chemistry
- 1D
- 20,000-year application
- no dynamic forest cohort

Role:
chemical-profile benchmark.

### Pelletier 2013
- geologic-time-scale eco-pedo-geomorphic coevolution
- 10 Myr reported states
- small numerical dt only solver stability

Role:
long-term structural benchmark only.

---

## E. corrected archive errors

### Gabet et al. 2021
Previous file incorrectly described DOI 10.1029/2020JF005858 as a biomass transport-efficiency paper.

Actual paper:
*Hilltop Curvature Increases With the Square Root of Erosion Rate.*

It has no direct biomass/root-state input.

Correct role:
warning that effective hillslope transport coefficients aggregate unresolved processes and vary with erosion rate.

### Pelletier et al. 2018
Previous file incorrectly described DOI 10.1002/esp.4306 as a direct biomass-diffusivity numerical paper.

Actual paper:
*Which way do you lean? Using slope aspect variations to understand Critical Zone processes and feedbacks.*

Correct role:
conceptual/synthesis Critical Zone reference, not direct annual biomass-to-diffusivity law.

### Kirwan & Shugart 2008
Classified correctly now as:
*A Biologically Based Model of Tree Throw on Hillslopes*, AGU Fall Meeting abstract.

It is an early preliminary numerical precedent, not a peer-reviewed full article.

---

## F. weathering interpretation tightened

LPJ-GUESS-CNP must not be called a full geomorphic soil-production model.

Correct chain:
```
LPJ-GUESS runoff + Tsoil + lithology
 -> daily empirical chemical-weathering/P-release flux
 -> [new coupling] solid mass/volume conversion
 -> regolith-thickness update
```

Oeser & von Blanckenburg 2020 is retained as a critical constraint:
NPP/productivity does not show a simple monotonic positive relation with silicate-weathering rate.

Therefore no:
```
NPP -> universal weathering multiplier
```
is adopted.

---

## final paper hierarchy

### production-core process sources
- Dantas de Paula et al. 2025
- Gabet & Mudd 2010
- Gabet et al. 2003
- Doane et al. 2021
- Constantine et al. 2012
- Lamb et al. 2011

### advanced validation
- REWTCrunch 2022
- SoilGen 2022
- Roering 2001
- Jackson & Roering 2009
- Roering & Gerber 2005

### comparison / long-term consistency
- SSSPAM 2019/2021
- HydroLorica 2020
- Pelletier 2013
- Pelletier et al. 2018
- Gabet et al. 2021

## updated unresolved after mass-balance review
1. 100-year magnitude of chemical front advance, dissolved mass loss and woody mechanical production
2. Gounsa lithology, rock density and initial C/Cr state
3. select/calibrate chemical front model: DynSoil/MErSiM vs Braun-type hydrologic front
4. residual `D_bg`
5. LPJ-GUESS woody cohort -> rootwad/root-fracture geometry
6. tree-throw probability/volume from cohort state
7. partition chemical dissolved loss between mobile A/B and deeper C/Cr


---

## G. weathering mass-balance review

새 결정:
`decisions/2026-09-21_WEATHERING_MASS_BALANCE.md`

이전:
```
chemical weathering flux
 -> density conversion
 -> regolith thickness
```
처럼 압축해 표현했던 gap을 철회한다.

정확한 분리는:

```
chemical dissolved mass loss
!=
bedrock-to-regolith front advance
```

### mobile A/B soil
Yoo 2007, Brosens 2020:

```
dM_AB/dt
=
Phi_AB + D_phys - E_phys - W_AB
```

### C/Cr regolith
DynSoil/MErSiM:

```
dh_reg/dt
=
P_r - E_boundary
```

while mineral dissolution is tracked separately:

```
W_chem
=
integral K tau^sigma x dz
```

### Hartmann/LPJ-GUESS correction
Hartmann 2011 parent model computes bulk rock-weathering flux first, then derives P liberation from lithology-specific P content.

Therefore Gounsa should retain separate:
```
F_bulk_chem
F_P_release
```

and should not reconstruct geomorphic mass loss from the LPJ-GUESS P pool if the parent bulk-weathering relation can be evaluated directly.

### current front candidates
- DynSoil/MErSiM: preferred transient state architecture
- Braun 2016: groundwater-driven weathering-front alternative

The conceptual mass-balance gap is now resolved. The remaining issue is quantitative calibration and 100-year significance.
