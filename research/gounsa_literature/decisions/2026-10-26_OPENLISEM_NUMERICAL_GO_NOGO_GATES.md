# OpenLISEM 7.5.2의 고운사 유수침식 연구용 최종 판정: 사전 등록 GO/NO-GO 검증 기준

기록일: 2026-10-26. 판정 대상: 개발진 공식 Windows 7.5.2 `lisem.exe`, SHA256 `f8a5722ed0b370f32fb3dae5c55465427abe75b1155b50bf12aa5516d6b4ca79`. 원본 code `v7.5.2`의 결과와 공개 `main_C`의 별도 버전은 섞어 주장하지 않는다.

## 사용자 결정
**충분한 검증 이후 침식 계산의 안정성과 물리 보존성을 충족하지 못하면 OpenLISEM을 고운사 유수침식 주 모델 후보에서 폐기한다.** LAI interception, throughfall, drip kinetic energy, 2D dynamic wave, runoff detachment와 산지 출판 연구의 존재만으로 채택하지 않는다. 기존 2026-10-23 원본 Windows 검증의 불합격 사실을 우선한다.

## 과거 실험 확인된 기준선 (새로 실행한 결과 아님)
기본 원본 7.5.2:
- Kinematic: synthetic oak 1h 20mm/h, Δt=0.25,0.5,1,2,10s에서 sediment export 각각 19.714, 39.560,79.626,161.111,853.798kg/ha, water export 14.051,14.050,14.048,14.045,14.020mm. 약 43x 변화 = 이전 판정 불합격.
- 2D dynamic wave original: oak Δt=5,10,20s => sediment export 6.011,266.691,1568.682kg/ha, max cell net removal 162154.609,200566.703,10876.315t/ha. 10s ≈14.86m eroded thickness @1350kg/m3 versus synthetic 0.25m hydrologic soil depth.
- `GetSV(d)` default branch 99.9μm=0.008974524m/s, 100μm=1.272261766m/s, standard SI Zanke ≈0.00778984m/s at 100μm. Original `GetSV` implementation has discontinuity/parenthesis/units error.
- `SedimentSSContinuous()` soil finite-store limiter `DetachMaterial()` is commented out, as is part of concentration cap; `SwitchUseMaterialDepth=false`. `soildep1.map` is hydrological depth, not linked native finite erodible soil-stock.
- 2026-10-25 factory/advanced options validation also found `Advanced Options=0` overriding asserted options and a GUI/engine settling-velocity runfile key mismatch. Eight small-grid 2026-10-25 cases had water outflow=0 at outlet and were non-diagnostic for exported erosion; their gross detach+deposition are not catchment-exported sediment.

## Required test order — original exe before any fork

### Gate 0: binary, inputs, experimental consistency
- Pin exact Windows installation executable + SHA256; explicitly verify original model via native `lisem -ni -f -r`.
- Archive native entire .run, map rasters, rainfall time series and their hashes, source version, start/end, timestep, internal CFL dt, output keys, stdout/stderr. Every run = identical forcing, geometry, soil and boundaries except one named factor.
- Keep 1h storm with 1h recession for reference; check actual precipitation (input and native output) to <0.1% across timesteps.
- `Advanced Options=1` when toggling advanced switches; engine-supported `SettlingVelocity` key explicitly set and verified. Separate no-switch, alternative original, corrected-fork branches. A zero water/sediment outlet trial is **NON-DIAGNOSTIC**, not pass.

### Gate 1: canonical slope hydrology and 2D outlet
- Use one consistent 2D FullSWOF dynamic domain (not 1D kinematic proxy), e.g. past 100m x100m at 5m grid/25% slope and Ksat 2mm/h; verify LDD georeferencing, actual cell size (PCRaster GDAL 1m LDD transform gotcha), outlet, water flood edge flux, model min/max DEM and stage.
- Run no-rain/no-inflow zero-source control; positive rain with confirmed >0 nonzero runoff at valid domain boundary.
- Compare precipitation, canopy Δstore, net rain, infiltration, channel/flood/surface terminal storage, ET if on, boundaries. **Provisional** absolute residual <0.1mm or <0.1% of rainfall (whichever larger). This is a registered conservative benchmark tolerance, not a theorem nor proof of sediment validity.

### Gate 2: physical settling-rate source diagnostic
- Evaluations at d=50,99.9,100,100.1,101,150μm for original default, original alternative and *independent external SI reference* (not substituting this reference into original).
- Reject selected native settling implementation if an infinitesimal grain-size perturbation around 100μm creates ~100x jump without physical phase-transition justification, or native values clearly inconsistent with dimensionally correct settling relations. Record units and gravity/viscosity.
- An alternative published/native settling scheme can be tested as its own **original supported option**; do not claim switching it repairs the other failures.

### Gate 3: genuine 2D numerical convergence
- Same geometry/initial and boundary conditions, sediment options held fixed, compare external dt 20,10,5,2.5,1.25s, optionally 0.625s. Record internal CFL microsteps and whether storm rain amount matches.
- Compare four separate outputs: water export hydrograph and volume, sediment outlet mass and time series, net soil loss mass/map, gross detachment and deposition maps.
- **Provisional GO tolerance** only when fine Δt/2 vs Δt sediment export and integrated net soil loss both differ <=5%, hydrograph timing/peak stable, and a further refinement does not reverse the trend. Near-zero exports need an independent absolute tolerance tied to measured/nontrivial event signal; trivially 0/0 is NOT pass.
- If any data show >10% fine-step differences at the two finest tested resolutions or erratic non-monotone >O(1) dependence, NO-GO, unless a documented boundary/input defect caused them, in which case correct that defect and repeat **once**. Do not tune cohesion or erodibility merely to suppress output.

### Gate 4: independent sediment and soil-stock ledgers
- In kg (not t/ha) for each step and event: `virgin_soil_stock_initial`, `extracted_original_soil`, `deposited_mobile_layer`, `resuspended`, `outlet_export`, `still_in_water`, `soil_stock_end`, and any external sediment source.
- Separate gross cumulative detachment/redeposition cycling from **net** eroded original-soil stock and outlet export. Check `initial soil + input - output = final soil + deposited + suspended`; provisional net residual <=0.1% of relevant mass with finite precision floors and no negative stocks.
- The native model's `soildep1.map` does NOT imply a finite erosional mass stock. If the original cannot enforce finite soil stock in a shallow sandstone slope, Gounsa process requirement fails. External-capped output merely hides the problem and is NOT PASS.
- 0.25m soil + bulk density 1350kg/m3: initial finite available column 3375 t/ha per cell, unless an independently documented renewal/new supply term exists. No cell should erode more native soil than is available in that cell.

### Gate 5: vegetation-to-erosion signal
- Only after all above passed: independent LAI vs Smax vs plant height vs litter perturbations, control equal Ksat, Manning, soil cohesion and stone fraction at same time; then species-structural scenarios Oak / Miscanthus.
- Native source terms to observe: canopy CStor, RainNet, directrain, LeafDrain, KE direct/drip, splash detachment, flow-driven detachment, deposition, export. Non-significant or near-zero effect needs a sensitivity/data interpretation, not an artificially amplified coefficient.
- Stemflow original built-in not shown active; dynamic LPJ roots conversion not native and not assumed.

## Final decision, no circular rescue
- **PASS**: unmodified original supported parameterization that meets Gate 0–5, with no undocumented edits; and evidence repeatable and independently auditable. Label candidate, not yet field-validated Gounsa final model until TLS/sediment observations.
- **FAIL / DISCARD FOR GOUNSA WATER EROSION ENGINE**: nonconvergence, nonsensical settling behavior without a native reliable alternative, unacceptable finite soil stock defect, broken sediment ledger, invalid 2D outlet, or inability to make physically plausible soil loss, after justified boundary/configuration correction and one repeat.
- **PATCHED FORK**: any modifications of `GetSV`, `DetachMaterial`, concentration/soil stock or erosion source terms = new code lineage; its success does *not* restore the unmodified OpenLISEM verdict. No fork just to force a preferred vegetation ranking.
- Official examples may be used as independent reproducibility targets, but official example download failure is distinct from model numerical failure.
- Existing 2026-10-23 results are already **FAIL baseline**; new test series is a defined opportunity to falsify diagnosis by correcting external input errors or choosing an original native option, NOT an assumed impending success.
- If native options still fail, stop OpenLISEM and proceed with independent verified source engine; no indefinite repair work.

## Provenance
- [Prior failure audit](2026-10-26_OPENLISEM_752_PREVIOUS_NUMERICAL_FAILURE_RECOVERY.md).
- [Source and steep-slope native feature audit](2026-10-26_OPENLISEM_THREE_CRITERIA_SOURCE_AND_STEEP_SLOPE_AUDIT.md).
- Windows original runs: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/39928519655 ; https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/39929498985 ; https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40185751985
- Source `v7.5.2`: https://github.com/vjetten/openlisem/tree/v7.5.2


## 2026-10-26 same-session source recheck (not a new executable run)
Connected GitHub source `vjetten/openlisem` `v7.5.2` vs `main_C` independently inspected:
- Both `erosion/lisErosionAux.cpp` `GetSV` have the *same* original problematic expression `sqrt(1.0 + 0.01*(1.65*GRAV*dm*dm*dm)-1.0)/dm`, with threshold `d<100`. Thus source on current main_C does NOT show default scheme repair.
- `main_C/erosion/lisSWOF2DSediment.cpp` line ~640 `//detachment = DetachMaterial(...)`, line ~673 `//if(SS + detachment > MAXCONC * sswatervol)` still commented.
- `main_C/model/lisDataInit.cpp` has `SwitchUseMaterialDepth = false;` at ~1990 and 2113. Native finite soil stock remains disabled there.
- Conclusion: upgrading solely from 7.5.2 binaries to current main_C source cannot be asserted to fix erosion mass/stability problems. A fresh native convergence run with alternative **original-supported** settling scheme, properly enabled advanced controls and verified outlet is still necessary to distinguish correctable setup from native mathematical issue.
