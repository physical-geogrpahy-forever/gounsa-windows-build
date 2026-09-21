# 서지정보
Yu, L., Zanchi, G., Akselsson, C., Wallander, H., & Belyazid, S. (2018). Modeling the forest phosphorus nutrition in a southwestern Swedish forest site. Ecological Modelling, 369, 88-100.
DOI: 10.1016/j.ecolmodel.2017.12.018

# 이 논문을 찾은 이유
고운사에서 필요한 식생-수분-양분-광물풍화의 양방향 feedback이 실제 forest ecosystem model에 구현된 사례인지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- dynamic forest ecosystem / biogeochemistry model
- ForSAFE에 phosphorus cycle module을 통합

# 공간 구조
- forest stand / layered soil profile
- 1D vertical soil representation
- 2D hillslope lateral routing 없음

# 적용 환경
- southern Sweden spruce forest
- 장기 forest nutrient dynamics

# 핵심 과정
- tree growth
- soil hydrology
- litter and SOM decomposition
- soil chemistry
- mineral weathering
- nutrient uptake
- litter return
- P mineralization
- sorption/desorption
- atmospheric deposition
- nutrient limitation feedback

# 식생 입력
- dynamic tree biomass and growth
- nutrient demand and uptake
- litter production and return
- water demand
- nutrient/water availability에 의해 actual growth가 제한됨

# 핵심 식
핵심은 단일 weathering 식이 아니라 coupled ecosystem mass balance이다.

tree growth -> water/nutrient demand -> soil uptake
weathering + deposition + decomposition -> soil nutrient availability -> tree growth
tree growth -> litter return -> soil chemistry

ForSAFE weathering은 PROFILE/SAFE lineage의 mineral-specific kinetic weathering을 동적으로 사용한다.

# 파라미터와 단위
- modeled plant P uptake: 약 0.50 g P m-2 yr-1
- 그중 약 80%는 mineralization
- 나머지 약 20%는 deposition + weathering의 net input
- 그 net input에서 weathering이 약 2/3를 담당한다고 모델이 추정

# 원 논문의 구현 범위
- ForSAFE에 P cycle을 실제 구현
- measured soil-water chemistry, tree biomass, biomass nutrient concentration과 비교
- nutrient limitation과 soil biogeochemistry를 동적으로 연결
- weathering-derived nutrient가 vegetation growth에 feedback

# 고운사에 직접 사용할 수 있는 부분
1. 현재까지 가장 직접적인 dynamic forest vegetation <-> mineral weathering model precedent 중 하나.
2. LPJ-GUESS를 vegetation engine으로 유지하더라도 water/nutrient demand, uptake, litter return, chemistry를 연결하는 interface 설계에 직접 참고 가능.
3. weathering nutrient release -> vegetation uptake -> litter return -> soil chemistry를 mass-conserved coupling으로 구현하는 근거.

# 새로운 coupling이 필요한 부분
- ForSAFE의 vegetation engine을 LPJ-GUESS로 대체하는 것은 NEW COUPLING.
- vertical stand hydrology를 고운사 shallow/deep/lateral hillslope flow로 확장하는 것도 NEW COUPLING.
- erosion/deposition/fresh-mineral supply와 연결하는 것도 별도 coupling.

# 한계
- 2D hillslope model 아님.
- 지형진화 없음.
- postfire erosion/spall 없음.
- Swedish spruce parameter를 고운사에 직접 전이할 수 없음.

# 최종 판정
- 강하게 채택
- 역할: forest vegetation-hydrology-nutrient-weathering feedback architecture의 핵심 published model precedent.

# 참고 링크 / DOI
- https://doi.org/10.1016/j.ecolmodel.2017.12.018