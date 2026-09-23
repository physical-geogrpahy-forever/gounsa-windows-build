# 서지정보
Balaguer-Romano, R., Espelta, J. M., Brotons, L., Aquilué, N., & De Cáceres, M. (2025). Wildfire connectivity under drought-induced impacts and landscape management strategies in a Mediterranean region. Journal of Environmental Management, 395, 127844. https://doi.org/10.1016/j.jenvman.2025.127844

# 이 논문을 찾은 이유
cohort-based process model을 실제 x-y landscape grid에 배치해 spatially explicit forest succession을 수행한 published example을 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 응용
- spatially explicit forest dynamics
- wildfire connectivity / management scenario

# 공간 구조
- medfate v4.8.0 + medfateland v2.5.2
- Barcelona Metropolitan Region 313,000 ha
- 200 m raster cells (4 ha)
- 각 wildland cell에 topography, soil, vegetation state 입력
- 실제 geographic grid cells

# 적용 환경
- Mediterranean forests and shrublands
- drought-prone fire landscape

# 핵심 과정
- plant growth and mortality
- forest succession
- tree and shrub cohort dynamics
- drought impacts
- landscape management
- forest output -> wildfire connectivity analysis

# 식생 입력
- forest inventory-derived species composition and structure
- tree cohorts
- shrub cohorts
- overstory and understory species
- daily meteorological forcing

# 핵심 식
MEDFATE의 daily water/carbon/growth equations and annual forest dynamics를 각 raster cell에 적용한다.

# 파라미터와 단위
- grid resolution: 200 m
- historical simulation: 2015–2023
- future simulation: 2024–2050
- daily meteorological input

# 원 논문의 구현 범위
각 raster cell에서 stand-level MEDFATE forest dynamics를 수행하였다. forest cells는 overstory tree species와 understory shrub species를 함께 포함했다. shrubland-only cells는 검증 부족으로 biomass를 동적으로 바꾸지 않았다.

# 고운사에 직접 사용할 수 있는 부분
- BiomeE와 유사한 local cohort process model을 GIS cells에 반복 배치하는 published precedent
- 각 cell의 soil/topography/vegetation을 독립 state로 유지
- tree + shrub understory dynamics
- daily forcing
- landscape scale output mapping

# 새로운 coupling이 필요한 부분
- published application resolution 200 m를 고운사 5–25 m급으로 축소할 경우 계산비용과 parameter scale 검증 필요
- hourly geomorphic storm engine과 day-level MEDFATE state exchange
- erosion/deposition-driven soil-depth change
- Korean species parameters

# 한계
- 200 m resolution was selected because of computational limitations
- shrubland-only dynamics not validated in this study
- herbaceous succession is not demonstrated at the same level as tree/shrub dynamics
- no geomorphic feedback in the published application

# 최종 판정
- 채택: spatially explicit cohort forest model precedent
- 특히 'local cohort physiology/demography + raster landscape wrapper' 구조의 직접적 선례

# 참고 링크 / DOI
https://doi.org/10.1016/j.jenvman.2025.127844
