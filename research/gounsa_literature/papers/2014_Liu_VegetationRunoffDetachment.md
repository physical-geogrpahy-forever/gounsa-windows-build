# 서지정보
Liu, Y., Wang, T.-W., Cai, C.-F., & Cheng, D.-B. (2014). Effects of vegetation on runoff generation, sediment yield and soil shear strength on road-side slopes under a simulation rainfall test in the Three Gorges Reservoir Area, China. *Science of the Total Environment, 485-486*, 93-102.

# 이 논문을 찾은 이유
초본과 초본+관목 혼합군집에서 AGB와 root weight density가 침식에 미치는 효과를 검토했다.

# 연구 유형
- 현장/강우실험

# 공간 구조
- plot

# 적용 환경
- 도로사면

# 핵심 과정
- runoff
- soil detachment
- shear strength

# 식생 입력
- AGB
- root weight density
- RLD

# 핵심 식
예시 경험식 `SDR=-64.620 ln(RWD)+80.309`가 이 채팅 정리에 기록되었으나 연구지 특이식이다.

# 파라미터와 단위
RWD, RLD, AGB.

# 원 논문의 구현 범위
혼합식생의 침식저감 효과를 실험적으로 비교.

# 고운사에 직접 사용할 수 있는 부분
혼합군집에서 지상부와 지하부 양을 따로 볼 근거.

# 새로운 coupling이 필요한 부분
경험식을 고운사 모델에 직접 이식하는 것은 금지. 사용 시 새로운 coupling과 재보정 필요.

# 한계
수치모델 아님.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.scitotenv.2014.03.053
