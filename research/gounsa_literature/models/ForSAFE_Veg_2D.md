# ForSAFE-Veg + ForSAFE-2D

업데이트: 2026-09-23

# 왜 검토했는가
고운사 strict vegetation criteria에서 특히 드문 조합인 다음 기능을 가진 새 모델 계열인지 확인했다.

- explicit understory vegetation
- daily soil-water response
- actual forest hillslope lateral hydrology
- forest ecosystem biogeochemistry

# 계보
```
ForSAFE
  + Veg
  -> ForSAFE-Veg

ForSAFE
  + lateral saturated/unsaturated water and chemistry transport
  -> ForSAFE-2D
```

ForSAFE-Veg와 ForSAFE-2D가 동일 논문에서 하나의 완전 통합된 cohort-hillslope vegetation model로 검증된 것은 아니다. 같은 ForSAFE family의 서로 다른 확장이다.

# 식생 구조
## Tree component
- PnET 계열 tree photosynthesis/growth/phenology/transpiration/uptake
- stand-level forest process representation
- litter decomposition 및 nutrient cycling과 연결

## Ground vegetation: Veg
- herbaceous layer 최대 약 1.8 m
- species-specific community composition
- soil moisture, soil solution N, pH, light, temperature response
- rooting depth와 shading height를 통한 경쟁
- species relative cover가 동적으로 변화

중요:
Veg는 단순 static ground cover가 아니지만, age/size cohort demographic engine도 아니다.

# 수문 및 공간 구조
ForSAFE-2D:
- actual forest hillslope application
- lateral soil-water and chemical transport
- saturated/unsaturated zones
- forest-to-stream discharge
- daily simulation
- Northern Sweden hillslope validation

# 고운사 5개 기준 판정
| 기준 | 판정 | 이유 |
|---|---|---|
| 1 spatial cohort | **FAIL** | tree는 stand-process, Veg는 species cover/community. age/size cohort geography가 아님 |
| 2 explicit understory succession | **STRONG-PARTIAL** | species-level herbaceous community와 competition은 매우 명시적이나 seed/recruit cohort 기반 천이와는 다름 |
| 3 soil-topography coupling | **STRONG** | soil water, soil chemistry가 식생 과정과 직접 연결되고 ForSAFE-2D가 lateral soil water를 계산 |
| 4 hillslope/catchment precedent | **YES** | Northern Sweden actual forest hillslope |
| 5 <= daily | **YES** | ForSAFE-2D hydrology/transport daily |

# 고운사에서의 가치
ForSAFE family는 현재까지 찾은 모델 중 다음 조합의 가장 좋은 보조 비교 사례 중 하나다.

```
explicit understory species response
+ soil moisture/light/root-depth competition
+ daily forest hillslope hydrology
```

따라서 MEDFATE의 herb recruitment extension이나 LPJ/FATES의 understory parameterization을 설계할 때 ecological benchmark로 쓸 가치가 있다.

# 생산 엔진으로 채택하지 않는 이유
고운사에서 요구하는 핵심은 geomorphic cell에 대응하는 cohort/size/age structured vegetation이다.

ForSAFE-Veg의 ground vegetation state는 상대 피복과 environmental niche response 중심이고, ForSAFE tree growth도 strict demographic cohort 구조가 아니다.

따라서 criterion 1 때문에 production vegetation engine으로는 현재 탈락이다.

# 새로운 coupling
ForSAFE family를 실제 고운사 production model에 쓴다면 다음은 새로운 coupling이다.
- age/size cohort demography
- fire 이후 seedbank/recruit dynamics
- shrub/tree/herb cohort succession
- event-driven soil geometry remap
- geomorphic DEM/soil-depth feedback

# 관련 논문
- `papers/2019_Belyazid_ForSAFEVeg.md`
- `papers/2021_Zanchi_ForSAFE2D.md`

# 최종 판정
**보조근거 / process comparator**

기존 top shortlist인 LPJ-GUESS SEC + external hydrology, FATES, MEDFATE를 대체하지 않는다.
