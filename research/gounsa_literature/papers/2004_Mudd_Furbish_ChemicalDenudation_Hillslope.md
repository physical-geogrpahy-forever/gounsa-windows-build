# 서지정보
Mudd, S. M., & Furbish, D. J. (2004). Influence of chemical denudation on hillslope morphology. *Journal of Geophysical Research: Earth Surface, 109*(F2), F02001. DOI: 10.1029/2003JF000087.

# 이 논문을 찾은 이유
고운사에서 chemical weathering을 단순 용존 손실로만 두지 않고, 사면의 토양질량수지와 지형형태에 실제로 어떻게 연결해야 하는지 확인하기 위해 검토했다.

# 연구 유형
- theoretical hillslope model
- depth-integrated mass conservation
- steady-state morphology analysis

# 공간 구조
- 1D hillslope
- soil mantle
- soil production
- diffusive lateral transport
- chemical denudation/deposition

# 적용 환경
- generic soil-mantled hillslopes

# 핵심 과정
- soil production
- mechanical hillslope transport
- chemical denudation/deposition
- spatial variation in chemical mass loss
- hillslope morphology

# 식생 입력
explicit vegetation state는 없다.

따라서 식생모델 근거가 아니라:
```
chemical weathering
<-> hillslope mass balance
<-> morphology
```
를 연결하는 이론적 backbone으로 사용한다.

# 핵심 식/구조
논문은 기존 soil-thickness/elevation continuity에 chemical mass-loss term을 추가한 depth-integrated soil-mass conservation equation을 유도한다.

개념적으로:

```
soil mass change
=
soil production
- divergence of mechanical soil transport
- chemical denudation
+ chemical deposition
```

steady-state 1D hillslope에서 chemical denudation의 downslope spatial gradient가 존재하면 단순 diffusion-only parabolic profile에서 벗어날 수 있다.

특정 조건에서는 convex-concave steady-state hillslope가 가능하다.

# 핵심 결과
```
spatially varying chemical denudation
 -> hillslope-form change
```

즉 W_chem은 단순한 local diagnostic이 아니라 장기적으로 z/H에 영향을 줄 수 있는 질량수지항이다.

또 chemical denudation과 mechanical denudation의 상대크기가 hillslope morphology를 바꾼다.

# 고운사에 직접 사용할 수 있는 부분
현재 mobile-soil balance:

```
dM_AB/dt
=
rho_parent P_sand
+ deposition
- physical erosion
- W_chem
```

에 대한 강한 이론적 선례다.

또:
```
vegetation
 -> hydrology / CO2
 -> spatial W_chem
 -> H / z
 -> vegetation
```
feedback에서 W_chem이 실제 지형상태를 갱신해야 함을 지지한다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS vegetation/hydrology가 chemical denudation spatial pattern을 만들도록 하는 것은 새로운 coupling이다.

# 한계
- vegetation 없음
- 1D
- steady-state 중심
- mineral reaction network 없음
- 100년 postfire transient model 아님

# 최종 판정
- **핵심 채택: chemical-denudation hillslope mass-balance backbone**
- production chemistry engine이 아니라 Landlab mass balance와 W_chem 연결 근거

# 참고 링크 / DOI
https://doi.org/10.1029/2003JF000087
