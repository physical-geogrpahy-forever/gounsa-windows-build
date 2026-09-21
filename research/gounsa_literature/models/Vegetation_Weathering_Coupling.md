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

## competing vegetation-weathering pathways

Do not assume vegetation always increases weathering.

### enhancement pathways

```
root / SOM respiration
 -> soil and fracture CO2
 -> acidity
 -> mineral dissolution
```

```
root exudation / organic ligands
 -> local reaction kinetics
 -> mineral dissolution
```

```
nutrient uptake / return
 -> proton and ion balance
 -> soil solution chemistry
 -> mineral dissolution
```

Osorio-Leon et al. 2025 provides direct deep-rhizosphere reactive-transport evidence that this pathway can be large at a specific site.

### damping / supply-limitation pathways

Oeser & von Blanckenburg 2020:
```
higher NPP
does not imply
higher weathering rate
```

because nutrient recycling and abiotic supply controls can dominate.

Zuo et al. 2024:
```
vegetation
 -> lower erosion
 -> lower fresh-mineral supply
 -> lower supply-limited weathering
```

Therefore no scalar vegetation enhancement factor is used in the production architecture.

## biomechanical root-weathering mechanics status

Mechanistic evidence is advancing:
- Calusi et al. 2020: root as mechanical inclusion, stress and fracture-regrowth cycle in soil media
- Wright et al. 2026: FE crack-propagation approach in high-strength environments, conference abstract
- Pawlik et al. 2023: sandstone field evidence for root involvement in weathering
- Malik et al. 2019: crack widening recorded by root anatomy, but root-pressure causation inconclusive

Current boundary:

```
root mechanics
 -> process support / future sensitivity

NOT

LPJ-GUESS FineRootC
 -> calibrated annual sandstone production flux
```


## third-pass refinements: roots, mycorrhiza, spatial hydrology

### root vertical distribution is a required chemical-weathering state

Gatz-Miller et al. 2023 used 2D reactive transport over 170 years and compared simplified versus dynamically evolving root architecture.

The root representation changed:
- local water uptake
- solute transport
- depth and geometry of geochemical zones

Therefore the Gounsa chemical-weathering interface must preserve at minimum:

```
FineRootC(z)
root fraction by layer
root-access depth
root water uptake by layer
```

Do not collapse all belowground vegetation state to total FineRootC.

### root exudate availability is partitioned

Garcia-Arredondo et al. 2023 shows root-derived DOC can be partitioned among:
- microbial consumption
- mineral sorption
- redox reactions
- dissolved transport

Therefore:

```
root exudation source
!=
100% mineral-weathering ligand
```

REWTCrunch sensitivity should include an exudate availability / partition term rather than treating all root C as chemically available.

### mycorrhiza scope

Mycorrhizal functional type, fungal hypha weathering, and fungal oxalate allocation are **excluded from current production and sensitivity architecture**.

Relevant literature is archive/reference only.

Do not create:
```
PFT -> AM/EcM -> weathering
```
or any mycorrhizal multiplier.

Vegetation-weathering production remains based on root state, respiration/CO2, hydrology, litter/SOM, nutrient uptake/return, and non-mycorrhizal DOC/organic-ligand sensitivity.

### sandstone-specific biogeochemical sensitivity

Potysz & Bartz 2024 shows simulated rhizospheric organic conditions can enhance sandstone deterioration, with strong dependence on:
- Fe-bearing cement
- goethite vs hematite
- cement dissolution
- sandstone matrix/mineralogy

Therefore Gounsa sandstone petrography is required not only for P_sand(H) but also for chemical vegetation-weathering parameterization.

### spatial hydrology alternatives

BioRT-Flux-PIHM and Wen et al. 2022 show that:
```
topography
 -> shallow/deep flow partition
 -> residence time
 -> chemical reaction environment
 -> W_chem / solute export
```

can matter at watershed/hillslope scales.

Current WITCH/PROFILE production target remains, but BioRT is now a spatial alternative / validation engine.

### possible W_chem -> soil-production bridge

Yu & Hunt 2018 provides a transport-limited framework connecting chemical weathering / solute transport to gross soil production and erosion-adjusted net soil formation.

This is a future mechanistic sensitivity only.

Current production remains:
```
W_chem
!=
P_sand(H)
```

until a mass-conserved sandstone-specific front model is adopted.


## fourth-pass non-mycorrhizal production core

Authoritative decisions:
- `decisions/2026-09-21_MYCORRHIZA_EXCLUSION.md`
- `decisions/2026-09-21_SOIL_WEATHERING_FOURTH_PASS_NON_MYCORRHIZAL.md`

### production-required vegetation states

```
PFT / NPP
FineRootC(z)
root fraction by layer
root access depth
root water uptake by layer
root / belowground respiration
litter / SOM state
nutrient uptake / return
soil temperature
soil water / runoff / drainage
```

### production-required reaction/hydrologic states

```
pCO2 / CO2 source by depth
pH / H+
mineralogy
reactive surface area
soil water
flow-path depth
water residence time
saturation state / reaction affinity
secondary-mineral state
```

### optional sensitivity only

```
root-derived DOC / organic ligand source
```

Root-exudate sensitivity is optional because:
- Calvaruso 2013 verifies a strong living-root dissolution pathway
- Chibesa 2025 shows compound/mineral-specific response
- Lawrence 2014 shows profile-scale net response can differ from local dissolution enhancement
- Garcia-Arredondo 2023 shows root-derived C partitions to sorption and microbial consumption

Do not require explicit exudate speciation in first production.

### hydrologic control

Maher 2010 makes fluid residence time a central weathering control.

Therefore:
```
runoff only
!= sufficient hydrologic weathering state
```

At minimum test:
- drainage
- subsurface flow-path depth
- water residence time

### deep-root CO2

Tune 2020, Tune 2023, and Osorio-Leon 2025 support:

```
deep rooting
 -> below-soil respiration / CO2
 -> bedrock-zone acidity
 -> chemical weathering
```

Thus root access depth may exceed mobile-soil thickness and CO2 source may occur in C/Cr or fractured bedrock.

### no mycorrhiza

Current production and sensitivity contain no:
```
AM / EcM
mycorrhizal_type
fungal weathering multiplier
fungal oxalate allocation
```


## current judgment
- vegetation effect on chemical weathering: **explicitly required**
- vegetation effect on physical sandstone production: **mechanistically supported but quantitatively unresolved**
- Hartmann-only: **benchmark, no longer sufficient as the complete vegetation-weathering representation**
