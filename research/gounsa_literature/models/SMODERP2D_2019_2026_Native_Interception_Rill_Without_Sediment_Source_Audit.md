# SMODERP2D (2019–2026) 실제 공개 실행코드 기능 검증 — 수관차단/세류유출 있지만 유사박리·퇴적 활성경로 부재

## 학술·출처
- 2019 Landa et al. 공식 FOSS4G 논문 DOI https://doi.org/10.5194/isprs-archives-XLII-4-W14-143-2019 ; [논문별 기록](../papers/2019_Landa_Jerabek_Pesek_Kavka_SMODERP2D_OpenSource_Parallel.md). 7pp PDF web text+page1 screenshot 직접 확인. §2.1 original D8 raster inflow balance, sheet formula and Manning rill, 2019 GPU TensorFlow speed.
- 2022 Kavka et al. [Water 14(3),327](../papers/2022_Kavka_Jerabek_Landa_SMODERP2D_SheetRill_ThreeScaleValidation.md), https://doi.org/10.3390/w14030327; **2×8m simulated rainfall plot; 50m² Wischmeier field plot; 36.6ha remotely sensed rill field with actual 5m simulation raster**, not 5cm and not sediment measured loss per raster.
- 2022 [Neumann doctoral dissertation](../papers/2022_Neumann_SMODERP_Sediment_Transport_PhD_Experimental_Evaluation.md) university publication http://hdl.handle.net/10467/104997 ; >450 rain simulator experiments 2015–2021 slopes4–34° rainfall40–160mm/h, **purpose was building a sediment transport extension into existing runoff SMODERP**. Published thesis/model code integration are different facts.

## Real original publicly accessible code
- https://github.com/storm-fsv-cvut/smoderp2d ; GPL, 2026 repo default `master` source read (no native run). Website https://smoderp.fsv.cvut.cz?lang=en and manual https://storm-fsv-cvut.github.io/smoderp2d-manual/.
- source `smoderp2d/core/vegetation.py` blob SHA `c91b1b7079c4676492d818e1cc3b9c5b197b82be` class `VegArrs(veg,ppl,pi)`; `ppl` Czech note "pomerna plocha listova (leave area index)" = leaf area proportion/input, `pi` maximum potential interception [mm→m]. **Neither a demonstrated real LAI canopy Smax state eq nor a separate growing/crown drop KE code**.
- `smoderp2d/processes/rainfall.py` blob `e4deb1cfb613de89dcd47a2afcaca885d905d07f` lines154–195 `current_rain`: `interc=ppl*rainfallm`; `sum_interception += interc` while not yet saturated; effective rainfall `NS=rainfallm-interc` before saturation or `rainfallm-(pi-sum_interception_pre)` at saturation, returns `NS` for water supply. No canopy drip drainage, leafdrop height KE or evaporative store flux (within this source path).
- `smoderp2d/core/kinematic_diffuse.py` blob `8902dc78d252121b3f9930bb8c228946343f1c86`, `get_kinematic()` and `get_diffuse()` classes **inherit `Mfda` or `D8`** depending `Globals.mfda`. `get_diffuse` updates flow direction from (DEM+h), but **inherits directional raster algorithms**, not a cell-face 2D momentum conservative SWE solver.
- `smoderp2d/core/surface.py` blob `4b325bd5a4c2cf44073a74219b0ebe6b92f3256b` `get_surface(): class Surface(... get_diffuse() or get_kinematic())`, sheet/rill discharge, rill width, rill threshold, CFL water balance.
- `smoderp2d/time_step.py` blob `ef6bf5373512a8b377d15cc8af87158cfef91e3c` 629 lines actual time step imports rain, infiltr, rill, sheet, surface retention, stage and inflow; **no per-grain sediment state concentration, spatial detachment/advection/deposition execution**. Repo code searches `sediment` hit QGIS metadata/plans only, `detach`/ `deposition` returned zero numerical functions, `erosion` hits project name/document strings. **This is a bounded complete active-source search**, not metaphysical proof no private/unreleased solver exists.
- Current `tests/data/reference/test_rill/control_point/` CSV columns `waterLevel, sheetFlow, sheetVRunoff, sheetFlowVelocity, ... rill width`, not mass erosion/deposition/SS.
- `smoderp2d/core/flow.py` D8/MFDA directional inflow not actual free four-edge 2D surface sediment.

## Critical semantic difference
- Developers name it 'soil erosion model' because **rill occurrence and sheet vs rill runoff physically indicate erosion risk** and enable agricultural engineering. However **flow path showing rill hydrograph and rill width != modelling mass of detached soil or deposition**. A 'rill' function name by itself does not mean soil is physically being detached and sent through sediment continuity.
- Paper 2019 abstract describes "soil erosion" but actual printed methods Eqs1–6 only water. Paper 2022 abstract and §3 says rill occurrence classification as a substitute for soil erosion risk, not direct sediment concentration balance.
- Neumann2022 explicit goal to implement sediment process after field data comparison; citation does not prove current 2026 master already has sediment.

## Gounsa strict assessment
| Gate | Source evidence |
|---|---|
| Event-based rainfall | YES |
| Canopy fraction interception first-storage cap | YES, `ppl,pi` |
| Actual LAI-varying canopy hydrological storage/drain and branch drip KE | NOT SHOWN |
| Multi-direction flow | MFDA **route**, not free SWE |
| Rain impact sediment detachment | NO in public active path |
| Flow-induced sediment detachment | NO in public active path |
| Suspended sediment advection/deposition | NO in public active path |
| Actual <=0.10m published numerics | NOT SHOWN; benchmark field grid5m |
| Published forest steep 5cm erosion mass/convergence | NO |
| Whole native 2019 build reproducibility | 2026 public source yes, 2019 tag byte-exact not verified, no run performed |

**Final decision: NO-GO single original 5–10cm LAI+runoff+sediment engine.** Do not send Work to repair it; Work is separately modifying OpenLISEM. SMODERP2D could be an independent *rill-initiation* plot benchmark. If later released sediment module appears, require exact git blob/tag, runtime `time_step` call and published soil mass test, not thesis presence.

## Sources
https://doi.org/10.5194/isprs-archives-XLII-4-W14-143-2019
https://doi.org/10.3390/w14030327
https://dspace.cvut.cz/entities/publication/3155d66e-c8c2-463b-9e5a-72539e77c103
https://github.com/storm-fsv-cvut/smoderp2d/blob/master/smoderp2d/core/vegetation.py
https://github.com/storm-fsv-cvut/smoderp2d/blob/master/smoderp2d/processes/rainfall.py
https://github.com/storm-fsv-cvut/smoderp2d/blob/master/smoderp2d/core/kinematic_diffuse.py
https://github.com/storm-fsv-cvut/smoderp2d/blob/master/smoderp2d/time_step.py
