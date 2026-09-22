# 서지정보
Cerdà, A. (2001). Effects of rock fragment cover on soil infiltration, interrill runoff and erosion. *European Journal of Soil Science, 52*(1), 59-68. https://doi.org/10.1046/j.1365-2389.2001.00354.x

# 이 논문을 찾은 이유
고운사 개념도에서 `armour -> infiltration 감소 -> runoff 증가`를 일반적인 방향으로 둘 수 있는지 검증하기 위해 찾았다.

# 연구 유형
- 현장 강우모의 실험

# 공간 구조
- plot
- interrill surface

# 적용 환경
- Mediterranean scrubland
- 자연 stony soil

# 핵심 과정
- infiltration
- ponding
- interrill runoff
- sediment concentration
- interrill erosion
- surface rock-fragment cover

# 식생 입력
- 직접 식생상태 없음

# 핵심 식
보편 수치모델식보다 paired field experiment가 핵심이다.
표면 석력이 존재할 때 ponding과 runoff가 지연되고 steady-state infiltration은 증가하였다.
석력을 제거한 뒤 steady-state infiltration은 44.5에서 27.5 mm h^-1로 감소했고 runoff coefficient, sediment concentration, erosion rate는 각각 약 3배, 33배, 39배 증가했다.

# 파라미터와 단위
- rainfall intensity: 55 mm h^-1
- infiltration: mm h^-1
- rock-fragment surface cover

# 원 논문의 구현 범위
자연토양에서 표면에 놓인 rock fragments가 sealing 및 runoff/erosion을 억제하고 infiltration을 높일 수 있음을 실험적으로 보여준다.

# 고운사에 직접 사용할 수 있는 부분
- `armour -> infiltration 감소`를 고정 부호로 두면 안 된다는 강한 근거
- surface-resting fragment는 infiltration 증가와 erosion 감소를 동시에 만들 수 있음
- armour hydrology와 armour shielding을 별도 항으로 모델링할 근거

# 새로운 coupling이 필요한 부분
고운사 fragment size/embeddedness/cover에서 infiltration modifier를 계산하는 단계는 **새로운 coupling**이다.

# 한계
Mediterranean scrubland의 interrill 실험이며 급경사 산림 rill 조건과 직접 동일하지 않다.

# 최종 판정
- 핵심 채택 근거
- armour-hydrology 방향성 수정의 핵심 문헌

# 참고 링크 / DOI
https://doi.org/10.1046/j.1365-2389.2001.00354.x
