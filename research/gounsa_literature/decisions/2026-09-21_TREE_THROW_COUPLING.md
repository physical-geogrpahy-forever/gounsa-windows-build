# 결정: LPJ-GUESS woody cohort -> tree throw / root-plate coupling

날짜: 2026-09-21

## 결정
Tree throw를 단일 annual probability 또는 biomass-modified diffusivity로 처리하지 않는다.

두 전도경로를 분리한다.

### live/surviving tree
```
LPJ-GUESS DBH/height/stand state
 -> ForestGALES/fgr
 -> critical wind speed / overturning risk
 -> uprooting event
```

### fire-killed standing dead tree
```
fire mortality
 -> dead-standing cohort
 -> Gallaway-type delayed toppling
 -> uprooting vs breakage
 -> root-plate event
```

## root-plate geometry
Priority:
1. Kim et al. 2014 Taehwa Korean root-plate data
2. Gallaway et al. 2009 DBH-volume relationship as fallback/sensitivity
3. generic Gabet-Mudd rootwad geometry only when local allometry unavailable

## event displacement
Use Greenwood/Gabet geometry for:
```
root-plate geometry + slope
 -> downslope travel distance
```

## DEM update
Use Doane annual stochastic pit-mound architecture.

Tree throw is a discrete topographic event, not a change in background diffusivity.

## physical bedrock disturbance
Use Gabet & Mudd geometric intersection architecture, with explicit uncertainty in fracture efficiency.

Do not describe it as a mechanistic root-force fracture model.

## stem breakage
ForestGALES calculates overturning and stem breakage separately.

Only:
```
overturning
```
feeds root-plate geomorphology.

Stem breakage feeds CWD/deadwood state instead.

## Korean constraints
- Kim et al. 2014: local root-plate geometry/allometry
- Park 2026: slope, DBH, edge/exposure and vegetation context jointly affect Korean pine uprooting susceptibility

## software
fgr is public R source and implements stand and individual-tree ForestGALES methods.

However its repository license is:
```
GPLv3 + Commons Clause / non-commercial restrictions
```
so do not call it unrestricted FOSS.

The archived repository also labels itself beta/testing software.

## unresolved calibration
1. Korean species/PFT anchorage parameters
2. exact local DBH-root-plate regressions from Kim 2014 figures
3. local wind climate/event forcing
4. fire-killed snag toppling-rate function
5. fine/coarse fraction in uprooted root plate
6. bedrock fracture efficiency
7. snow-loading module decision

## final judgment
The tree-throw model structure is now selected.

Remaining work is local parameterization and implementation rather than searching for a different overarching model.
