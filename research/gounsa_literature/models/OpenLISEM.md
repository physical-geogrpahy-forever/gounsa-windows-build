# OpenLISEM lineage

## 핵심 문헌
- Wu et al. (2021), Catena 207, 105658, DOI 10.1016/j.catena.2021.105658
- Wu, Baartman & Nunes (2021), Catena 207, 105620, DOI 10.1016/j.catena.2021.105620
- current OpenLISEM source code inspected in this chat

## 고운사에서 검토한 이유
2D/spatial hydrology + erosion + sediment transport를 산불 산림 유역에서 실제 적용한 모델 중 root cohesion까지 받을 수 있는 후보인지 확인했다.

## 공간구조
- spatially distributed
- current code includes 2D SWE/flood-flow paths
- runoff, sediment transport and erosion modules
- burned Mediterranean catchment application exists

## vegetation/root implementation confirmed from source code
Input maps include:
- `coh.map`: soil cohesion
- `cohadd.map`: extra cohesion by e.g. plant roots
- vegetation cover
- litter cover
- LAI
- plant height

Current initialization includes approximately:
```
CohesionSoil = COHCalibration * (Cohesion + Cover * RootCohesion)
```

Then detachment efficiency `Y` is calculated from cohesion.

## interpretation
Root cohesion can be supplied spatially, but:
- it is an external map
- it is weighted by vegetation cover
- the model itself does not dynamically derive root cohesion from root biomass/RLD

Therefore it does not satisfy the strict “quantitative vegetation state directly calculated by model” requirement.

## 산불 적용
2021 Part 1/2:
- burned Mediterranean forest catchment
- 18.5 km2
- pre/postfire runoff and sediment response
- event and return-period analysis

## 고운사에 쓸 수 있는 부분
- 2D/spatial burned-catchment modeling precedent
- root-cohesion input architecture
- splash/flow erosion and sediment transport

## 새로운 coupling
LPJ-GUESS FineRootC/RLD -> root cohesion map is **새로운 coupling** unless an independent published conversion equation is used and cited.

## 최종 판정
**보조 2D/postfire lineage.**
Strict quantitative vegetation coupling fails in current implementation.

## 2026-10-26 공개 ORIGINAL source 확인에 따른 판정 수정
앞에서 '보조'로 내렸던 점수는 원본 소스 내부의 생태수문 과정에 대한 평가가 부족했다. 이번 점검에서는 **실제 동일 공개 소스의 원래 구현 코드**를 다음과 같이 직접 확인했다.
- official GPLv3 source `vjetten/openlisem`, `main_C`, `hydro/lisInterception.cpp::cell_Interception`: `Cv=Cover`, `Smax=CanopyStorage`, `canopen=1-exp(-0.45*LAI)`, `CS=Smax*(1-exp(-canopen*RainCumInt/Smax))`, `RainNet = Cv*LeafDrain + (1-Cv)*Rainc`; separate litter cover + water storage. **No unimplemented SWEHR Rutter assumption.** This is the implemented specific original openLISEM interception method.
- `erosion/lisErosionSplash.cpp::SplashDetachment`: `directrain=(1-Lc)*(1-Cv)*Rainc*1000`, `throughfall=(1-Lc)*Cv*LeafDrain*1000`, `KE_LD=max(15.3*sqrt(PlantHeight)-5.87,0)`, direct and leaf drip separate KE terms. Splash detachment scaled by `(1-StoneFraction)` and optionally `(1-GrassFraction)`; in dynamic 2D pushes sediment into `SSFlood`.
- `erosion/lisSWOF2DSediment.cpp::SWOFSediment` uses actual 2D SWOF/SWE sediment advection and detachment/deposition, multiple sediment components; `erosion/lisErosion.cpp` provides flow detachment including stone/grass.
- Sources complete and available with GPLv3. **BUT** the user had previous Qt6/QWT repository inaccessible failures in Linux and native Windows installed 7.5.2 downloaded setup; no rebuilt exact current source/exe version proof and no complete original runoff/sediment mass QA here. Do not pretend this source was successfully compiled, and do not equate 7.5.2 Windows setup with present GitHub main_C source commit without hash/build provenance.
- Still missing per-stem SF spatial localization and dynamic root RLD from cohort; rock surface protection exists but no fire spall weathering/fragment transport physics. Root cohesion external map and cover-weighting cannot become automatic RLD dynamics.
- **Amended assessment:** candidate for the entire published, physically separate canopy+leafdrip+2D erosion package from truly open original source. Major practicality obstacle = dependency/build environment and exact release identification, not missing original canopy erosion source.
- Decision: [strict source-based model audit](../decisions/2026-10-26_FULL_OPEN_SOURCE_NATIVE_2D_VEGETATION_EROSION_MODELS.md).

## 2026-10-26 신규 급경사지 OpenLISEM 실증 선례 및 원본 소스 SHA

- **Opedes et al. (2025)**, *Earth Surface Processes and Landforms*, 50(6), e70074, DOI: https://doi.org/10.1002/esp.70074. Ugandan Mount Elgon Ukha subcatchment 44.5 km², grid 12.5m, dynamic-wave 2D solver, calculation dt 15s. 조사된 도랑 중 82%의 설치지가 10–30° 경사이며 이는 유역 전체 경사 분포가 아님. LAI, canopy height, cover, litter, root extra cohesion, stone input 사용. Discharge calibration NSE 0.72 and KGE 0.61, **sediment observation/independent erosion validation unavailable**. 실측 토사 검증 성공으로 서술 금지. See `../papers/2025_Opedes_OpenLISEM_MountElgon_Trenches.md`.
- OpenLISEM official `vjetten/openlisem`, `main_C` investigated at SHA **`d894c72428947247ce49eb88353dadf49b3123e8`**. `hydro/lisInterception.cpp::cell_Interception`: `canopen=1-exp(-0.45*LAI)`, `CS=Smax*(1-exp(-canopen*RainCumInt/Smax))`, `RainNet=Cv*LeafDrain+(1-Cv)*Rainc`. `model/lisDataInit.cpp`: storage equations `0.2856 LAI` and `0.59 LAI^0.88` among multiple LAI equations, with optional user-supplied `smax` map; calibration not validated for Gounsa young oak/Miscanthus. `erosion/lisErosionSplash.cpp`: direct rainfall vs leaf drainage separate splash energy; `erosion/lisSWOF2DSediment.cpp`: 2D runoff-driven detachment and sediment advection/deposition; `flow/lisOverlandflow.cpp`: FullSWOF2D MUSCL with DEM.
- **Source negative result:** `StemflowFraction` exists in header but its `lisDataInit.cpp` read and UI mapping are commented out; native per-stem SF unverified, not a mandatory first-order filter here.
- **Source caveat:** Built-in event-wise erosion-induced DEM change not demonstrated. Surface spall weathering/fragmentation and cohort root biomass→root cohesion are not native automatic processes. Newly implemented links MUST be labeled new coupling.
- **Operational caveat:** 2026 Windows 7.5.2 installer and main_C SHA source equivalence has not been proven; no native binary run, independent 2D water/sediment balance nor Gounsa validation performed in this check. Do not claim Qt6/QWT Linux failures have been fixed.
- **Revised rank:** Strong native-source candidate for the three current priorities (LAI interception/throughfall/drip, explicit runoff detachment, published steep 2D catchment usage), **not selected as finally validated Gounsa engine** and **does not satisfy previous stricter native dynamic RLD coupling condition**. See `../decisions/2026-10-26_OPENLISEM_THREE_CRITERIA_SOURCE_AND_STEEP_SLOPE_AUDIT.md`.

## 2026-10-26 이전 7.5.2 전체모델 실행 실패 이력 재복구 — 운영 판정 보류 (중요)

과거 2026-10-23 Windows-2022 GitHub Actions에서 개발진 원본 OpenLISEM 7.5.2 `lisem.exe -ni -f -r` **실제로 원본 전체 실행 성공** (SHA256 `f8a5722ed0b370f32fb3dae5c55465427abe75b1155b50bf12aa5516d6b4ca79`). 단 100x100m 가상사면 운동파에서 dt 0.25→10s를 바꾸자 참나무 runoff 14.051→14.020mm로 거의 동일한데 sediment export 19.714→853.798kg/ha로 >43배 증가. 2D native dt 5/10/20s의 출력도 비수렴하고 oak dt=10s 단일격자 최대 순침식 200566.703t/ha, 토사깊이 환산 14.86m(가상 수문토심 0.25m). 100µm 원본 GetSV 침전속도 1.272262m/s는 99.9µm 0.008975m/s 대비 141.8배 불연속, 표준 SI Zanke 약 0.00779m/s와 큰 차이. `SedimentSSContinuous`의 `DetachMaterial` 및 SS 농도상한 처리 주석, SwitchUseMaterialDepth false로 유한 토층 제한 없음. 2026-10-25 통제실험서 설정 생성 잘못(Advanced Options OFF), GUI vs engine settling-velocity 키 불일치, 공식예제 다운로드 실패 및 경계 배출 0 등 확인. 이는 Qt6/QWT Linux 종속성 설치와 **별개인 물리 및 수치 심각 문제**.

따라서 **원본 소스에 LAI canopy/drip 2D flow가 있다는 이유만으로 엔진 원본 7.5.2을 재추천하지 않는다**. 새 산지 논문 Opedes 2025는 실제 적용 선례이나 과거 7.5.2 가상 고운사 수렴 불합격을 무효화하지 않는다. **원본 = 보류**, 원본 수정 포크는 정확한 수정 선언 및 native numerical regression 검증 후 별도 판정. 상세 [결정](../decisions/2026-10-26_OPENLISEM_752_PREVIOUS_NUMERICAL_FAILURE_RECOVERY.md).

## 2026-10-26 Windows 원본 2D 신규 12회 시험 결과: NO-GO

이전 2026-10-23 원본 결과를 인용만 한 것이 아니라 공식 OpenLISEM 7.5.2 Windows 바이너리를 이용해 5m 해상도 1ha 가상 사면에서 실제 12개 2D 전체 계산을 다시 실행했다. Advanced Options=1, 2D 유역경계 개방, 총강우 20mm, 원본 개발진 기본 SettlingVelocity=1과 대체 SettlingVelocity=3을 식생별 시간간격 5/10/20초에 교차 적용했다. 모든 실행 정상 종료, 경계 물 배출 >0, 원본 출력의 물/유사수지는 폐합. **유사유출량 시간간격 수렴 실패**: Oak 기본식 0.005993→123.037727→832.588686kg/ha, 원본 대체식도 0.030954→28.707586→268.530307kg/ha. Miscanthus 원본 대체식 0.018893→0.044177→88.121322kg/ha. Oak 기본식 20초 최대 한 격자 순침식 5982.9t/ha > 초기 25cm 가상토심 질량 3375t/ha. **원본 7.5.2 고운사 유수침식 엔진 채택 최종 NO-GO**, 수정 포크는 원본 통과로 보지 않는다. 자세한 실험 원자료, runfile/시나리오, 12개 원본 totals.csv 및 soilloss.map [검증 보고](../decisions/2026-10-26_OPENLISEM_752_NATIVE_2D_STABILITY_FAILED.md), [Actions run 40304135775](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40304135775). 기존 기능 선례로 이 판정을 되돌리지 않는다.


## 2026-10-27 신규 5cm 및 1cm 공개 학술 선례 확인과 7.5.2 구분
- **Maggioli et al. (2022)** https://doi.org/10.3389/fevo.2022.765148 : TLS 기반 5cm DEM·식생 높이/피복→LAI 추정→수관저류량 입력, 스페인 375m² 건조사면, LISEM 5cm 격자와 1초 시간간격, 18개 강우사상의 침투·지표유출·침식. 공간 routing은 논문상 **kinematic-wave**. 5cm 격자별 침식/퇴적 DoD 관측과 검증은 입증 안 됨. 정확한 LISEM 실행버전 식별 안 됨.
- **Epple et al. (2025)** https://doi.org/10.1002/esp.70127 : 실제 LISEM 1cm 격자에서 rain-simulator 실험포 수문·침식, 시간별 DEM 지형고도 갱신, 비디오 기반 PTV 유속/SfM DoD와 비교. 논문에는 LAI 수관저류를 이 1cm 시나리오에서 활성화했다는 증거가 없음. 정확 코드 태그도 없음.
- **Naranjo et al. (2021)** https://doi.org/10.5194/hess-25-5561-2021 : OpenLISEM v4.96에서 격자별 유사배출 이상치(4m 440.9Mg vs 2m 128.4Mg 등) 학술 지적.
- **판정 변경:** 초고해상도+수관저류+침식 논문이 아예 없다는 과거 선별 결론은 **명시적으로 철회**한다. 그러나 선행연구의 LISEM 버전이 v7.5.2와 같은 원본인지 미확인이며 Gounsa 7.5.2 native 유사수송 수치 QA 탈락은 그대로 유지. 새로운 코드 재채택은 소스-원문 동일성/강우시간간격 및 침식 수렴/전방위 2D 확인을 전제로만 한다. 문헌 [정정 기록](../decisions/2026-10-27_SUB10CM_LISEM_NEW_PUBLISHED_EVIDENCE_REVERSAL.md).

## 2026-10-27 핵심 계보 정정
개발진은 **세 가지를 구분**: 1990년대 LISEM original (De Roo 등의 LDD/1D 운동파), Victor Jetten의 **OpenLISEM Classic**(`vjetten/openlisem`, 2026-10에 v7.5.2), Bastian van den Bout의 **신형 LISEM / Lisem Integrated Spatial Earth Modeller**(`bastianvandenbout/LISEM`, 별도 소프트웨어, 알파 버전, 스크립트 및 지형모의). LISEM Hazard는 이 신형 계열의 기원/관련 모델. 공식 https://lisemmodel.com/docs/home/ / https://lisemmodel.com/docs/about/ / https://lisemmodel.com/docs/downloads/.
**Epple et al.(2025)** 1cm 실험 논문은 공식 `https://lisemmodel.com/`을 `LISEM (2024)`로 인용하고 Bastian van den Bout에게 연구지원 감사, LISEM scripting 사용을 명시하여 신형 계열로 강하게 판정. 동일 소스태그는 미확인. 따라서 **Gounsa OpenLISEM Classic 7.5.2 수치 불안정성 검증은 신형 LISEM에 대한 검증이 전혀 아니다.**
**Maggioli et al.(2022)** 5cm + LAI 수관저류 + erosion은 원 LISEM과 Jetten/De Roo 2001을 인용하고 운동파 사용을 명시하여 Classic 계열 적용 논문으로 추정. v7.5.2 적용 단정 불가.
공식 신형 LISEM hydrology https://lisemmodel.com/docs/hydrology/ 의 입력은 `vegetation cover`, `vegetation height`, `SMax Canopy`, LAI, 예를 들어 `Smax Broadleaved Forest=0.2856 LAI`, `Smax Clumped Grass=0.59 LAI^0.88`. **식생 및 수관저류가 새로운 LISEM 계열에도 명시적으로 존재**하는 독립 개발자 근거. 다만 1cm Epple 시나리오에서 interception을 활성화한 것은 아님.

## 2026-10-27 원본 태그/브랜치 재감사 및 네이티브 판정 재확인
- 상세 [감사 결정문](../decisions/2026-10-27_OPENLISEM_752_SOURCE_NATIVE_REAUDIT_NO_GO.md) 및 2026-10-26 Windows [원본 NO-GO](../decisions/2026-10-26_OPENLISEM_752_NATIVE_2D_STABILITY_FAILED.md)를 참조.
- `v7.5.2`와 `main_C` 직접 blob 비교에서 `lisErosionAux.cpp`, `lisSWOF2DSediment.cpp`, `lisInterception.cpp`, `lisErosionSplash.cpp`, `lisBoundary.cpp` 동일. `lisSWOF2DopenMUSCL.cpp`은 다르지만 태그와 동일 핵심 유사/침전속도 코드를 사용하는 main_C를 미시험 상태에서 수정판으로 추천하지 말 것.
- 실제 active 2D path는 `OverlandFlow2Ddyn -> fullSWOF2openMUSCL -> SWOFSediment -> SedimentSSContinuous -> SWOFSedimentAdvection -> Boundary2Ddyn`. `fullSWOF2open()`은 obsolete.
- 소스에 실제 LAI canopy storage/drain, direct/leaf drip splash, full 2D SWE 및 flow erosion/deposition이 있지만 **Windows 원본 2D native 12회 외부 dt 민감도(유사배출 수백~수천배)와 국지 유한토사재고 비현실성으로 NO-GO**. 전역수지 닫힘은 문제 해결이 아님.
- 1/2초 및 2m 추가 native Actions는 timeout으로 수치결과 미확보; cm격자 genuine2D 침식 검증 없음. 해당 모델을 다시 선행논문 5cm를 근거로 재채택하지 말 것.
