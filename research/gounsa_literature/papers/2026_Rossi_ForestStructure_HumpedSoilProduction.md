# 서지정보
Rossi, M. W., Tucker, G. E., Anderson, S. P., Anderson, R. S., & McGlinchy, J. (2026). Coevolving topography, patchy soils, and forest structure. *Proceedings of the National Academy of Sciences, 123*(12), e2519374123. DOI: 10.1073/pnas.2519374123.

# 이 논문을 찾은 이유
식생 구조가 실제 산지 사면에서 soil production과 bedrock exposure를 바꾸는지, 그리고 이를 landscape-evolution model에서 어떤 soil-production law로 표현해야 하는지 확인하기 위해 검토했다.

# 연구 유형
- field remote sensing + geomorphic modeling
- drone imagery
- airborne lidar
- Landlab landscape-evolution simulation

# 공간 구조
- mountain hillslopes
- opposing topographic aspects
- patchy soil / bedrock outcrop pattern
- elevation/incision gradient

# 적용 환경
- Rampart Range, Colorado
- unglaciated forested mountain range
- relatively uniform lithology

# 핵심 과정
- forest structure
- aspect-dependent biomass
- bedrock exposure
- soil production
- depth-dependent soil creep
- hillslope evolution

# 식생 입력
관측 측면:
- tree density
- canopy height
- forest biomass proxy

모델 해석:
- aspect-dependent weathering / soil-production intensity

논문은 full dynamic vegetation model을 Landlab에 직접 coupling한 production model을 제시하는 것이 아니라, vegetation/forest structure와 soil production 사이의 geomorphic feedback을 관측과 모델로 제약한다.

# 핵심 결과

## observed aspect contrast
equator-facing hillslopes:
- low elevation: 약 20% bedrock exposure
- high elevation: 약 3%

pole-facing hillslopes:
- low elevation: 약 11%
- high elevation: 약 1%

pole-facing slopes가 더 heavily forested.

## soil production function
고전적인 monotonic exponential production function만으로는 patchy soil-to-bedrock transition을 충분히 재현하기 어렵다.

논문은:
```
humped soil-production function
```
즉:
```
P(H=0) lower
P(H>0 small) maximum
P(H large) lower
```
구조가 bedrock outcrop과 soil patch를 생성하는 데 필요하다고 판단한다.

## hillslope transport
humped production을 depth-dependent soil creep와 결합하면 aspect-dependent weathering 차이에 따라 bedrock outcrop height/frequency gradient를 재현할 수 있다.

## forest interpretation
논문은 higher forest biomass와 lower bedrock exposure의 correspondence를 근거로:

```
forest dynamics
 -> root-zone weathering
 -> higher soil production
 -> lower bedrock exposure
 -> hillslope morphology
```

가능성을 제시한다.

# 파라미터와 단위
세부 humped-function coefficient는 본 md에서 임의 복원하지 않는다.
Published paper/code archive를 구현 단계에서 다시 확인한다.

Observed:
- bedrock exposure [%]
- canopy/tree structure from lidar/drone
- topographic aspect/elevation

# 원 논문의 구현 범위
Landscape simulations were built in Landlab.

핵심은:
- humped production
- depth-dependent creep
- aspect-dependent weathering
로 patchy rocky hillslopes를 설명하는 것이다.

# 고운사에 직접 사용할 수 있는 부분
**현재 Mode B 선택을 매우 강하게 지지한다.**

기존 고운사 Mode B:
```
shallow finite-depth hump / zero-depth suppression
```

는 더 이상 단순 sensitivity 아이디어만이 아니라 2026 forested mountain Landlab study의 강한 structural precedent를 가진다.

또한 식생 feedback 후보:
```
LPJ-GUESS root-zone state
 -> aspect/local vegetation-dependent soil-production modifier
```
가 물리적으로 plausible하다.

그러나 논문이 직접 FineRootC-to-P_sand equation을 제공한 것은 아니다.

# 새로운 coupling이 필요한 부분
금지:
```
P_sand = P_hump(H) * f(FineRootC)
```
를 근거 없이 바로 쓰는 것.

가능한 향후 coupling:
```
LPJ-GUESS root-zone state
 -> relative weathering/production potential
 -> humped P_sand(H) parameter sensitivity
```

이 연결은 새로운 coupling이며 site calibration이 필요하다.

# 한계
- Colorado mountain forest
- 고운사 sandstone-specific 아님
- vegetation-weathering causality를 직접 조작한 실험이 아님
- published abstract/main text에서 biomass-to-production universal equation은 없음

# 최종 판정
- **핵심 채택: forested hillslope humped soil-production + depth-dependent creep precedent**
- 고운사 Mode B의 우선순위를 크게 상승
- direct root-biomass multiplier는 여전히 금지
- forest structure를 soil-production sensitivity와 연결할 가치가 매우 높음

# 참고 링크 / DOI
https://doi.org/10.1073/pnas.2519374123
