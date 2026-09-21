# 서지정보
Kronnäs, V., Akselsson, C., & Belyazid, S. (2019). Dynamic modelling of weathering rates – the benefit over steady-state modelling. *SOIL, 5*, 33-47. DOI: 10.5194/soil-5-33-2019.

# 이 논문을 찾은 이유
ForSAFE의 실제 dynamic weathering에서 식생과 수문 피드백이 어떤 변수로 weathering rate를 바꾸는지 확인하기 위해 검토했다.

# 연구 유형
- dynamic numerical model comparison
- PROFILE vs ForSAFE

# 공간 구조
- layered forest soil profile

# 적용 환경
- southern Sweden spruce forests

# 핵심 과정
- mineral weathering
- soil moisture and temperature
- runoff
- tree nutrient uptake
- litter decomposition
- soil chemistry
- forest management / clearcut effects

# 식생 입력
- tree uptake
- litterfall and decomposition
- forest growth
- dynamically simulated hydrology

# 핵심 식
ForSAFE weathering equations are the PROFILE equations but dynamic.

Weathering responds to:
- soil temperature
- soil moisture
- mineralogy
- exposed mineral surface area
- soil density
- H+
- organic ligands
- CO2
- base-cation and Al inhibition

ForSAFE dynamically models several variables that PROFILE treats as inputs, including runoff, soil moisture, litter decomposition and tree nutrient uptake.

# 파라미터와 단위
원 논문에서 monthly timestep ForSAFE 사용.
weathering fluxes are reported for base cations and individual layers.

# 원 논문의 구현 범위
forest rotation 동안 seasonal, interannual and decadal weathering changes를 계산하며 PROFILE steady-state 결과와 비교한다.

# 고운사에 직접 사용할 수 있는 부분
산불 후 식생 소실/회복이:
```
transpiration
soil moisture
soil temperature
litter decomposition
nutrient uptake
soil solution chemistry
```
를 통해 weathering을 변화시킬 수 있다는 published dynamic forest-model precedent.

# 새로운 coupling이 필요한 부분
LPJ-GUESS outputs를 PROFILE-style weathering kinetics에 입력하는 것은 새 coupling이다.

# 한계
- Scandinavian forest chemistry
- sandstone-specific parameterization 아님
- lateral geomorphology 없음

# 최종 판정
- **채택: dynamic forest vegetation-weathering feedback의 강한 근거**
- B-WITCH와 함께 고운사 chemical-weathering interface 설계에 사용

# 참고 링크 / DOI
https://doi.org/10.5194/soil-5-33-2019
