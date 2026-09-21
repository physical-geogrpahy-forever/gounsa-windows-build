# 서지정보
Schaller, M., & Ehlers, T. A. (2022). Comparison of soil production, chemical weathering, and physical erosion rates along a climate and ecological gradient (Chile) to global observations. *Earth Surface Dynamics, 10*, 131-150. DOI: 10.5194/esurf-10-131-2022.

# 이 논문을 찾은 이유
식생량과 기후가 hillslope soil production, chemical weathering, physical erosion에 각각 어떤 관계를 갖는지 실제 관측자료와 global compilation으로 검증하고, Pelak biomass-soil production formulation의 relevance를 확인하기 위해 검토했다.

# 연구 유형
- field cosmogenic-nuclide / geochemical mass balance
- climate-ecological transect
- global data compilation
- competing model comparison

# 공간 구조
- granitoid soil-mantled hillslope pedon locations
- Chilean Coastal Cordillera climate/ecological gradient
- global hillslope compilation

# 적용 환경
4 Chilean zones:
- arid
- semi-arid
- Mediterranean
- temperate humid

vegetation ranges from sparse to forested.

# 핵심 과정
- soil production
- chemical weathering
- physical erosion
- denudation
- climate
- vegetation cover / LAI / NPP / rooting variables

# 식생 입력
compiled vegetation variables include:
- vegetation fraction
- LAI
- NPP
- rooting depth
- evapotranspiration

# 핵심 관측
Chilean soil production:
```
~7-290 t km^-2 yr^-1
```

chemical weathering:
```
0-211 t km^-2 yr^-1
```

physical erosion:
```
~11-91 t km^-2 yr^-1
```

Rates change nonlinearly across precipitation/ecological gradient.

Important conclusion:
observed variation in soil production rates most closely resembled models explicitly accounting for:
```
soil thickness
+
biomass
```

Chemical weathering did not monotonically increase with vegetation/climate. In temperate settings, vegetation could reduce physical erosion and to some extent chemical weathering.

# Pelak formulation comparison
The paper/supplement reconstructs Pelak et al. 2016 as:

```
P(h,b)
=
[P0 + Pv b(h)] exp(-ks h)
```

with vegetation equilibrium response:

```
b(h)
=
(r/m)[1-exp(-kg h)]
```

The supplement reports Pelak parameter examples but notes unit adjustments in the comparison.

Therefore these coefficients are **not copied to Gounsa**.

# 고운사에 직접 사용할 수 있는 부분
Strong empirical/model-comparison support that:
```
P_sand
```
may require both soil depth and vegetation state to explain broad hillslope variation.

However:
```
biomass ↑
!= chemical weathering ↑ monotonically
```

Thus physical/regolith-production vegetation effect and chemical-weathering vegetation effect must remain distinct.

# 새로운 coupling이 필요한 부분
A Gounsa sandstone version:

```
P_sand(H, vegetation)
```

would be a new coupling and requires sandstone/site calibration.

LPJ-GUESS total biomass cannot be inserted into Pelak coefficients without matching the biomass definition and units.

# 한계
- granitoid-focused global comparison
- climatic and vegetation effects covary
- primarily long-term steady-state production rates
- not postfire transient
- Pelak equation tested as broad comparison, not site-calibrated sandstone process law

# 최종 판정
- **핵심 채택: soil thickness + biomass soil-production evidence**
- vegetation-sensitive Mode B sensitivity now deserves explicit testing
- no coefficient transfer to Gounsa

# 참고 링크 / DOI
https://doi.org/10.5194/esurf-10-131-2022
