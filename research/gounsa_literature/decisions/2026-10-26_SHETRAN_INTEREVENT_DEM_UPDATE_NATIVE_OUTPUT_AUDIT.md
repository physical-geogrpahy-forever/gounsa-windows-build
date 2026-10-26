# SHETRAN: 강우사상 종료 후 DEM 및 토심 갱신 가능성, 원본 출력 및 재시작 상태 정밀검증 (2026-10-26)

## 결론
**사상별 DEM 갱신은 원리적으로 가능하며 원본 SHETRAN의 공개 입력/출력 경로가 실제 존재한다.** 매 사상 내부의 수리-침식 동시 지형피드백이 없다는 이유만으로 이 모델을 연구에서 제외해서는 안 된다. 단, 현 원본의 표준 hotstart는 sediment 입경 상태를 보존하지 않으므로 DEM만 교체하면 **물리적으로 동일한 다사상 연속계산은 불가능**하다. 원본을 고치지 않는 이벤트 간 외부 후처리 도구는 실제 개발했고 단위시험 4/4를 통과했지만, 아직 실제 SHETRAN 원본 예제 HDF5를 읽어 일련의 사상을 실행한 것은 아니다.

## 원본 버전과 근거
SHA `cf9cd540add78ad3accbaf62b4199d2032887f6b` SHETRAN v4.7.2 Fortran, https://github.com/nclwater/Shetran/tree/cf9cd540add78ad3accbaf62b4199d2032887f6b .
- 공식 매뉴얼 https://research.ncl.ac.uk/shetran/SHETRAN%20V4%20User%20Guide.pdf , 표 Fig2.3 / section 3.1, FR37-FR39 ZGRUND.
- 공식 Sediments & Snow 사용안내 https://research.ncl.ac.uk/shetran/Shetran%20Easy%20Setup-%20sediment%20and%20snow.pdf , pages 2–3, original Aire sediment-on HDF5 input plan.
- 원본 `src/visualisation/visualisation_interface_left.f90` L1020–1040: `s_t_dp = DLS*1000` [mm], `s_v_er=GNU*86400*1000` [mm/day]. **원본 SYOVER의 GNU=(DR+DF)/RHOSO≥0, 즉 총원토양 박리속도이다.** Visualisation 주석이 'signed erosion/deposition velocity'라고 부르더라도 실제 해당 원본 SYOVER 계산식에는 음의 deposition rate가 없음. `s_t_dp`는 각 격자 퇴적층 총 두께, 유사수송 모델 `SYCOLM`이 갱신함.
- `src/visualisation/visualisation_interface_centre.f90` L147,L151 and L310–312: `s_t_dp, s_v_er, s_dis` available in original HDF5; `s_dis` per-face per grain size [kg/s].
- official `examples/Aire_at_Kildwick_Bridge-AllOptions-withdates/model/input_Aire_at_Kildwick_Bridge_visualisation_plan.txt` items 14/15 (s_v_er / s_t_dp) as `BASIS^grid_as_grid : SCOPE^squares`; original Cobres equivalent items13/14. Native HDF5 output file `shegraph.h5`. Visualisation sampling times configured via TIMES pattern; source `s_v_er` = instantaneous GNU at output step, **not pre-integrated hourly/event mean**.
- `src/frame/FRmod.f90` L5628–5630 `CALL AREADR(ZGRUND,..., FRD)` loads original grid elevations. User Guide FR37 title, FR38 row index descending, FR39 `(10G7.0)` elevations m.
- `src/sediment/SYmod.f90` `SYCOLM` L1187–1295 uses `DDLS=FETA*GNU*DTSY`, `DLSE=(1-A1)*VDSUM/AREAE`, `FBETAE`, `FDELE`, `QSEDE`; `FETA=(1-THSAT)/(1-PLS)` L2979 adjusts bulk soil to loose sediment porosity. Therefore loose layer change `DLS_end-DLS_initial` should not be interpreted as another native original soil detachment.
- Important **original built-in legacy net erosion formula exists** in `src/frame/FRmod.f90` L3490, L3680: output ID44 `GNUCUM=GNUCUM + GNU*(RESNOW-PREVTM)*3600*1000`; `BUFFER=GNUCUM-(DLS-DLSSRT)*1000` [mm]. **However** declarations L155–159 explicitly have no initialization for `PREVTM`, `GNUCUM`, and `SEDSRT` baseline set only when nonzero DLS is seen. This original output is **potentially invalid due to undefined initial state** and must NOT be trusted until tested.
- Source C does **NOT** require one-hour internal terrain change: event-based operator splitting accepts SHETRAN erosion and loose-layer state after a storm, then updates all physical terrain/grid states before next storm. Cumulative effects of a storm within that same 1h are neglected and should be checked for convergence as rainfall intensity/depth changes.

## Correct event-level bridge quantity
```
E_i[n] [m] = integral_{storm n} GNU_i(t) dt
DeltaDLS_i[n] = DLS_i(t_end) - DLS_i(t_start) [m]
DeltaZ_i[n] = -E_i[n] + DeltaDLS_i[n]
Z_i[n+1] = Z_i[n] + DeltaZ_i[n]
H_soil_i[n+1] = H_soil_i[n] - E_i[n]
```
Interpretation: `Z` is event-to-event **effective exposed/loose top surface**; erosion lowers native soil matrix, ΔDLS raises/depresses mobile loose-layer thickness. If hydraulic `ZGRUND` should instead represent mineral surface independent of a loose layer, this identification needs site/output validation; do not double add DLS in both DEM and water-surface geometry. Elevation and soil layer depths cannot be patched independently of groundwater, original bank/channel and mesh geometry.
Porosity/solid volume independent QA per cell:
`M_solid,soil_eroded = A_i * (1-THSAT_i) * E_i * rho_particle`
`M_solid,loose_change = A_i * (1-PLS_i) * DeltaDLS_i * rho_particle`
and mobile sediment in water, in/out per class, channel boundary, and deposits comprise rest of ledger. Erosion coefficient GKR/GKF and soil texture can evolve with exposure depth only if original soil layers and inputs are updated consistently. These are source-based outer-coupling equations, **not a new native SHETRAN equation**.

## Critical blocking restart problem discovered
- Original `docs/Hotstart.md` and `src/frame/FRmod.f90` L1358–1396 official hotstart reads/writes canopy CSTORE, water elevation HRF, face QOC, soil pressure head VSPSI, snow and water diagnostics only; **no `DLS`, `FBETA`, `FDEL`** sediment store.
- Original `src/sediment/SYmod.f90::SYREAD` L4220–4245 supports original sediment initialization by **`:SY51` DLS loose layer depth, `:SY52` FBETA sediment particle-size fractions, `:SY53` FDEL mobile sediment concentration** in native SYD file.
- Default visualisation exposes `DLS` but does not expose `FBETA` and `FDEL` by those names. Legacy `src/frame/FRmod.f90::FRRESP` L3580–3615 output IDs 21 (DLS*FBETA_k) and 22 (FDEL_k converted to concentration) may enable preserving these classes **if properly configured and verified**. It is not proven that these legacy raw outputs can be read as-is by current V4.7.2 CLI in this study. Until class storage is recoverable, exact event restart is not achieved.
- Native hydrological hotstart surface water elevation HRF is absolute elevation; after ZGRUND DEM modification, the water-depth relation HRF-ZGRUND and vertical VSPSI/soil mesh state must be adjusted or re-equilibrated with **physically conservative surface/subsurface water redistribution**. Merely copying old head states might yield spurious water.
- Source sediment mass output `BALSED` in `SYmod.f90` L4668–69 is an empty routine; no independent closure demonstrated. Numerical operator-splitting must check water/solid ledger before scientific site predictions.

## Native original FR39 numerical representation hazard
- Original User Guide says `FR39 (10G7.0)`. Each scalar occupies exactly 7 characters. At surface elevation ~600m, sub-mm DEM changes often cannot be represented exactly. Silent rounding across hundreds of events would erase erosion signal.
- The external bridge hard-fails if a `G7.0` roundtrip error exceeds configurable tolerance; do not silently truncate.
- Before actual Gounsa setup choose consistent local vertical datum for **all** elevation-dependent inputs (ZGRUND, channels, subsurface nodes, water/soil states), not just FR39, or explicitly accumulate sub-grid rounding residual across events.

## Source-preserving external bridge actually implemented and tested
- New `experiments/shetran_original_event_bridge.py` in Gounsa main. It DOES NOT edit original `nclwater/Shetran` code. Inputs:
  1. unmodified copy of native `input_*_frd.txt` with FR37-FR39,
  2. CSV samples `time_s,iy,ix,rate_mm_day` exported from actual original `s_v_er` HDF5 (requires t=0 and event end for each cell),
  3. initial soil depth CSV `iy,ix,depth_m`,
  4. event initial and final `s_t_dp` grids CSV `iy,ix,s_t_dp_mm`.
- Numerically integrates sampled erosion via trapezoidal rule and outputs `input_next_frd.txt`, `next_dem.csv`, `next_soil_depth.csv`, `next_sy51_loose_depth.csv`, `QA_AND_RESTART_BLOCKERS.json` marking **restart_ready=false**. This program does NOT automatically generate `SY52` and `SY53`; it is not a complete SHETRAN end-to-end event chain.
- Four synthetic **postprocessor-only** checks: (1) analytic 10mm soil erosion+5mm loose accumulation=5mm lowering, initial soil 0.2→0.19m, exact FR39 parser and roundtrip; (2) precision loss rejection for 650.00012m at 7-character input; (3) missing final-timestep abort; (4) native soil stock overerosion abort. GitHub Actions **4/4 PASS** https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40280065364 .
- **No native SHETRAN executable compiled or run** and no original Cobres HDF5 result was imported into postprocessor in this task. Do not infer that real event chain works from bridge unit tests.

## Remaining to reach fully valid inter-event simulation
1. Untouched original SHETRAN v4.7.2 build and original sediment-enabled Cobres run with real HDF5 output, actual s_v_er,s_t_dp time/space snapshots.
2. Independent sediment size/class and bulk-vs-loose mass budget. Record FBETA/FDEL through existing original legacy output (if functioning) or else acknowledge native release cannot losslessly restart all sediment state without explicit development beyond original.
3. Integrate original GNU at each sediment substep exactly or quantify sampling error from HDF5 frequency, especially 10–50mm/h.
4. Generate complete new FRD (terrain), SYD (SY51/52/53, soil/rock state), VSI/hotstart hydraulic state, plus consistent channel/bank/stratigraphic elevations. Examine original 7-character fixed-width numerical error under true Gounsa datum.
5. Run event1→event2 using original SHETRAN without any core modification, compare water+sediment inventories, soil layer thickness, runoff maps, and output mesh consistency; compare to a continuous original two-event baseline if possible.
6. Only then add measured Gounsa drone/TLS and vegetation states (not guessed coefficients).

## Final decision
SHETRAN is **not ruled out by lack of within-event terrain update**; its published per-cell sediment and original sediment-plain outputs make event-split terrain coupling defensible. Source-traced hooks are real. However full original sediment/hydrology state restart with event topographic update remains **unverified and partly absent**, and precise fixed-width input is a practical limitation. Do not claim achieved Gounsa event-restart run.
