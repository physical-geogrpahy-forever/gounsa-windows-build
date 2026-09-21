# Vegetation-weathering coupling for Gounsa

## current corrected structure

Vegetation effects on weathering are split into three classes.

### A. dynamic chemical weathering: production core

```
LPJ-GUESS
├─ PFT / NPP
├─ root and litter state
├─ soil water / runoff / drainage
├─ soil temperature
├─ root / litter / SOM respiration
└─ nutrient uptake / turnover
        |
        v
vegetation-weathering interface
        |
        v
WITCH / PROFILE-style mineral reactions
        |
        ├─ dissolved mass loss W_chem
        └─ nutrient release
```

Published precedents:
- B-WITCH
- WITCH-ASPECTS
- ForSAFE
- Banwart biological proton-cycle model
- Taylor root/mycorrhizal weathering model

### B. explicit root-exudation chemistry: advanced option

```
FineRootC(z,t)
 -> exudation
 -> microbial reactions / acidity
 -> mineral dissolution
```

Primary precedent:
REWTCrunch.

This is not required for the first production run because of parameter burden, but it is no longer correct to state that vegetation has no direct chemical-weathering pathway.

### C. biomechanical root weathering: not hard-locked

Evidence:
- Gabet & Mudd 2010 numerical root-fracture/tree-throw model
- Pawlik et al. 2023 sandstone field evidence
- Pawlik et al. 2016 review
- Malik et al. 2019 crack/root anatomy

Problem:
no transferable universal:

```
FineRootC
 -> annual sandstone soil-production rate
```

has been established.

Therefore do not invent:
```
P_sand = P_sand(H) * f(root biomass)
```

for the production baseline.

## sandstone front-production treatment

Keep:

```
P_sand(H)
```

as background bedrock-to-mobile-soil production / front lowering.

Mandatory sensitivity:
- Mode A exponential
- Mode B shallow finite-depth hump

Vegetation modifies the geomorphic system around this law through:
- water erosion
- Gabet root transport
- dry ravel
- mobile-soil depth H
- chemical dissolution W_chem

Direct biomechanical root fracture remains an optional future sensitivity unless a defensible site-calibrated law is found.

## mass-balance rule
To avoid double counting:

```
P_sand(H)
= parent-material -> mobile-soil production / boundary lowering

W_chem,AB
= dissolved chemical loss from mobile soil / explicitly modelled weathering domain
```

If WITCH is extended into the parent-material front and its dissolution is converted into boundary lowering, P_sand must be re-partitioned or recalibrated. Do not add both independently over the same mass.

## feedback to LPJ-GUESS
Intended full feedback:

```
LPJ-GUESS
 -> water / T / respiration / uptake / litter
 -> chemical weathering
 -> P and other nutrient release
 -> LPJ-GUESS-CNP nutrient pools
 -> growth / roots / litter
```

The return arrow from weathering to LPJ-GUESS is a new coupling, although two-way forest-soil feedback has strong precedent in ForSAFE.

## current judgment
- vegetation effect on chemical weathering: **explicitly required**
- vegetation effect on physical sandstone production: **mechanistically supported but quantitatively unresolved**
- Hartmann-only: **benchmark, no longer sufficient as the complete vegetation-weathering representation**
