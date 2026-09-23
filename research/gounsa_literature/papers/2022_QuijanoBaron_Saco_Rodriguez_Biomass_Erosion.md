# Quijano-Baron, Saco & Rodriguez (2022)

## 서지정보
Quijano-Baron, J., Saco, P. M., & Rodriguez, J. F. (2022). Modelling the effects of above and belowground biomass pools on erosion dynamics. *Catena, 213*, 106123. https://doi.org/10.1016/j.catena.2022.106123

## 이 논문을 검색한 이유
고운사 통합모델에서 vegetation engine이 산출하는 leaf, root, litter, soil-C 상태를 실제 erosion/landform equations에 어떻게 연결할지에 대한 직접적인 선례를 찾기 위해 검토했다.

## 연구 유형
- coupled vegetation-hydrology-landform evolution modelling
- idealized 100-year numerical experiments
- daily forcing/state evolution
- open-forest / tropical savanna vegetation case

## 핵심과정
모델은 동적 hydrology, vegetation, biomass pools, landform evolution/erosion modules를 결합한다.

식생 biomass pools:
- leaves
- roots
- litter
- soil carbon

geomorphic effects:
1. root biomass -> soil erodibility 감소
2. leaf cover -> diffusive erosion 감소
3. litter -> overland-flow resistance 증가
4. soil carbon -> soil water retention 증가 -> runoff/erosion 변화

즉 식생을 하나의 cover coefficient로 줄이지 않고 서로 다른 biomass pools가 서로 다른 침식과정에 작용하도록 분리한다.

## 시간 및 적용규모
- daily data/process coupling
- idealized 100-year simulations
- tropical open-forest/savanna parameterization

이는 고운사의 `100-year + daily vegetation + storm/geomorph submodel` 구조와 시간규모가 매우 가깝다.

## 고운사에 사용할 수 있는 부분
이 논문의 가장 큰 가치는 식생엔진 자체가 아니라 coupling interface이다.

```text
vegetation engine
  leaf biomass / LAI
  root biomass
  litter
  soil C
        |
        v
geomorph engine
  erodibility
  diffusivity
  flow resistance
  soil-water retention
        |
        v
runoff / erosion / deposition / terrain
```

따라서 LPJ-GUESS SEC, FATES, EDYS 등 어느 vegetation engine을 선택하더라도 이 논문의 biomass-pool separation은 고운사 geomorphic coupling 설계에 사용할 수 있다.

## 고운사에서 필요한 확장
논문 식생모듈은 고운사에서 요구하는 species-rich herb-shrub-tree demographic succession engine이 아니다.

따라서 고운사에서는:
- cohort/PFT/species별 root biomass를 합성 또는 기능군별 분리
- litter quality/amount
- canopy/leaf pool
- soil-C state
를 geomorph equations에 연결해야 한다.

또한 산불 후 초기에는 vegetation cover와 root/litter 보호효과의 회복시점이 서로 다르므로 각 pool을 독립적으로 업데이트해야 한다.

## 한계
- 최종 vegetation-engine 후보가 아님
- rich succession/seed recruitment 없음
- published test is open-forest tropical savanna, not Korean temperate mountain forest
- high-resolution rill/channel network coupling은 별도 구현 필요

## 최종 판정
**매우 중요한 geomorph-coupling template / 생산 식생모델 후보는 아님.**

EDYS가 native erosion-soil-depth feedback의 architecture benchmark라면, 이 논문은 modern biomass-pool-to-erosion equation benchmark로 사용한다.
