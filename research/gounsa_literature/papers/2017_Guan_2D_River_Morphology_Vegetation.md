# 서지정보
Guan, M., & Liang, Q. (2017). *A two-dimensional hydro-morphological model for river hydraulics and morphology with vegetation*. Environmental Modelling & Software, 88, 10-21. DOI: 10.1016/j.envsoft.2016.11.008.

# 이 논문을 찾은 이유
2D flow, sediment, vegetation, bank failure and bed deformation를 한 framework에 통합한 모델이 고운사 water-erosion engine보다 더 완성된 vegetation-morphodynamic precedent인지 확인하기 위해 검토했다.

# 연구 유형
- 2D integrated hydro-morphodynamic numerical model

# 공간 구조
- full 2D shallow-water equations
- non-equilibrium sediment transport
- bed deformation
- secondary-flow dispersion
- river-scale model

# 적용 환경
- laboratory channels
- natural river
- emergent/submerged vegetation
- hillslope rainfall erosion 아님

# 핵심 과정
- river hydraulics
- sediment transport
- bed deformation
- bank failure
- vegetation-induced flow resistance

# 식생 입력
- vegetation cover/patches
- emergent/submerged vegetation hydraulic properties
- no dynamic root biomass/RLD soil-detachment resistance identified

# 핵심 식
Vegetation primarily enters hydrodynamics/sediment transport through vegetation resistance and spatial cover.

# 파라미터와 단위
vegetation drag/cover and river sediment parameters; exact values in original paper.

# 원 논문의 구현 범위
2D river hydraulics and morphology with vegetation effects and bank failure.

# 고운사에 직접 사용할 수 있는 부분
Shows that vegetation can be integrated directly inside a full 2D hydro-morphological solver instead of only as an external post-processing coefficient.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root/litter states and rainfall soil detachment would require major **new coupling**.

# 한계
- river environment
- no rainfall/interrill erosion
- vegetation is mainly cover/drag, not quantitative belowground biomass

# 최종 판정
- structural precedent only
- not superior to current hillslope-engine candidates for Gounsa

# 참고 링크 / DOI
https://doi.org/10.1016/j.envsoft.2016.11.008
