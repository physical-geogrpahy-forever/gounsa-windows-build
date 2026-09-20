# 서지정보
Kim, D.-H. (2023). *Effects of Soil Particle Size on Relationship Between Mound-Puddle Type Microtopography Roughness and Soil Erosion Rate on a Hillslope Basin: Hairsine-Rose Model Analysis*. Water Resources Research, 59. DOI: 10.1029/2022WR033879.

# 이 논문을 찾은 이유
Hairsine-Rose 2D/dynamic-wave 계열이 microtopography and roughness 변화에 따라 erosion pattern을 어떻게 반응시키는지, 고운사 고해상도 DEM에 적합한지 검토했다.

# 연구 유형
- numerical Hairsine-Rose erosion analysis
- dynamic-wave hillslope modeling

# 공간 구조
- hillslope basin with mound-puddle microtopography
- spatially distributed dynamic-wave flow and erosion
- full implementation details require original paper for exact dimensional classification

# 적용 환경
- synthetic/controlled hillslope-basin microtopography
- various particle sizes

# 핵심 과정
- rainfall-runoff
- microtopographic flow concentration
- erosion/deposition
- particle-size-dependent response

# 식생 입력
없음.

# 핵심 식
The study applies a dynamic-wave + Hairsine-Rose simulator and varies mound-puddle roughness and sediment particle size.

Key finding:
erosion quantity can change substantially with microtopographic roughness even when bulk rainfall-runoff conditions are otherwise comparable.

# 파라미터와 단위
- mound/puddle geometry
- sediment particle size / settling velocity
- rainfall-runoff variables
- Hairsine-Rose erosion parameters

# 원 논문의 구현 범위
Examines interaction between small-scale topographic roughness and Hairsine-Rose sediment dynamics.

# 고운사에 직접 사용할 수 있는 부분
Supports using a 2D/microtopography-resolving engine rather than predetermined rill geometry, especially where postfire roughness changes and flow concentration are important.

# 새로운 coupling이 필요한 부분
Vegetation/root/litter effects remain absent and require new coupling.

# 한계
- no forest/postfire vegetation
- no root state
- primarily a numerical sensitivity study

# 최종 판정
- **supporting Hairsine-Rose engine evidence**
- reinforces importance of microtopography in the final Gounsa water-erosion solver

# 참고 링크 / DOI
https://doi.org/10.1029/2022WR033879
