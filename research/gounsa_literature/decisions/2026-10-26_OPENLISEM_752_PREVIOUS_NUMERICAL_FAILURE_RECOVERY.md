# 2026-10-26 과거 OpenLISEM 7.5.2 실패 원인 복구 및 재추천 금지 조건

## 왜 이 결정 기록을 작성하는가
2026-10-26 다른 대화에서 `main_C` LAI 수관차단과 원본 2D 침식 구현 및 Opedes et al.(2025) Mount Elgon 경사지 적용 선례를 발견하고 OpenLISEM을 실행 우선순위에 다시 올렸다. **그러나 2026-10-23부터 25일까지 원본 Windows 7.5.2를 실제 실행한 기존 실패 검증을 누락했다.** 원본 모형의 필요 프로세스 존재 여부와 *침식량의 수치·물리적 신뢰성*을 구분해야 한다. **기존 실패를 해소하기 전 최종 채택 또는 실행 우선 재설정을 정당화하지 못함.**

## 근거 원본 보고서
- `SOURCE_VERIFICATION_REPORT_KO.md`, 날짜 2026-10-23, Windows original complete-model runs and QA. 원본 2D / 운동파 source-original Windows exe, sha256 `f8a5722ed0b370f32fb3dae5c55465427abe75b1155b50bf12aa5516d6b4ca79`.
- `Gounsa_OpenLISEM_752_root_cause_audit_20261023_KO.md`, 2026-10-23, source `v7.5.2` vs Windows logs, standalone GetSV numeric tests.
- `OpenLISEM_752_official_example_and_native_control_audit_20261025_KO.md`, 2026-10-25, original 7.5.2 executable, factory/legacy/advanced/alternative paired input control.
- `OpenLISEM_full_build_check_20261023.txt` Debian Linux full-build feasibility, Qt6/QWT/DNS problem.

공식 Windows binary actual full-model execution was **successful** on GitHub Actions Windows 2022 using `lisem -ni -f -r <runfile>`. It was the user's uploaded setup distribution lineage. Do **not** falsely claim 'native Windows original full-model run never happened'. Linux build from source with Qt6/QWT was blocked but this was not the ultimate validation failure.

### Primary Windows execution proof
- Kinematic original model: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/39928519655
- 2D original model: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/39929498985
- Experiment branch: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/openlisem-752-virtual-trial-20261023
- 2026-10-25 official-example access run: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40184494173
- 2026-10-25 advanced-options controls: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40185751985

## Failure 1: hydrology approx stable, sediment fails dt convergence
**Same synthetic 100x100m, 25% grade, 5m grids, 1h 20 mm/h rain + 1h recession, kinematic, cohesion 12 kPa, efficiency relation 2.** Note not measured Gounsa site values:
| dt (s) | Oak runoff (mm) | Oak sediment exported (kg/ha) | Miscanthus exported (kg/ha) |
|---:|---:|---:|---:|
| 0.25 | 14.051 | 19.714 | 10.363 |
| 0.5 | 14.050 | 39.560 | 20.771 |
| 1 | 14.048 | 79.626 | 41.718 |
| 2 | 14.045 | 161.111 | 84.093 |
| 10 | 14.020 | 853.798 | 438.867 |

Oak sediment release >43x by changing dt 0.25 to 10s, while water export changes <0.3%. It is not permissible to call this convergence. The 2D dynamic wave has its own CFL timestep: a different route, not automatically comparable to this.

**Synthetic 2D full dynamic, 1h rain + 10 min recession**:
| dt(s) | oak exported kg/ha | oak max cell net soil loss t/ha |
|---:|---:|---:|
|5|6.011|162154.609|
|10|266.691|200566.703|
|20|1568.682|10876.315|
Grid max 200566.703 t/ha at bulk density 1350 kg/m3 means 14.86m removed; synthetic input hydrological soil depth 0.25m. This is not a claim that the physical model requires 0.25m soil storage; rather, **native soil-material availability constraint is not connected to hydrological soil depth**. The 2D result fails finite-layer plausibility under Gounsa research assumptions.

## Failure 2: original GetSV() implementation
In official `v7.5.2/erosion/lisErosionAux.cpp::GetSV(d)`, default Stokes branch for d<100 um and Zanke-commented branch for d>=100 um. Direct source check:
- GetSV(99.9 um) = 0.008974524 m/s
- GetSV(100 um) = 1.272261766 m/s
- standard SI Zanke expression at 100 um is about 0.00778984 m/s.
- Discontinuity ~141.8x; factor 163.32 vs physically standard SI value.
- Bug-shaped expression `sqrt(1 + X - 1)` unlike `sqrt(1+X)-1`, plus unit handling inconsistency.
For shallow overland sheet water this can force near-immediate deposition each timestep; nonlinear Y detachment update can then create timestep-dependent total sediment. **Strong mechanistic candidate, not independently proven as the only cause**. A/B corrected native binary + native run with otherwise identical forcing remains needed.

## Failure 3: finite available soil mass and sediment concentration
- `v7.5.2/erosion/lisSWOF2DSediment.cpp::SedimentSSContinuous()` comments out `DetachMaterial(r,c,...)` even though auxiliary implementation exists. `SwitchUseMaterialDepth=false` initialization. 
- Concentration ceiling branch for detachment commented out in same routine; `MaxConcentration` caps **reported concentration**, not actual sediment mass.
- `soildep1.map` is hydrologic model soil depth, not automatic a finite erodible mass store. In Gounsa, explicit sediment stock and event-interevent soil-thickness feedback are necessary.

## Failure 4: input and GUI / engine control (our workflow error + software discrepancy)
- Early synthetic runfile set `Deposition exponential=1` while `Advanced Options=0`; engine overrode it, thus prior declaration of enabled exponential model was incorrect (input-generation script error).
- GUI `Settling Velocity` key vs source parser `SettlingVelocity` mismatch.
- Official Classic-compatible example was not acquired: downloaded Ganspoel_Hydrology.7z links yielded three HTTP403 and one DNS failure, no official example 7.5.2 run.
- 2026-10-25 factory / legacy / advanced / alternative 8 native runs all exited 0 but **outlet water and sediment were 0**, with water remaining inside domain. The trial cannot prove the physical correctness of exported sediment / boundaries. Internal gross detachment and deposition t totals differ dramatically with options and dt and are NOT catchment net exported erosion mass.

## What actually was validated (vs not)
| Item | Status |
|---|---|
| Native Windows official 7.5.2 exe runs and writes outputs | VERIFIED (2026-10-23) |
| Linux source Qt6/QWT full build in provided Debian runtime | FAILED/environment |
| Native LAI canopy interception + direct/leafdrop splash and native 2D overland detachment | VERIFIED source features |
| Postfire/steep catchment published application | Opedes et al. 2025 provides mountain 2D instance, but NOT native code numerical convergence proof |
| Gounsa synth 2D runoff / erosion timestep stability | FAILED |
| Gounsa synth finite cell soil mass plausibility | FAILED |
| Native default GetSV physically correct at 100 μm | FAILED |
| Spatial per-stem stemflow and dynamic LPJ root coupling | NOT AVAILABLE as automatic original functionality |
| Exact official example 7.5.2 repro, observed Gounsa vegetation and erosion QA | NOT DONE |

## Decision / exclusions
1. **Do not place unmodified OpenLISEM 7.5.2 first for Gounsa erosion quantification based only on three feature existence criteria.** Flag as conditionally recoverable / 2D ecosystem hydrology and erosion literature case, not a validated Gounsa research engine.
2. Prelim source repair minimum: `GetSV` dimensional/parenthesis error, available finite erodible material mass if needed in shallows, concentration mass limitation, controls runfiles and boundaries; then native full-model water/sediment closure and internal gross erosion vs net export separation. All edits explicitly label as **patched fork**, not unmodified published original OpenLISEM.
3. Run dt convergence on the same original synthetic Oak and Miscanthus domain and 2D dynamic wave 5/10/20s, independently audit per-cell soil loss, source terms and sediment flux. Compare source-independent controls such as Hairsine–Rose SWEHR/SHETRAN/Iber only when those also validated.
4. Existing code includes needed processes but this is insufficient for scientific use. Publishable output must await closed sediment budget, stability, finite material checks and field controls.
5. Prior 2026-10-26 "high priority OpenLISEM" decision (same day `2026-10-26_OPENLISEM_THREE_CRITERIA_SOURCE_AND_STEEP_SLOPE_AUDIT.md`) must be interpreted as **feature-and-publication screening only**, overridden for operational selection by this earlier failure recovery.
