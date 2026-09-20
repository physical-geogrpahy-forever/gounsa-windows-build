# 서지정보
Wang, C., Fu, X., Zhang, X., Wang, X., Zhang, G., & Gong, Z. (2024). Modeling soil erosion dynamic processes along hillslopes with vegetation impact across different land uses on the Loess Plateau of China. *CATENA, 243*, 108202.

# 이 논문을 찾은 이유
woodland, grassland, farmland에서 vegetation effect를 detachment와 sediment transport capacity에 각각 넣는 최신 hillslope erosion model로 검토했다.

# 연구 유형
- 수치모델

# 공간 구조
- hillslope dynamic erosion model

# 적용 환경
- Loess Plateau
- 다양한 land use

# 핵심 과정
- soil detachment capacity
- sediment transport capacity

# 식생 입력
- vegetation impact parameter
- 직접 입력은 주로 cover 계열로 정리됨

# 핵심 식
vegetation이 `D_c`와 `T_c`를 서로 다른 decay 방식으로 수정. woodland > grassland > farmland의 vegetation effect가 보고됨.

# 파라미터와 단위
vegetation decay coefficients. 정확한 수치와 단위는 원문 재검증 필요.

# 원 논문의 구현 범위
detachment와 transport capacity의 feedback을 동적으로 계산.

# 고운사에 직접 사용할 수 있는 부분
목본과 초본의 process parameter가 동일하지 않다는 수치모델 선례.

# 새로운 coupling이 필요한 부분
LPJ-GUESS biomass/root traits로 VED vegetation parameter를 설명하려면 새로운 coupling.

# 한계
biomass 직접 입력보다는 vegetation cover 중심.

# 최종 판정
- 보조근거
- 유수침식 구조 후보

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2024.108202
