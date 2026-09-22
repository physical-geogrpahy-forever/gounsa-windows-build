# TROLL 4.0 model lineage

## 핵심 구조
TROLL 4.0은 fine-scale individual-based forest dynamics model이다.

- individual trees
- 1 m3 aboveground voxels
- configurable belowground voxels
- spatially explicit 1 m seedling bank
- soil water balance
- fine-root biomass by depth
- root water uptake
- daily fine-scale light/water calculations

## LiDAR 적합성
모델 논문은 3D remote-sensing structure와 직접 비교할 수 있음을 명시한다.
따라서 LiDAR CHM/forest structure를 초기화와 검증에 활용하는 후보로 매우 강하다.

## Root representation
- total fine-root biomass = leaf biomass assumption
- rooting depth is DBH function
- exponential vertical distribution
- root length density used in water uptake
- root horizontal spread across belowground voxels is not represented

## 고운사 장점
1. vegetation spatial scale가 LiDAR와 매우 잘 맞는다.
2. fine-root mass와 vertical profile이 explicit state/equation으로 존재한다.
3. seed bank도 1 m spatially explicit이다.
4. belowground water availability가 tree functioning에 feedback한다.

## 결정적 한계
1. tropical forest 중심
2. current stand topography flat
3. current publication에서 litter decomposition and wood decay는 future development
4. fire disturbance가 mature production module이 아님
5. temperate/boreal transfer itself is future direction

## 판정
LiDAR + root spatial architecture의 benchmark로 유지.
현재 고운사 production vegetation model로는 미완성 과정이 너무 많아 보류.
