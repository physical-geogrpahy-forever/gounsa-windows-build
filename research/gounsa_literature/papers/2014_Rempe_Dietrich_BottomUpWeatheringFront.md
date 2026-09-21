# 서지정보
Rempe, D. M., & Dietrich, W. E. (2014). A bottom-up control on fresh-bedrock topography under landscapes. *Proceedings of the National Academy of Sciences, 111*(18), 6576-6581. DOI: 10.1073/pnas.1404763111.

# 이 논문을 찾은 이유
사면의 weathering-front depth가 위에서 내려오는 infiltration만으로 결정되는지, 아니면 channel incision과 groundwater drainage가 아래에서 제어하는지 확인하기 위해 검토했다.

# 연구 유형
- analytical hillslope model
- field comparison
- Critical Zone weathering-front theory

# 공간 구조
- soil-mantled hillslope
- surface topography
- fresh-bedrock boundary
- groundwater/drainage profile
- divide-to-channel geometry

# 적용 환경
- actively eroding hillslopes
- field comparisons at multiple sites

# 핵심 과정
- channel incision
- bedrock uplift/exhumation
- groundwater drainage
- weathering-front position
- fresh-bedrock topography
- hillslope geometry

# 식생 입력
explicit vegetation state는 없다.

하지만 fresh bedrock가 drainage된 뒤:
- atmospheric acids/oxidants
- biotically controlled acids/oxidants
가 접근하여 weathering이 가능해진다는 구조를 가진다.

고운사에서는 식생이 weathering-front 위치를 직접 정하는 것이 아니라, drainage 후 반응환경을 조절하는 별도 경로로 처리한다.

# 핵심 가설
fresh bedrock 내부의 stagnant/equilibrated pore water가 channel incision-induced hydraulic gradient로 배수되면:

```
fresh bedrock drainage
 -> reactive meteoric water / gases can enter
 -> weathering begins
```

따라서:
```
uppermost undrained fresh bedrock
```
가 weathering front의 bottom-up control이 될 수 있다.

# 핵심 결과
weathered-zone thickness:

```
Z_surface - Z_fresh_bedrock
```

는 surface topography와 groundwater/drainage geometry의 coupling으로 예측된다.

모델은:
- divide toward channel weathered-zone thinning
- upslope increase in bedrock residence within weathered zone
을 예측한다.

중요한 spatial controls:
- channel incision rate
- hillslope dimensions
- bedrock hydraulic conductivity / porosity
- groundwater gradient

# 고운사에 직접 사용할 수 있는 부분
고운사의 weathering-front model에서:

```
top-down vegetation/hydrology
```
만으로 Z_weathered를 계산하지 않을 근거.

특히:
```
channel / drainage-base elevation
groundwater / deep drainage state
```
를 bottom-up boundary condition으로 고려할 수 있다.

100년 model에서는 inherited weathering profile을 초기조건으로 두고:
- water-table/deep-flow variations
- incremental weathering
만 갱신하는 현재 방향과 잘 맞는다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS vegetation/hydrology와:
- bedrock drainage
- weathering-front chemistry
를 연결하는 것은 NEW COUPLING이다.

# 한계
- steady-state analytical theory
- reaction kinetics 단순화
- vegetation explicit 없음
- sandstone-specific 아님
- groundwater table = complete reaction-front control assumption은 site-dependent

# 최종 판정
- **핵심 채택: bottom-up weathering-front boundary model**
- top-down infiltration/vegetation control과 별도 sensitivity로 유지
- water table을 weathering front와 무조건 동일시하지 않음

# 참고 링크 / DOI
https://doi.org/10.1073/pnas.1404763111
