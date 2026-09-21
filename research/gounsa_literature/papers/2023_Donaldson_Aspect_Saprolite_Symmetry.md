# 서지정보
Donaldson, A. M., Zimmer, M., Huang, M.-H., Johnson, K. N., Hudson-Rasmussen, B., Finnegan, N., Barling, N., & Callahan, R. P. (2023). Symmetry in Hillslope Steepness and Saprolite Thickness Between Hillslopes With Opposing Aspects. *Journal of Geophysical Research: Earth Surface, 128*(7), e2023JF007076. DOI: 10.1029/2023JF007076.

# 이 논문을 찾은 이유
사암 우세 산지에서 현재 식생, 토양수분, perched groundwater가 aspect별로 다른데도 saprolite thickness가 달라지는지 확인하기 위해 검토했다.

# 연구 유형
- paired hillslope field study
- terrain analysis
- vegetation mapping
- soil pits
- geophysics
- hydrologic monitoring

# 공간 구조
- opposing north/south-facing hillslopes
- ridge to stream
- soil
- saprolite
- weathered bedrock

# 적용 환경
- Arbor Creek, central California Coast Range
- sandstone-dominated hillslopes with local shale
- rain-dominated Mediterranean climate
- north-facing: denser woody vegetation
- south-facing: more open/grass-dominated

# 핵심 과정
- aspect microclimate
- vegetation
- soil moisture
- perched groundwater
- lateral flow
- saprolite weathering
- inherited landscape state

# 핵심 결과
North-facing slopes:
- denser vegetation
- higher shallow soil moisture

그런데:
```
average slope ~24°
saprolite thickness ~6 m
```
로 opposing aspects 간 큰 차이가 없었다.

Hydrology는 달랐다.

South-facing slope에서 saprolite-weathered-bedrock interface의 perched groundwater가 더 지속적으로 나타났고, north-facing slope에서는 oak water uptake가 saturated conditions를 줄였을 가능성이 있다.

따라서 저자들은 두 상반된 pathway가 균형을 만들 수 있다고 제안한다.

```
south-facing:
more lateral/perched water
 -> stronger hydrologic chemical weathering

north-facing:
deeper woody roots
 -> stronger biological weathering
but
 -> stronger water uptake
 -> less saturated/lateral flow
```

또 legacy framework:
과거 더 균일한 woody vegetation과 기후가 현재 saprolite symmetry를 남겼을 가능성을 제시한다.

# 고운사에 직접 사용할 수 있는 부분
아주 중요한 interaction constraint.

```
more trees
!=
more wetness
!=
thicker saprolite
```

Tree water uptake는 chemical-weathering water availability를 줄이는 동시에 biological/root weathering을 강화할 수 있다.

즉 vegetation effect 내부에도 반대부호 경로가 있다.

또:
```
current vegetation difference
!= inherited saprolite-thickness difference
```
를 직접 지지한다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS vegetation이:
- root biological forcing
- water uptake
를 동시에 weathering engine에 전달해야 한다.

두 효과를 하나의 vegetation factor로 상쇄시키는 empirical multiplier는 사용하지 않는다.

# 한계
- observational natural experiment
- causal process rates 분리 어려움
- long-term inherited state
- annual postfire weathering law 없음

# 최종 판정
- **핵심 채택: sandstone aspect + vegetation + hydrology + inherited saprolite constraint**
- Donaldson 2026의 직접 선행연구
- current vegetation multiplier 금지 강화

# 참고 링크 / DOI
https://doi.org/10.1029/2023JF007076
