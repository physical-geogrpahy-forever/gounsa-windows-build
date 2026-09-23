# 서지정보
Tang, J., Pilesjö, P., Miller, P. A., Persson, A., Yang, Z., Hanna, E., & Callaghan, T. V. (2014). Incorporating topographic indices into dynamic ecosystem modelling using LPJ-GUESS. Ecohydrology, 7, 1147–1162. DOI: 10.1002/eco.1446

# 이 논문을 찾은 이유
고운사 식생모델 후보가 다음 조건을 동시에 만족하는지 확인하기 위해 검토했다.
1. 공간명시적 cohort 구조
2. 하층식생과 천이
3. 토심 또는 WHC/토양수분 저장
4. 유역/지형 적용
5. 일 이하 시간해상도

# 연구 유형
- 수치모델 개발 및 유역 적용

# 공간 구조
- LPJ-GUESS 생태계 동태를 실제 50 m 격자로 배치
- Stordalen catchment 적용
- DEM 기반 topographic index와 drainage-network 효과 반영
- 표준 LPJ-GUESS의 독립 grid-cell 한계를 보완하려는 distributed hydrology 확장

# 적용 환경
- 북스웨덴 Stordalen catchment
- 복잡한 지형과 습윤/한랭 환경

# 핵심 과정
- woody cohort establishment, growth, mortality
- herbaceous understory
- light, water, soil-resource competition
- daily carbon assimilation and soil-water update inherited from LPJ-GUESS
- DEM/topographic-index driven spatial water redistribution
- catchment runoff evaluated at six outlets

# 식생 입력/상태
- age/PFT cohorts
- herbaceous understory PFTs
- LAI
- root distribution by soil layer
- biomass and carbon pools

# 토양/수문
- LPJ-GUESS soil-water bucket/WHC framework inherited
- topographic index modifies spatial water availability and catchment runoff response
- explicit 50 m distributed catchment application

# 시간해상도
- vegetation physiology and soil-water balance: daily LPJ-GUESS loop
- reported runoff evaluation includes monthly summaries, but the ecological/hydrological process engine is daily

# 고운사에 직접 사용할 수 있는 부분
- 50 m actual geographic cells containing LPJ-GUESS cohorts
- herbaceous understory and woody succession within each cell
- DEM-derived topographic control on water availability
- catchment application provides direct precedent for terrain-explicit vegetation demography

# 새로운 coupling이 필요한 부분
- current Gounsa target requires 1–25 m vegetation grid and 1–5 m geomorph grid
- storm-driven soil-depth change and root exposure/burial are not native
- explicit hourly erosion feedback would require external geomorph loop
- intercell seed dispersal is not part of standard LPJ-DH

# 한계
- hydrological redistribution is simpler than 3D Richards/ParFlow approaches
- 50 m validation does not prove 10–25 m scale validity
- shrubs are less explicit than in FATES/MEDFATE

# 최종 판정
- 채택 후보
- 현재 5개 고정 조건을 가장 균형 있게 만족하는 published precedent 중 하나
- PF-LPJG 2026과 함께 LPJ-GUESS spatial ecohydrology lineage의 핵심 근거

# 참고 링크 / DOI
- https://doi.org/10.1002/eco.1446
