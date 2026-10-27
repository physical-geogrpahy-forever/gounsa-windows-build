# 서지정보
Bathurst, J. C., Moretti, G., El-Hames, A., Moaven-Hashemi, A., & Burton, A. (2005). Scenario modelling of basin-scale, shallow landslide sediment yield, Valsassina, Italian Southern Alps. *Natural Hazards and Earth System Sciences, 5*, 189–202. https://doi.org/10.5194/nhess-5-189-2005

# 이 논문을 찾은 이유
급경사지 산림피복 변화와 산사태 기원 토사 공급을 SHETRAN으로 다룬 연구 확인.

# 연구 유형
산사태-유사량 결합 SHETRAN의 과거 공간분포 검증 및 산림/기후 시나리오. 출판사 원문 초록 확인.

# 공간 구조
이탈리아 남부 알프스 Valsassina 180 km².

# 적용 환경
고산 및 산지 사면, 50년 산사태 관측 기록.

# 핵심 과정
산사태의 공간분포 재현은 양호했지만 발생빈도 과대추정 가능, 전체 토사유출량에 대한 얕은 산사태의 상대 기여가 크지 않을 가능성. 전면 산림 및 따뜻하고 건조한 미래 조건은 산사태 빈도와 유사량을 완만하게 줄임.

# 식생 입력
산림피복과 얕은 산사태 위험을 위한 뿌리 응집력.

# 핵심 식
기본 유수박리식에 더해 산사태 발생 및 퇴적 공급을 계산하는 별도 모듈 적용. 사면 sheet flow 침식과 혼동 금지.

# 파라미터와 단위
산사태 위험의 soil cohesion, root cohesion [Pa], slope [도] 등 입력을 본문에서 설정.

# 원 논문의 구현 범위
산사태-유사량 결합 SHETRAN의 과거 공간분포 검증 및 산림/기후 시나리오. 출판사 원문 초록 확인.

# 고운사에 직접 사용할 수 있는 부분
고운사 사면 위험에서 유수침식과 산사태를 별개 프로세스로 구분해야 한다는 사례.

# 필요한 새로운 coupling
본 단일 강우 침식 목적에는 원본 산사태 모듈을 무조건 켜지 않는다. 필요 시 별도 검증.

# 한계
대유역 장기 산사태 재현. 4m 격자 강우사상 중 퇴적량 검증과 다름.

# 최종 판정
산지 적용 및 별도 대규모 사면붕괴 연구의 보조근거.

# 참고 링크 / DOI
https://doi.org/10.5194/nhess-5-189-2005
