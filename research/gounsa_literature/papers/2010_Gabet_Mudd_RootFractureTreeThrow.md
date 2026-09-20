# 서지정보
Gabet, E. J., & Mudd, S. M. (2010). *Bedrock erosion by root fracture and tree throw: A coupled biogeomorphic model to explore the humped soil production function and the persistence of hillslope soils*. Journal of Geophysical Research: Earth Surface, 115, F04005. DOI: 10.1029/2009JF001526.

# 이 논문을 찾은 이유
Pelletier보다 짧은 시간간격에서 forest population, root fracture, tree throw, physical bedrock erosion과 soil creep를 실제로 함께 계산하는 published numerical model이 있는지 확인하기 위해 검토했다.

# 연구 유형
- coupled numerical biogeomorphic model
- forest population + physical weathering + hillslope transport

# 공간 구조
- 1D hillslope profile
- 100 m long model hillslope
- finite-difference soil-creep update
- explicit spatial soil-thickness/bedrock surface

# 적용 환경
- forested soil-mantled hillslope
- Oregon Coast Range analogue
- conifer / Douglas-fir parameterization
- weak sandstone analogue

# 핵심 과정
- tree recruitment and growth
- stochastic mortality
- root fracture of bedrock
- tree throw
- clast weathering
- bedrock erosion
- soil mantling
- continuous soil creep

# 식생 입력
Original model:
- individual conifer trees
- tree age
- tree size
- spacing/competition
- rootwad volume
- mortality probability
- tree-throw probability

For Gounsa, LPJ-GUESS cohort state can replace the simplified internal forest-growth representation, but that replacement is a new coupling.

# 시간간격
**Annual timestep.**

At every annual step the model updates:
- seed recruitment
- mortality
- stochastic tree throw
- physical clast weathering
- bedrock lowering
- soil creep

Thus this is directly compatible with a 100-year outer geomorphic clock.

# 핵심 식

## background soil creep
The model represents background smoothing with linear diffusion:

```
q_sc = -D S
```

where:
- `q_sc`: sediment flux [m^2 yr^-1]
- `D`: diffusivity [m^2 yr^-1]
- `S`: local slope [-]

The paper uses:
```
D = 2.5e-3 m^2 yr^-1
```
for its Oregon Coast Range analogue after excluding an assumed fire-driven share from a landscape-scale estimate.

To mimic interannual climate variation, `D` is redrawn each year from a normal distribution with a standard deviation of 50% of the mean.

This numerical value is **not transferable to Gounsa**.

## physical weathering of clasts
At every annual step exposed clast surfaces are weathered.

For the weak-sandstone analogue the paper adopts a maximum disintegration rate:
```
0.5 mm yr^-1
```

Again this is lithology-specific and must not be copied to Gounsa.

## tree mortality / throw
Mortality and the subset of deaths producing tree throw are treated stochastically each year.

# 파라미터와 단위
- `D`: m^2 yr^-1
- `q_sc`: m^2 yr^-1
- clast-disintegration rate: length yr^-1
- rootwad/tree geometry
- tree mortality and throw probabilities [yr^-1]

# 원 논문의 구현 범위
This is a real annual numerical model in which vegetation and physical geomorphic processes evolve together.

It is not merely a long-term equilibrium relation.

# 고운사에 직접 사용할 수 있는 부분

### 1. woody mechanical weathering
```
woody cohort / root system
 -> root fracture
 -> physical bedrock erosion
```

### 2. tree throw
```
tree mortality
 -> stochastic uprooting
 -> pit/mound + lateral sediment displacement
```

### 3. annual process clock
The annual numerical architecture fits LPJ-GUESS much better than Pelletier 2013's geologic-timescale eco-pedo-geomorphic runs.

# 새로운 coupling이 필요한 부분
LPJ-GUESS replaces the paper's simplified internal tree-population model:

```
LPJ-GUESS DBH / cohort density / mortality / root state
 -> Gabet-Mudd root-fracture and tree-throw geometry
```

This is a **new coupling**.

For background creep, the linear `D S` law need not be retained if a more appropriate steep-slope nonlinear law such as Roering is selected.

# 한계
- 1D
- conifer/Oregon calibration
- weak sandstone physical analogue
- explicitly focuses on physical weathering
- chemical weathering is not dynamically modeled
- internal forest demography is much simpler than LPJ-GUESS
- linear creep is less suitable near critical slopes than Roering-type nonlinear transport

# 최종 판정
**핵심 채택: annual woody mechanical-weathering and tree-throw model lineage.**

For Gounsa:
- retain annual root-fracture/tree-throw process architecture
- replace simplified vegetation with LPJ-GUESS states
- use independently selected background creep law
- do not copy Oregon sandstone coefficients

# 참고 링크 / DOI
https://doi.org/10.1029/2009JF001526
