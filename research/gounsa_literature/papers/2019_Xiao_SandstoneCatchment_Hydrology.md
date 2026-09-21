# 서지정보
Xiao, D., Shi, Y., Brantley, S. L., Forsythe, B., DiBiase, R., Davis, K., & Li, L. (2019). Streamflow Generation From Catchments of Contrasting Lithologies: The Role of Soil Properties, Topography, and Catchment Size. *Water Resources Research, 55*(11), 9234-9257. DOI: 10.1029/2018WR023736.

# 이 논문을 찾은 이유
고운사와 관련성이 높은 temperate-forest sandstone catchment에서 lithology가 soil properties, hillslope length, storage and flow generation을 어떻게 바꾸는지 정량적으로 확인하고, weathering hydrology의 sandstone-specific structural controls를 정리하기 위해 검토했다.

# 연구 유형
- physics-based distributed hydrologic modeling
- paired-catchment comparison
- virtual swap experiments

# 공간 구조
두 인접 first-order catchment:
- Shale Hills: shale, 0.08 km2
- Garner Run: sandstone, 1.34 km2

# 적용 환경
- central Pennsylvania
- similar temperate climate
- both forested
- contrasting lithology/topography/soil properties

# 핵심 과정
- infiltration
- storage
- discharge
- soil hydraulic properties
- topography
- catchment size
- lithology
- boulder/colluvial structure

# 식생 입력
두 catchment 모두 deciduous broadleaf-dominated temperate forest.

Observed vegetation:
- Shale Hills had about 60% greater biomass
- maximum LAI about 19% larger than Garner Run
- both had higher biomass in valley floor than ridge top

Simulation itself used simplified/uniform LAI because detailed temporal LAI was unavailable.

# 핵심 결과

Garner Run sandstone catchment:
- lower drainage density
- extensive valley fill
- bouldery sandy soils
- longer hillslopes
- larger riparian zone
- larger dynamic storage

Reported maximum slope lengths:
```
GR north-facing ~357 m
GR south-facing ~670 m

SH north-facing ~115 m
SH south-facing ~126 m
```

With same soil/topography but larger catchment size:
```
dynamic storage
~0.12 m -> ~0.17 m
```

Virtual experiments showed soil properties were particularly important; transferring shale calibration directly to sandstone failed until sandstone-specific boulder/soil structure was represented.

# 고운사에 직접 사용할 수 있는 부분

## 1. sandstone is a hydrologic architecture, not just a reaction coefficient

```
sandstone lithology
 -> soil texture / boulders / porosity
 -> storage / connectivity
 -> residence time
 -> weathering
```

Therefore:
```
W_chem = f(lithology)
```
alone is insufficient.

## 2. hillslope length
Longer sandstone hillslopes can alter storage and transit context.

This supports Ferrier & Perron / Pedrazas hillslope-length controls.

## 3. vegetation feedback
Observed biomass varied with catchment and hillslope position, but the hydrologic simulations did not dynamically resolve vegetation.

For Gounsa:
```
LPJ-GUESS vegetation
 -> LAI / root water uptake / ET
 -> sandstone hydrologic structure
 -> W_chem
```
remains a NEW COUPLING.

# 새로운 coupling이 필요한 부분
- Gounsa sandstone soil/boulder state -> hydraulic parameters
- LPJ-GUESS ET/root uptake -> distributed hydrology
- hydrology -> residence-time/reactive transport

# 한계
- hydrology paper, not direct weathering-rate model
- Pennsylvania Tuscarora sandstone differs from Gounsa
- dynamic vegetation not modeled
- catchment-scale rather than individual hillslope-only experiment

# 최종 판정
- **핵심 보조 채택: forested sandstone catchment hydrologic architecture**
- lithology-specific hydraulic structure must precede weathering parameterization
- direct weathering coefficient source 아님

# 참고 링크 / DOI
https://doi.org/10.1029/2018WR023736
