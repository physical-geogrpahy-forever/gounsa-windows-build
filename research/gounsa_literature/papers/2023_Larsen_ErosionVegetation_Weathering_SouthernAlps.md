# 서지정보
Larsen, I. J., Eger, A., Almond, P. C., Thaler, E. A., Rhodes, J. M., & Prasicek, G. (2023). The influence of erosion and vegetation on soil production and chemical weathering rates in the Southern Alps, New Zealand. *Earth and Planetary Science Letters, 608*, 118036. DOI: 10.1016/j.epsl.2023.118036.

# 이 논문을 찾은 이유
산지 사면에서 식생형 차이와 침식률 차이가 동시에 존재할 때 soil production과 chemical weathering을 실제로 무엇이 더 강하게 지배하는지 확인하기 위해 검토했다.

# 연구 유형
- cosmogenic 10Be soil-production analysis
- geochemical mass balance
- drainage-divide natural experiment
- vegetation-gradient comparison

# 공간 구조
- migrating drainage divide
- rapidly vs slowly eroding catchment sides
- ridgetops / hillslopes
- contrasting ecosystem zones

# 적용 환경
- western Southern Alps, New Zealand
- temperate rainforest
- tussock grassland
- unvegetated alpine ecosystem
- strong erosion-rate contrast

# 핵심 과정
- soil production
- physical erosion
- chemical weathering
- mineral residence time
- topographic curvature
- vegetation contrast
- drainage-divide migration

# 식생 입력
observed vegetation classes:
- temperate rainforest
- tussock grassland
- unvegetated alpine

Dynamic vegetation model은 아니다.

# 핵심 결과
빠르게 침식되는 쪽에서:
- soil production
- physical erosion
- chemical weathering rate

가 모두 유의하게 높았다.

그러나:
```
chemical-weathering intensity
```
는 drainage divide 양쪽이나 vegetation type에 따라 유의한 차이를 보이지 않았다.

핵심 해석:

```
fluvially driven erosion
 -> hillslope curvature
 -> mineral residence time
 -> soil production / chemical weathering rate
```

가 vegetation class보다 강한 제어였다.

논문 결론은 서부 Southern Alps에서 soil production과 chemical weathering이 vegetation보다 landscape response to erosion에 더 강하게 매개된다는 것이다.

# 고운사에 직접 사용할 수 있는 부분
매우 중요한 negative constraint.

금지:
```
more forest biomass
 -> automatically higher W_chem
```

고운사에서는:
```
vegetation
 -> erosion / hydrology

erosion
 -> fresh-mineral supply / residence time

fresh-mineral supply + residence
 -> W_chem
```
경로를 별도 state로 유지해야 한다.

즉 식생효과가 존재하더라도 erosion/mineral-residence control에 의해 가려질 수 있다.

# 새로운 coupling이 필요한 부분
SWEHR/Landlab annual erosion/deposition에서:
- fresh-mineral fraction
- mineral residence proxy
를 chemical-weathering engine에 넘기는 것은 NEW COUPLING이다.

# 한계
- New Zealand alpine setting
- lithology/site-specific
- dynamic vegetation 없음
- vegetation class와 elevation/climate가 공변
- postfire 100-year transient가 아님

# 최종 판정
- **핵심 채택: erosion/mineral-residence control can dominate vegetation signal**
- vegetation-sensitive weathering multiplier 금지 강화
- hillslope transport -> chemistry feedback의 핵심 field evidence

# 참고 링크 / DOI
https://doi.org/10.1016/j.epsl.2023.118036
