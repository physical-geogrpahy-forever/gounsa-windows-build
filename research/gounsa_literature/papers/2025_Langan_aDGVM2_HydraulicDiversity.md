# 서지정보
Langan, L., Scheiter, S., Hickler, T., & Higgins, S. I. (2025). Amazon forest resistance to drought is increased by diversity in hydraulic traits. Nature Communications, 16, 8246. https://doi.org/10.1038/s41467-025-63600-1

# 이 논문을 찾은 이유
최신 aDGVM2에서 plant hydraulics, root architecture, daily timestep, current code availability를 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 응용 및 process enhancement
- trait-based individual vegetation model

# 공간 구조
- representative 1 ha stands
- continental applications are multiple stands/grid locations
- lateral terrain hydrology는 없음

# 적용 환경
- Amazon forest
- drought experiments and continental climate scenarios

# 핵심 과정
- daily individual vegetation
- improved plant hydraulics
- root architecture and rooting depth
- competition for water
- functional trait diversity
- reproduction, inheritance, mutation
- mortality and biomass response to drought

# 식생 입력
- individual adaptive traits
- hydraulic traits
- below-ground allocation
- root shape and depth
- climate and soil state

# 핵심 식
plant hydraulic and trait framework가 individual performance와 water competition에 연결된다. 각 plant의 root architecture와 rooting depth가 water availability 및 경쟁 결과에 영향을 준다.

# 파라미터와 단위
- 1 ha stand
- daily time step
- daily climate forcing
- hydraulic trait ranges
- root depth and root-shape traits
- exact equations and parameter tables are in the article supplementary notes

# 원 논문의 구현 범위
- 1 ha stand daily simulations
- tropical forest drought experiments
- trait diversity and water competition
- 2025 study-specific code snapshot archived openly on Zenodo

# 소프트웨어 가용성
Zenodo record:
- aDGVM2 v1.0-LL
- DOI 10.5281/zenodo.16265491
- C++ source including adgvm.cpp and water-model files
- record describes the software as Open
- development status is marked Unsupported

따라서 older project pages의 historical non-public status만으로 현재 aDGVM2를 closed-source라고 단정하면 안 된다.

# 고운사에 직접 사용할 수 있는 부분
- criterion 3 local soil-water/root-hydraulic response의 강한 process reference
- criterion 5 daily timestep 직접 근거
- root depth/shape trait를 vegetation response에 반영하는 구조
- code audit가 가능한 study-specific open snapshot

# 새로운 coupling이 필요한 부분
- external geomorphic model에서 soil-water/layer state를 overwrite하는 API
- lateral hillslope flow
- dynamic soil geometry remapping
- 2D-aDGVM spatial branch와 aDGVM2 최신 hydraulics integration

# 한계
- Amazon/tropical focus
- 1 ha representative stands
- full individual-based computational burden
- published external hydrology coupling 없음

# 최종 판정
- 강한 process benchmark
- aDGVM2를 conditional candidate로 유지하는 근거
- 현재 top production shortlist를 바로 교체하지는 않음

# 참고 링크 / DOI
- https://doi.org/10.1038/s41467-025-63600-1
- code: https://doi.org/10.5281/zenodo.16265491
