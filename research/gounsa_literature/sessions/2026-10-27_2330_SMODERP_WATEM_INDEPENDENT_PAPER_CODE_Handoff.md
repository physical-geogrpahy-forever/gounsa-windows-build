# 2026-10-27 독립 논문 및 원본 GitHub 소스 검증 세션: SMODERP2D와 WaTEM-SEDEM

## 시작 작업
사용자는 OpenLISEM 기존 수정·고해상도 native 시험을 별도 Work로 맡기고 다른 기존 학술 모델 찾기를 계속 지시. 반드시 고운사 GitHub SYSTEM/MASTER/INDEX/현재 결정 읽고 중복 후보를 피함. 이 세션은 LISEM 코드를 건드리지 않았음.

## 신규 논문/학위논문 4건
1. [Landa et al.(2019)](../papers/2019_Landa_Jerabek_Pesek_Kavka_SMODERP2D_OpenSource_Parallel.md), doi10.5194/isprs-archives-XLII-4-W14-143-2019. Public full PDF/screenshot inspected. Real published 2D raster D8 rainfall/runoff/critical rill/CFL and GPU parallel implementation, no active soil sediment equation shown.
2. [Kavka et al.(2022)](../papers/2022_Kavka_Jerabek_Landa_SMODERP2D_SheetRill_ThreeScaleValidation.md), doi10.3390/w14030327. Original publisher HTML indexed Methods: artificial plot2×8m 60mm/h for30min, natural runoff plot~50m², field36.6ha rill map model mesh **5m**, not 5cm. Calibrated runoff and rill occurrence, not actual sediment deposition/soil mass.
3. [Neumann (2022) PhD](../papers/2022_Neumann_SMODERP_Sediment_Transport_PhD_Experimental_Evaluation.md), hdl10467/104997. Research 450+ rainfall simulator tests (slopes4–34°, rain40–160mm/h) and soil transport capacity K-R formula empirical crop CS protection. Explicit 2022 thesis abstract: current SMODERP had rain-runoff, sediment process sought as addition. **Dissertation prototype != current published compiled active sediment module**.
4. [Van Rompaey et al.(2001)](../papers/2001_VanRompaey_Verstraeten_VanOost_WaTEM_SEDEM_AnnualSediment.md), doi10.1002/esp.275. Historical annual soil loss spatially distributed, not event. Current KU Leuven source is materially later.

## New public source entire computational process audited
### SMODERP2D
- Official https://github.com/storm-fsv-cvut/smoderp2d; `processes/rainfall.py::current_rain` proportional leaf-area `ppl*rain` bounded `pi` static maximum storage, no dynamic canopy-drain/leafdrop KE.
- `core/kinematic_diffuse.py` `Kinematic/Diffuse(Mfda if Globals.mfda else D8)`, flow remains **directed** despite raster format; `time_step.py` active 629 lines water sheet/rill/infiltration/no sediment detachment/advection/deposition function; code searches `detach` `deposition` zero computational matches. Does NOT meet independent rain+flow sediment process. [model audit](../models/SMODERP2D_2019_2026_Native_Interception_Rill_Without_Sediment_Source_Audit.md), [decision](../decisions/2026-10-27_SMODERP2D_ACTUAL_SOURCE_RILL_RUNOFF_NOT_SEDIMENT_NATIVE_NO_GO.md).

### WaTEM/SEDEM
- KU Leuven official https://github.com/watem-sedem/watem-sedem; Free Pascal LGPL3, Windows/Linux releases, archived v5.0.1 https://doi.org/10.5281/zenodo.10997288.
- `common/runmodel.pas` DEM routing and RUSLE LS; `docs/watem-sedem.rst` annual RUSLE soil loss E=R K LS C P, `docs/routing.rst` directional flux to 1 or 2 neighboring cells, `docs/formulas-units.rst` min(incoming+gross, TC) per grid, real net erosion and deposition, but **annual and cover-C only**, no subhourly rainfall canopy states/drip KE/XY momentum. [model audit](../models/WaTEM_SEDEM_2024_Pascal_Native_Annual_RUSLE_Sediment_Audit.md).

## Final comparison and results
[Both-source decision](../decisions/2026-10-27_SMODERP2D_AND_WATEM_SEDEM_PUBLIC_SOURCE_COMPLEMENTARY_GAPS.md): SMODERP2D has native event hydrology/rill but no sediment mass; WaTEM has native sediment mass/deposition but annual raster routing/no event canopy/hydrodynamics. **Both NO-GO** strict gounsa user original 5–10cm canopy/throughfall/drip impact, 4-edge 2D free run, rain/flow detachment and local sediment conservation.

## Files written
- Papers: 4 paths above
- Models: 2 paths above
- Decisions: 2 paths above
- MASTER.md notes new source lines, INDEX.md reindexed at execution: **Papers501, Models105, Decisions103**. Note concurrent Work workflows occasionally commit during research, must re-read actual index at next start.
- Sessions: this file

## Remaining gaps
- Need actual runnable SAME publication-version source and cm simulation with real LAI canopy/impact + free 2D SWE/flow detachment/deposition and stable mesh/timestep soil mass. Not found yet.
- Already screened Kim(2013) tRIBS-OFM/FEaST, Long & He(2009/10), PSEM2D 5cm, Maggioli LISEM5cm, Epple new LISEM1cm, SHAETRAN cm paper absent, Classic openLISEM7.5.2 numerical failure, SPHY-MMF daily, AHMS-SED20km, TREX2017 90m, CASC2D-SED and other screened 2D source. Do not repeat as novel without a new exact source.
- Work is responsible only for OpenLISEM source fixing; this transcript supplies complementary independent literature info without adding ad hoc coupling.
