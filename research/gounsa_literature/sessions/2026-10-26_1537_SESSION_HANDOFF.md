# 2026-10-26 SHETRAN 사상별 DEM 연동 인계

## 기존 연구 위치
- MASTER.md, INDEX.md, models/SHETRAN.md, decisions/2026-10-26_SHETRAN_472_NATIVE_IMPLEMENTATION_CALLGRAPH_AUDIT.md
- 원본 nclwater/Shetran 고정 SHA: cf9cd540add78ad3accbaf62b4199d2032887f6b
- 추가 상세 검토: [강우사상 경계 DEM 상태 감사](../decisions/2026-10-26_SHETRAN_EVENT_BOUNDARY_DEM_STATE_AUDIT.md)

## 새로 확인한 사실
1. native HDF5 s_v_er=GNU×86400000 mm/day, s_t_dp=DLS×1000 mm, 입경별 s_dis kg/s, face ovr_flow m³/s.
2. FRRESP output type 44 is GNUCUM - 1000*(DLS-DLSSRT), but PREVTM/GNUCUM initialization and SEDSRT baseline detection, ZERO-time FRRESP call can invalidate it.
3. SYCOLM DDLS=FETA*GNU*DTSY, mass by size and loose sediment thickness, plus SY51 DLS, SY52 FBETA, SY53 FDEL initial conditions available.
4. Original hotstart saves hydrological states but no sediment full restart confirmed; cannot assume terrain state alone enough.
5. Event-end NEW COUPLING: z_next=z_now - sum GNU*dt + (DLS_end-DLS_start), with correct initial elevation/loose layer convention.
6. Original BALSED empty; external independent sediment mass accounting required.

## 이번 세션의 한계
- 원본 코드와 공식 문서만 검증; binary native 빌드/예제 실행/결합 성공은 검증되지 않음.
- 코드 원본 변경 없음. DEM 갱신 실행 결과 수치 없음.

## 다음 시작 지점
1. 같은 SHA 기준 원본 예제 native 실행 및 물/유사수지.
2. 원본 output 44 고장 재현 단위시험 및 외부 GNU, DLS 적산 함수.
3. SY51–SY53 입경별 퇴적 상태 재주입 후 event2 무강우/강우 테스트.
4. water hotstart와 변경된 FR37 지형에 따른 수면과 토양층의 연속성/초기충격 검증.
5. 현장 적용 전 산지 확산파와 세류 미해상성 검증.
