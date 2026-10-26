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
