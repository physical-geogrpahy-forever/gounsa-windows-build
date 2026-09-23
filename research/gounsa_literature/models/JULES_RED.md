# JULES-RED model lineage

업데이트: 2026-09-23

## 현재 판정
JULES + Robust Ecosystem Demography (RED)는 고운사 5조건을 다시 적용했을 때 새로 **top-tier shortlist에 들어갈 가치가 있는 simplified demographic land-surface model**이다.

핵심 장점은 다음 조합이다.

```text
PFT mass-class demography
+ tree / shrub / grass succession
+ subhourly JULES physiology and soil hydrology
+ TOPMODEL / river-routing catchment precedent
+ direct layer-wise soil-moisture prescription/restart capability
+ root biomass and root litter outputs
```

그러나 RED의 understory/light competition은 FATES 또는 LPJ-GUESS SEC/PPA보다 단순하다. 경쟁은 주로 seedling recruitment에 사용되는 gap fraction과 `tree > shrub > grass` dominance hierarchy로 계산되며, explicit 3-D/within-cell canopy positions나 PPA understory layers는 없다.

---

# 1. cohort structure
RED represents each PFT as a number-density distribution over plant mass.

Current JULES v8.1 `RED_PARMS` exposes per-PFT:
- `mclass`: number of mass classes
- `mass0`: lowest mass class
- `massi`: highest mass class
- `height0`
- `crwn_area0`
- allometric exponents for mass -> crown area / height / LAI / growth
- baseline mortality
- reproductive allocation `alpha_recrt`

The original RED v1 numerical experiments used:
- 10 mass classes for tree PFTs
- 8 mass classes for shrub PFTs
- 1 mass class for grass PFTs

Thus RED is a true size/mass cohort model for woody vegetation, while grass remains a single demographic class.

RED does not retain individual x-y plant positions or disturbance-patch age.

Criterion 1:
**PARTIAL-STRONG.**
- geographic JULES grid boxes are explicit
- demographic mass classes exist inside each grid box
- within-cell cohort positions are not explicit

---

# 2. understory and succession
This is considerably stronger than ordinary TRIFFID.

RED v1 explicitly models:
```text
net assimilate
 -> fraction to seed production
 -> seedling influx into lowest mass class
 -> gap-limited establishment
 -> growth through mass classes
 -> mortality
```

Competition is implemented using a functional-group hierarchy:
```text
tree > shrub > grass
```

Current JULES v8.1 `dom_order` documentation explicitly defines:
- 3 = trees
- 2 = shrubs
- 1 = grass

The RED model paper demonstrated a bare-soil succession experiment in which:
1. fast grass PFTs dominate early,
2. evergreen shrubs replace grasses by shading grass seedlings,
3. broadleaf trees subsequently replace much of shrub and grass vegetation.

Vegetation fractional cover approached its steady state in about 20 years in that idealized experiment, while full biomass equilibration took much longer.

This is unusually close to the biological trajectory required for Gounsa postfire recovery.

### Important limitation
Competition is deliberately parsimonious.
- only the lowest/seedling mass class is directly subject to gap competition
- tree/shrub/grass hierarchy determines which existing vegetation excludes seedlings
- there is no explicit x-y crown geometry
- there is no PPA-style multilayer canopy/understory demographic light solver
- within each co-competing class RED v1 tends toward competitive exclusion of subdominant PFTs unless parameterization is modified

Therefore criterion 2 is:
**STRONG, but less structurally explicit than FATES or LPJ-GUESS SEC/PPA.**

---

# 3. soil-topography / geomorph coupling readiness

## 3A external soil-water state coupling: STRONG
JULES v8.1 has mature layered soil-water state variables and allows direct prescribed soil wetness.

Important interfaces:
- `sthuf`: unfrozen soil wetness for each soil layer
- prescribed-data interface can prescribe `sthuf` through time for selected/all soil levels
- restart/initial-condition files can set layer-wise soil wetness and temperature
- TOPMODEL configuration adds `zw` water-table depth and deep-layer wetness
- soil hydraulic properties can vary spatially and vertically through ancillary data

Vegetation water stress can use:
- layer-wise soil water
- weighted root distribution
- field-capacity / wilting-point-type thresholds (`sm_crit`, `sm_wilt`)
- optionally soil water potential and PFT-specific opening/closing potentials

Thus an external Gounsa hydrology/geomorph engine can, in principle, drive JULES-RED vegetation by updating/prescribing layer soil-water states at daily or finer synchronization points.

## Native soil limitation
`dzsoil_io`, the soil-layer thickness vector, is normally constant across the domain in standard JULES.

Hence spatially variable shallow bedrock/soil depth is not as naturally represented as in MEDFATE or LPJ-GUESS-RE unless the domain is tiled/split or source code is extended.

## 3B dynamic soil geometry
Storm erosion/deposition changing soil depth and layer geometry is **NEW COUPLING**.

Required remapping would include:
- layer water mass
- soil C/N pools
- root fraction / effective rooting distribution
- litter/interface state
- hydraulic properties if texture/coarse-fragment content changes

Criterion 3 overall:
**STRONG for state exchange, MODERATE for soil geometry.**

---

# 4. catchment / topography precedent
JULES has strong catchment hydrology precedent independent of RED.

Published Great Britain regional/catchment configurations include:
- TOPMODEL saturation-excess runoff
- 50 m source DEM/topographic-index data aggregated to 1 km JULES grids
- explicit water-table depth
- surface and subsurface runoff
- subdaily river-flow routing with the River Flow Model

JULES v8.1 also provides OASIS river-model coupling infrastructure.

Important qualification:
- these are JULES hydrology precedents, not published fine-resolution JULES-RED postfire catchment experiments
- the best published JULES-RED field test identified so far is Harwood Forest, an upland Sitka spruce plantation, not a distributed catchment demography study

Criterion 4:
**STRONG lineage precedent, but direct JULES-RED catchment-demography validation is limited.**

---

# 5. time structure
Current JULES v8.1:
- main land-surface timestep can be seconds-scale; typically 30 or 60 min
- photosynthesis, stomatal conductance, energy and soil-water processes operate on the main timestep
- `triffid_period` is the period for dynamic vegetation calls and is permitted to be >=1 day
- RED is activated only with `l_triffid = TRUE`

RED v1 standalone experiments used a 1-month demographic timestep, but the paper explicitly describes this as a numerical choice and reports robustness when the timestep is short relative to regrowth and mortality timescales.

The current JULES configuration therefore does not impose a one-month lower bound. A daily dynamic-vegetation call is configuration-permitted.

Criterion 5:
**STRONG.**
- subhourly ecophysiology/hydrology
- dynamic vegetation scheduling can be daily
- published RED v1 benchmark used monthly demography, which must be stated separately

---

# 6. roots, litter and geomorphic outputs
JULES v8.1 outputs include:
- `rootC`: PFT root carbon biomass
- `root_litC`: PFT root-turnover litter carbon
- `leafC`, `woodC`, total vegetation C
- `lit_c`, leaf/root/wood litter fluxes
- layer soil-water extraction `ext`
- PFT water-stress factor `fsmc`
- soil moisture by layer
- water-table depth `zw`
- surface/subsurface runoff and baseflow

PFT root depth is controlled by `rootd_ft_io` and can be used as an exponential root-depth distribution for weighting soil moisture uptake.

This provides a direct bridge to Gounsa erosion/root terms:
```text
PFT rootC
+ PFT root-depth function
 -> layer root-mass estimate
 -> root biomass / RLD helper
 -> erosion and slope-process coupling
```

Conversion from carbon mass to physical root mass/RLD remains a documented helper/coupling, not a native JULES geomorph variable.

---

# 7. fire
JULES includes INFERNO and a switch that feeds burnt area into dynamic vegetation.

RED theory allows additional disturbance mortality to be PFT- and mass-class dependent.

However current public documentation does not by itself prove that the full INFERNO -> size-specific RED mortality pathway is production-ready in JULES v8.1. Do not claim this without source/application confirmation.

For the current Gounsa design this is not fatal if the observed wildfire is imposed as the initial disturbance and the model is used primarily for postfire recovery.

---

# 8. actual JULES-RED field application
Argles et al. (2023) applied JULES-RED to Harwood Forest, Northumberland, UK:
- upland Sitka spruce plantation
- stand planted in 1973
- initial tree density 2500 trees ha-1 in historical simulations
- observed 2018 size distribution mapped to RED mass classes in fitted runs
- GPP and forest structure evaluated
- thinning represented as size-structure mortality/removal

This confirms that RED mass classes are usable beyond idealized global DGVM experiments.

But it is a single-PFT managed conifer stand, so it does not validate herb-shrub-tree postfire succession.

---

# 9. spatial-resolution implication for Gounsa
JULES itself can be run for arbitrary grid collections, but most catchment precedents are much coarser than the proposed Gounsa vegetation grid.

No published 10-50 m JULES-RED catchment simulation was identified in this audit.

A plausible test architecture is:
```text
25-50 m vegetation / soil grid
 -> JULES-RED per geographic cell
 -> hourly/subhourly surface physics
 -> daily demographic update

1-5 m geomorph grid
 -> aggregate soil water / erosion / soil-depth state to vegetation grid
 -> disaggregate vegetation root/litter effects back to geomorph grid
```

This remains to be benchmarked computationally and ecologically.

---

# 10. five-criteria verdict
| Criterion | Verdict | Main reason |
|---|---|---|
| 1 spatial cohort | PARTIAL-STRONG | geographic cells + mass cohorts, but no within-cell x-y cohorts |
| 2 explicit understory succession | STRONG | actual grass -> shrub -> tree succession, shrub/tree mass classes, recruitment; simplified gap hierarchy rather than multilayer canopy |
| 3 soil/geomorph coupling readiness | STRONG 3A / CUSTOM 3B | layer soil-water can be prescribed/restarted; layer geometry spatially fixed by default |
| 4 catchment/topography | STRONG lineage precedent | TOPMODEL + subdaily river routing; direct RED catchment application still lacking |
| 5 <=daily | STRONG | 30-60 min LSM, dynamic vegetation call permitted daily; original RED test monthly |

---

# current role
**Promote to top-tier comparison set.**

JULES-RED is especially attractive if the project wants:
- much lighter demography than FATES
- explicit shrubs rather than grass + tree only
- root/litter and hydrology in one mature land-surface model
- hourly water/energy response
- direct external soil-moisture forcing capability

It is less attractive than FATES when the priority is biologically rich seed-bank/cohort ecology and less attractive than LPJ-GUESS SEC/PPA when explicit canopy gaps and woody understory light structure are central.

The most important unresolved items are:
1. practical 10-50 m computational benchmark
2. Korea-specific PFT parameterization
3. current JULES-RED fire coupling
4. dynamic spatially varying soil-depth implementation
5. whether the simplified seedling-gap competition is adequate for the observed Gounsa herb/shrub understory sequence

## key references
- Argles, A. P. K., Moore, J. R., Huntingford, C., Wiltshire, A. J., Harper, A. B., Jones, C. D., & Cox, P. M. (2020). Robust Ecosystem Demography (RED version 1.0): a parsimonious approach to modelling vegetation dynamics in Earth system models. Geoscientific Model Development, 13, 4067-4089. DOI 10.5194/gmd-13-4067-2020.
- Argles, A. P. K. et al. (2023). Modelling the impact of forest management and CO2-fertilisation on growth and demography in a Sitka spruce plantation. Scientific Reports, 13, 13487. DOI 10.1038/s41598-023-39810-2.
- Lewis et al./Blyth et al. JULES Great Britain hydrology lineage; GMD 2019 catchment calibration/application.
- JULES v8.1 User Guide, 2026, `JULES_VEGETATION`, `RED_PARMS`, soil, hydrology, prescribed-data, output-variable documentation.
