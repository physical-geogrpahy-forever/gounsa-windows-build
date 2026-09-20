# 서지정보
Hao, H., Di, H., Jiao, X., Wang, J., Guo, Z., & Shi, Z. (2020). Fine roots benefit soil physical properties key to mitigate soil detachment capacity following the restoration of eroded land. *Plant and Soil, 446*, 487-501.

# 이 논문을 찾은 이유
woodland, scrubland, grassland를 함께 비교하면서 fine-root length density와 soil detachment를 직접 연결한 실험근거를 찾기 위해 검토했다.

# 연구 유형
- 현장/실험

# 공간 구조
- plot

# 적용 환경
- woodland
- scrubland
- grassland
- bare land

# 핵심 과정
- soil detachment

# 식생 입력
- fine-root length density
- root length density
- soil shear strength

# 핵심 식
이 채팅 정리에는 예시 경험식 `D_c = 5.35 RLD_fine^-0.44`, `D_c = 24.73 SS^-0.95`가 기록됨.

# 파라미터와 단위
RLD, shear strength. 연구지 특이 계수로 직접 이식 금지.

# 원 논문의 구현 범위
fine roots가 soil physical properties와 detachment를 어떻게 바꾸는지 현장자료로 분석.

# 고운사에 직접 사용할 수 있는 부분
FineRootC -> fine-root length density -> detachment 저항의 parameterization evidence.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC를 RLD로 바꾸고 수치침식모델에 연결하는 것은 새로운 coupling.

# 한계
수치 지형모델이 아니라 실험/통계 연구.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1007/s11104-019-04353-x
