# MEDFATE + medfateland

업데이트: 2026-09-23 deep source audit

## 현재 판정
BiomeE/BiomeEP와 유사한 cohort process model을 **실제 GIS 공간단위로 확장한 가장 직접적인 공개 구현 사례 중 하나**.

고운사에서는 특히 다음 조합이 강점이다.
```text
actual geographic cells
+ tree/shrub cohorts
+ explicit herb cohorts in physiology/growth
+ cohort root-depth profiles
+ daily event-loop control
+ lateral/groundwater hydrology
+ explicit option to delegate bulk soil hydrology externally
```

가장 큰 약점은 **herbaceous demography의 비대칭성**이다.

## 식생 표현
MEDFATE:
- tree cohorts
- shrub cohorts
- optional species-specific herb cohorts (`herbData`)
- seed bank / seedling bank for woody regeneration
- cohort-specific fine-root depth distribution
- daily water/carbon/growth
- woody recruitment and forest dynamics

개별목 x,y는 추적하지 않는다.

## 공간 확장
medfateland:
- sf point/cell based spatial units
- terra raster topology for connected grid cells
- forest, soil, topography, weather state per spatial unit
- parallel execution
- explicit seed dispersal among stands
- lateral surface flow
- lateral subsurface flow
- groundwater/baseflow
- channel routing
- optional SERGHEI coupling

핵심 함수 계열:
- spwb_spatial / growth_spatial / fordyn_spatial
- spwb_land / growth_land / fordyn_land
- spwb_land_day / growth_land_day

This is much closer to a controllable Gounsa daily raster workflow than FATES/ELM.

## 실제 published spatial application
Balaguer-Romano et al. 2025:
- medfate 4.8.0 + medfateland 2.5.2
- Barcelona Metropolitan Region
- 313,000 ha
- 200 m raster grid
- daily weather forcing
- tree + understory shrub species
- growth, mortality and forest succession simulated 2015–2050

Current package topology is user-defined; no hard-coded 10–25 m prohibition was identified. Fine-resolution cost/scale validity remains untested.

---

# 1. external hydrology interface
Current source makes the external-hydrology option explicit.

In `spwb_day_c.cpp`, internal bulk soil-water balance is only called when:
```text
control.soilDomains != "none"
```

The one-day water/growth machinery accepts:
- runon
- layer-wise lateralFlows
- waterTableDepth
- external source/sink terms

Therefore:
```text
external hydrology owns bulk soil-water redistribution
 -> MEDFATE consumes hydrologic forcing/state
 -> vegetation physiology/growth responds daily
```
is directly compatible with the code architecture.

Criterion 3A:
**VERY STRONG**

---

# 2. dynamic soil layer geometry: exact source finding
MEDFATE has a direct layer-redefinition function:
```text
soil_redefineLayers(x, widths)
```

This is useful because layer geometry can actually be rebuilt after a geomorphic event.

However the source documentation explicitly states:
> if an initialized `soil` object is supplied, hydraulic parameters are recalculated and the value of state variables is lost.

Therefore this function is **not** a conservative erosion/deposition remapper.

Correct Gounsa use:
```text
old initialized soil state
 -> save water / C / N / other conserved pools
 -> compute new layer geometry from erosion/deposition
 -> call/reimplement layer redefinition
 -> conservatively map saved state into new layers
 -> recompute root fractions
 -> resume daily simulation
```

This is still a new coupling, but the exact insertion point is unusually clear.

Criterion 3B:
**CUSTOM but implementation-friendly**

---

# 3. root structure
Current source `src/root.cpp` explicitly reads root-depth parameters from all three life-form tables.

For `herbData` it reads:
- Z50
- Z95
- optional Z100

Trees and shrubs use analogous depth-profile information.

Thus existing herb cohorts are not cosmetic ground cover. They have explicit vertical root profiles participating in soil-water competition.

After an erosion event, required new rule remains:
```text
removed soil volume
 -> calculate roots physically removed from each cohort profile
 -> reduce live root/plant state if appropriate
 -> recompute Z-profile fractions over surviving soil
```

MEDFATE does not natively interpret layer redefinition as physical root severing.

---

# 4. herb demographic audit: decisive source evidence
MEDFATE documentation/NEWS can be misleading if read too broadly because recent releases mention both:
- seed recruitment with daily/annual environmental filters
- support for `herbData`

The source audit resolves this.

## 4.1 recruitment gap
`R/regeneration.R` explicitly removes herb vegetation when constructing the recruitment forest:
```text
if("herbData" %in% names(recr_forest)) recr_forest$herbData <- NULL
if("herbCover" %in% names(recr_forest)) recr_forest$herbCover <- NULL
```

The recruit-generation pathway then constructs tree/shrub recruit cohorts from woody recruitment/seedling banks.

Therefore:
```text
herb seed -> seed bank -> germination -> new herb cohort
```
is not implemented symmetrically with woody recruitment.

## 4.2 daily mortality gap
Current `src/growth_day_c.cpp` provides an even stronger source-level limitation.
In the daily mortality/fire section:
```text
bool dynamicCohort = true;
if((ctype[j] == "shrub") && (!shrubDynamics)) dynamicCohort = false;
else if(ctype[j] == "herb") dynamicCohort = false;
```

Thus herb cohorts are explicitly excluded from the dynamic cohort mortality branch used for carbon starvation/desiccation and related daily demographic loss.

Trees and dynamic shrubs can undergo these daily mortality calculations; herbs do not use the same demographic pathway.

Correct interpretation:
```text
existing herbData
 -> root profile, water competition, physiological/growth representation: YES

new herb recruitment: NO
herb demographic mortality as tree/shrub cohorts: NO
```

Hence MEDFATE has a physically meaningful **herb physiological layer**, but not a complete herb population-demography layer.

For Gounsa this is more serious than previously thought because early postfire herb colonisation, dieback and replacement can directly control erosion resistance.

---

# 5. woody daily response
MEDFATE's `growth_day_c.cpp` does update woody plant structure and fine-root state daily and contains daily mortality logic for trees and dynamic shrubs.

Source outputs include:
- FineRootBiomass
- FineRootArea
- fine-root area growth per day
- sapwood/leaf growth
- DBH / height
- rhizosphere/root hydraulic conductance

This gives MEDFATE an important advantage over LPJ-GUESS for immediate woody physiological response after a storm, even though herb demography remains incomplete.

---

# 6. event coupling architecture
MEDFATE/medfateland remains the easiest of the top candidates for explicit day-by-day coupling.

A plausible Gounsa loop is:
```text
hourly/event geomorph-hydrology
 -> aggregate hydrologic state to vegetation cell
 -> if soil geometry changed: conservative remapper
 -> MEDFATE one-day growth/water call
 -> update tree/shrub/herb physiology
 -> return roots, litter, LAI, biomass
 -> next event/day
```

Because state objects are ordinary R/Rcpp data structures, inspection and controlled mutation are much easier than in FATES/ELM.

---

# 7. direct missing module if MEDFATE is selected
The missing biology is now precisely defined.

Needed herb extension:
```text
species-specific herb seed bank
 -> dispersal / local seed rain
 -> germination environmental filter
 -> recruit herbData row/cohort
 -> herb density/cover/biomass dynamics
 -> mortality / disappearance
```

Existing MEDFATE code can then handle:
- daily water/carbon physiology
- root profiles
- competition for water/light to the extent represented

This is still smaller than writing an entire vegetation model, but it is no longer just a tiny recruitment helper; a **complete herb demographic lifecycle** must be added and validated.

---

# 8. 10–25 m resolution
No code-level minimum cell-size restriction was identified.

Cell-count scaling relative to a 200 m application:
- 25 m: 64× more cells per unit area
- 10 m: 400× more cells per unit area

Recommended benchmark sequence:
1. 25 m vegetation grid
2. 10 m only on small subcatchment
3. 1–5 m geomorph grid remains separate
4. adopt finer vegetation grid only if results materially change

---

# 9. five-criteria verdict after source audit
| criterion | verdict |
|---|---|
| 1 spatial cohort | **STRONG**: actual GIS cells + tree/shrub cohorts, no individual-tree burden |
| 2 explicit understory succession | **STRONG for shrubs, PARTIAL/WEAK for herb demography** |
| 3 soil/root coupling | **VERY STRONG external interface; custom conservative layer remap needed** |
| 4 watershed/topography | **STRONG**: lateral surface/subsurface/groundwater/channel framework |
| 5 <=daily | **STRONG for physiology and woody dynamics; herb population dynamics absent** |

---

# current role
**Most implementation-friendly top-tier candidate, but biologically incomplete for early herb succession.**

Compared with LPJ-GUESS SEC:
- easier actual-GIS daily coupling
- daily woody structural/mortality response is more direct
- weaker canopy-gap structure
- herb recruitment/mortality missing

Compared with FATES:
- dramatically easier software/control path
- actual geographic cells are native and transparent
- much weaker herb demographic completeness and less mechanistic full-plant hydraulics

Compared with JULES-RED:
- much stronger cohort/root geometry and cell-specific soil representation
- easier geomorphic layer manipulation
- less complete tree/shrub/grass demographic symmetry

Current decision tradeoff:
```text
MEDFATE
= easiest geomorphic engineering
+ daily woody/root response
- must build and validate full herb demographic lifecycle

FATES
= strongest ready biology
+ daily demography
+ strongest hydraulics
- hardest engineering stack

LPJ-GUESS SEC
= best persistent canopy-gap cohort architecture
- annual allocation/mortality requires explicit event damage hook
- branch integration work
```

## key references
- De Cáceres et al. 2023, GMD 16:3165–3201. DOI 10.5194/gmd-16-3165-2023
- Balaguer-Romano et al. 2025, Journal of Environmental Management 395:127844. DOI 10.1016/j.jenvman.2025.127844
- emf-creaf/medfate source audit, 2026-09-23
- medfateland current documentation/source, 2026
