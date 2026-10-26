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
