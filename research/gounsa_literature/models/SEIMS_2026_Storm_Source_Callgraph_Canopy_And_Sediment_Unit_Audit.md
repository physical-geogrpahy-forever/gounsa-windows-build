# SEIMS vdev 원본 폭풍사상 코드 심층감사: 빌드/강우수관차단/박리·퇴적 실제 실행 연결 및 수송능 단위

검증일: 2026-10-27. **OpenLISEM 관련 Work와 별도로** `lreis2415/SEIMS`의 개발 브랜치 **`dev` 실제 C++ 소스와 api/CMake 타깃**을 GitHub API로 직접 판독. 원논문 Zhu et al. (2019), *Environmental Modelling & Software 122*, 104526 DOI https://doi.org/10.1016/j.envsoft.2019.104526. 프레임워크를 논문이 공개했어도 해당 dev HEAD가 2019 논문 바이너리와 같다는 증거는 아님.

## 1. 소스 blob, 컴파일 엔트리의 실재
| 코드파일 (`seims/src/seims_main/modules/` 이하) | Git blob SHA | 호출/검증 내용 |
|---|---|---|
| `erosion/CMakeLists.txt` | 968b306f551f04e727eaf1e2176a528277b0fd2d | `SPLASHERO_PARK`와 `KinWavSed_OL` 둘 다 `ADD_SUBDIRECTORY`; 각각 shared library CMake 존재 |
| `erosion/SPLASHERO_PARK/SplashEro_Park.cpp` | 91e81a03929153d7534ce6198354208c1928b70f | rain splash 실제 `Execute()` |
| `erosion/SPLASHERO_PARK/api.cpp` | a2baf7a45b3b0a993cc491333efdc1b346d29420 | `VAR_NEPR` (순강우 mm) 입력, `VAR_DETSPLASH` (kg) 출력, interception/overland dependency; `D_LeafDrain` 입력은 **주석** |
| `erosion/KinWavSed_OL/KinWavSed_OL.cpp` | 64e47107bf52a4814a0cfd41615a93cdac99a53c | 실제 유수박리, 수송능, 퇴적, route |
| `erosion/KinWavSed_OL/api.cpp` | 4c8b47bc1e163a9a6ce1e013f8e1ab04cb0c6056 | `D_DETSplash` (kg), `D_QOverland` (m3/s), `FLOWIN_INDEX`, `ROUTING_LAYERS` 분명한 연결 |
| `hydrology/PI_SVSC/Interception_SVSC.cpp` | cae0ac97a60e216f26089f65b8ff49e206f5496b | 수관저장 `m_st`, seasonal max capacity, `NEPR` 출력, explicit LAI 없음 |
| `hydrology/PI_MCS/Interception_MCS.cpp` | e8b4baabd34f3f94e65590d3e8d776b2f4daa0d0 | seasonal canopy storage, storm-mode 잘못된 식별자 다수 |
| `hydrology/PI_MCS/Interception_MCS.h` | 84a6b3dfc9150062cc86f168a72ab52243fe94b8 | `m_pcp` 멤버는 있으나 `m_P` 없음 |
| `hydrology/PI_SVSC/api.cpp` | 6ebb38b1daf03bb9cbfff20a1fb52ea97397dbf3 | `INTERC_MIN/MAX`, seasonal capacity exponent 사용, canopy drain/LAI 입력 없음 |

현재 원본의 빌드 타깃은 CMake에 모두 등록돼 있으므로 '이 두 침식 모듈이 소스에만 있고 아예 빌드에서 빠졌다'는 해석은 잘못. 그러나 **CMake 타깃 존재 ≠ 사용자 정의 config에서 두 모듈을 동일하게 선택 및 native 전체 실행 성공**.

## 2. 성공적으로 연결된 부분: 강우박리 → 유수박리 + 퇴적
- `SplashEro_Park.cpp:166–191`: `RainInten=NEPR*3600/timestep` [mm/h], water shield `Fw`, rain detachment `Dr=Omega*Fw*USLE_C*USLE_K*(RainInten)^2*(2.96*S0^0.79+0.56)` [코드 주석 kg/(m²·min)]; `DETSplash=Dr*(dt/60)*slope_area` [kg/cell].
- `SPLASHERO_PARK/api.cpp:37–41`: storm precipitation input **`VAR_NEPR` from an interception module**, output `VAR_DETSPLASH`; potential canopy storage reduces net precip, but **leaf-drip impact physics has no separate active input**. Explicit commented `D_LeafDrain` source metadata line60.
- `KinWavSed_OL/api.cpp:40–48`: `FLOWIN_INDEX` & `ROUTING_LAYERS` source inputs; `D_DETSplash` and `D_QOverland` module inputs.
- `KinWavSed_OL.cpp:318–341`: `Dsp=m_DETSplash`; `Df=m_DETOverland` computed by `CalcuFlowDetachment`; `m_Sed_kg+=(Df+Dsp)`, `Dep=max(concentration-TC,0)`, `m_SedDep=Dep*Vol`. **This proves rain+runoff source, sediment availability and local deposition numerical formula are native.**
- `KinWavSed_OL.cpp:488–509`: `Sin=Σ m_Qsn[flowInID]`, `Qin=Σ m_Qkin[flowInID]`, where `flowInID` enumerated by `m_flowInIndex[id]`; advection is **upstream neighbor indices, one-dimensional kinematic routing-network**, not full conservative, arbitrary signed four-face XY 2D SWE sediment.
- `KinWavSed_OL.cpp:395–402`: water volume `m_WH/1000` confirms `m_WH` in **mm** and volume m³. `CalcuVelocityOverlandFlow:263–279` Manning hydraulic radius `m_WH/1000`, so `m_V` is **m/s**.

## 3. 원본 수송능 계산의 단위 불일치 의심점: 매우 높은 우선순위
`KinWavSed_OL.cpp:297–315`:
```cpp
q = m_V[id] * m_WH[id] * 60.f; // comment: m2/s -> m2/min
const float threshold = 0.046f;
if (q < threshold) Ctrans = eco1 * K * S0 * sqrt(q);
else               Ctrans = eco2 * K * S0 * q*q;
Ctrans /= q; // kg/m3
```
하지만 같은 소스 `WaterVolumeCalc`·`CalcuVelocityOverlandFlow`은 **`m_WH`를 mm로 저장**하고 `/1000` 적용하므로 `q`를 [m²/min]으로 계산하려면 **`m_V * (m_WH/1000) * 60`**을 써야 한다. 현재 코드의 `q` 숫자값은 의도한 m²/min q보다 **1000배** 크다. `0.046` 분기와 수송능 `q²` 및 `q^{1/2}` 적용 구간을 바꾸므로 단순 표기 오류가 아니다. 원저자 의도한 `eco1,eco2,K`의 보정 단위가 어디까지 이 오류를 상쇄하는지는 논문 실행판과 관측값을 검토해야 한다.

**독립 C++ 수치 재현 검증 실시** (original source expression isolated, full SEIMS binary run 아님):
`m_V=0.1m/s`, `m_WH=5mm`, `slope=0.2`, `K=0.3`, `eco1=eco2=1`인 **예시 테스트 매개변수**에서
- raw original code (q=30), SI-converted intended (q=0.03) (1000배).
- original q chooses `HIGH q²`, corrected q chooses `LOW √q`;
- q로 나눈 계산된 `TC`: original **1.76504521624**, depth-converted **0.339683110243**, 약 **5.196배** 차이. 이 TC 차이는 선택 매개변수의 **격리 계산 예시**이며 고운사/실험현장 예측비 또는 최종 소스 오류 효과의 보편적 배수가 아니다.
- Independent harness G++ 17/Wall clean compiled, no SEIMS full package build. Files saved as `research/gounsa_literature/code_audits/SEIMS_TransportCapacity_UnitProbe.cpp` and `SEIMS_TransportCapacity_UnitProbe_Output.txt`.

## 4. 수관차단과 적하의 실제 입출력
- `PI_SVSC::Execute` lines 96–144: `capacity=min+(max−min)*f(dayOfYear)`, `available=capacity−stored`, `NEPR=P−loss`. Rainfall amount units mm; `LAI` input absent. Evaporation only non-storm mode. No leaf-drip kinetic-energy distribution, no Rutter exponential water drainage in active source.
- `PI_MCS::Execute` likewise monthly sine `MIN/MAX` seasonal capacity and `NEPR` output; no dynamic LAI/canopy leafdrip calculation in code. It is a separate optional interception module, not required to use both.
- **New storm-specific source issues in `PI_MCS`**: header declares `m_pcp` (line79) but not `m_P`; `Interception_MCS.cpp:132` `m_P[i]=m_P[i]*...` inside `#ifdef STORM_MODE`, **undeclared m_P**. Both `SetValue` branches lines 64 and75 under `#ifdef STORM_MODE` assign `m_hilldt=data`, but those functions' arguments are named **`value`**, not `data`. These are source-level **compiler diagnostics expected if PI_MCS compiled with STORM_MODE**, not an observed whole package build failure. `PI_SVSC` exists as different optional module, so **SEIMS entirely noncompilable** is NOT supported.
- Separate nonstorm `PI_MCS::Execute` line173 `m_IntcpET[i]=m_canSto[i]` appears to override earlier `min(PET,storage)` L167–172, but this is outside the user's short-storm mode and not native-executed to verify; mention as separate potential code issue, not core verdict.

## 5. Physically unavailable requirements and explicit limitations
- No **LAI computed inside rainfall-impact→drip kinetic energy** path; user needs LAI→water storage/drainage→soil incoming rainfall direct and leafdrip KE separation. Source model currently computes some interception from seasonal capacity maps, passes through net precipitation but **uses USLE-C** to represent vegetation effect on splash and overland detachment.
- Full free signed independent XY SWE flux absent in tested kinematic sediment module. `CASC2D_OF` as separate hydro module cannot magically replace `FLOWIN_INDEX` sediment path without new coupling. Module combinability ≠ published fully 2D native original.
- No original 5–10cm verified storm+canopy+sediment published run in 2019 article, no native field model comparison for Miscanthus/oak. Exact source used by published 2019 paper may differ from current dev.
- Physical soil-stock and evolving `DEM` not explicitly present in inspected `CalcuFlowDetachment` / sediment routing. `m_SedDep` formula is sediment retained within a cell, not verified time-integrated elevation `Δz` output.
- Isolated C++ comparison is NOT native full-model water/sediment mass closure, no full SEIMS build, no native 10cm simulation.

## 엄격 판정
**SOURCE+EROSION CALLGRAPH PASS**, **rain + flow detachment link PASS**, **deposition formula PASS**; **LAI→throughfall/leafdrip impact FAIL**, **fully bidirectional 2D sediment FAIL**, **published 5–10cm FAIL**, **transport capacity SI consistency serious source-level issue**. Under user's high-resolution single-model constraints **SEIMS rejected as operational main engine**. Do not present this as solution despite code accessibility; save scientific code concerns for reference.

## Upstream evidence
- https://github.com/lreis2415/SEIMS/blob/dev/seims/src/seims_main/modules/erosion/SPLASHERO_PARK/api.cpp
- https://github.com/lreis2415/SEIMS/blob/dev/seims/src/seims_main/modules/erosion/KinWavSed_OL/KinWavSed_OL.cpp
- https://github.com/lreis2415/SEIMS/blob/dev/seims/src/seims_main/modules/erosion/KinWavSed_OL/api.cpp
- https://github.com/lreis2415/SEIMS/blob/dev/seims/src/seims_main/modules/hydrology/PI_MCS/Interception_MCS.cpp
- https://github.com/lreis2415/SEIMS/blob/dev/seims/src/seims_main/modules/hydrology/PI_SVSC/Interception_SVSC.cpp
- https://doi.org/10.1016/j.envsoft.2019.104526
