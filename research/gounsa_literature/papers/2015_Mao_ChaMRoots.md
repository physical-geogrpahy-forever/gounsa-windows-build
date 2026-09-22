# 서지정보
Mao, Z., Saint-André, L., Bourrier, F., Stokes, A., & Cordonnier, T. (2015). Modelling and predicting the spatial distribution of tree root density in heterogeneous forest ecosystems. Annals of Botany, 116(2), 261-277. DOI: 10.1093/aob/mcv092

# 이 논문을 찾은 이유
LiDAR와 HETEROFOR의 개체목 위치, DBH를 고운사 1-5 m 지형격자의 실제 3차원 뿌리분포로 변환할 published root-distribution model을 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- semi-mechanistic 3D root-distribution model
- 산악림 현장자료 보정 및 검증

# 공간 구조
- tree cluster scale
- 주변 여러 나무의 영향을 중첩
- 수평거리와 토심을 동시에 고려
- root interception density(RID)를 공간적으로 예측

# 적용 환경
- French Alps
- uneven-aged mountain forests
- Abies alba
- Picea abies
- 서로 다른 종조성과 밀도를 가진 두 산악림

# 핵심 과정
ChaMRoots는 세 하위모델로 구성된다.

1. 공간적 이질성
- 표토 0-0.2 m의 가장 가는 뿌리 RID
- tree species
- breast-height basal area
- tree-to-point distance
- surface-emerging stone obstacle

2. root diameter spectrum
- 1 mm 이상 뿌리를 최대 50 mm까지 직경급으로 분배

3. vertical profile
- soil depth에 따른 RID 분배

# 식생 입력
- individual tree position
- species
- basal area at breast height
- distance from tree to raster/evaluation point
- soil/stone obstacle information

# 핵심 출력
- RID: number of roots m-2
- diameter-class root density
- depth-dependent root density

# 고운사에 직접 사용할 수 있는 부분
HETEROFOR 또는 LiDAR inventory와의 인터페이스가 매우 직접적이다.

```
LiDAR/HETEROFOR
  tree x,y
  DBH / basal area
  species
      |
      v
ChaMRoots
      |
      +--> fine-root RID raster
      +--> coarse-root diameter spectrum
      +--> vertical root profile
```

이 결과는 과정별로 다르게 사용할 수 있다.

- 유수침식: RLD/RSAD 계열로 변환 또는 별도 forest-root erosion relation과 연결
- root-driven soil disturbance: 공간적 root abundance 입력
- shallow landslide: Schwarz spatial root reinforcement/RBM의 root distribution 입력
- soil weathering: depth-dependent root presence

# 새로운 coupling이 필요한 부분
- HETEROFOR fine-root biomass와 ChaMRoots RID 사이의 질량 일관성 제약
- 한국 수종의 species coefficient
- fire mortality 후 live RID -> dead-root RID 시간변화
- 뿌리 성장/고사에 따른 annual spatial update
- 암편이 많은 고운사 토양에서 obstacle term 재보정

# 한계
- French Alpine conifer-dominated forests에서 보정됨
- 한국 참나무류, 소나무류에 그대로 parameter transfer하면 안 됨
- root biomass 자체가 아니라 RID를 예측
- fire-induced root mortality/decay를 자체 계산하지 않음

# 최종 판정
- 채택 후보
- HETEROFOR/LiDAR -> spatial root distribution helper로 현재 가장 강한 published interface 중 하나
- root reinforcement 자체는 Schwarz RBM 계열로 별도 계산

# 참고 링크 / DOI
https://doi.org/10.1093/aob/mcv092
