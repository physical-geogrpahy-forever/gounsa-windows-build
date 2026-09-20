# 서지정보
Yoo, K., & Mudd, S. M. (2008). Toward process-based modeling of geochemical soil formation across diverse landforms: A new mathematical framework. *Geoderma, 146*(1–2), 248–260. https://doi.org/10.1016/j.geoderma.2008.05.029

# 이 논문을 찾은 이유
고운사에서 기반암, 풍화된 C/Cr, 이동 가능한 A+B 토양층을 하나의 토심으로 합치지 않고 기능적으로 분리할 수 있는 이론적 선례를 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- 방법론
- 토양지형 결합모델

# 공간 구조
- 사면의 토양 질량수지와 지구화학 질량수지를 결합
- eroding, depositional, level landform을 포괄

# 적용 환경
- 다양한 사면과 토양경관을 대상으로 한 일반 이론틀

# 핵심 과정
- PDZ 생산
- weathering front propagation
- mineral dissolution
- colloidal translocation
- colluvial transport

# 식생 입력
- 이 논문의 핵심은 식생 biomass가 아니라 토양층 구조와 지구화학 과정
- 고운사의 LPJ-GUESS coupling은 원 논문 밖의 작업

# 핵심 식
토양을 다음 두 기능층으로 구분한다.
- PDZ: physically disturbed zone
- CAZ: physically undisturbed but chemically altered zone

개념적 흐름:
```text
R -> CAZ -> PDZ
```

# 파라미터와 단위
세부 반응식과 계수는 원문 구현 전 재검증 필요.

# 원 논문의 구현 범위
물리적으로 교란되어 이동 가능한 상부층과 그 아래 화학적으로 변질되었지만 상대적으로 비이동성인 층을 분리해 토양형성과 사면수송을 통합한다.

# 고운사에 직접 사용할 수 있는 부분
고운사에서 R, C/Cr, AB를 분리하는 구조적 근거. 특히 풍화전선 이동과 이동성 토양생산을 서로 다른 경계과정으로 다뤄야 한다는 근거가 된다.

# 새로운 coupling이 필요한 부분
고운사의 pedogenic A/B/C를 PDZ/CAZ와 일대일 대응시키는 것은 원 논문에 없다. 따라서
```text
R -> C/Cr -> AB
```
구조는 Yoo와 Mudd의 기능적 분리를 참고한 새로운 coupling이다.

# 한계
- C horizon = CAZ, A+B = PDZ라고 단정할 수 없음
- 식생뿌리, fire spall, coarse fragments를 고운사 방식으로 직접 추적하지 않음

# 최종 판정
- 구조적 근거로 채택
- 고운사 층 구분의 개념틀로 사용
- 정확한 층 대응은 새로운 coupling으로 명시

# 참고 링크 / DOI
https://doi.org/10.1016/j.geoderma.2008.05.029
