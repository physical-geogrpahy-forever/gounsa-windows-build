# 서지정보
Kang, Y., Huang, M., Hou, J., Tong, Y., & Pan, Z. (2021). *Two-dimensional hydrodynamic robust numerical model of soil erosion based on slopes and river basins*. Journal of Arid Land, 13(10), 995-1014. DOI: 10.1007/s40333-021-0085-2.

# 이 논문을 찾은 이유
GPU 기반 genuine 2D rainfall-runoff erosion model이 slope와 watershed/gully erosion을 동시에 계산하므로 Iber+/Wang 2023보다 고운사 엔진으로 나은지 확인하기 위해 검토했다.

# 연구 유형
- GPU-based 2D hydrogeomorphological numerical model
- slope and watershed erosion validation

# 공간 구조
- genuine 2D shallow-water equations
- Godunov-type scheme
- structured square grid
- GPU acceleration
- Green-Ampt infiltration
- hydrodynamics + morphology

# 적용 환경
- indoor rainfall-erosion slope case
- Coquet River basin numerical case
- rilled hillslopes and basin-scale erosion
- forest/root-specific validation 없음

# 핵심 과정
- rainfall runoff
- Green-Ampt infiltration
- 2D surface hydraulics
- erosion/deposition
- erosion-depth/morphological evolution
- gully erosion

# 식생 입력
No explicit dynamic vegetation/root biomass/RLD erosion-resistance formulation identified.

# 핵심 식
The model solves 2D SWEs with a Godunov-type numerical method and couples sediment/morphological processes.

Exact detachment/transport equations and parameter definitions must be taken from the full article before coding.

# 파라미터와 단위
- shallow-water hydraulic variables
- Green-Ampt infiltration parameters
- erosion/deposition and sediment parameters
- exact units to be verified in full paper

# 원 논문의 구현 범위
High-resolution 2D slope and basin erosion simulation with GPU acceleration.

# 고운사에 직접 사용할 수 있는 부분
- genuine 2D rainfall-runoff erosion
- GPU high-resolution implementation
- basin and rilled-slope applicability
- morphology evolution

# 새로운 coupling이 필요한 부분
Any LPJ-GUESS quantitative vegetation state affecting erosion parameters is **new coupling**.

# 한계
- no direct root/litter quantities
- no postfire forest validation
- available web text is insufficient for complete equation audit
- engine maturity/source-code availability must be checked

# 최종 판정
- **2D engine comparison candidate**
- no evidence yet that it improves the vegetation coupling problem relative to Iber+, Kim 2013 or SERGHEI-SE

# 참고 링크 / DOI
https://doi.org/10.1007/s40333-021-0085-2
