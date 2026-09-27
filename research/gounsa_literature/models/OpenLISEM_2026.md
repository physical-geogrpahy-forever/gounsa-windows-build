# OpenLISEM — current 2026 model status

## 확인 시점
2026-09-28

## 현재 공개 버전
- stable/current release line includes 7.4.9 (2026-02)
- 7.5.0 beta releases in 2026-03 to 2026-05
- open-source code on GitHub / binaries on SourceForge

## 공간구조
- raster distributed model
- 1D kinematic runoff option
- 2D diffusive/dynamic shallow-water flow options based on FullSWOF lineage
- catchment-scale runoff, flooding, channel flow and sediment dynamics

## 수문
- full water balance
- interception
- evapotranspiration
- Green-Ampt infiltration
- SWATRE infiltration/soil-water option
- recent 7.4.9 line added experimental 3-layer Green-Ampt infiltration and redistribution
- time-series rainfall input; simulation time/output expressed in minutes and solver timestep user/numerically controlled

## 유사/입도
- splash/runoff/channel/flood sediment dynamics
- suspended load and bedload options
- median grain-size or multiple grain-size classes
- user-defined or estimated GSD
- detachable material depth / dynamic soil properties

## 최신 2026 기능 중 관련사항
- dynamic crusting separated from static crusting
- SWATRE and Green-Ampt parameter handling improvements
- MUSCL 2D flow rewrite in v7.4 line
- continued sediment-class and 2D-flow support

## 고운사와의 적합성
장점:
- actively maintained 2026 software
- catchment hydrology + infiltration + 2D flow + multiclass sediment를 하나의 framework에서 운용
- forest/mountain catchment event modelling에 구조적으로 적합
- external rainfall time series can be supplied; hourly forcing can be represented even though internal numerical time steps are smaller

핵심 한계:
- surface coarse-fragment **physical weathering/fragmentation** module 확인되지 않음
- dynamic surface GSD가 Green-Ampt/SWATRE hydraulic parameters를 자동 갱신하는 기능 확인되지 않음
- rock-fragment cover/embeddedness를 별도 armour-hydrology state로 다루는 기능 확인되지 않음
- large spall fragments/dry-ravel particle routing은 별도 coupling 필요

## 최종 판정
- **현재 유지보수되는 통합 hydrology + 2D flow + multiclass sediment software 후보**
- 고운사 hydrology/erosion framework로 재검토 가치가 큼
- 그러나 표면 암편 풍화와 GSD→infiltration feedback을 해결하는 단일 모델은 아님

## 출처
- https://github.com/vjetten/openlisem
- https://sourceforge.net/projects/lisem/
