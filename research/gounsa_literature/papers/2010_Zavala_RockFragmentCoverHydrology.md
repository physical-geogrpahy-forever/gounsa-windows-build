# 서지정보
Zavala, L. M., Jordán, A., Bellinfante, N., & Gil, J. (2010). Relationships between rock fragment cover and soil hydrological response in a Mediterranean environment. *Soil Science and Plant Nutrition, 56*(1), 95–104. https://doi.org/10.1111/j.1747-0765.2009.00429.x

# 이 논문을 찾은 이유
고운사 표면 석력과 fire spall 잔류가 runoff와 interrill soil loss를 감소시키는 armour 효과를 가질 수 있는지 조작실험 근거를 찾기 위해 검토했다.

# 연구 유형
- 강우모의 현장실험
- 석력 제거 조작실험

# 공간 구조
- plot scale
- 분포형 수치모델 아님

# 적용 환경
- 스페인 남서부 지중해성 비경작 나지
- 자연상태에 가까운 bare soil

# 핵심 과정
- runoff
- ponding
- infiltration
- interrill erosion
- surface rock-fragment protection

# 식생 입력
- 비경작 나지
- 식생 biomass를 입력으로 사용하지 않음

# 핵심 식
석력피복률이 서로 다른 조건에서 36회의 강우모의실험을 실시했다.
- 강우강도: 26.8 mm h^-1
- 지속시간: 60 min
- 피복률 구간: <50%, 50–60%, >60%

높은 석력피복률의 시험구에서 석력을 제거한 뒤 동일 실험을 반복했다.

현재 채팅에서 확인한 제거 전후 값:
- rock fragment cover: 68.02% -> 3.04%
- runoff coefficient: 4.83% -> 11.07%
- steady-state runoff rate: 2.60 -> 4.58 mm h^-1
- soil loss도 유의하게 증가

논문은 soil loss rate와 rock fragment cover 사이를 지수함수로 기술하지만, 고운사 적용용 exact coefficient는 이 세션에서 복구하지 못했다.

# 파라미터와 단위
- rock fragment cover: %
- rainfall intensity: mm h^-1
- runoff rate: mm h^-1
- soil loss: 원문 단위와 회귀계수는 구현 전 재검증 필요

# 원 논문의 구현 범위
표면 석력이 ponding과 runoff를 지연하고 infiltration을 증가시키며 soil loss를 낮추는 효과를 직접 실험한다.

# 고운사에 직접 사용할 수 있는 부분
surface coarse fraction 또는 안정된 fire spall이 세립질 토양침식을 줄일 가능성의 가장 직접적인 비교근거 중 하나.

# 새로운 coupling이 필요한 부분
```text
CF_surface -> K_fine,eff
```
또는 rock-fragment cover에서 fine-soil erodibility를 계산하는 수치모델식은 고운사에서 새로운 coupling이다.

# 한계
- fire spall 자체를 실험한 것이 아님
- bare soil의 지중해 환경이며 산불 후 산림사면과 다름
- 석력의 입경, 매몰비, 공간배열에 따라 효과가 달라질 수 있음
- 회귀식을 고운사에 무보정 적용하면 안 됨

# 최종 판정
- armour 효과의 핵심 보조근거로 채택
- 고운사 계수는 별도 현장실험 또는 보정 필요

# 참고 링크 / DOI
https://doi.org/10.1111/j.1747-0765.2009.00429.x
