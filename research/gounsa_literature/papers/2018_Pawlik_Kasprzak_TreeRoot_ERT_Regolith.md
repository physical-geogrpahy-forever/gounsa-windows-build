# 서지정보
Pawlik, L., & Kasprzak, M. (2018). Regolith properties under trees and the biomechanical effects caused by tree root systems as recognized by electrical resistivity tomography (ERT). Geomorphology, 300, 1-12.
DOI: 10.1016/j.geomorph.2017.10.002

# 이 논문을 찾은 이유
고운사 100년 postfire model에서 살아있는 식생이 사라진 뒤 root channel, 수분경로, regolith architecture가 즉시 초기화되는지 여부를 검토하기 위해 찾았다.

# 연구 유형
- 산지 현장 geophysics
- electrical resistivity tomography, ERT
- 수치 weathering model 아님

# 공간 구조
- Polish Outer Western Carpathians의 3개 산지 연구지
- 각 site에서 hillslope-scale long profile과 tree microsite short profiles를 결합
- 총 21 ERT profiles
- long profile: 최대 189 m
- short profile: 19.5 m

# 적용 환경
- 산림 산지
- dominant geological substratum: Carpathian flysch
- living tree, decaying stump, pit-and-mound microsite 비교

# 핵심 과정
- root channels
- root-zone moisture migration
- soil/regolith electrical-property heterogeneity
- persistent biogeomorphic legacy after tree mortality or cutting
- root-regolith architecture

# 식생 입력
- living mature tree
- decaying stump with roots left in situ
- uprooted-tree microsite
- biomass나 RLD 시계열 입력은 없음

# 핵심 식
weathering 또는 permeability의 직접 process equation은 없다.
ERT inversion을 통해 resistivity structure를 비교한다.

# 파라미터와 단위
- long ERT profile length: 최대 189 m
- short ERT profile length: 19.5 m
- total profiles: 21
- resistivity: ERT-derived electrical resistivity, 보통 ohm m 계열의 물리량이나 본 archive에서는 논문 결과를 hydrologic/weathering coefficient로 직접 환산하지 않음

# 원 논문의 구현 범위
- tree roots가 root channels와 moisture migration을 통해 soil/regolith property를 공간적으로 복잡하게 만들 수 있음을 geophysical signal로 확인
- decaying stump microsite의 영향은 living tree보다 약했지만, 나무가 쓰러지거나 잘린 뒤 수십 년이 지나도 ERT에서 식별 가능했다고 보고
- 즉 vegetation disturbance 후 subsurface structure가 즉시 사라지지 않음

# 고운사에 직접 사용할 수 있는 부분
1. postfire에서 `vegetation biomass -> 0`이라고 root-created hydrologic architecture를 동시에 0으로 만들면 안 된다.
2. initial subsurface state에 inherited root channels / biopore connectivity를 둘 근거가 된다.
3. preferential/vertical/lateral connectivity sensitivity는 current vegetation과 vegetation legacy를 구분할 필요가 있다.

# 새로운 coupling이 필요한 부분
후보 상태변수:
- `C_rootlegacy` 또는 동등한 root-channel/biopore legacy state
- current live roots와 별도로 초기값을 보존
하지만 논문은 decay law나 transferable time constant를 주지 않으므로 production baseline에 임의의 지수감쇠식을 넣지 않는다.

# 한계
- ERT는 root channels와 moisture state를 직접 permeability로 측정하는 방법이 아니다.
- flysch setting이며 고운사 사암과 암석구조가 동일하지 않다.
- uprooting 관련 부분은 현재 고운사 production scope에서 제외한다.
- chemical weathering flux나 soil production rate를 직접 제공하지 않는다.

# 최종 판정
- 채택
- 역할: post-disturbance subsurface hydrologic legacy와 root-regolith architecture persistence의 구조적 근거
- decay coefficient는 미정

# 참고 링크 / DOI
- https://doi.org/10.1016/j.geomorph.2017.10.002