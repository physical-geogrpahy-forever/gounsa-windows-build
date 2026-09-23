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
Current default PFT framework includes:
- multiple tree PFTs
- multiple extratropical shrub PFTs
- C3/C4 grass PFTs

PPA canopy structure identifies upper-canopy and understory cohorts. FATES is not restricted to woody vegetation.

### 2025 grass-demography audit
Gao et al. (2025) is direct evidence that grass is a **demographic PFT**, not prescribed ground cover.

In CLM-FATES annual-grass simulations:
- model started from bare ground
- grass plants recruited repeatedly from seed
- cohorts grew under PFT-specific allometry
- light/space/water competition affected grass structure
- drought-deciduous phenology and drought-driven mortality changed population size and biomass
- mortality/recruitment fed litter and fuel dynamics
- fire interacted with live grass and litter fuel

Therefore criterion 2 must treat FATES grass dynamics as genuine vegetation demography.

### Seed bank and recruitment nuance
FATES technical documentation describes a **PFT-specific seed bank** for each patch, with seed production, germination and decay. This generic seed-bank structure applies across PFTs.

However, the newer environmentally sensitive Tree Recruitment Scheme (TRS), including explicit forest-floor seedling emergence, seedling mortality and transition to sapling cohorts, is currently documented specifically as a **tree recruitment** module.

Correct interpretation:
```text
tree/shrub/grass PFTs + generic demographic recruitment
= YES

detailed environmentally sensitive seedling microenvironment
= currently strongest/documented for trees
```

Thus FATES is substantially stronger biologically than models where herbs are only cover or biomass pools, while herb/shrub early-recruitment ecology is still less mature than the tree implementation.

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

Shuman et al. (2024) demonstrated dynamic ecosystem assembly and tree-grass feedback under FATES-SPITFIRE. Fire mortality is size/PFT dependent for woody vegetation. Current grass implementation does not impose the same direct fire-kill pathway used for woody plants; combustion of aboveground grass biomass and subsequent carbon starvation can nevertheless affect grass state.

## succession
Growth, recruitment, mortality, competition for light/water/nutrients, seed state and disturbance produce succession.
Post-disturbance grass/open-canopy phases are therefore mechanistically possible rather than imposed land-cover classes.

Important caveat for Gounsa:
- simultaneous tree/shrub/grass PFTs are supported by the parameter system
- but a published Korean/temperate postfire application validating the full herb -> shrub -> tree trajectory has not been identified
- Korea-specific PFT/species calibration remains necessary

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
```text
storm
 -> geomorphic state change
 -> restart/state modification
 -> continue vegetation physiology
```

However practical support for changing soil geometry and conservatively remapping carbon/water/root pools at arbitrary erosion/deposition events still needs implementation testing and would be a **새로운 coupling**.

## spatial limitation
FATES disturbance patches are spatially implicit area fractions and have no x-y coordinate. FATES technical documentation explicitly notes that the notional patch area does not represent a meaningful internal spatial dimension.

Therefore a Gounsa coupling must use host-model grid/column locations as the real GIS unit. Internal patches cannot be directly mapped onto specific fine geomorphic pixels.

## implementation complexity
This is the largest disadvantage.
FATES does not normally run as a small standalone forest executable; it is embedded in CTSM/CLM or ELM. Adding ParFlow further increases infrastructure and computational complexity.

## five-criteria status for Gounsa
1. spatially explicit cohort structure: **PARTIAL**
   - actual host grid is explicit
   - internal disturbance patches are spatially implicit
2. explicit understory and succession: **STRONG**
   - tree/shrub/grass PFTs
   - PFT seed bank/recruitment
   - actual grass demographic application exists
   - detailed TRS seedling microenvironment remains tree-focused
3. soil depth / water storage / multilayer hydrology: **STRONG**
4. watershed / hillslope / topography precedent: **STRONG**
5. <= daily, preferably hourly: **STRONG**
   - half-hourly biophysics and daily demography

## current verdict
**Ecologically and temporally the strongest ready demographic-cohort candidate with a published hillslope hydrology coupling, but spatial interpretation is imperfect and implementation is heavy.**

Strengths:
- tree/shrub/grass
- actual grass demographic recruitment/growth/mortality
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
- full temperate postfire herb-shrub-tree succession has not been specifically validated

## related papers
- `papers/2022_Fang_FATES_ParFlow_Topography.md`
- `papers/2025_Gao_FATES_AnnualGrass.md`
- `papers/2025_EckesShephard_DemographyModels.md`

## key external references
- Gao et al. (2025), New Phytologist 245:2480–2495. DOI 10.1111/nph.20421
- Shuman et al. (2024), GMD 17:4643–4670, FATES-SPITFIRE ecosystem assembly.
- FATES technical documentation, seed dynamics and recruitment sections.
