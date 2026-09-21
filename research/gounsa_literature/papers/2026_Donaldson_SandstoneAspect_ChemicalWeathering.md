# 서지정보
Donaldson, A., Callahan, R. P., Barling, N., Rempe, D. M., Huang, M.-H., & Zimmer, M. (2026). Neighboring Ridgetops With Distinct Weathering Drivers Have Strikingly Similar Saprolite Chemical Weathering. *Journal of Geophysical Research: Earth Surface, 131*(4), e2025JF008348. DOI: 10.1029/2025JF008348.

# 이 논문을 찾은 이유
고운사와 매우 관련성이 높은 sedimentary/sandstone hillslope에서 vegetation, water cycling, topographic relief, fracturing이 chemical weathering profile을 실제로 어떻게 결정하는지 확인하기 위해 검토했다.

# 연구 유형
- paired-ridgetop deep drilling
- geochemistry
- physical rock characterization
- hydrologic monitoring
- natural experiment

# 공간 구조
- neighboring ridgetops
- 6-40 m boreholes
- soil / saprolite / fractured bedrock / fresh bedrock
- pole-facing oak slope vs equator-facing grassy slope

# 적용 환경
- Arbor Creek, central California Coast Range
- coarse-grained metagreywacke sandstone
- shale interbeds
- Franciscan/Yolla Bolly sedimentary terrain
- thin soil 30-80 cm
- slopes around 24°

# 핵심 과정
- chemical depletion
- saprolite development
- fracture density
- root-rock interaction
- vadose-zone water cycling
- groundwater control
- paleoenvironmental legacy

# 식생 입력
natural vegetation contrast:
- pole-facing ridgetop: oak trees
- equator-facing ridgetop: grasses

No dynamic vegetation model.

# 핵심 결과

## shallow weathering
두 ridgetop은:
- topographic relief
- current vegetation
- water cycling
- fracture density

가 뚜렷이 다른데도:

```
<5 m shallow chemical-weathering magnitude
```
가 놀랍게 유사했다.

저자 해석:
```
Pleistocene cooler/wetter climate
+ historically wider tree cover
 -> legacy shallow weathering
```

가능성이 큼.

## deep weathering
차이는 주로:
```
5-25 m fractured bedrock
```
에서 강해졌으며 fracture density가 깊은 chemical reactions에 중요했다.

## basal control
Chemical depletion는 두 ridgetop 모두 stream-channel elevation까지 연장되었고 current water table과 일치했다.

즉:
```
groundwater
 -> weathering initiation depth
```
라는 bottom-up control이 강함.

## mass transfer
paper uses elemental mass-transfer coefficient:

```
tau_x
=
(X_regolith / X_protolith)
(I_protolith / I_regolith)
- 1
```

Bulk tau:
```
tau_b
=
(I_protolith / I_regolith)
- 1
```

# 고운사에 직접 사용할 수 있는 부분
이번 조사에서 가장 중요한 자료 중 하나.

### 100-year initialization rule
금지:
```
current vegetation
 -> reset whole weathering profile to equilibrium
```

대신:
```
inherited Z_weathering(x,y,t0)
+ inherited fracture/mechanical state
+ 100-year incremental vegetation/hydrology-driven change
```
로 간다.

### direct vegetation effect
현재 oak vegetation이 더 깊은 root-rock interaction과 water cycling을 만들더라도 누적 shallow chemical weathering은 paleo legacy에 의해 overprinted될 수 있다.

따라서 100년 postfire model에서는 식생효과를:
```
incremental W_chem
```
에 적용하고 inherited saprolite thickness 전체에 적용하지 않는다.

### fracture state
```
fracture density
```
를 chemical weathering / deep flow sensitivity에 포함할 강한 근거.

# 새로운 coupling이 필요한 부분
- LPJ-GUESS vegetation -> incremental W_chem
- Landlab/initial geology -> inherited weathering-front and fracture state
- groundwater level -> bottom-up weathering-front constraint

모두 새로운 coupling이다.

# 한계
- present and paleo vegetation effects가 누적되어 causal isolation 어려움
- metamorphosed sandstone setting
- current study interval 자체는 annual weathering-rate experiment가 아님
- Gounsa coefficient direct transfer 금지

# 최종 판정
- **핵심 채택: sandstone hillslope vegetation-hydrology-weathering + legacy constraint**
- 100-year initial-condition architecture를 직접 수정하는 수준의 근거
- direct biomass weathering multiplier를 강하게 반박
- fracture density / water table state 중요도 상승

# 참고 링크 / DOI
https://doi.org/10.1029/2025JF008348
