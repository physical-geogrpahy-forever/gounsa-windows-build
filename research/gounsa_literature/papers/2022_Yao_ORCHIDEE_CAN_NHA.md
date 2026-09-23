# 서지정보
Yao et al. (2022). Forest fluxes and mortality response to drought: model description (ORCHIDEE-CAN-NHA r7236) and evaluation at the Caxiuanã drought experiment. Geoscientific Model Development, 15, 7809–7839. https://doi.org/10.5194/gmd-15-7809-2022

# 이 논문을 찾은 이유
수목 cohort와 매우 짧은 수문/생리 timestep을 가진 ORCHIDEE-CAN 계열이 고운사의 식생-지형 coupling 후보가 될 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 개발 및 평가
- land-surface model + forest demography + plant hydraulics

# 공간 구조
- grid/site land-surface column
- tree cohorts/diameter classes
- fine geographic hillslope topology는 아님

# 적용 환경
- tropical forest drought experiment
- ORCHIDEE-CAN lineage itself calibrated/applied to temperate/boreal forests as well

# 핵심 과정
- 30 min energy/water/photosynthesis
- daily carbon allocation
- recruitment and mortality
- tree cohort competition/self-thinning
- dynamic root water uptake
- root-stem-leaf hydraulic architecture
- cavitation-induced mortality

# 식생 입력
- tree cohort size/biomass
- root, stem, leaf pools
- hydraulic traits
- soil water potential

# 핵심 식
Hydraulic fluxes are controlled by water-potential gradients and resistances between soil, roots, stems and leaves. Simulated loss of hydraulic conductance feeds drought mortality.

# 파라미터와 단위
- land-surface timestep: 30 min
- vegetation carbon processes: daily

# 원 논문의 구현 범위
수목 수리학과 drought mortality 개선이 핵심이며 independent herb/shrub succession은 핵심 기능이 아니다.

# 고운사에 직접 사용할 수 있는 부분
- subdaily soil-plant hydraulic coupling precedent
- daily cohort stress/mortality response

# 새로운 coupling이 필요한 부분
- spatial catchment topology
- herb/shrub demographic succession
- geomorphic soil-depth changes

# 한계
ORCHIDEE-CAN multi-layer canopy의 `sub-canopy`는 독립 understory plant community와 동의어가 아니다. Chen et al. 2016 evaluation에서도 understory와 overstory를 같은 species로 처리한 한계를 명시했다.

# 최종 판정
- 보조근거
- strict vegetation-engine shortlist에서는 criterion 2 때문에 탈락

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-15-7809-2022
