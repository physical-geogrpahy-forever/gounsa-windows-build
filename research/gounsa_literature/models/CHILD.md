# CHILD model lineage

## 범위
고운사 문헌검토에서 CHILD 계열의 vegetation-erosion-landscape evolution 연결을 통합 관리한다.

## 확인된 계보
- Tucker & Bras (1999): fractional vegetation cover와 erosion feedback의 초기 eco-LEM 선례
- Collins, Bras & Tucker (2004): vegetation cover state와 erosion feedback
- Istanbulluoglu & Bras (2005): vegetation-modulated landscape evolution
- Yetemen et al. (2015): energy, water, biomass, elevation continuity를 한 모델에서 결합

## 핵심 지형 골격
- sediment/elevation mass balance
- fluvial detachment/transport
- hillslope diffusion

## 식생 처리의 발전
초기 CHILD는 vegetation cover를 상태변수로 사용했다. Yetemen et al. (2015)은 live/dead biomass를 계산하고 `biomass -> LAI -> vegetation cover -> Manning roughness -> effective shear stress` 경로를 구현한다.

## 고운사에 사용할 수 있는 부분
- 지상부 vegetation structure가 hydraulic resistance를 통해 유수침식에 영향을 주는 구조
- erosion이 vegetation을 다시 제거하는 양방향 feedback
- 기본 LEM 골격과 vegetation module을 분리하여 볼 수 있는 구조

## 새로운 coupling
LPJ-GUESS의 상층 PFT biomass와 실제 지표면 understory/ground structure를 CHILD roughness 변수로 바꾸는 식은 published CHILD에 없다. 고운사 적용 시 새로운 coupling이다.

## 중요한 제한
LPJ-GUESS canopy LAI/FVC를 geomorphically effective ground cover와 동일시하지 않는다. 산림 canopy cover가 높아도 지표면 하층식생과 litter 상태는 별개다.

## 관련 논문
- ../papers/2005_Istanbulluoglu_Bras_VegetationLandscapeEvolution.md
- ../papers/2015_Yetemen_SolarRadiationLandscapeEvolution.md

## 판정
- 유수침식의 지상부 수리저항 구조: 채택
- canopy FVC를 사면확산 modifier로 직접 사용: 미채택
