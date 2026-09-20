# 서지정보
Pelletier, J. D., et al. (2013). Coevolution of nonlinear trends in vegetation, soils, and topography with elevation and slope aspect. *Journal of Geophysical Research: Earth Surface, 118*, 741–758. https://doi.org/10.1002/jgrf.20046

# 이 논문을 찾은 이유
고운사에서 기반암 풍화, 토양생산, 식생, 사면수송을 장기 지형발달 안에서 연결할 수 있는지 검토했다.

# 연구 유형
- 수치모델
- 현장자료 기반 매개변수화

# 공간 구조
- distributed landscape evolution framework

# 적용 환경
- 미국 남서부 산지
- 화강암 기반 산지

# 핵심 과정
- soil production/weathering
- colluvial hillslope transport
- vegetation-topography coevolution

# 식생 입력
- EEMT의 biological energy
- AGB

# 핵심 식
```text
P = P0 exp[-h cos(theta) / h0]
P0 = a exp(b EEMT)
```
현재 채팅에서 확인한 연구지 계수는 a = 0.037 m kyr^-1, b = 0.03 m^2 yr MJ^-1, h0 약 0.5 m이다. 이 값은 고운사에 직접 이식하지 않는다.

사면수송은 토양두께를 포함한 비선형 수송식이며 k_d를 EEMT와 AGB에 연결한다.

# 파라미터와 단위
- P, P0: 길이/시간
- h, h0: 길이
- EEMT: 에너지 관련 변수
- AGB: 지상부 생체량

# 원 논문의 구현 범위
식생에 의해 조절되는 에너지와 생체량을 풍화와 사면수송에 연결해 토양과 지형의 공진화를 모의한다.

# 고운사에 직접 사용할 수 있는 부분
R에서 풍화층으로의 장기 풍화전선 이동 구조와 EEMT 사용.

# 새로운 coupling이 필요한 부분
고운사의 R, C/Cr, AB 구조에서는 다음 확장이 필요하다.
```text
P_R_to_C = P0(EEMT) exp[-(H_AB + H_C) cos(theta) / h0_R]
```
이 식은 Pelletier 원식을 고운사 두 층 구조로 확장한 새로운 coupling이다. LPJ-GUESS NPP와 ET를 이용한 EEMT 계산도 별도 coupling이다.

# 한계
- 원 논문의 soil/regolith 정의와 pedogenic A/B/C는 동일하지 않음
- 연구지 P0 계수는 지역종속적
- AGB 기반 사면수송과 다른 식생효과를 동시에 쓰면 중복계산 가능

# 최종 판정
- R에서 C/Cr로의 장기 풍화 구조에 채택 후보
- 사면수송 AGB 항은 보조근거

# 참고 링크 / DOI
https://doi.org/10.1002/jgrf.20046
