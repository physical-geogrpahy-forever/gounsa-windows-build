# FATES model lineage

## 성격
Functionally Assembled Terrestrial Ecosystem Simulator.
- cohort-based vegetation demography
- cohorts resolved by PFT and size
- disturbance-history patches
- upper canopy and understory canopy layers
- host land model: CTSM/CLM or ELM/E3SM

## time structure
- land-surface/biophysical exchange: typically half-hourly or subdaily
- cohort NPP and physiology respond at fine temporal resolution
- demographic growth, mortality and recruitment are updated on slower schedules
- disturbance/fire modifies patch/cohort state dynamically

## vegetation and understory
Current PFT framework includes:
- trees
- extratropical shrubs
- C3/C4 grasses

PPA canopy structure identifies upper-canopy and understory cohorts.
Recent grass applications demonstrate full demographic dynamics for annual grasses, not merely prescribed ground cover.

## roots and litter
Cohort state includes fine-root carbon.
FATES explicitly tracks:
- leaf litter
- fine-root litter
- aboveground CWD
- belowground CWD

Root litter receives both root turnover and cohort mortality fluxes.

## fire
SPITFIRE lineage is deeply integrated.
Fuel state includes live grass, leaf litter and CWD classes. Fire affects vegetation mortality and disturbance patches.

## succession
Growth, recruitment, mortality, competition for light/water/nutrients, seed state and disturbance produce succession.
Post-disturbance grass/open-canopy phases occur in recent model intercomparisons and applications.

## restart/event coupling
FATES and host models have full restart-state infrastructure. This is a major advantage for the Gounsa requirement:
```
storm
 -> geomorphic state change
 -> restart/state modification
 -> continue vegetation physiology
```

However practical support for changing soil geometry and remapping carbon/water pools at arbitrary event times still needs implementation testing.

## spatial limitation
FATES disturbance patches are spatially implicit area fractions and have no x-y coordinate.

Therefore a geomorph coupling must use host-model grid/column locations as the real GIS unit. Internal FATES patches cannot be equated with specific rills, hollows or depositional pixels.

## implementation complexity
This is the largest disadvantage.
FATES does not normally run as a small standalone forest executable; it is an external module embedded in CTSM/CLM or ELM.

For Gounsa this means substantially more infrastructure than BiomeE/BiomeEP or NECN.

## current verdict
**Ecologically the most complete cohort candidate, technically one of the heaviest.**

Strengths:
- tree/shrub/grass
- explicit understory canopy
- fine roots and root litter
- CWD
- fire
- succession
- subdaily physiology
- robust restart infrastructure

Weaknesses:
- spatially implicit internal patches
- heavy host-model stack
- substantial customization needed for event-driven soil-depth changes

## related papers
- `papers/2025_Gao_FATES_GrassFire.md`
- `papers/2025_EckesShephard_DemographyModels.md`
