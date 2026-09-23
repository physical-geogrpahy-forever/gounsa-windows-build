# 서지정보
Pfeiffer, M., Hoffmann, M. P., Scheiter, S., Nelson, W., Isselstein, J., Ayisi, K., Odhiambo, J. J., & Rötter, R. (2022). Modeling the effects of alternative crop-livestock management scenarios on important ecosystem services for smallholder farming from a landscape perspective. Biogeosciences, 19, 3935–3957. https://doi.org/10.5194/bg-19-3935-2022

# 이 논문을 찾은 이유
aDGVM2가 daily vegetation dynamics와 grass/tree/shrub growth forms를 실제 multi-hectare landscape application에서 사용한 선례를 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 응용
- landscape/rangeland management simulation

# 공간 구조
- representative 1 ha stands
- multiple hectares/subareas simulated across landscape
- internal lateral hydrology between hectares는 없음

# 적용 환경
- smallholder crop-livestock landscape
- grassland and woodland

# 핵심 과정
- daily individual plant growth/state
- competition
- grazing
- biomass dynamics
- grass/tree/shrub life forms
- annual/perennial grass strategies
- reproduction and mortality inherited from aDGVM2

# 식생 입력
- growth form: grass, tree, shrub, perennial or annual grass
- leaf traits
- allocation traits
- root and crown shape
- fire response
- reproduction
- mortality

# 핵심 식
본 검토에서는 process schedule과 growth-form structure가 핵심이다. aDGVM2는 representative 1 ha stand에서 개별 식물의 일별 성장과 상태를 계산한다.

# 파라미터와 단위
- 1 ha representative stands
- daily vegetation state
- grazing intensity and land-use management
- trait-based plant state

# 원 논문의 구현 범위
- landscape-level scenario with many individual hectare simulations
- explicit grass, tree, shrub and annual/perennial grass growth forms
- daily plant dynamics

# 고운사에 직접 사용할 수 있는 부분
- criterion 2와 5의 강한 근거
- herb, shrub and tree life forms가 동일 vegetation engine에서 경쟁하는 사례
- early succession biological benchmark

# 새로운 coupling이 필요한 부분
- cells 간 lateral water flow
- actual terrain connectivity
- erosion/deposition state remap
- Korean postfire species/trait initialization

# 한계
- landscape is an ensemble of 1 ha stands rather than hydrologically connected terrain cells
- tropical/subtropical rangeland-oriented parameterization
- full individual-based computation

# 최종 판정
- 보조근거
- aDGVM2 criterion 2 and 5 evidence

# 참고 링크 / DOI
- https://doi.org/10.5194/bg-19-3935-2022
