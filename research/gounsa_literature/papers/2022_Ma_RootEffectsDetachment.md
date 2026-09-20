# 서지정보
Ma, J., Li, Z., Sun, B., & Ma, B. (2022). Mechanism and modeling of different plant root effects on soil detachment rate. *CATENA, 212*, 106109.

# 이 논문을 찾은 이유
초본, 관목, 교목을 하나의 실험계에서 비교하면서 root effect를 모델링한 연구를 찾기 위해 검토했다.

# 연구 유형
- 실험 + 예측모델

# 공간 구조
- plot/flume

# 적용 환경
- 초본
- 관목
- 교목

# 핵심 과정
- soil detachment

# 식생 입력
- root mass density
- root-soil composite properties

# 핵심 식
root-sensitive zone, soil-property-dominant zone, stable zone을 구분하는 root-response structure를 제시. 정확한 식은 원문 재검증 필요.

# 파라미터와 단위
RMD와 soil properties.

# 원 논문의 구현 범위
Agropyron, Medicago, Caragana, Robinia 등 식물형을 비교하고 detachment prediction model을 개발.

# 고운사에 직접 사용할 수 있는 부분
초본/관목/교목을 하나의 universal biomass coefficient로 처리하지 않을 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS PFT root mass와 soil properties를 detachment model에 연결하면 새로운 coupling.

# 한계
landscape evolution model이 아니라 실험기반 예측모델.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2022.106109
