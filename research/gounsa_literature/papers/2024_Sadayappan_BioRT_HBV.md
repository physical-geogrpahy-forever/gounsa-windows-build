# 서지정보
Sadayappan, K., Stewart, B., Kerins, D., et al. (2024). BioRT-HBV 1.0: A Biogeochemical Reactive Transport Model at the Watershed Scale. *Journal of Advances in Modeling Earth Systems, 16*, e2024MS004217. DOI: 10.1029/2024MS004217.

# 이 논문을 찾은 이유
full distributed RTM보다 단순하면서도 weathering, root respiration, DOC/DIC, soil moisture/temperature dependence를 포함하는 저비용 watershed model이 있는지 확인하기 위해 검토했다.

# 연구 유형
- parsimonious watershed reactive transport model
- HBV hydrology + biogeochemical reaction network

# 공간 구조
- spatially implicit bucket-type watershed
- shallow zone
- deep zone
- groundwater / stream connection

# 적용 환경
- headwater catchment
- hydro-biogeochemical modeling

# 핵심 과정
- chemical weathering
- mineral dissolution / precipitation
- soil respiration
- root respiration
- root exudate contribution to DOC/DIC
- nutrient transformation
- ion exchange
- surface complexation
- solute transport

# 식생 입력
- root respiration/exudate source terms
- potential evapotranspiration indirectly through HBV hydrology
- vegetation cover/forest dynamics itself is not prognostic DGVM state

# 핵심 식
General environmental reaction-rate form:

```
r
=
k A
f(T)
f(Sw)
f(Zw)
```

where:
- r: reaction rate [mol m^-3 s^-1]
- k: rate constant [mol m^-2 s^-1]
- A: reactive surface area [m2 m^-3]
- T: temperature
- Sw: soil water saturation/moisture state
- Zw: water-table state

Weathering uses TST-type form:

```
r
=
k A_mineral a^m
(1 - IAP / K_eq)
```

Carbon reaction network includes root respiration/exudate source terms coupled to shallow-zone DOC/DIC.

# 파라미터와 단위
- k [mol m^-2 s^-1]
- reactive surface area [m2 m^-3 or mineral-specific basis]
- soil moisture
- water table
- Q10 / temperature dependence
- DOC/DIC and root respiration source terms

# 원 논문의 구현 범위
minimal-data watershed RTM with explicit weathering and soil/root respiration chemistry.

# 고운사에 직접 사용할 수 있는 부분
WITCH/PROFILE 또는 BioRT-Flux-PIHM의 복잡성이 지나칠 경우, reaction-law prototyping과 sensitivity test에 유용하다.

특히:
```
T
+ soil moisture
+ water-table state
+ root respiration / DOC
 -> weathering
```
의 구현식을 명확하게 제공한다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root respiration, litter/SOM, runoff state를 BioRT-HBV state에 넣는 것은 새로운 coupling이다.

# 한계
- spatially implicit
- PFT/root architecture 없음
- hillslope topography and lateral heterogeneity representation이 단순함

# 최종 판정
- **보조 채택: parsimonious reaction-law benchmark**
- production spatial engine보다는 검증 및 sensitivity에 적합

# 참고 링크 / DOI
https://doi.org/10.1029/2024MS004217
