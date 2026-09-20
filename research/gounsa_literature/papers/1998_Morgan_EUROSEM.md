# 서지정보
Morgan, R. P. C., Quinton, J. N., Smith, R. E., Govers, G., Poesen, J. W. A., Auerswald, K., Chisci, G., Torri, D., & Styczen, M. E. (1998). *The European Soil Erosion Model (EUROSEM): a dynamic approach for predicting sediment transport from fields and small catchments*. Earth Surface Processes and Landforms, 23(6), 527-544. DOI: 10.1002/(SICI)1096-9837(199806)23:6<527::AID-ESP868>3.0.CO;2-5.

# 이 논문을 찾은 이유
root-density-dependent cohesion을 실제 erosion model에 넣은 De Baets 2008 수정판의 본체인 EUROSEM이 rill/interrill, vegetation, sediment transport를 어떻게 구성하는지 확인하기 위해 검토했다.

# 연구 유형
- dynamic distributed event-based numerical erosion model

# 공간 구조
- linked slope-plane and channel elements
- finite-difference routing
- small catchment
- genuine 2D SWE는 아님

# 적용 환경
- fields
- small catchments
- smooth slopes, rilled surfaces, furrows

# 핵심 과정
- explicit interrill flow/erosion
- explicit rill flow/erosion
- sediment transport/deposition
- rainfall interception and energy
- infiltration
- rock-fragment effects
- dynamic rill geometry
- channel erosion

# 식생 입력
Base EUROSEM represents vegetation mainly through:
- plant cover
- interception
- rainfall energy
- flow velocity/roughness
- soil cohesion inputs can be modified in later root-explicit research versions

# 핵심 식
EUROSEM dynamically solves water/sediment mass balance and computes rill/interrill sediment transport.

Flow detachment depends on soil resistance/cohesion and transport-capacity-related efficiency.

Later De Baets 2008 work uses this detachment equation to back-calculate cohesion and make it root-density-dependent.

# 파라미터와 단위
- soil cohesion
- transport capacity
- rill geometry/density
- vegetation cover
- rock-fragment cover
- rainfall energy
- hydraulic parameters

Exact equation definitions remain in the original documentation/user guide.

# 원 논문의 구현 범위
EUROSEM can simulate smooth, rilled and furrowed slope surfaces with dynamic rill/interrill routing and sediment transport.

# 고운사에 직접 사용할 수 있는 부분
- explicit rill/interrill process architecture
- soil cohesion as an erosion-resistance state
- dynamic rill geometry precedent
- a mature base for later root-density-dependent cohesion work

# 새로운 coupling이 필요한 부분
Using EUROSEM root-cohesion relations inside a genuine 2D solver is **new coupling**.

# 한계
- not genuine 2D
- base vegetation effects are substantially cover-based
- event model
- catchment represented by linked planes/channels

# 최종 판정
- **핵심 계보 근거**
- final 2D engine: 탈락
- root-cohesion submodel base: 채택

# 참고 링크 / DOI
https://doi.org/10.1002/(SICI)1096-9837(199806)23:6%3C527::AID-ESP868%3E3.0.CO;2-5
