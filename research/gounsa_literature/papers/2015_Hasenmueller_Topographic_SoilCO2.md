# 서지정보
Hasenmueller, E. A., Jin, L., Stinchcomb, G. E., Lin, H., Brantley, S. L., & Kaye, J. P. (2015). Topographic controls on the depth distribution of soil CO2 in a small temperate watershed. *Applied Geochemistry, 63*, 58-69. DOI: 10.1016/j.apgeochem.2015.07.005.

# 이 논문을 찾은 이유
사면 위치가 soil pCO2를 직접 조직화하고, 그 결과 carbonic-acid weathering potential이 공간적으로 달라지는지 확인하기 위해 검토했다.

# 연구 유형
- multi-year field soil-gas monitoring
- topographic catena comparison

# 공간 구조
- ridgetop
- planar midslope
- swale
- valley floor
- north/south aspect
- measurements from near surface to bedrock

# 적용 환경
- Susquehanna Shale Hills Critical Zone Observatory
- temperate forest
- shale-derived soils

# 핵심 과정
- soil respiration
- CO2 diffusion
- soil moisture
- soil depth
- texture/porosity
- topographic convergence
- carbonic-acid weathering potential

# 식생 입력
- living forest vegetation
- roots and microorganisms as CO2 sources
- litter as heterogeneous C input

dynamic vegetation model은 아니다.

# 핵심 결과
Topographic position was the strongest predictor of soil pCO2.

Valley floor and swales:
- deeper soils
- wetter conditions
- lower gas diffusivity
- higher pCO2

Ridgetop and planar slopes:
- shallower soils
- drier conditions
- higher CO2 diffusion
- lower pCO2

Observed hillslope variation in pCO2 was nearly sevenfold.

High pCO2 in wetter/deeper positions could lower porewater pH by up to about 1 pH unit relative to water equilibrated with atmospheric CO2.

Aspect itself was a weaker predictor than catena position and moisture/depth.

# 고운사에 직접 사용할 수 있는 부분
매우 중요한 spatial rule.

Do not calculate:

```
pCO2 = f(root respiration only)
```

because concentration also depends on:
- soil depth
- moisture
- porosity
- gas diffusion
- convergence/topographic position

Thus:

```
LPJ-GUESS CO2 production
+
terrain/hydrologic gas-retention state
 -> pCO2
 -> W_chem
```

is more defensible.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root/litter respiration source를 terrain-dependent CO2 production/diffusion model로 변환하는 것은 NEW COUPLING이다.

# 한계
- shale
- soil profile mostly above bedrock
- chemical weathering flux directly measured하지 않음
- pCO2 effect on weathering inferred from known chemistry

# 최종 판정
- **핵심 채택: topographic control on soil pCO2 weathering driver**
- hillslope catena state must influence CO2 retention/diffusion
- direct aspect multiplier는 부적절

# 참고 링크 / DOI
https://doi.org/10.1016/j.apgeochem.2015.07.005
