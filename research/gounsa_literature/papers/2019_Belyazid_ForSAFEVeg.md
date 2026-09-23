# 서지정보
Belyazid, S., Phelan, J., Nihlgård, B., Sverdrup, H., Driscoll, C., Fernandez, I., Aherne, J., Teeling-Adams, L. M., Bailey, S., Arsenault, M., Cleavitt, N., Engstrom, B., Dennis, R., Sperduto, D., Werier, D., et al. (2019). Assessing the Effects of Climate Change and Air Pollution on Soil Properties and Plant Diversity in Northeastern U.S. Hardwood Forests: Model Setup and Evaluation. Water, Air, & Soil Pollution, 230, 106. https://doi.org/10.1007/s11270-019-4145-6

# 이 논문을 찾은 이유
고운사 후보 중 산림의 하층 초본 식생을 피복 보정항이 아니라 종별 경쟁과 환경 반응으로 명시적으로 계산하면서 토양수분과 연결하는 모델이 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- ForSAFE + Veg 통합 모델 평가

# 공간 구조
- forest site/plot 기반
- 본 논문 자체는 연결된 2D terrain model이 아님
- ForSAFE-2D 계열과 결합 가능한 동일 model family

# 적용 환경
- 미국 북동부 활엽수림
- Hubbard Brook Experimental Forest
- Bear Brook Watershed in Maine

# 핵심 과정
- ForSAFE: tree photosynthesis, growth, phenology, transpiration, nutrient uptake, litter decomposition, soil hydrology, soil chemistry
- Veg: herbaceous understory plant-community composition
- Veg는 soil moisture, soil solution N, pH, light, temperature를 이용
- species 간 competition은 rooting depth와 shading height를 통해 반영

# 식생 입력
- tree biomass 및 tree nutrient state
- ground vegetation species-specific niche/trait parameters
- rooting depth
- shading height
- moisture, N, pH, light tolerance

# 핵심 식
Veg의 각 환경 driver에 대한 species response는 Gaussian response로 기술되며, site suitability는 pH, N, soil moisture, light response를 결합한다.

# 파라미터와 단위
- herbaceous layer는 최대 약 1.8 m 높이 범위로 정의
- species cover를 상태/검증 변수로 사용
- plant niches는 light, water, N, pH 및 경쟁 관련 trait로 parameterize
- 본 연구에서는 Veg species-level parameter의 calibration이 필요했음

# 원 논문의 구현 범위
- 45 ground-vegetation species의 상대 피복을 포함한 understory community composition
- tree biomass, soil solution chemistry와 함께 장기 변화 모의
- 하층식생이 단순 고정 cover가 아니라 환경 및 경쟁에 따라 동적으로 바뀜

# 고운사에 직접 사용할 수 있는 부분
- 기준 2의 중요한 비교근거: explicit understory species composition
- soil moisture/light/rooting depth/shading competition으로 하층식생 반응을 계산하는 구조
- 산불 후 초기 초본 및 관목성 하층식생의 environmental filtering을 설계할 때 참고 가능

# 새로운 coupling이 필요한 부분
- age/size cohort demography
- 산불 후 seedbank, recruit cohort, shrub/tree cohort succession과의 연결
- geomorphic event 후 soil geometry/state remapping
- ForSAFE-2D와 고운사 erosion/topography engine의 state exchange

# 한계
- Veg는 demographic cohort engine이 아니라 species cover/community model이다.
- tree component도 고운사에서 원하는 spatial cohort demography와 다르다.
- species-specific ground vegetation 결과는 calibration에 민감했다.

# 최종 판정
- 보조근거
- criterion 2의 좋은 understory-process comparator
- strict production vegetation engine으로는 criterion 1 부족

# 참고 링크 / DOI
- https://doi.org/10.1007/s11270-019-4145-6
