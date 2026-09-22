# 서지정보
Neuman, S. P. (1976). Wetting front pressure head in the infiltration model of Green and Ampt. *Water Resources Research, 12*(3), 564-566. https://doi.org/10.1029/WR012i003p00564

# 이 논문을 찾은 이유
고운사 stony-soil hydraulic conductivity curve K(h)를 Iber+ Green-Ampt의 wetting-front suction/pressure-head parameter로 바꿀 때 임의의 suction 값을 보정하지 않고 published theoretical relation을 사용할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- 이론 수문모델
- Green-Ampt parameter derivation

# 공간 구조
- 1D infiltration wetting front

# 적용 환경
- unsaturated infiltration

# 핵심 과정
- wetting-front pressure head
- relative hydraulic conductivity
- Green-Ampt infiltration

# 식생 입력
- 없음

# 핵심 식
Neuman은 Green-Ampt wetting-front pressure head를 soil hydraulic characteristics로부터 이론적으로 유도한다.
이 식은 Bouwer (1964)가 horizontal-flow analogy로 제안한 관계와 동일한 형태이다.

핵심적으로 wetting-front suction은 임의의 texture lookup 값을 써야 하는 상수가 아니라, soil hydraulic conductivity function을 이용해 결정할 수 있다.

정확한 수치 구현 시 Neuman 원문의 적분식과 부호 convention을 그대로 따른다.

# 파라미터와 단위
- relative hydraulic conductivity
- matric/pressure head
- wetting-front pressure head

# 원 논문의 구현 범위
Green-Ampt의 wetting-front pressure parameter를 underlying hydraulic functions와 연결한다.

# 고운사에 직접 사용할 수 있는 부분
- stony-soil effective K(h)가 확보되면 Iber+ Green-Ampt의 suction parameter를 별도 calibration 없이 산정할 수 있는 published 이론근거
- GEM/HYDRUS-derived hydraulic curve와 Iber Green-Ampt 사이의 비자의적 parameter bridge

# 새로운 coupling이 필요한 부분
stony-soil effective K(h)를 Neuman relation에 넣어 Iber+ input으로 생성하는 software workflow 자체는 새로운 coupling이지만 새 경험식은 아니다.

# 한계
Green-Ampt의 sharp wetting-front approximation 자체의 한계는 남는다.

# 최종 판정
- 핵심 채택
- Iber+ Green-Ampt suction parameter의 이론적 산정 근거

# 참고 링크 / DOI
https://doi.org/10.1029/WR012i003p00564
