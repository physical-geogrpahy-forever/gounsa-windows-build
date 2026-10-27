# 2026-10-27 22:52 이후 독립 원본코드 심층감사: HydroSed2D 및 Le(2015) FullSWOF-HR

## 사용자 지시
Work는 원본 OpenLISEM 수치수정 담당. 본 세션의 과업은 기존 모델과 다른 연구 탐색, 반드시 공개 source와 실제 호출경로를 검증. 이 세션은 Classic OpenLISEM 빌드나 수정에 개입하지 않음.

## 수행한 실제 코드 읽기
- GitHub 공식 `psu-efd/HydroSed2D` v1.0 Full Fortran source `swefvm.f90`, `swe.f90`, `sediment.f90`, `initialization.f90`, `module.f90`, `auxsubs.f90`, `auxfuncs.f90`, `buildMeshData.f90`, `restart_output.f90`, `results_output.f90`, `readGambitMesh.f90`, `readGMSHMesh.f90`, `Makefile.gfortran` 등 직접 connector로 획득 및 검사.
- `swefvm.f90`: event-time loop calls `swe()` then optionally `sediment()` only when `sedimentctl==1 && scalc==1`; no canopy/interception/effective rain or rainfall source.
- `sediment.f90` source: stress→Shields→single grain MPM/Grass bedload xy face/edge flux→Exner bed z update. Bedload physical flux yes, raindrop splash and concentration-class HR no. `calc_shear()` unguarded division by water depth Q1^(4/3) possible dry-cell numerical risk, **not proven actual failure**.
- `initialization.f90` loads inlet/outlet h,u,v,Q, mesh, dt, sediment.dat `diam,porosity,Shields,Grass parameters`, NOT LAI/canopy/rainfall.
- Existing [HydroSed2D model record](../models/HydroSed2D_Fortran_Original_Source_Audit.md) already existed from other project actor, appended observations instead of duplicate. Model source exact public but no native downloaded/compiled here: Linux container gfortran exists but DNS to GitHub codeload failed.

## Newly discovered scientific paper and code identity
- [Le, Cordier, Lucas, Cerdan (2015)](../papers/2015_Le_Cordier_Lucas_Cerdan_FullSWOF_HairsineRose_2D_Sediment_Splitting.md), DOI10.1002/2014WR015690, WRR51 987–1005. Full publisher HTML methods §2–4, 2D test/limitations directly verified.
- Full 2D SWEs+HR multiclass sediment in journal research: h,u,v, concentration c_i, deposited m_i, rain detachment and water stream-power entrainment, cover by deposited particles, deposition. Numerical Strang split gives sediment positivity under water CFL alone; reported tested 100x speed advantage.
- 2D dataset Thiès Senegal experiment 10m×4m, V-shaped 1% longitudinal+1% transverse, 70mm/h 120min, 10 grain classes 10–1000μm. Actual published grid cell size dx/dy unavailable in accessible text, do NOT claim 5cm.
- **Crucial section 4.3**: water shallow and stream power below entrainment threshold, therefore *the 2D case has essentially no flow-driven sediment detachment*, rainfall impact is dominant, flow advects sediment. So publication does not establish both source terms significant and tested for steep gounsa.
- Public [FullSWOF 2D](https://github.com/BUCEA/FullSWOF_Rif) v1.07.00 2016 original baseline Makefile compiles hydrology+rain/infiltration/boundary/SW solver only, NO Hairsine-Rose sediment lib. Article study says authors 'add erosion component to SW code'; exact 2015 modified branch/files with HR not deposited in located public archive. [Detailed source-release audit](../models/FullSWOF_2D_2015_Le_HairsineRose_CodeLineage_And_Numerical_Gates.md).

## New decisive source verdict
- [Le2015 vs HydroSed2D code-level decision](../decisions/2026-10-27_FULLSWOF_HR_LE2015_VS_HYDROSED2D_NATIVE_2D_SOURCE_GATE.md). Two real 2D systems: HydroSed2D released Fortran bedload Exner but no dynamic rain/canopy and raindrop; Le2015 paper HR rain + flow equations/dep but matching compiled source not public and no canopy.
- This follows the user's rule: source existence cannot be inferred from paper wording and baseline package cannot be portrayed as modified study version.
- New academic paper file x1, model source audit x1, existing HydroSed2D updated, decision x1, MASTER and INDEX updated. At commit time INDEX: Papers507, Models110, Decisions107. Other concurrent actors update repository frequently; re-read index before next action.

## Next research gate
- Seek *actual deposited modified* FullSWOF-HR C++ (not just baseline) and author case data with valid source hash to clarify source limitation. If none, archived no-go.
- For any original 2D sediment solver, inspect main-step forcing `rain->canopy storage->throughfall->splash`, 2D h,u,v and interface flux, sediment c_i/Exner/source at actual same executable SHA. Need 5–10cm published mesh not just TLS/UAV DEM.
- Don't recommend hydro-only, bedload-only or source-less papers as ready single canopy/rain/flow erosion original. Classic OpenLISEM stability patch remains with separate Work.
