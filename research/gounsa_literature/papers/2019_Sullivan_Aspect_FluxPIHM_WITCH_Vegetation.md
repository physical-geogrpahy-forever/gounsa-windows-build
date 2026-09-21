# 서지정보
Sullivan, P. L., et al. (2019). Exploring the effect of aspect to inform future earthcasts of climate-driven changes in weathering of shale. *Journal of Geophysical Research: Earth Surface*. DOI: 10.1029/2017JF004556.

# 이 논문을 찾은 이유
사면 방향과 수문, 광물풍화, 식생의 양분 흡수 및 낙엽 반환을 실제 결합한 published model이 있는지 확인하기 위해 검토했다.

# 연구 유형
- hillslope Critical Zone modeling
- coupled hydrology + weathering + vegetation nutrient cycling
- field-constrained aspect comparison

# 공간 구조
- opposing hillslope aspects
- soil/weathered shale profile
- distributed hydrologic flow
- vegetation-mediated nutrient cycling

# 적용 환경
- Shale Hills Critical Zone Observatory, Pennsylvania
- temperate forest
- shale parent material

# 핵심 과정
- aspect-driven energy/hydrologic differences
- Flux-PIHM hydrology
- WITCH mineral weathering
- vegetation nutrient uptake
- litterfall / biolifting
- solute-depth profiles

# 식생 입력
식생효과는 단순 biomass multiplier가 아니라:
- dissolved nutrient uptake by vegetation
- aboveground transfer
- litter return to near-surface soil
형태로 구현된다.

# 핵심 결합
모델 구조:

```
Flux-PIHM
 -> water flux / hydrologic state

WITCH
 -> mineral dissolution / chemical weathering

vegetation cycling
 -> nutrient uptake
 -> aboveground biomass transfer
 -> litter return / biolifting
```

즉:
```
hydrology
+ mineral kinetics
+ vegetation nutrient cycling
```
을 실제로 연결한 published precedent다.

# 핵심 결과
Vegetation nutrient cycling을 포함하면 depth-dependent solute profiles의 재현성이 개선되었다.

동시에 vegetation cycling이 weathering을 단순히 증가시키지 않았다.

논문에서 vegetation effect를 포함할 경우 shale weathering이 약 10% 감소하는 결과가 보고되었다.

이는:
```
vegetation
 -> nutrient uptake / recycling
 -> reduced dissolved export / altered reaction demand
 -> lower net weathering
```
가능성을 보여준다.

# 사면방향 해석
Aspect 자체가 weathering coefficient가 아니다.

```
aspect
 -> energy / water balance
 -> hydrology
 -> vegetation nutrient cycling
 -> mineral reaction environment
```

으로 작용한다.

# 고운사에 직접 사용할 수 있는 부분
매우 중요하다.

현재 고운사 구조:

```
LPJ-GUESS
 -> hydrology
 -> nutrient uptake
 -> litter return

WITCH/PROFILE
 -> mineral weathering
 -> nutrient release
```

을 직접 지지하는 published coupling precedent다.

특히:
```
weathering nutrient release
 -> plant uptake
 -> litter return
 -> soil solution chemistry
```
의 양방향 feedback이 실제 구현 가능함을 보여준다.

# 새로운 coupling이 필요한 부분
Flux-PIHM vegetation module을 LPJ-GUESS로 교체하고:
- root distribution
- root water uptake
- root respiration
- CNP demand
를 전달하는 것은 NEW COUPLING이다.

# 한계
- shale
- full dynamic forest succession 아님
- fire/postfire 없음
- Gounsa sandstone-specific reaction network 아님

# 최종 판정
- **핵심 채택: hillslope hydrology + WITCH + vegetation nutrient cycling direct precedent**
- current Gounsa architecture의 가장 강한 published integration evidence 중 하나
- 식생이 weathering을 항상 증가시키는 것이 아니라는 직접 모델근거

# 참고 링크 / DOI
https://doi.org/10.1029/2017JF004556
