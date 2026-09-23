# 서지정보
Rumohr, Q., Grimm, V., Lennartz, G., Schäffer, A., Toschki, A., Roß-Nickoll, M., & Hudjetz, S. (2023). LandS: Vegetation modeling based on Ellenberg's ecological indicator values. MethodsX, 11, 102486. https://doi.org/10.1016/j.mex.2023.102486

# 이 논문을 찾은 이유
WoodS의 후속 계열이 현재도 유지되는지, 그리고 고운사에서 필요한 환경상태 입력과 하루 단위 spatial vegetation dynamics를 더 유연하게 제공하는지 확인하기 위해 검토했다.

# 연구 유형
- model/method update
- GraS 및 WoodS 계열의 후속 Landscape Succession Model
- spatial raster vegetation succession

# 공간 구조
- cell-based raster landscape
- cell-specific vegetation composition and environmental indicator maps
- herbaceous vegetation is mandatory
- woody vegetation module is optional and inherited from WoodS

# 적용 환경
- semi-natural landscapes
- Central European grassland and forest environments
- management-change and post-disturbance landscape applications를 목표로 함

# 핵심 과정
- species-specific herbaceous cover growth
- competition and self-regulation
- spread to adjacent cells
- land-use effects
- environmental filtering based on Ellenberg-like Ecological Indicator Values
- optional WoodS woody encroachment

# 환경 입력
LandS는 species/site EIV를 이용해 다음 환경축을 표현한다.
- light
- moisture
- temperature
- soil reaction/pH
- nitrogen
- cutting
- grazing
- trampling

site EIV map은 observation, soil map, DTM 및 expert knowledge로 구성할 수 있다.

# 시간 구조
- simulation period는 years로 설정
- 한 해 내부 timestep은 one-day 또는 one-week 선택 가능
- 많은 growth/spread process가 각 timestep에 실행됨
- 다만 현재 vegetation development는 실제 계절적 dieback이나 detailed plant physiology를 계산하는 구조가 아님

# 토양 및 수문 관련 판정
LandS의 `moisture`는 Ellenberg-style site indicator이며 mechanistic soil water state가 아니다.

따라서 다음과 동일시할 수 없다.
- volumetric soil water content
- matric potential
- root-zone water uptake
- water table depth
- layer-specific lateral flow

외부 geomorphic/hydrologic model의 일별 soil-water state를 직접 overwrite하는 published interface는 확인되지 않았다.

# 소프트웨어 가용성
논문은 GitHub에서 executable, user guide, initialization files를 제공한다.
하지만 Data availability에는 source code를 공유할 permission이 없다고 명시되어 있다.

이는 고운사처럼 state-exchange coupler를 직접 삽입하려는 경우 중요한 제약이다.

# 고운사에 사용할 수 있는 부분
- WoodS 계열이 사라진 일회성 모델이 아니라 2023년까지 후속 개발되었다는 근거
- herbaceous species-level landscape succession의 간단하고 계산효율적인 구조
- soil map과 DTM으로 spatial environmental suitability를 초기화하는 방법론
- 1-day landscape iteration 가능성

# 필요한 새로운 coupling
- EIV moisture를 mechanistic soil-water stress/state로 대체 또는 보완
- external soil geometry and water state input
- root depth/distribution and water uptake
- woody module과 최신 LandS herb module의 고운사 조건 검증
- source code 접근 또는 재구현

# 한계
- current publication의 주된 model extension과 tests는 herbaceous vegetation 중심
- woody vegetation은 optional이며 current test setup에서 사용되지 않음
- moisture representation은 ecological indicator, not hydrology
- source code not shared publicly according to paper
- forest canopy physiology, roots, C/N cycling이 현재 top candidates보다 단순함

# 다섯 기준 판정
1. spatial cohort/hybrid: **PARTIAL**. raster vegetation strong, herb cover state, optional woody individual lineage.
2. explicit understory succession: **STRONG for herbs; PARTIAL overall** because current woody integration is inherited rather than newly tested.
3. external soil/terrain state coupling: **FAIL/PARTIAL**. static site EIV input is possible but mechanistic state exchange is absent and source access is restricted.
4. terrain/catchment precedent: **PARTIAL**. DTM/site maps are accepted, but no routed catchment hydrology.
5. <= daily: **YES for scheduling**, but not equivalent to daily process ecophysiology.

# 최종 판정
- WoodS/LandS biological-spatial benchmark lineage로 유지
- production shortlist에는 승격하지 않음
- 특히 기준 3의 외부 soil-state coupling과 source availability 때문에 MEDFATE, LPJ-GUESS, FATES보다 불리함

# 참고 링크 / DOI
- https://doi.org/10.1016/j.mex.2023.102486
- executable lineage: https://github.com/gaiac-eco/LandS
