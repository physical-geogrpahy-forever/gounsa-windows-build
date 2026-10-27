# 고운사 단일 강우사상 연구: SHETRAN 대 EUROSEM 원본 코드 전경로 감사

작성일: 2026-10-27, 아시아/서울.
범위: **기존 단일모델만**. 결합모델, Rutter+SWEHR 신모델 개발, 장기 식생천이와 풍화는 이 의뢰의 답이 아니다.
연구질문: **1ha 미만 단일 혼재식생 사면**의 실제 참나무 맹아와 억새가 **같은 DEM 안에** 있을 때, 동일 한 강우사상에서 **식생 수관차단을 ON/OFF**한 두 원본모델 계산의 국지 침식, 퇴적, 순지형변화 지도 차이.

## 0. 원본 증거와 검증 수준 분류

- SHETRAN 원본: [nclwater/Shetran, SHA `cf9cd540add78ad3accbaf62b4199d2032887f6b`](https://github.com/nclwater/Shetran/tree/cf9cd540add78ad3accbaf62b4199d2032887f6b), CMake 버전 4.7.2.0, GNU GPLv3, commit timestamp 2026-10-12. 본 세션에서 실제 upstream 코드 `ETmod.f90`, `SYmod.f90`, `OCmod2.f90`, `sglobal.f90`, `FRmod.f90`를 **GitHub connector에서 새로 원문 재취득해 함수별 확인**. 기존 [2026-10-26 6회 원본 native CI](2026-10-26_SHETRAN_472_NATIVE_COBRES_RAIN_QA.md) 실행은 이미 완료. **이번 10-27 세션에서 원본을 새로 빌드/실행하지 않았다.** 현재 컨테이너는 github.com DNS 접근 불가.
- EUROSEM 원본: [TheSoilman/EUROSEM, SHA `8652944da6e1e8436495aa0c08765e2399830dd7`](https://github.com/TheSoilman/EUROSEM/tree/8652944da6e1e8436495aa0c08765e2399830dd7), 1998 Fortran 공개본이 2023 GitHub에 수록된 형태. 이번 세션에서 `emainl.for`, `eurseml.for`, `eplanel.for`, `eusedl.for`, `eurozl.for`, `Euroa.for`, `test.par` 실제 읽음. 기존 [2026-10-26 24회 원본 보존검사](2026-10-26_EUROSEM_1998_NATIVE_SEDIMENT_LEDGER_RILL_FAILURE.md)와 [시간간격 검증](2026-10-26_EUROSEM_729_LOW_VEGETATION_SENSITIVITY_ROOT_CAUSE_REAUDIT.md)을 중복 실시하지 않았고 기존 CI 기록과 비교.
- 검증 등급: **SOURCE CONFIRMED**는 코드상 계산경로 존재, **NATIVE RUN CONFIRMED**는 기존 Actions 원본 구동 성공, **MASS/CONVERGENCE/OBS NOT VERIFIED**는 아직 독립적으로 입증되지 않았음을 의미. 원본 수치 실행 성공은 측정현장 재현성이나 질량보존 검증과 동의어가 아니다.

## 1. SHETRAN 4.7.2: 함수 및 실제 입력과 출력

### 1.1 원본 수관차단 호출
`src/evapotranspiration/ETmod.f90`:
- `ETSIM` (L918 이후)에서 격자별 `ETIN(IEL)`.
- `ETIN` (L790-825)에서 셀 `NVC(IEL)` 식생유형을 읽고 `CPLAI=MIN(CLAI(N),1)*PLAI(N)` 계산, `ET` 호출. 실제 코드에서 `CLAI` 수관 상태가 피복된 수관면적과 강우차단에 작용하지만, **LAI >1일 때 `MIN(CLAI,1)`로 포화**되는 구조. `CLAI`와 `PLAI`의 식생학적 정의/매개변수 배정은 입력매뉴얼까지 확인할 필요가 있음.
- `ET` (L451-532): `CSTORE(IEL)` [mm], `CSTCAP(N)` [mm], `CK(N)`, `CB(N)`, `DRAIN`, `EINT`, `PNET`. 직접통과 `PNET_0=precip*(1-CPLAI)*dt`, 수관흡수/증발 `Q=CPLAI*(precip-PE)`, 저장과 배수 질량보존을 사용. `PNET+=DRAIN`; 최종 `ETIN`에 `PNETTO=PNET/1000` [m/s], `DRAINA=DRAIN/(1000*DTUZ)` [m/s].
- **LAI가 수관저장능을 자동 결정하는 식은 없다.** `CSTCAP`은 식생유형별 독립 입력, 시변값 입력방식은 `MODECS` 존재. 따라서 참나무/억새별 LAI, 수관저장능, 배수계수, 줄기/초본 높이를 실제 입력으로 별도 지정해야 하며, `CLAI`만 바꾸고 전 물리를 자동 재보정한다고 주장 금지.
- **코드 결함 검증 필요**: `ET`에서 `F1=MIN(CT1/CSTCAP(N),ONE)`를 `CSTCAP<=0` 예외 처리보다 앞서 계산한다 (L495-505): 0 저장능으로 OFF를 구현하면 부동소수점 0 나눗셈 가능. `ETIN`의 `BEXSM` 눈모듈 활성화 시 `ET` 미호출 분기가 공유 `DRAIN`, `PNET`의 새 값 할당을 보장하지 않는다고 upstream 정적 주석도 경고(L758-761). 고운사 비적설 단일 사건에서 눈모듈 비활성화 시 예외 분리 가능하지만 원본 전 조건 검증으로 포장 금지.

### 1.2 강우에너지와 강우/유수 박리의 내장 연결
`src/sediment/SYmod.f90`:
- `SYMAIN` L3450-3468에서 `SYWAT`→`SYOVER`, 그 뒤 입경별 `SYCOLM`과 경계 전파. `SYWAT` L4413+의 `FCC=PLAI*MIN(CLAI,1)`, `DRAINA`, `PNETTO`, `DRDROP`, `LRAIN`을 전달.
- `SYOVER` L3766-3803에서 `GMR=(1-FCC)*a*LRAIN^b`, `GMD=TGMD(XDRIP,DRDRIP,FDRIP)*DRAINA`; 강우박리 `DR=GKR*exp[-max(0,DWAT1/DRDROP-1)]*(1-FCG-FCROCK)*(GMR+GMD)` [kg/m²/s], 유수박리 `DF=GKF*(1-FCROCK)*max(0,tau-tauc)/tauc`. `GNU=(DR+DF)/RHOSO` [m/s], `DLS>=DLSMAX`면 새 원토양 박리 0.
- **양쪽 박리항은 실제 별개의 식이지만, 수문 경로상 강우사상의 유효강우 변화가 전단응력에도 영향을 준다.** 식생 canopy ON/OFF가 두 항의 변화로 전달되는 것이 가능. `FCG`와 `FCROCK`은 지표 보호용 별도 입력이며 LAI 또는 생물량과 같은 변수가 아님. `FCG`는 강우박리에만 직접 적용, 유수박리는 `FCROCK`만 명시적으로 적용. 뿌리량/RLD 기반 `GKF,GKR` 자동 갱신은 없고, 1회 사상 두 run 사이에 토양값을 동일하게 유지하면 실험의 통제변수는 지킬 수 있다.
- **현장 혼재 식생 공간화**: `NVC(IEL)`는 셀별 식생유형, `NVC`가 수관 매개변수군을 연결. `FCG(IEL),FCROCK(IEL)`는 격자별. 원본 코드에서 2종 이상 식생 입력은 가능. 동일 격자 안에서 참나무 수관과 억새 상하층이 정확히 중첩되는 층별 2-수관 저장/배수는 `NVC` 단일값으로는 직접 표현되지 않는 한계.
- **원형 수간유하우 위치**: ET+SY 체인에서 per-stem basal source는 확인되지 않았음. `DRAINA`는 기본적으로 해당 격자 수관적하, 기부 집중 물공급이 아님. 사용자에게는 stemflow 우선순위가 낮지만 없다고 명시할 필요는 있다.

### 1.3 2D 수리 및 입경별 이송/퇴적
- `src/overland_channel/OCmod2.f90::OCQGRD` L996-1064: 수면고도차 `DZ=ZI(1)-ZI(0)`, 수심 `HM=ZI(HI)-ZGI(HI)`와 Strickler roughness·face width, `Q(LO)=CONVM*sqrt(|DZ|)/sqrt(L)`, `Q(HI)=-Q(LO)`. 지표 4방향 격자의 **2D 확산파 형식**; 온전한 2D 운동량/관성 포함 Saint-Venant solver가 아님. 억새 포기/그루터기 사이의 run-around/runon에 대해 해상도 의존적 효과가 있으니 특히 microtopography와 관측 비교 필요.
- `SYMAIN` L3545-3610: `ISORT` 순서에 따른 element 순회, `QOC(IEL,FACE)` 네 면에서 물 유량 읽음, `SYCOLM` 4면 입경별 유사유량 `QSED`를 주변 셀 `ICMREF`로 전달. 이는 1D D8 하도라우팅과 다르며 명시적인 **4-face sediment transport** 경로가 존재.
- `SYCOLM` L1139-1296: `FDELE` 부유 이동상, `DLSE` loose-layer depth, `FBETAE` 입도, `SOSDFE` 원토양 입도, `QSEDE` 면별 유사 플럭스. `DDLS=FETA*GNUE*DTSY`로 새로 박리된 원토양을 이동가능한 표층상에 공급하고, 가용 공급량과 `SYOVTR` 수송능, `FPCRIT` 농도 제한에 따라 면별 이송 및 남은 `DLS` 갱신. **흐름 도중 유사 이동과 국지 퇴적은 내장**.
- 주의: `SYCOLM`에 실제 현장 토심 `H`를 원토양 박리 가능량 상한으로 제한하는 로직 없음. `DLSMAX`는 퇴적물 보호 임계두께이지 **잔존 토심 제한이 아니다**. 암반이 얕은 곳의 과도 박리를 필터링하지 못하면 물리적 결과 부적합.
- `SYOVER`에서 `GNU`는 한 수문간격에 한 번 계산, `NEPS` 유사 하위시간단계에서는 `DLS`가 바뀌어도 같은 `GNU` 사용. `DLSMAX`를 중간에 넘을 때 박리중단이 다음 수문간격까지 늦어질 수 있다.
- 원본 `ZGRUND`는 `SYMAIN` `INTENT(IN)`; 흐름에 영향을 주는 DEM은 사건 중 새 토사퇴적/박리로 갱신되지 않는다. 1회 계산에서 **event-end local deposition and gross erosion maps는 계산 가능**, 다만 `∆z` 자체는 보존된 `GNU` 시간적산과 `DLS_end-DLS_start`로 후처리 추산해야 하며 **사건 중 자동 rill-incision/굴착 피드백은 없다**.
- `src/core/sglobal.f90` L119-133: 수평격자 범위 1000x1000, 총 요소 250000, 입경 상한 7종. 예컨대 100x100m, dx=0.5m -> 200x200=40000 grid는 **정적 배열 상한 이내**. 실제 해당 해상도 계산 성능, 안정성 및 자료 지원 여부는 미검증.

### 1.4 출력을 사용하는 데 필요한 경고
- **원본 `BALSED`는 빈 SUBROUTINE** (`SYmod.f90` L4668–4669). 따라서 코드의 개별 이송식은 보존형으로 보이지만 **전체 입경별 총유사 질량보존을 실제 확인했다고 하면 안 된다**.
- 기존 native Cobres `s_v_er` [mm/day]는 시간별 **순침식량이 아닌 원토양 박리 속도**, `s_t_dp` [mm]는 loose-deposit depth, `s_dis` [kg/s]는 sediment face flux. `s_v_er`를 사건 전체 시간에 적산한 `E_orig`와 `s_t_dp(end)-DLS_initial`로 구분. `∆z_approx=-∫GNUdt+(DLS_end-DLS_start)`는 density/state 일치가 확인된 경우에만 사용하고 **순부피의 보존을 별도 증명**.
- **초기 출력 BUG**: Cobres native 예제의 `SY51 DLS_initial=30mm`인데 HDF5 시각 0 `s_t_dp=0mm`는 SYMAIN 초기화 전 출력. 처음 보이는 30mm를 강우 퇴적이라고 잘못 판정할 위험. 반드시 실제 SY51 입력기준 비교.
- **종료시각 초과**: 기존 native 48시간 Cobres 실험 종료표에서 18.90–51.73분 초과한 기록 존재. 1시간/수시간 강우 직후 정확한 출력 비교에는 매우 부적합할 수 있으므로 종료시간을 두 사건에서 동일한 정확한 timestamp로 제한하는 테스트 필요. 원본 time end gate, adaptive timestep 확인.
- **첫 sediment timestep 누락 위험**: `SYMAIN` 첫 호출은 `SYREAD/SYINIT`만 하고 침식/이송은 `ELSE`에 있으므로, simulation 첫 수문 timestep 후 첫 SYMAIN 호출이면 첫 강우단계 sediment 계산이 빠진다. 이전 `run_sim` 감사 자료로 실제 호출위치를 확인. 한 시간 폭우 시작 직후에는 치명적일 수 있음.
- **경계조건**: `SYBC` 빈 stub임에도 `NSYB>0`이면 외부 sediment boundary 입력을 쓰는 코드경로 존재. 외부 sediment inflow는 비활성화된 zero-inflow domain으로 제한 후 검증.

### 1.5 독립 기존 native 실행성과, 정확한 의미
- [Actions 40287116566](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40287116566): 원본과 동일한 코드를 GNU Fortran으로 컴파일, 원본 Cobres 2 km 육상격자 176개에서 건조 및 10/20/30/40/50mm/h 강우 **3시간** + 총 48시간 출력 **6/6 실행 성공**. 수관과 토양입력은 원본 Cobres. `s_v_er` 최대는 강우별 2.708,67.260,105.330,133.284,430.591 mm/day; `s_t_dp` 변화도 발생. **이 수치가 1ha 미만 고운사 국지 침식량이라는 주장 불가.**
- 독립 입경별 유사질량수지, 0.5–1m 격자 수렴성, actual mixed vegetation `NVC` map, canopy ON/OFF pair, hotspot erosion/deposition spatial validation, zero-initial soil stock 또는 bedrock guard는 기존 CI에서 **미검증**.
- 결론: 구현기능이 실제로 가장 충실한 **단일모델 후보**이지만, 지금 상태로 **최종 검증 합격이라고 표기하지 말 것**.

### 1.6 canopy OFF의 원본 실험상 주의
- ON: 같은 사면 `NVC`, `CLAI`, `PLAI`, `CSTCAP,CK,CB`, 각 식생별 `XDRIP,DRDRIP,FDRIP`를 사용.
- OFF: 입력 `PLAI=0`으로 canopy 면적 0을 만들면 `CPLAI=0`과 `FCC=0`, 수관수량/강우충격 감소가 제거되지만 **토양 증발/증산 분할에도 `CPLAI` 사용**하므로 순수한 수관차단만 달라지는 대조인지 점검이 필요. `CSTCAP=0`은 0나눗셈 위험이 있으므로 무검증 설정 금지.
- **정확한 canopy ablation 스위치가 원본 입력에 독립 존재하는지는 확인되지 않았다.** 두 native 시나리오를 동일 NVC/FCG/FCROCK/토양/거칠기/초기 상태에서 실행하는 것은 가능성 있지만, canopy만 분리하려면 원본 변수를 수정할 때 다른 ET 과정이 함께 바뀌는지 확인해야 한다. 원본 실험결과라고 하기 전 A/B 수문상태와 source consistency 검증.

## 2. EUROSEM 1998: 함수 및 원본 공간 한계

### 2.1 수관 인터페이스
- `emainl.for::PAREAD` L957-963 입력: `COVER, ISHAPE, VPANG, PBASE, PLHGT, DERO, ISTONE`; `PLHGT` 원본 파일 단위 cm → m로 변환. **LAI 또는 PFT별 biomass/RLD 실제 내장 입력 없음**.
- `eurseml.for::INTERC` L352-420: `COVER` 비율, `DINTR` [mm]로 `VEGSTO(k)=COVER*DICMAX*(1-exp(-cumd))`; 이산적 `DINTRT=∆VEGSTO`, `TFALL=RAIN*(1-COVER)`, `STEMD`를 `ISHAPE, VPANG`에서 추산, `DRIPD=COVER*RAIN-DINTRT-STEMD`. 식생별 저장 물리라기보다는 **누적강우 경험식**이며 LAI→저장용량 자동 갱신이나 canopy evaporation/drainage dynamics 없음.
- **물리적 유한 저류 검증 필요**: 첫 인터벌 `RAIN=0.1mm, COVER=0.9, DINT=1.5mm` 가정이면 `VEGSTO=0.12847mm`인데 해당 인터벌 canopy intercepted precipitation은 0.09mm, 즉 `DRIPST=-0.03847mm`로 **음수 수관배수 발생이 원식에서 가능**. 이 경우의 실제 native 실행 및 코드예외 처리는 미검증이며 원본 algebraic counterexample. 무조건 모든 강우에서 오류라고 일반화하지 말 것.
- `eplanel.for::PLANE` L~149-230에서 `INTERC`, `KINET` 호출 후 원시 강우 시계열 `QI`에서 `DINTRT/dt`만 차감하여 유효강우 생성. `STEMD`, `DRIPD`, `TFALL`은 **같은 1D 사면요소 안에서 분배된 물량**이지 별도 xy 기부/적하 위치별 지표공급이 아님. 공간구조를 바꾸지 못함.
- `KINET`에서 `DRIPKE = max(15.8 sqrt(PLHGT_m)-5.87,0)*DRIPD/RAIN` (하한 0); `DRIPS`는 `DMMSEC=RMMSEC*DRIPD/RAIN`을 또 써서 적하 박리가 `(DRIPD/RAIN)^2`에 비례함. **강우량에 대한 적하 비율 이중 적용 의심이 원본 코드에서 재확인됨**. [기존 원본 vs 수정 포크 실행](2026-10-26_EUROSEM_729_LOW_VEGETATION_SENSITIVITY_ROOT_CAUSE_REAUDIT.md)에서 박리 `RDET`은 실제 변하지만 일부 총 출력은 수송능 지배로 둔감. 이 이중가중이 반드시 논문과 반대라는 결론은 논문 단위식 대조가 필요하며 임의 수정판을 원본으로 쓰지 않는다.
- 입력 `PLANTH(cm)`를 3으로 입력하면 코드에서 0.03m가 되어 `15.8 sqrt(H)-5.87<0`, 적하 운동에너지가 0. 기존 729 가상실험의 실제 실수임. 3m 식생 입력에는 300cm 필요.

### 2.2 수리, 유사수송, rill profile
- `eplanel.for::PLANE`: 요소 `XL,W,S`에 대한 downslope 단면 1D 유동, 요소 연결 `NU/NR/NL/NC`, `IMPLCT` overland/interrill, `XPLINF` infiltration, `SEDCOM` detachment/advection. 1D rill/interrill 별 계산을 포함하지만 **동일 2D raster의 x,y 면별 flow exchange 또는 2D 이동 유사 flux 없음**.
- `eusedl.for::SEDCOM` L467-742: `LCH=0` 세류간/면상, `LCH=1` 세류, `LCH=2` 하도; `DRIPS`의 분리된 splash input 및 transport capacity `CAPAC`, `DTRC=DTRF*CEX+RDET`, `DLA` 원토양 박리/퇴적 두께갱신, `DIRNET/DRLNET` 수송집계. 원본 출구 `SEDTO T`과 내부 ledger는 별개.
- `eurseml.for::RILLWI` L64-118: `DELA` 부호로 세류 폭/깊이를 갱신한다. `eplanel.for` L840-870이 `SMDA+=DLA` 후 일정 변화에서 `RILLWI` 호출. **기존 1D 가정 세류단면의 변화**이지 2D 지형격자에서 새 집중류 경로가 발생하는 기능 아님.
- **원본의 유사수지식 존재**: `eplanel.for` L919-922 `rillbal=stout+sumdrl+susprl-sedin`, `inrlbal=sumqirr+sumdir+suspir`. 이전 '유사수지 구현 자체가 없다'는 진술은 오류.
- **가능한 비보존 문제 경로**: `SEDCOM` `RDET`와 `DTRF*CEX` 합의 단위/폭 처리, `DLA`→`DRLNET`과 `RILLWI`의 시간·체적해석, 그리고 집계 `SUSPRL`을 독립 검증해야 함. 과거 단순 수관효과 작다고 해서 physical mechanism이 불가능하다는 주장은 철회. 그러나 누락 저장량 vs 실제 유사 비보존의 정확 원인은 **아직 불명**.

### 2.3 기존 native 실험 결과의 정확한 판정
- [Actions 40326142263](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40326142263): 30/50mm/h × dt15/30/60s × rill off/on × 2 MCODE = 24 실행, 모두 모델 exit와 물수지 통과. **세류 없을 때 총유사수지 0.1% 이내 9/12, 세류 있을 때 0/12**.
- dt15s 세류 포함 전체 slope residual: 30mm/h Govers 14.32%, Everaert 21.48%; 50mm/h Govers 16.99%, Everaert 20.50%. 세류간 → 세류 측방 유사이동은 별도 `QLRAV,CLAT` 계측 [Actions 40326648315](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40326648315)에서 일치하여, 간단한 cross-boundary 전달 누락으로 설명되지 않음.
- **수치적 판단은 세분화**: 원본 dt15/30s 1D test에서 일부 침식 유출량은 0.3% 안팎의 수렴 경향 있음; 전부 시간간격 수치 비수렴 모델이라고 말하면 오류. 하지만 세류 case의 physical ledger는 large residual; 원본 vegetation LAI 입력이 없고 2D x/y 격자 아닌 구조이므로 위 오류를 풀어도 **고운사 혼재사면 국지 E/D 지도용 단일모델로 부적합**.
- 원본 대표 `test.par`는 `NELE=2`, 1차 사면 100m×145m, `PLANTH(cm)`, `COVER` 및 prescribed rills 입력. 이 input 형식으로 1ha 이내 0.5m 2D cell 40000개를 표현할 수 있다는 결론 금지.

## 3. 고운사 현장의 엄격 비교표

| 필수 요건 | SHETRAN 4.7.2 | EUROSEM 1998 |
|---|---|---|
| 한 공개 원본에 canopy+runoff+sediment+deposition 내장 | **YES** | **YES** (1D) |
| 식생 두 유형이 같은 실제 DEM 2D 격자에 혼재 | **YES, NVC(IEL) per cell**; 중첩 혼합피복은 한계 | **NO**, 1D 사면 요소 |
| LAI 등 정량 수관상태가 실제 canopy water에 영향 | **YES partial**, CLAI*PLAI, CSTCAP 독립 제약 필요 | **NO direct native LAI**, COVER+DINT만 |
| 저장, 직접강우/leafdrip 박리 분리 | **YES**, ET+SY call graph 확인 | **YES**, but potential double drip ratio |
| 2D runoff 및 4-face sediment transport | **YES, diffusion-wave** | **NO, 1D interrill/rill** |
| 소사면 국지 퇴적 지도 | **원본 DLS cell update 확인** | 1D profile only |
| 원토양 분리/loose layer | **YES** | partial, ledger failure rilled |
| 강우사상 내 침식에 의한 DEM/흐름 갱신 | **NO** | rill cross-section update only, no 2D DEM |
| 정밀 유사질량수지 직접 검증 | **NO**, BALSED empty | **FAIL for 12/12 rilled** |
| 고운사 0.5m 격자 ON/OFF 결과/관측 검증 | **NO** | **NO** |
| 단일 기존 엔진으로의 연구 적합성 | **조건부 가능성, 검증 전 채택 보류** | **핵심 공간조건 불충족으로 제외** |

## 4. 결론 및 소규모 단일강우 사건에서의 조건부 판정

**EUROSEM은 제외**: 수관 수문 및 박리 모듈이 원본에 있어도 독립적인 진정한 2D 사면 유동·퇴적 지도를 생성할 수 없으며, 세류 원본 수지 불일치도 존재한다. 원본의 약점을 임의 결합/변환으로 회피하면 사용자 '단일모델' 요건과 충돌.

**SHETRAN은 남는 단일모델 후보이며, 바로 최종 선택을 선언할 수는 없다.** 原본 모델은 dynamic canopy, 2D diffusion routing, 4-face sediment, local DLS가 모두 실제로 구현되어 있다. 1ha 미만 초소규모 적용은 원본 배열 상한상 허용되나 **학술적 검증 규모 및 numerical correctness/0.5m 안정성은 미확인**. 굵은 수치 해상도로만 이뤄진 Cobres native 예제 결과를 그 증거로 재사용하면 안 된다.

### 판정 우선순위 (새 결합물리 개발 금지, 기존 SHETRAN 내부 검증만)
1. 소규모 2D 원본 그대로 테스트: DEM 상 인접 2종 NVC(참나무 맹아, 억새), 동일 수관 외 soil/FCG/rock/roughness, 주어진 단일 강우. 가상구성이면 SYNTHETIC 명시.
2. ET에서 canopy `CSTCAP` 양수인 두 시나리오, `CLAI/PLAI` 조절에 의한 canopy OFF 구현이 다른 ET/source 항에 영향을 주는지 분리 추적; native input-only canopy-only toggle 검증. 첫 timestep부터 sediment 실제 처리되는지 확인.
3. 첫 timestep 강우, 0mm/h, 10–50mm/h + 강우 종료 후 `CSTORE/PNETTO/DRAINA`와 물수지.
4. `s_v_er`를 coarse HDF5에서 적산하지 말고 내부 `GNU×DTUZ` 정확값과 `DLS`, `FBETA`, `FDEL`, 경계 입경별 유사량을 독립 감사; 첫 출력 초기상태/마지막 종료시각 오류 통제.
5. 지형과 LAI NVC map의 0.25/0.5/1m(실측 및 연산여건 따라 조정) x-y 해상도 민감도 + 물/유사수지 통과. 국지 E(x,y), D(x,y), `∆z(x,y)`, ON−OFF 차분을 함께 확인.
6. 매 격자 사용가능한 초기 H를 초과한 원토양 박리가 발생했는지 반드시 확인. 원본이 이 제한을 자체 해결한다고 선전하지 않는다.
7. 마지막에만 mixed vegetation real-site data 적용 및 현장 관측과 정량 비교. 누락된 실제 현장데이터가 있다면 결과는 설계/가상 민감도로 표시.

### 출처 (코드 원형)
- [SHETRAN ETmod.f90](https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/evapotranspiration/ETmod.f90).
- [SHETRAN SYmod.f90](https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/sediment/SYmod.f90).
- [SHETRAN OCmod2.f90](https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/overland_channel/OCmod2.f90).
- [SHETRAN sglobal.f90](https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/core/sglobal.f90).
- [EUROSEM eurseml.for](https://github.com/TheSoilman/EUROSEM/blob/8652944da6e1e8436495aa0c08765e2399830dd7/eurseml.for).
- [EUROSEM eplanel.for](https://github.com/TheSoilman/EUROSEM/blob/8652944da6e1e8436495aa0c08765e2399830dd7/eplanel.for).
- [EUROSEM eusedl.for](https://github.com/TheSoilman/EUROSEM/blob/8652944da6e1e8436495aa0c08765e2399830dd7/eusedl.for).
- [EUROSEM test.par](https://github.com/TheSoilman/EUROSEM/blob/8652944da6e1e8436495aa0c08765e2399830dd7/test.par).
