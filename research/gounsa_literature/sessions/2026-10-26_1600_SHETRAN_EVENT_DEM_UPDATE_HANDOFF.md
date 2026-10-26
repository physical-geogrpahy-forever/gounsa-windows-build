# 고운사 SHETRAN 다사상 DEM 갱신 모델 감사 및 외부 재시작 입출력 도구 인계 (2026-10-26)

## 사용자 요구
원본 SHETRAN으로 강우에 따른 유수침식 및 퇴적을 사상마다 계산하고, 원래 DEM/토심을 갱신해 다음 강우사상에 반영. 같은 채팅 계속. 원본 Fortran 모형을 임의 변경하거나 가상 식생계수를 추가하지 않는다.

## 실제 검증한 원본
- SHA cf9cd540add78ad3accbaf62b4199d2032887f6b, v4.7.2 original Fortran from `nclwater/Shetran`.
- 공식 HDF5 output `s_v_er=GNU*86400000` [mm/day] (원토양 박리속도, NOT net); `s_t_dp=DLS*1000` [mm] (loosely deposited/mobile sediment depth); `s_dis` [kg/s] per grain/faces and `ovr_flow` [m3/s].
- `SYCOLM` converts GNU soil to loose-layer thickness with `FETA=(1-THSAT)/(1-PLS)`, updates DLS, FBETA, FDEL, QSED per grid face and grain class.
- Original archived legacy `FRmod::FRRESP` ID 44 net soil loss formula `GNUCUM - (DLS-DLSSRT)*1000` [mm] exists; **UNSAFE** because `GNUCUM` and `PREVTM` are declared with no startup initialization; code explicitly warns.
- Original hotstart docs `docs/Hotstart.md` and `FRmod::FRINIT` omit DLS/FBETA/FDEL; restart original sediment storage needs original `SYmod::SYREAD` `:SY51` DLS, `:SY52` FBETA, `:SY53` FDEL. Standard HDF5 `s_v_er/s_t_dp` omit the latter two. Legacy `FRRESP` ID21 and ID22 have class-resolved loose/mobile sediment accessors; configured native output not yet verified.
- Original FRD `FR37–FR39 ZGRUND`, Fortran `10G7.0` per 7-char field, units m. Submillimeter precision might be lost; do not silently round DEM update. Need consistent local datum for all vertical variables.
- Operator-split external formula `z_next=z_old−∫GNUdt+(DLS_end−DLS_start)`, `H_soil_next=H_soil_old−∫GNUdt`; physical interpretation relies on exposed top surface vs loose-layer survey. HDF5 GNU snapshots sample instantaneous erosion rate so interpolated trapezoid is NOT exact native GNU accumulation.

## Actually created and tested
- `experiments/shetran_original_event_bridge.py`: independent Python (stdlib) EXTERNAL tool only; no changes to published SHETRAN source.
- `experiments/test_shetran_original_event_bridge.py`: four synthetic validation scenarios including analytic 10mm soil erosion+5mm loose deposition=5mm net lowering, native FRD roundtrip, prohibit losing 7char precision, reject rates without event endpoints and erosion beyond available soil stock. 4/4 passed.
- `.github/workflows/shetran_original_event_bridge_qa.yml`: runs four unit tests plus downloads exact pinned original `examples/Cobres/model/input_cob_frd.txt`, reads **all 17×29=493** original FR39 cells, roundtrips full original `input_next_frd.txt` through external postprocessor with zero exported synthetic GNU/DLS, checks all 493 elevations unchanged. Actual CI passed:
  https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40280645823
- Outputs `input_next_frd.txt`, `next_dem.csv`, `next_soil_depth.csv`, `next_sy51_loose_depth.csv`, `QA_AND_RESTART_BLOCKERS.json`. Tool intentionally emits `restart_ready=false` because original FBETA/FDEL and hydraulics continuity **not** yet restored.
- New source-based decision `research/gounsa_literature/decisions/2026-10-26_SHETRAN_INTEREVENT_DEM_UPDATE_NATIVE_OUTPUT_AUDIT.md` (MASTER.md, INDEX.md updated).

## Limits
**We did not compile/run native original SHETRAN for an actual rain+sediment event here.** No actual Cobres sediment HDF5 output was tested or imported. Only original-Cobres FRD syntax and byte-preserving unchanged-grid external roundtrip were tested. No physical Gounsa field DEM input or full next-event sediment continuity. No claim exact native substep erosion integration or full sediment mass closure.

## Next physical native validation
1. Native SHETRAN original unchanged compile/run Cobres existing sediment-on test; read actual `s_v_er`, `s_t_dp`, `s_dis` snapshots and HDF5 numerical grids with correct time and orientation.
2. Recover output `FBETA` and `FDEL` by documented original legacy FRRESP IDs 21/22 if format and source version allow; otherwise exact sediment restart impossible without clearly labeled diagnostic extension. Avoid pretending DLS alone is complete.
3. Verify 2-consecutive-event timing, soil moisture, groundwater/HRF and canopy CSTORE replay consistency after change in ZGRUND and soil-column absolute heights.
4. Build exact GNU sediment substep integral or quantify HDF temporal sample bias. Validate signed 4-face sediment budget, raster mask, porosity conversion, two storms and mass conservation.
5. Add root/litter and spatial Miscanthus and Quercus only after original package full process-level reproduction passes.
