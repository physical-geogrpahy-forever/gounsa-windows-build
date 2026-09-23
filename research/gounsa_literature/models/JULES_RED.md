# JULES-RED model lineage

업데이트: 2026-09-23 source-level audit 포함

## 현재 판정
JULES + Robust Ecosystem Demography (RED)는 경량 demographic land-surface model로서 비교가치가 높다.

핵심 조합:
```text
PFT mass-class demography
+ tree / shrub / grass succession
+ subhourly JULES physiology and soil hydrology
+ daily RED demography in current source path
+ catchment/TOPMODEL/routing lineage
+ layer-wise prescribed soil-water state
+ root biomass and root-litter outputs
```

그러나 고운사에서는 다음 세 가지 때문에 LPJ-SEC, FATES, MEDFATE보다 우선순위가 낮다.
1. standard soil layer thickness와 total soil depth가 domain 전체에서 동일
2. root architecture가 PFT-level prescribed exponential profile 중심
3. canopy/understory competition이 SEC/PPA/FATES보다 단순

---

# 1. current public source
2026-09-23 source audit used the public `MetOffice/jules` repository.
RED is implemented as a normal JULES science component, including:
- `src/science/params/red_io_mod.F90`
- `src/science/vegetation/veg3_red_dynamic_mod.F90`
- `src/science/params/veg3_param_mod.F90`
- host control path in `src/control/shared/next_gen_biogeochem_mod.F90`

This matters because RED is no longer just a theory paper implementation; its demographic state and call path are visible in the maintained JULES source tree.

---

# 2. cohort structure
RED represents each PFT as a number-density distribution over plant mass.

Current source/parameters expose:
- `mclass`: number of mass classes
- `mass0`: lowest mass class
- `massi`: highest mass class
- `height0`
- `crwn_area0`
- `alpha_recrt`: assimilate allocation to reproduction
- `mort_base`: baseline mortality
- allometric exponents
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

# 3. source-level demography
Current `veg3_red_dynamic_mod.F90` confirms the full demographic flux calculation.

For each PFT and mass class the code computes:
- total assimilate
- reproductive allocation `P_s`
- structural-growth allocation `g`
- individual mass-class growth `g_mass`
- seedling influx into the first mass class
- flux between adjacent mass classes
- baseline + additional mortality
- updated plant number density
- demographic litter

Seedling influx is explicitly:
```text
reproductive assimilate
 / first-class plant mass
 * (1 - shading fraction)
```

Growth out of a class becomes the input flux to the next class.
Therefore RED genuinely moves populations through mass classes rather than simply relabelling vegetation fractions.

---

# 4. understory and succession
RED competition is deliberately parsimonious.

`dom_order` separates broad life forms:
```text
3 = tree
2 = shrub
1 = grass
```

Current demographic code calculates a PFT-specific seedling shading fraction from existing PFT fractional cover and a competition coefficient matrix.
Only successful recruitment enters the smallest mass class.

RED v1 bare-ground experiments showed the qualitative sequence:
```text
early grass
 -> shrub dominance
 -> tree dominance
```

This is biologically close to the broad postfire trajectory required at Gounsa.

Important limitation:
- no SEC-style persistent x-y canopy gaps
- no FATES/PPA-style explicit multilayer cohort canopy
- competition is mainly a gap/shading filter on seedling establishment
- grass has only one demographic mass class in the standard RED design

Criterion 2:
**STRONG but simplified**

---

# 5. time structure: source-level correction
This is stronger than previously inferred from configuration alone.

In current `next_gen_biogeochem_mod.F90`, the RED dynamics call passes:
```text
CALL veg3_red_dynamic(..., rsec_per_day, ...)
```

Inside `veg3_red_dynamic`, changes in plant number density are multiplied by `dt` directly.

Therefore the current next-generation JULES vegetation path implements **one-day RED demographic updates** at source level, not merely a theoretical ability to choose daily updates.

Fast land-surface water, energy and carbon fluxes remain subdaily/half-hourly class.

Criterion 5:
**VERY STRONG**

---

# 6. external soil-water state coupling
JULES prescribed-data infrastructure supports layer-wise soil wetness state.
Initial/restart states also expose layered soil-water variables and TOPMODEL water-table state.

Therefore an external Gounsa hydrology engine can in principle own the hydrologic state and prescribe/update JULES soil wetness.

Criterion 3A:
**STRONG**

---

# 7. decisive soil-depth limitation
Current JULES soil structure stores:
```text
dzsoil(:)
= thickness of soil layers
```

Standard JULES configuration treats this as the common soil-layer geometry rather than a freely changing geometry for each fine terrain cell during a run.

This is a major mismatch with Gounsa where:
- soil depth is spatially heterogeneous
- erosion/deposition can change active soil depth through time

Literal storm-driven cell-specific layer geometry therefore requires a source extension, separate domains/configurations, or an external abstraction.

Criterion 3B:
**WEAK / CUSTOM**

---

# 8. roots: source-level limitation
This is the most important reason JULES-RED remains below FATES/MEDFATE for Gounsa geomorphic coupling.

JULES uses PFT parameter `rootd_ft_io` for root-depth weighting.
The recommended soil-moisture-stress mode calculates stress in each layer and weights it using an exponential PFT root fraction profile.

Current RED/JULES state reconstructs total vegetation carbon from the mass-class number-density distribution, but then derives:
```text
leafC(PFT)
rootC(PFT)
woodC(PFT)
```
at the PFT aggregate level.

Source inspection shows `rootC` is calculated as a PFT-level carbon pool, not retained separately for each RED mass class.

Therefore:
```text
RED woody size distribution
 -> detailed mass classes

root biomass
 -> PFT aggregate rootC
 -> prescribed PFT depth profile
```

This loses cohort-size information exactly at the root interface.

For Gounsa erosion/slope-process coupling, layer root mass would need to be reconstructed as:
```text
PFT rootC
* exponential layer root fraction
```

rather than read as a native cohort-by-layer root state.

By comparison:
- FATES has cohort fine-root state plus layer hydraulic/root-profile machinery
- MEDFATE explicitly carries cohort root-depth distributions including herbs
- LPJ-GUESS can provide PFT/cohort vegetation state but still requires custom layer remapping

---

# 9. dynamic erosion/deposition coupling
JULES does not natively evolve soil geometry from erosion/deposition.

Required new coupling:
```text
old/new soil interfaces
 -> remap soil water
 -> remap soil C/N
 -> estimate roots in removed layer from PFT rootC/profile
 -> remove/export those roots
 -> recompute surviving PFT root profile
 -> continue RED demography
```

Because standard soil geometry is domain-wide and root biomass is PFT-aggregated, this operation is structurally more invasive than the equivalent event remap in MEDFATE and less physically explicit than FATES.

---

# 10. catchment/topography precedent
JULES hydrology has strong catchment precedent independent of RED:
- TOPMODEL saturation-excess runoff
- water-table depth
- surface/subsurface runoff
- river routing
- fine-resolution hydrology experiments

However direct fine-resolution JULES-RED forest-demography catchment validation remains limited.

Criterion 4:
**STRONG lineage precedent / direct RED precedent limited**

---

# 11. field evidence
Argles et al. 2023 applied JULES-RED to Harwood Forest, Northumberland:
- managed upland Sitka spruce plantation
- observed tree size structure mapped to RED mass classes
- forest growth and demographic structure evaluated
- thinning represented through size-structured removal

This proves RED mass classes are usable beyond idealised global simulations.

It does not validate multi-PFT postfire herb-shrub-tree succession in a Korean mountain forest.

---

# 12. five-criteria verdict after source audit
| Criterion | Verdict | Main reason |
|---|---|---|
| 1 spatial cohort | PARTIAL-STRONG | geographic grid + woody mass classes; no internal x-y cohort positions |
| 2 understory succession | STRONG-SIMPLIFIED | tree/shrub/grass recruitment hierarchy; simplified canopy competition |
| 3 soil/geomorph coupling | water STRONG, geometry WEAK/CUSTOM | soil water can be controlled; dynamic cell-specific layer geometry difficult |
| 4 catchment/topography | STRONG lineage | mature JULES hydrology; direct fine RED catchment validation limited |
| 5 <=daily | **VERY STRONG** | current source calls RED dynamics with one-day timestep |

---

# current role
**Lightweight demographic fallback / comparator, not first-choice production engine.**

The source audit improves RED's temporal score but lowers confidence in its root-geomorph interface relative to FATES and MEDFATE.

JULES-RED is attractive if:
- computational simplicity is important
- broad grass -> shrub -> tree succession is sufficient
- daily mass-class demography is desired
- external soil moisture forcing matters more than explicit shallow-soil/root geometry

For Gounsa, higher-priority paths remain:
1. LPJ-GUESS SEC/PPA + external hydrology + custom soil/root remapper
2. FATES + ELM/ParFlow or equivalent host hydrology
3. MEDFATE + medfateland + herb-recruitment extension

JULES-RED remains the parsimonious fallback.

## key references
- Argles et al. (2020). Robust Ecosystem Demography (RED version 1.0). GMD 13:4067-4089. DOI 10.5194/gmd-13-4067-2020.
- Argles et al. (2023). Scientific Reports 13:13487. DOI 10.1038/s41598-023-39810-2.
- MetOffice/jules public source audit, 2026-09-23.
