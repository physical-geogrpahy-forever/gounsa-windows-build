# 서지정보
Braga, A., Martínez-Aranda, S., & García-Navarro, P. (2026). *Evaluation of the Performance of a Finite Volume Physics-Based Model for Soil Erosion Simulation*. Water, 18(15), 1870. DOI: 10.3390/w18151870.

# 이 논문을 찾은 이유
SERGHEI-SE의 최신 finite-volume hydro-erosive implementation과 성능을 확인하고 고운사 2D 엔진 후보인지 평가하기 위해 검토했다.

# 연구 유형
- physics-based numerical model evaluation

# 공간 구조
- genuine 2D shallow-water equations
- 2D depth-averaged solid transport
- bed evolution
- finite-volume discretization

# 적용 환경
- analytical hillslope
- V-catchment rainfall-runoff benchmark
- laboratory erodible-bed test
- catchment-scale application을 염두에 둔 framework

# 핵심 과정
- runoff generation
- sediment mobilization
- solid transport
- deposition
- bed evolution

# 식생 입력
이 논문에서 dynamic root biomass 또는 RLD가 core erosion parameter로 직접 들어가는 구조는 확인되지 않았다.

# 핵심 식
2D shallow-water, solid-transport, bed-evolution PDE system을 결합한다. 정확한 식은 원문을 따른다.

# 파라미터와 단위
erosion/transport parameters와 finite-volume numerical parameters. 정확한 값과 단위는 원문 표를 따른다.

# 원 논문의 구현 범위
SERGHEI-SE finite-volume erosion solver의 numerical accuracy, conservation, stability를 평가한다.

# 고운사에 직접 사용할 수 있는 부분
- 최신 genuine 2D hydro-erosion engine 비교후보
- high-resolution catchment 계산용 HPC/finite-volume architecture

# 새로운 coupling이 필요한 부분
LPJ-GUESS root/litter quantities를 erosion parameters에 연결하면 **새로운 coupling**이다.

# 한계
strict quantitative vegetation-state 조건을 만족하지 않는다.

# 최종 판정
**2D 엔진 비교후보.** vegetation bridge는 별도 필요.

# 참고 링크 / DOI
10.3390/w18151870
