# 서지정보
Yoo, K., & Mudd, S. M. (2008). Discrepancy between mineral residence time and soil age: Implications for the interpretation of chemical weathering rates. *Geology, 36*(1), 35-38. DOI: 10.1130/G24285A.1.

# 이 논문을 찾은 이유
사면에서 erosion/deposition과 soil mixing이 일어날 때 chemical weathering의 reaction time을 soil age로 대신해도 되는지 확인하기 위해 검토했다.

# 연구 유형
- theoretical/process mass-balance study
- hillslope soil-age vs mineral-residence analysis

# 공간 구조
- soil mantle / weathering zone
- hillslope material input/output
- depth-integrated mineral inventory

# 적용 환경
- generic eroding/depositional soil landscapes

# 핵심 과정
- weathering-zone expansion
- young-mineral addition
- chemical weathering
- physical soil loss
- soil/mineral residence-time distributions

# 식생 입력
explicit vegetation model은 없다.

따라서 vegetation source가 아니라 사면 transport-weathering coupling의 temporal constraint로 사용한다.

# 핵심 개념
논문의 핵심은:

```
soil age
!=
mineral residence time
```

이다.

Weathering-zone expansion은 young mineral mass를 soil system에 계속 추가하며, erosion/deposition과 mixing 때문에 bulk soil age와 특정 mineral의 reaction exposure time이 달라진다.

따라서 weathering kinetics를:
```
W = f(soil age)
```
만으로 해석하면 오류가 생길 수 있다.

# 고운사에 직접 사용할 수 있는 부분
고운사에서는:
- SWEHR erosion/deposition
- Landlab hillslope redistribution
- P_sand fresh-material input
이 동시에 발생한다.

따라서 chemical-weathering state에는 단순 cell age가 아니라 최소한:
```
fresh-mineral fraction
erosional/depositional status
effective mineral residence proxy
```
를 고려할 필요가 있다.

특히 footslope deposition 후:
```
old local soil + younger/older imported mineral
```
이 섞이므로 local soil age 하나로 weathering을 계산하면 안 된다.

# 새로운 coupling이 필요한 부분
Landlab/SWEHR material flux를 mineral-residence or fresh-mineral state로 바꾸는 것은 NEW COUPLING이다.

첫 production에서는 full age-distribution tracking 대신:
- fresh mineral fraction
- imported sediment fraction
를 저비용 state로 시험할 수 있다.

# 한계
- dynamic vegetation 없음
- detailed reactive transport 없음
- lithology-specific sandstone equation 없음
- long-term conceptual framework

# 최종 판정
- **핵심 채택: mineral residence time != soil age constraint**
- hillslope sediment transport -> chemical-weathering temporal state coupling의 필수 근거
- coefficient source 아님

# 참고 링크 / DOI
https://doi.org/10.1130/G24285A.1
