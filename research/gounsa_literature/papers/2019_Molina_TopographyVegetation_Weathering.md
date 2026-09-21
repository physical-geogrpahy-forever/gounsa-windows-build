# 서지정보
Molina, A., Vanacker, V., Corre, M. D., & Veldkamp, E. (2019). Patterns in Soil Chemical Weathering Related to Topographic Gradients and Vegetation Structure in a High Andean Tropical Ecosystem. *Journal of Geophysical Research: Earth Surface, 124*(2), 666-685. DOI: 10.1029/2018JF004856.

# 이 논문을 찾은 이유
고운사에서 사면 위치와 식생 구조가 chemical weathering을 함께 제어하는지 직접 검증한 hillslope-scale field study를 찾기 위해 검토했다.

# 연구 유형
- hillslope toposequence field study
- geochemical mass balance
- vegetation-topography comparison

# 공간 구조
10개 soil toposequence:
- shoulder
- backslope
- toeslope

총 30 soil profiles.

Vegetation types:
- tussock grass
- cushion-forming plants
- native Polylepis forest

# 적용 환경
- high Andean tropical catchment
- andesitic parent material
- postglacial volcanic soils

# 핵심 과정
- topographic convergence/divergence
- soil-water residence time
- dissolved and particulate redistribution
- soil chemical weathering
- soil organic C
- vegetation structure
- soil hydrology
- regolith volumetric strain

# 식생 입력
- vegetation type / structure
- forest vs grass vs cushion vegetation
- soil organic carbon association
- vegetation-controlled infiltration, transpiration and preferential flow

# 핵심 결과

## topographic pathway
논문은 hillslope position이:
```
surface and subsurface flow
water residence time
particle redistribution
solute redistribution
```
를 통해 soil weathering을 바꿀 수 있음을 명시한다.

Downslope에서 일반적으로 더 긴 subsurface flow path와 water residence time이 가능하지만, long residence time이 chemical equilibrium에 접근하면 in-situ weathering flux가 계속 증가하지 않을 수도 있다.

따라서:
```
downslope
!= automatically more weathering rate
```

## vegetation pathway
soil weathering extent는 vegetation type과 유의하게 연결되었다.

Forest soils는 cushion-plant soils보다:
- Ca, K, Na, Si, Fe mass-transfer patterns
- acidity
- total mass loss
에서 뚜렷한 차이를 보였다.

Soil organic C와 volumetric strain의 연관성은 biotic agents가 weathering 동안 regolith dilation에 기여할 수 있음을 시사한다.

## coupled interpretation
Vegetation과 hydrology가 서로 독립이 아니다.

```
topography
 -> moisture / convergence / saturation
 -> vegetation pattern
 -> infiltration / transpiration / rooting
 -> water residence / chemistry
 -> weathering
```

이라는 coupled hillslope system이다.

# 파라미터와 단위
- total mass loss [kg m^-2]
- mass-transfer coefficients
- soil pH
- soil organic C
- total porosity
- volumetric strain
- soil profile depth

# 원 논문의 구현 범위
field pattern analysis이며 실행형 process model은 아니다.

# 고운사에 직접 사용할 수 있는 부분
매우 중요하다.

고운사에서는 chemical weathering을 cell-independent chemistry만으로 계산하지 않고 최소한:

```
hillslope position
flow convergence/divergence
water residence time
vegetation state
```

의 상호작용을 sensitivity 또는 production hydrology에 반영할 근거가 된다.

또한:
```
vegetation
<-> hillslope hydrology
<-> weathering
```
을 하나의 feedback으로 봐야 한다는 직접 hillslope evidence.

# 새로운 coupling이 필요한 부분
LPJ-GUESS vegetation state와 Landlab/BioRT hillslope hydrology를 weathering engine에 전달하는 것은 새로운 coupling이다.

# 한계
- andesitic volcanic soils
- high-Andean ecosystem
- field correlations and mass balance, not a causal numerical vegetation-weathering model
- forest effect와 hydrologic site effect가 일부 공변

# 최종 판정
- **채택: hillslope topography + vegetation + weathering 핵심 field constraint**
- 사면 위치별 hydrology-weathering coupling을 production/sensitivity에 넣는 핵심 근거
- coefficient source로 직접 사용하지 않음

# 참고 링크 / DOI
https://doi.org/10.1029/2018JF004856
