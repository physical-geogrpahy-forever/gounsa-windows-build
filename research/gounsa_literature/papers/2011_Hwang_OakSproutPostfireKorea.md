# 서지정보
Hwang, H., Ryu, S.-R., & Lim, J. (2011). Oak sprout dynamics after a 1996 stand-replacing fire in Korea. *Forest Science and Technology, 7*(4), 184-191. https://doi.org/10.1080/21580103.2011.640809

# 이 논문을 찾은 이유
고운사와 같은 한국 산지 산불 후 참나무류가 왜 빠르게 우점할 수 있는지, 특히 얕고 발달이 불량한 산지 토양에서 맹아재생의 역할을 확인하기 위해 검토했다.

# 연구 유형
- 장기 산불 후 현장조사

# 공간 구조
- burned forest plots

# 적용 환경
- Goseong-gun, Gangwon-do, Korea
- 산지
- poorly developed soil
- stand-replacing wildfire

# 핵심 과정
- postfire sprouting
- natural regeneration
- oak replacement of pine
- disturbance legacy

# 식생 입력
- Quercus dentata
- Q. mongolica
- Q. serrata
- Q. variabilis
- pre-existing stump/root systems

# 핵심 식
보편 경쟁식보다 regeneration mechanism이 핵심이다.
산불 후 참나무는 기존 stump/root system에서 즉시 sprouting할 수 있어 seedling establishment를 처음부터 거치지 않는다.

# 파라미터와 단위
sprout abundance, height/growth, stump/root condition 등. 세부값은 원문 사용 시 재검증한다.

# 원 논문의 구현 범위
1996 고성 대형산불 뒤 자연복원지에서 주요 참나무류의 sprout dynamics를 추적한다.

# 고운사에 직접 사용할 수 있는 부분
- 산불 후 oak dominance를 단순 soil-moisture optimum이 아니라 **pre-existing rootstock + resprouting legacy**로 모델링할 강한 국내 근거
- 얕고 발달이 불량한 산지토양에서도 참나무 맹아가 빠르게 산림을 재형성할 수 있음

# 새로운 coupling이 필요한 부분
LPJ-GUESS disturbance mortality 뒤 surviving belowground reserve/rootstock에서 resprout cohort를 생성하는 규칙은 **새로운 coupling**이다.

# 한계
석력피복 자체를 독립변수로 조작한 연구는 아니므로 `high armour -> oak`의 직접증거는 아니다.

# 최종 판정
- 핵심 채택
- 고운사 oak postfire regeneration의 직접 국내근거

# 참고 링크 / DOI
https://doi.org/10.1080/21580103.2011.640809
