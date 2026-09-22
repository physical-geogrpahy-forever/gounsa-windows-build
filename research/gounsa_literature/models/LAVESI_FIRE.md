# LAVESI-FIRE model lineage

## 구조
LAVESI는 spatially explicit individual-based forest model이다.
- individual tree x,y positions
- individual seeds
- wind-driven seed dispersal
- yearly establishment/growth/competition/mortality
- environment grid approximately 0.2 m x 0.2 m in recent applications

LAVESI-FIRE:
- climate-driven wildfire occurrence
- local fire intensity
- tree mortality
- seed mortality
- litter-layer reduction
- postfire regeneration

LAVESI-CryoGrid:
- forest state -> soil thermo-hydrology
- soil environment -> vegetation
의 양방향 model coupling 선례를 제공한다.

## 고운사 장점
- genuine fine spatial tree and seed positions
- topography/slope/TWI input precedent
- spatial postfire regeneration
- litter layer as an explicit spatial state
- open source LAVESI-FIRE code

## 고운사 한계
- boreal/permafrost and a limited tree-species set에 강하게 특화
- yearly vegetation update
- quantitative fine-root biomass, dead-root mass, coarse-root architecture가 geomorphic output state로 구현되어 있지 않음
- litter layer는 height 중심이며 고운사 erosion interface에 필요한 mass/contact/cover 변환이 추가로 필요

## 판정
공간적 산불-천이 비교모델 및 coupling architecture의 강한 보조근거.
주 식생모델로는 root-state 부재 때문에 보류.

## 관련 논문
- papers/2022_Kruse_LAVESI_CryoGrid.md
- papers/2024_Gluckler_LAVESI_FIRE.md
