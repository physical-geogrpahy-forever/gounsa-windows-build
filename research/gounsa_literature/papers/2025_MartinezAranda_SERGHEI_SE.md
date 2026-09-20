# 서지정보
Martínez-Aranda, S., Caviedes-Voullième, D., Segovia-Burillo, J., Morales-Hernández, M., Gaspar, L., Navas, A., & García-Navarro, P. (2025 preprint). *SERGHEI-SE: An Open-Source High-Performance-Computing Model for Soil Erosion and Sediment Transport Processes in Catchments*. SSRN preprint. 세부 최종 journal publication은 이후 2026 평가 논문과 구분한다.

# 이 논문을 찾은 이유
최신 HPC genuine 2D catchment erosion model이 root/vegetation quantity를 직접 다루는지 확인하기 위해 검토했다.

# 연구 유형
- physically based HPC numerical model
- preprint/model description

# 공간 구조
- genuine 2D shallow-water equations
- 2D suspended transport
- soil erosion/deposition
- high-resolution catchment scale

# 적용 환경
- synthetic tests
- Mediterranean catchment

# 핵심 과정
- rain-to-runoff
- runoff-driven erosion
- suspended sediment transport
- soil redistribution
- surface elevation change

# 식생 입력
- vegetation protection/land management/bedrock exposure를 modification factor로 처리
- 해당 factor는 Sentinel-2 기반
- root biomass/RLD 직접입력 아님

# 핵심 식
SEHS closure model을 사용. exact equations는 final publication/model documentation에서 관리한다.

# 파라미터와 단위
원문 식/코드 기준.

# 원 논문의 구현 범위
HPC 2D hydro-erosive simulation at catchment scale.

# 고운사에 직접 사용할 수 있는 부분
최신 2D hydro-erosion engine 비교후보.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root/litter quantities를 vegetation modification factor 대신 넣으면 **새로운 coupling**.

# 한계
strict quantitative vegetation condition 미충족.

# 최종 판정
**2D 엔진 비교후보, vegetation coupling은 탈락.**
