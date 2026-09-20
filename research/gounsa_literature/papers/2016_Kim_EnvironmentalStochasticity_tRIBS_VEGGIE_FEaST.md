# 서지정보
Kim, J., Ivanov, V. Y., & Fatichi, S. (2016). *Environmental stochasticity controls soil erosion variability*. Scientific Reports, 6, 22065. DOI: 10.1038/srep22065.

# 이 논문을 찾은 이유
동적 vegetation model인 VEGGIE와 genuine 2D Hairsine-Rose erosion model인 FEaST가 실제로 한 coupled modeling system 안에서 사용되므로, quantitative vegetation state가 erosion resistance까지 직접 연결되는지 확인하기 위해 검토했다.

# 연구 유형
- coupled ecohydrology-hydrodynamics-erosion numerical modeling
- long-term/event-scale soil-erosion variability analysis

# 공간 구조
- tRIBS hydrology
- VEGGIE dynamic vegetation
- 2D Saint-Venant overland flow
- Hairsine-Rose sediment movement
- triangular mesh
- event sequences and long-term aggregation

# 적용 환경
- USLE unit-plot datasets across multiple U.S. environments
- numerical experiments include long event sequences
- mountain/postfire forest 전용은 아님

# 핵심 과정
- dynamic vegetation-water-energy coupling
- rainfall/runoff generation
- 2D overland flow
- rainfall- and flow-driven erosion
- original cohesive soil
- deposited erodible layer
- surface shielding/armoring
- event-to-event erosion memory

# 식생 입력
The coupled system includes VEGGIE, which dynamically represents vegetation-water-energy interactions.

However, in the erosion analysis reported here, FEaST erodibility states are controlled primarily by:
- original-soil particle-size distribution and erodibility
- deposited-layer particle-size distribution
- deposited-layer cover fraction H
- hydrometeorological antecedent conditions

The paper does **not** establish a direct:
```
root biomass / RLD
 -> FEaST J, detachability, or critical stream power
```
coupling.

# 핵심 식
FEaST is the 2D Hairsine-Rose erosion component described in Kim et al. (2013).

A key state is:
```
H = area fraction/protection associated with highly erodible deposited soil
```
versus:
```
1-H = original intact cohesive soil
```

Antecedent surface PSD and H are updated between events, producing source-limited/transport-limited alternation.

# 파라미터와 단위
See Kim et al. (2013) for Hairsine-Rose detachment/entrainment parameters.
This paper focuses on stochastic variability and antecedent geomorphic states rather than new erosion coefficients.

# 원 논문의 구현 범위
The coupled tRIBS-VEGGIE-FEaST framework simulates ecohydrology and 2D erosion in one modeling system and allows erosion-state memory between events.

# 고운사에 직접 사용할 수 있는 부분
1. Very strong precedent for running a dynamic vegetation/ecohydrology model together with a 2D Hairsine-Rose erosion model.
2. Event-to-event soil-surface memory and armoring are important for a 100-year simulation.
3. A deposited loose layer should persist between storms rather than be reset each event.

# 새로운 coupling이 필요한 부분
Dynamic vegetation is present, but the direct quantitative vegetation-to-erodibility bridge is not provided.
Thus:
```
LPJ-GUESS FineRootC/litter
 -> J / a / UC / shielding
```
remains a **new coupling**.

# 한계
- no direct root biomass/RLD erosion-resistance coupling
- vegetation is not shown to directly update the FEaST cohesive-soil resistance parameters
- study objective is erosion variability, not vegetation-control parameterization

# 최종 판정
- **핵심 structural precedent**
- does not solve the quantitative root/litter coupling gap
- strengthens the case for FEaST/Hairsine-Rose as the hydrodynamic-erosion core

# 참고 링크 / DOI
https://doi.org/10.1038/srep22065
