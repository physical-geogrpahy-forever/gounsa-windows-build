# 서지정보
De Cáceres, M., Molowny-Horas, R., Cabon, A., Martínez-Vilalta, J., Mencuccini, M., García-Valdés, R., Nadal-Sala, D., Sabaté, S., Martin-StPaul, N., Morin, X., D'Adamo, F., Batllori, E., & Améztegui, A. (2023). MEDFATE 2.9.3: a trait-enabled model to simulate Mediterranean forest function and dynamics at regional scales. Geoscientific Model Development, 16, 3165–3201. https://doi.org/10.5194/gmd-16-3165-2023

# 이 논문을 찾은 이유
BiomeE/BiomeEP와 유사한 cohort 기반 식생모델 가운데 공간명시적 landscape wrapper와 결합 가능한 사례를 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- cohort-based forest ecophysiology and dynamics

# 공간 구조
- 기본 MEDFATE는 stand 내부에서 수평 위치를 명시하지 않는 1D vertical cohort model
- tree/shrub cohorts를 개별 좌표가 아니라 size/species cohort로 표현
- 이후 medfateland가 실제 GIS point/cell 공간단위로 확장

# 적용 환경
- 지중해성 산림
- 지역 규모 forest inventory 기반 적용

# 핵심 과정
- 일 단위 water balance
- photosynthesis, carbon balance
- plant growth, senescence, mortality
- annual recruitment and forest dynamics
- tree and shrub cohort competition
- vertical canopy structure
- soil layers and cohort-specific root-depth distribution

# 식생 입력
- tree cohorts: species, DBH, height, density
- shrub cohorts: species, height, cover
- optional herbaceous layer
- fine-root depth metrics Z50, Z95, optional Z100
- seed bank, seedling bank
- snags, litter and soil carbon states supported in current framework

# 핵심 식
세부 생리식은 model reference에 따르며, cohort별 carbon-water balance와 soil-layer별 root distribution을 이용한다.

# 파라미터와 단위
- daily weather forcing
- forest dynamics top-level: annual
- subdaily plant hydraulics possible in advanced transpiration modes
- root depths: mm

# 원 논문의 구현 범위
MEDFATE 자체는 stand-scale cohort model이며 plant x,y coordinates를 추적하지 않는다. 하지만 tree/shrub cohorts의 동적 성장, mortality, recruitment, fine-root vertical distribution을 계산한다.

# 고운사에 직접 사용할 수 있는 부분
- explicit individual-tree coordinates 없이 cohort vegetation dynamics
- dynamic tree and shrub understory
- daily water/carbon/growth response
- fine-root depth profile state
- mortality and regeneration
- previous simulation state를 다음 simulation input으로 재사용 가능

# 새로운 coupling이 필요한 부분
- 고운사 실제 GIS cells 간 공간연결은 medfateland 사용
- geomorphic event 후 soil depth/root exposure/burial을 MEDFATE state로 remap
- 한국 온대 수종 parameterization
- erosion resistance conversion from root/litter state

# 한계
- 기본 MEDFATE는 spatially explicit하지 않음
- 표준 forest dynamics의 주 state는 woody tree/shrub cohorts이며 herbaceous layer는 tree/shrub와 같은 수준의 장기 demography가 아님
- Mediterranean parameterization을 고운사에 직접 이식할 수 없음

# 최종 판정
- 보조근거에서 핵심후보로 승격
- medfateland와 결합하면 spatial cohort vegetation engine의 매우 직접적인 선례

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-16-3165-2023
