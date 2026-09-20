# 서지정보
Pawlik, Ł., Šamonil, P., Král, K., Adam, D., & Godziek, J. (2026). Wind and Topographic Impacts on Forest Biogeomorphic Disturbances. Land Degradation & Development, 37(12), 8095-8111. https://doi.org/10.1002/ldr.70641

# 이 논문을 찾은 이유
tree uprooting과 soil transport를 species, forest structure, extreme wind, slope exposure와 함께 설명하는 최신 자료를 찾기 위해 검토했다.

# 연구 유형
- 장기 tree census + geomorphic analysis

# 공간 구조
- forested hillslope

# 적용 환경
- 산림사면

# 핵심 과정
- tree uprooting
- soil transport
- wind disturbance
- topographic control

# 식생 입력
- tree species
- forest structure
- tree-fall direction

# 핵심 식
현재 채팅에서 단일 보편 flux 식은 확인하지 않았다.

# 파라미터와 단위
uprooting probability, tree structure, wind, slope aspect. 세부 단위 원문 재검증 필요.

# 원 논문의 구현 범위
tree uprooting과 soil transport가 tree species, forest structure, extreme wind, slope exposure에 의해 달라짐을 분석한다.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS woody cohort size/density와 wind, aspect를 tree-throw probability에 연결할 최신 관측근거.

# 새로운 coupling이 필요한 부분
cohort state를 uprooting probability와 sediment flux로 바꾸는 것은 새로운 coupling이다.

# 한계
직접적인 root-growth creep 식은 아니다.

# 최종 판정
- 보조근거
- tree-throw forcing에 매우 중요

# 참고 링크 / DOI
https://doi.org/10.1002/ldr.70641
