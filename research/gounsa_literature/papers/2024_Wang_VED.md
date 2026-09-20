# 서지정보
Wang, C., Fu, X., Zhang, X., Wang, X., Zhang, G., & Gong, Z. (2024). *Modeling soil erosion dynamic processes along hillslopes with vegetation impact across different land uses on the Loess Plateau of China*. CATENA, 243, 108202. DOI: 10.1016/j.catena.2024.108202.

# 이 논문을 찾은 이유
woodland, grassland, farmland에서 vegetation effect를 soil detachment와 sediment transport capacity에 각각 넣는 최신 hillslope erosion model이 고운사에 더 좋은 단일 대안인지 확인하기 위해 재검토했다.

# 연구 유형
- process-based hillslope erosion numerical model
- runoff-plot calibration/validation

# 공간 구조
- 1D hillslope sediment-discharge evolution
- slope-length 방향 dynamic erosion model
- genuine 2D shallow-water solver는 아님

# 적용 환경
- Loess Plateau
- woodland
- grassland
- farmland
- multiple river basins/runoff-plot datasets

# 핵심 과정
- soil detachment capacity
- sediment transport capacity
- detachment-transport feedback
- vegetation-modified hydrodynamics

# 식생 입력
주 입력은 vegetation cover / land-use-specific vegetation effect이며 root biomass/RLD를 직접 상태변수로 사용하지 않는다.

# 핵심 식
VED는 Foster-Meyer 계열의 detachment-transport feedback을 바탕으로 vegetation이:
- soil detachment capacity `Phi`
- sediment transport capacity `T_c`
- runoff/hydrodynamic effect
를 서로 다른 decay relation으로 수정하도록 구성한다.

Calibration parameters include:
- `k1, beta1`
- `k2, beta2`
- `a1, a2`

# 파라미터와 단위
exact equations and units are retained in the original paper.
핵심은 vegetation decay coefficients가 woodland > grassland > farmland 순으로 달랐다는 점이다.

# 원 논문의 구현 범위
detachment와 transport capacity의 feedback을 dynamic hillslope model로 계산하고 vegetation impact를 양쪽 모두에 반영한다.

# 고운사에 직접 사용할 수 있는 부분
1. vegetation effect를 detachment뿐 아니라 sediment transport capacity에도 넣어야 할 수 있다는 model precedent
2. woody/grass/crop vegetation의 erosion-effect coefficient가 동일하지 않다는 근거
3. slope length가 길어질수록 vegetation sediment-reduction contribution이 변한다는 점

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC/litter/PFT traits로 VED vegetation parameters를 설명하려면 새로운 coupling이다.

# 한계
- vegetation effect가 quantitative root/litter mass 직접입력보다는 cover/land-use calibration 중심
- genuine 2D 아님
- Loess Plateau plot data 기반
- dynamic vegetation growth model과 직접 coupled되지 않음

# 최종 판정
- **보조근거**
- 식생이 detachment capacity와 transport capacity 모두를 바꿀 수 있다는 점은 중요
- 그러나 고운사의 strict 2D + quantitative vegetation 요구를 만족하는 최종 엔진은 아님

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2024.108202
