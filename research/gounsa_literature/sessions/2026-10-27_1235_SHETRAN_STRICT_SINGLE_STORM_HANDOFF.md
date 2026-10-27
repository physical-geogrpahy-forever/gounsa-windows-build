# 2026-10-27 고운사 단일 강우사상 SHETRAN 엄격검증 인계

**마감:** 2026-10-27 18:00 KST.
**연구요구:** 1ha 미만 실제 고운사 사면에 참나무 맹아와 억새의 혼재 공간배치를 입력하고, **동일 강우사상**에 수관차단 ON/OFF만을 비교하여 **2D 격자별 직접강우·수관적하, 수문, 원토양 박리, 국지 퇴적, 순 지표고도변화 지도**를 산출. 장기 식생천이/풍화/다른 모형 결합이 아니라 공개 원본 **단일 SHETRAN**을 엄격 검증하고자 한 사용자 요청.

## 결론
- **기능검증 합격:** 원본 SHETRAN 4.7.2 SHA `cf9cd540add78ad3accbaf62b4199d2032887f6b` GNU Fortran 기반 4m 합성사면 0.2816ha 176 격자, 서로 다른 참나무 맹아형/억새형 NVC, 수관차단 ON/OFF 실제 네이티브 실행 성공. 원본 ETIN 수관질량수지, PET=0 조건의 비수관 증발산 혼란변수 없음, 원본 강우/유수 박리 및 4방향 유사교환과 국지적 퇴적 및 고도차 후처리 검증.
- **독립 원본 유사수지 합격:** 이동퇴적층+부유유사에 대해 ON 0.000406%, OFF 0.001575% 잔차, 그러나 합성 폐쇄 경계로 배출량 0. 0/1/10/30mm 초기 이동퇴적층 변화 8/8실행 성공, 박리량 변화 없음(이 사건과 매개변수 조건 내).
- **국지 지형 변화 존재:** ON 5셀 순상승, 161셀 순하강, OFF 4셀 순상승, 166셀 순하강. 최대 ON−OFF 같은 격자 ∆z 차 약 0.00684mm. 사건 내 DEM→flow 재반영 없음. 실제 Gounsa dataset 아닌 합성 지형.
- **중대 미검증/불합격:** 4m 동일 도메인 고정으로 TMAX를 더 작게 해도 누적 원토양 박리량과 공간 퇴적층이 단조 수렴하지 않음. 초기 F7.3 TMAX 정밀도 오류를 **F7.5로 수정한 원본 재시험 [40444641155](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40444641155)까지 통과 실행 확인**. ON 원토양 박리 source .03125h vs .015625h nominal **4.8888% 차이**, OFF .0625h vs .015625h **2.1253% 차이**, 수렴 실패. 실제 각 격자 누적 강우 90mm를 [40444623808](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40444623808)에서 확인, 다른 증발산량 0. 즉 강우량 불일치 때문이 아님. 외부 개방 유출구, 미세공간 2m/1m/0.5m 수렴, 실제 토심 상한, 고운사 현장자료/식생 LAI/수관저장능/강우 검증 없음. **고운사 최종 정량분석 엔진 채택 선언 불가**.
- 실제 원본 주엔진과 진단용 수정빌드를 명확히 구별: 수문/침식/유사수송 등 계산식은 건드리지 않고 `ETIN`, `SYMAIN`에 `WRITE` 추가하여 독립 native 물수지/유사수지 기록. 이를 '원본 바이너리 그대로'라고 기술하지 않는다.

## 가장 중요한 자료
- [전체 판정 및 수치검증 보고서](../decisions/2026-10-27_SHETRAN_STRICT_NATIVE_SMALL_PLOT_VALIDATION_VERDICT.md)
- [세부 실험 4m ON/OFF 및 local net deposition 기록](../decisions/2026-10-27_SHETRAN_NATIVE_MIXED_CANOPY_ON_OFF_REPRO_TEST.md)
- [원본 SHETRAN/EUROSEM 소스 비교](../decisions/2026-10-27_SHETRAN_EUROSEM_SINGLE_MODEL_NATIVE_CODE_AUDIT.md)
- [순지형 변화 3 PNG + 176 셀 CSV Actions artifact](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40444819384/artifacts/12706579843)
- [고정 SHETRAN 원본 단일모델 수관 ON/OFF 질량수지 + 4m 실행](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40441094575)
- [ETIN 강우·수관저류/통과/증발 및 PET0 root ET 혼란변수 없음](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40443924320)
- [실제 176 셀 유사 순유입 순유출 및 bed 저장 증가 구분](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40442738443)
- [실제 GNU적산과 DLS로 ∆z after-event](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40443359926)
- [old F7.3 TMAX approximate finer timestep convergence, 재검증 필요](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40443456084)
- [corrected F7.5 near-exact TMAX rerun, nonconvergence confirmed](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40444641155)
- [actual rainfall integration vs time interval exact 90mm no matter TMAX, old F7.3](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40444177959)
- [corrected F7.5 gross storm forcing validation rerun, exact 90mm per cell](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40444623808)
- [initial bed 0,1,10,30mm 8/8 original native](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40444030737)

## 다음 해야 할 검증
1. F7.5 정밀화 후 TMAX=0.125,0.0625,0.03125,0.015625h 유동·유사 시간 수렴 재판정. **강우 event gross rain=90mm 통제**.
2. 한 실제 사면의 지면 DEM와 참나무 맹아/억새 위치지도, 각 종 LAI, `CSTCAP/CK/CB` 및 canopy drip height/diameter/frac, 실측 rainfall을 확보하지 않은 상태에서 synthetic result를 Gounsa event forecast라고 표기 금지.
3. 수치수렴 확인 실패면 SHETRAN 탈락 여부 결론. 개방 외부 경계와 공간 격자수렴 아직 안 했으므로 모델 채택 완료로 보고 금지. 
4. 보고서와 `research/gounsa_literature/MASTER.md`에 최신 검증 결과 기재 유지. 문헌 한 편 추가 조사한 건 없으므로 papers 신규파일 없음.

## 이미 확인된 논쟁점
- EUROSEM 원본은 1D `PLANE`+rill/interrill이며 Gounsa 국지 2D 자유흐름의 대체 단일모델이 아님. 기존 rilled 12/12 sediment mass budget fail.
- SHETRAN 원본은 자체 canopy+2D diffusion flow+native SYCOLM 4방향 수송 및 퇴적 기능이 존재, 하지만 rill initiation/DEM feedback 원본 미구현. 0.5m 해상도는 static array capacity 내여도 물리적/수치적 검증과 동의어가 아님.
