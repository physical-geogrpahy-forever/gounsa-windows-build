# 서지정보
Barnes, M. S., Bathurst, J. C., Lewis, E., & Quinn, P. F. (2023). Leaky dams augment afforestation to mitigate catchment scale flooding. *Hydrological Processes, 37*(6), e14920. https://doi.org/10.1002/hyp.14920

# 이 논문을 찾은 이유
수관 및 산림 변화가 소규모 폭우 상대 유량보호효과에 미치는 영향을 보여주는 최신 SHETRAN 시나리오

# 연구 유형
영국 북부 상류 및 Irthing 유역에서 산림피복/소규모 하천댐 설치의 홍수 수문 시나리오

# 공간 구조
산림 상류유역과 더 넓은 하천 유역 비교

# 적용 환경
영국 초지, 산림 및 하천

# 핵심 과정
100% grassland vs 100% forest, leaky dam 등으로 첨두유량과 연간 유출량을 모의 비교

# 식생 입력
토지피복 grassland→forest 변화

# 핵심 식
주로 SHETRAN 유출모듈 사용; 침식-퇴적을 직접 수치검증한 연구가 아님

# 파라미터와 단위
Irthing의 20개 유량첨두 평균 17.7% 감소, 가장 큰 첨두 4.4% 감소, 장기 유출 33.5% 감소(100% woodland vs grassland)

# 원 논문의 구현 범위
영국 북부 상류 및 Irthing 유역에서 산림피복/소규모 하천댐 설치의 홍수 수문 시나리오

# 고운사에 직접 사용할 수 있는 부분
강우 규모가 커질수록 산림의 유출 저감 상대효과가 줄어들 수 있는 SHETRAN 선례

# 필요한 새로운 coupling
강우적하 토양박리 및 공간퇴적은 현재 고운사 실험에서 추가로 비교

# 한계
원논문 수문 중심. 침식 저감 효과도 같이 약해진다고 추론 금지

# 최종 판정
식생 효과가 강우사상 규모에 의존하는 수문 근거

# 참고 링크 / DOI
https://doi.org/10.1002/hyp.14920

# 연구코드 버전 주의
이 출판 논문은 SHETRAN의 원천 논문 또는 응용 사례지만, 각 논문이 2026-10-12 upstream SHA cf9cd540add78ad3accbaf62b4199d2032887f6b의 4.7.2.0 바이너리를 직접 사용한 사실은 증명되지 않음.
