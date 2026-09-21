# 서지정보
Hodges, C., Kim, H., Brantley, S. L., & Kaye, J. (2019). Soil CO2 and O2 Concentrations Illuminate the Relative Importance of Weathering and Respiration to Seasonal Soil Gas Fluctuations. Soil Science Society of America Journal, 83, 1167-1180.
DOI: 10.2136/sssaj2019.02.0049

# 이 논문을 찾은 이유
고운사 사암 산림사면에서 `root respiration -> soil pCO2 -> chemical weathering` 경로를 hillslope position, lithology, depth와 함께 다룰 수 있는 직접 현장근거를 찾기 위해 검토했다.

# 연구 유형
- 현장 관측 / 토양가스 시계열
- 수치모델 아님

# 공간 구조
- 하나의 shale watershed와 하나의 sandstone watershed에서 catena를 따라 관측
- 각 지점에서 지표부터 기반암까지 3개 깊이의 soil gas를 관측
- 3개 growing season에 걸친 반복 관측
- genuine 2D 모델이 아니라 hillslope-position 비교 관측

# 적용 환경
- 미국 Pennsylvania의 humid temperate forest
- Susquehanna Shale Hills Critical Zone Observatory
- sandstone / shale 비교

# 핵심 과정
- root 및 soil respiration
- gas diffusion
- soil pCO2 / pO2
- seasonal saturation / reducing microsites
- silicate weathering과 respiration 신호의 분리
- hillslope position effect

# 식생 입력
- 직접적인 biomass 또는 RLD 입력은 없음
- sandstone 쪽의 더 높은 macroporosity가 깊은 root respiration을 허용한 것으로 해석
- 따라서 식생효과는 관측된 soil gas state를 통해 간접적으로 나타남

# 핵심 식
논문의 핵심 진단량은 apparent respiratory quotient, ARQ이다.
본 archive에서는 원문의 정확한 계산식을 재구성해 이식하지 않고, 다음 관찰적 의미만 사용한다.
- aerobic respiration + diffusion이 지배하면 ARQ가 1에 가까움
- ARQ가 1에서 벗어나면 respiration 외 weathering/redox 과정이 soil gas budget에 중요할 수 있음

# 파라미터와 단위
- soil pCO2: 부피 농도, %
- soil pO2: 부피 농도, %
- valley floor에서 pCO2 > 5%
- valley floor에서 pO2 < 16%
- anaerobic microsite respiration 추정 기여: 약 36 g C m^-2 yr^-1
- ARQ: 무차원

# 원 논문의 구현 범위
- soil gas의 lithology, hillslope position, depth, season 효과를 관측적으로 분리
- sandstone watershed에서 동일 깊이 기준 pCO2가 더 높고 pO2가 더 낮았음
- 저자들은 sandstone의 더 큰 macroporosity와 깊은 root respiration을 중요한 원인으로 해석
- late growing season의 습윤한 microsite에서 anaerobic respiration 가능성을 제시

# 고운사에 직접 사용할 수 있는 부분
1. `R_CO2 != pCO2`를 유지해야 한다.
2. pCO2는 vegetation state뿐 아니라 porosity, gas diffusivity, depth, saturation, hillslope position의 결과 상태여야 한다.
3. 사암은 광물반응뿐 아니라 macropore/root-access architecture를 통해 깊은 CO2 source를 바꿀 수 있다.
4. valley/footslope의 높은 수분상태에서는 O2 제한 및 redox 상태도 weathering context에 포함할 필요가 있다.

# 새로운 coupling이 필요한 부분
`LPJ-GUESS root/belowground respiration by depth -> soil gas transport/state -> pCO2(z), pO2(z) -> chemical weathering` 연결은 고운사에서 새로 구현해야 한다.
첫 구현에서는 full gas transport를 강제하지 않더라도, 최소한 respiration source와 gas state를 별도 변수로 유지한다.

# 한계
- 직접적인 chemical weathering rate를 산출한 논문이 아니다.
- sandstone의 구체 petrography와 고운사 사암은 동일하지 않다.
- macroporosity -> deeper root respiration 해석은 현장자료에 기반한 저자 해석이며 범용 계수로 옮길 수 없다.
- root biomass, FineRootC, root depth의 직접 정량관측을 LPJ-GUESS 형식으로 제공하지 않는다.

# 최종 판정
- 채택
- 역할: sandstone forest에서 lithology + hillslope position + depth + soil gas + root respiration을 연결하는 process evidence
- 계수 전이는 금지

# 참고 링크 / DOI
- https://doi.org/10.2136/sssaj2019.02.0049