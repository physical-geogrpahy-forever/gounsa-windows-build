# 서지정보
Welivitiya, W. D. D. P., Willgoose, G. R., & Hancock, G. R. (2021). *Evaluating a new landform evolution model: A case study using a proposed mine rehabilitation landform*. Earth Surface Processes and Landforms, 46(11), 2298-2314. DOI: 10.1002/esp.5175.

# 이 논문을 찾은 이유
고운사 목표기간과 같은 **100년**에서 weathering-capable soilscape-landform model을 실제로 운용한 published example이 있는지 확인하기 위해 검토했다.

# 연구 유형
- numerical landform-evolution model evaluation
- SSSPAM vs SIBERIA comparison

# 공간 구조
- catchment-scale DEM
- layered soil/profile state
- distributed erosion and deposition

# 적용 환경
- proposed post-mining rehabilitation landform
- not forest/postfire

# 핵심 과정
SSSPAM capability includes:
- short precipitation events / variable rainfall / annual-average rainfall
- erosion
- deposition
- diffusion
- physical weathering
- armouring
- subsurface profile evolution

# 식생 입력
No dynamic vegetation/root state comparable to LPJ-GUESS.

# 시간간격 / simulation horizon
The paper explicitly performs a:
```
100-year short-term evolution simulation
```

and also longer 10,000-year comparisons.

This demonstrates that a coupled soilscape-landform framework can operate on the same century-scale horizon as Gounsa.

The model can use:
- short-term rainfall events
- variable precipitation
- time-averaged annual precipitation

# 원 논문의 구현 범위
SSSPAM and SIBERIA gave broadly comparable short-term erosion/landform behavior.

SSSPAM additionally represents subsurface soil evolution and armouring.

# 중요한 해석
The existence of a 100-year SSSPAM simulation means:
```
100-year soilscape/landform simulation is technically feasible
```

but it does **not** mean its weathering parameterization is automatically appropriate for measurable forest-weathering changes over 100 years.

Indeed, later applications sometimes disable the weathering module for 100-year runs because physical weathering/profile evolution can be slow relative to the target interval.

# 고운사에 직접 사용할 수 있는 부분
- timescale feasibility benchmark
- soil-profile/armour bookkeeping
- possible coarse-fragment module comparison
- useful independent check on annual landform integration

# 새로운 coupling이 필요한 부분
LPJ-GUESS vegetation/root state is absent.
A forest/postfire coupling would be new.

# 한계
- post-mining substrate
- no forest succession
- physical weathering, not chemical weathering
- overlap with SWEHR erosion and armour state

# 최종 판정
**보조 후보.**

SSSPAM proves that century-scale coupled soilscape-landform modelling exists, but it is not as direct a biological-process match as:
- LPJ-GUESS-CNP daily chemical weathering
- Gabet & Mudd annual woody physical weathering
- Gabet 2003 + Doane annual hillslope biogenic transport

# 참고 링크 / DOI
https://doi.org/10.1002/esp.5175
