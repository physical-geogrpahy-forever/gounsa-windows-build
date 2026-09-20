# LORICA 계열

## 계보
- Lorica: soil-landscape evolution model
- HydroLorica: van der Meij et al. (2020), 수문을 명시적으로 결합
- ChronoLorica: van der Meij et al. (2023), particle-age와 geochronometer tracer를 추가

## 고운사에서 검토한 이유
고운사에서 단일 토심이 아니라 여러 토양층의 gravel, sand, silt, clay, 유기물 조성과 그 이동 이력을 추적할 수 있는 선례를 찾기 위해 검토했다.

## 공통 공간구조
- raster-based soil-landscape framework
- 각 셀 아래에 여러 토양층
- 층 두께와 조성이 시간에 따라 변화 가능

## 핵심과정
- soil profile development
- erosion and deposition
- water-driven redistribution
- bioturbation and tree throw
- particle mixing and tracing

## HydroLorica의 추가점
- spatial water balance
- runoff
- run-on
- reinfiltration
- water erosion
- vegetation state와 soil water availability 연결

## ChronoLorica의 추가점
- particle ages
- radionuclide inventories
- 입자의 이동과 혼합 이력 추적

## 고운사에서 직접 사용할 수 있는 구조
- H_AB와 H_C 같은 층 상태를 단일 토심과 분리
- CF_surface, CF_AB, CF_C 또는 fine/coarse mass pool을 수직적으로 추적
- erosion/deposition으로 profile composition을 갱신
- provenance 또는 tracer를 이용해 기존 coarse fragment와 새로 생성된 spall을 구분할 수 있다는 구조적 선례

## 새로운 coupling
고운사에서는 LORICA 전체를 실행엔진으로 가져오지 않고 LPJ-GUESS와 최종 지형엔진 사이에 profile-state 구조만 가져오는 방향을 검토한다. 따라서 다음은 모두 새로운 coupling이다.
- LPJ-GUESS 토양수분과 LORICA형 profile state 연결
- dynamic H_AB/H_C를 식생 root-accessible storage와 연결
- fire-spall provenance를 coarse-particle tracer로 추가
- 고운사 최종 침식엔진의 erosion/deposition 결과를 profile composition에 반영

## 사용하지 않을 부분
HydroLorica의 수문전체를 그대로 이식하면 고운사의 기존 LPJ-GUESS 수문과 중복되므로 기본안으로 채택하지 않는다.

## 최종 판정
- 다층 soil profile과 coarse-fraction 구조: 채택 근거
- 전체 LORICA/HydroLorica engine: 미채택
- particle provenance/tracer 개념: 보조근거

## 참고문헌
van der Meij, W. M., Temme, A. J. A. M., Wallinga, J., & Sommer, M. (2020). Modeling soil and landscape evolution – the effect of rainfall and land-use change on soil and landscape patterns. *SOIL, 6*, 337–358. https://doi.org/10.5194/soil-6-337-2020

van der Meij, W. M., Temme, A. J. A. M., Binnie, S. A., & Reimann, T. (2023). ChronoLorica: Introduction of a soil–landscape evolution model combined with geochronometers. *Geochronology, 5*, 241–261. https://doi.org/10.5194/gchron-5-241-2023
