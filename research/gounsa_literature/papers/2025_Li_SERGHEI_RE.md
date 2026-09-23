# 서지정보
Li, Z., Rickert, G., Zheng, N., Zhang, Z., Özgen-Xian, I., & Caviedes-Voullième, D. (2025). SERGHEI v2.0: introducing a performance-portable, high-performance, three-dimensional variably saturated subsurface flow solver (SERGHEI-RE). Geoscientific Model Development, 18, 547–562. https://doi.org/10.5194/gmd-18-547-2025

# 이 논문을 찾은 이유
MEDFATE + medfateland가 SERGHEI와 실제 source-level coupling을 갖는 것이 확인되어, 고운사에서 SERGHEI가 단순 2D surface-flow backend인지 아니면 3D subsurface hydrology까지 확장 가능한지 검증하기 위해 확인했다.

# 연구 유형
- 수치모델 개발
- 고성능 3D variably saturated subsurface flow solver

# 공간 구조
- 3D structured grid
- Richards equation 기반 variably saturated subsurface flow
- Kokkos 기반 CPU/GPU performance portability
- SERGHEI framework 내 surface-subsurface integrated simulation으로 확장되는 구조

# 적용 환경
- infiltration/drainage benchmarks
- hydrogeological applications
- geotechnical applications
- agricultural/hydrological applications

# 핵심 과정
- 3D Richards equation
- saturated/unsaturated flow
- iterative/non-iterative numerical schemes
- spatially distributed subsurface water redistribution

# 식생 입력
이 논문 자체는 vegetation dynamics 논문이 아니다. 식생 coupling은 SERGHEI-RE 자체의 검증 대상이 아니며 medfateland 쪽 coupling layer에서 수행된다.

# 핵심 식
Richards equation 기반 variably saturated subsurface flow. 논문은 여러 numerical solution schemes와 Kokkos parallel implementation을 검증한다.

# 파라미터와 단위
토양 수리특성, retention/conductivity closure, grid resolution, boundary conditions 등 Richards solver 표준 상태량을 사용한다. 세부 benchmark parameter는 원 논문 및 공개 test cases를 따른다.

# 원 논문의 구현 범위
- SERGHEI-RE 독립 3D Richards solver의 정확도, 강건성, 확장성 검증
- desktop, multi-CPU, multi-GPU에서 performance portability 제시
- SERGHEI integrated surface-subsurface framework의 구성요소로 설계
- 논문은 주로 subsurface solver 자체의 성능과 검증에 집중

# 고운사에 직접 사용할 수 있는 부분
1. 고운사 사면에서 3D/측방 subsurface flow를 계산할 수 있는 현대 공개 hydrology engine 후보
2. medfateland의 이미 존재하는 SERGHEI coupling을 향후 3D subsurface hydrology로 확장할 수 있는 계보 근거
3. GPU/CPU 병렬화가 가능해 fine-grid hydrology의 계산비용 완화 가능

# 새로운 coupling이 필요한 부분
- medfateland의 현재 SERGHEI interface가 SERGHEI v2.0의 integrated SWE+RE configuration과 그대로 호환되는지 검증 필요
- geomorphic erosion/deposition이 soil-layer geometry를 바꿀 경우 Richards grid와 MEDFATE soil object의 conservative remapping 필요
- vegetation root uptake와 SERGHEI-RE source/sink term의 층별 mapping 검증 필요
- sediment/Exner geomorph module과의 완전한 vegetation feedback은 별도 coupling

# 한계
- 이 논문은 식생 demographic model이 아니다.
- SERGHEI-RE paper에서는 integrated surface-subsurface system 전체보다 RE solver 검증에 초점을 둔다.
- medfateland과의 v2.0 coupling은 이 논문에서 검증하지 않았다.

# 최종 판정
- 채택: hydrology-engine lineage evidence
- MEDFATE + SERGHEI 경로를 강화하는 핵심 근거
- 단독 식생모델 근거는 아님

# 참고 링크 / DOI
- https://doi.org/10.5194/gmd-18-547-2025
- Model code: https://doi.org/10.5281/zenodo.13166466
- Test cases: https://doi.org/10.5281/zenodo.13282882
