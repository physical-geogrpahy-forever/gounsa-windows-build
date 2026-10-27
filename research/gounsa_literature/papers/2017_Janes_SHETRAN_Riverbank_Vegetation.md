# 서지정보
Janes, V., Holman, I., Birkinshaw, S., O'Donnell, G., & Kilsby, C. (2017). Improving bank erosion modelling at catchment scale by incorporating temporal and spatial variability. *Earth Surface Processes and Landforms, 43*(1), 124–133. https://doi.org/10.1002/esp.4149

# 이 논문을 찾은 이유
식생 효과 및 공간구조를 반영하는 SHETRAN의 유사계산 적용 범위와 원본/개선모듈의 경계를 확인.

# 연구 유형
SHETRAN 기존 하안침식 모형을 개선하여 식생 및 하천 곡률과 시간변화를 반영하는 **연구용 수정 모델**. 출판사 전문 초록 확인.

# 공간 구조
잉글랜드 북서부 Eden 유역 하도.

# 적용 환경
온대 하천과 하안식생.

# 핵심 과정
곡률과 하안식생, 홍수 연속 발생을 반영한 모델을 하안침식 추정/검증. 모의 연간 하안침식량 617–4063t, 추정 관측 범위 211–4426t/년. 홍수시점 집적으로 잠재적 하안침식량 61% 증가.

# 식생 입력
하안식생의 계절적 소실과 회복.

# 핵심 식
기존 SHETRAN bank erosion 식을 연구자들이 수정했으므로 원본 4.7.2 기능이라고 보고 금지.

# 파라미터와 단위
연간 토사량 t/년, 유량과 하안 유사저항 계수.

# 원 논문의 구현 범위
SHETRAN 기존 하안침식 모형을 개선하여 식생 및 하천 곡률과 시간변화를 반영하는 **연구용 수정 모델**. 출판사 전문 초록 확인.

# 고운사에 직접 사용할 수 있는 부분
모델 확장 연구 시 '원본 SHETRAN'과 '새로운 coupling/개선형'을 구분하는 선례.

# 필요한 새로운 coupling
고운사 산림사면 직접침식과 하안침식은 별개. 본 목적에서는 새 bank erosion 개발 불필요.

# 한계
하안침식 및 공간적 하천 연결 중심, 소규모 사면 수관차단 ON/OFF와 직접 동일하지 않음.

# 최종 판정
보조방법론 근거. 원본 모델 기능의 직접 검증으로 사용 불가.

# 참고 링크 / DOI
https://doi.org/10.1002/esp.4149
