# 서지정보
Kim, J., & Ivanov, V. Y. (2014). *On the nonuniqueness of sediment yield at the catchment scale: The effects of soil antecedent conditions and surface shield*. Water Resources Research, 50. DOI: 10.1002/2013WR014580.

# 이 논문을 찾은 이유
tRIBS-FEaST Hairsine-Rose model에서 surface shield/armoring과 antecedent soil state가 장기 고운사 erosion memory에 얼마나 중요한지 확인하기 위해 검토했다.

# 연구 유형
- 2D process-based erosion numerical study

# 공간 구조
- tRIBS-FEaST
- Hairsine-Rose erosion/sediment transport
- catchment-scale spatial simulations

# 적용 환경
- catchment-scale numerical experiments
- multisize soil/sediment

# 핵심 과정
- original/deposited soil states
- surface shielding
- armoring
- particle-size sorting
- antecedent soil moisture
- nonunique sediment yield

# 식생 입력
No quantitative root/litter erosion-resistance coupling is central to this paper.

# 핵심 식
The model explicitly evolves:
```
original cohesive soil
+ deposited loose soil
+ size-selective sediment transport
+ shield fraction H
```

Coarse-surface shielding can make sediment response nonunique even under similar hydrologic forcing.

# 파라미터와 단위
Hairsine-Rose FEaST parameters from the 2013 model lineage.

# 원 논문의 구현 범위
Demonstrates dynamical memory of erosion through antecedent particle-size composition and deposited-layer shielding.

# 고운사에 직접 사용할 수 있는 부분
Highly relevant to:
- postfire fines removal
- residual/coarse-fragment exposure
- armor development
- event-to-event sediment-supply exhaustion

# 새로운 coupling이 필요한 부분
Fire-spall/coarse-fragment production and vegetation-dependent resistance are outside the paper.

# 한계
- no dynamic root resistance
- not specifically postfire forest

# 최종 판정
- **채택: surface shield/armoring memory precedent**
- strengthens Hairsine-Rose/FEaST for Gounsa's coarse-fragment problem

# 참고 링크 / DOI
https://doi.org/10.1002/2013WR014580
