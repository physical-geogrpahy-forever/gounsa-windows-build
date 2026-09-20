# SSSPAM soilscape-landform evolution lineage

## 핵심 논문
- Welivitiya, Willgoose & Hancock 2019, Earth Surface Dynamics 7, 591-607, DOI 10.5194/esurf-7-591-2019
- Welivitiya, Willgoose & Hancock 2021, Earth Surface Processes and Landforms 46, 2298-2314, DOI 10.1002/esp.5175

## 고운사에서 검토한 이유
Pelletier 계열보다 짧은 simulation horizon에서:
- soil profile
- weathering
- diffusion
- erosion/deposition
- armouring
- evolving topography
를 함께 계산하는 실제 soilscape-landform model이 있는지 비교하기 위해 검토했다.

## 공간구조
- DEM / distributed landform
- multilayer soil profile
- state-space matrix representation
- evolving surface elevation and soil grading

## 과정
SSSPAM includes:
- fluvial erosion
- deposition
- diffusive transport
- surface armouring
- physical weathering
- depth-dependent weathering functions
- particle-size/profile evolution

## weathering
Weathering is primarily **physical fragmentation**.

The model can use different depth-dependent weathering functions, including:
- exponential
- humped exponential
- reversed/dynamic forms in later lineage

The 2019 paper explicitly states that chemical transformations are not represented in that formulation.

## timescale
A major strength:
- can use short rainfall events
- variable precipitation
- annual-average precipitation
- 2021 paper demonstrates a **100-year short-term landform simulation**

Thus SSSPAM is much closer to the Gounsa 100-year simulation horizon than Pelletier's 10-Myr eco-pedo-geomorphic experiments.

However, weathering can still be intrinsically slow. Later 100-year applications sometimes disable the weathering module.

## vegetation
No LPJ-GUESS-like dynamic vegetation/root state.

This is the decisive biological limitation for Gounsa.

## relation to Gounsa modules

### potentially useful
- physical soil-profile bookkeeping
- particle-size evolution
- armour formation/breakdown
- coarse-fragment supply
- independent 100-year LEM benchmark

### overlaps with existing chosen modules
- SWEHR already calculates event erosion/deposition and deposited-layer shielding
- Gabet/Mudd explicitly represents woody mechanical weathering
- LPJ-GUESS-CNP already provides daily hydroclimatic chemical weathering

Using SSSPAM as a whole would therefore duplicate several states/processes.

## new coupling if adopted
```
LPJ-GUESS
 -> SSSPAM weathering / soil-profile parameters
```
would be new.

Reconciling SSSPAM surface grading/armour with SWEHR `M[k]`, `H` and PSD would also be new and potentially complex.

## current judgment
**Do not use SSSPAM as the primary full Gounsa model.**

Retain it as:
1. century-scale feasibility benchmark
2. physical weathering/profile comparison
3. strong candidate source when coarse-fragment/armour module is finalized

It is a better timescale comparison than Pelletier but a worse vegetation-process match than the modular LPJ-GUESS + Gabet + Doane architecture.
