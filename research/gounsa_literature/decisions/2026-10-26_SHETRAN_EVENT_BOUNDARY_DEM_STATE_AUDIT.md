# SHETRAN 4.7.2: 강우사상 경계의 DEM 갱신과 퇴적 상태 전달 원본 코드 감사

작성: 2026-10-26. 유형: 소스코드 기반 분석 및 외부 결합 설계. **원본 바이너리 실행 검증 아님.**

## 1. 기존 연구와 연결
- [SHETRAN 모델 계보](../models/SHETRAN.md)
- [실제 함수 연결 감사](2026-10-26_SHETRAN_472_NATIVE_IMPLEMENTATION_CALLGRAPH_AUDIT.md)
- 공식 설명서: https://research.ncl.ac.uk/shetran/SHETRAN%20V4%20User%20Guide.pdf
- 출력 예제: https://research.ncl.ac.uk/shetran/Shetran%20Easy%20Setup-%20sediment%20and%20snow.pdf
- Fortran **원본 공개 저장소** nclwater/Shetran SHA cf9cd540add78ad3accbaf62b4199d2032887f6b
- 원본 소스 변경 없음. 원본 실행, native 예제 수지검증 아직 수행하지 않음.

## 2. 관측 가능한 원본 출력과 의미
- HDF5 s_v_er [mm/day]: 현 시점 GNU [m/s] × 86,400,000. **원지반 박리속도**, 누적 순지형변화 아님.
- HDF5 s_t_dp [mm]: 현 시점 DLS [m] × 1,000. **유동 가능한 표층 퇴적층 두께**, 순침식량 아님.
- HDF5 s_dis [kg/s]: 입경별, face별 유사유출. 출구 경계 부호와 수송 계산의 체적-질량 변환 검사 필요.
- HDF5 ovr_flow [m³/s]: 격자/하도 face별 수리 유량.
- 검증 근거: `src/frame/FRmod.f90` `FRRESP` CASE 21/25/27/44, `src/visualisation/visualisation_interface_left.f90`, `examples/Cobres/model/input_cob_visualisation_plan.txt`.
- 출력에는 시간축이 포함되어 있어 시계열 기록을 통해 외부 적산 가능. 다만 출력 주파수가 계산 timestep보다 낮으면 수치적 적산 오차를 측정해야 함.

## 3. 물리적 지표고도 갱신(외부 NEW COUPLING)
`z_b`를 원토양 상면의 기준고도, `DLS`를 별도의 표층 느슨한 퇴적층 두께라고 정의하고, 물리적 지표고도 `z_s=z_b+DLS`로 일관되게 관리한다. 사상 n의 처음과 끝에서:
```text
E_n(i) = sum_k GNU_n(i,k) * dt_k   [m]
z_b(n+1,i) = z_b(n,i) - E_n(i)
DLS(n+1,initial,i) = DLS(n,end,i)
z_s(n+1,i) = z_s(n,i) - E_n(i) + DLS(n,end,i)-DLS(n,start,i)
```
이 식은 `src/frame/FRmod.f90` CASE(44)의 누적 침식-퇴적층 변화 구조와 일치하지만, **원본에서 지형갱신을 수행한다는 뜻은 아님**. `SYMAIN`의 `ZGRUND` 인자는 INTENT(IN)이고, 실행 중 수리모형의 지표고도는 원래 상태로 고정. 위 식은 사상 종료 후 새 FR DEM으로 공급하는 독립 결합 연산.

유의: 위 `z_b` 분해는 외부 상태관리의 정의임. 처음 제공한 DEM이 실제 지표고도라면 최초 `z_b=z_s-DLS_start`로 환산하고 초기 `DLS`를 두 번 더하지 않아야 한다. 표층 퇴적층 두께가 지반 측량고도에 그대로 대응하는지, 압밀과 공극률 변화 및 암편 보호를 어떻게 처리할지는 별도 검증 필요.

## 4. CASE(44) 출력의 확인된 결함
원본 `FRRESP`, source `src/frame/FRmod.f90`:
```fortran
IF (.NOT. SEDSRT) THEN
   DO J = 1, total_no_elements
      IF (NOTZERO(DLS(J))) SEDSRT = .TRUE.
      DLSSRT(J) = DLS(J)
   END DO
END IF
DO J = 1, total_no_elements
   GNUCUM(J) = GNUCUM(J) + GNU(J)*(RESNOW-PREVTM)*3600.0D0*1000.0D0
END DO
...
CASE (44)
   BUFFER(J) = GNUCUM(IEL) - (DLS(IEL)-DLSSRT(IEL))*1000.0D0
...
PREVTM = RESNOW
```
- `GNUCUM` 및 `PREVTM` 선언 시 초기값과 첫 사용 전 초기화 불명확: 원본 자체의 `docs/code_analysis/analysis_frmod.md` 경고와 일치.
- `SEDSRT`가 최초 `DLS>0`을 기다리므로 초기 `DLS=0`인 격자에 사상 중 최초 퇴적이 일어나면 baseline `DLSSRT`가 늦게 잡힐 수 있음.
- `run_sim.f90`에서는 첫 contaminant 활성 시 `FRRESP(AIOSTO,ZERO,.FALSE.)` 호출 경로가 존재하여 `PREVTM` 기준시각을 0으로 되돌리는 결함이 있음. 원본 `docs/code_analysis/analysis_frmod.md`에서도 동일 문제 지적.
- `GNU`는 토양 격자에 정의된 침식률로서 링크/하도 격자 전체에 일괄 적용해서는 안 됨.
- **결정: 출력 44 단독 사용 금지**. `GNU` timestep 적산 + `DLS` 시작/종료 차이를 외부 독립 계산해 교차검증. 44번 자체도 장기적으로 초기화 및 시간 기준 정정 테스트 가능.

## 5. 토사 저장과 다음 사상 초기조건
- `SYCOLM` source `src/sediment/SYmod.f90`는 `DDLS=FETA*GNU*DTSY`를 통해 원토양의 입경분포 `SOSDF`를 표층 유사 공급으로 환산하고 `DLS`, `FBETA`, `FDEL`을 이동/퇴적 후 갱신한다. `FETA=(1-THSAT)/(1-PLS)`가 관련 초기화 `SYINIT`에 존재.
- `SY51`: 초기 `DLS` [m], `SY52`: 표층 퇴적물 조성 `FBETA`, `SY53`: 부유사 `FDEL`. 실제 `examples/Cobres/model/input_cob_syd.txt`에서 초기조건 입력 확인.
- 하도가 있으면 `DLS` 하나만으로 부족. channel `DCBED`, `DCBSED`, `DDBSED`, `ARBDEP` 및 하도 저고/형상도 별도 검토.
- 수문 `HOTSTART`는 `docs/Hotstart.md`와 `run_sim.f90` 확인 시 수관 `CSTORE`, 수면/지하수 상태 `HRF,VSPSI` 등을 기록하나 **퇴적층 `DLS,FBETA,FDEL` 전체 자동 저장은 확인되지 않음**. 지형이 변할 때 기존 절대수위/지하수 수두와 VS 수직격자의 정합성을 반드시 검사.
- `FRmod.f90` `:FR37`은 `ZGRUND` 지형 입력을 읽음; 새 격자고도 재입력 시 전체 도메인/요소 대응관계 유지와 관련 지반/토양층 경계의 일관성이 필요.
- 산불 후 사암 암편 공급, 변형, 토심 소진과 bedrock 노출 제한은 원본 SHETRAN 자동 모델 기능이 아님. 외부 상태와 근거식이 필요.

## 6. 재현 가능한 최소 검증
1. Native Cobres sediment example 무변경 실행(소스와 binary 버전 비교). 모델이 계산됐다는 주장은 재실행 후에만.
2. 비강우/비유출: `GNU≈0`, `DLS_end≈DLS_start`, `delta z≈0`.
3. 침식만 유도한 단일 격자: `delta z≈-sum GNU dt`; 퇴적만 유도하면 `delta z≈delta DLS`.
4. 초기 `DLS=0` 이후 새 퇴적 발생: `CASE44`와 독립 적산 차이 점검.
5. 사상 n 종결 퇴적층 `DLS/FBETA/FDEL`을 n+1 초기조건으로 재입력하고 **강우 0**의 후속 짧은 실행에서 비물리적 퇴적 초기화나 대량 유사 발생 여부 검사.
6. water budget `BALWAT` 및 격자와 출구별 외부 sediment balance 작성. **원본 `BALSED`는 현재 빈 함수**이므로 별도 질량수지 계산 필수. 전체 입경별 유사유출량과 표층 저장, 부유 저장, 원토양 제거의 밀도/공극률 환산 일관성 검증.
7. event1 DEM 업데이트 후 event2에 동일/변경 지형 투입한 두 조건에서 `ovr_flow`, `s_v_er`, `s_t_dp` 차이와 인공 초기충격 검사. 10,20,30,40,50 mm/h 민감도는 검증 종료 후 실시.
8. 지형 변동과 토심 한계를 현장 TLS/드론 고도차, 암편분포로 검증. 원본 SHESED 기반 산지 유동은 진정한 2D 공간 격자형 확산파이지만 dynamic SWE가 아니며 자동 rill incision도 없음.

## 7. 판정
- **사상별 DEM 전달 가능성: 소스 기준 조건부 가능**.
- **출력 44번을 곧바로 DEM 갱신량으로 사용: 보류** (초기화/시간 기준 오류).
- **원본 native 모델 실제 유사/물수지 및 재시작 성공: 아직 검증하지 않음**.
- **고운사 최종 적용성: 후보 유지**. 강우강도, 고기복 격자, 원토양/표층 퇴적층, 식생(억새 vs 참나무 맹아), 암편, 토심과 하도 갱신을 비교검증한 뒤 결정.


## 후속 전체 소스 감사로 추가된 제한
[2026-10-26_SHETRAN_472_FULL_PATH_SOURCE_AUDIT.md](2026-10-26_SHETRAN_472_FULL_PATH_SOURCE_AUDIT.md)에서 첫 sediment step은 `SYMAIN`의 초기화 전용 경로로 생략, 수문 timestep 내 `GNU` 고정에 따른 `DLSMAX` 저감 지연, `VS08` 토층깊이 재설정, water hotstart 및 sediment 경계조건의 원본 미완성을 추가 검증하였다. 이 문서의 '조건부 가능'은 실행 성공 판정이 아니다.
