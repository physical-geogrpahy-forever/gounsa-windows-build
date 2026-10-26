# SHETRAN: full source-level vegetation canopy, splash, flow erosion inspection (2026-10-26)

## Identity and archival provenance
- Source: https://github.com/nclwater/Shetran , default master, licensed GPL-3.0. Current inspected project `CMakeLists.txt` declares SHETRAN 4.7.2.0. Unlike `nclwater/Shetran-public` (binary/executable archive ONLY), `nclwater/Shetran` contains full Fortran `src/`, build rules, example datasets and documentation.
- Original source is **actually publicly available**, not hypothetical code constructed from a paper. No code modifications were made; no compiled native SHETRAN test was performed in this task.
- Original line evidence as inspected on 2026-10-26:
  - `src/evapotranspiration/ETmod.f90`, stored canopy CSTORE, `CSTCAP` [mm], exponential drainage via `CK` [mm/s], `CB` [1/mm], updated inside `ET` L450–529, per-vegetation LAI/cover and canopy state, and `DRAINA` [m/s] returned by `ETIN` L817. Rutter-type dynamic canopy water balance **present in original code**.
  - `src/sediment/SYmod.f90` `SYWAT` L4413–4499 computes canopy sheltered fraction `FCC = PLAI*min(CLAI,1)`, distinguishes canopy drip `DRAINA` and direct rain `LRAIN`, and raindrop effective diameter `DRDROP`.
  - `SYOVER` L3658–3806: ground erosion original published, both `DR` rainsplash and `DF` flow-driven, independent canopy drip fall height `XDRIP` [m], drop size `DRDRIP` [m], drip fraction `FDRIP`, ground-cover `FCG`, non-erodible rock fraction `FCROCK`, ponding-depth damping, critical bed shear stress `SYCRIT`, loose layer protection `DLS>=DLSMAX`.
  - In detail `DR=GKR*exp(-max(0,DWAT1/DRDROP-1))*(1-FCG-FCROCK)*(GMR+GMD)`, where `GMR=(1-FCC)*a*LRAIN**b`, `GMD=TGMD*DRAINA`, `TGMD=πρw²g/6*c*(1-exp(-2XDRIP/c))*DRDRIP³*FDRIP`. `DF=GKF*(1-FCROCK)*max(0,τ-τc)/τc` (source L3685–3700 and executable statements 3766–3803). SHETRAN has an ACTUAL original leaf-drip momentum separate from direct rain, which SWEHR 2017 public C does not.
  - multi particle sediment sizes up to `NSEDEE=7` originally at `src/core/sglobal.f90`. Sediment source/transport functions `SYCOLM`, `SYLINK`, channel bed `SYBED` and fine fraction `SYFINE`.
  - Hillslope runoff is spatial finite-difference 2D-grid connected by 4 faces `QOC(IEL,FACE)`, with 3D subsurface; not a simple 1D D8-only erosion route. However **rill-scale self-incision is not explicitly solved**: original Wicks & Bathurst (1996) SHESED abstract explicitly says 'sheet overland flow (without rilling)'. Automatically emerging rills therefore must NOT be claimed.
  - **Independent sediment mass balance is NOT turnkey in released source:** `src/sediment/SYmod.f90` L4668 `SUBROUTINE BALSED; end subroutine BALSED`; top comments say placeholder. Native sediment mass QA must be implemented only as an explicitly labelled source auditing/diagnostic layer; current original original isn't independently proven mass-conserved in this chat.
- Original ready-to-read sediment-enabled examples:
  - `examples/Cobres/model/rundata_cob.txt` explicitly lists `17: sediment yield input → input_cob_syd.txt`.
  - `examples/Cobres/model/input_cob_syd.txt`: `SY24 XDRIP, DRDRIP, FDRIP` values 3.0m, .005m, .5 (single generic veg example only), `SY41 FCG`, `SY42 FCROCK`, seven size classes.
  - `examples/Aire_at_Kildwick_Bridge-AllOptions-withdates/model/input_Aire_at_Kildwick_Bridge_syd.txt` also present and called in rundata; example is NOT evidence that site Gounsa vegetation model calibrated.
- Build: `COMPILING.md` includes Linux gfortran, Intel ifx, Windows ifx+Visual Studio, CMake, external HDF5 1.14.6, zlib-ng, Fortran stdlib 0.8.1, fypp. No claim of successful present model build. The local Linux environment here lacks network DNS for git clone; compiling such large source requires downloading tarballs; an executable and original examples may be used independently if available. No fabricated Linux success.

## Rutter/interception
Original model uses Rutter-type canopy storage and exponential drainage. Unlike McGuire SWEHR (2016) incomplete public C, this **source contains real `CSTORE`, `CK`, `CB`, `DRAIN`, `DRAINA`** calls. Evidence `ETmod.f90`, not just article. Check mathematical balance from implementation before quantitative simulation.
## Strongest vegetation-erosion mechanism
Leaf drip kinetic/momentum physics in `SYOVER` uses separate fall height and drop diameter; direct impact uses raindrop rainfall; ground-cover and rock-cover shield erosion separately. This is precisely the core that Gounsa needs before root/litter and per-plant stemflow. Distinguish canopy cover fraction `FCC` from close-to-ground protective cover `FCG`. Original can represent sparse oak sprouts vs dense Miscanthus via **mapped vegetation/cover and differing plant parameter records**, not dynamic RLD / per-stem spatial SF.

## Gounsa explicit limitations
- rill formation (automatic concentrated flow incision): not independently present in original hillslope SHESED; model 2D sheet flow not equivalent to a dedicated evolving rill network.
- individual trunk/tussock SF supply footprint: not confirmed in original `ETmod/SYmod`; do not claim yes.
- dynamic root length density/break strength linked directly to biomass: not found. GKF/GKR are soil-type coefficients not direct fine-root mass.
- `FCROCK` is non-erodible surface fraction input; not fire spall rock weathering, redistribution or armouring rates.
- long-term soil depth and postfire vegetation coupling separate; no site calibrated output.
- Externally field-measured map/rain data and at least new native example rerun required before acceptance. Sediment BALSED is currently stub.

## References
Wicks & Bathurst 1996, Journal of Hydrology 175:213–238, DOI 10.1016/S0022-1694(96)80012-6 (SHESED physical rain leaf drip flow erosion without rilling).
Ewen, Parkin & O'Connell 2000 J Hydrologic Engineering 5:250–258 DOI 10.1061/(ASCE)1084-0699(2000)5:3(250)
SHETRAN official https://research.ncl.ac.uk/shetran/


## 2026-10-26 GitHub 원본 버전 고정
감사 대상으로 확인한 `nclwater/Shetran` 공개 master HEAD: `cf9cd540add78ad3accbaf62b4199d2032887f6b`. 버전 정보는 CMake `project(SHETRAN VERSION 4.7.2.0)`. 미래 소스 변경이 생겨도 본 조사 결과는 이 commit의 실제 Fortran 원본 함수와 대응해야 한다. 원본 고정 링크: https://github.com/nclwater/Shetran/tree/cf9cd540add78ad3accbaf62b4199d2032887f6b


## 2026-10-26 후속 정밀 코드 추적: 전체 실행 순서와 별도 저감항

[상세 원본 소스 감사](../decisions/2026-10-26_SHETRAN_472_NATIVE_IMPLEMENTATION_CALLGRAPH_AUDIT.md)

원본 SHA `cf9cd540add78ad3accbaf62b4199d2032887f6b`; 모든 아래 함수는 공개 Fortran 4.7.2 원본에 실제 존재함. **수치 결과/원본 예제 실행은 아직 하지 않았음**.

1. `driver/run_sim.f90` L272 `ETSIM` → L276 `VSSIM` → L295 `OCSIM` → L311 `SYMAIN`. `ETmod.f90::ETIN` 는 `CPLAI=PLAI*min(CLAI,1)` 를 계산한다. `ET` 는 수관저류 `CSTORE` [mm], `CSTCAP`[mm], 지수배수 `CK`[mm/s]/`CB`[1/mm]를 이용해 `DRAIN`과 유효강우 `PNET`를 계산. `ETIN`은 `PNETTO=PNET/1000` [m/s]과 `DRAINA=DRAIN/(1000*DTUZ)`[m/s]를 별도 출력.
2. `SYmod.f90::SYWAT` 는 `PNETTO` 및 `DRAINA`를 받아 canopy sheltered fraction `FCC=PLAI*min(CLAI,1)`, `LRAIN=max(PNETTO-DRAINA,0)/(1-FCC)` (FCC<1), raindrop effective `DRDROP`, 4-face water `QOC` 및 대표 수심 `DWAT1`, 전단 `TAUK`를 구함.
3. `SYOVER` 의 실제 강우박리: `DR=GKR*exp(-max(0,h/DRDROP-1))*(1-FCG-FCROCK)*(GMR+GMD)`. 직접우 `GMR=(1-FCC)*AD(i)*LRAIN**BD(i)`, 수관적하 운동량 `GMD=TGMD*DRAINA`, `TGMD`는 `XDRIP,DRDRIP,FDRIP`로 계산. **운동량 기반 충격 계산**이라는 점을 KE 모델과 구별한다.
4. 실제 유수박리 `DF=GKF*(1-FCROCK)*max(0,tau-tau_c)/tau_c`. 매우 중요: **FCG는 DR에만 직접 곱해지고 DF에는 직접 사용되지 않음**, 반면 **FCROCK은 두 박리식을 모두 억제**한다. `GKR/GKF`는 토양종류 입력이지 root biomass/RLD 변수가 아님.
5. 지표 퇴적층 `DLS>=DLSMAX` 일 때 `GNU=0`, 그 외 `GNU=(DR+DF)/RHOSO`. 토사수송 `SYCOLM`은 `GNU` 공급을 입경별 원토양 PSD `SOSDFN` 및 각 격자의 `DLS,FBETA,FDEL` 저장고에 혼합하고 Yalin/Engelund-Hansen 이송능과 `FPCRIT`로 제한해서 4-face `QSED`를 공급하며, `SYLINK/SYBED`는 채널에 사용됨.
6. **지표고도 변화 부재 명확히 확인**: `SYMAIN` 원본 `ZGRUND(NEL)` 는 `INTENT(IN)`; `GNU` 계산이 경사진 사면 DEM을 직접 낮추거나 수리 경계를 갱신하지 않음. Wicks&Bathurst 1996 원문도 `without rilling`. *유사유출 모형*이지 사면 지형발달/rill 성장 모델이 아님. 하도 `ARBDEP` 업데이트와 지표고도 Exner를 혼동 금지.
7. **BALSED 빈 함수** (`SYmod.f90` L4668–69). 기본 `BALWAT` 만 실제 호출. 유사모형 질량보존 정확도는 별도 실시 전 검증 불가.
8. `DRAINA`는 수관 총 배수 흐름이며 개별 참나무 기부 SF/억새 포기 흐름이 아니다. `FCG`는 입력한 지표피복 면적이고 억새 biomass/RLD를 동적 계산하지 않음. `FCROCK`는 고정된 표면 비침식 비율이며 spall 풍화/암편 이송을 계산하지 않음.
9. 원래 `ETmod.f90` L497는 `CT1/CSTCAP` 계산이 0용량 점검보다 먼저 있어 경계값 위험. 눈-수관 분기에서 stale DRAINA/PNETTO 경고가 코드 주석으로 존재; native zero-capacity/rain-cessation edge tests 필요.


## 수리해석 결정적 구분: 2D 공간 유동이나 완전 천수방정식은 아님
`src/overland_channel/OCmod2.f90::OCQGRD` L909–1064의 원본 Strickler 기반 격자면 유량 `Q=CONVM*sqrt(abs(DZ))/sqrt(L)`를 직접 확인. 4방향 인접 격자 수위차를 이용하는 **2D 확산파(Manning–Strickler)** 근사이며 2D 천수방정식 관성항까지 적분하는 해법이 아니다. `OCmod.f90::OCSIM`는 암시적 수위 블록행렬을 푼다. 따라서 고운사 고기복·세류 발달 및 0.5m TLS 지형변화의 직접 예측력이 SWEHR 2D SWE와 동일하다고 주장 불가. 또한 `SYMAIN`의 `ZGRUND INTENT(IN)`은 사면 지표고도 미갱신을 명시한다. [근거](../decisions/2026-10-26_SHETRAN_472_NATIVE_IMPLEMENTATION_CALLGRAPH_AUDIT.md).


## 2026-10-26 사상 간 지표고도 갱신에 관한 정정
**원본 SHETRAN에 사상 내부 Exner/rill 지형갱신이 없다는 것은 강우사상별 지형발달 연구에 사용할 수 없다는 뜻이 아니다.** 고운사에는 event-splitting sequential DEM update가 적절한 첫 구현이다. 원본 sediment output은 `src/visualisation/visualisation_interface_left.f90` 의 `s_v_er` = signed `GNU` *86400*1000 [mm/day], `s_t_dp` = `DLS` *1000 [mm]; `examples/Cobres/model/input_cob_visualisation_plan.txt`에는 원본 기능으로 둘 다 **grid_as_grid** 출력되도록 설정되어 있음. 시나리오 시간별 `s_v_er` 적분으로 원지반 박리 두께 `E_{soil}`를, `s_t_dp`의 사상 전후 차이로 느슨한 표층퇴적물 저장층 변화 `ΔDLS`를 구분한다. 사상 종료 후 `z_{soil,next}=z_{soil,current}-E_{soil}`; 정의 및 밀도변환 검증을 거쳐 물리적 지표고도 `z_{surface,next}=z_{soil,next}+DLS_{end}`를 준비한다. `DLS`는 **이동가능한 느슨한 표면 유사층 깊이**이지, 항상 안정적인 퇴적지형고도를 의미하지 않으므로 정착/공극률/퇴적 정착 조건을 확인할 것. 이전 이벤트의 초기 DLS는 중복 더하지 않는다. 이수송/퇴적입경, 암편과 토심도 새로운 상태로 갱신하고 다음 사건의 SHETRAN DEM에 입력한다. 원래 코드 `ZGRUND INTENT(IN)`은 **한 번의 실행 도중 갱신되지 않음**을 의미할 뿐, 서로 다른 강우사상 사이에 외부 모델이 입력 지형을 갱신하는 것을 금지하지 않는다. 사상별 교환을 하려면 습윤상태 및 지하수, 수관 저장고, 퇴적층 질량의 연결성과 물수지 유사수지를 검증한다. 한 사상 내 rill 형성이 유동을 크게 바꾸는 경우 사상 간 DEM 업데이트만으로는 충분하지 않을 수 있다. 앞서 '미구현'이라는 사실만으로 SHETRAN을 배제한 해석은 철회한다.


## 2026-10-26 사상 간 DEM 갱신의 원본 출력 결함 및 상태변수 감사
[새 결정문: SHETRAN_EVENT_BOUNDARY_DEM_STATE_AUDIT](../decisions/2026-10-26_SHETRAN_EVENT_BOUNDARY_DEM_STATE_AUDIT.md) 에 native `FRRESP` output 44의 `GNUCUM/PREVTM` 초기값과 `SEDSRT` baseline, contaminant `RESNOW=0` 호출 결함, `SY51/52/53` 초기 `DLS/FBETA/FDEL` 입력 및 hotstart 불완전성, 단순 모형 기반 지형 업데이트와 별도 물/유사수지 검증 계획을 기록했다. **원본 실행 검증 아님.**


## 2026-10-26 전 호출경로 재감사
[SHETRAN 4.7.2 전체 호출경로 원본 코드 감사](../decisions/2026-10-26_SHETRAN_472_FULL_PATH_SOURCE_AUDIT.md) 참조. 이전 사상별 DEM 갱신 가능성에 추가 조건: **첫 SYMAIN 호출은 초기화만 수행하여 최초 수문 시간간격의 sediment 계산을 건너뜀**, `DLSMAX` 억제율은 수문 timestep 동안 고정된 `GNU`에 늦게 반영, `VS08` 지반기준층이 DEM 갱신 시 그대로 하강할 위험, 원본 sediment hotstart 불완전, 출력 44 초기화/시간 오류. native 빌드/실행 및 수지검증은 아직 하지 않음.


## 2026-10-26: 원본 native 실행으로 이전 "미구동" 판정 갱신
- [원본 native Cobres 강우사상 검증](../decisions/2026-10-26_SHETRAN_472_NATIVE_COBRES_RAIN_QA.md)은 앞선 정적 코드검토 뒤 추가 수행한 실증 단계다. upstream SHETRAN 원본 Fortran 4.7.2.0을 GNU Fortran Debug로 성공적으로 컴파일하고 실제 입력 복제 사상 0,10,30,50 mm/h(3시간)를 native 실행하였다. 핵심 수치: max s_v_er=0/2.708/105.330/430.591 mm/day. 자세한 수치와 모든 조건은 링크에 기록. 20,40 mm/h native 재검증도 추가 자동화 실행 중(현재 결과 확인 전).
- 원본의 t=0 HDF5 s_t_dp=0 mm는 SY51 초기퇴적층 30 mm가 초기화되기 전 출력되는 현상으로서 30mm 실제 퇴적으로 해석하면 오류. native 외부 bridge는 SY51을 기준으로 해야 한다.
- 사건 종료 시각 FR6 48h를 native 최종 기록이 48.315~48.632h로 초과하였다. 다음 사건을 정확히 시간 연결하려면 timestep end cap 및 수문입력 적산 검증 필요.
- **native Cobres 물리모형 실행 성공과 native 고운사 DEM 피드백, 유사수지 폐합, sediment hotstart는 구분해야 함.**


### 2026-10-26 native 5개 강우강도 시험 최종 확인
- 이전의 20, 40 mm/h '진행 중' 기록을 갱신: [GitHub Actions 40287116566](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40287116566)에서 원본 SHETRAN Fortran 빌드, 건조 기준과 10/20/30/40/50 mm/h(3시간) native 실행, HDF5 분석 모두 **success**.
- 20 mm/h 최대 순간 원토양 박리율 67.259918 mm/day, hourly HDF5 근사 최대 누적 박리 6.769896 mm, 초기 SY51 대비 최대 DLS 증가 5.415897 mm. 40 mm/h: 각각 133.283951 mm/day, 23.506236 mm, 20.078381 mm. 모두 Cobres 2km 예제, 고운사 예측 아님.
- HDF5 근사 순지표고 변화 Δz 범위: 20mm/h [-1.3540,+0.02479] mm(174개 하강/2개 상승), 40mm/h [-4.82008,+4.04589] mm(173개 하강/3개 상승); 물리적 DEM을 native 모형에 재주입한 결과는 아님.
- 40 mm/h 시나리오 FR6 48h 종료시각 초과 51.73분 확인. native 정확 GNU 시간 적산, 유사질량수지, 사상별 sediment-hotstart+토층 및 지형 재입력은 미완료.
- 정밀 수치와 한계: [Native rainfall QA](../decisions/2026-10-26_SHETRAN_472_NATIVE_COBRES_RAIN_QA.md).
