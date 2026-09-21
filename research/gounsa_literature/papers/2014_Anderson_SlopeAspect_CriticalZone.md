# 서지정보
Anderson, S. P., Hinckley, E.-L. S., Kelly, P., & Langston, A. (2014). Variation in Critical Zone Processes and Architecture across Slope Aspects. *Procedia Earth and Planetary Science, 10*, 28-33. DOI: 10.1016/j.proeps.2014.08.006.

# 이 논문을 찾은 이유
opposing hillslope aspects에서 vegetation, water, biogeochemistry, soil, weathering이 어떻게 함께 달라지는지 Gordon Gulch 자료를 통합해 확인하기 위해 검토했다.

# 연구 유형
- Critical Zone field synthesis
- aspect natural experiment

# 공간 구조
- opposing north/south-facing hillslopes
- soil to lower Critical Zone

# 적용 환경
- Gordon Gulch, Colorado Front Range
- montane forest

# 핵심 과정
- slope-aspect energy balance
- snow/water delivery
- vegetation contrast
- soil moisture
- biogeochemistry
- weathering
- critical-zone architecture

# 식생 입력
- contrasting forest structure by aspect
- no dynamic vegetation model

# 핵심 결과
저자들은 opposing aspects의 water, biogeochemistry, soil, weathering 차이를 종합하여:

```
water and energy delivery to lower Critical Zone
```

가 Critical Zone architecture 진화에서 매우 중요한 climate control이라고 정리한다.

즉 aspect 자체가 causal coefficient라기보다:

```
aspect
 -> energy/snow/water
 -> vegetation/hydrology
 -> lower-CZ weathering
```

경로가 핵심이다.

# 고운사에 직접 사용할 수 있는 부분
고운사에서 aspect별 고정 weathering multiplier를 두지 않고 LPJ-GUESS + hydrology를 통해 실제 state를 계산해야 한다는 근거.

# 새로운 coupling이 필요한 부분
terrain aspect -> LPJ-GUESS microclimate/hydrology -> chemical/weathering front 연결은 새로운 coupling.

# 한계
- synthesis paper
- no universal process equation
- vegetation causality 독립분리 안 됨
- lithology differs from Gounsa

# 최종 판정
- **보조 채택: aspect -> energy/water -> vegetation/weathering architecture**
- direct coefficient source 아님

# 참고 링크 / DOI
https://doi.org/10.1016/j.proeps.2014.08.006
