# MIN3P root-reactive-transport lineage

## 목적
Spatial root state와 reactive transport를 직접 결합하는 mechanistic root-soil chemistry model lineage.

## Gérard et al. 2017
ArchiSimple -> spatial root architecture -> root surface density per control volume -> MIN3P -> uptake + pH + transport + mineral dissolution

- 2D soil domain
- 7500 control volumes
- dynamic root update
- multicomponent reactive transport

## 핵심 interface
고운사에서 chemistry engine에 넘길 식생 상태는 다음처럼 depth/spatially resolved 되어야 한다.
- root surface density
- RLD
- layer-wise fine-root biomass
- water/nutrient uptake by depth
- root-induced chemical source/sink terms

## 고운사 적용 시 주의
LPJ-GUESS FineRootC -> root surface density 변환은 published MIN3P 기능이 아니라 NEW COUPLING.

## 부족한 점
- hillslope routing 없음
- geomorphic erosion/deposition 없음
- forest succession engine 없음
- application chemistry가 sandstone forest와 다름

## 최종 판정
- 채택
- 역할: root-state -> reactive-transport interface의 mechanistic reference