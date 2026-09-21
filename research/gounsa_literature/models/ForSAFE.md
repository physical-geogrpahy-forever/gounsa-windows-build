# ForSAFE

## 모델 목적
장기 forest ecosystem에서 vegetation, hydrology, decomposition, soil chemistry, mineral weathering feedback을 동적으로 계산한다.

## 핵심 구성
- PnET-derived forest growth
- PULSE hydrology
- DECOMP litter/SOM decomposition
- SAFE/PROFILE soil chemistry and mineral weathering

## 핵심 feedback
climate + tree state -> potential growth -> water/nutrient demand -> soil uptake
weathering + deposition + decomposition -> soil-solution nutrients -> actual tree growth
tree growth -> litter/nutrient return -> soil chemistry -> weathering environment

## Weathering
PROFILE lineage의 mineral-specific kinetic weathering을 동적으로 사용한다.
ForSAFE에서는 runoff, soil moisture, temperature, litter decomposition, tree nutrient uptake 등이 시간에 따라 변하므로 weathering도 seasonal/interannual/decadal하게 달라진다.

## 고운사 관련 장점
- 실제 dynamic forest model
- vegetation과 mineral weathering이 양방향으로 연결됨
- nutrient release -> uptake -> growth -> litter return의 mass-balance 구조 존재
- water/nutrient limitation이 tree growth에 feedback
- 단순 biomass weathering multiplier가 아님

## 고운사 관련 한계
- stand / soil-profile 중심
- 2D hillslope lateral flow 없음
- evolving topography 없음
- erosion/deposition/fresh-mineral supply 없음
- postfire geomorphic processes 없음
- vegetation engine이 LPJ-GUESS가 아님

## 고운사에서의 역할
ForSAFE 자체를 최종 통합모델로 채택하기보다 vegetation-weathering coupling architecture의 최우선 published precedent로 사용한다.

LPJ-GUESS -> ForSAFE-like water/nutrient interface -> PROFILE/WITCH or other chemistry

이 결합은 NEW COUPLING이다.

## 관련 archive papers
- papers/2018_Yu_ForSAFE_PhosphorusWeathering.md
- papers/2019_Kronnas_ForSAFE_Weathering.md

## 최종 판정
- 강한 채택
- 역할: dynamic forest vegetation-weathering feedback architecture