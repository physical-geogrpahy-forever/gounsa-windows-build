# BioRT watershed reactive-transport lineage

## 목적
고운사 chemical weathering에서 WITCH/PROFILE 계열 외에:
- 공간 수문
- soil respiration
- plant nutrient uptake
- mineral dissolution
을 watershed scale에서 결합하는 대안을 정리한다.

## 핵심 논문
- Zhi et al. 2022: BioRT-Flux-PIHM v1.0
- Sadayappan et al. 2024: BioRT-HBV 1.0
- Wen et al. 2022: 2D forest-hillslope reactive transport application

## BioRT-Flux-PIHM

구조:

```
Flux
 -> energy balance / ET

PIHM
 -> precipitation
 -> interception
 -> infiltration
 -> recharge
 -> surface runoff
 -> shallow lateral flow
 -> deep flow

BioRT
 -> mineral dissolution / precipitation
 -> aqueous complexation
 -> surface complexation
 -> ion exchange
 -> plant nutrient uptake
 -> soil respiration
 -> microbial reactions
 -> solute transport
```

장점:
- watershed scale
- spatially explicit hydrology
- shallow/deep lateral and vertical flow
- mineral weathering과 plant uptake/respiration이 같은 chemistry network 안에 존재

단점:
- LPJ-GUESS 같은 forest succession 없음
- explicit root biomass/exudation은 REWTCrunch보다 약함
- geomorphic soil-production thickness를 직접 업데이트하지 않음

## BioRT-HBV

간소화된 watershed RTM.

General rate:

```
r
=
k A f(T) f(Sw) f(Zw)
```

Weathering TST form:

```
r
=
k A_mineral a^m
(1-IAP/K_eq)
```

포함:
- root respiration
- root-exudate-related DOC/DIC source
- soil respiration
- chemical weathering
- nutrient transformations

역할:
- low-data reaction-law prototype
- sensitivity benchmark

공간적으로는 implicit하므로 고운사 production spatial engine에는 부족하다.

## Wen et al. 2022 hillslope precedent

2D hillslope RTM:

```
hydrologic regime
 -> flow-path depth
 -> residence time
 -> soil carbon transformation
 -> mineral weathering
 -> lateral/vertical solute export
```

중요한 의미:
- grid cell을 독립적으로 weathering시키는 것만으로는 실제 spatial coupling이 충분하지 않을 수 있음
- topography-driven subsurface flow와 water residence time을 chemical weathering에 연결해야 함

## relation to B-WITCH

B-WITCH strength:
- dynamic vegetation model precedent
- PFT/NPP
- respiration
- nutrient uptake/return
- litter/root return

BioRT strength:
- spatial hydrology
- lateral/deep flow
- modern reactive transport structure

따라서 두 계열은 경쟁후보라기보다 서로 보완적이다.

Potential Gounsa architecture:

```
LPJ-GUESS vegetation interface
 -> BioRT-style spatial hydrology/RT chemistry
```

또는:

```
LPJ-GUESS vegetation interface
 -> WITCH/PROFILE chemistry
 + separate spatial hydrology correction
```

이 exact system은 새로운 coupling이다.

## relation to SWEHR / Landlab

BioRT를 production chemistry engine으로 사용할 경우:

```
Landlab/SWEHR topography + soil depth
 -> subsurface hydrologic state
 -> BioRT chemistry

LPJ-GUESS
 -> ET / roots / respiration / uptake
 -> BioRT chemistry

BioRT
 -> W_chem / nutrients
 -> mass balance / LPJ-GUESS-CNP
```

이때 SWEHR surface runoff와 BioRT subsurface hydrology의 water balance가 중복되지 않도록 shared water-state 설계가 필요하다.

## current judgment

### BioRT-Flux-PIHM
- **strong spatial alternative / validation engine**
- WITCH/PROFILE보다 spatial hydrology가 강함
- LPJ-GUESS vegetation interface를 별도로 이식해야 함

### BioRT-HBV
- **parsimonious reaction-law benchmark**
- production spatial engine은 아님

### Wen 2022
- **2D hillslope hydrology-weathering benchmark**

## unresolved
1. Gounsa에서 subsurface lateral flow가 W_chem spatial pattern에 얼마나 중요한가
2. WITCH vs BioRT code practicality
3. LPJ-GUESS hydrology와 BioRT hydrology의 overlap
4. SWEHR event hydrology와 long-term subsurface water balance separation
5. sandstone mineral assemblage and reactive surface area

## references
- Zhi et al. 2022. DOI 10.5194/gmd-15-315-2022
- Wen et al. 2022. DOI 10.1029/2022WR032314
- Sadayappan et al. 2024. DOI 10.1029/2024MS004217
