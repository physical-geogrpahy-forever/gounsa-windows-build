# 서지정보
Doane, T. H., Edmonds, D. A., Yanites, B. J., & Lewis, Q. (2021). *Topographic roughness on forested hillslopes: A theoretical approach for quantifying hillslope sediment flux from tree throw*. Geophysical Research Letters, 48(20), e2021GL094987. DOI: 10.1029/2021GL094987.

# 이 논문을 찾은 이유
tree throw를 background creep와 분리하고, 100년 고운사 simulation에서 실제 연 단위 stochastic event로 계산할 수 있는 published numerical structure인지 확인하기 위해 검토했다.

# 연구 유형
- theoretical / numerical model
- stochastic pit-mound production
- sediment-flux inference

# 공간 구조
- 2D synthetic hillslope surface
- stochastic pit-mound couplets
- roughness statistics linked to sediment flux

# 적용 환경
- forested hillslopes

# 핵심 과정
- tree throw
- pit-mound production
- topographic roughening
- diffusion-like smoothing
- tree-throw sediment flux

# 식생 입력
- tree-throw event production rate
- event geometry / displaced sediment volume
- transport distance

# 시간간격
**One-year numerical timestep.**

At each yearly step:
1. the number of new pit-mound couplets is sampled from an event-rate distribution
2. new events are added to the 2D surface
3. the surface evolves/smooths
4. roughness responds to the balance of production and smoothing

This is directly compatible with a 100-year Gounsa simulation.

# 핵심 식 / 구조
Mean tree-throw sediment flux is represented from:
```
volumetric entrainment/event rate
x
mean downslope travel distance
```

The exact roughness relation is developed in the paper and subsequent Doane lineage.

The model separates:
```
stochastic roughening by tree throw
```
from:
```
continuous diffusion-like smoothing
```

# 파라미터와 단위
- tree-throw event rate [events area^-1 yr^-1]
- displaced volume [m^3 event^-1]
- travel distance [m]
- roughness variance
- smoothing diffusivity

# 원 논문의 구현 범위
The model converts discrete annual tree-throw events into hillslope-scale roughness and sediment flux.

# 고운사에 직접 사용할 수 있는 부분
Use tree throw as a **separate annual event process** rather than increasing a generic diffusivity whenever woody biomass is high.

A Gounsa structure can be:

```
LPJ-GUESS woody cohorts
 -> mortality / uprooting probability
 -> annual tree-throw events
 -> pit/mound geometry + sediment displacement
```

# 새로운 coupling이 필요한 부분
LPJ-GUESS cohort DBH, density, mortality and disturbance history must be converted to:
- event probability
- displaced volume
- travel distance

That interface is a new coupling.

# 한계
- does not model root-growth bioturbation
- does not provide chemical weathering
- woody vegetation only
- local event-rate and geometry calibration required

# 최종 판정
**채택: q_treethrow annual stochastic component.**

Together with Gabet 2003 root-growth flux and a separate background creep law, this is better suited to a 100-year forest model than a single biomass-modified Pelletier diffusivity.

# 참고 링크 / DOI
https://doi.org/10.1029/2021GL094987
