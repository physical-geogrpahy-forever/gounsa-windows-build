# PREBAS

업데이트: 2026-09-23

# 왜 검토했는가
새로운 중간복잡도 후보로서 다음 조합을 만족하는지 확인했다.

- tree cohort/stratum structure
- daily GPP/ET/soil water
- ground vegetation
- spatial raster application

# 모델 구성
```
PRELES
  daily GPP + ET + soil water
      |
      v
CROBAS
  tree carbon allocation + stand growth
      |
      +--> litter
      v
YASSO
  soil carbon
```

최근 Rprebasso/PREBAS 구현은 stand structural variables를 cohort/stratum 수준에서 줄 수 있고 uneven-aged size-class application도 가능하다.

# 시간해상도
- photosynthesis: daily
- evapotranspiration: daily
- soil water: daily
- tree carbon allocation/structural growth: annual
- litter to YASSO: annual-scale interface가 기본

# ground vegetation
2023 national applications에는 ground vegetation module이 추가되어 있다.

그러나 이 모듈은 ground vegetation inventory를 이용한 empirical module이며, site type 및 below-canopy light 등에 따라 ground vegetation biomass/C를 추정한다.

중요:
```
ground vegetation biomass model
!=
herb/shrub demographic recruitment-succession engine
```

# 공간 구조
- stand model을 raster/grid unit별로 반복 실행 가능
- Finland wall-to-wall applications 존재
- 96 x 96 m 등 spatial unit 사용 사례 존재
- 그러나 lateral water transfer나 actual hillslope routing이 PREBAS core가 아님

# 고운사 5개 기준 판정
| 기준 | 판정 | 이유 |
|---|---|---|
| 1 spatial cohort | PARTIAL | tree strata/size classes 가능, raster unit 적용 가능. 그러나 native fine spatial cohort ecology는 제한적 |
| 2 explicit understory succession | **FAIL** | ground vegetation은 empirical biomass module, endogenous herb/shrub cohort recruitment가 아님 |
| 3 soil-topography coupling | MODERATE | soil depth, FC, wilting point, daily soil water를 사용하지만 external dynamic terrain coupling precedent는 약함 |
| 4 hillslope/catchment | **FAIL/WEAK** | national/regional grid는 있으나 lateral hillslope hydrology가 없음 |
| 5 <= daily | PARTIAL-STRONG | GPP/ET/soil water daily, structural growth annual |

# 장점
- 계산이 비교적 단순
- daily water/carbon
- stand strata representation
- open R implementation
- soil depth/field capacity/wilting point input
- regional raster scalability

# 고운사에 부적합한 핵심 이유
산불 직후 핵심인 herb -> shrub -> tree succession을 endogenous demographic process로 계산하지 않는다.
또한 storm-driven terrain change가 neighboring cells의 soil-water redistribution으로 이어지는 hillslope architecture가 없다.

# 관련 논문
- `papers/2023_Makela_PREBAS_ForestManagement.md`

# 최종 판정
**strict shortlist 탈락**

새로운 explicit-understory demographic extension 또는 actual hillslope coupling이 확인될 때만 재검토한다.
