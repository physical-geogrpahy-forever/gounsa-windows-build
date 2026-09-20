# 서지정보
Tan, Z., Leung, L. R., Li, H.-Y., & Cohen, S. (2022). Representing global soil erosion and sediment flux in Earth system models. *Journal of Advances in Modeling Earth Systems, 14*, e2021MS002756.

# 이 논문을 찾은 이유
PFT별 root biomass가 유수침식계수에 들어가는 실제 수치모델 선례를 확인하기 위해 검토했다.

# 연구 유형
- 수치모델

# 공간 구조
- 전지구 distributed Earth-system erosion model

# 적용 환경
- 전지구

# 핵심 과정
- rainfall-driven erosion
- runoff-driven erosion
- sediment flux

# 식생 입력
- PFT별 topsoil root biomass density
- cover, LAI, residue 변수도 사용

# 핵심 식
root biomass protection 계수 `b_R`가 PFT-specific이며 rainfall-driven과 runoff-driven erosion에서 계수를 구분한다.

# 파라미터와 단위
PFT-specific root coefficient. 정확한 표와 단위는 원문 재검증 필요.

# 원 논문의 구현 범위
ELM 내부 PFT 상태를 erosion parameterization에 반영한다.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS FineRootC를 PFT별 erosion resistance로 연결할 직접적인 모델 선례.

# 새로운 coupling이 필요한 부분
ELM 식 전체를 이식하지 않고 LPJ-GUESS root pool로 대체하면 새로운 coupling.

# 한계
cover, LAI, residue도 함께 쓰며 산지 2D 집중류 전용모델은 아니다.

# 최종 판정
- 채택 후보의 핵심 보조근거

# 참고 링크 / DOI
https://doi.org/10.1029/2021MS002756
