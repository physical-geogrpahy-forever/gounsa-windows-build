# New vegetation candidate screen without cycling

Date: 2026-09-23

# 목적
기존 FATES, LPJ-GUESS, MEDFATE, FORMIND, ED2, HETEROFOR, SEIB-DGVM, LandscapeDNDC, JULES-RED 등 이미 검토된 모델을 반복 검색하지 않고, repository에 없던 새 계열만 조사한다.

# 이번에 실제로 새로 검토한 계열
1. ForSAFE-Veg + ForSAFE-2D
2. JSBACH4 forest-age tiles
3. LPJ-wsl v2.0 age classes

CARAIB와 ORCHIDEE-MICT도 1차 검색에서 확인했으나 이번 결정 파일에서는 아직 canonical paper/model note를 완성하지 않았으므로 확정 판정표에서 제외한다.

# strict five-criteria result
| lineage | 1 spatial cohort | 2 understory | 3 soil-state coupling | 4 terrain/catchment | 5 <= daily | 판정 |
|---|---|---|---|---|---|---|
| ForSAFE-Veg + ForSAFE-2D | **FAIL** | **STRONG-PARTIAL** | STRONG | **YES actual forest hillslope** | **YES daily** | process comparator |
| JSBACH4 forest-age | WEAK-PARTIAL | WEAK-PARTIAL | PARTIAL | FAIL for fine target | fast land physics | reject |
| LPJ-wsl v2.0 | PARTIAL | WEAK-PARTIAL | PARTIAL | WEAK | daily ecosystem processes available | reject |

# 가장 중요한 새 결론
이번 batch가 중요한 이유는 "왜 완성형 후보가 잘 안 나오는가"를 더 명확하게 보여주기 때문이다.

ForSAFE family:
```
explicit ground vegetation
+ soil moisture/light/rooting-depth competition
+ actual forest hillslope
+ daily lateral hydrology
```
까지는 만족하지만 demographic cohort가 없다.

반대로 JSBACH4와 LPJ-wsl:
```
age-class demography
+ fast land-surface/ecosystem processes
```
는 있지만 actual fine terrain cohort와 explicit forest-floor succession이 약하다.

즉 기존 shortlist가 우연히 좁아진 것이 아니라, 현재 문헌에서 기능들이 서로 다른 model families에 분산되어 있다는 기존 결론이 추가로 강화되었다.

# shortlist 영향
이번 새 후보는 기존 top tier를 바꾸지 않는다.

고운사 strict criteria의 현재 핵심 후보:
- **LPJ-GUESS SEC/PPA + PF-style external hydrology**
- **FATES + ELM/ParFlow host**
- **MEDFATE + medfateland**

FORMIND-mHM은 동일 forest patch에서 demographic herb layer가 확인될 경우에만 재승격한다.

# 재검색 금지
다음 조건이 없는 한 이번 세 계열을 다시 broad-search하지 않는다.

## ForSAFE
- age/size cohort extension
- tree/shrub/herb demographic recruitment extension
- 또는 ForSAFE-2D와 cohort vegetation의 published direct integration

## JSBACH4
- actual fine-resolution terrain/catchment cohort implementation
- explicit understory herb/shrub demography

## LPJ-wsl
- fine catchment/hillslope application with explicit demographic understory
- PF-LPJG보다 직접적인 soil-terrain state exchange

# 다음 조사 방향
새 DGVM 이름을 계속 수집하는 것은 우선순위를 낮춘다.

남은 탐색은 다음 조합만 대상으로 한다.

```
actual terrain cells
+ cohort/size/age structured vegetation
+ endogenous herb/shrub/tree succession
+ daily/subdaily soil-water response
+ published hillslope/catchment application
```

특히 "ground-vegetation cohort forest model + lateral hillslope hydrology" 조합을 우선한다.

# 관련 파일
- `models/ForSAFE_Veg_2D.md`
- `models/JSBACH4_ForestAge.md`
- `models/LPJ_wsl_2_0.md`
- `papers/2019_Belyazid_ForSAFEVeg.md`
- `papers/2021_Zanchi_ForSAFE2D.md`
- `papers/2020_Nabel_JSBACH4_ForestAge.md`
- `papers/2021_Calle_LPJwsl_AgeClasses.md`
