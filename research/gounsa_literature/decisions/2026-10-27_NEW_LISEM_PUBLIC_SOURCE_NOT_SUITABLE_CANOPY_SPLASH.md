# 2026-10-27 신형 LISEM 공개 코드의 현장 연구 단일모델 적합성 판정

## 질문
'신형 LISEM으로 가용 가능한 코드 확인'에 대한 실제 공개 코드 원본 감사. 이전 OpenLISEM Classic v7.5.2의 수치결함을 신형 LISEM에 전가하지 않으며, 2025년 Epple 1cm 출판 사례와 소스 동일성 보장 없이 기술할 것.

## 공개물
- 개발자 `bastianvandenbout/LISEM` https://github.com/bastianvandenbout/LISEM 2022년 8월 마지막 원본 main SHA `6a5ef17d87bab4227d48673c95c12c61462114dd`.
- GitHub Beta 0.2.4 `source` https://github.com/bastianvandenbout/LISEM/releases/tag/source (2022-08-23 공개)와 공식 0.2.4 Windows portable/installer/python wheel https://lisemmodel.com/docs/downloads/ .
- **source `lisem/core/version.h` 실제 PATCH=3**. 따라서 0.2.4 배포물과 소스 태그의 1:1 재현성은 미확인. GUI/파이썬 코드 CMake 제공하나 빌드/네이티브 실행은 이번 감사에서 수행하지 않음.
- GNU GPLv3 `licence.txt` 및 `lisem/core/licence.h`; 루트 MIT LICENSE는 2017 Can Güney Aksakalli 제3자 이름으로 되어 있어 전체 코드 MIT라는 확신 불가.

## 코드 상태: 4대 핵심 프로세스
1. **동적 수관차단의 연결 누락:** `lisem/model/kernels/model_hydrology.cl` L302 수관 최대저류 `Smaxc`는 읽되 이후 사용 안 함, L310 이전 수관 물을 지표수에 합하고 L397 저장 출력 0. `model_evapotranspiration.cl` L151 `Smaxc`도 미사용, L169 LAI 계산 주석, L192 수관저장 0. `modelrun.cpp` 수문커널 `rain=0`이고 `model_flow.cl`에 지표 원강우맵 `T_RAIN`을 직접 공급하는 별도 경로. 즉 공식 사이트 canopy storage 설명과 2022 통합실행 수관물수지 기능은 구분해야 함.
2. **강우박리의 실행 입력 누락:** `model_sediment.cl` L348–423 직접비+throughfall 식 `rain_m` 필요. `modelruncompile.cpp:1637`이 해당 인자 81에 `0.0f`, `modelrun.cpp:546`도 `0.0`으로 설정. 따라서 해당 OpenCL 모델경로에서는 강우박리 계산 값이 입력 0이 되어 사상 중 직접우 및 적하박리가 억제. **코드 확인 결과**이지 별도 네이티브 사상 실험 결과가 아님.
3. **유수박리/퇴적 및 2D 흐름은 구현:** `model_flow.cl` XY face flux와 수심 유속, `model_sediment.cl` 이송능력/침전속도, 4면 유사수송/지형고도 업데이트 존재. 그러나 현장 안정성 미검증. 독립 스크립트 `lisem/algorithms/raster/rasterflow.h::AS_SplashErosion`는 강우인자를 받지만 통합 GUI hydro의 누락을 해결하지 않음.
4. **경계 유사배출량 코드 결함 후보:** `model_sediment.cl`의 `qfsout=qfsout+z_x1 < -1000 ? sflux_x1 : 0` 등 C/OpenCL precedence로 사면 경계 유사 합계 오류 가능. 원본 재컴파일 실험 전 정량 영향 단정 금지.

## 선행연구 적용 계보
- Maggioli et al.(2022) 5cm LAI 수관저류 및 침식은 고전 LISEM/Jetten-De Roo kinematic-wave 계열로 보이며 2022 신형 코드를 사용했다는 증거가 아님.
- Epple et al.(2025) 1cm DoD/PTV 검증은 `LISEM 2024 lisemmodel.com`을 인용하는 새 계열이나 **정확 소스 SHA/바이너리 없음**. 출판 결과를 2022 공개 소스의 검증으로 동일시 금지.

## 최종 판정
- 소스 공개: **YES**
- 공식 실행배포 존재: **YES**
- 코드상 2D 흐름, 침식/퇴적 식 존재: **YES**
- 공개판 네이티브 실제 작동하는 LAI 수관차단, 직접우/수관적하박리 입력: **NO (실행 호출 경로 불연결)**.
- 실제 가용한 2025년 논문 버전 확보/재현: **NO**.
- 고운사 연구용 원본 단일모델 **NO-GO** (2022 GitHub 배포 코드에 한정). 2025 출판 사용본/현행 별도 코드 존재 가능성은 별도 추적; 존재하지 않는다는 단정 금지.

## 코드 감사 상세
[모델 상세 감사](../models/LISEM_Integrated_VanDenBout_Source_Audit.md)
