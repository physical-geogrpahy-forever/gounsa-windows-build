# FATES model lineage

업데이트: 2026-09-23 deep source audit

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

Current default parameter file inspected on 2026-09-23 contains 14 PFTs, including:
- extratropical evergreen / hydrodeciduous / cold-deciduous shrubs
- arctic evergreen / cold-deciduous shrubs
- arctic C3 grass
- cool C3 grass
- C4 grass

Therefore shrub/grass life forms are native current PFTs, not inferred surrogates.

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

### Seed bank and recruitment
FATES contains PFT-specific seed production, seed pools/banks, germination and decay.
Source audit confirms `EDPhysiologyMod.F90` releases reproductive carbon to seed production and maintains germination pools used by recruitment.

Current code also contains explicit PFT-level inter-grid seed-dispersal parameters:
- `fates_seed_dispersal_fraction`
- `fates_seed_dispersal_max_dist`
- dispersal PDF scale/shape parameters

The parameter description explicitly states that the dispersal fraction is the fraction of seed rain dispersed to other grid cells.

Therefore the spatial limitation must be stated precisely:
```text
seed movement between host grid cells: YES
internal x-y position of FATES disturbance patches/cohorts: NO
```

The newer environmentally sensitive Tree Recruitment Scheme (TRS), including explicit forest-floor seedling emergence, seedling mortality and transition to sapling cohorts, is currently best documented for trees.

Correct interpretation:
```text
tree/shrub/grass PFTs + generic demographic recruitment
= YES

detailed environmentally sensitive seedling microenvironment
= currently strongest/documented for trees
```

## roots and litter
Cohort state includes fine-root carbon.
FATES explicitly tracks:
- leaf litter
- fine-root litter
- aboveground CWD
- belowground CWD

Root litter receives both root turnover and cohort mortality fluxes.

### source-level root profile audit
Current source uses `set_root_fraction()` in `FatesAllometryMod.F90` as the central normalized vertical root-profile routine.
The function is called from physiology, mortality, patch/cohort dynamics and soil-BGC pathways.

Important host interface:
```text
set_root_fraction(..., site%zi_soil, bc_in%max_rooting_depth_index_col)
```

Thus the host land model provides:
- actual soil-layer interfaces `zi_soil`
- the maximum soil/rooting layer allowed for the column

This is substantially useful for shallow soil/bedrock applications because roots can be prevented from occupying layers below the active soil column.

PFT root profile parameters include at least:
- `roota_par`
- `rootb_par`

so vertical shape is PFT parameterized.

### important geomorphic limitation
`set_root_fraction` recalculates a normalized root-depth distribution constrained by the available column. This does **not** by itself mean that erosion physically removes live root biomass.

For Gounsa:
```text
soil depth decreases
 -> allowed root profile becomes shallower
```
is native-compatible, but:
```text
eroded soil volume
 -> root biomass physically exported/killed
```
remains a new event-remapping rule.

This distinction is critical. After erosion, simply renormalizing all surviving fine-root C into a shallower profile would conserve plant root biomass unrealistically.

Required Gounsa rule:
1. determine fraction/mass of roots located in removed soil volume,
2. subtract that mass from live fine-root pool,
3. route removed/dead root C/N to sediment export or detrital pools,
4. then recalculate the surviving normalized profile using the new rooting-depth index.

## FATES-HYDRO
FATES-HYDRO resolves water transport through:
- rhizosphere
- absorbing root
- transporting root
- stem
- leaf

Absorbing roots are discretized by soil layer. Conductance depends on root biomass and root traits such as specific root length.
This makes FATES stronger than simple root-depth weighting models for plant hydraulics.

However, this sophistication increases state-remapping complexity after erosion/deposition because hydraulic organ/root state must remain consistent with changed soil geometry.

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

Coupling architecture:
```text
ParFlow -> soil moisture -> ELM -> FATES
FATES -> root water extraction -> ELM -> ParFlow
```

FATES does not communicate directly with ParFlow; the host ELM mediates state exchange.

This proves that a vegetation-demography cohort engine can be driven by explicit hillslope hydrology and actual terrain on subdaily/daily timesteps.

Important distinction:
- ELM/ParFlow columns are geographically explicit.
- FATES disturbance patches within a column remain spatially implicit and have no x-y location.
Thus a FATES patch cannot be identified with a specific rill, hollow or depositional subpixel.

## persistent single-patch option for Gounsa
A source/documentation audit materially reduces the practical severity of the internal-patch limitation for this specific project.

FATES exposes `mortality_disturbance_fraction`, defined as the fraction of canopy mortality that creates new disturbance area. In the mortality code the ordinary within-patch mortality term is multiplied by `(1 - mortality_disturbance_fraction)`, while the disturbance-rate contribution that drives patch fission is multiplied by `mortality_disturbance_fraction`.

Therefore, if:
- `mortality_disturbance_fraction = 0`,
- future fire-driven patch creation is disabled for a postfire-recovery experiment,
- land-use disturbance is disabled,

then ordinary cohort mortality can continue without generating new disturbance-history patches.

Recruitment is a separate demographic process. FATES retains PFT-specific seed banks, germination, recruit state and newly created cohorts independently of mortality-driven patch fission.

For Gounsa this supports:
```text
1 GIS vegetation cell
 -> 1 host column/site
 -> approximately 1 persistent FATES patch
 -> multiple tree/shrub/grass cohorts inside that patch
 -> PPA canopy/understory competition
 -> PFT seed bank and recruitment
 -> growth and mortality
```

This is especially defensible if the observed wildfire is the initial disturbance and the following 100-year recovery is simulated without another landscape fire.

Important caveats:
- project-specific configuration, not a published Gounsa implementation
- internal horizontal locations of cohorts still do not exist
- PPA represents canopy/understory competition statistically inside the cell
- future patch-creating disturbances restore the spatially implicit patch issue

## restart/event coupling
FATES and host models have full restart-state infrastructure.
This is useful for:
```text
storm
 -> geomorphic state change
 -> restart/state modification
 -> continue vegetation physiology
```

But changing soil geometry and conservatively remapping water/C/N/root/hydraulic state at arbitrary erosion/deposition events is still **new coupling**.

## spatial limitation
FATES disturbance patches are spatially implicit area fractions and have no x-y coordinate.
Therefore real geography must be represented by host grid/column locations.

Grid-cell seed dispersal exists, but that does not convert internal FATES patches into geographic subcells.

## implementation complexity
This remains the largest disadvantage.
FATES normally runs through CTSM/CLM or ELM/E3SM. Adding ParFlow creates a large Fortran/C++/MPI host stack.

Compared with LPJ-GUESS SEC:
- FATES biology/hydraulics is more integrated and current source is openly inspectable.
- LPJ-GUESS SEC is substantially lighter conceptually and has persistent within-patch gap positions.

Compared with MEDFATE:
- FATES herb/shrub/tree demographic symmetry is much stronger.
- MEDFATE is far easier to control as a daily GIS-cell event loop.

## five-criteria status for Gounsa
1. spatially explicit cohort structure: **PARTIAL natively; STRONGER PARTIAL in persistent-single-patch GIS-cell configuration**
2. explicit understory and succession: **VERY STRONG**
   - current tree/shrub/grass PFT set
   - PFT seed bank/recruitment
   - grid-cell seed dispersal
   - actual grass demographic application
3. soil depth / water storage / multilayer hydrology: **VERY STRONG**, especially with FATES-HYDRO and host rooting-depth limit
4. watershed / hillslope / topography precedent: **STRONG**
5. <= daily, preferably hourly: **STRONG**
   - half-hourly biophysics and daily demography

## current verdict
**Scientifically the strongest ready integrated demographic candidate, but technically the heaviest.**

Its relative standing after source audit:
- stronger than LPJ-GUESS on ready-made shrub/grass demographic symmetry and plant hydraulics
- weaker than LPJ-GUESS SEC on persistent explicit canopy-gap geography within the vegetation unit
- stronger than MEDFATE on herb recruitment
- much harder than MEDFATE to prototype and couple to a custom geomorphic engine
- root-depth restriction is cleaner for shallow bedrock than LPJ-GUESS-RE's bottom-layer root accumulation, but physical root loss after erosion is still custom

For a production choice, FATES should remain one of two primary biological engines to prototype alongside LPJ-GUESS SEC.

## related papers
- `papers/2022_Fang_FATES_ParFlow_Topography.md`
- `papers/2025_Gao_FATES_AnnualGrass.md`
- `papers/2025_EckesShephard_DemographyModels.md`

## key external references
- Fang et al. (2022), GMD 15:7879-7902, ELM-FATES-ParFlow hillslope coupling.
- Xu et al. (2023), GMD 16:6267-6286, FATES-HYDRO V1.0.
- Gao et al. (2025), New Phytologist 245:2480-2495. DOI 10.1111/nph.20421.
- Shuman et al. (2024), GMD 17:4643-4670, FATES-SPITFIRE.
- NGEET/fates source audit, current main branch, 2026-09-23.
