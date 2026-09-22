# 서지정보
de Wergifosse, L., André, F., Beudez, N., de Coligny, F., Goosse, H., Jonard, F., Ponette, Q., Titeux, H., Vincke, C., & Jonard, M. (2020). HETEROFOR 1.0: a spatially explicit model for exploring the response of structurally complex forests to uncertain future conditions – Part 2: Phenology and water cycle. Geoscientific Model Development, 13, 1459-1498. DOI: 10.5194/gmd-13-1459-2020

# 이 논문을 찾은 이유
고운사 지형모델은 강우와 토양수분 변화가 빠르므로, 식생모델이 시간별 수문과 개별목 root uptake를 처리할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- process-based forest ecohydrology

# 공간 구조
두 수문 옵션:
1. stand-scale soil water
2. individual-tree pedon별 soil water

개별목 pedon 방식에서는 전체 토양체를 나무별 토양체로 나누고 각각 독립 수분수지를 계산한다.

# 적용 환경
- 온대 혼효림
- 복잡한 구조의 산림

# 핵심 과정
- phenology
- throughfall
- stemflow
- foliage/bark interception
- soil evaporation
- ground vegetation transpiration
- individual tree transpiration
- root water uptake
- capillary rise/drainage
- Darcy soil-water transfer

# 식생 입력
- individual tree leaf area
- crown structure
- fine-root vertical proportion by horizon
- ground vegetation LAI
- hourly meteorology

# 핵심 식
토양층별 root uptake는 전체 uptake를 fine-root proportion과 토양수분 potential에 따라 분배한다.

개략:
```
UP_root(hr)
= UP_root * f_hr
+ compensatory_uptake(phi_hr, weighted_phi, f_hr, area)
```

# 파라미터와 단위
- meteorology: hourly
- soil water balance: hourly
- soil horizon depth: m
- fine-root proportion by horizon: fraction
- water uptake: L h-1
- soil water potential: cm water head

# 원 논문의 구현 범위
산림 수관에서 토양까지 시간별 물수지를 모의하고 개체목 수준 transpiration과 선택적 pedon water balance를 제공한다.

# 고운사에 직접 사용할 수 있는 부분
- 지형모델의 event/hourly water state와 시간축 호환성이 LANDIS-II보다 좋음
- 나무별 토양수분 스트레스
- fine-root vertical distribution을 이용한 water uptake
- ground vegetation의 수문영향

# 새로운 coupling이 필요한 부분
- geomorphic 2D lateral flow와 pedon water balance 사이의 교환
- LiDAR DEM의 cell-specific soil depth
- erosion/deposition 뒤 soil horizon geometry remapping

# 한계
pedon 사이 수평적 물 재분배는 계산하지 않는다. 따라서 HETEROFOR hydrology가 Iber/지형 수문엔진을 대체할 수 없다. 고운사에서는 외부 2D 수문상태를 경계/상태값으로 교환하는 것이 더 적절하다.

# 최종 판정
- 채택 후보
- 시간해상도와 root-water coupling 측면에서 매우 강함

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-13-1459-2020
