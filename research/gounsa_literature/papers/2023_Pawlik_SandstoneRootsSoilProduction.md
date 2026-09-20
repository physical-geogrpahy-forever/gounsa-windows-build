# 서지정보
Pawlik, Ł., Gruba, P., Gałązka, A., et al. (2023). Weathering and soil production under trees growing on sandstones - The role of tree roots in soil formation. *Science of the Total Environment, 902*, 166002. https://doi.org/10.1016/j.scitotenv.2023.166002

# 이 논문을 찾은 이유
100년 이내에도 살아 있는 목본뿌리가 기반암 균열과 토양생산에 직접 기여하는지 확인하기 위해 검토했다.

# 연구 유형
- 현장관측
- 토양/암석 분석

# 공간 구조
- tree-scale rhizosphere
- sandstone fractures

# 적용 환경
- 산림
- sandstone parent material

# 핵심 과정
- root wedging
- biomechanical weathering
- rhizosphere alteration
- soil production

# 식생 입력
- living tree roots
- root penetration into fractures

# 핵심 식
보편적인 soil-production equation을 제시한 연구로 확인하지 않았다.

# 파라미터와 단위
root/fracture geometry와 토양화학. 세부 수치 원문 재검증 필요.

# 원 논문의 구현 범위
뿌리가 sandstone crack과 fissure를 따라 침투하고 rock fragment를 분리하며 rhizosphere의 생물화학적 환경을 변화시킨다.

# 고운사에 직접 사용할 수 있는 부분
C/Cr까지 들어가는 woody roots를 수분흡수뿐 아니라 mechanical weathering의 원인으로 취급할 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS woody root biomass/depth를 R->C 또는 C/Cr production rate로 바꾸는 것은 **새로운 coupling**이다.

# 한계
현장근거이며 생산률 식은 별도 필요하다.

# 최종 판정
- 보조근거
- woody mechanical weathering의 최근 현장근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.scitotenv.2023.166002


## 2026-09-21 sandstone baseline role correction

이 논문은 sandstone fracture에 뿌리가 침투하고 fragment 분리 및 rhizosphere alteration에 기여한다는 기작근거로 사용한다.

그러나 보편적인 `root biomass -> annual soil-production rate` 식은 제공하지 않는다.

따라서 현재 baseline `P_sand(h) = P0_sand exp(-h/gamma_sand)`에 LPJ-GUESS root biomass multiplier를 추가하는 근거로 사용하지 않는다.

최종 역할: mechanism support only, not a production-coefficient source.
