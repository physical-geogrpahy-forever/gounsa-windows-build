# 서지정보
Wen, H., Sullivan, P. L., Billings, S. A., et al. (2022). From Soils to Streams: Connecting Terrestrial Carbon Transformation, Chemical Weathering, and Solute Export Across Hydrological Regimes. *Water Resources Research, 58*, e2022WR032314. DOI: 10.1029/2022WR032314.

# 이 논문을 찾은 이유
고운사처럼 사면에서 topography와 hydrologic flow path가 chemical weathering 및 solute export에 미치는 영향을 2D reactive transport로 다룬 온대 산림 사례를 찾기 위해 검토했다.

# 연구 유형
- 2D hillslope reactive transport model
- field-calibrated hydro-biogeochemical modeling

# 공간 구조
- 2D hillslope
- shallow and deep flow paths
- lateral stream export
- vertical gas export

# 적용 환경
- Fitch Forest, Kansas
- temperate forest / grassland ecotone

# 핵심 과정
- soil organic-carbon transformation
- soil CO2
- carbonate/silicate weathering
- DOC/DIC production and export
- hydrologic flow paths
- water residence time
- lateral and vertical transport

# 식생 입력
dynamic vegetation model은 없음.

식생/토양 생물활동은:
- soil organic carbon
- soil respiration / CO2
- ET-adjusted discharge forcing
형태로 반영된다.

# 핵심 식
핵심 구조:

```
hydrologic regime
 -> flow-path depth
 -> residence time
 -> carbon transformation
 -> mineral weathering / precipitation
 -> lateral + vertical solute flux
```

논문에서는 dry vs storm conditions와 permeability contrasts를 비교한다.

Silicate weathering은 느린 kinetics 때문에 carbonate보다 hydrologic sensitivity가 작았지만, dry conditions의 높은 acidity와 긴 residence time에서 더 높은 rate를 보였다.

# 파라미터와 단위
- discharge forcing [mm d^-1]
- water-table depth
- porosity
- soil OC abundance
- mineral kinetics
- soil CO2 and water chemistry calibration

# 원 논문의 구현 범위
2D hillslope에서 soil carbon transformations, chemical weathering, solute export를 함께 계산.

# 고운사에 직접 사용할 수 있는 부분
매우 유용한 spatial precedent다.

고운사에서:
```
DEM / slope
 -> subsurface flow paths
 -> residence time
 -> W_chem
```
경로를 무시하면 안 된다는 근거.

따라서 WITCH/PROFILE을 각 cell 독립으로만 돌리는 접근의 한계를 평가하는 benchmark로 사용한다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS와:
- soil CO2
- OC inputs
- ET
- root-zone depth
를 2D RTM에 전달하는 것은 새 coupling.

# 한계
- vegetation succession은 직접 모의하지 않음
- carbonate chemistry 비중이 큰 application
- geomorphic boundary lowering은 직접 계산하지 않음

# 최종 판정
- **채택: 2D hillslope hydrology-weathering coupling benchmark**
- 고운사 공간모델의 flow-path sensitivity 검증에 우선 사용

# 참고 링크 / DOI
https://doi.org/10.1029/2022WR032314
