# 서지정보
De Baets, S., Poesen, J., Gyssels, G., & Knapen, A. (2006). Effects of grass roots on the erodibility of topsoils during concentrated flow. *Geomorphology, 76*, 54-67.

# 이 논문을 찾은 이유
LPJ-GUESS FineRootC를 RLD/RD로 변환해 유수박리에 연결할 실험근거로 검토했다.

# 연구 유형
- 현장/수로 실험

# 공간 구조
- plot / flume

# 적용 환경
- 초본 토양
- concentrated flow

# 핵심 과정
- soil detachment

# 식생 입력
- root density
- root length density

# 핵심 식
상대 soil detachment가 root density 또는 RLD 증가에 따라 음의 지수형으로 감소하는 경험관계가 보고됨.

# 파라미터와 단위
RD/RLD와 경험계수. 연구지별 값 직접 이식 금지.

# 원 논문의 구현 범위
뿌리량과 concentrated-flow detachment의 실험관계.

# 고운사에 직접 사용할 수 있는 부분
FineRootC -> RLD 변환의 parameterization evidence.

# 새로운 coupling이 필요한 부분
이 회귀식을 수치모델에 넣는 것은 새로운 coupling.

# 한계
수치 지형모델이 아니라 실험연구.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.geomorph.2005.10.002
