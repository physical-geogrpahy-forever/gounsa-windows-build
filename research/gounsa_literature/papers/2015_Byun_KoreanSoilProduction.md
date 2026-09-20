# 서지정보
Byun, J., Heimsath, A. M., Seong, Y. B., & Lee, S. Y. (2015). Erosion of a high-altitude, low-relief area on the Korean Peninsula: Implications for its development processes and evolution. *Earth Surface Processes and Landforms, 40*(13), 1730–1745. https://doi.org/10.1002/esp.3749

# 이 논문을 찾은 이유
고운사와 같은 한국 산지에서 우주선기원 핵종을 이용해 자연 토양생산률과 토양두께 의존성을 정량화한 국내 경험자료가 있는지 확인하기 위해 검토했다.

# 연구 유형
- 현장측정
- 우주선기원 핵종
- 토양생산률 추정

# 공간 구조
- 대관령 고위평탄면과 사면
- 수치모델보다 현장 기반 soil production function 추정

# 적용 환경
- 한반도 고위 산지
- 화강암질 풍화대
- 동결작용이 가능한 고산환경

# 핵심 과정
- soil production
- catchment denudation
- bedrock incision
- 토양두께 의존 풍화와 생산

# 식생 입력
- 직접적인 biomass 입력은 없음

# 핵심 식
현재 채팅에서 복구된 토양생산 함수:
```text
P_s = (54 ± 1) exp[-(0.0068 ± 0.0026) h]
```
- P_s: m Myr^-1
- h: cm

따라서 P0는 약 54 m Myr^-1, 즉 0.054 mm yr^-1 수준이고 characteristic decay length는 약 147 cm이다.

정확한 식 표기와 오차는 실제 구현 전 원문 재검증 권장.

# 파라미터와 단위
- P_s: m Myr^-1
- h: cm
- catchment denudation: m Myr^-1

# 원 논문의 구현 범위
한국 산지에서 토양생산률이 토양두께에 따라 어떻게 달라지는지를 경험적으로 제약한다.

# 고운사에 직접 사용할 수 있는 부분
고운사 자연풍화와 토양생산의 크기차수를 판단하는 국내 analogue. 장기 자연생산률이 대략 10^-2에서 10^-1 mm yr^-1 규모임을 판단하는 데 도움을 준다.

# 새로운 coupling이 필요한 부분
이 함수가 측정한 경계를 고운사의 R->C 또는 C->AB 중 어느 경계에 대응시킬지는 자동으로 결정되지 않는다. 특정 경계에 배정하는 것은 새로운 coupling이며 operational definition 확인이 필요하다.

# 한계
- 고운사 현장계수가 아님
- 암질과 기후가 다름
- CRN 기반 soil production boundary를 pedogenic C->AB에 곧바로 대응시키면 안 됨

# 최종 판정
- 국내 정량 analogue로 채택
- 직접 매개변수 이식은 금지
- 고운사 풍화율의 사전범위와 시간척도 판단에 사용

# 참고 링크 / DOI
https://doi.org/10.1002/esp.3749
