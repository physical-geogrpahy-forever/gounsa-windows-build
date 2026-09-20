# 서지정보
Doten, C. O., Bowling, L. C., Lanini, J. S., Maurer, E. P., & Lettenmaier, D. P. (2006). *A spatially distributed model for the dynamic prediction of sediment erosion and transport in mountainous forested watersheds*. Water Resources Research, 42, W04417. DOI: 10.1029/2004WR003829.

# 이 논문을 찾은 이유
산림 산지에서 hydrology, vegetation, surface erosion, mass wasting, roads, fire scenario를 함께 다루는 distributed model이 고운사 유수침식 본체를 대체할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- spatially distributed hydrology-sediment numerical model
- DHSVM extension
- forest-management/fire scenario model

# 공간 구조
- watershed raster
- kinematic-wave overland flow
- surface sediment continuity solved spatially
- water/sediment routing proceeds from higher grid cells downslope
- genuine 2D SWE momentum field로 분류하지 않음

# 적용 환경
- Rainy Creek, east slopes of Cascade Mountains
- temperate mountainous forest
- roads
- basin-wide fire scenario

# 핵심 과정
- hillslope surface erosion
- road erosion
- mass wasting
- debris-flow routing
- channel sediment routing
- rainfall/leaf-drip detachment
- overland-flow detachment

# 식생 입력
Surface erosion uses:
- fractional overstory/understory vegetation cover
- throughfall and leaf-drip momentum
- empirical soil erodibility

Mass wasting uses:
- vegetation-dependent root cohesion

Fire scenario:
- understory removed
- overstory LAI set to 1
- root cohesion reduced by 2 kPa
- these changes held constant for six years

# 핵심 식
Surface erosion sediment continuity is based on finite-difference conservation of sediment mass.

Rainfall detachment is proportional to vegetation cover, throughfall/leaf-drip momentum and soil erodibility.

Flow detachment:
```
D_of = beta_de * Delta y * v_s * TC
```
where beta_de is empirical detachment efficiency and TC transport capacity.

The authors explicitly state rill erosion is not physically represented; beta_de implicitly accounts for enhanced detachment due to flow concentration.

# 파라미터와 단위
- root cohesion: kPa
- sediment concentration and transport-capacity variables
- detachment efficiency beta_de
- LAI and fractional cover

# 원 논문의 구현 범위
Dynamic prediction of major sediment sources in a mountain forest watershed and management/disturbance scenarios.

# 고운사에 직접 사용할 수 있는 부분
1. strong mountain-forest distributed sediment-model precedent
2. explicit forest-fire scenario integrating hydrology, surface erosion and root cohesion
3. shows why cover-based forest erosion models are insufficient for our strict biomass requirement

# 새로운 coupling이 필요한 부분
Dynamic LPJ-GUESS biomass/root states replacing fixed cover/LAI/root cohesion would be **새로운 coupling**.

# 한계
- surface erosion vegetation effect is cover-based
- rill erosion is implicit in calibrated detachment efficiency
- fire vegetation change is held fixed for six years, not dynamic recovery
- not genuine 2D SWE
- root cohesion affects mass wasting, not surface erosion resistance

# 최종 판정
- **mountain forest/postfire benchmark**
- final strict water-erosion engine: 탈락
- useful validation architecture and counterexample to cover-only approaches

# 참고 링크 / DOI
https://doi.org/10.1029/2004WR003829
