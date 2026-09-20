# 서지정보
Gurung, K., Field, K. J., Batterman, S. A., Poulton, S. W., et al. (2024). Geographic range of plants drives long-term climate change. Nature Communications, 15, 1805. https://doi.org/10.1038/s41467-024-46105-1

# 이 논문을 찾은 이유
dynamic vegetation model의 생산성을 chemical weathering modifier에 직접 넣는 최근 수치모델을 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- Earth system / deep-time biogeochemical model

# 공간 구조
- global gridded model

# 적용 환경
- 전지구
- 지질시대

# 핵심 과정
- biotic silicate weathering enhancement
- vegetation productivity
- carbon cycle feedback

# 식생 입력
- FLORA dynamic vegetation NPP
- broad plant functional types

# 핵심 식
현재 채팅에서 복구된 식:
f_biota = 0.0005 * NPP + f_minbiota * RCO2^r
f_minbiota = 0.32

# 파라미터와 단위
NPP와 dimensionless weathering enhancement factor. 정확한 NPP 단위와 r은 원문 재검증 필요.

# 원 논문의 구현 범위
동적 식생모델의 생산성을 global silicate weathering에 직접 연결한다.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS NPP를 chemical-weathering modifier로 쓰는 구조적 선례.

# 새로운 coupling이 필요한 부분
SCION-FLORA 계수를 고운사 R->C 또는 C/Cr 생산률에 적용하는 것은 새로운 coupling이며 계수 직접이식은 금지한다.

# 한계
deep-time global model이고 soil-production thickness를 직접 계산하지 않는다.

# 최종 판정
- 보조근거
- NPP-weathering coupling의 최근 선례

# 참고 링크 / DOI
https://doi.org/10.1038/s41467-024-46105-1
