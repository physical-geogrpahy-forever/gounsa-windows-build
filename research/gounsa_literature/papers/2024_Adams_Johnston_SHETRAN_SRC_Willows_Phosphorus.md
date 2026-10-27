# 서지정보
Adams, R., & Johnston, C. (2024). Evaluating the impacts of SRC willows on phosphorus export from a temperate grassland micro-catchment. *Nature-Based Solutions, 5*, 100118. https://doi.org/10.1016/j.nbsj.2024.100118

# 이 논문을 찾은 이유
식생 LAI/수관저류/뿌리깊이/조도를 실제 원본 SHETRAN 매개변수로 바꾸는 최근 소유역 사례

# 연구 유형
2018–2022 현장 인 유출 관측, 22ha grassland microcatchment / broader hydrology, SHETRAN baseline 대 willow 비교

# 공간 구조
모의 버드나무 구역 625m² 개별격자(25m), 더 큰 약 400ha catchment 모형 범위

# 적용 환경
북아일랜드 초지-버드나무 방목지, 인/세립유사 이동

# 핵심 과정
SHETRAN으로 시간별 유출량 재구성하고 관측 인 농도로 인부하량 계산; 식생 수문매개변수 변경 시뮬레이션

# 식생 입력
CLAI 초지 1.0 vs willow 0.2–1.2, CSTCAP 1 vs 5mm, RD 1.0 vs 1.6m, Strickler 1.0 vs 0.2, 월별 PET 변형

# 핵심 식
SHETRAN ET/수문 모듈, 인 유출량 계산은 SHETRAN 유사 모듈 자체의 보존/퇴적 계산 아님

# 파라미터와 단위
P3 634일 runoff 569→560mm, interception evaporation 163→209mm, actual ET 191→437mm (modelled willow cell)

# 원 논문의 구현 범위
2018–2022 현장 인 유출 관측, 22ha grassland microcatchment / broader hydrology, SHETRAN baseline 대 willow 비교

# 고운사에 직접 사용할 수 있는 부분
고운사 억새 및 참나무 매개변수 배치와 수관저류 민감도 비교의 직접 근거

# 필요한 새로운 coupling
직접강우 및 적하 충격/침식계수 별도 보정; 2시기 LiDAR DoD 검증

# 한계
식재에 따른 유수량 변화는 비교적 작으며 인 저감 주효과의 직접 모델 산출항과 관측 해석을 분리해야 함

# 최종 판정
고운사 수관차단 입력 설명용 최우선 최근 사례

# 참고 링크 / DOI
https://doi.org/10.1016/j.nbsj.2024.100118

# 연구코드 버전 주의
이 출판 논문은 SHETRAN의 원천 논문 또는 응용 사례지만, 각 논문이 2026-10-12 upstream SHA cf9cd540add78ad3accbaf62b4199d2032887f6b의 4.7.2.0 바이너리를 직접 사용한 사실은 증명되지 않음.
