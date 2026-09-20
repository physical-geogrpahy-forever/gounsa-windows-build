# LPJ-GUESS weathering coupling lineage

## 핵심 논문
Dantas de Paula, M., Forrest, M., Warlind, D., Darela Filho, J. P., Fleischer, K., Rammig, A., & Hickler, T. (2025). *Including the phosphorus cycle into the LPJ-GUESS dynamic global vegetation model (v4.1, r10994) – global patterns and temporal trends of N and P primary production limitation*. Geoscientific Model Development, 18, 2249-2274. DOI: 10.5194/gmd-18-2249-2025.

관련:
- Hartmann & Moosdorf 2011 chemical weathering model
- Hartmann et al. 2014 global chemical weathering + soil shielding
- Oeser et al. 2020
- Taylor et al. 2012 DGVM/weathering comparison
- Roque-Malo et al. 2022 REWTCrunch for root-induced reactive processes

## 현재 확인된 LPJ-GUESS-CNP weathering structure

LPJ-GUESS-CNP v1.0 contains a **real implemented daily weathering calculation**.

For each simulated patch:

```
F_PW
=
F_CW,i
* F_T
* F_s,i
```

and:

```
F_CW,i
=
(b_carbonate + b_silicate)_i
* p_i
* q
```

where:
- `q`: LPJ-GUESS prognostic runoff
- `T`: LPJ-GUESS prognostic daily soil temperature
- lithological parameters come from the Hartmann/Moosdorf CWM lineage
- `F_s,i`: soil-shielding factor

Temperature response:

```
F_T
=
exp[
  -(Ea_i/R)
  * (1/T - 1/T0)
]
```

with:
```
T0 = 284.15 K
```

## 시간간격

**Daily weathering rate for each LPJ-GUESS patch.**

This is the key distinction from Pelletier 2013.

```
LPJ-GUESS vegetation
 -> hydrology/runoff
 -> daily weathering
```

already exists within the model family.

## vegetation feedback

Vegetation does not enter as a simple biomass multiplier.

Instead:

```
vegetation structure
 -> LPJ-GUESS water balance
 -> prognostic runoff
 -> chemical weathering
```

This is more defensible for the 100-year Gounsa model than transferring a geologic-scale AGB/EEMT relation directly to annual vegetation succession.

## 고운사에서의 역할

### primary hydroclimatic chemical-weathering driver
Use LPJ-GUESS native:
- runoff
- soil temperature
- lithology/weathering parameters

rather than an external EEMT proxy.

### output caveat
LPJ-GUESS-CNP computes chemical-weathering/P-release flux.

It does **not** directly calculate:
```
bedrock -> regolith thickness
```

Thus a solid mass/volume balance is still needed if weathering must change C/Cr/soil thickness in the geomorphic grid.

## woody mechanical weathering is separate

Do not force all weathering into the CNP chemical term.

Use a separate annual physical pathway:
```
LPJ-GUESS woody cohort
 -> root fracture / tree throw
 -> physical bedrock erosion
```
with Gabet & Mudd 2010 as the main precedent.

## optional advanced chemical module

REWTCrunch can be used as:
- mechanistic validation
- sensitivity study for deep-root respiration/exudation
- possible future high-detail module

but is not required for the first production model.

## comparison with Pelletier 2013

Pelletier:
- excellent long-term eco-pedo-geomorphic framework
- geologic forcing/calibration
- 10 Myr reported landscape states
- small numerical dt only for solver stability

LPJ-GUESS-CNP:
- daily patch weathering
- actual dynamic LPJ-GUESS hydrology
- directly follows vegetation-induced runoff changes
- much better 100-year forcing interface

## 판정
**채택: daily hydroclimatic chemical-weathering core.**

Pelletier 2013 is demoted to long-term structural/reference use.

Remaining new coupling:
```
chemical weathering mass/mineral flux
 -> geomorphic regolith mass/thickness
```
