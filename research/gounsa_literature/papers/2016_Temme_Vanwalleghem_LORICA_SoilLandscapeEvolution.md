# 서지정보
Temme, A. J. A. M., & Vanwalleghem, T. (2016). LORICA - A new model for linking landscape and soil profile evolution: Development and sensitivity analysis. Computers & Geosciences, 90, 131-143.
DOI: 10.1016/j.cageo.2015.08.004

# 이 논문을 찾은 이유
고운사에서 필요한 사면 지형진화 + soil-profile evolution + chemical weathering이 실제 하나의 numerical model 안에서 함께 계산되는 사례인지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- soil-landscape evolution model
- sensitivity analysis

# 공간 구조
- raster DEM
- 각 grid cell 아래에 multiple soil layers
- vertical pedogenic processes + lateral geomorphic transport
- LAPSUS landscape model과 MILESD soil formation model 계보 결합

# 적용 환경
- 일반 soil-landscape coevolution framework
- 특정 산불 산림사면 전용 모델은 아님

# 핵심 과정
- erosion/deposition
- soil creep
- soil-profile evolution
- physical/chemical weathering
- clay/fine-particle redistribution
- armouring
- vegetation protection feedback on erosion
- soil property -> geomorphic process feedback
- geomorphic redistribution -> soil/weathering feedback

# 식생 입력
- vegetation은 landscape-evolution component에서 erosion에 negative feedback/protection을 제공
- LPJ-GUESS 같은 biomass/PFT/succession model은 아님
- quantitative root biomass, RLD, respiration, root water uptake 없음

# 핵심 식
논문의 핵심은 단일식보다 soil mass/profile과 lateral landscape transport를 같은 grid framework에서 갱신하는 구조이다.

soil development -> soil texture/profile -> erodibility/transport
erosion/deposition -> soil profile/mineral distribution -> chemical weathering

민감도 분석에서는 erosion 관련 변수가 chemical weathering 양에도 영향을 주었다.

# 파라미터와 단위
- model sensitivity analysis 중심
- soil layers와 grain-size/organic matter state를 cell별로 저장
- transferable sandstone-specific coefficient는 제공하지 않음

# 원 논문의 구현 범위
- soil profile와 landscape surface가 동시에 진화
- surface change가 soil development에 의존
- soil development가 landscape location과 redistribution history에 의존
- vegetation protection, armouring, particle-size selectivity를 erosion/deposition에 포함
- chemical weathering이 geomorphic redistribution과 연결됨

# 고운사에 직접 사용할 수 있는 부분
1. chemical weathering을 cell-local 독립 column으로만 두지 않고 erosion/deposition과 다시 연결하는 published model precedent.
2. grid cell별 multi-layer soil state와 DEM evolution을 동시에 유지하는 구조.
3. erosion -> mineral redistribution -> weathering feedback을 실제 soil-landscape model에서 구현한 사례.

# 새로운 coupling이 필요한 부분
- LORICA의 단순 vegetation protection을 LPJ-GUESS biomass/root state로 대체하는 것은 NEW COUPLING.
- root respiration, root water uptake, nutrient cycling을 chemical weathering에 연결하려면 별도 coupling 필요.
- 산불 후 SWEHR/LPJ-GUESS와 연결하는 것도 새 coupling.

# 한계
- dynamic forest vegetation model 아님.
- vegetation effect가 주로 erosion protection에 한정.
- root-mediated chemical weathering 없음.
- 고운사 100년 산불 후 사암 parameterization 없음.

# 최종 판정
- 강한 보조 채택
- 역할: soil-landscape-chemical-weathering coevolution의 핵심 spatial model precedent.
- vegetation-weathering 자체의 최종 모델은 아님.

# 참고 링크 / DOI
- https://doi.org/10.1016/j.cageo.2015.08.004