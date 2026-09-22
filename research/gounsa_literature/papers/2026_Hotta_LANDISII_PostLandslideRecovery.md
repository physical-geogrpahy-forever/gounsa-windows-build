# 서지정보
Hotta, W., Morimoto, J., Haga, C., & Nakamura, F. (2026). Evaluating the factors determining long-term post-landslide forest recovery using a spatially explicit forest landscape model. *Ecological Modelling, 521*, 111718. https://doi.org/10.1016/j.ecolmodel.2026.111718

# 이 논문을 찾은 이유
LANDIS-II/NECN을 실제 지형교란 환경에 적용하거나 수정한 선행연구가 있는지 확인하기 위해 검토했다.

# 연구 유형
- spatially explicit forest landscape simulation
- modified LANDIS-II NECN
- post-landslide forest recovery

# 적용환경
- mountain forest landslide slopes
- >100 yr recovery horizon

# 핵심 수정
공개 branch `whotta/Extension-NECN-Succession:ForLandslide` source inspection:
- slope angle as site variable
- soil depth map
- soil moisture map
- slope-dependent establishment probability
- establishment threshold AGB
- establishment threshold slope angle

# 핵심 식 구조
Slope affects establishment while vegetation remains below a recovery biomass threshold.

Source implementation:
```
if biomass < threshold and slope <= threshold_angle:
    establishment *= slope_adjustment
elif biomass >= threshold and slope <= threshold_angle:
    establishment *= base_adjustment
else:
    establishment = 0
```

# 토심
Soil depth is a site input and affects NECN bucket-water storage:
```
waterFull = soilDepth * fieldCapacity
waterEmpty = wiltingPoint * soilDepth
```

# 중요한 한계
Source inspection did not show soil depth or slope being dynamically updated by erosion/deposition.
Thus this is not a two-way vegetation-geomorphology evolution model.

# 고운사에 사용할 수 있는 부분
Strong precedent for:
```
slope / soil depth / soil moisture
 -> LANDIS-II establishment and recovery
```

This makes it defensible for an external geomorphic model to update soil-depth/topographic state and feed those states back to LANDIS-II.

# 새로운 coupling
The opposite direction:
```
LANDIS-II roots/litter/cohorts
 -> geomorphic erosion/weathering/landsliding
```
requires separate published geomorphic models.

# 최종 판정
**핵심 LANDIS-II–geomorphic-state precedent.**
Not itself a geomorphic erosion model.

# DOI / source
https://doi.org/10.1016/j.ecolmodel.2026.111718
Public modified source:
https://github.com/whotta/Extension-NECN-Succession/tree/ForLandslide
