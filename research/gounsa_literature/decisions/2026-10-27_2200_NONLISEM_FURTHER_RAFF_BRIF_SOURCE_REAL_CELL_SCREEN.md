# 2026-10-27 비LISEM 후속 실증선례 집중 탐색: Raff 2005 + Wang 2025 BRIF 정밀 판정

## 연구 지시와 선행 기록
OpenLISEM 실물 오류/실행 검증은 사용자가 다른 Work에게 맡김. 이 세션은 새 선행연구와 **실제 타 연구자 계산격자 + 활성 물리방정식 + 동일 공개 원본소스**만 확인. `research/gounsa_literature/SYSTEM.md`, `MASTER.md` 최신, `INDEX.md` 489 papers /101 models/97 decisions, latest 2025 AHMS-SED strict source and previously ruled-out PSEM_2D (genuine 5cm but canopy missing), Maggioli (5cm kin), Wei2017 TREX forest (90m) 등을 조사 전에 읽어 중복 걸러냄.

## 새로운 peer-reviewed 2005: Raff & Ramírez
- **Raff, D. A., & Ramírez, J. A. (2005)** *A physical, mechanistic and fully coupled hillslope hydrology model*, DOI [10.1002/fld.1016](https://doi.org/10.1002/fld.1016). Wiley 공식 초록을 직접 확인: **genuine 2D full SWE + 1D vertical Richards infiltration + sediment detachment and transport** coupled in one hillslope experiment. Authors give two simulated test problems representing surface organization.
- However **DOI/Wiley accessible abstract neither specifies numerical Δx=0.05/0.10m nor native canopy LAI/interception/throughfall/drip**. Bare-vs-vegetated soil patch effects mentioned in [Ramírez & Raff 2003 project synopsis](../papers/2003_Ramirez_Raff_Evolution_Landscapes_Hillslopes_Project_Synopsis.md) and cannot count as canopy interception without evidence. Wiley full article not freely retrieved. Targeted connected GitHub author/title/flow-erosion search found **no matching full published solver source**.
- A rigorous genuinely full-2D physics reference unlike generic 2D raster routing, **not an installable tested 5cm forest canopy engine**.
- [canonical paper](../papers/2005_Raff_Ramirez_Fully_Coupled_2D_Hillslope_Hydrology_Erosion.md).

## 새로운 published steep mountains vegetation model: Wang et al. (2025) BRIF
- **Wang, F., Ouyang, C., An, H., Chen, X., Zhou, S., & Xu, Q. (2025)**, *Earth and Space Science* DOI [10.1029/2024EA004076](https://doi.org/10.1029/2024EA004076): **BRIF** (Baseflow–Rainfall–Interception–Flood) land-use-dependent native crown fraction+LAI interception, infiltration, GPU 2D **local-inertial approximation** routing. Cutou mountainous (steep) catchment rain events, real computation Δx **2.5m** (6.32M grid elements); V catchment 1m; second watershed 8m. UAV survey DEM 0.3m **NOT** native grid Δx; LAI source 500m.
- Published forest example crown fraction **0.8** and LAI **10**, grass 0.05 LAI2; site land-use table, not universal species calibration. Actual flash-flood discharge validation. **No soil erosion or suspended/bed sediment/distributed deposition process** reported.
- DOI's Data Availability explicitly links author software [`chinafl/HFDM-GPU`](https://github.com/chinafl/HFDM-GPU), Zenodo DOI [10.5281/zenodo.15613301](https://doi.org/10.5281/zenodo.15613301), but **says 'part of core code'**, not entire native solver.
- Direct GitHub connector audit: `test/wind_cuda.cu` SHA `4c4d756f3aba141cb03f3ae451d792ba5fd5f500`, L~932–1099 `V_LAI/V_Smax/V_K` actually set: `V_Smax=0.1713*LAI`, `V_Smax=0.59*pow(LAI,0.88)`, `V_K=1-exp(-V_Cover*V_LAI)` for vegetation-type branches. `test/windmath_cuda.cuh` SHA `69444df5ac1438bf60d4c4104f1d326a6d58ceb4`, L86 kernel `Diff_interception` **prototype only**. Repo's enumerated 8 test files lack matching `windmath_cuda.cu` kernel implementation, while root `hfdm` is non-UTF8 **binary**. **Do not call full CUDA physics open source or build success**; no published sediment kernels in supplied source. Using a vegetation canopy+flooding model to predict erosion would require new coupling.
- [canonical paper](../papers/2025_Wang_Ouyang_An_BRIF_2D_Mountain_Interception_Flash_Flood.md), [direct source audit](../models/BRIF_HFDM_GPU_2025_LAI_2D_Interception_No_Sediment_Code_Audit.md).

## Existing studies expressly not duplicated
- PSEM_2D Nord & Esteves (2005) DOI10.1029/2004WR003690: genuine 5cm SWE+erosion validation but no native LAI canopy, already in `models/PSEM_2D.md`.
- Maggioli 2022 actual 5cm + canopy+erosion but kinematic, exact paper-version unknown. Another Work already handles LISEM.
- Epple 2025 cm-scale new LISEM lacking canopy in used test.
- 2010 Waldmann PROMET erosion module (internal 1m and PROMET 1km grid), already canonical `papers/2010_Waldmann_PROMET_Large_Scale_Erosion.md`; not a new discovery and no free SWE.
- 2026 Braga/Martínez-Aranda/García-Navarro published 2D sediment UWBU high-resolution, **already canonical** `papers/2026_Braga_SERGHEI_SE_Finite_Volume_Evaluation.md`, authors explicitly say future research must handle vegetation. Avoid double counting.
- 2012 MAHLERAN-MiC 30cm movement is kinematic single-direction, canopy absent in validation, already ruled out.
- 2025 AHMS-SED 20km physically active optional NoahMP canopy drip KE but full SWE and cm missing, previous session audited.

## Comparison
| published study | actual native Δx | LAI storage | genuine 2D dynamics | explicit rain/runoff sediment with local deposition | complete paper version source |
|---|---|---|---|---|---|
| Raff & Ramírez 2005 | unknown | unverified | YES full SWE | sediment detachment/transport present; deposition details unknown | source not found |
| Wang et al. 2025 BRIF | V 1m; forest 2.5m | YES canopy module | local inertial (not full SWE) | **NO** | partial CUDA code, missing critical kernel implementation |
| Known PSEM_2D 2005 | 0.05m | **NO** | YES full SWE | YES | entire source not found |
| Known Maggioli 2022 LISEM | 0.05m | YES | **NO** study uses kinematic | YES | exact paper build unresolved |

## Full-code and reproducibility position
Neither newly discovered source simultaneously passes **published native ≤10cm**, quantitative active canopy, true free X/Y hydrodynamics, splash & flow sediment with actual deposition, full publicly rebuildable matching original. This is a bounded negative result **not claim that such model cannot exist**. New Raff gives strong physically all-2D precedent and BRIF gives a published independently confirmed native LAI/forest hydrology precedent with explicitly measured resolution; neither can be prescribed as original forest erosion engine at 5cm.

## Required follow-up target
Seek original same-source **5cm canopy + free2D+sediment experimental run**, ideally per plot paper with source/version and dataset, not program name only. Keep unverified Δx/compiled code unknown and preserve all papers and source SHA.
