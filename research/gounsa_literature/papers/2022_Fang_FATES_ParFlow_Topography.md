# 서지정보
Fang, Y. et al. (2022). Modeling the topographic influence on aboveground biomass using a coupled model of hillslope hydrology and ecosystem dynamics. Geoscientific Model Development, 15, 7879–7901. https://doi.org/10.5194/gmd-15-7879-2022

# 이 논문을 찾은 이유
고운사 식생모델 후보가 다음 조건을 함께 만족하는지 확인하기 위해 검토했다.
- cohort vegetation
- 실제 지형과 lateral hydrology
- 토양수분과 뿌리의 직접 결합
- subdaily/daily process timestep
- 장기 vegetation demography

# 연구 유형
- 수치모델 coupling
- hillslope ecohydrology + vegetation demography

# 공간 구조
- ELM/FATES grid column은 실제 x,y 위치를 가진다.
- ParFlow는 3-D 지형 추종 수문모델이다.
- 연구 설정은 x,y 90 m grid, z 방향 15 layer였다.
- 30 m SRTM DEM을 90 m로 집계해 slope를 계산했다.
- 중요한 한계: FATES 내부 disturbance patch 자체는 x,y 위치가 없는 spatially implicit area fraction이다.

# 적용 환경
- Barro Colorado Island, Panama
- 복잡지형 열대림
- hillslope water redistribution과 biomass pattern

# 핵심 과정
- FATES cohort competition and demography
- ParFlow lateral/vertical hydrology
- ELM soil and land-surface biophysics
- topographic water redistribution
- plant water uptake and growth response

# 식생 입력과 상태
- PFT and size cohort
- cohort height/diameter
- leaf, stem, coarse root, fine root, seed pools
- soil-water-dependent physiology
- recruitment, growth, mortality

# 시간 구조
- ELM-FATES biophysical exchange: 30 min
- FATES vegetation dynamics: daily
- cohort daily carbon increment is allocated to organs and cohort structure changes

# 토양/수문
- ELM soil texture and organic matter determine hydraulic properties
- ParFlow resolves 3-D saturated/unsaturated hillslope flow
- soil moisture is exchanged with FATES
- actual topographic slope affects water redistribution

# 고운사에 직접 사용할 수 있는 부분
- half-hourly ecohydrology + daily cohort demography precedent
- actual terrain/hillslope hydrology can drive cohort vegetation dynamics
- fine-root and soil-water coupling architecture
- geomorphic model and vegetation grid can exchange hydrologic state on a fine temporal schedule

# 새로운 coupling이 필요한 부분
- FATES internal patches cannot be assigned to specific rill/hollow/depositional coordinates inside a grid cell.
- Gounsa erosion/deposition-driven soil-depth changes and root exposure/burial require external state remapping.
- 90 m published grid is much coarser than desired 10–25 m vegetation grid.

# 한계
- technically heavy ELM + FATES + ParFlow stack
- tropical calibration/application
- statistical disturbance patches inside grid cell
- no demonstrated geomorphic soil-profile thickness update after erosion/deposition

# 최종 판정
- 보조 채택 / 최상위 비교후보
- Criteria 2–5 are exceptionally strong.
- Criterion 1 is only partial because the host grid is spatially explicit but internal FATES disturbance patches are not.

# 참고 링크 / DOI
- https://doi.org/10.5194/gmd-15-7879-2022
