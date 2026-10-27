# LISEM Integrated Spatial Earth Modeller: 독립 C++/OpenCL 계보의 실제 수관 및 유사 침식 소스 감사

작성일 2026-10-26. **주의: 이 저장소는 OpenLISEM Classic 7.5.2 `vjetten/openlisem`와 다른 프로젝트**. Classic 7.5.2 실제 Windows 수치비수렴을 이 프로젝트에 그대로 전가하지도 않고, 이 프로젝트의 홈페이지 소개만으로 전자는 복구됐다고 주장하지도 않는다.

## 공개 출처
- Source: https://github.com/bastianvandenbout/LISEM/tree/6a5ef17d87bab4227d48673c95c12c61462114dd
- LISEM 0.2.x multi-hazard project; same author's overview https://lisemmodel.com/docs/about/ ; author research https://doi.org/10.5281/zenodo.7414954
- Repo API advertises MIT because root LICENSE begins `MIT License Copyright (c) 2017 Can Güney Aksakalli`, while repository also contains `licence.txt` GNU GPL v3 and developer website says GPLv3. **Whole-software licence must NOT be inferred to be MIT from repository metadata alone.** Treat model as distributed under publisher GPL3 until clarified.
- This inspection did not download/run compiled executable and cannot claim computational stability.

## Actual matching program modules read
- `lisem/model/kernels/model_sediment.cl` explicit rain impact (L348–422), flow detachment/deposition (L424–465), four-neighbor sediment flux (L470–519), original code provided.
- `GetSV` in this file L52–65 has the *parentheses corrected* relative to the v7.5.2 Classic default: `10*(sqrt(1+0.01*1.65*g*dm^3)-1)/dm`, distinct from Classic bug `10*sqrt(1+X-1)/dm`. That does NOT prove native convergent sediment balance, and is not reason to rehabilitate Classic.
- `modelruninit.cpp` L432–446 reads `SMAX Canopy` raster into `SMAX_CANOPY`.
- `model_hydrology.cl::hydrology` ~L289 `store_canopy=SCANOPY`, L302 `Smaxc=SMAX_CANOPY`, but L310 `h=h+store_canopy`, L326 `h=h+rain`, L397 `write_imagef(SCANOPYN,...,0)`. The observed `Smaxc` is read but **is not used** to limit/store rainfall in this hydrology kernel; no canopy water-budget LAI driven interception appears in inspected model hydrology kernel.
- `model_evapotranspiration.cl` L169 `//float LAI = ndvi * 4.0;` **commented out**, L192 `write_imagef(SCANOPYN,...,0)` too. NDVI is not native LAI-linked dynamic canopy store.
- `model_sediment.cl` L381–386 `directrain=(1-vegcover)*rain_m`, `throughfall=vegcover*rain_m`, with `KE_LD` from plant height; this partition does not consume actual canopy drainage or dynamic canopy storage, and relies on `vegcover` rather than LAI. Subtracting interception does not appear in this expression itself. **The model being capable of leaf-drip-like splash does not prove actual throughfall from a working water store.**

## Numerical code concern requiring any future source-level requalification
In `model_sediment.cl` ~L507–510 `qfsout = qfsout +z_x1 < -1000? sflux_x1 : 0` etc. Without parentheses a C-style ternary operator's precedence makes this evaluate a comparison with `qfsout+z_x1`, not `qfsout += (z_x1<-1000 ? sflux_x1 : 0)`. This is a **plausible report-flux bug from source reading**, not an experimentally confirmed water/sediment mass residual. Worth isolating only if the missing canopy test were ever resolved.

## What passes vs fails
- Complete readable erosion/hydrology source in unique GitHub codebase: YES.
- Genuine 2D surface water and 2D XY sediment flux functions: source shows 4-neighbor flux and hydro solvers; exact hydrodynamics full finite-volume consistency not revalidated.
- Native quantitative canopy water storage / LAI→throughfall used in erosion flux: **FAIL native code evidence**: stored canopy inputs ignored/reset in reviewed kernels, `throughfall` in sediment is proportional to `vegcover × rain`.
- Steep mountains case original lineage has Dominica landslide/flood studies; native *this version* observed Gounsa forest splash/sediment not verified.
- Stable timestep erosion transport/finite soil stock: **NOT TESTED**.

## 사용자 원칙 적용 최종 판정
**Discard for Gounsa complete native integrated engine** before time-expensive OpenCL build. This is due to missing *active* LAI canopy storage/throughfall/leaf drip link, not due to Classic 7.5.2 benchmark contamination. Scientific hydrodynamics / soil transport components can be cited only with these caveats. Never present as tested stable.

## Sources
https://github.com/bastianvandenbout/LISEM
https://lisemmodel.com/docs/about/
https://doi.org/10.5281/zenodo.7414954


## 2026-10-27 신형 LISEM 공개 원본의 추가 결정적 코드 감사

### 공개 상태, 버전 일치성 및 빌드
- 공식 GitHub `bastianvandenbout/LISEM`은 공개(public) 코드와 `CMakeLists.txt`, `lisem/model/` C++ 실행루틴, OpenCL 계산 커널 `lisem/model/kernels/`를 제공. 신형 Windows 포터블 실행파일/설치파일/파이썬 wheel 0.2.4 공식 https://lisemmodel.com/docs/downloads/ .
- 저장소 마지막 검색 가능 main commit **`6a5ef17d87bab4227d48673c95c12c61462114dd` = 2022-08-10**. GitHub 릴리스 `source`는 2022-08-23 게시 Beta 0.2.4 (source only; asset 별도 없음). **그러나 source `lisem/core/version.h`는 `MAJOR=0, MINOR=2, PATCH=3`**로 선언. 즉 릴리스 이름 0.2.4와 공개 main/CMake 빌드에서 읽는 소스 버전 0.2.3이 불일치. 2025 Epple 논문의 `LISEM (2024)` 실행본과 최신 GitHub SHA 동일 여부 **입증할 수 없음**.
- 공개 `README.md`는 under development, alpha, bugs 경고. `lisem/test/CMakeLists.txt`는 사실상 project declaration만 남은 빈 테스트 골격이며 검증된 canopy/hydro/sediment 회귀테스트 없음.
- `CMakeLists.txt`는 app/python/test 토글과 C++14/17/C/Fortran, OpenMP, Qt/OpenCL/OpenGL/기타 GIS dependency 체계를 보유. 독립 빌드 실행 및 cm급 native 시뮬레이션은 이번 코드 읽기에서 수행하지 않음.
- 루트 `LICENSE`는 제3자 `Can Güney Aksakalli` 2017 MIT 전문이며 **LISEM 소유자 전체 프로그램에 대한 MIT 근거가 아님**. `licence.txt`는 GPLv3 본문, `lisem/core/licence.h`는 Bastian van den Bout copyright 및 GPL 문구. 따라서 일반적으로 GPL 기반으로 판단하되 세부 라이선스 혼선은 기록.

### 수관저류 및 수관차단 미작동: 정확 경로
- `lisem/model/kernels/model_hydrology.cl:289,302,310,326,397`: `SCANOPY`에서 기존 물을 읽고 `Smaxc=SMAX_CANOPY`를 읽지만, **`Smaxc`를 이후 전혀 사용하지 않음**. `h=h+store_canopy`, `h=h+rain`, `write_imagef(SCANOPYN,...,0)`. 즉 수관 강우차단/저장/배수 물수지를 계산하지 않고 기존 저장을 지표수에 전량 합산한 뒤 저장을 0으로 만듦.
- `lisem/model/kernels/model_evapotranspiration.cl:151,169,192`: 같은 `Smaxc`를 읽지만 사용하지 않고, LAI 식은 `//float LAI = ndvi * 4.0;`로 주석 처리됨. `SCANOPYN`도 0으로 기록.
- `lisem/model/modelrun.cpp:162–170`에서 hydrology 호출 시 **rain scalar=0** (`PlaceArgument(38,(float)0.0)`). 반면 `lisem/model/modelruncompile.cpp:1266` `flow` 커널은 `T_RAIN` 원강우맵을 받아 `model_flow.cl:247,532`에서 지표수에 직접 추가하는 경로가 있음. **결과적으로 2D flow 원강우가 수관저류 경로를 통과하지 않음**. 이는 공식 웹사이트의 LAI/수관최대저류 `SMax Canopy` 설명이 바이너리의 실제 구현이라는 주장을 뒷받침하지 못함.
- 참고: `SCANOPY` 출력맵 존재 자체는 canopy mass conservation 검증 아님.

### 강우박리 호출 매개변수 0 고정: 별도 치명적 결함
- `lisem/model/kernels/model_sediment.cl:204,348–423`에는 `float rain_m`로 `directrain=(1-vegcover)*rain_m*1000`, `throughfall=vegcover*rain_m*1000`, `DetDT1/2`, `DetLD1/2` 빗방울 박리 계산이 구현.
- 그러나 `lisem/model/modelruncompile.cpp:1637`에서 **`m_CLProgram_Erosion->PlaceArgument(81,0.0f)`**, `lisem/model/modelrun.cpp:546`에서도 **`PlaceArgument(81,(float)0.0)`로 재설정**. 이 코드 경로에서 실제 `rain_m`은 0.0으로 전달된다. 따라서 **강우박리 직달우와 수관적하우 항이 모두 0이 됨**. 이 사실은 단순한 미검증이 아니라 **소스에 보이는 실행 경로상 강우박리 입력의 연결 부재**이다.
- `lisem/algorithms/raster/rasterflow.h:1375`의 `AS_SplashErosion(...,rainintensity,dt)` 독립 래스터 스크립트 함수에는 빗방울 박리/식생높이 항이 있지만 **이는 UI 통합모델 `modelrun.cpp`가 실행하는 커널과 별도 경로**이다. 해당 함수 존재만으로 통합모델의 rain_m=0 문제가 해결되지 않음. 그 별도 함수에도 동적 LAI 수관저류·수관배수 결합은 확인되지 않음.

### 유사수송 국지 배출 집계 및 실제 버그 후보
- `model_sediment.cl` 원본의 `qfsout = qfsout + z_x1 < -1000 ? sflux_x1 : 0.0f;` 형태가 4방향에서 반복. C/OpenCL의 연산자 우선순위상 `(qfsout + z_x1) < -1000 ? sflux_x1 : 0`로 해석되어 `qfsout += (z_x1 < -1000 ? sflux_x1 : 0)`와 같지 않음. 유역 외부 배출 집계에 영향을 줄 우려가 높은 정적 코드 결함. 바이너리 실행 비교 전까지 영향 규모 추정 금지.
- `model_flow.cl`은 실제 x/y 방향 인접면 유량 및 수면, 유속 계산함. `model_sediment.cl`도 x/y four-face sediment flux, 유수박리/퇴적 및 `DEMN` 업데이트 루틴 포함. 그러나 이 장점들이 canopy/precip splash missing과 구분되어야 함.

### 판정
| 항목 | 판정 |
|---|---|
| 2022 공개 소스 전체 가용 | **PASS** |
| 공식 0.2.4 Windows 배포 존재 | **PASS** (설치/실행 성공은 미검증) |
| 2025년 논문과 정확 동일 코드·릴리스 식별 | **미입증** |
| GUI 모델에서 입력 `SMax Canopy`에 의한 동적 LAI 수관차단 | **소스 경로 FAIL** (Smaxc 읽은 후 미사용; 수관저장 0으로 리셋) |
| GUI 모델의 침식모듈로 실제 강우강도 전달 | **소스 경로 FAIL** (rain_m=0 고정) |
| 2D 지표수유동/유사 및 침식 식 자체 존재 | **PASS** (실행 안정성은 미검증) |
| 1cm/5cm 동일 소스 native 실행·수치수지·DoD 검증 | **미실행/미입증** |

**따라서 신형 LISEM GitHub 2022 공개 소스는 연구자가 요구한 원본 단일모델의 필수조건(작동하는 동적 수관차단 및 강우박리)을 충족하지 않아 현재 상태로는 연구 주모델로 채택 불가.** 이 판정은 OpenLISEM Classic 7.5.2 수치문제로 인해 내린 것이 아니라 새 코드베이스의 실제 호출경로를 읽고 내린 독립적 결과다. Epple(2025)의 실제 1cm LISEM은 2024 사용버전으로 인용하므로 해당 후속 소스가 존재하고 비공개인지 또는 링크를 찾지 못했는지는 추가 확인 필요.

### 코드 링크
- [model_hydrology.cl](https://github.com/bastianvandenbout/LISEM/blob/6a5ef17d87bab4227d48673c95c12c61462114dd/lisem/model/kernels/model_hydrology.cl)
- [model_evapotranspiration.cl](https://github.com/bastianvandenbout/LISEM/blob/6a5ef17d87bab4227d48673c95c12c61462114dd/lisem/model/kernels/model_evapotranspiration.cl)
- [model_sediment.cl](https://github.com/bastianvandenbout/LISEM/blob/6a5ef17d87bab4227d48673c95c12c61462114dd/lisem/model/kernels/model_sediment.cl)
- [modelrun.cpp](https://github.com/bastianvandenbout/LISEM/blob/6a5ef17d87bab4227d48673c95c12c61462114dd/lisem/model/modelrun.cpp)
- [modelruncompile.cpp](https://github.com/bastianvandenbout/LISEM/blob/6a5ef17d87bab4227d48673c95c12c61462114dd/lisem/model/modelruncompile.cpp)
- [model_flow.cl](https://github.com/bastianvandenbout/LISEM/blob/6a5ef17d87bab4227d48673c95c12c61462114dd/lisem/model/kernels/model_flow.cl)
- [version.h](https://github.com/bastianvandenbout/LISEM/blob/6a5ef17d87bab4227d48673c95c12c61462114dd/lisem/core/version.h)
