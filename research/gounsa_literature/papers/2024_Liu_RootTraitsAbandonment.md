# 서지정보
Liu, L., Zhang, K., Wang, P., Shi, W., Liu, J., & Li, Y. (2024). Effects of root traits on soil detachment capacity driven by farmland abandonment. *CATENA, 239*, 107951.

# 이 논문을 찾은 이유
천이연령과 root traits가 soil detachment parameter를 어떻게 바꾸는지 검토했다.

# 연구 유형
- 현장/실험 + 예측식

# 공간 구조
- plot

# 적용 환경
- abandoned farmland succession

# 핵심 과정
- soil detachment
- erodibility

# 식생 입력
- RMD
- RLD
- RSAD

# 핵심 식
RSAD와 soil cohesion을 포함한 WEPP형 예측에서 `R²=0.95`, `NSE=0.95`가 이 채팅 정리에 기록됨.

# 파라미터와 단위
RSAD, cohesion, stream power 등.

# 원 논문의 구현 범위
5, 12, 24, 36년 천이단계를 비교.

# 고운사에 직접 사용할 수 있는 부분
FineRootC -> RSAD 변환의 최신 parameterization evidence.

# 새로운 coupling이 필요한 부분
LPJ-GUESS output을 RSAD로 변환해 유수침식식에 넣으면 새로운 coupling.

# 한계
완전한 landscape model이 아님.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2024.107951
