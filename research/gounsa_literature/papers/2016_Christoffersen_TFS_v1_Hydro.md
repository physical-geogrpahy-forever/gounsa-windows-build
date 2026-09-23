# 서지정보
Christoffersen, B. O., Gloor, M., Fauset, S., et al. (2016). Linking hydraulic traits to tropical forest function in a size-structured and trait-driven model (TFS v.1-Hydro). Geoscientific Model Development, 9, 4227-4255. https://doi.org/10.5194/gmd-9-4227-2016

# 이 논문을 찾은 이유
고운사 식생엔진 후보 중 size structure와 시간단위 plant hydraulics를 동시에 가진 모델이 있는지 확인하기 위해 검토했다.

# 연구 유형
수치모델 / 방법론

# 공간 구조
stand-scale, PPA 기반 수직 size structure. 실제 x-y 지형격자나 유역 연결은 없음.

# 적용 환경
열대림 drought / plant hydraulics

# 핵심 과정
- PPA 기반 수관 광경쟁
- individual tree size/trait distribution
- hourly soil-root-stem-canopy water flux
- photosynthesis, stomatal conductance
- daily C allocation

# 식생 입력
- tree size
- wood density, LMA, leaf N/P
- fine/coarse root biomass
- rooting depth
- hydraulic traits

# 핵심 식
Richards-type soil-plant hydraulic mass balance를 hourly로 풀고 transpiration과 stomatal conductance를 양방향으로 연결한다.

# 파라미터와 단위
wood density, leaf mass per area, hydraulic conductivity, P50, capacitance, rooting depth 등 측정가능한 hydraulic/structural traits.

# 원 논문의 구현 범위
논문 버전은 hourly hydraulics와 daily allocation을 구현했지만, 장기 수목 성장에 따라 allometric hydraulic properties를 계속 갱신하는 기능은 완성되지 않았다. 저자들도 1년 이상 장기 적용에는 해당 기능이 필요하다고 명시한다.

# 고운사에 직접 사용할 수 있는 부분
- size-dependent root/plant hydraulics 설계
- storm/drought 직후 hourly physiological response benchmark
- fine-root/coarse-root와 plant hydraulic resistance 연결

# 새로운 coupling이 필요한 부분
- 장기 recruitment/mortality/succession
- shrub/herb demographic layer
- actual terrain/catchment cells
- lateral hydrology
- erosion/deposition soil-depth update

# 한계
고운사의 100년 postfire herb-shrub-tree succession engine으로는 불완전하다. 열대 교목 중심이며 understorey herb/shrub demography가 없다.

# 최종 판정
보조근거 / plant-hydraulics benchmark

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-9-4227-2016
