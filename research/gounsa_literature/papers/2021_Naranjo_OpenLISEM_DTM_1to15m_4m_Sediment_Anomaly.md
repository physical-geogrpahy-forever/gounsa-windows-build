# 서지정보
Naranjo, S., Rodrigues Jr., F. A., Cadisch, G., Lopez-Ridaura, S., Fuentes Ponce, M., & Marohn, C. (2021). Effects of spatial resolution of terrain models on modelled discharge and soil loss in Oaxaca, Mexico. *Hydrology and Earth System Sciences*, 25, 5561–5588. https://doi.org/10.5194/hess-25-5561-2021

# 이 논문을 찾은 이유
OpenLISEM 기존 고운사 수치불안정 문제가 학술 문헌에서도 나타나는지, 해상도/물리 정확도 이질성 대조.

# 연구 유형
멕시코 Oaxaca 219.6ha 유역 39회 강우사상 관측과 OpenLISEM v4.96 지표유출/퇴적 보정 및 DTM 해상도 민감도 시험.

# 공간 구조
0.6m 원DTM을 1m, 2m, 4m, 8m, 15m로 재격자; 모델 계산은 1m 이상, **10cm 이하 실제 모델 실행이 아님**.

# 적용 환경
산림, 휴경, 옥수수, 침식 나지 등 토지피복, 여러 실험포/사면.

# 핵심 과정
강우사상 유출 및 침식/유사배출량; 세립 토사 유출수지 결과에서 4m 특이 극단값.

# 식생 입력
Sentinel-2에서 피복률과 LAI 추정. 시나리오별 입력, 입경/점착력, 유사 이동.

# 핵심 식
LISEM 침투, 피복별 차단, 강우/유수 박리 및 유사수송. 논문 §3.4.1 총유사배출 1m=191.9Mg, 2m=128.4Mg, **4m=440.9Mg(4개 이상치 강우사상 지배)**, 8m=38.1Mg, 15m=39.7Mg로 수문출력과 달리 유사수송의 불연속 해상도 반응을 직접 기록.

# 파라미터와 단위
220ha, 1m~15m, 1min 시간간격, OpenLISEM 4.96. DOI 위 참조.

# 원 논문의 구현 범위
4m anomalous sediment mass outputs 를 논문 저자들이 explicitly unexpected numerical combination이라고 지적, **10cm에서 검증 없음**.

# 고운사에 직접 사용할 수 있는 부분
LISEM 코드 자체의 수치강건성에 보수적 판단, 유사수지·시간/공간격자 안정성 필수.

# 새로운 coupling이 필요한 부분
10cm 미만의 고운사 토양기반 억새/참나무 LAI와 2D 전방위 유동, spatial DoD 검증.

# 한계
서로 다른 원본 버전(4.96과 7.5.2)에서의 현상으로 단일 원인 검증 아님. 동일 프로젝트 과거 7.5.2의 Δt 비수렴이 이 4m 이상치와 같은 버그라고 단정 불가.

# 최종 판정
보조근거: **LISEM의 5cm/1cm 선행연구가 존재하더라도 수치안정성 및 격자 재현성 검증을 생략 불가.**

# 참고 링크 / DOI
https://doi.org/10.5194/hess-25-5561-2021
