# 서지정보
Longo, M., Knox, R. G., Medvigy, D. M., Levine, N. M., Dietze, M. C., Kim, Y., Swann, A. L. S., Zhang, K., Rollinson, C. R., Bras, R. L., Wofsy, S. C., & Moorcroft, P. R. (2019). The biophysics, ecology, and biogeochemistry of functionally diverse, vertically and horizontally heterogeneous ecosystems: the Ecosystem Demography model, version 2.2 – Part 1: Model description. Geoscientific Model Development, 12, 4309-4346. DOI: 10.5194/gmd-12-4309-2019

# 이 논문을 찾은 이유
개체목 좌표를 쓰지 않으면서 subhourly ecohydrology와 cohort succession, grass/shrub PFT를 결합하는 중간복잡도 모델 후보를 검토하기 위해 확인했다.

# 연구 유형
- 수치모델
- cohort-based Ecosystem Demography model

# 공간 구조
- grid -> polygon -> site -> patch -> cohort hierarchy
- patch는 공통 disturbance history를 가진 면적비율이며 실제 x,y 위치가 없음
- cohort는 유사한 PFT와 크기/높이 집단

# 적용 환경
- 다양한 식생 및 기후
- 본 model-description/evaluation 계보는 열대림 중심이지만 dryland grass/shrub PFT 확장이 존재

# 핵심 과정
- subdaily radiation/energy/water exchange
- photosynthesis and respiration
- plant growth and allocation
- recruitment
- mortality
- disturbance
- hydrology
- soil biogeochemistry
- forest succession

# 식생 입력
- PFT
- cohort size/height/density
- leaf/root/structural biomass pools
- rooting and soil-layer information

# 시간 구조
- biophysical integration timestep은 수분 단위로 설정 가능하며 300-600 s 수준 사용례
- demographic and allocation processes는 일/월/연의 계층적 시간구조

# 하층식생
- smaller cohorts are shaded by larger cohorts
- grass PFTs 존재
- 별도 shrub PFT를 사용한 확장 사례 존재

# 지형/수문 입력
site-level metadata can include:
- soil depth
- slope
- aspect
- elevation
- topographic moisture index

# 고운사에 직접 사용할 수 있는 부분
- storm/event model과 시간해상도가 매우 잘 맞는 생리/수문
- tree/shrub/grass cohort competition 가능
- roots and soil state
- disturbance-driven succession
- soil depth를 외부 공간자료로 줄 수 있음

# 새로운 coupling이 필요한 부분
- 각 LiDAR/geomorph cell 또는 tile을 ED site로 외부 배치
- storm 후 변경된 DEM/soil depth를 site state에 재주입
- native patch fraction을 x,y geomorphic patch로 오해하지 않도록 wrapper 필요
- 한국 온대림 PFT parameterization

# 한계
ED patch는 공간적으로 implicit하므로 내부 patch를 사면의 특정 위치와 직접 연결할 수 없다. fine-scale spatial geomorph coupling은 외부 tile/site wrapper가 필요하다.

# 최종 판정
- 강한 후보
- 생리/수문/event coupling은 매우 강함
- 실제 x,y landscape representation 부족이 가장 큰 약점

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-12-4309-2019
