# 서지정보
Wang, T., Hou, J., Li, J., Li, P., Tong, Y., Zhang, N., Cheng, S., Li, J., & Li, Z. (2023). *A novel two-dimensional numerical model developed for slope soil erosion*. CATENA, 232, 107387. DOI: 10.1016/j.catena.2023.107387.

# 이 논문을 찾은 이유
Iber+, Wu, PSEM_2D보다 고운사 산지 사면침식에 직접적인 genuine 2D rainfall-runoff-morphodynamic engine이 존재하는지 확인하기 위해 검토했다.

# 연구 유형
- 2D numerical slope-erosion model
- rainfall-runoff-sediment-morphodynamics
- laboratory calibration/validation

# 공간 구조
- genuine 2D slope model
- overland-flow convergence represented in 2D
- morphology evolution coupled to erosion
- exact governing-equation implementation details are only partially accessible from the public article text and must be checked against the full paper before coding

# 적용 환경
- loess slope
- laboratory rainfall erosion experiments
- steep cohesive-soil slope context
- forest/postfire application 없음

# 핵심 과정
- rainfall-runoff
- sediment transport capacity
- erosion/deposition
- spatial erosion contribution
- morphology evolution
- rill development is treated as evolving topography rather than a static preassigned rill geometry

# 식생 입력
- vegetation/root/litter module not identified in the published model
- quantitative root biomass/RLD 없음

# 핵심 식
The paper develops a corrected sediment-transport-capacity relation for cohesive loess slopes and couples it to a two-dimensional runoff-sediment-morphology model.

Publicly accessible text confirms:
- existing 1D approaches were criticized because overland-flow paths are not fixed
- topographic change and erosion hydraulics are coupled
- model performance was evaluated against rainfall experiments

Exact governing equations and coefficient definitions require the full article before implementation.

# 파라미터와 단위
- corrected sediment transport capacity
- runoff and sediment-state variables
- morphodynamic variables
Exact parameter units require full-paper verification.

# 원 논문의 구현 범위
2D runoff and sediment erosion on a morphodynamically evolving loess slope.

Reported validation:
- runoff NSE approximately 0.83
- sediment-concentration NSE approximately 0.66
- spatial erosion pattern reproduced with strongest erosion in middle/lower slope

# 고운사에 직접 사용할 수 있는 부분
1. genuine 2D slope-specific erosion and morphodynamic evolution
2. fixed-rill geometry is unnecessary in principle
3. cohesive steep-slope sediment-transport formulation is closer to hillslope erosion than fluvial gravel-bar models

# 새로운 coupling이 필요한 부분
Any LPJ-GUESS root/litter state added to detachment, transport capacity, or critical erosion parameters is **새로운 coupling**.

# 한계
- vegetation absent
- loess-specific transport-capacity correction
- laboratory scale
- mountain forest/postfire validation absent
- public article access was insufficient to audit every governing equation; coding from this file alone is prohibited

# 최종 판정
- **2D engine comparison candidate**
- potentially closer geomorphically to Gounsa than generic river morphodynamic engines
- does not solve quantitative vegetation coupling
- cannot yet displace Iber+ without full-equation/source-code audit

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2023.107387
