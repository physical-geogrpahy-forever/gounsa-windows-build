# 서지정보
Jomaa, S., Barry, D. A., Heng, B. C. P., Brovelli, A., Sander, G. C., & Parlange, J.-Y. (2012). Influence of rock fragment coverage on soil erosion and hydrological response: Laboratory flume experiments and modeling. *Water Resources Research, 48*, W05535. https://doi.org/10.1029/2011WR011255

# 이 논문을 찾은 이유
rock-fragment cover를 hydrology와 size-selective erosion에 동시에 넣은 실제 수치모델 선례를 찾기 위해 검토했다.

# 연구 유형
- flume experiment
- process-based erosion modeling

# 공간 구조
- laboratory hillslope/flume
- Hairsine-Rose 기반 1D erosion model

# 적용 환경
- rock-fragment-covered soil surface

# 핵심 과정
- rainfall detachment
- overland flow
- infiltration
- sediment transport
- size-selective erosion
- shielding

# 식생 입력
- 없음

# 핵심 식
Hairsine-Rose model을 rock-fragment-covered exposed area에 맞게 수정했다.
rock fragments는 raindrop detachment를 차단하고 overland flow를 늦춰 transport capacity를 줄였으며 size class별 erosion을 선택적으로 변화시켰다.

# 파라미터와 단위
- rock-fragment cover: 20%, 40%
- rainfall intensity: 28, 74 mm h^-1
- sediment size classes
- exposed area fraction

# 원 논문의 구현 범위
표면 석력의 shielding과 hydrological response를 하나의 erosion modeling framework에서 다룬다.

# 고운사에 직접 사용할 수 있는 부분
- fragment cover를 exposed fine-soil fraction으로 바꿔 detachment area를 제한하는 구조
- armour와 sediment size class를 함께 추적할 수 있는 published modeling precedent
- surface fragments가 sealing을 억제하여 infiltration을 높일 수 있다는 근거

# 새로운 coupling이 필요한 부분
fire-spall-generated size classes와 고운사 2D rill/interrill engine에 Hairsine-Rose식 shielding을 이식하는 것은 **새로운 coupling**이다.

# 한계
완전한 산지 2D 모델이 아니며 fragment geometry가 단순화됨.

# 최종 판정
- 핵심 보조 모델근거

# 참고 링크 / DOI
https://doi.org/10.1029/2011WR011255
