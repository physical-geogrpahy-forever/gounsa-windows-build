# 서지정보
Doane, T. H., Yanites, B. J., Edmonds, D. A., & Novick, K. A. (2023). Hillslope roughness reveals forest sensitivity to extreme winds. *Proceedings of the National Academy of Sciences, 120*(3), e2212105120. https://doi.org/10.1073/pnas.2212105120

# 이 논문을 찾은 이유
tree throw를 고정 확산계수 대신 동적 산림구조와 극한풍 사건에 연결할 최근 연구를 찾기 위해 검토했다.

# 연구 유형
- 수치/통계 모델
- 지형관측 해석

# 공간 구조
- forested hillslope
- pit-mound roughness

# 적용 환경
- 산림사면

# 핵심 과정
- tree throw
- extreme wind
- stochastic roughening

# 식생 입력
- tree population sensitivity
- forest roughness signal

# 핵심 식
forest-floor roughness에서 tree-throw frequency의 확률분포를 추정하고 이를 extreme-wind distribution과 연결한다. 상세식은 원문 재검증 필요.

# 파라미터와 단위
tree-throw frequency, roughness, wind statistics. 세부 단위 원문 재검증 필요.

# 원 논문의 구현 범위
tree throw가 산림의 교란체제와 극한풍에 의해 시간적으로 변할 수 있음을 정량화한다.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS woody cohort와 풍속 forcing을 이용해 tree-throw probability를 시간변화시키는 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS DBH, density, mortality를 이 논문의 roughness 기반 tree-throw frequency에 직접 연결하면 **새로운 coupling**이다.

# 한계
root-growth creep나 유수침식을 계산하는 모델은 아니다.

# 최종 판정
- 보조근거
- tree-throw disturbance forcing에 채택 후보

# 참고 링크 / DOI
https://doi.org/10.1073/pnas.2212105120
