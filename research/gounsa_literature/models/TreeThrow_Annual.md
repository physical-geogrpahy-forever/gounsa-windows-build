# TreeThrow annual event-model lineage

## 목적
100년 고운사 사면수송에서 tree throw를 generic diffusivity에 포함하지 않고 **연 단위 discrete event**로 계산할 수 있는 actual model precedent를 관리한다.

## CSDMS TreeThrow model

Developers:
- Matthew Kirwan
- Hank Shugart

CSDMS metadata:
- terrestrial plot-scale model
- Fortran 77
- single processor
- typical runtime seconds to minutes
- GPL v2 listed in metadata
- **annual timestep**
- usually simulated for about 1000 years

CSDMS page also categorizes the source code as not publicly available, so the license metadata and actual downloadable-source status must not be conflated.

## represented processes
The model explicitly simulates:
```
individual tree growth
 -> death
 -> regeneration
 -> subset of deaths cause tree fall
 -> displaced sediment volume
 -> transport distance
 -> hillslope sediment flux
```

Sediment movement per fall depends on:
- sediment/soil-plate volume
- transport distance
- hillslope angle

Volume and transport distance depend on tree diameter.

## scale
Spatially implicit:
- one 1/12-ha plot in the CSDMS description

Therefore this model is not itself the final Gounsa raster engine.

Its importance is the **annual tree-demography-to-sediment-flux interface**.

## calibration requirements
CSDMS lists calibration of:
1. soil-plate volume vs tree diameter
2. soil-plate width vs tree diameter
3. soil-plate depth vs tree diameter

Southern Blue Ridge data were used in the documented calibration.

## relation to Doane 2021
Doane et al. 2021 provides a stronger modern spatial/topographic framework:
- annual stochastic pit-mound generation
- 2D surface roughness
- tree-throw sediment flux

The older TreeThrow model independently confirms that annual tree growth/death/diameter can be connected quantitatively to sediment movement.

## relation to LPJ-GUESS
LPJ-GUESS already computes the vegetation state.

Therefore Gounsa does **not** need the TreeThrow model's internal forest-growth component.

The useful interface is:

```
LPJ-GUESS
 DBH / density / mortality / disturbance
      |
      v
tree-fall / uprooting probability
      |
      v
rootwad / soil-plate volume
      |
      v
downslope displacement
      |
      v
q_treethrow
```

This is a **new coupling**.

## role in Gounsa
Use as:
- annual event-model precedent
- validation of annual timestep feasibility
- DBH -> displaced-volume architecture reference

Do not use as the sole spatial model because it is zero-dimensional/plot-scale.

## current judgment
**Strong supporting model for annual tree-throw implementation.**

Primary quantitative/spatial theory remains:
- Doane 2021/2024
- Gabet & Mudd 2010

CSDMS TreeThrow shows that the entire biological-event chain can be evaluated at a 1-year timestep.

## source
CSDMS Model:TreeThrow metadata, accessed 2026-09-21.
