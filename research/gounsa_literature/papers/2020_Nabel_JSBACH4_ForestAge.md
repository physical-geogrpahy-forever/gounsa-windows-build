# 서지정보
Nabel, J. E. M. S., Naudts, K., & Pongratz, J. (2020). Accounting for forest age in the tile-based dynamic global vegetation model JSBACH4 (4.20p7; git feature/forests) – a land surface model for the ICON-ESM. Geoscientific Model Development, 13, 185–200. https://doi.org/10.5194/gmd-13-185-2020

# 이 논문을 찾은 이유
기존 후보와 중복되지 않는 spatial age/cohort vegetation model인지, 그리고 고운사에서 individual-tree보다 가벼운 cohort middle ground가 될 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 개발
- tile-based DGVM / land-surface model

# 공간 구조
- hierarchical tile structure
- forest PFT 아래에 forest age classes를 추가
- geographic terrain cell 내부의 literal x-y cohort가 아니라 subgrid tile fractions

# 적용 환경
- global land-surface / Earth system modelling
- forest management 및 disturbance age structure

# 핵심 과정
- photosynthesis
- respiration
- forest age tracking
- disturbance/management에 따른 age-class redistribution
- tile별 ecosystem processes

# 식생 입력
- forest PFT
- age classes
- land-use/disturbance information

# 핵심 식
본 검토에서는 age-class transfer와 tile architecture가 핵심이다. 논문은 제한된 수의 age classes를 통해 age-dependent ecosystem processes를 계산한다.

# 파라미터와 단위
- forest age classes를 subgrid tile hierarchy로 관리
- 세부 parameter는 원 논문 및 JSBACH4 설정 재확인 필요

# 원 논문의 구현 범위
- 기존 tile-based JSBACH4에 forest age structure 추가
- exact forest age tracking과 age-dependent process calculation
- global/ESM scale

# 고운사에 직접 사용할 수 있는 부분
- computationally efficient age-class bookkeeping의 참고
- disturbance 이후 forest age redistribution의 비교 구조

# 새로운 coupling이 필요한 부분
- actual 10–50 m terrain grid에서 cohort geography
- explicit herb/shrub understory demography
- hillslope lateral hydrology와 geomorphic state exchange
- erosion/deposition soil-layer remapping

# 한계
- age-class tile은 고운사 기준의 spatial cohort와 다르다.
- explicit understory herb/shrub demographic strata가 핵심 구조가 아니다.
- fine hillslope/catchment precedent가 부족하다.

# 최종 판정
- 탈락
- efficient age-class DGVM benchmark로만 유지

# 참고 링크 / DOI
- https://doi.org/10.5194/gmd-13-185-2020
