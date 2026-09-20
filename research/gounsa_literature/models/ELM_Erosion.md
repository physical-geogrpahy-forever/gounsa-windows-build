# ELM-Erosion lineage

## 핵심 문헌
Tan et al. (2022), ELM-Erosion. Full bibliographic details are stored in the paper file and should be rechecked before manuscript citation.

## 고운사에서 검토한 이유
dynamic land/ecosystem model where PFT-specific root biomass directly influences erosion resistance.

## spatial structure
- land-model / large-scale grid
- around 0.5-degree lineage
- not hillslope-scale genuine 2D hydrodynamics

## vegetation state
- PFT-specific topsoil root biomass
- PFT-dependent root effectiveness
- dynamic vegetation state, not only cover

## erosion processes
rainfall-driven and runoff-driven erosion terms are modified by vegetation/root effects.

## 고운사에 쓸 수 있는 부분
Strong precedent for:
```
PFT-specific dynamic root biomass
 -> erosion resistance
```

This is especially relevant to LPJ-GUESS PFT/FineRootC outputs.

## 한계
- global/land-model scale
- does not solve rill/interrill 2D hydraulics
- spatial scale far from Gounsa hillslope DEM

## 새로운 coupling
ELM-Erosion root formulation transferred to Wu/Iber/another 2D engine is **new coupling**.

## 최종 판정
**core vegetation-erosion bridge precedent.**
