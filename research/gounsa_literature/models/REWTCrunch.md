# REWTCrunch model lineage

## 핵심 논문
Roque-Malo, S., Druhan, J. L., & Kumar, P. (2022). *REWTCrunch: A Modeling Framework for Vegetation Induced Reactive Zone Processes in the Critical Zone*. Journal of Geophysical Research: Biogeosciences, 127, e2021JG006562. DOI: 10.1029/2021JG006562.

## 모델 구조
REWTCrunch combines:
- MLCan multilayer canopy/root ecohydrology
- REWT root exudation and vertical transport
- CrunchFlow multicomponent reactive transport

Core:
```
root biomass(z,t)
 -> root exudation
 -> microbial/chemical reactions
 -> mineral dissolution / weathering products
 -> vertical solute transport
```

## 시간간격
The published simulations operate at a **daily timescale**.

The forcing includes:
- daily precipitation
- daily air temperature
- vegetation/LAI-derived biomass states
- soil moisture and temperature
- root uptake/exudation

Thus this is genuinely a short-timescale vegetation-weathering process model, not merely a geologic steady-state weathering relation.

## 식생 입력
The original application derives below-ground biomass from above-ground biomass/LAI and a vertical root-distribution probability function.

For Gounsa:
- replace that simplified root-biomass estimation with LPJ-GUESS native root states
- retain the reactive-transport logic only if detailed chemical-weathering validation is needed

That replacement is a **new coupling**.

## spatial structure
- vertically resolved soil profile
- arbitrary multilayer discretization
- no 2D lateral geomorphic routing
- not a landscape-evolution model

## key root-exudation formulation
The framework calculates exudation as a function of:
- root biomass through depth
- exudation rate per root mass
- control-volume geometry

It then sends updated chemical states and rate multipliers to CrunchFlow.

## source availability
A public REWTCrunch v1.0.0 software archive exists on Zenodo and links to the project GitHub repository.

This makes source-level inspection and future validation feasible.

## 고운사에서의 역할
**Advanced mechanistic validation module for chemical weathering.**

Strong points:
- daily timescale
- quantitative root state
- explicit root exudation
- explicit mineral dissolution
- vertically resolved rhizosphere

## why not primary production core
Compared with LPJ-GUESS-CNP:
- substantially higher parameter burden
- separate canopy/root model would be redundant
- coupling LPJ-GUESS to CrunchFlow is nontrivial
- no lateral geomorphic transport
- does not directly output regolith-thickness production

Therefore first implementation should not run full REWTCrunch everywhere for 100 years.

## new coupling
Even with mineral dissolution calculated, converting it into geomorphic production requires:

```
mineral dissolution / mass loss
 -> solid-volume change
 -> regolith/soil thickness change
```

This remains a new mass-balance coupling.

## current judgment
**채택 as mechanistic validation / advanced option, not primary whole-domain weathering engine.**

Use to test whether the simpler LPJ-GUESS-CNP weathering forcing misses important root-exudation effects.

## references
- DOI: 10.1029/2021JG006562
- Zenodo software archive: REWTCrunch v1.0.0
