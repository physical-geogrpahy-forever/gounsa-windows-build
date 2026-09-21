# 서지정보
Yoo, K., Amundson, R., Heimsath, A. M., & Dietrich, W. E. (2007). Integration of geochemical mass balance with sediment transport to calculate rates of soil chemical weathering and transport on hillslopes. *Journal of Geophysical Research: Earth Surface, 112*, F02013. DOI: 10.1029/2005JF000402.

# 이 논문을 찾은 이유
사면 위치별 chemical weathering이 local bedrock-derived soil뿐 아니라 상류에서 이동해 온 토양의 화학적 이력까지 포함해야 하는지 확인하기 위해 검토했다.

# 연구 유형
- process-oriented hillslope soil mass-balance model
- field geochemical calibration
- cosmogenic soil-production constraints

# 공간 구조
- 50 m hillslope transect
- upslope-to-downslope sediment flux
- local soil production
- lateral soil transport

# 적용 환경
- semiarid granodiorite hillslope
- southeastern Australian highlands

# 핵심 과정
- saprolite-to-soil conversion
- chemical weathering
- lateral sediment transport
- upslope sediment influx
- local soil production
- elemental mass balance

# 식생 입력
explicit dynamic vegetation 없음.

고운사에서는 vegetation이:
- soil production
- erosion/transport
- water balance
를 바꾸므로 이 mass-balance skeleton에 간접적으로 작용한다.

# 핵심 구조
핵심 출발점:

```
weathering substrate at hillslope position x
=
locally produced soil
+
soil imported from upslope
```

따라서 local chemical weathering은 단순:
```
W(x)=f(local H)
```
로 충분하지 않을 수 있다.

사면 질량수지에서:
- in-situ soil production
- upslope soil influx
- downslope soil outflux
- elemental depletion
을 함께 계산한다.

# 핵심 결과
논문은 chemical weathering rate와 soil transport rate를 hillslope position별로 동시에 추정할 수 있는 framework를 제시한다.

이론적으로:
```
sediment transport history
 -> mineral supply / residence
 -> chemical weathering
```
을 명시적으로 포함한다.

# 고운사에 직접 사용할 수 있는 부분
매우 중요하다.

SWEHR/Landlab에서:
```
erosion
deposition
upslope sediment delivery
```
가 발생하면 chemical-weathering state도 함께 갱신되어야 한다.

특히 depositional footslope에서는:
```
local soil
+
imported upslope soil
```
의 혼합을 고려하지 않으면 weathering history를 잘못 표현할 수 있다.

# 새로운 coupling이 필요한 부분
고운사에서는:
```
Landlab/SWEHR sediment flux
 -> mineral inventory / weathering age / provenance
 -> W_chem
```
연결이 새로운 coupling이다.

첫 production에서 완전한 particle-age tracking이 부담되면:
- depositional vs erosional state
- fresh-mineral fraction
를 단순 state로 둘 수 있다.

# 한계
- vegetation 없음
- granodiorite
- 1D transect
- long-term field mass balance
- reactive chemistry engine 아님

# 최종 판정
- **핵심 채택: hillslope sediment transport-chemical weathering mass balance**
- footslope/depositional weathering을 local-box로만 계산하지 않는 근거

# 참고 링크 / DOI
https://doi.org/10.1029/2005JF000402
