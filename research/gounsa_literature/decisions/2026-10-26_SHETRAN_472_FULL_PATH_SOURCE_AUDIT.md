# SHETRAN 4.7.2 원본 전체 호출경로 소스 감사: 고운사 강우사상별 지형갱신

일자: 2026-10-26
판정 유형: **공개 원본 Fortran 소스의 정적 검증**. 실행 또는 교정 완료 보고서가 아님.
소스 버전: `nclwater/Shetran` master의 고정 SHA `cf9cd540add78ad3accbaf62b4199d2032887f6b`.
선행 기록: [native call graph](2026-10-26_SHETRAN_472_NATIVE_IMPLEMENTATION_CALLGRAPH_AUDIT.md), [event DEM state audit](2026-10-26_SHETRAN_EVENT_BOUNDARY_DEM_STATE_AUDIT.md), [SHETRAN lineage](../models/SHETRAN.md).

## 0. 감사 방식과 범위
이전처럼 일부 함수만 확인하고 사용할 수 있다고 결론짓지 않는다.
1. `PROGRAM SHETRAN` → `SIMULATION` → `FRINIT` → `INFR,OCINI,FRDIM,INBK,VSIN` 및 hotstart.
2. `TMSTEP` → `ETSIM/ETIN/ET` → `VSSIM` → `OCSIM/OCQDQ/OCQGRD`.
3. `SYMAIN` 첫 호출 초기화 → `SYREAD/SYINIT` → 후속 호출 `SYWAT/SYOVER/SYBKER` → substeps `SYCOLM/SYLINK/SYBED`.
4. `BALWAT/BALSED/FRRESP/FROUTPUT`, HDF5 `visualisation_interface_left/centre/right`.
5. `FR37/OC35/VS08/SY51-SY53` 입력과 water hotstart가 다음 강우사상에 실제로 전달하는 상태를 추적.
읽은 주요 파일: `src/Shetran.f90`, `src/driver/run_sim.f90`, `src/driver/rest.f90`, `src/frame/FRmod.f90`, `src/evapotranspiration/ETmod.f90`, `src/subsurface/VSmod.f90`, `src/overland_channel/OCmod.f90`, `src/overland_channel/OCmod2.f90`, `src/overland_channel/OCQDQMOD.F90`, `src/sediment/SYmod.f90`, `src/sediment/SED_CS.F90`, `src/visualisation/visualisation_interface_left.f90`, `src/visualisation/visualisation_interface_centre.f90`, `src/visualisation/visualisation_interface_right.f90`, `src/core/state/AL_C.F90`과 저장소 내부 `docs/code_analysis/analysis_*.md`. 분석 문서는 구현 동작과 구분한다.

## 1. 직접 코드 확인 항목 (A: 정적 소스 사실 확정)

| ID | 결과 | 실제 코드 | 사상별 고운사 적용에 미치는 영향 |
|---|---|---|---|
| A01 | **처음 `SYMAIN` 호출은 퇴적 초기화만 수행**. `run_sim`의 첫 `SYMAIN` 호출은 최초 `ETSIM/VSSIM/OCSIM` 이후임. `PASS_symain==1` 분기는 `SYREAD/SYINIT`만 실행하고 침식수송의 `ELSE`를 건너뜀. | `run_sim.f90` L220-265, L264-318; `SYmod.f90` L3391-3450 | 첫 수문 시간간격 유사수송 누락 가능성 확정. 강우가 시간 0부터 시작하면 필수 시험 및 초기화 호출 이동 필요 |
| A02 | `SYOVER`은 수문 한 시간간격당 한 번 `GNU`를 산정. `SYCOLM`은 `NEPS` 하위간격마다 `DLS` 변경하지만 `GNU`는 유지 | `SYmod.f90` L3464-3493, L3586-3589, L3799-3803 | `DLSMAX` 초과 이후에도 해당 수문 단계에서 원토양 박리가 지속될 수 있음. 민감도 검증 필수 |
| A03 | `SYCOLM` 원토양 박리의 느슨한 퇴적층 공급 깊이는 `DDLS = FETA * GNU * DTSY`, `FETA=(1-THSAT)/(1-PLS)` | `SYmod.f90` L1214-1225, L2975-2982 | 원지반 `GNU` 두께와 표층 퇴적 `DLS` 두께는 동일 물성의 두께가 아님. 질량 환산 검증 |
| A04 | `s_v_er=GNU * 86400000` mm/day, `s_t_dp = DLS * 1000` mm, `s_dis=RHOSED*QSED` kg/s는 **상태 순간값과 face 유사유량** | `visualisation_interface_left.f90` L885-901, L1010-1040; `visualisation_interface_centre.f90` L294-312 | 기본 HDF5 관측 간격만으로 `GNU`를 정확히 적산했다고 주장 금지. 수문 전체 내부 간격에서 double-precision 누적 필요 |
| A05 | `FRRESP` #44는 `GNUCUM - 1000*(DLS-DLSSRT)`, `GNUCUM+=GNU*(RESNOW-PREVTM)*3600*1000` | `FRmod.f90` L3482-3491, L3678-3698 | 수치식 구조만 근거로 사용. 출력 44번 무검증 사용 금지 |
| A06 | `GNUCUM`, `PREVTM`에는 첫 사용 전 보장된 초기값이 없고, `SEDSRT`는 `DLS>0` 발견 후에야 기준상태 확정. `FRRESP`에 `RESNOW=0`을 넘기는 contaminant 초기화 경로 존재 | `FRmod.f90` L155-160, L3482-3491; `run_sim.f90` L323-332 | 출력 44번 시간적산 및 첫 퇴적 발생 시 기준두께 불일치 위험 |
| A07 | `BALSED` 본문이 비어 있음 | `SYmod.f90` L4668-4669 | 원본 내장 유사 질량보존 검증 없음. 별도 입경별 질량수지 필요 |
| A08 | `SYBC` 본문이 비어 있는데 `NSYB>0`이면 `QSEDB`를 `QSED`로 복사함. `QSEDB`의 생산 코드 확인되지 않음 | `SYmod.f90` L528-530, L3496-3518 | 퇴적물 외부 경계유입 조건 `NSYB>0` 사용 금지(별도 구현검증 전) |
| A09 | `SY51` 초기 `DLS`, `SY52` `FBETA`, `SY53` `FDEL` 입력 존재 | `SYmod.f90` L4220-4250 | 새 강우사상에 표층 저장과 입경별 유동상태 전달은 가능하지만 외부 입력파일 재구성 필요 |
| A10 | water hotstart는 `CSTORE, HRF, QSA, QOC, DQ*, SD,TS,SMELT,TMELT,VSPSI` 등 수문 상태를 기록. **`DLS/FBETA/FDEL/DCBED/DCBSED`는 기록하지 않음** | `run_sim.f90` L358-385; `FRmod.f90` L1353-1407 | hotstart만으로 sediment restart 불가능. 변경 DEM과 기존 수두, 수리유량 상태의 충격 검사 |
| A11 | grid `ZGRUND`는 `FR37`; channel link `ZGRUND`는 `OC35` 계열 입력에서 재할당하고 bank는 별도로 처리 | `FRmod.f90` L5626-5631; `OCmod.f90` L1670-1693; `FRmod.f90` L4015-4180 | 원본 DEM 파일만 바꾸면 하도 및 bank 고도가 불연속 가능. link-bank-grid 동시 갱신 |
| A12 | `VS08`의 `ZLYRBT = ZGRUND - RVSDUM`, 표층 `NTSOTP`는 `SYMAIN` 초기화 시 결정 | `VSmod.f90` L3630-3669, L3700-3730; `SYmod.f90` L3408-3411 | DEM만 낮추고 VS08 토층 두께를 그대로 두면 원래 토양층이 자동으로 새 지표면에 따라 내려가서 토심 감소가 재현되지 않을 수 있음 |
| A13 | `SYOVER` 원지반 박리는 `GNU=(DR+DF)/RHOSO`; `FCG`는 `DR`에 직접, `FCROCK`는 `DR/DF` 양쪽에 적용. `DLS>=DLSMAX`이면 `GNU=0` | `SYmod.f90` L3766-3803 | 뿌리량/RLD가 원본 `GNU`에 직접 들어가지 않음. 피복과 뿌리를 혼동하지 않는다 |
| A14 | `OCQGRD`는 인접 face 수위경사와 Strickler conveyance 기반 확산파; 관성 포함 2D 천수방정식 아님. `SYMAIN`의 `ZGRUND` 인자는 `INTENT(IN)` | `OCmod2.f90` L996-1064; `SYmod.f90` L3320-3332 | 강우사상 내부 지형갱신이 없지만 사상 사이 외부 갱신은 가능. 세류 미세 지형의 sub-event feedback은 해결되지 않음 |
| A15 | `SYBED`는 `DLS(link)`, `ARBDEP`, `DCBED`, `DCBSED`, `DDBSED`를 갱신하나 이 명령이 `ZGRUND`를 직접 변경하지 않음 | `SYmod.f90` L576-663 | 하도 퇴적 계산과 하도 수리 지형변경을 같은 기능이라고 하면 안 됨 |
| A16 | `TMSTEP`에서 `UZNEXT`를 강우량 한도 `PMAX/PINP` 등에 따라 단축하고 `precip_m_per_s=PTOT/UZNEXT/3.6E6`로 설정 | `rest.f90` L1325-1382 | 10–50 mm/h 실험에서는 같은 사건 지속시간, total rainfall, time-step 적산로그 확인 필요 |
| A17 | visualization 초기 호출은 `SYMAIN` 초기화 전에 이루어짐. `s_v_er,s_t_dp` getter는 단순 state read | `run_sim.f90` L218-263; `visualisation_interface_right.f90` L167-286 | 초기 시간 0의 sediment HDF5 snapshot은 초기화 여부 확인 전 신뢰하면 안 됨 |

## 2. 특정 설정에서 재현 가능한 원본 결함 또는 검토항목 (B: 사용 조건 명시)
1. **화재 직후 수관저장능 0**: `ETmod.f90` L495-504에서 `F1 = MIN(CT1/CSTCAP,ONE)`를 `CSTCAP<=0` 분기보다 먼저 계산. `-ffpe-trap=zero,invalid`로 검증; 나지/저 LAI 시나리오에서 중요한 예외.
2. **눈 기능 BEXSM 활성**: `ETIN` L800-817에서 `ET`을 건너뛰는 경로는 공유 변수 `DRAIN,PNET`의 새 값 할당을 보장하지 않음. `SMmod.f90`의 해당 경로까지 계절별 cold/dry 시험 필요. `docs/code_analysis/analysis_etmod.md` C1과 원본 `ETIN`을 대조.
3. **외부 수면 경계 + 음수 STRXX 저장마커**: `OCQDQMOD.F90` L184-202는 marker override 없이 음수 Strickler를 `OCQBC`로 전달. 내부 face L223-230, L316-323은 별도 override. `docs/code_analysis/analysis_ocqdqmod.md` C1과 대조. 조건 충족 시 경계유량 부호/solver 이상 가능.
4. **FRIND topology**: `FRmod.f90` L1173은 갱신되지 않은 `ITYPE`을 참조하는 consistency loop. `FRIND` 코드그리드 가장자리의 `I-1,J-1` 등의 인덱스 접근도 경계 마스크와 bounds-check 검사 필요. 내부 `analysis_frmod.md` 1.1~1.3.
5. **퇴적 경계 NSYB**: native `SYBC` 미구현은 일반적인 모든 영역에서의 `QSED` 실패를 뜻하지 않음. 외부 퇴적 경계유입을 활성화한 경우 한정.
6. **본체가 restart할 때**: `PASS_symain`은 모듈 변수이며 실행 중 세그먼트별 호출은 설계되어 있지 않음. 매 사상 별도의 프로세스 재실행/입력 재구성을 우선하고 동일 프로세스 재호출 시 reinitialization 명시해야 함.
7. **고운사 얕은 토양**: 원본 erosion step에는 사용 가능한 잔존 토심 `H`를 `GNU`에 따라 감소시키고 bedrock에서 박리량을 제한하는 코드가 없음. 이는 모형의 범위 한계이지 native 코드 오류라고 구분한다.
8. 원본 `SYOVTR`의 Engelund-Hansen/Yalin 수송능은 산지 산림 사면의 수리/유사조건에서 별도 적합성 검증 필요. 이 식에 root dynamics가 자동 내장되지는 않음.

## 3. 이전에 적절히 분리하지 못한 물리적 상태
다음 사상에 `z_s`만 넘기는 것은 **불충분**. 적어도:

| 계열 | 사상 경계 전달 또는 재구축 대상 | 근거 및 검토사항 |
|---|---|---|
| 물리적 고도 | `z_s, z_b`(외부 정의), grid `ZGRUND`, link `ZGRUND`, banks `ZGRUND` | grid DEM과 하도 및 bank 형상 일관성 |
| 퇴적 저장 | land `DLS, FBETA, PLS`; mobile `FDEL`; channel `DLS, DCBED, DCBSED, DDBSED, ARBDEP` | sediment hotstart 불완전; SY51-53과 channel initialisation 점검 |
| 토층 | 잔존 깊이 `H`, bedrock level, `NLYR,NTSOIL,ZLYRBT`, `VS08`, surface `NTSOTP` | 얕은 토양 유실 후 원위치 토양층을 그대로 재생성하지 않음 |
| 물 | `CSTORE, HRF, VSPSI, VSTHE`, 수면 깊이 `HRF-ZGRUND`, `QOC`, `DELTAZ` | 새로운 수리기하에서 초기 압력헤드 및 질량 불연속 방지 |
| 식생 | `NVC,CLAI,PLAI,FCG,FCROCK`, 식생별 XDRIP,DRDRIP,FDRIP, roughness 입력 | 원본 처리기능, 외부 LPJ-GUESS root/litter interface 구분 |
| 암편/토양생산 | spall 공급, 외부 암편 저장, 풍화 및 soil production | native 기능 아님, 새 coupling |

## 4. 지형식과 누적 방식의 정확한 한계
사상 n에 대해 원토양 침식두께 `E_i = Σ_{k∈n} GNU_i(k) DTUZ_k` [m], `DLS_start/end` [m]를 읽어
`z_surface_next = z_surface_start - E + (DLS_end-DLS_start)`
를 **사상 사이 외부 연동식으로 사용 가능**. 단 이 식은 `z_surface`가 느슨한 퇴적층까지 포함하는 실측 지표고도라는 기준에 따라 적용; 첫 사건의 `DLS_start`를 중복 더하지 않는다. `DLS`는 느슨한 퇴적층의 두께이며, 항상 안정화된 최종퇴적지형이 되는 것은 아니다. bulk porosity/soil solid fraction에 따른 질량 환산이 필요.

**권장 수치 적산의 단위와 정확도**: `dt=DTUZ` [s]를 쓰고 `GNU` [m/s]를 물리적 sediment step 이후마다 double precision으로 기록한다. 기존 HDF5 `s_v_er`는 기록 시각의 REAL형 순간 관측이므로, coarse HDF5 출력 사후 적분만으로 원본 timestep 적분 재현을 보장하지 못한다. `FRRESP` id44 버그 수정 없이 `GNUCUM`을 절대 참값으로 두지 않는다.

## 5. native 재현 실험의 합격 기준 (아직 실행되지 않음)
1. Cobres sediment 원본을 **일체 수정 없이** 실행하고 원본 로그 및 HDF5가 재현되는지 확인.
2. 매우 짧은 강우 event에서 첫 hydrological timestep `GNU,QSED` 기록: 시간0부터 강우 시 missing sediment step 재현.
3. `NEPS`를 1,2,5,10으로 바꿔 `DLSMAX` 교차 시각과 `E,DLS` 변화 추적. `DTUZ`도 독립 민감도.
4. `BEXSM=false/true`의 dry freeze, canopy `CSTCAP=0`, vegetation `CLAI=0`: 모든 변수 finite, 비강우 상태 물수지 잔차 제한.
5. `NSYB=0` 기본 vs `NSYB>0`: latter는 기대 실패 또는 수정 후 benchmark 필요.
6. `s_v_er` snapshot 사후 적산 vs 내부 `ΣGNU DTUZ`, `FRRESP` 44와 3자 비교.
7. event1 최종 상태 `DLS/FBETA/FDEL` 및 hydrological heads 재입력, event2 0강우 시험에서 인공 침식, 퇴적, 유출 충격이 없어야 함.
8. 일정 bedrock과 두 soil horizon 설정한 경사 실험에서 erosion 후 `VS08` 갱신, `H` 감소, `NTSOTP` 노출 전환, bedrock cap 검증.
9. grid-link-bank 2D 영역에서 DEM 변경과 수리하도 경계 연속성을 확인. 위어, head, 외부 boundary, 음수 STRXX 사용 시 별도 조건부 검사.
10. 모든 격자별 water-budget와 입경별 sediment solid-volume budget: initial soil solids + boundary inflow = final soil solids + final loose/suspended/channel storage + outflow (부호 및 동등부피 기준). 허용 오차는 solver/기준치 사전 결정.
11. 10,20,30,40,50 mm/h의 동일 강우사상과 동일 입력 상태 비교, 0강우 및 연속 강우와 토양두께 한계 시험.
12. DEM 갱신 후 event2가 event1과 동일 hydrograph를 만드는 잘못된 경계/상태 초기화가 없는지 확인. 변화 발생 시 모든 수지와 물리적 원인을 확인.

## 6. 현재 판정
**SHETRAN은 검토후보 유지, 즉시 최종채택 불가.**
- confirmed native features: 수관저류와 수관적하, 지하수/불포화 수문, 2D 평면 격자 확산파, 원토양 박리/입경별 퇴적층 유사수송.
- missing or defective for Gounsa: 첫 단계 퇴적 초기화, 내부 누적/시간기준 부정확, 퇴적 수지 부재, sediment restart, 토심/암편/식생뿌리 동역학 외부결합, 사건 내부 지형 미갱신.
- **최소한 native 원본 예제 실행 및 물/유사 수지 확인 전에는 모델이 성공적으로 구동되었다고 쓰지 않는다.**
- repository `docs/code_analysis`는 설계/정적 감사문이지 실제 numerical acceptance test가 아니다. 본 보고서도 실제 native 수치시험이 아니다.

## 7. 원본 확인 링크
- [run_sim.f90](https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/driver/run_sim.f90#L218-L396)
- [SYmod.f90](https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/sediment/SYmod.f90#L3391-L3656)
- [FRmod.f90](https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/frame/FRmod.f90#L3456-L3698)
- [ETmod.f90](https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/evapotranspiration/ETmod.f90#L451-L531)
- [VSmod.f90](https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/subsurface/VSmod.f90#L3625-L3740)
- [OCQDQMOD.F90](https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/overland_channel/OCQDQMOD.F90#L184-L359)
- [visualisation_interface_left.f90](https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/visualisation/visualisation_interface_left.f90#L885-L1040)
