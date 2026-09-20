# 서지정보
Ivanov, V. Y., Bras, R. L., & Vivoni, E. R. (2008). *Vegetation-hydrology dynamics in complex terrain of semiarid areas: 2. Energy-water controls of vegetation spatiotemporal dynamics and topographic niches of favorability*. Water Resources Research, 44. DOI: 10.1029/2006WR005595.

# 이 논문을 찾은 이유
tRIBS+VEGGIE가 장기 vegetation dynamics를 계산하면서 geomorphic/erosion feedback을 실제로 포함했는지 확인하기 위해 검토했다.

# 연구 유형
- dynamic ecohydrological numerical experiment
- long-term vegetation-topography analysis

# 공간 구조
- distributed complex terrain
- synthetic landscapes
- 50-year hydrometeorological realizations

# 적용 환경
- semiarid ecosystem
- sand/loam/clay scenarios

# 핵심 과정
- vegetation productivity
- water balance
- topographic vegetation niches
- long-term ecohydrologic feedback

# 식생 입력/상태
- dynamic vegetation biomass/carbon states inherited from Part 1
- root biomass distribution
- water stress
- productivity

# 핵심 식
This paper uses the tRIBS+VEGGIE process framework rather than introducing a new erosion law.

# 파라미터와 단위
See Part 1 for vegetation/root process equations.

# 원 논문의 구현 범위
The model explores 50-year vegetation-water-energy dynamics over complex terrain.

Crucially, the authors explicitly state that:
- feedbacks of vegetation on erosion and soil properties are neglected in this study
- landscape geometry and soil properties are held time invariant

# 고운사에 직접 사용할 수 있는 부분
This explicitly identifies the missing link later relevant to Gounsa:
```
dynamic vegetation/root state
 -> erosion/soil-property feedback
```
was **not** implemented, even though quantitative vegetation/root states were available.

# 새로운 coupling이 필요한 부분
LPJ-GUESS or VEGGIE root states driving soil erosion resistance is a new coupling.

# 한계
- erosion and landscape feedback intentionally omitted
- one vegetation type in major numerical experiments
- prescribed/invariant root-profile assumption noted as a strong assumption

# 최종 판정
- **historically important gap-identification paper**
- supports novelty/need for Gounsa coupling but is not itself an erosion solution

# 참고 링크 / DOI
https://doi.org/10.1029/2006WR005595
