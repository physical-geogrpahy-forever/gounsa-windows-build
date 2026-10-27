# 2026-10-27 마지막 엄격 검증: 원본 동일빌드, LAI 수관수지, 전방향 2D 유동/침식의 AND 조건

## 사용자 요구 (바뀌지 않음)
- **단일 기존 발표 모델과 실제 원본 프로그램**. 단순 서로 다른 논문식이나 패치한 모형을 기존 단일원본으로 속이지 않음.
- 5–10cm 실제 계산 격자와 6h, 강우강도 10–50 mm/h, 2D 사면에서 네 면 자유 유출.
- 나지, 억새, 어린 참나무 맹아 및 모자이크의 LAI 기반 수관차단 저장/수관통과, 임의 수간유하 추가보다 잎 낙수와 원래 runoff-induced detachment 중요.
- 명시적 rain-impact and direct runoff detachment plus sediment x/y flux, local deposition, nonnegative water/sediment and mass/soil-stock closure, event-based numerical stability.

## 마지막 새 계열 SRH-W (기성 논문 vs 공식 프로그램)
- [Lai (2009) canonical](../papers/2009_Lai_SRH_W_HybridMesh_2D_Watershed_Erosion.md), https://doi.org/10.1061/(ASCE)1084-0699(2009)14:1(15). 2D hybrid mesh conservative finite-volume hydrologic/erosion *research paper* exists, verification cases in abstract.
- Official U.S. Bureau of Reclamation `SRH-W v1.1` **2006–2007 manual** at https://www.usbr.gov/tsc/techreferences/computer%20software/models/srh2d/downloads/SRH-W%20v1.1%20User%20Manual%20June2007.pdf §1.3 explicitly "Only flow hydraulics and water runoff are modeled. Erosion and sediment transport are not available at present;" and "Only the flow routing module has been developed and released." Thus **2007 publicly documented executable did not implement 2009 paper's erosion extension**. This is version difference, not proof 2009 article never developed software.
- Manual §4/5 `LAND USE PROPERTIES` includes roughness and rainfall-interception **depth**, not shown LAI dynamic canopy reservoir/leaf-drip impact KE. Official 2007 PDF hosted 11.8MB, web open rejected file size; indexed passage examined, exact all-page visual not.
- Later government public `SRH-2D 3.3.1` with sediment executable and manual at https://www.usbr.gov/tsc/techreferences/computer%20software/models/srh2d/index.html is river-oriented distinct distribution. Its existence **does not prove original SRH-W forest 2009 code is released**.
- Native 2009 model complete source/runfiles, canopy and 5cm actual grid not identified; excluded as user's original directly executable program.

## Another code discovery screened without false publication status
- GitHub repository [Daishubinghydraulic/Shallow-water-equations-with-Hairsine-Rose-soil-erosion-equations](https://github.com/Daishubinghydraulic/Shallow-water-equations-with-Hairsine-Rose-soil-erosion-equations) README verified git blob `1ffff75bfe2426bf1d9a3ba8bfe99c4892bcc5fe`. Claims author VBA-in-Excel hill slope shallow water + HR equation for manuscript `Roll-Wave Evolution in Sediment-Laden Overland Flow Using a Coupled Shallow-Water–Sediment Model` **submitted** to WRR. Manuscript acceptance/peer-review published DOI NOT verified, no source code inspected except README, no canopy/2D xy mesh or complete executable source provenance. **Do not count as peer-reviewed and do not treat an Excel roll-wave workbook as genuine 2D canopy erosion program.**

## Previously actual-source verified most relevant branches (verified archive, not newly rerun)
| Model original code | Actual native code strength | Fatal missing link |
|---|---|---|
| **Classic OpenLISEM 7.5.2** | canopy LAI storage/throughfall and 2D runoff & sediment source available; several published TLS 5–10cm LISEM studies exist but hydraulic solver options differ | previous actual native Windows 12-run erosion numerical failure; academic 5cm kinematic studies cannot prove 5cm 2D dynamic stable. Work separately repairing/reproducing, **not succeeded in this investigator session** |
| **SHETRAN v4.7.2** | actual Fortran hydrology canopy store and rain/drip sheet detachment and sediment native routines, site mountain references | no published successful native 5–10cm source-and-case, doubtful localized rills; previous project NO-GO; do not reselect without evidence |
| **Deltares/Wflow.jl** | native code joins LAI canopy/Gash/Rutter→throughfall, direct and leafdrip KE→EUROSEM rain detachment, ANSWERS flow detachment, river sediment | overland sediment actual `accucapacityflux_rate!` through LDD/directed stream network, not full freely spreading 2D sediment |
| **SWAT+ subdaily** | `src/ero_ovrsed.f90` actual LAI canopy leaf KE and subdaily raindrop+runoff detachment | HRU spatial averaging, not genuine 2D mesh or 5cm |
| **Le et al.(2015) FullSWOF-HR** | published 2D finite-volume Hairsine-Rose multi-grain stable nonnegative precipitation and stream erosion model | 2015 HR extension source not in public 2016 `BUCEA/FullSWOF_Rif` base; no LAI canopy or verified cell5cm; 2D published trial flow erosion negligible |
| **psu-efd/HydroSed2D v1.0** | native v1 Fortran 2D unstructured SWE + MPM/Grass bedload + Exner actual call graph | no rainfall, canopy and rain detachment in released input/main loop. Potential dry-cell division risk not proven bug |
| **CASC2D-SED** | full archive original C active runoff and sediment/deposition | landuse **fixed** interception only, single outlet, no explicit rain splash, 30–330m case |
| **tRIBS-FEaST published 2013** | papers have 2D Roe finite volume + HR and forest hydrological Rutter source | current official tRIBS source no published FEaST sediment kernel, exact compiled source missing |
| **2017 Wei TREX** | one published forest hydrology/interception + 2D diffusion + rain and flow erosion and deposition model | published 90m, matching upgraded 2017 code not located, no real 5–10cm numerical proof |
| **2018 Eekhout SPHY-MMF** | published dynamic LAI Cmax and leafdrip energy, actual source original 2018 archive | time step daily, 200m cells, LDD routing instead of xy free flow; 2026 KE function differs |
| **2009 SRH-W** | 2009 published 2D hybrid mesh and erosion concept | 2007 available program hydro-only, exact 2009 paper erosion source/unstructured 5cm/LAI unverified |

## Honest strict outcome
**0 independently confirmed publicly released and field/numerically proven all-gates model** after examining original published source/runtime path across separate lineages. This is not proof no model exists anywhere: it is an empirical search result. More paper titles without code are *not a solution*. User's only conditionally plausible exact single model remains Classic OpenLISEM lineage pending other Work native test **that must reproduce 10cm and 5cm 2D dynamic canopy-on and -off storm, soil sediment closure**. Until Work returns actual checks, can't claim ready engine. This session's new SRH-W provides an additional code-release version mismatch and excludes the unverified published model.

## Native acceptance checklist (mandatory before any adoption)
1. Article actual numerical Δx/dy and model version tag + executable and original source SHA.
2. Source call-graph shows rain→LAI dynamic canopy store→throughfall/leafdrip water reaching soil→hydraulics and rain-splash (not cover-factor surrogate).
3. Actual 2D h,u,v conservative face flux and sediment species transport/deposition, flow detachment active and rain-detachment active on a test with separately measured contributions.
4. Multi-outlet freely open four edges explicitly config + exact sediment and water export closure.
5. Actual native 10cm and 5cm, dt/CFL refinement, positive h & c, bounded erodible soil and realistic signed DoD changes for 6h 10/30/50mm/h events.
6. If any missing, model excluded, not fixed by verbal promise or merging another model unacknowledged.

## References
https://doi.org/10.1061/(ASCE)1084-0699(2009)14:1(15)
https://www.usbr.gov/tsc/techreferences/computer%20software/models/srh2d/downloads/SRH-W%20v1.1%20User%20Manual%20June2007.pdf
https://github.com/Daishubinghydraulic/Shallow-water-equations-with-Hairsine-Rose-soil-erosion-equations
