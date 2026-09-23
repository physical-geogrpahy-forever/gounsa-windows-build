# 서지정보
Calle, L., & Poulter, B. (2021). Ecosystem age-class dynamics and distribution in the LPJ-wsl v2.0 global ecosystem model. Geoscientific Model Development, 14, 2575–2601. https://doi.org/10.5194/gmd-14-2575-2021

# 이 논문을 찾은 이유
LPJ-GUESS SEC/PF 계열과 별개의 LPJ age-class 구현이 고운사 strict spatial cohort 요구를 더 단순하게 만족할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 개발
- global DGVM with age-class module

# 공간 구조
- global grid cell 내부에 dynamic ecosystem age classes
- age-class area fractions를 추적
- actual fine x-y cohort geography가 아님

# 적용 환경
- global terrestrial ecosystems
- fire, land abandonment, wood harvest가 age distribution을 변화시킴

# 핵심 과정
- ecosystem age-class dynamics
- NPP, respiration, vegetation carbon
- disturbance-driven age transitions
- LPJ-wsl ecosystem processes

# 식생 입력
- PFT/ecosystem state
- age-class distribution
- climate and disturbance drivers

# 핵심 식
본 검토의 핵심은 age-class demographic bookkeeping이다. 논문은 grid cell 내 age-class distribution을 동적으로 추적하여 ecosystem stocks and fluxes에 연결한다.

# 파라미터와 단위
- global grid application
- code archived at Zenodo DOI 10.5281/zenodo.4409331
- 정확한 daily process 및 soil-layer parameter는 production 검토 시 원문 재확인 필요

# 원 논문의 구현 범위
- fire, land abandonment, harvest에 의해 변화하는 ecosystem age distribution
- age-dependent ecosystem stocks/fluxes
- computationally efficient global demography

# 고운사에 직접 사용할 수 있는 부분
- disturbance 이후 age-class redistribution의 계산 효율 참고
- demographic bookkeeping benchmark

# 새로운 coupling이 필요한 부분
- actual fine terrain cell 및 intercell demographic processes
- explicit postfire herb/shrub/tree understory succession
- hillslope lateral hydrology
- geomorphic soil-state overwrite 및 soil-layer remapping

# 한계
- age classes는 fine spatial cohort가 아니라 grid-cell subarea classes에 가깝다.
- 고운사에서 필요한 actual hillslope/catchment coupling precedent가 약하다.
- LPJ-GUESS SEC + PF-LPJG lineage보다 criterion 1, 2, 4가 불리하다.

# 최종 판정
- 탈락
- global age-class DGVM comparator로만 유지

# 참고 링크 / DOI
- https://doi.org/10.5194/gmd-14-2575-2021
- code: https://doi.org/10.5281/zenodo.4409331
