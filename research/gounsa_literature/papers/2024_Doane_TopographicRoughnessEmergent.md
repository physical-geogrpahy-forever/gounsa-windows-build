# 서지정보
Doane, T. H., et al. (2024). Topographic roughness as an emergent property of geomorphic processes and events. *AGU Advances, 5*, e2024AV001264. https://doi.org/10.1029/2024AV001264

# 이 논문을 찾은 이유
tree throw와 연속적인 creep을 한 diffusion coefficient에 뭉개지 않고 별도 process로 결합할 최신 이론을 찾기 위해 검토했다.

# 연구 유형
- 이론/수치모델

# 공간 구조
- hillslope roughness model

# 적용 환경
- forested hillslope

# 핵심 과정
- stochastic tree throw
- creep-like smoothing
- topographic roughness

# 식생 입력
- tree-throw event production rate

# 핵심 식
현재 채팅에서 복구된 개념형:
`mu_r = C * mu_p / K`
여기서 mu_r은 평균 roughness, mu_p는 stochastic roughening-event production rate, K는 smoothing diffusivity, C는 pit-mound geometry 계수이다.

# 파라미터와 단위
mu_p, K, pit-mound geometry. 정확한 정의와 단위는 원문 재검증 필요.

# 원 논문의 구현 범위
이산적 tree-throw roughening과 연속적 diffusion smoothing의 경쟁으로 topographic roughness를 설명한다.

# 고운사에 직접 사용할 수 있는 부분
`q_hill = q_creep + q_tree-throw`처럼 discrete event와 continuous transport를 분리해야 한다는 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS mortality/DBH를 mu_p로 변환하는 것은 **새로운 coupling**이다.

# 한계
root-growth bioturbation과 산불 CWD storage는 별도 과정이다.

# 최종 판정
- 보조근거
- tree throw와 creep 분리의 핵심 이론

# 참고 링크 / DOI
https://doi.org/10.1029/2024AV001264
