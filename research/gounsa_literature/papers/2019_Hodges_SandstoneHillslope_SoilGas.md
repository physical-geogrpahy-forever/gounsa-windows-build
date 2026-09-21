# 서지정보
Hodges, C., Kim, H., Brantley, S. L., & Kaye, J. (2019). Soil CO2 and O2 Concentrations Illuminate the Relative Importance of Weathering and Respiration to Seasonal Soil Gas Fluctuations. *Soil Science Society of America Journal, 83*(4), 1167-1180. DOI: 10.2136/sssaj2019.02.0049.

# 이 논문을 찾은 이유
고운사와 관련성이 높은 **temperate forest sandstone hillslope**에서 lithology와 hillslope position이 soil pCO2/pO2를 어떻게 바꾸는지 직접 확인하고, root respiration-derived CO2와 gas transport를 chemical-weathering interface에 넣을 근거를 찾기 위해 검토했다.

# 연구 유형
- multi-season soil-gas field monitoring
- paired lithology/catena comparison
- apparent respiratory quotient analysis

# 공간 구조
- ridgetop / midslope / valley floor
- multiple soil depths from surface to bedrock
- paired shale and sandstone watersheds

# 적용 환경
- Susquehanna/Shale Hills Critical Zone Observatory region, Pennsylvania
- humid temperate forest
- shale catchment
- **sandstone catchment**

# 핵심 과정
- root/soil respiration
- CO2 production
- O2 consumption
- gas diffusion
- seasonal redox
- lithology-dependent macroporosity
- hillslope-position effects

# 식생 입력
- temperate forest roots and soil biological respiration
- no dynamic vegetation model

# 핵심 결과

Both lithology and hillslope position significantly affected soil gas composition.

Valley floors:
```
pCO2 > 5%
pO2 < 16%
```
in some observations.

Controlling for depth, the sandstone watershed showed:
```
higher pCO2
lower pO2
```
than the shale watershed.

The authors attribute this partly to higher macroporosity in the sandstone system, allowing deeper rooting and greater root respiration at depth.

Seasonally, ARQ varied:
- >1 in wetter late-growing-season periods
- <1 in early spring

suggesting alternating anaerobic respiration and oxidation of reduced species.

# 고운사에 직접 사용할 수 있는 부분

매우 중요한 sandstone-specific gas constraint.

```
sandstone profile structure / macroporosity
 -> root depth / respiration
 -> pCO2 / pO2
 -> weathering reaction environment
```

Therefore:

```
R_CO2
!=
pCO2
```

and pCO2 requires:
- source strength
- depth
- moisture
- porosity
- gas diffusivity
- hillslope position

O2 should also be retained at least in advanced sensitivity because redox/weathering pathways can change seasonally.

# new coupling needed

Gounsa candidate:

```
LPJ-GUESS root/belowground respiration(z,t)
+
sandstone porosity/fracture state
+
soil/rock moisture
+
gas diffusion
 -> pCO2(z,t), pO2(z,t)
 -> mineral weathering
```

This is a NEW COUPLING.

# 한계
- soil gas study, not direct whole-rock weathering-rate measurement
- Pennsylvania sandstone differs from Gounsa
- dynamic forest succession not modeled
- annual postfire disturbance not included

# 최종 판정
- **핵심 채택: sandstone forest hillslope gas-chemistry constraint**
- root respiration and gas transport must be separated
- pCO2/pO2 spatial state gains priority in advanced chemistry
- coefficient direct transfer prohibited

# 참고 링크 / DOI
https://doi.org/10.2136/sssaj2019.02.0049
