# 서지정보
Ferrier, K. L., & Perron, J. T. (2020). The Importance of Hillslope Scale in Responses of Chemical Erosion Rate to Changes in Tectonics and Climate. *Journal of Geophysical Research: Earth Surface, 125*(9), e2020JF005562. DOI: 10.1029/2020JF005562.

# 이 논문을 찾은 이유
사면의 공간규모 자체가 chemical weathering/chemical erosion의 transient response를 어떻게 제약하는지 확인하고, 고운사 100년 모델에서 cell-local chemistry만으로 충분한지 검토하기 위해 읽었다.

# 연구 유형
- 3D landscape evolution + chemical weathering numerical model
- transient perturbation experiments

# 공간 구조
- first-order soil-mantled basins
- evolving 3D topography
- soil thickness field
- soil mineral abundance field
- downslope soil transport

# 적용 환경
- idealized soil-mantled landscapes
- tectonic/climatic perturbation experiments

# 핵심 과정
- rock uplift
- soil production
- diffusive soil transport
- mineral dissolution
- secondary mineral production
- chemical erosion
- physical erosion
- topographic evolution

# 식생 입력
explicit vegetation model은 없다.

그러나 논문은 hillslope response time이:
- soil transport efficiency
- river incision efficiency
에 의해 결정될 수 있고, 이 둘은 climate와 biota에 의해 영향을 받을 수 있다고 논의한다.

따라서 고운사에서는 vegetation이:
- soil production
- hillslope transport
- hydrology
를 바꾸어 chemical-erosion response time에 간접적으로 작용할 수 있다.

# 핵심 coupling
논문은 soil chemical weathering을 landscape evolution model에 직접 결합한다.

개념적으로:

```
bedrock lowering / soil production
 -> H

H + topographic gradient
 -> soil transport

soil mineral abundance
 + dissolution
 + transport
 -> chemical erosion

chemical erosion
 -> H / surface elevation

H / z / gradients
 -> transport and production
```

즉:
```
topography
<-> soil thickness
<-> soil mineralogy
<-> chemical erosion
```
의 양방향 feedback.

# 핵심 수학적 의미
논문 Equation 4의 soil-mineral evolution에는 topographic gradient와 mineral-abundance gradient의 dot product가 들어가며, 이것이 topography와 soil mineralogy를 직접 연결한다.

Characteristic hillslope diffusion time:

```
tau_diffusion
=
L^2 / D
```

where:
- L: horizontal hillslope length
- D: soil diffusivity

따라서 chemical-erosion transient response가 hillslope scale에 매우 민감하다.

# 핵심 결과
chemical erosion response time은 대체로:
1. hillslope length에 가장 강하게 좌우
2. uplift
3. soil production
4. soil transport
5. mineral dissolution
에 의해 보조적으로 조절

될 수 있었다.

reported idealized response times:
```
~10^3 - 10^6 yr
```
범위.

이 시간값을 고운사 100년 모델에 직접 적용하지 않는다.

중요한 점은:
```
chemical-weathering response time
!= local reaction time only
```

이며 hillslope-scale geomorphic transport timescale이 지배할 수 있다는 것이다.

# 고운사에 직접 사용할 수 있는 부분

## 1. hillslope length state
고운사 weathering sensitivity에서:
```
local slope
```
만 보지 않고:
```
distance to divide / channel
hillslope length
drainage density
```
도 고려할 근거.

## 2. sediment transport - mineral chemistry feedback
Landlab transport가 mineral inventory를 공간적으로 재배치하면 W_chem도 달라져야 한다.

## 3. 100년 해석
100년 동안 전체 hillslope chemical-weathering system이 새로운 equilibrium에 도달한다고 가정하지 않는다.

Postfire model은:
```
transient incremental response
```
를 계산한다.

이는 Donaldson 2026의 inherited-profile conclusion과 일치한다.

# 식생과의 연결
Published paper itself does not include vegetation.

Gounsa NEW COUPLING:

```
LPJ-GUESS
 -> root water uptake / hydrology
 -> soil production sensitivity
 -> hillslope transport sensitivity

        |
        v

Ferrier-Perron-type
soil/mineral/topography transient
```

단 q_bg에 biomass multiplier를 넣지 않는 현재 결정은 유지한다.

# 한계
- vegetation explicit 없음
- chemical dissolution is simplified relative to WITCH/PFLOTRAN
- very long characteristic response times
- sandstone-specific chemistry 없음
- postfire event processes 없음

# 최종 판정
- **핵심 채택: 3D hillslope chemical-erosion/topography coevolution precedent**
- hillslope length/transport timescale을 weathering response의 필수 spatial context로 추가
- first production chemistry engine이 아니라 landscape-scale coupling benchmark

# 참고 링크 / DOI
https://doi.org/10.1029/2020JF005562
