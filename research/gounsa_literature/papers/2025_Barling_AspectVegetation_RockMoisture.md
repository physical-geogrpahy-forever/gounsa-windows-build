# 서지정보
Barling, N., Callahan, R. P., Donaldson, A., Huang, M.-H., Rempe, D. M., Shahid, S., Smith, D., Giggy, L., Zimmer, M., et al. (2025). Greater Rock Moisture Deficits on a Pole-Facing Hillslope Due To Aspect-Related Variations in Vegetation Water Use. *Geophysical Research Letters, 52*(17), e2025GL115750. DOI: 10.1029/2025GL115750.

# 이 논문을 찾은 이유
aspect별 vegetation type 차이가 weathered-bedrock hydrology를 얼마나 직접적으로 바꾸는지 확인하고, aspect를 weathering multiplier가 아닌 vegetation-hydrology state로 처리할 근거를 찾기 위해 검토했다.

# 연구 유형
- paired-hillslope field experiment
- borehole NMR
- neutron probe
- time-lapse ERT

# 공간 구조
- opposing equator-facing and pole-facing hillslopes
- soil + saprolite + deep vadose zone
- near-ridge boreholes

# 적용 환경
- Arbor Creek, central California Coast Range
- Mediterranean oak savanna
- pole-facing: oak-dominated
- equator-facing: grass-dominated

# 핵심 과정
- aspect microclimate
- vegetation type
- rooting depth
- transpiration
- rock-moisture depletion
- deep vadose-zone storage

# 식생 입력
observed vegetation contrast:
- oak trees on pole-facing slope
- grasses on equator-facing slope

# 핵심 결과
일반 예상과 반대로:
```
equator-facing / grassy
= less and shallower moisture withdrawal

pole-facing / oak
= greater and deeper moisture withdrawal
```

Dynamic storage depth:
```
pole-facing ~9.5 m
equator-facing ~4.5 m
```

Winter-to-summer storage deficit:
```
pole-facing ~0.28 +/- 0.02 m
equator-facing ~0.17 +/- 0.01 m
```

즉 current deep moisture state는 insolation 자체보다 vegetation type/rooting/transpiration에 강하게 영향받을 수 있다.

# 고운사에 직접 사용할 수 있는 부분
매우 중요한 rule:

```
aspect
!= hydrologic dryness coefficient
```

고운사에서는:
```
aspect
 -> radiation/microclimate
 -> LPJ-GUESS vegetation
 -> root depth/transpiration
 -> soil/rock moisture
 -> flow residence
 -> W_chem
```
으로 처리해야 한다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS vegetation water use를 rock-moisture depth profile로 전달하는 것은 새로운 coupling.

# 한계
- direct weathering rate를 측정하지 않음
- oak vs grass vegetation contrast와 aspect가 공변
- semi-arid California
- current storage dynamics study

# 최종 판정
- **핵심 채택: aspect-vegetation-deep hydrology field constraint**
- direct aspect multiplier 금지 강화
- weathering에는 hydrologic intermediary를 통해 사용

# 참고 링크 / DOI
https://doi.org/10.1029/2025GL115750
