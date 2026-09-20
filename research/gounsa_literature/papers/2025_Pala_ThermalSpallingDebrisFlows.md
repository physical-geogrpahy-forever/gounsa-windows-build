# 서지정보
Pala, C., Melis, M. T., Pioli, L., Sarro, R., Loddo, S., Cinus, S., & Brunetti, M. T. (2025). Sediment generation through thermal spalling during the 2021 Montiferru Planargia wildfire and its contribution to postfire debris flows. *Scientific Reports, 15*, 30918. https://doi.org/10.1038/s41598-025-15527-2

# 이 논문을 찾은 이유
fire spall이 실제로 산불 후 강우와 토석류에 의해 이동해 postfire sediment source가 되는지 현장자료로 확인하기 위해 검토했다.

# 연구 유형
- 현장조사
- 원격탐사
- GIS
- rockfall simulation
- postfire debris-flow 조사

# 공간 구조
- 이탈리아 Sardinia, Montiferru–Planargia
- 2021년 대형산불 피해지 약 131 km^2
- 21개 소유역에서 산불 후 토석류 활동 추적

# 적용 환경
- tephrite–phonolite 등 화산암
- 얕은 토양
- 급경사 산림과 관목지
- 지중해성 산지

# 핵심 과정
- thermal spalling
- sheetwash
- rill-interrill erosion
- rain splash
- rockfall
- debris flow
- channel damming and breach

# 식생 입력
- land cover
- burn severity
- 산림과 관목지 여부
- 동적 biomass 모델은 아님

# 핵심 식
Sentinel-2의 NBR/dNBR로 burn severity를 산정하고, 69개 암석노두에서 spall thickness와 affected area를 조사했다.

핵심 관측값:
- spall thickness: 3 mm–13 cm
- affected rock-surface fraction: 0.07–74.57%
- 중앙값 약 20.3 ± 19%
- 산불 후 2년 동안 3개 강우사건과 연관된 33개 debris flow 관찰
- 6개 debris-flow deposit에서 형태적으로 spall로 판정된 암편 비율: 1.3–36.6%

토석류 퇴적물의 spall 판정은 신선한 파단면, 기존 풍화피막을 자르는 새 파단면, 현장 노두의 thermal-spall 형상과의 유사성 등 형태학적 기준에 근거한다. 일부는 syn-flow fragmentation일 가능성을 저자들도 인정한다.

# 파라미터와 단위
- burn severity: dNBR class
- spalled area: %
- spall thickness: mm 또는 cm
- rainfall cumulative: mm
- debris-flow deposit spall fraction: %

# 원 논문의 구현 범위
산불 중 생성된 spall이 이후 강우에 의해 이동하고 토석류 퇴적물에 포함될 수 있음을 현장자료로 보여준다. 또한 spall과 기존 암편, 유기물이 하도를 막아 임시 댐을 만들고 붕괴하면서 추가적인 침식을 유발할 수 있음을 기술한다.

# 고운사에 직접 사용할 수 있는 부분
- fire spall을 실제 mobile sediment reservoir로 두는 근거
- 생성과 이동을 분리해야 한다는 근거
- spall transport가 단순 sheetwash뿐 아니라 channel blocking과 debris-flow 과정에도 연결될 수 있다는 근거

# 새로운 coupling이 필요한 부분
```text
M_spall(t+1) = M_spall(t) + P_spall - E_spall - Burial
```
같은 reservoir mass balance와, shear-stress 기반 entrainment 식은 원 논문에 없는 새로운 coupling이다.

# 한계
- spall fraction은 주로 형태학적 판정에 의존
- 일부 신선한 파단면은 이동 중 파쇄일 수 있음
- spalling 자체가 soil loss를 몇 % 변화시키는지 대조실험으로 분리하지 않음
- slope, burn severity, sediment connectivity, prefire rockfall 등 여러 요인이 함께 작용

# 최종 판정
- fire spall의 실제 이동과 postfire sediment contribution의 핵심 근거로 채택
- fire spall이 fine-soil loss를 직접 얼마나 증가 또는 감소시키는지에 대한 계수 근거로는 불충분

# 참고 링크 / DOI
https://doi.org/10.1038/s41598-025-15527-2
