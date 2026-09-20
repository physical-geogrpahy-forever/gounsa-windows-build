# 서지정보
Roering, J. J., & Gerber, M. (2005). Fire and the evolution of steep, soil-mantled landscapes. 정확한 권호 및 페이지는 원문 재검증 필요.

# 이 논문을 찾은 이유
산불 후 dry ravel 및 비선형 사면수송계수가 어떻게 달라지는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 및 현장자료 기반 지형과정 해석

# 공간 구조
- hillslope transport law
- 장기 landscape evolution 해석

# 적용 환경
- 급경사 soil-mantled landscape
- 산불 후

# 핵심 과정
- nonlinear hillslope transport
- dry ravel
- postfire sediment flux

# 식생 입력
- 식생량 자체를 직접 계산하지 않음
- fire disturbance에 따른 transport coefficient와 critical slope 변화로 처리

# 핵심 식
비선형 hillslope flux law의 transport coefficient K와 critical slope Sc가 화재 이후 달라지는 방식으로 postfire transport enhancement를 표현한다.

# 파라미터와 단위
- K: hillslope transport coefficient
- Sc: critical slope
정확한 수치 및 단위는 원문 재검증 필요.

# 원 논문의 구현 범위
산불 전후 사면물질 이동률 차이를 비선형 transport law의 파라미터 변화로 나타낸다.

# 고운사에 직접 사용할 수 있는 부분
- 산불 후 dry-ravel 강화가 background diffusion과 다를 수 있다는 근거
- 별도 postfire hillslope transport state를 둘 수 있다는 근거

# 새로운 coupling이 필요한 부분
LPJ-GUESS biomass나 root state에서 K 또는 Sc를 계산하는 연결은 원 논문에 없다.

# 한계
식생량 기반 모델이 아니므로 고운사 식생 coupling의 최종식으로 직접 채택하지 않는다.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
원문 재검증 필요.
