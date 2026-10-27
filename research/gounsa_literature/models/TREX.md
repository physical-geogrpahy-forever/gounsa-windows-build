## 2026-10-28 published forest TREX vs original public CSU source executable path recheck
- Public original C source https://github.com/WatershedModels/trex_src_csu confirmed actual src/Makefile.gcc includes 2D source src/Interception-r4.c, src/WaterTransport-r4.c, src/OverlandSolidsErosion.c, src/OverlandSolidsDeposition.c, src/SolidsTransport.c. So historical TREX does indeed have native *simple interception and overland erosion/deposition* in the same source tree, not just docs.
- Native src/WaterTransport-r4.c invokes Rainfall(); Interception(); Infiltration(); OverlandWaterRoute();. Interception-r4.c computes remaining canopy interception depth and net rainfall; it is a threshold/bucket, **no native LAI time dependency/throughfall drainage/leaf kinetic energy** shown.
- Native src/SolidsTransport.c invokes deposition, advection, dispersion, transport capacity, then erosion. In src/OverlandSolidsErosion.c actual flow soil detachment depends on hydraulic friction slope, total vs grain shear, barefracov partition and available mass of sediment. Code query across public repo for `Splash` and `drip` returned **no matching source files or strings**. Neither grossrainrate nor netrainrate appears in src/OverlandSolidsErosion.c itself. Thus original CSU code is not a verified explicit rainfall splash/leafdrip erosion program; this differs from published 2017 Wei forest-improved study requirements.
- This official-looking older source is not demonstrated identical to Wei et al. 2017 author forest improved variant; source files include 2017 revisions but these are not proof of same modified publication source. No gcc full native build or 5/10cm performance performed.
- Verdict for user's strict needs: SOURCE EXISTS, 2D flow + native runoff erosion/deposition EXISTS, interception simple bucket EXISTS, but explicit native rain/drop detachment and LAI canopy detailed physics NOT VERIFIED / absent from inspected code. Thus do not re-promote as full-pass.
# TREX: Two-Dimensional Runoff, Erosion and Export

## 2026-10-26 current audit
Identity: original Colorado State University Velleux / England / Julien 2008, event-scale 2D overland / 1D stream, rain-on-grid, interception as equivalent depth, infiltration, distributed erosion deposition and bed-elevation adjustment. Original development from CASC2D.

## Native candidate status
- Source: [official TREX site](https://www.engr.colostate.edu/~pierre/ce_old/Projects/TREX%20Web%20Pages/TREX-Home.html) advertises complete source and hydrology/sediment example ZIP but actual original C source archive download/contents **not yet independently verified** (403 on web view, no source fetched into runtime).
- Numerics: actual source numerical stability and mass balance **NOT TESTED**. Do not repeat OpenLISEM error of recommending on model-paper features only.
- Genuine 2D: yes in published overland flow, but source numerical routing kind must be read prior to claiming full 2D dynamic SWE.
- Native LAI dynamic canopy and leaf drip impact: **UNCONFIRMED / NOT ESTABLISHED**, current published TREX model says canopy interception and surface storage equivalent depths. This is a major gap to user criterion.
- Ground cover/root or litter biomass as explicit quantitative state: no verified native process.
- Forest/mountain: Fukushima forested catchment 2017 via model adaptation; Naesung River Korea 2014 cited on developer site; distinct from original release's own validated scenarios.
- Exner/topography: developer site says bed elevation adjustment; verify that actual hillslope grid DEM is dynamically updated, not just channels, before claiming on-event feedback.

## Decision
Not selected; new original-source candidate in source retrieval tier. If canopy is purely depth parameter, rank behind fully vegetation-aware possible alternatives for single-native criteria. No new calibration until source/LAI+drip+sediment checks.

## Papers
[2008 Velleux et al](../papers/2008_Velleux_England_Julien_TREX_2D.md)


## 2026-10-26 **strict original-source recheck overrides earlier 'archive unavailable'**
**Actual full source found, reviewed**: [WatershedModels/trex_src_csu](https://github.com/WatershedModels/trex_src_csu), preservation copy of CSU original TREX; README claims source version `101017` updated 2018-05-18, pinned commit `5cfe714557333ecf8062ac04b5fba3165906a775`. `src/` directory contains 233 entries including original 2D overland C, solids and chemical transport, makefile. There is no excuse to say code unavailable. It is a third-party **archival mirror** of CSU source, not verified official-author release from CSU website; no original exe and no numerical test carried out.

Code-level ground truth:
- `src/Interception-r4.c` is **fixed remaining interception depth** deduction: `netrainrate = grossrainrate - interceptiondepth/dt` when rainfall fills it; otherwise 0, no active canopy LAI-driven storage/drain/release cycle, no throughfall vs leaf-drip kinetic energy.
- `src/OverlandSolidsErosion.c` flow sediment detachment, multiple transport-capacity/shear options, native `available` mass cap limiting potential erosion to physically available soil mass. This is better than OpenLISEM finite-material unbounded 7.5.2, but does not fix missing canopy physics.
- `src/OverlandWaterRoute-r3.c` grid-face 2D overland routing; no proof complete dynamic SWE.
- GitHub default-branch scoped code search: `throughfall`, `drip`, `raindrop`, `splash` returned no indexed original source matches; `canopy` matched only solar-radiation comment. Search-based absence is corroborating, not standalone proof.
- Full original code checked for these fundamental missing native capabilities, without creating a new canopy patch or claiming implicit LAI from landuse.

**STRICT GO/NO-GO: Reject TREX as Gounsa standalone original engine.** Failed primary quantitative LAI canopy interception/leafdrip criterion regardless of its excellent two-dimensional runoff + sediment source availability. Do not spend additional days building/test-run before features. Earlier statement that original source had not been located is superseded by this recheck, not a license to elevate TREX.

## 2026-10-27 **신규 2017 후쿠시마 단일 수관차단-강우 및 유수 박리+2D 퇴적 학술 선례**
- [Wei et al.(2017), J Hydro-Environment Research, 17, 18–29](../papers/2017_Wei_Kinouchi_Velleux_Fukushima_TREX_Forest_Interception_2D_Erosion.md) https://doi.org/10.1016/j.jher.2017.09.003 원논문 §4.1의 **2D overland diffusive-wave**, XY sediment continuity Eq1, 비세류 rain splash source Eq2 ∝ (net rainfall)² × (1-kv), flow erosion/deposition Eq3 ∝ αwv_s(Cm−Cs), land-use vegetation fraction, existing **hydrologic interception + ET**, subsurface/groundwater까지 **하나의 2017 모델 연구에서 사용됨**. Wei & Kinouchi(2014) forest hydrology improvement를 직접 연결해 서술. 실험은 Fukushima 137km², **90m DEM 계산격자**, 실측 유량/SSC/turbidity/size class time series + 공간순침식/퇴적 hotspot.
- 이것은 2014 forest hydrology와 옛 USLE C/P 기반 CASC2D-SED original sediment architecture를 어림짐작 결합한 것과 달리, **2017 실제 published integrated canopy-hydrology/2D sediment same research paper proof**임. 따라서 연구계보 **논문기능 미구현**이라고 일반적으로 비하해서는 안 됨.
- 그러나 원본 2017 updated TREX **exact source SHA, runfiles, canopy C(t)/drainage source, 5–10cm numerical benchmark** 전부 확보 못함. 2017 paper의 q_x,q_y = diffusive XY not full Saint-Venant momentum; canopy-drip energy separate no evidence. Archived `WatershedModels/trex_src_csu` `Interception-r4.c`에는 LAI dynamic capacity 없음; **2017 개선형을 2018 CSU archival source와 혼동 금지**. 따라서 user's strict reusable 5cm native program NO-GO 유지.
- [동년 companion 137Cs paper](../papers/2017_Wei_Kinouchi_Yoshimura_Velleux_Forested_Cesium_TREX.md) DOI 10.1016/j.jenvrad.2017.01.017의 수관 `137Cs washoff`는 **강우 수관저류 water budget와 다른 과정**; 둘을 동일시하면 안 됨.
