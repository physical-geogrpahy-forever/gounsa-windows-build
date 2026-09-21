# 결정: vegetation-weathering 문헌은 모델 연구를 우선한다

날짜: 2026-09-21

## 조사 기준 수정
현재 목표는 현장관측 메커니즘을 더 모으는 것이 아니라 고운사 production architecture에 직접 참고할 수 있는 published numerical model을 찾는 것이다.

앞으로 candidate model은 최소한 다음을 만족해야 한다.
1. numerical/computational model일 것
2. vegetation 또는 root state가 명시적인 state/input/process로 들어갈 것
3. hydrology, chemistry, weathering, soil-profile evolution, geomorphology 중 하나 이상을 동적으로 계산할 것
4. coupling이 코드/수식/algorithm으로 실제 구현되어 있을 것

현장연구는 mechanism support와 validation에만 사용한다.

## 이번 model-only mini-pass

### 1. ForSAFE
dynamic forest growth + hydrology + decomposition + soil chemistry + mineral weathering.

tree growth -> water/nutrient demand -> uptake
weathering/decomposition/deposition -> nutrient availability -> tree growth
tree growth -> litter return -> soil chemistry

판정: 핵심 채택.
현재 vegetation-weathering feedback의 가장 직접적인 forest-model precedent.

### 2. LORICA
DEM + multiple soil layers + erosion/deposition + creep + chemical weathering + soil-profile evolution.

soil development -> geomorphic susceptibility
erosion/deposition -> mineral/profile redistribution -> weathering

판정: 강한 보조 채택.
현재 soil-landscape-weathering spatial coevolution의 가장 직접적인 precedent.
단 vegetation은 단순 보호항으로, dynamic forest model이 아님.

### 3. SoilGen
1D vertical pedogenesis + Richards flow + heat + gas + solute + physical/chemical weathering.

판정: vertical-profile reference로 채택.
catena 연구에서도 pedon 사이 lateral water flux가 없으므로 full hillslope engine으로는 부족.

### 4. MIN3P-ArchiSimple
2D dynamic root architecture + spatial root surface density + multicomponent reactive transport + mineral dissolution.

판정: root-chemistry interface의 mechanistic reference로 채택.
산림사면/지형진화 모델은 아님.

## 현재 가장 타당한 역할 분담

LPJ-GUESS
 -> dynamic forest state

ForSAFE lineage
 -> vegetation <-> water/nutrients <-> mineral weathering interface

MIN3P-ArchiSimple
 -> root spatial state -> chemistry interface constraints

SoilGen
 -> vertical soil-profile / pedogenesis structure

LORICA
 -> erosion/deposition + soil profile + chemical weathering spatial coevolution

Flux-PIHM/WITCH, BioRT, PFLOTRAN/Crunch lineage
 -> connected hillslope hydrology/reactive transport

SWEHR/Landlab
 -> postfire erosion and geomorphic evolution

## 가장 중요한 결론
현재까지 확인한 published model 중 다음을 모두 동시에 구현하는 하나의 모델은 없다.

dynamic forest vegetation
+ connected hillslope hydrology
+ reactive chemical weathering
+ soil production/profile evolution
+ erosion/deposition
+ postfire disturbance

따라서 고운사 최종모델은 modular coupling이어야 한다.

그러나 이제 각 coupling 부위에는 실제 numerical-model precedent가 있다.

## 금지
- field observation을 candidate numerical model로 취급하지 않음
- vegetation cover 또는 biomass 하나를 universal weathering multiplier로 사용하지 않음
- SoilGen을 2D hillslope model이라고 부르지 않음
- LORICA vegetation component를 dynamic forest succession model이라고 부르지 않음
- MIN3P rhizosphere application을 sandstone hillslope model이라고 부르지 않음

## 다음 모델 조사 우선순위
1. ForSAFE의 spatial/hillslope 확장 또는 lateral flow 결합 연구
2. dynamic forest vegetation + hillslope hydrology + reactive weathering model
3. dynamic vegetation을 soil production/weathering-front evolution에 직접 넣은 numerical model
4. LORICA/HydroLorica 계열에서 chemical weathering과 dynamic vegetation이 동시에 구현된 후속 버전