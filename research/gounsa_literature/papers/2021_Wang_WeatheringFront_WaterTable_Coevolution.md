# 서지정보
Wang, W., et al. (2021). Coevolution of Weathering Front and Water Table. *Geophysical Research Letters, 48*, e2021GL092916. DOI: 10.1029/2021GL092916.

# 이 논문을 찾은 이유
bottom-up Rempe-Dietrich model과 top-down infiltration model 중 하나를 고운사에 고정해야 하는지, 아니면 weathering front와 water table을 독립적이고 coevolving한 상태로 둬야 하는지 확인하기 위해 검토했다.

# 연구 유형
- geophysical/weathering-profile analysis
- conceptual and process-model comparison
- transient Critical Zone interpretation

# 공간 구조
- ridge/weathering profile
- weathering front
- water table
- fractured/weathered zone

# 적용 환경
- mountain Critical Zone
- subsurface geophysical constraints

# 핵심 과정
- top-down infiltration/percolation
- bottom-up groundwater drainage
- weathering-induced porosity
- fracture connectivity
- weathering-front propagation
- water-table evolution

# 식생 입력
explicit vegetation model 없음.

고운사에서는 vegetation이:
- infiltration/recharge
- root water uptake
- CO2/reactivity
를 통해 top-down pathway에 작용할 수 있다.

# 핵심 이론구분

### bottom-up
Rempe & Dietrich:
```
drainage of equilibrated groundwater
 -> fresh bedrock becomes reactive
 -> weathering-front position
```

### top-down
Lebedeva/Brantley lineage:
```
reactive meteoric water / O2
 -> downward percolation
 -> reaction-front advance
```

# 핵심 결과
weathering front와 water table이 systematic하게 일치하지 않을 수 있다.

이것은 bottom-up mechanism을 부정한다기보다:
```
weathering-front system
= transient / coevolving
```
일 수 있음을 의미한다.

Weathering creates porosity/permeability which in turn changes infiltration, producing positive feedback.

```
weathering
 -> porosity/connectivity
 -> infiltration
 -> more weathering
```

초기 fracture density 차이가 이 feedback을 증폭할 수 있다.

# 고운사에 직접 사용할 수 있는 부분
중요한 state-separation rule:

```
Z_water_table
!=
Z_weathering_front
```

둘을 별도 state로 유지한다.

또:
```
fracture/permeability state
```
를 단순 lithology constant가 아니라 weathering과 함께 변할 수 있는 sensitivity state로 볼 근거가 된다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS-driven infiltration/root uptake를:
- transient water table
- top-down weathering
에 연결하고,
Landlab profile evolution을:
- porosity/permeability
와 연결하면 NEW COUPLING이다.

# 한계
- vegetation explicit 없음
- specific field geology
- full postfire model 아님
- quantitative Gounsa coefficients 제공 안 함

# 최종 판정
- **채택: water-table/weathering-front state separation and coevolution constraint**
- top-down vs bottom-up을 단일 hard rule로 고정하지 않는다
- first production에서 full dynamic permeability가 어렵다면 sensitivity로 유지

# 참고 링크 / DOI
https://doi.org/10.1029/2021GL092916
