# 고운사 기존모델 사용가능성 재감사

날짜: 2026-09-22

## 목적
새 coupling을 먼저 만들지 않고, 기존 published model 자체가 고운사 요구조건을 어디까지 충족하는지 다시 검증한다.

## 1. CAESAR-Lisflood

### 자체 구현
- reduced 2D hydrodynamics via LISFLOOD-FP
- rainfall catchment mode via TOPMODEL
- up to 9 grain-size fractions
- surface and subsurface active layers
- dynamic armouring
- erosion/deposition
- DEM evolution
- hours to millennia
- public source code

### 부족
- quantitative root biomass/RLD 없음
- litter biomass dynamics 없음
- PFT-specific vegetation 없음
- vegetation is maturity / erosion-proportion / critical-shear style
- explicit stony-soil Richards hydrology 없음

### 판정
**강한 single-engine comparator / armour-profile candidate**
하지만 고운사 전체 production model로 바로 채택하지 않음.

## 2. SSSPAM / mARM

### 자체 구현
- particle-size-resolved surface armour
- multilayer embedded PSD
- subsurface resupply
- erosion/deposition profile mass balance
- physical weathering
- soil-depth/profile evolution
- DEM evolution
- mARM5D public source code

### 부족
- fluvial erosion law 자체가 calibrated landscape-evolution relation
- rainfall vs flow detachment 분리 약함
- quantitative root biomass/RLD/litter erosion module 없음
- event-scale genuine 2D hydrodynamics 약함

### 판정
**가장 강한 existing armour/profile/weathering engine 후보**
하지만 단독 water-erosion production model로는 부족.

## 3. 현재 남겨둘 정밀검증 후보
1. CAESAR-Lisflood
2. SSSPAM/mARM
3. Iber+

이 셋을 먼저 완전히 검증한다.
OpenLISEM, PSEM_2D, SERGHEI-SE, Wu 2D, WEPP 등은 특정 기능 비교용으로 두되,
이 세 모델 검증 전에 새 coupling의 중심으로 올리지 않는다.

## 원칙
- 모델 자체 구현과 새로운 coupling을 혼동하지 않는다.
- 적용범위 밖 parameterization을 가져오지 않는다.
- 논문에 없는 vegetation/root relation을 발명하지 않는다.
- 전체 model 채택은 각 후보의 자체 기능 감사가 끝난 후에만 결정한다.
