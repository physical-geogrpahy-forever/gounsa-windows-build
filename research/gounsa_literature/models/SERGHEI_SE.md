# SERGHEI-SE lineage

## 핵심 문헌
- Martínez-Aranda et al. (2025 preprint), *SERGHEI-SE: An Open-Source High-Performance-Computing Model for Soil Erosion and Sediment Transport Processes in Catchments*
- Braga, Martínez-Aranda & García-Navarro (2026), Water 18(15), 1870, DOI 10.3390/w18151870

## 고운사에서 검토한 이유
latest open-source high-performance genuine 2D catchment-scale erosion framework.

## 공간구조
- 2D shallow-water equations
- 2D solid transport
- finite volume
- bed evolution
- HPC/high-resolution catchment computation

## vegetation
2025 model description uses a vegetation/land-management/bedrock modification factor, including Sentinel-2-derived inputs in the demonstrated setup.
Dynamic root biomass/RLD is not a core state variable.

2026 evaluation likewise does not solve the quantitative vegetation-state gap.

## 강점
- genuine 2D
- conservation-oriented finite-volume formulation
- catchment-scale HPC
- explicit surface evolution

## 한계
- quantitative root/litter state missing
- root recovery after wildfire not represented mechanistically

## 고운사에 쓸 수 있는 부분
Modern 2D-engine comparison and implementation architecture.

## 새로운 coupling
LPJ-GUESS root/litter states linked to erosion parameters are **new coupling**.

## 최종 판정
**2D-engine comparison candidate.**


## 2026-10-26 strict all-in-one source screening superseding "engine candidate" wording
- The model and its Braga et al. (2026) validation paper **were already archived** in this repository before today's search. This is not a new model discovery, only a new assessment.
- Peer-reviewed 2D SWE finite-volume and sediment/conservative bed deformation, paper-based analytical hillslope, V catchment, lab erodible-bed tests: documented. Official public BSD3 core and developer tests at https://gitlab.com/serghei-model/serghei , https://gitlab.com/serghei-model/serghei-tests.
- Native **LAI → dynamic canopy water store → stem/canopy drainage → throughfall → distinct direct and leafdrip kinetic splash source** is **NOT demonstrated** in the released SERGHEI-SE source. The documented vegetation factor protecting the bed is NOT proof of a working canopy water cycle or species-specific drip.
- Spanish 2026 Moncayo prefire mountain article relates to hydrological runoff calibration (no direct independent native local soil erosion/rill validation in the cited abstract).
- Current GitLab C++ file-by-file source audit was **not completed** in this conversation. No original binary was built or run. Do not claim code-verified canopy negative; treat absence of positive proof as a **strict exclusion under user direction "의심이 되면 버려"**.
- **VERDICT: exclude from all-required native Gounsa water-erosion main-engine candidate; maintain independent open genuine-2D erosional/morphodynamic benchmark.** Fully stable numerical sediment dt convergence for exact current source not experimentally proven in our environment.
See [full additional screening](../decisions/2026-10-26_POST_TIMEOUT_NEW_2D_ENGINES_SERGHEI_LISEM_SEIMS.md).
