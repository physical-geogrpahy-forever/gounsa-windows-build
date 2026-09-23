# 서지정보
Shevliakova, E., et al. (2024). The Land Component LM4.1 of the GFDL Earth System Model ESM4.1: Model Description and Characteristics of Land Surface Climate and Carbon Cycling in the Historical Simulation. Journal of Advances in Modeling Earth Systems. https://doi.org/10.1029/2023MS003922

# 이 논문을 찾은 이유
LPJ-GUESS/FATES 외에 `cohort demography + explicit understory/grass + subdaily hydrology + topographic water redistribution`에 가까운 land-surface model이 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 개발/설명
- Earth system land model
- cohort vegetation demography + land hydrology

# 공간 구조
- geographic ESM grid
- grid 내부 dynamic land tiles
- tile 내부 PPA vegetation cohorts와 emergent canopy layers
- actual 10-50 m hillslope cells가 아니라 sub-grid mosaic

# 적용 환경
- global land surface
- primary/secondary forest, grassland, pasture 등

# 핵심 과정
- cohort recruitment, growth, mortality
- PPA light competition
- 30 min energy/water exchange
- daily biomass change
- daily fire
- plant hydraulics
- groundwater/runoff/river routing

# 식생 입력/상태
- cohort age/size/density
- leaf, fine root, sapwood, heartwood, seeds, NSC
- cohort-specific rooting depth and fine-root biomass
- tree and C3/C4 grass PFTs

# 핵심 식/구조
PPA가 cohort 높이와 crown area를 이용해 canopy layers를 emergently 구성한다. 각 cohort는 soil layer의 fine-root biomass와 hydraulic resistance에 따라 물을 흡수한다.

# 파라미터와 단위
- land-atmosphere timestep: 30 min
- vegetation biomass update: daily
- soil/root hydraulic state: layer-resolved

# 원 논문의 구현 범위
ESM4.1 global land component. Fine catchment geomorphology 목적의 모델이 아니다.

# 고운사에 직접 사용할 수 있는 부분
- tractable PPA cohort architecture
- cohort-specific root-water coupling
- subdaily hydrology/energy exchange
- daily fire and vegetation response

# 새로운 coupling이 필요한 부분
- real LiDAR DEM terrain cells
- external geomorphic soil-state overwrite
- dynamic erosion/deposition layer remapping
- richer shrub/herb PFT succession

# 한계
- sub-grid tile spatiality is statistical/parameterized relative to Gounsa terrain objective
- shrub-rich understory is weak
- no fine mapped mountain catchment validation identified

# 최종 판정
- 보조근거 / strong comparator
- 고운사 주 식생엔진 후보로는 LPJ-GUESS spatial-hydrology lineage와 FATES 아래

# 참고 링크 / DOI
https://doi.org/10.1029/2023MS003922
