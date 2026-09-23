# 서지정보
Fang, Y., Leung, L. R., Koven, C. D., Bisht, G., Detto, M., Cheng, Y., McDowell, N., Muller-Landau, H., Wright, S. J., & Chambers, J. Q. (2022). Modeling the topographic influence on aboveground biomass using a coupled model of hillslope hydrology and ecosystem dynamics. Geoscientific Model Development, 15, 7879–7901. DOI: 10.5194/gmd-15-7879-2022

# 이 논문을 찾은 이유
고운사 후보가 spatial cohort vegetation + explicit hillslope hydrology + subdaily/day coupling을 동시에 만족하는 실제 선례인지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 결합 및 사면 적용

# 공간 구조
- ELM–ParFlow–FATES coupling
- 실제 terrain-following ParFlow grid와 ELM/FATES column을 1:1 대응
- x,y resolution 90 m
- 31 x 21 horizontal cells, 15 vertical hydrologic layers
- DEM 기반 slope/convexity와 lateral subsurface flow 명시

# 적용 환경
- Barro Colorado Island, Panama
- 50 ha forest dynamics plot을 포함하는 tropical hillslope domain

# 핵심 과정
- FATES PFT x size cohorts
- canopy and understory cohort layers
- recruitment, growth, mortality, competition, disturbance
- ParFlow 3D variably saturated subsurface flow and overland flow
- topography-driven water-table and soil-moisture gradients
- half-hourly ELM/FATES biophysics
- daily vegetation demographic updates

# 식생 입력/상태
- cohort PFT, height, DBH, stem density
- leaf, fine-root, sapwood, storage, structural and reproductive C pools in FATES lineage
- canopy-layer index: overstory vs understory
- seed bank and seedling recruitment are available in current FATES framework

# 하층식생
- FATES framework itself supports explicit understory cohorts and modern parameter sets include shrubs and C3/C4 grasses.
- However, this 2022 hillslope experiment used only two tropical tree PFTs representing early- and late-successional strategies.
- Therefore the paper validates spatial hillslope coupling, not grass/shrub understory performance.

# 토양/수문
- ParFlow terrain-following 3D hydrology
- lateral groundwater/subsurface flow
- overland flow
- vertically variable grid down to bedrock
- ELM soil-water state exchanged with FATES

# 시간해상도
- ELM/FATES biophysics: half-hourly
- vegetation dynamics: end of each day
- ParFlow hydrology resolves the coupled land-hydrology timestep at fine temporal scale

# 고운사에 직접 사용할 수 있는 부분
- actual x,y hillslope column + internal FATES cohort architecture
- explicit lateral hillslope water redistribution
- subdaily biophysics and daily demography
- direct precedent that aspatial ED/FATES patches can sit inside spatially explicit geographic columns

# 새로운 coupling이 필요한 부분
- Gounsa requires dynamic erosion/deposition and soil-depth remapping after storms
- tree/shrub/grass Korean PFT parameterization required
- 90 m published scale is coarser than desired 10–25 m vegetation cells
- fire/postfire succession would need the current FATES/SPITFIRE implementation integrated with this hillslope setup

# 한계
- actual application only used tree PFTs
- FATES disturbance patches remain internally non-geographic area fractions
- computationally heavy E3SM/ELM + ParFlow stack

# 최종 판정
- 핵심 비교 후보
- criteria 1,3,4,5 strongly satisfied
- criterion 2 is strong in the current FATES model, but not demonstrated with shrub/grass in this particular hillslope study

# 참고 링크 / DOI
- https://doi.org/10.5194/gmd-15-7879-2022
