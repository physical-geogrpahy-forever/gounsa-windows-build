# 서지정보
Zhou, S., Li, J., Li, P., Chang, E., Yu, K., Liu, X., Wan, Q., & Wang, Y. (2025). Vegetation restoration regulates slope-scale sediment source-sink transitions on the Loess Plateau: Evidence from field scouring experiments. Geomorphology, 110074. https://doi.org/10.1016/j.geomorph.2025.110074

# 이 논문을 찾은 이유
식생천이가 총 erosion rate뿐 아니라 사면 내 erosion/deposition source-sink 공간구조를 바꾸는지 확인하기 위해 검토했다.

# 연구 유형
- 현장 scouring experiment
- 3D topographic change analysis

# 공간 구조
- slope-scale
- 3D erosion/deposition mapping

# 적용 환경
- 식생복원 사면

# 핵심 과정
- runoff erosion
- deposition
- sediment source-sink transition
- connectivity

# 식생 입력
- succession age/stage

# 핵심 식
이 채팅에서 직접 복구된 보편식은 없다. 1, 11, 15, 25년 succession stage와 여러 inflow 조건에서 erosion/deposition pattern을 비교했다.

# 파라미터와 단위
inflow 4, 8, 16 L min-1. 기타 단위 원문 재검증 필요.

# 원 논문의 구현 범위
succession duration에 따라 runoff/erosion reduction과 deposition area가 비선형적으로 변화한다.

# 고운사에 직접 사용할 수 있는 부분
100년 천이모델 검증 시 outlet sediment yield뿐 아니라 source area, sink area, deposition patch, connectivity를 함께 검증해야 한다는 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS succession state를 SIBERIA/2D erosion source-sink coefficients로 변환하는 것은 새로운 coupling이다.

# 한계
현장실험이며 직접적인 biomass-based process equation은 아니다.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.geomorph.2025.110074
