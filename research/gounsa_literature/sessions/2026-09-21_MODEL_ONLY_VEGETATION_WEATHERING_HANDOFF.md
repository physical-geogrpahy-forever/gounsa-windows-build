# Gounsa model-only vegetation-weathering handoff

날짜: 2026-09-21
브랜치: gounsa-water-erosion-deep-review-2026-09-21

## 사용자 수정사항
현재 목표는 field observation 추가가 아니라 실제 numerical model 연구의 탐색과 선택이다.
앞으로 3-4편씩 model papers만 우선 검토한다.

## 이번 소묶음에서 새로 저장한 model papers
- papers/2018_Yu_ForSAFE_PhosphorusWeathering.md
- papers/2022_GarciaGamero_SoilGen_CatenaWeathering.md
- papers/2017_Gerard_MIN3P_ArchiSimple_RootReactiveTransport.md
- papers/2016_Temme_Vanwalleghem_LORICA_SoilLandscapeEvolution.md

## 새 model files
- models/ForSAFE.md
- models/SoilGen.md
- models/MIN3P_Root_ReactiveTransport.md
- models/LORICA.md

## decision
- decisions/2026-09-21_MODEL_ONLY_VEGETATION_WEATHERING_SCREEN.md

## main synthesis update
- models/Hillslope_Vegetation_Weathering.md에 model-only screen 추가

## 핵심 판정

### ForSAFE
dynamic forest vegetation <-> hydrology/nutrients <-> mineral weathering의 가장 직접적인 published model precedent.

### LORICA
raster DEM + multi-layer soil + erosion/deposition + chemical weathering을 결합한 soil-landscape coevolution model.
단 vegetation은 단순 protection feedback.

### SoilGen
vertical water/heat/gas/solute + pedogenesis + chemical weathering.
단 independent 1D pedons이며 lateral flow 없음.

### MIN3P-ArchiSimple
dynamic root architecture -> control-volume root surface density -> reactive transport/mineral dissolution.
root-chemistry interface의 mechanistic precedent.

## 현재 구조
LPJ-GUESS -> dynamic forest state
ForSAFE -> vegetation-weathering ecosystem interface
MIN3P -> spatial root-chemistry interface
SoilGen -> vertical pedogenesis/weathering reference
LORICA -> geomorphic redistribution-weathering spatial coupling
Flux-PIHM/WITCH, BioRT, PFLOTRAN/Crunch -> connected hydrology/reactive transport
SWEHR/Landlab -> postfire geomorphology

## 이번에 하지 않은 것
- INDEX 전체 재생성
- field-paper 추가
- arbitrary coupling coefficient 생성

## 다음 model-only 조사
1. ForSAFE spatial/hillslope extensions
2. forest vegetation + lateral hillslope hydrology + reactive weathering
3. dynamic vegetation + soil-production/weathering-front evolution
4. LORICA/HydroLorica 후속 중 chemical weathering과 vegetation dynamics를 동시에 구현한 버전

## 연결/작업 안정화
대규모 단일 batch 대신 파일별 작은 commit으로 저장했다.