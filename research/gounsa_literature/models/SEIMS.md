# SEIMS 원본 2D 및 침식 소스 감사 — 2026-10-26

## 실체
GPL-3.0, [lreis2415/SEIMS](https://github.com/lreis2415/SEIMS); Zhu et al. (2019) *Environmental Modelling & Software* 122:104526. Native C++ framework, erosion modules and real examples exist, cross-platform.

## 실제 함수
- `modules/erosion/SPLASHERO_PARK/SplashEro_Park.cpp` separate splash detachment, requires canopy **cover fraction** and other factors, not original measured LAI-linked leafdrip source.
- `modules/erosion/KinWavSed_OL/KinWavSed_OL.cpp` passes `m_DETSplash`, executes flow detachment and receives upstream sediment, `GetSedimentInFlow`, `CalcuFlowDetachment`, subsequent sediment routing. This is **kinematic wave network** not native full 2D spatial lateral sediment shallow-water law.
- `modules/hydrology/CASC2D_OF/CASC2D_OF.cpp` includes overland model and `m_flowOutIndex` and downstream routing; cannot infer full 2D coupled sediment solely from CASC2D model label.

## 고운사 기준
Original source YES, separate rain and runoff detachment YES, exact native LAI canopy-storage/leafdrip energetics UNKNOWN/NO evidence; true 2D sediment grid-face conservative flux FAIL native positive proof; steep burned forest observed sediment validation NO. Reject as native main engine before numerical sensitivity tests. Published hydrologic application not false, rather all-native fit fails.

## 참고
[Zhu 2019](../papers/2019_Zhu_Parallelized_SEIMS_Framework.md)


## 2026-10-27 추가 실제 STORM CMake→메타데이터→침식 소스→수송능 단위감사
- **[상세 별도 source audit](SEIMS_2026_Storm_Source_Callgraph_Canopy_And_Sediment_Unit_Audit.md)** 및 [GO/NO-GO 결정](../decisions/2026-10-27_SEIMS_STORM_SOURCE_BUILDTARGET_LAI_AND_TRANSPORT_Q_UNITS_NOGO.md). 실제 `lreis2415/SEIMS` `dev` 소스 코드 직접 열람, 2019 공개 논문 SHA와는 구별. 원본 `SPLASHERO_PARK`와 `KinWavSed_OL`은 모두 CMake `ADD_LIBRARY` 빌드 대상, 소스 메타데이터 `D_DETSplash` output→input, `KinWavSed_OL::GetSedimentInFlow`은 `Dsp+Df`와 수송능초과 `SedDep` 실제 계산 **확인**. 이 부분에 대해서는 '유수/강우박리 코드가 없다'고 하면 틀림.
- 그러나 실제 `SPLASHERO_PARK/api.cpp`은 interception 후 순강우 `NEPR`와 USLE-C로 splash를 산출, `D_LeafDrain` input은 **주석**. `PI_SVSC` 수관저류는 계절적 min/max capacity, **LAI 직접 입력 및 적하 KE 없음**. `KinWavSed_OL`의 `FLOWIN_INDEX`기반 유사수송은 **방향성 upstream network**로 자유 XY 유사 계산이 아님.
- **원본 의심 수치 오류 발견 및 실제 격리 C++ 컴파일 시험**: 같은 `KinWavSed_OL.cpp` `m_WH`는 mm (`WaterVolumeCalc`/Manning R에서 `/1000`)이나 `GetTransportCapacity:299`은 `q=m_V*m_WH*60`이라고 계산하며 m²/min을 주석으로 표기. q 입력은 의도된 m²/min보다 1000배 커질 수 있음. 예시 0.1m/s와5mm에서 q30 대0.03, 임계값0.046에서 고/저 수송능 분기 역전; 격리 테스트 수송능값1.765 대0.340. **실제 SEIMS 전체유사량 오차를 1000배로 주장하지 않음**. 
- `PI_MCS` `STORM_MODE` 전용 부분에 undeclared `m_P`와 `data` 참조가 있어 컴파일 장애 후보. 별도 `PI_SVSC` 있으므로 SEIMS 전체가 컴파일 불가라고 판정하지 않음. **5cm published native 성공선례 없음**. 현행 all-in-one Gounsa 제외 판정 유지.
