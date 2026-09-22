# 결정: 고운사 dynamic armour는 SSSPAM/mARM 계보를 기반으로 한다

날짜: 2026-09-22

## 사용자 원칙
- 자의적 empirical coefficient를 만들지 않는다.
- 가능한 한 기존 published model과 공개 구현을 사용한다.
- 새로운 coupling이 필요하면 coupling 자체는 명시하되, process equation을 새로 발명하지 않는다.

## 핵심 결정
고운사의 dynamic armour / embedded rock-fragment profile / weathering / soil-depth evolution은 **ARMOUR -> mARM -> mARM3D/mARM5D -> SSSPAM 계보를 기본으로 한다.**

### 이유
이 계보는 이미 다음을 기존 모델로 구현한다.
- particle-size-resolved surface grading
- selective fine removal
- dynamic armour formation
- parent-to-daughter weathering transition
- multilayer embedded PSD
- subsurface resupply
- erosion/deposition mass balance
- soil-depth update
- DEM evolution

따라서 별도의 custom armour factor를 만들 이유가 없다.

## event hydrology/erosion engine
현재 우선후보는 OpenLISEM+SWATRE.

확인된 기존 기능:
- Richards-equation SWATRE
- theta-h-K lookup tables
- 2D SWOF surface flow
- rainfall/splash detachment
- flow detachment
- sediment transport/deposition
- static surface stone shielding
- litter interception and splash shielding

## OpenLISEM을 전체 장기모델로 쓰지 않는 이유
source inspection 결과:
- StoneFraction is static input
- material-depth evolution switch is currently disabled
- dynamic armour is not fully active
- some multiclass-sediment controls are inactive/commented
- root effect is cohesion input, not quantitative root-state dynamics

따라서 OpenLISEM은 **event-scale hydro-erosion engine**으로 사용하고, event 종료 후 actual erosion/deposition mass를 SSSPAM state updater로 넘긴다.

## 권장 구조
```
LPJ-GUESS vegetation state
        |
        | rainfall interception / litter / root-related resistance inputs
        v
OpenLISEM + SWATRE
  - theta-h-K based soil water
  - 2D surface flow
  - splash / flow detachment
  - erosion / deposition mass
        |
        | E_a(x,y), D_a(x,y)
        v
SSSPAM / mARM3D state updater
  - size-class selective removal
  - surface armour
  - embedded PSD
  - profile resupply
  - weathering transition
  - soil depth
  - DEM
        |
        +------------------------------+
        |                              |
        v                              v
next-event soil hydraulic state    vegetation soil-depth/moisture state
```

## 자의성이 남는 부분
이 구조에서도 완전히 사라지지 않는 부분이 있다.

### 1. OpenLISEM root resistance
OpenLISEM의 root cohesion input과 LPJ-GUESS FineRootC 사이에는 direct published mapping이 없다.
따라서 기존 WEPP/root-detachment 또는 별도 measured root-cohesion relation을 찾아야 한다.

### 2. litter
OpenLISEM은 litter cover fraction을 사용한다.
LPJ-GUESS SurfaceLitC -> litter cover conversion은 별도 published relation이 필요하다.

### 3. fire-spall source
fire severity -> spall mass/PSD는 아직 별도 published quantitative model이 필요하다.

### 4. SSSPAM weathering rate
원 parameter를 고운사에 이식하지 않는다.
Welivitiya & Hancock 2024의 experimental parameter-estimation method를 사용해 고운사 sandstone-specific rate를 얻는 방향.

## 대안 비교
### Iber+
장점:
- clean modern 2D hydrodynamics
- multiclass sediment/Exner architecture

단점:
- stony-soil Richards hydrology가 native가 아님
- dynamic embedded PSD/profile armour는 없음
- long-term profile coupling이 별도 필요

### OpenLISEM+SWATRE
장점:
- measured theta-h-K direct input
- Richards soil water + 2D surface flow + erosion in one existing codebase
- postfire applications already 존재

단점:
- dynamic armour/profile evolution 부족

### SSSPAM alone
장점:
- armour/profile/weathering/soil-depth/DEM 가장 강함

단점:
- D8, own fluvial erosion parameterisation requires calibration
- high-resolution event hydrodynamics 약함

## 현재 최종 선택
**OpenLISEM+SWATRE for event hydro-erosion + SSSPAM/mARM for long-term armour/profile evolution**

이것이 현재까지 조사한 범위에서:
1. 매립 석력이 많은 현장조건을 가장 잘 보존하고
2. 2D runoff를 유지하며
3. dynamic armour를 기존 model로 처리하고
4. arbitrary armour equation을 만들지 않는
가장 방어적인 구조이다.
