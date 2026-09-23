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
Code DOI: 10.5281/zenodo.16908049

## 공개 기반
- LPJ-GUESS Release v4.0.1
- ParFlow v3.13.0
- coupled code archived separately on Zenodo
- Zenodo archive is open and contains both model source trees plus technical documentation

## 해결한 문제
`1-D local LPJ soil/runoff` -> `3-D surface-subsurface flow + groundwater + two-way state exchange`

## coupling
- ParFlow runs hourly
- after 24 ParFlow steps, state is exchanged with LPJ-GUESS
- ParFlow soil moisture overwrites LPJ-GUESS soil-water state daily
- LPJ-GUESS computes daily P-ET / vegetation water fluxes
- flux is returned to ParFlow and disaggregated for the next hourly hydrologic cycle

## source-level implementation point
Jia et al. explicitly reports that the MPI coupler is embedded in LPJ-GUESS `framework.cpp`.
Before coupling they also modified LPJ-GUESS to:
- replace the original soil discretization with 4 variable-depth layers: 0.1, 0.3, 0.6, 1.0 m
- accept layer-specific sand/clay/silt
- overwrite internal LPJ soil moisture using ParFlow state
- preserve native solvers on each side of the MPI coupling

This is important because the coupler itself is concentrated around the LPJ framework/soil-state exchange rather than canopy demography.

## 공간
Published Danube demonstration:
- 10 km resolution
- 38 years
- explicit lateral groundwater flow

## 고운사 의미
**가장 강한 modern open soil-state exchange precedent.**
고운사에서 원하는 `external hydrology owns the water state -> vegetation reads state -> vegetation returns uptake/ET` 구조의 직접 선례다.

## 한계
- published resolution is far too coarse for Gounsa
- current paper used one patch of a single stand type per grid cell and disabled patch-destroying disturbance
- LPJ-GUESS base is v4.0.1, not the 2026 SEC/PPA branch
- fine hillslope 10-50 m validation absent

---

# 4. Branch C: LPJ-GUESS-RE v1.0

## 핵심 논문
Verbruggen et al. (2025), GMD 18:6623-6645.
DOI: 10.5194/gmd-18-6623-2025
Code DOI: 10.5281/zenodo.15024130

## 기반 버전
- LPJ-GUESS v4.1.1 revision 10118
- archive open
- authors explicitly recommend using the latest LPJ-GUESS as base when not reproducing their experiment

## 해결한 문제
`bucket-like vertical soil movement` -> `process-based 1-D Richards soil hydrology`

## 핵심 특징
- default 15 soil layers
- custom layer number/thickness possible
- free-drainage, bedrock, aquifer bottom boundary conditions
- soil water potential, conductivity and root sink physically resolved
- adaptive subdaily numerical integration inside the daily ecosystem step
- Runge-Kutta Cash-Karp adaptive solver via Boost odeint

## 식생-토양 연결
매일 각 patch의 식물은 모든 토층에서 물을 흡수할 수 있다.
Layer uptake depends on:
- layer soil water
- PFT root fraction
- patch water demand
- cohort water-stress status
- cohort FPC
- PFT `emax`

Vertical root fraction uses an asymptotic depth distribution with PFT-specific beta-root.

## 고운사 의미
토양-지형 모델이 바꾸는 soil profile depth/layer thickness와 가장 자연스럽게 맞물릴 수 있는 LPJ branch.

## 매우 중요한 shallow-soil 문제
현재 LPJ-GUESS root allocation은 토양 하단까지 cumulative root fraction이 1에 도달하지 않으면 남은 root fraction을 bottom layer에 배정한다.
Verbruggen et al.은 soil depth가 약 1 m 이하일 때 bottom layer에 root biomass가 비정상적으로 집중될 수 있고, 이 때문에 bottom-layer transpiration 기여가 커질 수 있음을 직접 보고한다.

따라서 고운사처럼 얕은 토심이 핵심인 경우 다음 규칙을 그대로 쓰면 안 된다.

금지할 처리:
```text
soil erosion -> shallower profile -> missing root fraction compressed into bottom surviving layer
```

고운사에서 필요한 처리:
```text
soil erosion -> removed soil volume
            -> root biomass physically contained in removed volume is lost
            -> surviving profile root fractions are renormalized only after root loss
            -> dead/removed roots are transferred to exported sediment or local detrital pool according to process assumption
```

이 `erosion -> root truncation/remap`은 LPJ-GUESS-RE native 기능이 아니며 새로운 coupling이다.

## 한계
- still 1-D vertical hydrology
- no native lateral terrain routing
- dynamic erosion/deposition during a run and conservative remapping of existing water/C/N/root pools are not provided as a geomorphic event interface
- standard root-profile truncation is problematic for very shallow soils

---

# 5. Branch D: SEC / PPA canopy revision 13221

## 핵심 논문
Stoebke et al. (2026), GMD 19:3595-3615.
DOI: 10.5194/gmd-19-3595-2026
Code: Zenodo 10.5281/zenodo.18133363

## 코드 접근성
- published paper states revision 13221
- code archived under Mozilla Public License 2.0
- Zenodo public metadata is available, but direct file access may require repository access/login depending on record version

## 해결한 문제
`patch mean-field canopy` -> `persistent gap and explicit within-patch canopy structure`

## SEC
- each tree cohort retains a fixed horizontal position / crown-area centroid inside the notional patch
- cohort mortality therefore reduces crown area locally and leaves persistent gaps
- avoids full individual-tree computation
- new cohorts establish where forest-floor light is sufficient
- cohorts are not explicit individual trees

This is a particularly good match to the requested architecture:
`individual tree model보다 가볍고, conventional cohort보다 공간적으로 명시적인 hybrid`.

## PPA
- cohorts are sorted into canopy and understory layers according to crown area/height structure
- explicit multi-layer light competition
- cohorts can be promoted/demoted between canopy layers dynamically

## understory
- woody recruitment/understory layer is explicit
- forest-floor irradiance is spatially heterogeneous in SEC
- herbaceous understory receives residual forest-floor PAR
- gap colonisation and shade-intolerant -> shade-tolerant replacement are improved

## computational implication
The paper reports SEC required more than twice the computational resources of the standard LPD canopy scheme for a fixed patch set, but SEC converged with fewer replicate patches.
This matters for Gounsa because one can reduce replicate patch count if a GIS-cell interpretation is used.

## 한계
- SEC coordinate is a simplified within-patch representation, not a full GIS 2-D x-y coordinate for every cohort
- herbaceous vegetation does not have the same rich age-cohort demography as tree cohorts
- no lateral catchment hydrology in this paper
- tree individuals inside a cohort do not shade each other separately

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

The weakness is no longer scientific absence of components. It is **software integration, shallow-soil root remapping and fine-scale validation**.

---

# 8. Branch compatibility audit

## SEC/PPA + PF-LPJG
**상대적으로 충돌 가능성이 낮은 조합.**

이유:
- SEC/PPA primarily modifies canopy geometry, crown area, light interception, establishment and self-thinning.
- PF-LPJG primarily modifies framework-level MPI exchange, soil discretization/state, hydrological forcing and runoff replacement.
- published descriptions place the PF coupler in `framework.cpp`, not in the canopy-light engine.

따라서 revision mismatch를 이식해야 하지만 scientific/process modules are largely orthogonal.

판정:
**realistic merge candidate.**

## SEC/PPA + RE
**역시 비교적 현실적인 조합.**

RE changes vertical soil-water physics and soil-layer representation.
SEC changes canopy and cohort light structure.
The principal biological intersection is root-water stress feeding growth, not shared canopy code.

판정:
**realistic merge candidate.**

## RE + PF-LPJG
**그대로 둘 다 켜는 것은 비효율적/중복.**

Both replace or substantially modify soil-water physics.
If ParFlow owns 3-D soil water, there is little reason to simultaneously integrate the LPJ-GUESS-RE Richards solver for the same water column.

Instead, high-value RE features to port into the PF-LPJG route are:
- arbitrary layer thickness support
- shallow soil/bedrock boundary representation
- layer-aware root water extraction logic
- soil hydraulic state bookkeeping where still needed by LPJ processes

while **ParFlow remains the sole water-state solver**.

Recommended architecture:
```text
SEC canopy/demography
+ PF-LPJG hydrology ownership
+ selected RE soil-geometry ideas
- RE Richards solver itself
```

This is cleaner than running two competing Richards solvers.

---

# 9. Gounsa candidate architecture after deep audit

```text
actual GIS vegetation unit: 10-50 m
        |
        +-- LPJ-GUESS SEC
        |     tree cohort age/size
        |     persistent canopy gaps
        |     woody recruitment
        |     shrub/herbaceous competition
        |
        +-- external hydrology owner
        |     ParFlow or project hydrology
        |     hourly/event scale
        |     lateral + vertical water
        |
        +-- soil geometry interface
              variable active soil depth
              bedrock
              conservative state remap

geomorph engine: 1-5 m if necessary
        |
        +-- erosion/deposition
        +-- DEM update
        +-- soil-depth update
        +-- root truncation/burial update
```

Daily synchronization:
```text
1. hourly/event hydrology + geomorphology
2. aggregate cell water/soil state to vegetation unit
3. physically remove/bury roots according to changed soil geometry
4. pass soil-water state to LPJ-GUESS
5. run daily physiology
6. annual or scheduled demographic processes retain LPJ-GUESS native timing
7. return FineRootC, litter, LAI/FPC, biomass and water uptake to geomorph/hydrology
```

Important: a 6-hour storm does **not** require tree demography every hour. It requires soil/root state to be modified immediately by the event, after which daily physiology can respond to the changed state.

---

# 10. State variables required for geomorphic coupling

Minimum vegetation -> geomorph outputs:
- PFT/cohort aboveground biomass
- FineRootC / live root biomass
- litter inputs and standing litter if available
- LAI/FPC/canopy interception state
- cohort mortality/root turnover
- root fraction by soil layer

Minimum geomorph/hydrology -> vegetation inputs:
- active soil-layer thicknesses
- total soil depth / bedrock depth
- soil moisture or water potential by layer
- water-table state where relevant
- soil texture/coarse fragment changes if erosion/deposition changes material
- surface elevation and slope-derived hydrologic forcing

Event remap pools that cannot be ignored:
- water mass
- soil C/N pools
- live fine roots
- dead roots/root litter
- mineral N if the profile is truncated

---

# 11. 현재 판정

**LPJ-GUESS remains the strongest development lineage, and the deep audit improves rather than weakens its position.**

But the preferred implementation route is now more specific:

```text
Preferred:
SEC/PPA revision 13221 biology/canopy
+ PF-LPJG-style external hydrology ownership
+ selected LPJ-GUESS-RE variable-depth/bedrock concepts
+ new conservative geomorphic state remapper
```

Do **not** attempt:
```text
SEC + full RE Richards solver + full ParFlow water solver simultaneously
```
because the latter two duplicate ownership of soil-water physics.

The principal new development required for Gounsa is no longer a new vegetation model. It is a robust event-driven state-remapping layer for:
- changing soil depth
- root truncation/burial
- water/C/N conservation
- daily restart/continuation

This is the component to prototype before committing to the final engine.
