# 서지정보
Song, C., Fu, S., Liu, B., & Zhao, H. (2026). Slope-dependent erosion control by rock fragments: experiments and model improvements. *Geoderma, 468*, 117756. https://doi.org/10.1016/j.geoderma.2026.117756

# 이 논문을 찾은 이유
고운사처럼 급경사인 조건에서 rock-fragment armour의 erosion-control 효과를 완만한 실험사면 계수로 그대로 적용할 수 있는지 확인하기 위해 찾았다.

# 연구 유형
- simulated-rainfall experiment
- empirical model improvement

# 공간 구조
- hillslope plots

# 적용 환경
- slope gradients 8.7-70%
- rock-fragment cover 0-80%

# 핵심 과정
- runoff
- sediment concentration
- soil loss
- slope-dependent armour efficiency

# 식생 입력
- 없음

# 핵심 식
기본 cover relation:
`C = a exp(-b Rc)`

여기서 erosion-reduction coefficient `b`가 slope에 따라 감소한다.
실험에서 b는 slope 8.7%의 0.0102에서 slope 70%의 0.0032까지 감소하였다.
급경사 및 낮은 cover에서는 runoff/sediment-concentration 감소효과가 약해지거나 역전될 수 있었다.

# 파라미터와 단위
- slope: 8.7-70%
- fragment cover Rc: 0-80%
- b: slope-dependent fitted coefficient

# 원 논문의 구현 범위
rock-fragment cover의 erosion-control efficiency를 slope-dependent하게 정량화한다.

# 고운사에 직접 사용할 수 있는 부분
- 고운사 armour shielding coefficient를 slope-independent constant로 두지 않을 근거
- steep slope에서는 hydraulic forcing이 armour protection을 부분적으로 압도할 수 있음을 표현할 근거

# 새로운 coupling이 필요한 부분
fire-spall size distribution, dynamic exhumation 및 고운사 rill engine에 이 slope-dependent cover relation을 넣는 것은 **새로운 coupling**이다.

# 한계
산불/산림 특이 모델이 아니며 empirical cover relation이다.

# 최종 판정
- 핵심 보조근거
- steep-slope armour correction 후보

# 참고 링크 / DOI
https://doi.org/10.1016/j.geoderma.2026.117756
