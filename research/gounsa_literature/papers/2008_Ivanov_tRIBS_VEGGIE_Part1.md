# 서지정보
Ivanov, V. Y., Bras, R. L., & Vivoni, E. R. (2008). *Vegetation-hydrology dynamics in complex terrain of semiarid areas: 1. A mechanistic approach to modeling dynamic feedbacks*. Water Resources Research, 44, W03429. DOI: 10.1029/2006WR005588.

# 이 논문을 찾은 이유
tRIBS-VEGGIE-FEaST 계열에서 VEGGIE가 실제로 어떤 quantitative vegetation/root states를 계산하는지, 그리고 이 상태들이 erosion model에 연결될 잠재성이 있는지 확인하기 위해 검토했다.

# 연구 유형
- dynamic ecohydrological numerical model
- vegetation-water-energy-carbon coupling

# 공간 구조
- distributed TIN basin model
- complex topography
- soil layers/root profile

# 적용 환경
- semiarid ecosystems
- central New Mexico validation

# 핵심 과정
- photosynthesis
- stomatal control
- carbon assimilation
- carbon allocation
- foliage loss
- recruitment
- phenology
- soil-water uptake
- energy balance
- dynamic vegetation growth

# 식생 입력/상태
VEGGIE is not a simple cover model.

It explicitly includes:
- vegetation carbon pools
- leaves
- living sapwood for woody PFTs
- fine roots
- carbohydrate reserves
- PFT-specific allometry
- LAI derived from carbon pools
- fine-root allocation
- root-depth distribution

Relative fine-root fraction by soil layer is represented with an exponential root profile based on Jackson et al. (1996), with a vegetation-type-specific decay parameter.

During normal growth, assimilated carbon is allocated among leaves, living sapwood and fine roots.

# 핵심 식
The paper derives time-varying vegetation characteristics from PFT-specific carbon pools and allometry.

Root distribution:
an exponential vertical profile provides the relative fine-root fraction in each soil layer, allowing different vegetation types to have distinct root distributions.

Exact equation symbols and coefficients should be taken from the original paper before implementation.

# 파라미터와 단위
- carbon pools
- fine-root biomass
- root distribution decay parameter
- LAI
- PFT-specific allometric parameters
- hourly to interannual vegetation states

# 원 논문의 구현 범위
Dynamic vegetation and ecohydrology, including quantitative carbon allocation and root distribution, are solved over complex terrain.

# 고운사에 직접 사용할 수 있는 부분
Important structural precedent:
```
dynamic vegetation carbon pools
 -> fine-root biomass
 -> soil-layer root distribution
```

This demonstrates that the tRIBS family already contained the ecological state variables needed for a quantitative root-erosion coupling before FEaST was added.

# 새로운 coupling이 필요한 부분
This paper does not connect root biomass to erosion resistance. Any:
```
fine-root biomass / RLD
 -> FEaST J, a, UC
```
linkage remains a **new coupling**.

# 한계
- semiarid-focused vegetation model
- not an erosion paper
- LPJ-GUESS remains the vegetation model chosen for Gounsa

# 최종 판정
- **채택: dynamic quantitative vegetation-state precedent**
- not the final vegetation model for Gounsa
- important evidence that coupling dynamic root states to tRIBS/FEaST is conceptually consistent with the model family

# 참고 링크 / DOI
https://doi.org/10.1029/2006WR005588
