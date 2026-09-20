# 서지정보
Yang, L., Chu, W., Zhang, W., Zhang, L., Huang, B., Wang, Z., Wang, T., Yang, X., & Wu, Y. (2026). *The potential alleviation of vegetation restoration on future soil erosion in China using a coupled dynamic vegetation evolution model*. Environmental Impact Assessment Review, article 108550. DOI: 10.1016/j.eiar.2026.108550.

# 이 논문을 찾은 이유
LPJ-GUESS를 실제 soil-erosion model과 coupled한 최신 논문이 quantitative biomass/root coupling을 제공하는지 확인하기 위해 검토했다.

# 연구 유형
- coupled dynamic vegetation + empirical soil-loss assessment
- national-scale scenario modeling

# 공간 구조
- China-wide regional grid
- hillslope process-based 2D erosion model 아님

# 적용 환경
- China
- potential natural vegetation restoration
- SSP2-4.5 future scenario

# 핵심 과정
- LPJ-GUESS vegetation succession
- rainfall erosivity / soil-loss assessment through CSLE
- restoration effects on erosion

# 식생 입력
LPJ-GUESS outputs include LAI and PFT dynamics, but erosion coupling proceeds through:
```
LPJ-GUESS LAI
 -> Fractional Vegetation Cover (FVC)
 -> CSLE B factor
 -> soil loss
```

# 핵심 식
The study converts simulated PNV-LAI to FVC using a canopy radiative-transfer approach and then computes the vegetation-related CSLE B factor.

# 파라미터와 단위
- LAI
- FVC
- CSLE B factor
- rainfall/soil/topographic CSLE factors

# 원 논문의 구현 범위
Dynamic vegetation evolution is used to update an empirical/semi-empirical soil-loss factor at national scale.

# 고운사에 직접 사용할 수 있는 부분
- confirms LPJ-GUESS can operationally drive erosion assessments through time
- useful precedent for temporal coupling and PFT/LAI outputs

# 새로운 coupling이 필요한 부분
A quantitative FineRootC/litter -> physically based detachment model is not provided. Creating that linkage remains a new coupling.

# 한계
- LAI is transformed to FVC
- vegetation effect is a cover/B-factor representation
- no rill/interrill process separation
- no 2D flow
- no sediment routing/morphodynamics
- does not meet Gounsa strict quantitative-biomass criterion

# 최종 판정
- **탈락 as final Gounsa water-erosion formulation**
- retain only as direct LPJ-GUESS-to-erosion coupling precedent
- do not use its LAI -> FVC -> B-factor pathway in the final model

# 참고 링크 / DOI
https://doi.org/10.1016/j.eiar.2026.108550
