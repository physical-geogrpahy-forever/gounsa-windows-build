# 서지정보
Poesen, J., Ingelmo-Sanchez, F., & Mucher, H. (1990). The hydrological response of soil surfaces to rainfall as affected by cover and position of rock fragments in the top layer. *Earth Surface Processes and Landforms, 15*(7), 653-671. https://doi.org/10.1002/esp.3290150707

# 이 논문을 찾은 이유
고운사에서 같은 rock-fragment cover라도 표면에 얹혀 있는 armour와 토양에 매립된 석력이 infiltration/runoff에 서로 반대 효과를 낼 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- laboratory rainfall experiment
- simple hydrological model

# 공간 구조
- soil surface/top layer
- plot scale

# 적용 환경
- sealing-prone topsoil with rock fragments

# 핵심 과정
- infiltration
- runoff generation
- surface sealing
- rock-flow reinfiltration
- fragment-position effect

# 식생 입력
- 없음

# 핵심 식
같은 cover에서도 fragment position에 따라 효과 방향이 달라진다.
- fragments resting on surface: water intake 증가, runoff concentration 지연, runoff volume 감소
- fragments well embedded in top layer: infiltration 감소, runoff 증가
저자들은 bare surface, embedded-fragment area, resting-fragment-covered area의 면적비를 이용한 simple runoff model을 제시했다.

# 파라미터와 단위
- rock-fragment cover fraction
- resting versus embedded fraction
- infiltration/water intake
- runoff coefficient

# 원 논문의 구현 범위
rock-fragment hydrology의 부호를 cover만이 아니라 vertical position/embeddedness가 결정하는 것을 실험과 모델로 보여준다.

# 고운사에 직접 사용할 수 있는 부분
- armour state에 `surface-resting fraction`과 `embedded fraction`을 분리할 강한 근거
- fire-spall 직후 표면에 놓인 암편과 시간이 지나 토양에 매립/정착된 암편의 hydrological effect를 다르게 줄 근거

# 새로운 coupling이 필요한 부분
고운사 동적 sediment deposition/soil production에 따라 resting fragment가 embedded fragment로 전환되는 규칙은 **새로운 coupling**이다.

# 한계
산불사면이 아니며 실험토양의 sealing 특성이 고운사와 다를 수 있다.

# 최종 판정
- 핵심 채택
- armour hydrology의 position-dependent 구조 근거

# 참고 링크 / DOI
https://doi.org/10.1002/esp.3290150707
