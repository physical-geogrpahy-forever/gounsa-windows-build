# 서지정보
Jia, Z., Chen, S., Fu, Y. H., Martín Belda, D., Wårlind, D., Olin, S., Xu, C., & Tang, J. (2026). Advancing ecohydrological modelling: coupling LPJ-GUESS with ParFlow for integrated vegetation and surface-subsurface hydrology simulations. Geoscientific Model Development, 19, 1727–1747. DOI: 10.5194/gmd-19-1727-2026

# 이 논문을 찾은 이유
LPJ-GUESS의 cohort/understory 생태구조를 실제 공간명시 3D 유역수문과 결합하면서 일 또는 시간 단위로 상호작용시키는 최신 선례인지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 결합 및 유역 적용

# 공간 구조
- ParFlow-LPJ-GUESS two-way coupling
- each LPJ-GUESS patch aligns with a ParFlow vertical column
- actual x,y distributed hydrological grid
- Danube River Basin application at 10 km resolution

# 적용 환경
- Danube River Basin
- surface, vadose zone, groundwater and river-basin hydrology

# 핵심 과정
- LPJ-GUESS age/PFT cohorts
- establishment, growth, mortality and competition
- herbaceous understory in standard LPJ-GUESS vegetation framework
- ParFlow 3D saturated-unsaturated flow and overland flow
- daily vegetation-water exchange with hourly hydrology

# 토양/수문
- LPJ-GUESS soil discretization modified to four variable-depth layers: 0.1, 0.3, 0.6, 1.0 m, total 2 m
- layer-specific sand, clay, silt inputs
- ParFlow soil moisture overwrites LPJ-GUESS soil moisture state each day
- deep hydrogeology and water-table dynamics represented in ParFlow
- model depth/layer thickness adjustable by research objective

# 시간해상도
- ParFlow: hourly
- LPJ-GUESS vegetation/ecophysiology coupling exchange: daily
- LPJ-GUESS returns daily P-ET, disaggregated to hourly boundary forcing for ParFlow

# 고운사에 직접 사용할 수 있는 부분
- direct precedent for daily cohort vegetation + hourly 3D hillslope/watershed hydrology
- externally supplied soil moisture state can overwrite internal LPJ-GUESS hydrology
- variable soil layer depths make geomorphic soil-depth coupling conceptually more tractable than standard fixed two-layer LPJ-GUESS

# 새로운 coupling이 필요한 부분
- published application resolution is 10 km, much coarser than Gounsa
- soil thickness changes caused by erosion/deposition are not native
- root exposure/burial and vegetation mortality from geomorphic events need external event rules
- intercell seed dispersal is not demonstrated in the coupled paper

# 한계
- coarse published application
- one patch per stand in the coupled experiment
- patch-destroying disturbance switched off during the coupled simulation

# 최종 판정
- 핵심 비교 후보
- strongest published precedent for daily LPJ-GUESS cohort ecology coupled to hourly 3D hydrology
- combine conceptually with the finer 50 m LPJ-DH precedent when assessing Gounsa feasibility, but do not present the combination as an existing single published model

# 참고 링크 / DOI
- https://doi.org/10.5194/gmd-19-1727-2026
