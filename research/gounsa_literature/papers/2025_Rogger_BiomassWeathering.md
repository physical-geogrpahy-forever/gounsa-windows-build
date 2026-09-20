# 서지정보
Rogger, J., Korasidis, V. A., Bowen, G. J., Shields, C. A., Gerya, T. V., & Pellissier, L. (2025). Loss of vegetation functions during the Paleocene-Eocene Thermal Maximum. *Nature Communications, 16*, 11369.

# 이 논문을 찾은 이유
동적 식생모델 biomass를 weathering enhancement factor에 직접 쓰는 최근 선례로 검토했다.

# 연구 유형
- 수치모델

# 공간 구조
- 전지구 deep-time

# 적용 환경
- 지질시대

# 핵심 과정
- silicate weathering

# 식생 입력
- dynamic vegetation total biomass

# 핵심 식
개념적으로 `omega_silw = omega_abiotic * f_BM`; normalized biomass에 따라 weathering enhancement가 증가한다.

# 파라미터와 단위
현대 열대림 수준까지 최대 약 6배 enhancement를 허용하는 설정이 이 채팅 정리에 기록됨.

# 원 논문의 구현 범위
biomass-dependent chemical-weathering benchmark.

# 고운사에 직접 사용할 수 있는 부분
biomass-weathering 연결의 현대적 비교대상.

# 새로운 coupling이 필요한 부분
고운사 절대계수로 쓰려면 완전한 새 보정/coupling 필요.

# 한계
total normalized biomass이며 PFT/root organ 분리 없음, deep-time 목적.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1038/s41467-025-66390-8
