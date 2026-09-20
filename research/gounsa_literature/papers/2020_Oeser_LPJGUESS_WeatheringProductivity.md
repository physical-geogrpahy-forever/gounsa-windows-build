# 서지정보
Oeser, R. A., & von Blanckenburg, F. (2020). Do degree and rate of silicate weathering depend on plant productivity? *Biogeosciences, 17*, 4883-4917.

# 이 논문을 찾은 이유
LPJ-GUESS NPP를 weathering multiplier로 직접 써도 되는지 검증하기 위해 검토했다.

# 연구 유형
- 현장비교 + geochemical analysis
- LPJ-GUESS NPP 사용

# 공간 구조
- 기후/식생 transect

# 적용 환경
- arid shrubland
- sclerophyll woodland
- humid temperate forest

# 핵심 과정
- silicate weathering
- denudation
- nutrient recycling

# 식생 입력
- LPJ-GUESS NPP

# 핵심 식
보편적인 `NPP 증가 -> weathering 증가` 관계가 확인되지 않았으며 denudation rate가 더 강한 제어변수로 정리됨.

# 파라미터와 단위
NPP 범위와 geochemical weathering rates. 세부값은 원문 재검증 필요.

# 원 논문의 구현 범위
식생생산성과 weathering의 현장관계를 검토한다.

# 고운사에 직접 사용할 수 있는 부분
NPP를 단순 weathering multiplier로 쓰지 말아야 한다는 반례.

# 새로운 coupling이 필요한 부분
NPP를 직접 multiplier가 아니라 root growth, exudation, respiration, nutrient demand의 upstream state로 쓰는 구조는 새로운 coupling.

# 한계
지형발달모델이 아니라 현장/지화학 검증연구.

# 최종 판정
- 핵심 제약근거

# 참고 링크 / DOI
https://doi.org/10.5194/bg-17-4883-2020
