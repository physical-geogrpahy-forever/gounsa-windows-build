# 서지정보
Jia, Z., Chen, S., Fu, Y. H., Martín Belda, D., Wårlind, D., Olin, S., Xu, C., & Tang, J. (2026). Advancing ecohydrological modelling: coupling LPJ-GUESS with ParFlow for integrated vegetation and surface-subsurface hydrology simulations. Geoscientific Model Development, 19, 1727–1747. https://doi.org/10.5194/gmd-19-1727-2026

# 이 논문을 찾은 이유
고운사 5조건 중 실제 cohort vegetation, topography-driven catchment hydrology, soil-depth/soil-moisture representation, <=daily coupling을 현대 공개코드에서 동시에 만족하는 계열을 찾기 위해 검토했다.

# 연구 유형
- coupled model description 및 basin-scale validation
- LPJ-GUESS + ParFlow = PF-LPJG

# 공간 구조
- ParFlow의 실제 3D terrain-following geographic grid와 LPJ-GUESS grid를 coupling
- published Danube application은 10 km resolution
- ParFlow가 surface/subsurface lateral flow와 groundwater를 실제 인접 cell 간 계산

# 식생 및 cohort 구조
- LPJ-GUESS의 age-based tree cohorts를 유지
- establishment, growth, mortality, interspecific competition 및 ecological succession을 포함
- cohorts가 light, space, soil resources를 경쟁
- 논문 자체의 Danube 실험에서는 shrub/grass understory 구성을 별도로 상세 보고하지 않아, 하층식생 criterion은 model capability와 case-study demonstration을 구분해야 함

# 토양 및 수문
- ParFlow가 3D variably saturated Richards equation과 overland flow를 계산
- LPJ-GUESS soil moisture/runoff module을 ParFlow로 대체
- LPJ 측 soil layers를 0.1, 0.3, 0.6, 1.0 m thickness의 4층, 총 2 m로 수정
- layer-specific sand/clay/silt 입력
- ParFlow soil moisture가 LPJ-GUESS internal soil state를 매일 overwrite
- groundwater convergence, capillary rise, lateral groundwater flow, stream formation을 mechanistically 계산

# 시간 구조
- ParFlow: hourly timestep in the published coupling setup
- LPJ-GUESS: daily
- ParFlow output을 매 24 hydrologic steps마다 LPJ-GUESS로 전달
- LPJ-GUESS P-ET를 다시 hourly ParFlow forcing으로 분배

# 적용 환경
- Danube River Basin
- 38-year simulation, 1980–2018
- streamflow, soil moisture, ET, water-table depth를 관측/RS 자료와 평가
- topography와 groundwater가 vegetation-water interactions에 미치는 영향을 분석

# 검증 결과 중 구조적으로 중요한 점
- stand-alone LPJ-GUESS보다 streamflow와 surface soil moisture 개선
- low flow 및 peak timing 개선
- WTD와 lateral groundwater representation을 실제 검증

# 공개성
- coupled PF-LPJG code가 Zenodo DOI 10.5281/zenodo.16908049로 공개
- ParFlow와 사용 LPJ-GUESS 버전도 archive 제공

# 고운사에 직접 사용할 수 있는 부분
- hourly physically based landscape hydrology + daily cohort vegetation의 two-way coupling architecture
- 실제 terrain/grid에서 soil moisture를 vegetation model에 주고 vegetation ET를 다시 hydrology에 반환하는 pattern
- event/hourly geomorph engine과 daily vegetation engine을 분리하는 고운사 설계에 매우 가까운 선례

# 새로운 coupling이 필요한 부분
- published scale 10 km를 10–50 m hillslope scale로 downscale하면 검증이 새로 필요
- erosion/deposition에 따른 DEM과 dynamic soil thickness change
- root exposure/burial and root-mass removal
- 고운사에서 explicit shrub/herb succession setup 검증

# 한계
- Danube application의 10 km resolution은 고운사 fine-scale precedent가 아님
- fixed/static root distribution과 fixed rooting depth가 논문에서도 limitation으로 지적됨
- coupled structure가 계산적으로 무거움

# 최종 판정
- 핵심 현대 후보/선례
- 5조건 중 공간성, 토양수문, 유역지형, 시간해상도는 강하게 만족
- 하층식생의 명시적 case-study demonstration과 fine-resolution validation은 추가 확인 필요
