# 서지정보
Kirwan, M. L., & Shugart, H. H. (2008). *A Biologically Based Model of Tree Throw on Hillslopes*. AGU Fall Meeting Abstract, December 2008.

# 이 논문을 찾은 이유
개체 기반 산림천이와 tree-throw sediment transport를 직접 연결한 초기 numerical precedent를 확인하기 위해 검토했다.

# 연구 유형
- conference abstract
- preliminary numerical model
- **peer-reviewed full journal article 아님**

# 공간 구조
- gap-sized forest domain, about 0.1 ha
- spatially implicit/plot-scale tree-throw sediment transport

# 적용 환경
- forest succession
- tree-fall hillslope transport

# 핵심 과정
- annual tree establishment/growth
- stochastic mortality
- tree fall
- uprooted sediment volume
- downslope displacement

# 식생 입력
The FORET forest model simulates:
- individual tree establishment
- annual growth
- mortality
- canopy competition
- species-specific growth response

Tree size controls the amount of sediment moved.

# 핵심 구조
Upon mortality, a fraction of trees fall and uproot sediment.

Sediment flux depends on:
- displaced sediment volume
- transport distance
- hillslope angle

Both volume and transport distance are related to tree diameter.

# 고운사에 직접 사용할 수 있는 부분
Strong conceptual precedent for:
```
dynamic forest cohort state
 -> tree mortality
 -> tree throw
 -> sediment flux
```

This makes LPJ-GUESS cohort outputs a natural upstream driver.

# 새로운 coupling이 필요한 부분
LPJ-GUESS -> tree-throw probability/geometry remains a new coupling.

# 한계
- conference abstract
- preliminary model
- early model results did not reproduce all field expectations
- not suitable as sole quantitative parameter source

# 최종 판정
**보조 모델계보 only.**

For quantitative implementation prefer:
- Constantine et al. 2012
- Doane et al. 2021
- Gabet & Mudd 2010
while retaining Kirwan-Shugart as the early annual forest-demography precedent.
