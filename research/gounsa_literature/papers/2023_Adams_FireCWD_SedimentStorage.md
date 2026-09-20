# 서지정보
Adams, K. V., Dixon, J. L., Wilcox, A. C., & McWethy, D. B. (2023). Fire-produced coarse woody debris and its role in sediment storage on hillslopes. *Earth Surface Processes and Landforms, 48*(9), 1665-1678. https://doi.org/10.1002/esp.5573

# 이 논문을 찾은 이유
산불 뒤 죽은 목본을 litter로만 처리하지 않고 CWD가 사면 퇴적물 저장과 연결성을 바꾸는지 확인하기 위해 검토했다.

# 연구 유형
- 현장 관측
- 산불 후 사면지형 연구

# 공간 구조
- hillslope
- 국지적 log-sediment storage

# 적용 환경
- 산불 후 산림사면

# 핵심 과정
- coarse woody debris
- sediment trapping
- hillslope connectivity
- tree throw 감소

# 식생 입력
- fire-produced downed wood
- log geometry와 배치

# 핵심 식
이 채팅에서 직접 복구된 핵심은 CWD 뒤 저장토사량과 장기 soil-production equivalent 비교이다. 단일 보편 수송식은 확인하지 않았다.

# 파라미터와 단위
log 크기, 방향, 저장퇴적물 체적. 세부 단위와 식은 원문 재검증 필요.

# 원 논문의 구현 범위
산불 후 생성된 쓰러진 목재가 downslope sediment transport를 차단하고 저장공간을 만든다.

# 고운사에 직접 사용할 수 있는 부분
dead WoodC를 SurfaceLitC로만 보내지 않고 별도 CWD pool로 두어 sediment storage와 connectivity를 조절해야 한다는 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS tree mortality/wood pool을 CWD 개수, 길이, 직경, 방향으로 변환하는 것은 **새로운 coupling**이다.

# 한계
수치 LEM이 아니라 현장 제약이다. 연구지의 약 300년치 soil production 상당 저장량을 고운사에 직접 이식하면 안 된다.

# 최종 판정
- 보조근거
- post-fire CWD 모듈은 채택 후보

# 참고 링크 / DOI
https://doi.org/10.1002/esp.5573
