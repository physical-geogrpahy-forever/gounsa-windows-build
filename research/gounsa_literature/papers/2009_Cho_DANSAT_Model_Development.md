# 서지정보
Cho, J., & Mostaghimi, S. (2009). *Dynamic agricultural non-point source assessment tool (DANSAT): Model development*. Biosystems Engineering, 102(4), 486-499. DOI: 10.1016/j.biosystemseng.2009.01.011.

# 이 논문을 찾은 이유
interrill, rill, channel erosion을 구분하면서 dynamic plant growth, roots, residues와 erodibility를 연결하는 distributed continuous model을 찾기 위해 검토했다.

# 연구 유형
- distributed physically based continuous numerical model
- model development

# 공간 구조
- grid-based distributed watershed model
- overland/channel routing
- 이 채팅의 검증 결과 genuine 2D shallow-water field로 보지 않는다

# 적용 환경
- small agricultural watersheds

# 핵심 과정
- interception
- ET
- infiltration
- percolation
- overland flow
- channel flow
- interflow/baseflow
- interrill detachment
- rill detachment
- channel detachment
- transport capacity/routing
- dynamic soil/plant/residue states

# 식생 입력
Dynamic variable component:
- plant growth
- crop variables
- live/dead root biomass
- residue decomposition
- detachment-related soil parameters

WEPP-style routines are used for erosion-parameter dynamics.

# 핵심 식
이 채팅에서의 핵심 확인점은 dynamic plant/root/residue state가 interrill/rill erodibility 조정으로 이어진다는 것이다. Exact equations는 원문 및 WEPP documentation을 기준으로 구현한다.

# 파라미터와 단위
WEPP-derived Ki/Kr-related states, root and residue pools. Exact units는 원문 표 기준.

# 원 논문의 구현 범위
small agricultural watershed에서 hydrology, sediment, dynamic management/plant state를 continuous simulation.

# 고운사에 직접 사용할 수 있는 부분
- dynamic vegetation/root/residue -> Ki/Kr-related erosion resistance의 실제 numerical-model precedent
- interrill/rill/channel separation

# 새로운 coupling이 필요한 부분
LPJ-GUESS states를 DANSAT variables로 대체하거나 genuine 2D engine에 parameterization을 이전하면 **새로운 coupling**.

# 한계
- agricultural emphasis
- genuine 2D surface-flow field가 아님
- mountain forest validation 부족

# 최종 판정
**핵심 보조근거: biomass-dependent Ki/Kr model lineage.**

# 참고 링크 / DOI
10.1016/j.biosystemseng.2009.01.011
