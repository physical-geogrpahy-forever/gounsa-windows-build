# 서지정보
Lapides, D. A., Hahm, W. J., Forrest, M., Rempe, D. M., Hickler, T., & Dralle, D. (2024). Inclusion of bedrock vadose zone in dynamic global vegetation models is key for simulating vegetation structure and function. *Biogeosciences, 21*(7), 1801-1826.

# 이 논문을 찾은 이유
LPJ-GUESS와 유사한 DGVM에서 soil 아래 weathered bedrock root zone을 명시적으로 표현할 필요성을 확인하기 위해 검토했다.

# 연구 유형
- 수치모델

# 공간 구조
- vertical soil + weathered bedrock reservoir

# 적용 환경
- 얕은 토양 위 weathered/fractured bedrock

# 핵심 과정
- root water access
- bedrock vadose storage
- vegetation structure/function

# 식생 입력
- root distribution
- vegetation water demand

# 핵심 식
soil-only root zone과 bedrock vadose reservoir를 구분해 vegetation water access를 모의하는 구조.

# 파라미터와 단위
bedrock moisture storage, rooting depth, transpiration 관련 변수. 세부식은 원문 재검증 필요.

# 원 논문의 구현 범위
weathered bedrock moisture reservoir를 DGVM에 추가한다.

# 고운사에 직접 사용할 수 있는 부분
고운사에서 `Z_r > H_AB` 및 C/Cr water storage를 허용해야 한다는 강한 구조적 근거.

# 새로운 coupling이 필요한 부분
C/Cr root access를 hydrology뿐 아니라 chemical weathering에 연결하면 새로운 coupling.

# 한계
지형발달모델 자체는 아니다.

# 최종 판정
- 핵심 보조근거

# 참고 링크 / DOI
https://doi.org/10.5194/bg-21-1801-2024
