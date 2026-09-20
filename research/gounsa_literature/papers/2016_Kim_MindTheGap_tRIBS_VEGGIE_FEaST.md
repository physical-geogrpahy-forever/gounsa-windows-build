# 서지정보
Kim, J., Ivanov, V. Y., & Fatichi, S. (2016). *Soil erosion assessment—Mind the gap*. Geophysical Research Letters, 43(24), 12446-12456. DOI: 10.1002/2016GL071480.

# 이 논문을 찾은 이유
tRIBS-VEGGIE-FEaST가 2D erosion 내부의 original/deposited-soil erodibility를 어떻게 취급하고, vegetation model의 존재가 실제 erodibility coupling까지 의미하는지 확인하기 위해 검토했다.

# 연구 유형
- process-based numerical erosion uncertainty study

# 공간 구조
- tRIBS-VEGGIE-FEaST
- 2D overland flow and sediment transport
- plot/event scale numerical experiments

# 적용 환경
- observed soil-loss variability across upland plots
- numerical event-scale soil erosion

# 핵심 과정
- 2D rainfall/runoff
- Hairsine-Rose erosion
- original intact cohesive soil
- deposited noncohesive soil
- particle-size distributions
- evolving surface shield
- geomorphic internal variability

# 식생 입력
VEGGIE is part of the coupled modeling platform, but this study's erosion experiments vary initial soil erodibility and deposited-layer states rather than deriving FEaST erosion resistance from root biomass/RLD.

# 핵심 식
The paper explicitly distinguishes:
```
original intact cohesive soil
vs
deposited noncohesive soil
```

Their detachabilities are represented separately.
Original-soil resistance to flow-driven entrainment is represented by the Hairsine-Rose specific energy of entrainment `J`.

# 파라미터와 단위
- original/deposited soil detachabilities
- J: specific energy of entrainment
- H: surface shield/deposited fraction
- multisize PSD

# 원 논문의 구현 범위
Tests how uncertainty in soil substrate composition and erodibility leads to nonunique soil-loss response even under comparable hydrologic forcing.

# 고운사에 직접 사용할 수 있는 부분
- strong justification for maintaining soil-surface state and erodibility through time
- supports a model where wildfire changes original/deposited/loose-layer states rather than only multiplying a cover factor
- reinforces use of Hairsine-Rose/FEaST for event-to-event geomorphic memory

# 새로운 coupling이 필요한 부분
No direct VEGGIE biomass/root-to-J relation is supplied.

# 한계
- does not solve quantitative vegetation resistance
- focus is uncertainty/nonuniqueness, not forest root recovery

# 최종 판정
- **핵심 Hairsine-Rose/FEaST supporting paper**
- vegetation component coexistence is structurally important but not a direct root-erodibility solution

# 참고 링크 / DOI
https://doi.org/10.1002/2016GL071480
