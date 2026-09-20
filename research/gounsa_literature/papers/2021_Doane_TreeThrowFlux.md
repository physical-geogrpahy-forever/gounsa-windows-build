# 서지정보
Doane, T. H., Edmonds, D. A., Yanites, B. J., & Lewis, Q. (2021). Topographic roughness on forested hillslopes: A theoretical approach for quantifying hillslope sediment flux from tree throw. *Geophysical Research Letters, 48*(20), e2021GL094987.

# 이 논문을 찾은 이유
tree throw를 background creep와 분리해 정량화할 모델식을 찾기 위해 검토했다.

# 연구 유형
- 수치 / 이론모델

# 공간 구조
- forested hillslope

# 적용 환경
- 산림 사면

# 핵심 과정
- tree throw sediment flux
- topographic roughness

# 식생 입력
- tree-throw frequency
- tree-generated pit-mound geometry

# 핵심 식
평균 flux를 tree-throw volumetric entrainment rate와 mean travel distance의 곱 형태로 정량화한다.

# 파라미터와 단위
tree-throw frequency, displaced volume, travel distance.

# 원 논문의 구현 범위
tree throw를 연속 creep와 분리해 hillslope sediment flux로 계산한다.

# 고운사에 직접 사용할 수 있는 부분
고운사 `q_treethrow` 별도항의 직접 모델 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS tree size/density/mortality를 throw frequency와 volume으로 연결하는 것은 새로운 coupling.

# 한계
목본 전용이며 root-growth flux는 별도 필요.

# 최종 판정
- 채택 후보

# 참고 링크 / DOI
https://doi.org/10.1029/2021GL094987
