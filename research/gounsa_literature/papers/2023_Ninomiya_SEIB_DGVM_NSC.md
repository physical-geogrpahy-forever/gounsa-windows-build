# 서지정보
Ninomiya, H., Kato, T., Vegh, L., & Wu, L. (2023). Modeling of non-structural carbohydrate dynamics by the spatially explicit individual-based dynamic global vegetation model SEIB-DGVM (SEIB-DGVM-NSC version 1.0). Geoscientific Model Development, 16, 4155-4170. DOI: 10.5194/gmd-16-4155-2023

# 이 논문을 찾은 이유
SEIB-DGVM이 개별목 수준에서 root carbon state와 daily turnover를 실제로 유지하는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 확장
- carbon allocation / NSC model

# 공간 구조
- 기본 virtual forest 30 m x 30 m
- 1 m x 1 m establishment cells
- individual trees spatially explicit aboveground

# 적용 환경
- point and global validation
- multiple climatic regions

# 핵심 과정
- photosynthesis
- respiration
- NSC allocation
- leaf/trunk/root storage
- tissue turnover
- establishment
- mortality
- wildfire/heat stress in base SEIB dynamics

# 식생 입력
- leaf biomass
- trunk biomass
- root biomass
- leaf NSC
- trunk NSC
- root NSC

# 핵심 식
Daily NPP is allocated among leaf, trunk and root NSC pools. Root and leaf NSC turnover follows the general organ turnover at daily steps.

# 파라미터와 단위
- physiology: daily
- trunk growth: monthly
- establishment/disturbance: annual
- NSC concentration: mg g-1 in validation

# 원 논문의 구현 범위
SEIB-DGVM에 기관별 NSC를 추가하여 drought/stress 및 carbon allocation을 더 물리적으로 표현한다.

# 고운사에 직접 사용할 수 있는 부분
- root carbon state가 단순 추정치가 아니라 모델 상태량이라는 근거
- fire mortality 후 root/dead-root transition을 확장할 starting point
- daily root turnover 정보

# 새로운 coupling이 필요한 부분
- live root -> dead root explicit geomorph state
- root biomass -> RLD/RSAD/root reinforcement
- horizontal root footprint
- root decay kinetics after fire

# 한계
NSC와 fine-root biomass가 있다고 해서 공간적 root architecture가 해결되는 것은 아니다.

# 최종 판정
- 채택: SEIB root-state 계보 근거

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-16-4155-2023
