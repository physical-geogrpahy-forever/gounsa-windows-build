# 서지정보
Argles, A. P. K., Robertson, E., Harper, A. B., Morison, J. I. L., Xenakis, G., Hastings, A., McCalmont, J., Moore, J. R., Bateman, I. J., Gannon, K., Betts, R. A., Bathgate, S., Thomas, J., Heard, M., & Cox, P. M. (2023). Modelling the impact of forest management and CO2-fertilisation on growth and demography in a Sitka spruce plantation. *Scientific Reports*, 13, 13487. https://doi.org/10.1038/s41598-023-39810-2

# 이 논문을 찾은 이유
RED가 이론적 DGVM cohort model에 그치지 않고 실제 온대/냉온대 산림에서 수목 size distribution과 탄소 flux를 모의한 사례가 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 적용 및 현장자료 평가
- JULES-RED forest demography

# 공간 구조
- stand/site application
- RED tree mass classes
- distributed catchment application은 아님

# 적용환경
- Harwood Forest, Northumberland, UK
- upland Sitka spruce plantation
- 1973년 식재, 약 50년생 stand 평가

# 핵심과정
- RED tree mass-class growth
- JULES carbon assimilation and fluxes
- stand structural development
- thinning management
- CO2 fertilisation

# 식생입력
- observed 2018 tree size distribution for fitted runs
- historical simulations initialized with 2500 trees ha-1 in lowest RED mass class
- Needle-leaved Evergreen Tree PFT

# 핵심식
RED의 mass-class continuity/recruitment framework를 JULES carbon assimilation과 결합했다. 관리 시나리오에서는 stand age 25년에 수목의 1/3을 size distribution 전체에서 균등 제거하는 방식으로 thinning을 구현했다.

# 파라미터와 단위
- initial density: 2500 trees ha-1
- tree mass classes [kg C]
- stand biomass [kg/t C area-1]
- GPP/NPP/respiration carbon flux

# 원 논문의 구현 범위
1973-2017 historical simulations와 2015-2020 관측기간 평가를 수행했다. JULES-RED는 관측 size structure 및 GPP seasonal/diurnal cycle을 일정 수준 재현했으며 thinning과 historical CO2를 포함한 경우 stand structure 평가가 개선됐다.

# 고운사에 직접 사용할 수 있는 부분
- RED mass classes가 실제 산림 stand 구조에 적용 가능하다는 근거
- 온대권 conifer forest에서 demographic initialization과 field evaluation precedent
- 관측 size distribution을 cohort initial condition으로 넣는 방법

# 필요한 새로운 coupling
- mixed Korean temperate forest PFT calibration
- herb/shrub/tree mixed succession
- spatial hillslope/catchment deployment
- geomorphic soil state exchange

# 한계
1. 단일 우점 침엽수 plantation
2. 하층 초본/관목 천이를 검증하지 않음
3. catchment/topographic gradient 실험이 아님
4. management experiment이므로 natural postfire succession과 직접 동일하지 않음

# 최종 판정
**보조근거 / JULES-RED field-demography validation.**

고운사 최종모델 채택 근거는 RED 2020의 multispecies succession 구조와 JULES hydrology/coupling 능력을 함께 보아야 하며, 이 논문만으로 criterion 2 또는 4를 충족했다고 보지 않는다.

# 참고 링크 / DOI
https://doi.org/10.1038/s41598-023-39810-2
