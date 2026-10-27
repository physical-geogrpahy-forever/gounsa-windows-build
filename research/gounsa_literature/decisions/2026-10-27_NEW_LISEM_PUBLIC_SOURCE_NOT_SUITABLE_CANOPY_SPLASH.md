# 2026-10-27 추가 감사 및 이전 판정 정정

**공개 source에서 찾은 문제를 공식 0.2.4 실행판의 결함으로 곧바로 일반화했던 것은 부정확함.** 새 브랜치를 확인하여 버전별로 분리한다.

1. GitHub main SHA 6a5ef17d87bab4227d48673c95c12c61462114dd (2022-08-10)의 lisem/core/version.h는 **0.2.3**.
2. 그동안 누락했던 **GitHub develop** SHA 1e55e6c0bfda28d56a9e1d37e1c21c616820c6a1 (2022-12-12)의 version.h는 **0.2.5**. develop의 model_hydrology.cl에도 수관최대저류량 Smaxc 미사용 및 SCANOPYN=0, modelruncompile.cpp:1637 및 modelrun.cpp:541에도 강우박리 인자81=0.0가 존재. 즉 공개 main뿐 아니라 develop에서도 해당 연결 문제 확인.
3. **공식 SourceForge의 별도 신형 LISEM 0.2.4 Windows 설치판 및 portable ZIP은 실제 공개**(2022-09-07). 버전 0.2.4 바이너리를 가져와 내장 OpenCL 커널과 실제 실행을 분석한 적이 없으므로 **0.2.4 실행판에도 동일 문제가 있다고 단정 불가**.
4. 공식 개발자 2022-07-09 공개 설명 https://lisemmodel.com/blog/2022/07/09/Release-0.2.4/ 에는 0.2.3의 인터페이스 통합모델 강우 입력 오류를 0.2.4에서 수정했다는 내용 명시. 어떤 코드 변경인지는 아직 식별하지 못했음. 0.2.4에 문제가 해결되지 않았다고 공개 0.2.3 소스로 단정하면 안 됨.
5. 공식 빌드 설명 https://lisemmodel.com/docs/compiling/ 은 main/develop/website 3개 브랜치 존재를 명시. 이를 초기 조사에서 누락했음.
6. Epple et al.(2025)의 LISEM (2024) 인용은 해당 해 소프트웨어 버전 릴리스의 증명이 아닐 수 있고, 해당 1cm 실행본의 정확 소스 SHA, 스크립트 내용은 별도 확인 필요.
7. 공식 SourceForge 신형 LISEM 디렉터리에서 0.2.5 또는 2024 이후 새 공개 바이너리는 확인 못했음. 단 이는 비공개 버전 존재/부재의 증명 아님.

**수정 판정: GitHub 공개 0.2.3(main) 및 0.2.5(develop) 소스 기반 통합모델은 수관차단 및 강우박리 연결의 정적 코드 NO-GO. 0.2.4 별도 공식 바이너리는 판정 보류(미시험). '신형 LISEM 전체 공개판이 작동하지 않는다'는 일반화 철회.**

공식 파일:
- https://github.com/bastianvandenbout/LISEM/tree/develop
- https://github.com/bastianvandenbout/LISEM/tree/main
- https://sourceforge.net/projects/lisem/files/LISEM%20%28beta%20release%20new%20software%29/Installer/
- https://sourceforge.net/projects/lisem/files/LISEM%20%28beta%20release%20new%20software%29/Portable/

---

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
