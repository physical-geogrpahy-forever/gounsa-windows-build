# SORTIE-ND model lineage audit

## 현재 버전
- SORTIE-ND 7.06
- released 1 July 2026
- open source core and GUI code are available

## 공간 구조
- individual trees have explicit locations
- arbitrary grids can hold spatial state
- many grid resolutions are configurable
- example Partitioned Biomass grid defaults to 8 m x 8 m but can be changed

## forest dynamics
- seed production/dispersal
- recruitment
- growth
- mortality
- neighbourhood competition
- snags and tree fall
- substrate dynamics

## surface substrate
The Substrate behavior tracks:
- forest floor litter
- forest floor moss
- scarified soil
- tip-up mounds
- decayed logs
- fresh logs

This is useful for geomorphic roughness/storage and recruitment microsites.

## disturbance and fire
SORTIE-ND has an Episodic Mortality behavior that can mimic:
- fire
- insect outbreak
- disease
- other mortality episodes

But this is not a mechanistic wildfire spread/combustion module.
A fire event is prescribed as mortality.

## postfire precedent
Clason et al. 2022 used SORTIE-ND to project observed postfire stands to 100 years since fire.
Ghose et al. 2026 validated fine-scale spatial pattern against a postfire chronosequence.

## biomass and root limitation
SORTIE-ND can calculate leaf, branch and bole biomass.
However the documented Partitioned Biomass and Dimension Analysis behaviors are analysis/output behaviors and do not supply a dynamic root-biomass state.

No HETEROFOR-like:
- fine-root allocation
- root turnover
- root-water uptake by soil horizon
was identified in the standard model.

Thus a Gounsa coupling would require:
```
SORTIE tree x,y,DBH
 -> ChaMRoots / allometric root helper
 -> separate root state
```

This is possible, but substantially more external biology than with HETEROFOR.

## water/soil feedback
SORTIE is fundamentally a neighbourhood forest-dynamics framework, not a fine-time-step forest ecohydrology model.
Soil/light grids can influence demographic behaviors, but hourly tree-pedon water balance comparable to HETEROFOR is not a standard core process.

## current verdict for Gounsa
Strengths:
- very mature spatial individual-tree framework
- open source and recently maintained
- strong recruitment/neighbourhood dynamics
- substrate/litter/log spatial states
- postfire 100-year application
- flexible grids

Weaknesses:
- no native root biomass/turnover state
- no mechanistic wildfire
- weaker physiological water/root coupling

Therefore:
- retain as a strong spatial/postfire comparator
- below HETEROFOR for the primary vegetation-geomorph engine
- potentially valuable if HETEROFOR implementation/access becomes impractical

## related papers
- papers/2022_Clason_SORTIE_Postfire100yr.md
- papers/2026_Ghose_SORTIE_SpatialValidation.md
