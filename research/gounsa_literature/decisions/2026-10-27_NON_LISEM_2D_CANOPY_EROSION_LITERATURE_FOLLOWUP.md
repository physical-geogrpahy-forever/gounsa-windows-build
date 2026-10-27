# 2026-10-27 독립 문헌조사: OpenLISEM 제외 2D 식생수관 및 강우 유수침식 기존 연구

## 명시적인 조사 범위
OpenLISEM 소스빌드, 분기 검증, 수치오류 진단 및 5/10cm native test는 **다른 Work 담당**. 본 조사는 다른 학술 모델, 기존 원본 공개 여부, 실제 사용 해상도와 직접 과정만 검토한다. `SYSTEM.md`, `INDEX.md` (시작 473 papers/97 models/90 decisions), 최신 기존 strict audits 먼저 확인하여 같은 논문 중복 생성 금지.

## 논문별 확인 결과

### 1. Abrantes, Simões, de Lima & Montenegro (2021)
DOI https://doi.org/10.2478/johh-2021-0003
- 2.00×2.00m laboratory **two-directional slope flume**, X 1%, Y 10%. Actual two-direction discharge/sediment output measured separately, Y direction good, low X direction underestimated. Cross-axis + total sediment/rainfall hydrograph data validation published.
- Active paper physics: 2D unsteady overland flow, Horton–SCS infiltration, 2D sediment equation, rill / interrill detachment and deposition.
- **No published demonstrable canopy LAI bucket or leaf-drip process.** DOI paper full-text PDF is listed as open access but current web retrieval returned octet-stream and local download inaccessible, so exact `Δx`, timestep and full SWE vs wave-approx have **not been audited to equation level**. Physical plot 2×2m is not proof native 5cm compute.
- GitHub searches exact DOI and author title yielded no matching complete numerical source in checked results.
- [Canonical paper](../papers/2021_Abrantes_Simoes_2D_Experimental_Two_Direction_Erosion.md). **Important two-outlet physics reference only, no standalone Gounsa candidate.**

### 2. Hinsberger & Yörük (2025): HydroAS GS–Govers
DOI https://doi.org/10.1007/s40710-025-00797-9; full original Springer HTML verified. FVM 2D SWE rain-on-grid + Govers transport capacity + Exner sediment bed evolution, multiple field rill observations. Source was **cm-resolution survey DEM**, but **0.25m and 1m actual computational meshes**, not 5–10cm.
- The actual paper uses **effective rainfall with infiltration excluded** and **raindrop splash omitted** (see source original §2/§3). No LAI canopy storage and leafdrip.
- Official vendor https://www.hydrotec.de/software/hydroas-en/ offers commercial licenses and separate GS sediment module, downloadable releases require authorized user login; **not a publicly editable original source**. Proprietary status independent from ability to operate a licensed executable. Source same-version program not found.
- Smaller 25cm grid predicts small rill erosion more accurately than 1m; larger rill needs calibration transport-capacity scale factors 10/1.2/3 depending on fields.
- [Canonical paper](../papers/2025_Hinsberger_Yoruk_HydroAS_2D_Rill_Erosion_025m.md), [Model native audit](../models/HydroAS_Govers_2D_Sediment_NonOpen_Canopy_Audit.md). **Relevant quantitative morphodynamics reference, not native all-pass.**

### 3. Mueller, Güntner, Francke & Mamede (2010): WASA-SED
DOI https://doi.org/10.5194/gmd-3-275-2010, official original source https://github.com/TillF/WASA-SED, README, original `docs/index.md`, `src/Hillslope/soilwat.f90` blob SHA `536d2392c441988f43899fbbf25fcb9c9191a767`, `src/Hillslope/sedi_yield.f90` blob SHA `43af5642e1879ad7794f47299dbf5b7234256ad8` explicitly read.
- Version1 original GMD + newer 2025 manual. **Source fully public Fortran, compiler Makefile and tutorials, LAI + native interception, downstream sediment and reservoir storage are true.**
- However `soilwat.f90` L50 etc routed `q_surf_in`→`q_surf_out` as terrain components; `sedi_yield.f90` L181–195 `USLE / Onstad-Foster / MUSLE / MUST` erosion, subbasin/LU/TC/SVC hierarchical **semi-distributed model**. This is neither genuine XY 2D SWE nor 5cm grid face sediment and morphodynamics.
- Physical application 445km² Isábena catchment, river/reservoir sediment. **Source PASS, hard 2D resolution FAIL.**
- [Canonical](../papers/2010_Mueller_Guntner_WASA_SED_Dryland_Sediment.md), [Code audit](../models/WASA_SED_2026_Public_Fortran_Canopy_Erosion_Source_Audit.md).

### 4. Downer, Pradhan, Ogden & Byrd (online 2014, issue 2015), GSSHA erosion sensitivity
DOI https://doi.org/10.1061/(ASCE)HE.1943-5584.0001104. USACE original GSSHA 2D diffusive-wave rainfall-runoff, infiltration and sediment; paper documents historical CASC2D-SED large storm **strong sediment overprediction beyond calibration event**, and evaluates detachment limit/transport capacity approaches. Full numerical after/before not audited (abstract only). Coupled surface cover factors are **not verified native LAI storage and leaf-drip KE**, and 5cm published source unconfirmed.
- `CI-WATER/gsshapy` Github source is Python model input/ORM, **not original GSSHA solver**.
- [Canonical](../papers/2014_Downer_Pradhan_Ogden_Byrd_GSSHA_Sediment_Transport_Limits.md).

### 5. Raza et al. (2021) systemic review
DOI https://doi.org/10.3390/land10040422, 51 soil erosion models compared. Explicit lack in mature field-scale models for complex patch cropping and multi-D sediment with canopy interception, but a 2021 review is not proof post-2021 integrated code never exists.
- [Canonical](../papers/2021_Raza_Ahrends_Field_Erosion_51_Model_Review.md).

## Previously archived (not new discoveries)
- Wu et al. (2020) *J Hydrol* DOI 10.1016/j.jhydrol.2019.124346, 2D diffusive wave + two-layer infiltration + modified WEPP rill/interrill erosion; existing `papers/2020_Wu_Two_Dimensional_Rainfall_Runoff_Soil_Erosion.md` and `models/Wu_2D.md`, **no native LAI canopy identified**. Not relabelled as new.
- 2024 Iber+ and 2005 PSEM_2D are previously archived, hydrodynamics and erosion strong but canopy/native code issues; unchanged.
- New LISEM is assigned Work and excluded from this audit intentionally.

## Cross-model comparison and selection
| Origin | Native canopy interception | XY bidirectional hydrodynamics | Rill/interrill erosion+deposition | Exact published 5/10cm | Public same executable/source |
|---|---|---|---|---|---|
| Abrantes2021 | not shown | YES for 2D unsteady flow, exact SWE full math TBD | YES | mesh size not verified | no matching complete source found |
| HydroAS2025 | not shown | YES SWE | YES rill TC+Exner, **splash excluded** | NO; actual min 25cm | NO proprietary |
| WASA-SED2010 | **YES** via LAI interception | **NO**, semi-distributed TC runoff | hillslope USLE family, not dynamic XY sediment | NO | **YES** Fortran GPL? NO: project license CC-like customized |
| GSSHA2014/2015 | canopy cover factor in erosion, LAI actual reservoir unknown | 2D **diffusive** (not full SWE) | YES within GSSHA sediment | NO example confirmed | gsshapy only input helper, original solver source not established |

**No new full-pass original, 5–10cm native vegetation-interception/free-2D rainfall+flow erosion code.** Records are bounded documented negative results, not proof impossible. Crucial: do not substitute a C++/Fortran repo that has interception and "erosion" for a true 2D sediment solver, or a published cm DEM for computational mesh.

## Independent next research priority
- New high-resolution full paper **with native canopy on, real X/Y 2D flow + sediment and a publicly accessible matching solver** only; search supplements/code mirrors and actual scientific validation. Do not send source debugging tasks back to the parallel Work on LISEM, and do not introduce user-unapproved new coupling.
