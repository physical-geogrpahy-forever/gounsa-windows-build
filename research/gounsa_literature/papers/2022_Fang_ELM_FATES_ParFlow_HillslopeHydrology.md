# 서지정보
Fang, Y., Leung, L. R., Koven, C. D., Bisht, G., Detto, M., Cheng, Y., McDowell, N., Muller-Landau, H., Wright, S. J., & Chambers, J. Q. (2022). Modeling the topographic influence on aboveground biomass using a coupled model of hillslope hydrology and ecosystem dynamics. Geoscientific Model Development, 15, 7879–7901. https://doi.org/10.5194/gmd-15-7879-2022

# 이 논문을 찾은 이유
고운사 식생모델의 엄격 기준인 공간명시적 cohort 구조, 명시적 천이, 토양수분/토심, 실제 사면/유역, 1일 이하 시간간격을 동시에 만족하는 published coupled model이 있는지 확인하기 위해 검색했다.

# 연구 유형
- 수치모델 개발 및 결합
- ELM + FATES + ParFlow

# 공간 구조
- 실제 지리 격자 기반 hillslope domain
- 수평 해상도 90 m
- 31 x 21 horizontal grid
- ParFlow 3D surface-subsurface hydrology
- 각 ParFlow vertical column이 ELM land/soil column과 대응
- FATES 내부 disturbance patch는 좌표 없는 면적분율이므로 실제 x,y 구조는 ELM/ParFlow grid가 담당

# 적용 환경
- Barro Colorado Island, Panama
- 열대산림 hillslope
- 지형고도, 경사, convexity, groundwater-table gradient를 명시

# 핵심 과정
- FATES cohort vegetation dynamics
- PFT/size cohort competition and coexistence
- ParFlow 3D Richards-equation subsurface hydrology
- overland flow
- lateral subsurface flow
- groundwater-table dynamics
- plant root extraction
- hydraulic-failure mortality experiment

# 식생 입력/상태
- cohort biomass and size structure
- roots and root water uptake through host land model
- PFT-specific physiology
- FATES recruitment/mortality/demography architecture

# 시간 구조
- ELM-FATES biophysics and ParFlow state exchange: half-hourly at each ELM model step
- vegetation dynamics: end of each day / daily

# 핵심 결합
각 ELM model step에서 ELM이 infiltration, evaporation, root extraction 등을 ParFlow에 전달하고 ParFlow가 soil-moisture state를 반환한다.

# 토양과 수문
- explicit soil moisture profile
- groundwater-table depth
- 3D lateral subsurface flow
- topographic water redistribution
- surface hydrology

# 고운사에 직접 사용할 수 있는 부분
1. cohort vegetation과 3D hillslope hydrology를 subdaily로 결합한 직접적인 published precedent
2. 실제 x,y grid에서 topographic moisture redistribution이 vegetation biomass/mortality에 feedback하는 구조
3. 폭우 전후 soil-moisture state를 vegetation에 즉시 전달할 수 있는 coupling philosophy
4. FATES의 fine roots, litter, CWD, seed/recruitment, tree/shrub/grass PFT 구조와 결합 가능

# 새로운 coupling이 필요한 부분
- 고운사 시간단위 geomorphic erosion/deposition model과 DEM/soil-depth exchange
- erosion/deposition 후 soil layers 및 root profile remapping
- 10–25 m급 vegetation/hydrology grid 적용
- 한국 온대림 PFT calibration
- fire-spall, dry ravel, shallow landslide processes

# 한계
- published coupled experiment는 90 m이며 고운사 목표 10–25 m보다 거칠다.
- published FATES experiment에서 사용한 PFT는 초기/후기 천이 열대 수목 2개였고 shrub/grass understory를 실제로 운용한 사례는 아니다.
- FATES 내부 patches는 실제 geographic patch가 아니다.
- 계산량과 구현 복잡도가 높다.

# 엄격 5조건 판정
1. 공간명시 cohort: 강함. Geographic column은 명시적, internal FATES patches는 통계적.
2. 하층식생/천이: 모델 기능 자체는 매우 강함. 다만 이 published coupled case는 trees-only.
3. 토심/WHC: 강함. Explicit soil moisture and groundwater hydrology.
4. 유역/지형: 매우 강함. Hillslope topography and lateral flow 직접 구현.
5. 시간간격: 통과. Half-hourly coupling, daily vegetation dynamics.

# 최종 판정
- 채택 후보
- 현재까지 고운사 요구조건에 가장 가까운 published cohort-hillslope coupling 선례 중 하나
- 향후 temperate shrub/grass understory와 10–25 m 계산 가능성 검증 필요
