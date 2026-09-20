# Gounsa literature second-pass handoff

날짜: 2026-09-21  
브랜치: `gounsa-water-erosion-deep-review-2026-09-21`

## 이번 세션 목적
풍화 및 사면수송 후보문헌을 원문/DOI 기준으로 다시 감사하고, 잘못 연결된 서지와 역할을 정정한다.

## 유지된 핵심결론

```
Pelletier 2013
!= 100-year primary process engine
```

100년 고운사는 daily/event/annual multi-rate architecture를 사용한다.

## production process hierarchy

### chemical-weathering forcing
Dantas de Paula et al. 2025 LPJ-GUESS-CNP
- daily patch calculation
- runoff + soil temperature + lithology
- chemical-weathering/P-release forcing
- **not** direct geomorphic regolith-production engine

### woody mechanical weathering
Gabet & Mudd 2010
- annual model
- root fracture
- tree throw
- physical bedrock erosion

### root-growth/decay transport
Gabet et al. 2003
- process equations
- root mass + turnover + depth/geometry
- not full numerical LEM

### tree throw
Doane et al. 2021
- annual stochastic pit-mound events
- primary spatial/tree-throw theory

Constantine et al. 2012
- forest-gap/tree-size/storm windthrow support

### postfire dry ravel
Lamb et al. 2011
Roering & Gerber 2005
Jackson & Roering 2009

## background creep

First implementation:
```
q_bg = -D_bg S
```
as a residual term.

Roering 2001 nonlinear transport remains sensitivity/alternative.

Reason:
a field-calibrated total forest diffusivity may already contain root growth, tree throw and disturbance transport. Those are represented separately in Gounsa, so using the total coefficient risks double counting.

## chemical validation

REWTCrunch 2022:
- daily
- root biomass/exudation
- reactive transport
- mineral dissolution
- advanced mechanistic validation

SoilGen 2022:
- daily hydrology
- 1D profile chemistry
- independent benchmark

## comparison only

SSSPAM:
- 100-year landform simulations
- physical weathering/profile/armour
- no dynamic forest/root state
- overlaps SWEHR surface/sediment states

HydroLorica:
- daily/monthly/yearly hydrology
- authors warn simplified vegetation is not suitable for annual-decadal ecological study

Pelletier 2013:
- 10 Myr geologic-time-scale coevolution
- long-term consistency only

## archive corrections

### 1. Gabet et al. 2021
Old incorrect file:
`papers/2021_Gabet_HillslopeTransportEfficiency.md`

was removed.

Actual DOI 10.1029/2020JF005858:
`Hilltop Curvature Increases With the Square Root of Erosion Rate`

Canonical:
`papers/2021_Gabet_HilltopCurvature_ErosionRate.md`

No direct biomass/root-state input.

### 2. Pelletier et al. 2018
Old incorrect file:
`papers/2018_Pelletier_Biomass_Diffusivity.md`

was removed.

Actual DOI 10.1002/esp.4306:
`Which way do you lean? Using slope aspect variations to understand Critical Zone processes and feedbacks`

Canonical:
`papers/2018_Pelletier_SlopeAspect_CriticalZone.md`

Not a direct biomass-diffusivity numerical model.

### 3. Kirwan & Shugart 2008
Reclassified as AGU Fall Meeting abstract:
`A Biologically Based Model of Tree Throw on Hillslopes`

Use only as early model-lineage support.

### 4. Roering & Gerber 2005
Exact citation restored:
Geology 33(5), 349-352, DOI 10.1130/G21260.1.

### 5. Jackson & Roering 2009
New canonical file:
`papers/2009_Jackson_Roering_Postfire_Oregon.md`

Supports separate dry-ravel/root-decay/landslide processes.

## updated model/decision files
- `models/LPJ_GUESS_Weathering.md`
- `models/REWTCrunch.md`
- `models/Short_Timestep_Weathering_HillslopeTransport.md`
- `decisions/2026-09-21_WEATHERING_HILLSLOPE_TIMESCALE.md`
- `decisions/2026-09-21_WEATHERING_HILLSLOPE_SECOND_PASS_AUDIT.md`
- `MASTER.md`

## remaining unresolved items
1. chemical-weathering flux -> solid regolith mass/thickness conversion
2. Gounsa lithology parameters
3. LPJ-GUESS woody cohort -> root-fracture/rootwad geometry
4. residual background `D_bg`
5. cohort state -> tree-throw event probability/volume
6. quantify actual weathering magnitude over 100 years
7. coarse-fragment/armour reconciliation with SWEHR
8. fire-spall production module
