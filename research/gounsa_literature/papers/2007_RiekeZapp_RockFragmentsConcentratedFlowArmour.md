# 서지정보
Rieke-Zapp, D., Poesen, J., & Nearing, M. A. (2007). Effects of rock fragments incorporated in the soil matrix on concentrated flow hydraulics and erosion. *Earth Surface Processes and Landforms, 32*, 1063-1076. https://doi.org/10.1002/esp.1469

# 이 논문을 찾은 이유
고운사에서 석력이 존재하는 토양에서 미세물질이 먼저 빠져나가며 armour가 시간에 따라 발달하고, 그 armour가 rill incision을 억제하는 동적 과정을 직접 구현할 근거를 찾기 위해 검토했다.

# 연구 유형
- flume experiment
- concentrated-flow process study

# 공간 구조
- 1D flume
- rill/concentrated flow

# 적용 환경
- stony soil
- 경사 7% 및 14%

# 핵심 과정
- rill incision
- concentrated-flow hydraulics
- selective removal of fines
- rock-fragment exhumation
- dynamic surface armouring
- headcutting

# 식생 입력
- 없음

# 핵심 식
단일 armour 방정식보다 시간진화의 process classification이 핵심이다.

1. Continuous rill incision: rock fragment가 거의 없고 rill incision 지속
2. Transitional surface: fines가 제거되며 fragment가 노출되어 armour 증가, sediment yield 감소
3. Surface armour: 안정적 fragment cover가 형성되어 sediment yield가 매우 작음

# 파라미터와 단위
- rock-fragment content: 0-40 vol%
- slope: 7%, 14%
- discharge: 5.7, 11.4 L min^-1
- surface rock-fragment cover
- sediment yield
- Darcy-Weisbach roughness

# 원 논문의 구현 범위
concentrated flow가 fine material을 선택적으로 제거하고 남은 rock fragments가 surface armour를 형성하며 flow energy를 소산하고 rill incision을 억제하는 과정을 실험적으로 추적한다.

# 고운사에 직접 사용할 수 있는 부분
- armour fraction을 고정 초기조건이 아닌 **동적 상태변수**로 둘 직접 근거
- `fine-soil removal -> fragment exhumation -> armour increase -> rill detachment 감소`
- armour가 이미 발달한 곳에서는 runoff가 존재해도 sediment supply/detachment가 제한될 수 있다는 근거
- rill incision과 armour stabilization의 경쟁 구조

# 새로운 coupling이 필요한 부분
fire-spall supply와 기존 soil-matrix fragments를 하나의 size-class armour state로 결합하는 것은 **새로운 coupling**이다.

# 한계
산불 실험이 아니며 실제 2D 산지 지형은 아니다.

# 최종 판정
- 핵심 채택
- 고운사 dynamic armouring의 가장 직접적인 process 근거 중 하나

# 참고 링크 / DOI
https://doi.org/10.1002/esp.1469
