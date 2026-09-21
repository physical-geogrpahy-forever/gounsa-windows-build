# 서지정보
Milodowski, D. T., Mudd, S. M., & Mitchard, E. T. A. (2015). Erosion rates as a potential bottom-up control of forest structural characteristics in the Sierra Nevada Mountains. *Ecology, 96*(1), 31-38. DOI: 10.1890/14-0649.1.

# 이 논문을 찾은 이유
고운사에서 풍화와 토양두께가 식생에 영향을 주는 반대방향 feedback:
```
geomorphology/weathering -> forest structure
```
의 현장근거를 확인하기 위해 검토했다.

# 연구 유형
- LiDAR forest-structure analysis
- field plots
- erosion-gradient natural experiment

# 공간 구조
- Sierra Nevada mountain basins
- mixed coniferous/deciduous forest
- order-of-magnitude erosion-rate gradient

# 적용 환경
- northern California Sierra Nevada
- actively eroding mountain forest

# 핵심 과정
- long-term erosion
- slope steepness
- weathering-zone depth/extent
- soil/saprolite moisture storage
- nutrient availability
- aboveground biomass

# 식생 입력
- AGB
- canopy/forest structure
- field plot biomass
- no dynamic vegetation model

# 핵심 결과
mean basin slope, used as an erosion-rate proxy, explained about:
```
32% of AGB variance
```
with P < 0.001.

This geomorphic association outweighed the effects of:
- mean annual precipitation
- temperature
- bedrock lithology
within the study area.

Interpretation:
```
higher erosion
 -> steeper topography
 -> thinner / less extensive weathering zone
 -> reduced moisture storage and nutrient availability
 -> lower forest AGB
```

# 고운사에 직접 사용할 수 있는 부분
매우 중요한 reverse feedback:

```
erosion / soil loss
 -> H_AB and weathered-rock storage
 -> water/nutrient availability
 -> LPJ-GUESS biomass/root recovery
```

따라서 geomorphic state가 LPJ-GUESS로 되돌아가는 return coupling에는:
- soil thickness
- weathered-rock water storage
- nutrient state
를 포함할 근거가 있다.

# 새로운 coupling이 필요한 부분
Landlab/SWEHR state를 LPJ-GUESS rooting/water/nutrient domain으로 되돌리는 것은 새로운 coupling이다.

# 한계
- erosion proxy가 mean basin slope
- observational association
- annual postfire dynamics 아님
- direct soil-production equation 없음

# 최종 판정
- **채택: geomorphology/weathering -> forest-structure feedback 핵심 field evidence**
- vegetation-sensitive soil-production과 함께 양방향 eco-geomorphic loop를 완성하는 근거
- coefficient source가 아님

# 참고 링크 / DOI
https://doi.org/10.1890/14-0649.1
