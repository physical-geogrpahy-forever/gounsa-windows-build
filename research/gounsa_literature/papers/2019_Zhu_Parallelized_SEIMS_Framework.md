# Zhu et al. (2019) SEIMS 모듈형 유역모델

## 서지정보
Zhu, L.-J., Liu, J., Qin, C.-Z., & Zhu, A.-X. (2019). A modular and parallelized watershed modeling framework. *Environmental Modelling & Software, 122*, 104526. https://doi.org/10.1016/j.envsoft.2019.104526

## 이 논문을 검색한 이유
고운사 요구 2D 급경사지 유수침식, 식생량과 수관 과정, 원본 공개코드를 하나의 기존 모델에서 확보할 가능성.

## 연구유형 및 적용환경
완전 공개 C++/Python 플러그인 기반 분포형 유역모델 프레임워크, 관측 보정/유역 관리 시나리오; 고운사 산불 사암 사면의 2D 침식 현장 검증은 아니다.

## 공간구조, 실제 원본 코드 확인 (2026-10-26)
원본 GPL3 https://github.com/lreis2415/SEIMS 의 다음 구현 직접 읽음:
- `seims/src/seims_main/modules/hydrology/CASC2D_OF/CASC2D_OF.cpp`: CASC2D 유래 수문 모듈을 포함하나 입력 `m_flowOutIndex`와 `m_downStreamReachId`를 사용하며, 코드 이름만으로 2D 양방향 면 유동이라고 판정하지 못한다.
- `seims/src/seims_main/modules/erosion/SPLASHERO_PARK/SplashEro_Park.cpp`: 강우박리 별도 계산, 식생 수관 피복비 `canopy cover fraction`, USLE C/K 등이 필수 입력.
- `seims/src/seims_main/modules/erosion/KinWavSed_OL/KinWavSed_OL.cpp`: 침식 `CalcuFlowDetachment()`, `m_DETSplash` 수용, `GetSedimentInFlow()`, 지표유사 유입을 **upstream/downstream routed kinematic wave**로 계산. 원본 2D Shallow-Water multi-face sediment advection과 동일하지 않음.

## 핵심과정
강우박리 `D_DETSplash`, 유수박리 `CalcuFlowDetachment`, 유사수송 및 침강/퇴적, 물리기반 유역 유동과 플러그인 연결. 그러나 2D 지표 수송에서 물과 유사 모두 xy 4면 플럭스를 이용하는 완전 2D 원본 기능을 확인하지 못했다.

## 식생입력, 모수 및 단위
Splash module 수관 `canopy_cover` [-], `USLE_C`, `USLE_K`; plant-growth source elsewhere. LAI 기반 dynamic canopy storage/throughfall/leafdrip energy → `SPLASHERO_PARK` native direct 연결 확인 없음. 시간간격, 유사종류, 단위 등은 각 원본 input API 기준, 논문 기능만으로 단정하지 않음.

## 원래 제공 범위 및 새로운 coupling
파편화된 공개 모듈의 native 제어 및 interface는 존재. 진짜 2D 흐름에서 multi-face conservative sediment transport와 LAI-driven canopy-throughfall-to-splash source 구현은 **새로운 coupling**에 해당하며, 원본 단일 2D 엔진 기능이라고 주장하지 않는다.

## 한계, 최종 판정
**주 엔진 탈락 (필수 원본 2D 유사수송과 LAI 수관과정 연결 검증 불가).** 원본은 실제로 공개돼 있으나 2D 경사면 rill/DEM morphodynamics 및 native convergence도 검증되지 않았다. 개발진 문서 및 DOI는 실존; 새 native 실행/관측 정확도 검증 없음.

## 원문과 원본 링크
https://doi.org/10.1016/j.envsoft.2019.104526
https://lreis2415.github.io/SEIMS/
https://github.com/lreis2415/SEIMS
