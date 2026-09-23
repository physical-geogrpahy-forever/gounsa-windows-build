# JULES-RED model lineage

업데이트: 2026-09-23, public-documentation correction 포함

## 현재 판정
JULES + Robust Ecosystem Demography (RED)는 경량 demographic land-surface model로서 비교가치가 높다.

핵심 조합:
```text
PFT mass-class demography
+ tree / shrub / grass succession
+ subhourly JULES physiology and soil hydrology
+ catchment/TOPMODEL/routing lineage
+ layer-wise prescribed soil-water state
+ root biomass and root-litter outputs
```

그러나 고운사에서는 다음 세 가지 때문에 LPJ-SEC, FATES, MEDFATE보다 우선순위가 낮다.
1. standard soil layer thickness와 total soil depth가 domain 전체에서 동일
2. root architecture가 PFT-level prescribed exponential profile 중심
3. canopy/understory competition이 SEC/PPA/FATES보다 단순

---

# 1. 공개버전 정정
이 파일의 이전 버전은 `JULES v8.1`이라고 적었으나 2026-09-23 현재 공개 JULES documentation의 `Latest` user guide는 **v7.9**로 확인된다.

따라서 별도의 확실한 source가 없는 한 이후 고운사 검토에서는 **public JULES v7.9 documentation**을 기준으로 한다.

RED는 v7.9 public guide의 `JULES_RED` / `RED_PARMS`에 정식 포함되어 있다.

---

# 2. cohort structure
RED represents each PFT as a number-density distribution over plant mass.

Public v7.9 `RED_PARMS` exposes:
- `mclass`: number of mass classes
- `mass0`: lowest mass class
- `massi`: highest mass class
- `height0`
- `crwn_area0`
- `alpha_recrt`: assimilate allocation to reproduction
- `mort_base`: baseline mortality
- allometric exponents `phi_a`, `phi_g`, `phi_h`, `phi_l`
- `dom_order`: PFT competition hierarchy

The original RED v1 numerical experiments used approximately:
- tree PFTs: 10 mass classes
- shrub PFTs: 8 mass classes
- grass PFTs: 1 class

Thus RED is a true size/mass demographic model for woody vegetation, while grass remains much more aggregated.

RED does not retain individual plant x-y coordinates or geographic disturbance patches inside a cell.

Criterion 1:
**PARTIAL-STRONG**

---

# 3. understory and succession
RED explicitly represents:
```text
net assimilate
 -> reproductive allocation
 -> influx into lowest mass class
 -> competition/gap-limited establishment
 -> growth through mass classes
 -> mortality
```

Public v7.9 documentation confirms `dom_order`:
```text
3 = tree
2 = shrub
1 = grass
```

RED v1 bare-ground experiments showed the qualitative sequence:
```text
early grass
 -> shrub dominance
 -> tree dominance
```

This is biologically close to the broad postfire trajectory required at Gounsa.

Important limitation:
- competition is deliberately parsimonious
- no SEC-style persistent x-y canopy gaps
- no detailed PPA multilayer demographic canopy
- hierarchy acts primarily on establishment/gap access

Criterion 2:
**STRONG but simplified**

---

# 4. time structure
JULES fast land-surface processes can operate at subhourly/half-hourly timesteps.

Recent JULES-RED application evidence, Chou et al. 2025 preprint and author response:
- carbon/water fluxes: half-hourly
- vegetation dynamics: daily

The original RED v1 idealised experiments used a coarser demographic step; therefore original RED benchmark settings and recent JULES-RED application settings must not be conflated.

Criterion 5:
**STRONG for current application precedent**

---

# 5. external soil-water state coupling
Public v7.9 `JULES_PRESCRIBED` explicitly supports `sthuf`:
- soil wetness for every soil layer
- can be prescribed at the beginning of each model timestep
- state is then allowed to evolve during that timestep

Initial conditions likewise expose layer-wise `sthuf` and, with TOPMODEL, water-table state such as `zw`.

Therefore an external Gounsa hydrology engine could drive JULES through time-varying layer soil-water states.

Criterion 3A, external water-state injection:
**STRONG**

---

# 6. decisive soil-depth limitation
Public v7.9 `JULES_SOIL`:
- `sm_levels` controls number of soil layers
- `dzsoil_io` controls layer thicknesses
- documentation explicitly states that layer depths and therefore total soil depth are **constant across the domain**

Typical recommended profile is:
```text
0.10 m
0.25 m
0.65 m
2.00 m
= 3.0 m total
```

This is a major mismatch with Gounsa where shallow regolith/soil depth may vary strongly from cell to cell and may be modified by erosion/deposition.

A source-code extension, domain splitting, or external state abstraction would be required for literal dynamic cell-specific layer geometry.

Criterion 3B, geomorphic soil geometry:
**WEAK / CUSTOM**

---

# 7. roots and litter
Public JULES PFT parameters include `rootd_ft_io`.

Recommended water-stress mode:
- calculates stress in each soil layer
- weights layers using root fractions
- assumes an exponential root distribution
- `rootd_ft_io` is the e-folding depth

Alternative mode uses `rootd_ft_io` as total root-zone depth.

This is simple and robust but root architecture is much more prescribed/static than:
- MEDFATE woody seedling daily root-depth development
- FATES cohort hydraulics/root-layer machinery

Public outputs include:
- `rootC`: PFT root carbon biomass
- `root_litC`: root-turnover litter C
- soil water extraction diagnostics

For Gounsa one can derive a layer root-mass estimate from:
```text
rootC
+ root depth profile
```

but this is still a derived coupling, not a native geomorphic root state.

---

# 8. dynamic erosion/deposition coupling
JULES does not natively evolve soil layer geometry from erosion/deposition.

Needed custom event remap:
```text
old/new soil interfaces
 -> remap soil water
 -> remap soil C/N
 -> remove roots in eroded material
 -> recompute surviving root distribution
 -> handle litter/interface pools
 -> continue RED demography
```

This is a **새로운 coupling**.

Because standard `dzsoil_io` is global, this coupling is structurally more invasive than the equivalent operation in MEDFATE and likely more invasive than changing host soil geometry in FATES.

---

# 9. catchment/topography precedent
JULES hydrology has strong catchment precedent independent of RED:
- TOPMODEL saturation-excess runoff
- water-table depth
- surface/subsurface runoff
- subdaily River Flow Model routing
- Great Britain catchment applications at half-hourly land-surface timestep

An idealised groundwater development study also demonstrated fine horizontal resolution hydrology, but this is not the same as a published fine-resolution JULES-RED forest-demography catchment simulation.

Criterion 4:
**STRONG lineage precedent / direct RED precedent limited**

---

# 10. field evidence
Argles et al. 2023 applied JULES-RED to Harwood Forest, Northumberland:
- managed upland Sitka spruce plantation
- observed tree size structure mapped to RED mass classes
- forest growth and demographic structure evaluated
- thinning represented through size-structured removal

This proves RED mass classes are usable beyond idealised global simulations.

It does not validate multi-PFT postfire herb-shrub-tree succession in a Korean mountain forest.

---

# 11. five-criteria verdict after source/documentation correction
| Criterion | Verdict | Main reason |
|---|---|---|
| 1 spatial cohort | PARTIAL-STRONG | geographic grid + woody mass classes; no internal x-y cohort positions |
| 2 understory succession | STRONG-SIMPLIFIED | tree/shrub/grass hierarchy and recruitment, but simplified light competition |
| 3 soil/geomorph coupling | water STRONG, geometry WEAK/CUSTOM | `sthuf` prescribable; `dzsoil_io` fixed across domain |
| 4 catchment/topography | STRONG lineage | mature JULES hydrology, direct fine RED catchment validation limited |
| 5 <= daily | STRONG | half-hourly fluxes and recent daily vegetation-dynamics application |

---

# current role
**Comparator / lightweight fallback, not current first-choice production engine.**

JULES-RED remains attractive when:
- computational simplicity is prioritized
- tree/shrub/grass broad succession is sufficient
- external soil moisture forcing is more important than explicit shallow-soil geometry

It is less attractive at Gounsa because:
1. very shallow, spatially heterogeneous soil depth is central
2. root-depth response is comparatively simple/static
3. canopy-gap/understory competition is less explicit than LPJ-SEC or FATES

Current higher-priority implementation paths:
1. LPJ-GUESS SEC/PPA + PF-LPJG style external hydrology
2. FATES + ELM/ParFlow
3. MEDFATE + medfateland + herb-recruitment extension

JULES-RED remains the parsimonious fallback.

## key references
- Argles, A. P. K. et al. (2020). Robust Ecosystem Demography (RED version 1.0). Geoscientific Model Development, 13, 4067-4089. DOI 10.5194/gmd-13-4067-2020.
- Argles et al. (2023). Scientific Reports 13, 13487. DOI 10.1038/s41598-023-39810-2.
- Martínez-de la Torre et al. (2019). GMD 12, 765-784. DOI 10.5194/gmd-12-765-2019.
- Chou et al. (2025). EGUsphere 2025-4536 preprint and author response.
- JULES public v7.9 User Guide, accessed 2026-09-23: `JULES_RED`, `JULES_SOIL`, `JULES_PRESCRIBED`, `JULES_PFTPARM`, output variables.
