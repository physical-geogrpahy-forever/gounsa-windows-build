# LPJ-GUESS spatial cohort and hydrology branches

업데이트: 2026-09-23

## 목적
고운사 5조건에 대해 LPJ-GUESS를 하나의 고정 모델로 보지 않고, 서로 다른 개발 branch가 각각 어떤 약점을 해결했는지 분리해서 기록한다.

중요 원칙:
현재 문헌에 존재하는 서로 다른 branch의 기능을 합쳐서 `기존 단일 모델`이라고 부르지 않는다. branch merge가 필요하면 반드시 **새로운 coupling/code merge**라고 기록한다.

---

# 1. LPJ-GUESS 기본 식생 구조

기본/유럽형 LPJ-GUESS에서는 한 patch 안에서 다음이 함께 경쟁한다.
- tree PFT/species age cohorts
- shrub PFTs
- grass/herbaceous PFTs

경쟁 자원:
- light
- water
- nitrogen
- space

시간 구조:
- photosynthesis, respiration, phenology, hydrology, soil C/N: daily
- allocation, turnover, establishment, mortality: mainly yearly

주의:
- tree는 age cohorts로 세분 가능
- herbs/grasses는 일반적으로 patch당 대표 average individual/population으로 취급되므로 수목과 같은 다중 age-cohort 구조는 아니다

따라서 `tree + shrub + herbaceous succession`은 존재하지만 모든 life form이 동일한 cohort 해상도를 갖는 것은 아니다.

---

# 2. Branch A: LPJ-DH / LPJG-WHyMe-TFM

## 핵심 논문
Tang et al. 2014 및 후속 Stordalen catchment 연구.

## 해결한 문제
`coarse independent grid cells` -> `actual fine catchment grid + DEM-driven lateral routing`

## 핵심 특징
- Stordalen catchment 약 16 km2
- 50 m geographic grid
- DEM-derived slope, flow direction, drainage area
- grid-to-grid daily water redistribution
- LPJ-GUESS vegetation dynamics retained
- trees, shrubs, C3 grass
- runoff evaluated at multiple outlets

## 고운사 의미
현재까지 확인된 LPJ-GUESS 계열 중 **가장 직접적인 fine-catchment precedent**.

## 한계
- old/legacy branch
- lateral hydrology simpler than ParFlow
- within-cell vegetation patch/cohort positions are not actual x-y locations
- modern canopy SEC/PPA and LPJ-GUESS-RE are not demonstrated in this branch

---

# 3. Branch B: PF-LPJG 2026

## 핵심 논문
Jia et al. (2026), GMD 19:1727-1747.
DOI: 10.5194/gmd-19-1727-2026

## 공개 기반
- LPJ-GUESS Release v4.0.1
- ParFlow v3.13.0
- coupled code archived separately on Zenodo

## 해결한 문제
`1-D local LPJ soil/runoff` -> `3-D surface-subsurface flow + groundwater + two-way state exchange`

## coupling
- ParFlow runs hourly
- after 24 ParFlow steps, state is exchanged with LPJ-GUESS
- ParFlow soil moisture overwrites LPJ-GUESS soil-water state daily
- LPJ-GUESS computes daily P-ET / vegetation water fluxes
- flux is returned to ParFlow and disaggregated for the next hourly hydrologic cycle

## 공간
Published Danube demonstration:
- 10 km resolution
- 38 years
- explicit lateral groundwater flow

## 고운사 의미
**가장 강한 modern open soil-state exchange precedent.**
사용자가 정정한 criterion 3의 정확한 모범사례다.

## 한계
- published resolution is far too coarse for Gounsa
- current paper used one patch of a single stand type per grid cell and disabled patch-destroying disturbance
- LPJ-GUESS base is v4.0.1, not the 2026 SEC/PPA branch
- fine hillslope 10-50 m validation absent

---

# 4. Branch C: LPJ-GUESS-RE v1.0

## 핵심 논문
Verbruggen et al. (2025), GMD 18:6623-? / LPJ-GUESS-RE v1.0.
DOI: 10.5194/gmd-18-6623-2025
Code DOI: 10.5281/zenodo.15024130

## 해결한 문제
`bucket-like vertical soil movement` -> `process-based 1-D Richards soil hydrology`

## 핵심 특징
- 15 soil layers
- custom layer thicknesses
- therefore configurable total soil depth
- free-drainage, bedrock, aquifer bottom boundary conditions
- soil water potential, conductivity and root sink physically resolved
- adaptive subdaily numerical integration inside the daily ecosystem step

## 고운사 의미
토양-지형 모델이 바꾸는 soil profile depth/layer thickness와 가장 자연스럽게 맞물릴 수 있는 LPJ branch.

## 한계
- still 1-D vertical hydrology
- no native lateral terrain routing
- dynamic erosion/deposition during a run and conservative remapping of existing water/C/N/root pools are not provided as a geomorphic event interface

---

# 5. Branch D: SEC / PPA canopy revision 13221

## 핵심 논문
Stoebke et al. (2026), GMD 19:3595-3615.
DOI: 10.5194/gmd-19-3595-2026
Code: Zenodo 10.5281/zenodo.18133363

## 해결한 문제
`patch mean-field canopy` -> `persistent gap and explicit within-patch canopy structure`

## SEC
- each tree cohort retains an aggregated crown-area centroid at a fixed within-patch position
- cohort mortality therefore leaves persistent canopy gaps
- avoids full individual-tree computation
- new cohorts establish where forest-floor light is sufficient
- paper configuration allowed multiple new cohorts per PFT per year

This is a particularly good match to the requested architecture:
`individual tree model보다 가볍고, conventional cohort보다 공간적으로 명시적인 hybrid`.

## PPA
- cohorts are sorted into canopy and understory layers according to crown area/height structure
- explicit multi-layer light competition

## understory
- woody recruitment/understory layer is explicit
- forest-floor irradiance is spatially heterogeneous in SEC
- herbaceous understory leaf area responds dynamically to remaining PAR
- gap colonisation and shade-intolerant -> shade-tolerant replacement are improved

## 한계
- SEC spatial coordinate is a simplified within-patch representation, not a full GIS 2-D x-y coordinate for every cohort
- herbaceous vegetation does not have the same rich age-cohort demography as tree cohorts
- no lateral catchment hydrology in this paper

---

# 6. Branches must not be conflated

Currently published:

```text
LPJ-DH
= fine catchment routing precedent

PF-LPJG
= modern 3-D hydrology/state-exchange precedent

LPJ-GUESS-RE
= variable-depth, Richards vertical soil precedent

SEC/PPA revision 13221
= modern spatial canopy/cohort + understory-light precedent
```

Not currently identified as an existing published single codebase:

```text
SEC/PPA revision 13221
+ PF-LPJG
+ LPJ-GUESS-RE
+ fine 10-50 m catchment routing
```

That combination is therefore a **새로운 coupling/code merge**.

---

# 7. Why this lineage is now unusually strong for Gounsa

Taken as a development lineage rather than an already assembled model, essentially every required component has a published precedent:

1. spatial cohort/hybrid
   - SEC tree cohorts with persistent local gaps
2. explicit understory/succession
   - shrub + herbaceous PFT competition in LPJ-GUESS
   - woody understory/recruitment and forest-floor herb light in SEC/PPA
3. soil-terrain connection
   - PF-LPJG direct soil-state overwrite
   - LPJ-GUESS-RE configurable soil depth/Richards layers
4. catchment/topography
   - LPJ-DH 50 m catchment
   - PF-LPJG 3-D basin hydrology
5. timestep
   - daily LPJ physiology/ecohydrology
   - hourly ParFlow
   - subdaily adaptive Richards solver in RE

The weakness is no longer scientific absence of components. It is **software integration and fine-scale validation**.

---

# 8. Gounsa candidate architecture to test, not yet claim as existing model

```text
10-50 m geographic vegetation/soil units
        |
        +-- LPJ-GUESS SEC cohort canopy
        |     tree cohort age/size + persistent gaps
        |     shrub/herbaceous competition
        |
        +-- external/fine terrain hydrology
        |     PF-LPJG style daily state exchange
        |
        +-- variable soil profile
              LPJ-GUESS-RE style layer thickness / bedrock

1-5 m geomorphic grid remains separate if required
```

At storm/day synchronization:
- terrain model updates soil depth, layer geometry, water state and DEM-derived flow variables
- vegetation receives soil-water / potential / depth constraints
- vegetation returns root uptake, LAI, biomass, root mass, litter and interception

Dynamic erosion/deposition layer remapping remains a new coupling.

---

# 9. Current verdict

**Promoted to the strongest overall model lineage for further implementation audit, but not yet a single ready-made model.**

Reason:
- unlike most alternatives, each major Gounsa requirement now has a close LPJ-GUESS published branch precedent
- SEC directly addresses the desired middle ground between individual-tree and non-spatial cohort models
- PF-LPJG demonstrates the exact external soil-state exchange principle requested by criterion 3
- LPJ-DH demonstrates fine catchment operation
- RE gives an internally clean path for variable/shallow soil profiles

Next task is therefore not additional broad name collection. It is to quantify the difficulty of merging the SEC/PPA branch with PF-LPJG/RE and determine whether 10-50 m Gounsa execution is computationally and numerically practical.
