# SHETRAN 4.7.2 고운사 1ha 미만 단일 강우사상: 원본 모델 엄격 검증 결과와 NO-GO 항목

검토일: **2026-10-27**, 원본 `nclwater/Shetran` commit `cf9cd540add78ad3accbaf62b4199d2032887f6b`. 용도는 **참나무 맹아와 억새가 1ha 미만 사면에 동일하게 혼재하는 지형에서, 한 번의 강우사상 동안 수관차단 ON/OFF에 따라 국지 원토양 침식, 국지 퇴적, 지표고도 순변화가 어떻게 달라지는가**이다. **반드시 기존 단일 모델 SHETRAN 원본 물리식만**. GitHub workflow의 진단용 소스는 original upstream에 Fortran `WRITE` 계측만 추가, 새로운 프로세스/모형 결합 아님. 이는 코드 기능 및 수치 QA이며 **실제 고운사 실측 기상/DEM/LAI 검증이 아니다**.

> **긴급 정정 (2026-10-27):** 이전 보고서의 `TMAX` 실험은 실제로 `PMAX`를 변경한 도구 오류다. **SHETRAN의 '시간간격 수렴 불합격' 주장을 철회하고 '진정한 TMAX 시험 미검증'으로 정정**했다. [자세한 원본 코드 교차확인](2026-10-27_SHETRAN_TIMESTEP_ROOT_CAUSE_CRITICAL_CORRECTION.md).\n\n## A. 이미 입증된 기능 (PASS)

### A1. 혼재식생 2D native 단일모델 실행
- Upstream source pristine built with GNU Fortran. [Actions 40441094575](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40441094575).
- 하나의 17×29 셀 사면 내부에 **참나무 맹아형/억새형 NVC 2종**을 격자별 지정. 4m 셀, 활성육상 셀 176개, **면적 2816m²=0.2816ha** (bounding 7888m²). 강우 30mm/h×3h, 전 1시간 무강우 warmup, 총12시간. **실제 고운사 미세지형 데이터 아님**: 2km Cobres 지형을 4m로 임의 스케일해 만든 가상사면, 구조적/계수 대표성 없음.
- 수관차단 ON/OFF 모두 원본 모델 실행 성공. 단 수관 OFF는 `PLAI=0`이므로 잠재증발산 미영향 조건을 추가로 시험하지 않으면 순수 수관차단 비교라고 인정 불가. PET 0 조건에서 아래 A2로 해결.

### A2. native ETIN 수관 수분보존과 증발산 혼란변수 검사: PASS 이 특정 PET=0 실험
- [Actions 40443924320](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40443924320), upstream `ETmod.f90::ETIN/ET`에 단일 `WRITE`만 추가, 176 셀× 시간단계.
- ON 34,496 식생격자 시간단계: 원강우 총 15840.0 셀별 mm 합계 (=176×90), 지표 도달 강우 총 15646.55391108 mm, 최종 수관저장량 변화 합계 193.44608892 mm, 수관증발 0. 수관수지 최대 단일단계 잔차 **9.77×10⁻¹⁵ mm**, 모든 셀 종료시각 누적 잔차 절댓값 합 3.27×10⁻¹² mm.
- OFF 27,632 단계: 원강우 15840.0, 지표 도달 15840.0, 저장/증발 0, 잔차 0.
- 뿌리흡수 `ERZA`, 토양증발 `ESOILA` 및 기타증발 `EEVAP`의 ON/OFF 총량이 **모두 0** (시험 PET 0). **이 가상사상에서는 수관 ON/OFF 효과가 다른 증발산 효과와 섞이지 않았음을 실측한 코드 증거**. 실제 비영 PET 사상에서 `PLAI` 변경의 증발산 교란 여부는 별도 검증 전까지 일반화 금지.

### A3. 원토양 박리 + 4방향 유사 이동 + 이동가능 퇴적층 저장: PASS
- [Actions 40442738443](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40442738443), 원본 `SYMAIN→SYOVER→SYCOLM` 4면 `QSED`, 입도 및 `GNU` + `DLS`, `FDEL`을 Fortran native 단계에 기록. ON 원토양 박리 176/176 셀, 총 원토양 새 유사 공급 **0.11443825974 m³ solid**, 다른 셀에서 순유입된 셀 74개, 순유출 100개. OFF 원토양 박리 176/176, 새 공급 **0.13779875301m³ solid**, 순유입 73개, 순유출 100개. 이는 gross eroded sediment supply이고 출구 배출량 아님.
- 초기 loose-bed stock, 자기격자의 신생 원토양 박리량, 최종 부유유사를 분리: 자기격자의 생성유사만으로 설명되지 않는 **외부 유입 유사의 최종 표층저장 증가 셀** ON 74개, OFF 72개. 순감소 셀 ON/OFF 각 100개. 이는 원본 모델의 국지 유사수송 및 퇴적층 축적 발생 증거이나 아직 순지표고도 상승의 직접 증거는 아님.

### A4. 실제 event-end 순지표고도 변화까지 native 기반 독립 적산: PASS, 사상 도중 DEM 피드백은 없음
- [Actions 40443359926](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40443359926). 원본 내부 `GNU×DTSY` 및 `DLS`를 격자별 정확 적산. `∆z_post = [DLS_end−DLS_start] − Σ GNU DTSY` [m]. 주의: 원본 모델에 존재하지 않는 지형고도 prognostic field를 새로 넣은 게 아니라 **사상 후 고도변화 후처리/진단**. 지형이 유동에 강우사상 도중 재반영되지 않음; underlying soil + mobile sediment bulk conversion은 native `FETA=(1−THSAT)/(1−PLS)`를 별도 검사 (unit source residual ~2×10⁻¹⁸m³).
- ON **5개 셀 순상승**(∆z>0.001mm), **161개 순하강**(∆z<−0.001mm), 10개 거의 변화 없음. 최대 +0.0151004mm, 최소 −0.0895759mm, 평균 −0.0080300mm.
- OFF **4개 순상승**, **166개 순하강**, 6개 거의 변화 없음. 최대 +0.0138351mm, 최소 −0.0897838mm, 평균 −0.0096751mm.
- **ON−OFF 최대 같은 셀 순고도차 0.006835895mm**, 평균 ON−OFF +0.0016451mm. 비교 출력은 현장 검증이 아니라 가상 4m 한 사례; 본격 0.5m 이하 tussock/coppice crown 형상 재현 불가.

### A5. 이동가능 유사 원본 전체 수지: PASS, **폐쇄형 영역에만 한정**
- [Actions 40441094575](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40441094575). ON 195 내부 유사계산 단계 누적 잔차 −4.645586×10⁻⁷ m³ solid, **박리량 대비 0.000406%**. OFF 156단계 −2.17017×10⁻⁶m³ solid, **0.001575%**. 원본 `BALSED` stub가 비어 있어 진단용 WRITE 계측을 별도 컴파일. 새 프로세스식 삽입 아님. 토심 재고 자체의 원토양 mass ledger는 미검증.
- 무하도 작은 사면은 현재 **외부 경계 sediment export가 0**. 폐쇄영역의 유사재분배가 보존된다고 해서 실제 지형 출구를 통한 sediment throughput이 검증되는 것은 아님.

### A6. 원본 Cobres의 불필요한 두꺼운 이동퇴적층 입력 민감도: 8/8 native PASS, 값 거의 불변
- [Actions 40444030737](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40444030737).
- `SY51c` initial loose depth를 **0, 1, 10, 30mm**로 지정, 나머지 동일 4m×176 셀×3h 강우×dry-warmup. **8/8 원본 native 종료 성공**.
- ON gross original soil source **0.11443825974 m³ solid**가 네 경우에 동일, OFF **0.13779875301 m³ solid**도 동일. 종료시점 평균 `DLS-DLS_initial`: ON 약 **0.058055mm**, OFF 약 **0.069905mm**; native sediment stock balance 각 회 통과.
- 단지 이동가능 초기퇴적층 두께를 0–30mm 바꾸는 이 실험에서는 결과가 안정된다는 증거. *원토양 토심 H=0*, 초기 세토 재고가 고갈되는 조건, 더 강한 비/집중 유동, 식생 가을 이후는 미검증.

## B. 실패 또는 필수 미검증 (NO-GO 판정 유지)

### B1. **중대 정정: 진짜 TMAX 시간간격 수렴성은 이전 시험에서 검사되지 않았다**
- [치명적인 입력 검증오류의 원본 소스 증거와 정정](2026-10-27_SHETRAN_TIMESTEP_ROOT_CAUSE_CRITICAL_CORRECTION.md). 원본 `FRmod.f90:5455`는 `(4F7.0,L7)` 순서로 `PMAX,PALFA,QMAX,TMAX,BSOFT`를 읽는다. **과거 시험 도구는 첫 필드 `PMAX`만 바꾸고 실제 네 번째 필드 `TMAX`는 1h로 남겼다**.
- 과거 "TMAX에 따른 누적 침식량 4.88877%/5.8% 차이"와 "시간간격 수렴성 불합격" 주장은 정당하지 않으므로 **철회**한다. 정밀도 F7.3→F7.5 수정도 PMAX 필드를 건드리는 오류는 치유하지 못했다.
- 원본 `TMSTEP`에서 PMAX는 `PTOT>PMAX`이면 실제 `UZNEXT=MIN(UZNEXT,PMAX/PINP)`로 제한하는 **강우 시간분할 매개변수**이다. 그래서 과거 실험의 차이는 `PMAX`를 1mm에서 작은 값으로 낮췄을 때 수문/수관/유사가 민감하다는 것만 보여준다. **그 반응이 원본 부정확성인지 초기시간적 처리 탓인지는 추가 원인 분해 전까지 단정 금지**.
- 입력 스크립트를 전면 정정해 `TMAX`만 네 번째 7자리 필드에 쓰고 `PMAX=1.0mm`을 원본대로 유지했다. 또한 원본 `BSOFT=T`의 초기 102단계 기반 softstart를 `F`로 꺼서 불필요한 단계수 혼란을 분리하였다. [진정한 TMAX native 실험](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40445638896) / [강우량 검산 native 실험](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40445644339). 이 재실행의 수치를 확인하기 전까지 **시간수렴 미검증**.
- **현재 고운사 최종선정은 여전히 보류**: 고해상도 공간수렴, 실측혼재 canopy/토성/경계, 유한 토심, real site observations 없음. 이것은 별개 문제이고 시간간격 시험이 잘못되었다는 사실로 이 항목들이 해결되지는 않는다.

### B2. 고해상도 공간 수렴성: **미검증**
- 4m 176 셀 단 한 해상도만 공간 시험. <1ha 규모 억새 포기 및 참나무 맹아의 패치 간 침식/퇴적 위치는 0.5m 또는 그보다 미세한 DTM과 식생관측 필요. 2m, 1m, 0.5m **같은 물리적 영역**에 대한 격자 refinement 전까지 final model이라고 판정 금지. 4m vs 2km는 서로 다른 영역/지형이므로 수렴시험이 아님.

### B3. 실제 물과 유사의 개방 경계/outlet: **미검증**
- 지금 4m 합성사면은 native no-channel flow boundary를 이용한 폐쇄 경계. 침식-퇴적 hotspot이 발생할 수는 있지만 실제 사면의 유사배출량/퇴적량 분배에는 출구 조건 영향이 큼. `SYBC`의 비어 있는 루틴, `QOC` 경계와 river-link 접속을 원본으로 재검증하지 않는 한 실제 연구 현장의 open outlet 경계 재현 주장 금지.

### B4. 초본 포기와 참나무 맹아 실제 3D 수관 및 원토양 유한성
- `NVC`는 격자당 한 식생유형. 격자당 억새/참나무 수관층이 중첩되는 경우 multi-canopy 저장 별도 native 표현 미확인. `CLAI` 및 `PLAI` canopy 상태량, `CSTCAP` 수관저장량, `SY24` 잎적하 높이/물방울직경과 직접충격을 모두 실제 canopy 측정으로 제약 필요.
- original `DLSMAX`는 loose sediment 보호 임계치이지 **잔존 초기 토심 H 최대박리 제한이 아니다**. 얕은 암반 토심과 흙의 available mass limiter 미구현. 수관차단만 활성화해도 암반 표면 원토양 과박리 위험.
- event 중 원토양 박리→DEM 변화→다음 hydraulic 계산으로 feedback 없음. 이벤트 종료 후 ∆z postprocess 가능하지만 모형 기능을 사건 내 완성 morphodynamic 모델이라고 부르는 것은 부정확.

## C. 결론

**한 개 완전공개 기존 원본 모델로서 SHETRAN 4.7.2는 동적 수관차단, 직접강우/leafdrip, 2D 유동, 강우박리와 유수박리, 4면 유사 수송 및 국지적 퇴적, 이벤트 말미 순지표고도 후처리를 실제 계산할 수 있다는 점까지 코드 및 native로 검증됐다.** 그러나 현재 중요 output `E(x,y),D(x,y),∆z(x,y)`의 수치적 시간간격 수렴 **미검증**, spatial refinement, open outlet, 토심 상한 및 **실제 고운사 DEM/현장 데이터 검증 미실시**. 엄격한 기준상 **고운사 최종 연구용 model로 선정 완료라고 선언할 수 없다.** 단일모델 검증 통과라고 포장하지 말고, event proof-of-capability with nonconvergence issue로 보고한다.

**EUROSEM**은 canopy+rain/flow+rill 내장원본임에도 1D plane 요소를 토대로 하여 mixed oak+tussock를 같은 실제 2D 격자에서 나타낼 수 없고 rill full-ledger fails; 이번 과제의 대체 단일모델 불가. 원본/수정 툴 기록은 [기존 원본 코드 감사](2026-10-27_SHETRAN_EUROSEM_SINGLE_MODEL_NATIVE_CODE_AUDIT.md).

### A7. 가상사면 격자별 침식-퇴적 지도 및 수치표 출력
- [동일 4m 가상사면 원본 GNU 적산 후 3개 PNG 및 셀별 CSV](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40444819384/artifacts/12706579843). 수관차단 ON, OFF, ON−OFF 각 순지표고도 변화 지도, 원토양 박리량과 퇴적층 증감량 및 순∆z의 176개 셀 CSV. 이미지와 CSV에는 실제 Gounsa 공간좌표/현장자료가 없으므로 현장 DEM 변화도라고 부르지 않는다.

## 관련 실행 코드
- [원본 native 전처리와 동일 격자 ON/OFF 실험](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/shetran_mixed_canopy_native_20261027.py).
- [원본 단계별 유사 고체체적 수지 계측](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/shetran_instrument_sediment_qa_20261027.py).
- [겹치는 식생 혼재사면 셀별 수송 진단](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/shetran_spatial_flux_eval_20261027.py).
- [같은 셀 원토양 박리와 잔존 퇴적층으로 순고도 산출](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/shetran_net_surface_change_20261027.py).
- [원본 수관 water budget 및 ET 혼란변수 분석](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/shetran_canopy_water_eval_20261027.py).
- [동일 4m 도메인의 추가 fine timestep series](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/shetran_dt_fine_20261027.py).
- [초기 sediment bed 0/1/10/30mm 대조](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/shetran_loose_layer_sensitivity_20261027.py).

## 원본 코드
- [SHETRAN ETmod.f90](https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/evapotranspiration/ETmod.f90)
- [SHETRAN SYmod.f90](https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/sediment/SYmod.f90)
- [SHETRAN OCmod2.f90](https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/overland_channel/OCmod2.f90)
