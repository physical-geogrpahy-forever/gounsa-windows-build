# MEDFATE + medfateland + SERGHEI deep source audit

업데이트: 2026-09-23

# 왜 별도 감사했는가
MEDFATE/medfateland는 고운사 후보 중 actual GIS cell, daily vegetation state, tree/shrub cohorts, explicit root profiles와 외부 hydrology delegation이 가장 투명하다. 2026 source tree에 SERGHEI coupling이 실제로 존재하므로, 단순 문서상 옵션인지 실제 two-way state exchange인지 확인했다.

# 핵심 결론
현재 medfateland source에는 **실제 daily two-way MEDFATE-SERGHEI interface가 존재한다.**

MEDFATE -> SERGHEI:
- NetRain / throughfall
- soil layer별 PlantExtraction
- soil layer별 HerbTranspiration
- Snowmelt
- SoilEvaporation

SERGHEI -> MEDFATE:
- new layer-wise soil moisture state
- MEDFATE soil W에 difference 적용
- belowLayers Wpool에도 difference 적용

따라서 이는 단순 output post-processing이 아니라 hydrologic state feedback이다.

# source evidence
`emf-creaf/medfateland/src/serghei.cpp`

주요 순서:
```text
MEDFATE local daily calculation
 -> collect NetRain
 -> collect PlantExtraction[layer]
 -> collect HerbTranspiration[layer]
 -> add Snowmelt / SoilEvaporation source-sink
 -> MedFateLand_Serghei::compute_daily_step()
 -> read SERGHEI soil W[layer]
 -> update MEDFATE soil/rhizosphere water state
```

# SERGHEI backend
medfateland documentation allows watershed model:
- TETIS
- SERGHEI

SERGHEI v2.0 adds:
- 3D variably saturated Richards solver SERGHEI-RE
- iterative/non-iterative solution schemes
- Kokkos CPU/GPU portability
- framework designed for integrated surface-subsurface flow

This means MEDFATE-SERGHEI has a plausible development path from current distributed water transfer to genuine surface + 3D subsurface hydrology.

# critical maturity audit
Current coupling must not be described as a mature turnkey package.

## 1. build/distribution maturity
2026-05-06 `_SERGHEIcoupling.Rmd` states users must compile medfateland and SERGHEI together.
The vignette still has incomplete/placeholder sections for branch download, dynamic-library build and testing.
CRAN medfateland does not bundle SERGHEI.

## 2. source path
Current source contains a developer-local include path:
```cpp
#include "/home/miquel/serghei-master/src/MedFateLand_Serghei.h"
```
This is evidence of a development integration rather than a polished portable distribution.

## 3. possible indexing defect requiring test
Current `serghei.cpp` moisture update contains:
```cpp
for(int l=0; l<W_soil.size();l++) {
  W_soil[l] = W_soil[i] + W_diff[l];
}
```
Inside this layer loop, `W_soil[i]` is suspicious because `i` is the spatial-unit index and `l` the soil-layer index. The likely intended expression may be `W_soil[l] + W_diff[l]`, but this must be verified by execution/tests before calling it a bug.

Therefore coupling source should be audited and tested before production use.

# biological state sent to hydrology
Important for Gounsa:
- woody plant extraction and herb transpiration are explicitly separated in medfateland outputs
- layer-specific uptake is sent to hydrology
- throughfall and soil evaporation are likewise explicit

This is a good interface for the postfire sequence because herbaceous recovery can change water uptake before woody biomass has recovered.

However MEDFATE still lacks a complete endogenous herb demographic lifecycle. Existing herb cohorts have physiology/root profiles, but native woody-style seed bank -> recruit cohort -> demographic mortality is absent for herbs.

# soil geometry and geomorphic feedback
MEDFATE can redefine soil layers, but this is not a conservative geomorphic remapper.
For Gounsa, erosion/deposition requires:
```text
old layer geometry + state
 -> geomorph event changes surface elevation / active soil depth
 -> conservative remap of water/C/N/other pools
 -> calculate roots removed/buried
 -> recompute root fractions and rhizosphere state
 -> hand new layered state to SERGHEI and MEDFATE
```

This remains a new coupling.

# comparison with LPJ-PF and FATES-ParFlow
## advantage
- actual GIS/raster units are native and transparent
- daily state objects are easy to inspect and mutate in R/Rcpp
- source-level vegetation-hydrology interface is much smaller and easier to understand
- herb and woody water uptake are separately visible

## disadvantage
- current SERGHEI build interface is immature
- v2.0 SWE+RE compatibility with medfateland coupling not yet demonstrated
- MEDFATE herb demographic lifecycle incomplete
- canopy-gap/light demography simpler than LPJ-GUESS SEC or FATES PPA

# current verdict
**High-potential engineering route, not yet turnkey.**

If the project prioritizes implementability and direct geomorphic state mutation, MEDFATE + medfateland + SERGHEI may be more practical than FATES/ParFlow and possibly LPJ-GUESS SEC/PF.

But before promotion above LPJ/FATES, four tests are mandatory:
1. compile current medfateland with current SERGHEI branch on Linux/Windows or WSL
2. unit-test layer-wise W exchange and confirm/fix indexing
3. verify compatibility with SERGHEI v2.0 integrated SWE+RE, not only older SWE API
4. implement/prototype herb recruitment and mortality lifecycle

# relevant files and papers
- `models/MEDFATE_MEDFATELAND.md`
- `papers/2025_Li_SERGHEI_RE.md`
- De Cáceres et al. 2023 MEDFATE model paper
- Caviedes-Voullième et al. 2023 SERGHEI framework
- Li et al. 2025 SERGHEI v2.0, DOI 10.5194/gmd-18-547-2025

# final status
**Top-tier experimental integration candidate / implementation audit required.**
