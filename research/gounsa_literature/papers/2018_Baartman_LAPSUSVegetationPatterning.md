# 서지정보
Baartman, J. E. M., Temme, A. J. A. M., & Saco, P. M. (2018). The effect of landform variation on vegetation patterning and related sediment dynamics. *Earth Surface Processes and Landforms*. https://doi.org/10.1002/esp.4377

# 이 논문을 찾은 이유
absolute vegetation density가 LAPSUS의 erosion/deposition parameters에 어떻게 들어가는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- coupled dynamic vegetation + LAPSUS LEM

# 공간 구조
- grid-based catchment/hillslope
- multiple-flow routing
- annual LEM + daily vegetation model

# 적용 환경
- 반건조 patterned vegetation

# 핵심 과정
- overland-flow erosion
- deposition
- infiltration
- vegetation growth/dispersal

# 식생 입력
- vegetation density V, g m-2

# 핵심 식
`C = gamma * Q^m * Lambda^n`
`D = K * Q * Lambda`
`T = P * Q * Lambda`

vegetation density가 K, P, infiltration을 조절한다.

# 파라미터와 단위
- V: g m-2
- K, P: LAPSUS surface factors
- vegetation breakpoint: 약 5 및 20 g m-2
- 검토된 구현에서 높은 vegetation에서 K를 매우 낮추고 P를 크게 높이는 강한 scaling을 사용

# 원 논문의 구현 범위
dynamic vegetation density와 erosion/deposition을 연결한다.

# 고운사에 직접 사용할 수 있는 부분
- absolute vegetation density를 쓰는 점
- detachment와 deposition 효과를 분리하는 구조

# 새로운 coupling이 필요한 부분
고운사 PFT별 biomass로 K와 P를 산정하는 것은 원 논문 밖의 `새로운 coupling`이다.

# 한계
고정 biomass breakpoint와 강한 K/P scaling이 연구설정 의존적이다.

# 최종 판정
- 탈락
- 직접 파라미터 이식 비권장

# 참고 링크 / DOI
https://doi.org/10.1002/esp.4377
