# 서지정보
Geyman, E. C., Paige, D. A., & Lamb, M. P. (2025). The contribution of rock strength to soil production. *Nature, 647*, 921-927.

# 이 논문을 찾은 이유
soil production에서 vegetation 효과를 넣더라도 bedrock strength를 고정 background로 둘 수 있는지 검토하기 위해 찾았다.

# 연구 유형
- 현장/과정해석

# 공간 구조
- hillslope soil-production system

# 적용 환경
- 암반-토양 사면

# 핵심 과정
- soil production
- rock weakening
- weathering state

# 식생 입력
- 직접 식생변수 없음

# 핵심 식
이 채팅에서 특정 원식은 복구되지 않았으며 핵심은 soil depth만이 아니라 rock strength 변화가 soil production rate를 강하게 제어한다는 점이다.

# 파라미터와 단위
rock strength, soil production rate. 세부값 원문 재검증 필요.

# 원 논문의 구현 범위
soil production의 rock-strength control을 검토.

# 고운사에 직접 사용할 수 있는 부분
풍화/토양생산 potential을 고정값이 아니라 lithology, fracture state, rock strength와 함께 제약해야 한다는 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root effects와 rock-strength state를 함께 soil-production law에 넣으면 새로운 coupling.

# 한계
식생-지형 결합모델이 아님.

# 최종 판정
- 핵심 제약근거

# 참고 링크 / DOI
이 채팅에서 DOI 미복구
