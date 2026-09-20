# 서지정보
Eltner, A., Favis-Mortlock, D., Grothum, O., Neumann, M., Laburda, T., & Kavka, P. (2025). *Using 3D observations with high spatio-temporal resolution to calibrate and evaluate a process-focused cellular automaton model of soil erosion by water*. SOIL, 11, 413-?. DOI: 10.5194/soil-11-413-2025. 정확한 page end는 원문 재검증 필요.

# 이 논문을 찾은 이유
최신 RillGrow가 rill initiation/growth, splash, deposition, slumping, multi-grain sediment를 얼마나 구현하는지 확인하기 위해 검토했다.

# 연구 유형
- numerical model calibration/evaluation
- cellular automaton erosion model

# 공간 구조
- raster cellular automaton
- microtopography
- overland flow routing은 D8 steepest direction
- plot scale

# 적용 환경
- laboratory and field rainfall simulation plots

# 핵심 과정
- emergent rill network
- Green-Ampt infiltration option
- splash redistribution
- flow erosion/deposition
- slumping/toppling
- clay/silt/sand fractions

# 식생 입력
- bare-soil 중심
- dynamic vegetation/root biomass 없음

# 핵심 식
local cell-based erosion rules; exact S1-S14 equations은 supplement를 따른다.

# 파라미터와 단위
flow, splash, slumping erodibility를 sediment fraction별로 입력.

# 원 논문의 구현 범위
rill network가 topography-flow-erosion feedback으로 자발적으로 발생.

# 고운사에 직접 사용할 수 있는 부분
- emergent rill network의 독립 계보
- McGuire와 별개의 rill-generation 비교후보

# 새로운 coupling이 필요한 부분
LPJ-GUESS vegetation quantities를 erodibility/slumping에 넣으면 **새로운 coupling**.

# 한계
- plot scale
- bare-soil 중심
- D8 local routing
- 산지 large-domain 적용 곤란

# 최종 판정
**보조근거/비교후보.** strict 최종 엔진은 아님.

# 참고 링크 / DOI
10.5194/soil-11-413-2025
