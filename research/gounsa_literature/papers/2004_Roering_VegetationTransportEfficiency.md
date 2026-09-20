# 서지정보
Roering, J. J., Almond, P., Tonkin, P., & McKean, J. (2004). Constraining climatic controls on hillslope dynamics using a coupled model for the transport of soil and tracers: Application to loess-mantled hillslopes, South Island, New Zealand. *Journal of Geophysical Research: Earth Surface, 109*, F01010.

# 이 논문을 찾은 이유
grass/shrub에서 forest로 바뀔 때 bioturbation transport efficiency가 달라지는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 / 역산

# 공간 구조
- hillslope

# 적용 환경
- loess hillslope
- 식생체제 변화

# 핵심 과정
- diffusive soil transport
- tracer transport

# 식생 입력
- grass/shrub vs forest 식생체제

# 핵심 식
식생체제별 transport coefficient `K`를 역산한다. biomass 직접식은 아니다.

# 파라미터와 단위
forest 조건 예시 `K_H≈0.016±0.005 m² yr⁻¹`가 이 채팅 정리에서 기록됨.

# 원 논문의 구현 범위
식생체제 변화가 hillslope transport efficiency를 바꾼다.

# 고운사에 직접 사용할 수 있는 부분
고정 `D` 하나를 천이 전 기간에 쓰면 안 된다는 독립 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS biomass로 `K`를 동적으로 계산하려면 새로운 coupling.

# 한계
biomass 직접 입력이 아님.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1029/2003JF000034
