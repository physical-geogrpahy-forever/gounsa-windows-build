# 서지정보
미복구. 2025년 Geoscientific Model Development의 LPJ-GUESS phosphorus-cycle 구현으로 현재 채팅에서 검토했다. 정확한 저자, 제목, DOI는 원문 재검증 필요.

# 이 논문을 찾은 이유
LPJ-GUESS 자체 계보 안에서 weathering flux를 prognostic runoff 및 lithology/temperature와 연결한 선례를 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- LPJ-GUESS 확장

# 공간 구조
- LPJ-GUESS patch/grid

# 적용 환경
- terrestrial ecosystem model

# 핵심 과정
- phosphorus weathering
- runoff-dependent weathering

# 식생 입력
직접 biomass weathering modifier는 현재 채팅에서 확인하지 않았다. LPJ-GUESS 내부 hydrology가 핵심이다.

# 핵심 식
현재 채팅에서 복구된 식:
F_PW = F_CW,i * F_T * F_s,i
F_CW,i = (b_carbonate + b_silicate)_i * p_i * q
여기서 q는 LPJ-GUESS patch의 prognostic runoff.

# 파라미터와 단위
원문 재검증 필요.

# 원 논문의 구현 범위
LPJ-GUESS 내부 runoff와 temperature/lithology를 P weathering에 사용한다.

# 고운사에 직접 사용할 수 있는 부분
고운사 weathering module에서도 외부 proxy보다 LPJ-GUESS가 계산한 runoff를 쓰는 것이 계보상 가능하다는 근거.

# 새로운 coupling이 필요한 부분
P weathering 식을 geomorphic R->C/Cr weathering thickness로 바꾸는 것은 새로운 coupling이다.

# 한계
정확한 서지정보가 현재 채팅에서 복구되지 않았다.
biomass가 weathering을 직접 강화하는 식은 아니다.

# 최종 판정
- 보류
- 원문 재검증 필요
