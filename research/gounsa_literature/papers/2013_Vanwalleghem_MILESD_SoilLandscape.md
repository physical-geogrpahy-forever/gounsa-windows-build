# 서지정보
Vanwalleghem, T., Stockmann, U., Minasny, B., & McBratney, A. B. (2013). A quantitative model for integrating landscape evolution and soil formation. *Journal of Geophysical Research: Earth Surface, 118*(2), 331-347. DOI: 10.1029/2011JF002296.

# 이 논문을 찾은 이유
사면의 weathering, pedogenesis, soil horizons, erosion/deposition을 하나의 spatial model에서 연결한 선례를 확인하고, 식생/수문 state를 고운사에 추가할 backbone으로 쓸 수 있는지 검토했다.

# 연구 유형
- spatially explicit mechanistic soil-landscape model
- MILESD: Model for Integrated Landscape Evolution and Soil Development

# 공간 구조
- 6.25 km2 application
- spatial grid
- three soil horizons + bedrock layer
- lateral erosion/deposition
- vertical soil-profile evolution

# 적용 환경
- Werrikimbe National Park, Australia
- long-term natural soil-landscape development

# 핵심 과정
- bedrock weathering
- physical fragmentation
- chemical weathering
- clay translocation
- organic matter
- soil-horizon evolution
- erosion/deposition
- sediment export

# 식생 입력
dynamic vegetation model은 없다.

원 논문은 chemical-weathering controls로:
- runoff
- lithology
- temperature
- vegetative cover
- tectonics/exposure
를 인식하지만, vegetation을 LPJ-GUESS처럼 prognostic하게 계산하지 않는다.

# 핵심 physical weathering
Physical fragmentation depends on:
- particle size
- depth below surface

Depth is used as a proxy for temperature-amplitude attenuation.

# 핵심 chemical weathering
Chemical weathering depends on:
- mineral surface area
- soil depth

and recognizes broader controls including:
- water flow
- temperature
- solution chemistry
- vegetative cover

하지만 full vegetation-process coupling은 없다.

# 핵심 결과
MILESD는:
```
weathering
 -> soil-horizon evolution
 -> erosion/deposition
 -> sediment export
 -> landscape redistribution
```
를 하나의 mass-balanced profile-landscape model로 연결한다.

60,000-year application에서 catena-scale soil thickness trends를 reasonably reproduced.

# 고운사에 직접 사용할 수 있는 부분
MILESD는 다음 구조의 강한 선례다.

```
vertical soil profile
+
weathering
+
lateral hillslope transport
+
erosion/deposition
```

즉 고운사에서:
```
A/B mobile soil
C/Cr weathered zone
bedrock
```
를 따로 state로 유지하면서 Landlab lateral flux와 연결하는 architecture에 유용하다.

# 식생 관련 판단
MILESD는 식생을 explicit dynamic state로 계산하지 않으므로:
```
LPJ-GUESS -> MILESD weathering
```
은 새 coupling이다.

고운사 production에서 직접 채택할 vegetation-weathering equation은 제공하지 않는다.

# 한계
- 60 kyr timescale
- dynamic vegetation 없음
- fire 없음
- chemical reaction network가 WITCH/BioRT/PFLOTRAN보다 단순
- sandstone-specific calibration 없음

# 최종 판정
- **보조 채택: spatial soil-profile + landscape evolution backbone**
- chemical-weathering engine으로는 WITCH/BioRT/PFLOTRAN 계열보다 약함
- profile bookkeeping/soil-horizon architecture 비교대상

# 참고 링크 / DOI
https://doi.org/10.1029/2011JF002296
