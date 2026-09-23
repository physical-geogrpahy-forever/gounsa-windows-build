# FATES model lineage

## 성격
Functionally Assembled Terrestrial Ecosystem Simulator.
- cohort-based vegetation demography
- cohorts resolved by PFT and size
- disturbance-history patches
- upper canopy and understory canopy layers
- host land model: CTSM/CLM or ELM/E3SM

## time structure
- land-surface/biophysical exchange: typically half-hourly
- photosynthesis, respiration, canopy energy and plant-soil hydraulic calculations: subdaily/30 min class
- vegetation growth, mortality, recruitment and disturbance: daily
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
FATES-HYDRO weights belowground conductance by root biomass through soil layers and resolves cohort hydraulic state.

## fire
SPITFIRE lineage is deeply integrated.
Fuel state includes live grass, leaf litter and CWD classes. Fire affects vegetation mortality and disturbance patches.

## succession
Growth, recruitment, mortality, competition for light/water/nutrients, seed state and disturbance produce succession.
Post-disturbance grass/open-canopy phases occur in recent model intercomparisons and applications.

## actual hillslope/topography precedent: ELM-FATES + ParFlow
Fang et al. (2022) coupled ELM-FATES to the 3-D ParFlow hydrology model to simulate topographic control on tropical-forest biomass at Barro Colorado Island.

Key facts:
- actual x-y-z hydrologic domain
- x-y grid resolution 90 m
- 15 vertical ParFlow layers
- 30 m DEM aggregated to 90 m for terrain slopes
- lateral and vertical soil-water redistribution by ParFlow
- ELM-FATES biophysical exchange every half hour
- vegetation dynamics at the end of each day
- soil moisture controls cohort physiology and daily carbon allocation

This proves that a vegetation-demography cohort engine can be driven by explicit hillslope hydrology and actual terrain on subdaily/daily timesteps.

Important distinction:
- ELM/ParFlow columns are geographically explicit.
- FATES disturbance patches within a column remain spatially implicit and have no x-y location.
Thus a FATES patch cannot be identified with a specific rill, hollow or depositional subpixel.

## restart/event coupling
FATES and host models have full restart-state infrastructure. This is a major advantage for the Gounsa requirement:
```
storm
 -> geomorphic state change
 -> restart/state modification
 -> continue vegetation physiology
```

However practical support for changing soil geometry and conservatively remapping carbon/water/root pools at arbitrary erosion/deposition events still needs implementation testing and would be a **new coupling**.

## spatial limitation
FATES disturbance patches are spatially implicit area fractions and have no x-y coordinate.

Therefore a Gounsa coupling must use host-model grid/column locations as the real GIS unit. Internal patches cannot be directly mapped onto specific fine geomorphic pixels.

## implementation complexity
This is the largest disadvantage.
FATES does not normally run as a small standalone forest executable; it is embedded in CTSM/CLM or ELM. Adding ParFlow further increases infrastructure and computational complexity.

## five-criteria status for Gounsa
1. spatially explicit cohort structure: PARTIAL
   - actual host grid is explicit
   - internal disturbance patches are spatially implicit
2. explicit understory and succession: STRONG
3. soil depth / water storage / multilayer hydrology: STRONG
4. watershed / hillslope / topography precedent: STRONG
5. <= daily, preferably hourly: STRONG
   - half-hourly biophysics and daily demography

## current verdict
**Ecologically and temporally the strongest cohort candidate, but spatial interpretation is imperfect and implementation is heavy.**

Strengths:
- tree/shrub/grass
- explicit understory canopy
- fine roots and root litter
- CWD
- fire
- succession
- half-hourly physiology
- daily demography
- demonstrated 3-D hillslope hydrology coupling
- robust restart infrastructure

Weaknesses:
- spatially implicit internal patches
- heavy host-model stack
- event-driven soil-depth changes remain custom state-remapping work
- published hillslope example is 90 m, much coarser than desired Gounsa vegetation cells

## related papers
- `papers/2022_Fang_FATES_ParFlow_Topography.md`
- `papers/2025_Gao_FATES_GrassFire.md`
- `papers/2025_EckesShephard_DemographyModels.md`
