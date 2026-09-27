# 서지정보
Monsalve, A. D., Anderson, S. R., Gasparini, N. M., & Yager, E. M. (2025). RiverBedDynamics v1.0: a Landlab component for computing two-dimensional sediment transport and river bed evolution. *Geoscientific Model Development, 18*, 3427–3451. https://doi.org/10.5194/gmd-18-3427-2025

# 이 논문을 찾은 이유
고운사에서 1시간 단위 외부 forcing과 결합 가능한 최신 2D 표면 입도분포 transport engine이 있는지 확인하기 위해 검토했다.

# 연구 유형
- Landlab component/model description
- physically based 2D sediment transport and morphodynamics
- analytical/benchmark validation + synthetic watershed demonstration

# 공간 구조
- genuine 2D raster grid
- `OverlandFlow`와 동적 결합
- channelized flow와 unchannelized overland flow에 동일한 shear-stress/transport framework를 적용할 수 있다고 설명

# 적용 환경
- 주 대상은 gravel-bed river와 watershed
- hillslope overland-flow 적용 가능성을 명시하지만, steep forest hillslope에 대한 직접 검증은 없음

# 핵심 과정
- non-steady 2D overland flow
- local shear stress
- grain-size-specific bed-load transport
- erosion/deposition
- active-layer grain-size evolution
- substrate stratigraphy tracking
- surface elevation update

# 표면 입도 상태
각 node에서 grain-size distribution을 저장하고 `D50`, geometric mean, geometric standard deviation 등을 계산한다. 입도별 Exner mass balance를 이용해 active-layer GSD를 갱신한다.

# 시간 구조
- component 자체는 short-term hours to years를 주요 적용범위로 제시
- published test에서는 내부 최대 timestep이 수 초 수준인 경우가 있음
- synthetic watershed 예는 24시간 rainfall experiment를 수행
- 따라서 `1-hour external forcing / coupling interval`과 결합하는 것은 구조적으로 가능하지만, solver 내부 timestep 자체가 1시간인 모델은 아니다.

# 수문
- `OverlandFlow`와 결합해 수심, 유속, 유량을 계산
- **infiltration module은 RiverBedDynamics v1.0 자체에 없음**
- 논문 본문에서 infiltration을 구현하거나 surface GSD로 hydraulic conductivity를 갱신하지 않음

# 풍화
- **없음**
- fragmentation/weathering에 의한 parent-to-daughter grain-size conversion을 제공하지 않음

# 표면입도와 수리 피드백
- GSD는 sediment mobility/critical shear/transport 계산에 직접 사용됨
- Manning roughness는 published tests에서 외생값이며, 저자들은 future enhancement로 bed grain properties와 water depth에 따른 time-varying roughness를 제안
- 즉 현재 GSD -> roughness feedback은 구현되어 있지 않음

# 고운사에 직접 사용할 수 있는 부분
- 최신 genuine 2D surface GSD transport/deposition engine
- 입도별 질량보존과 active-layer sorting
- 시간가변 rainfall/flow에 따른 grain-size-specific transport
- Landlab 기반이라 Shmilovitz fragmentation이나 SoilInfiltrationGreenAmpt 등과 software coupling하기 쉬움

# 새로운 coupling이 필요한 부분
- infiltration
- surface GSD/rock cover -> infiltration hydraulic parameters
- physical weathering / fragmentation
- dry ravel / hillslope particle runout
- LPJ-GUESS vegetation
- fire-spall PSD supply
- steep forest hillslope parameterization

# 한계
- 주 검증대상은 gravel-bed rivers
- infiltration 없음
- weathering/fragmentation 없음
- macro-roughness boulder/vegetation effects 미구현
- steep mountain rivers에 대해서도 저자들이 추가 transport equations를 future refinement로 제시

# 최종 판정
- **2025년 기준 가장 강한 2D dynamic surface-GSD transport 후보 중 하나**
- 고운사 전체 표면암편 모델 하나로는 불충분
- 특히 `풍화`와 `침투`가 없어 단독 채택 불가
- 다만 고운사의 2D 입도별 이동/퇴적 module 후보로는 Shmilovitz 2024보다 공간구조 면에서 우수

# 코드
Source code archived on Zenodo as RiverBedDynamics v1.0.

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-18-3427-2025
