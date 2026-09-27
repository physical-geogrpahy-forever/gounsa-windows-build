# 서지정보
Cea-Gómez, L., García-Feal, O., Nord, G., Piton, G., & Legoût, C. (2024). Implementation of a GPU-enhanced multiclass soil erosion model based on the 2D shallow water equations in the software Iber. *Environmental Modelling & Software, 179*, 106098. https://doi.org/10.1016/j.envsoft.2024.106098

# 이 논문을 찾은 이유
고운사에서 최신 계열의 genuine 2D rainfall-runoff, infiltration, rainfall-driven/flow-driven erosion, multiple sediment classes, surface loose-layer grain-size evolution을 한 numerical model 안에서 처리하는 사례를 확인하기 위해 검토했다.

# 연구 유형
- physically based distributed numerical model
- GPU finite-volume solver
- laboratory to hillslope to meso-catchment validation/application

# 공간 구조
- genuine 2D shallow-water equations
- hillslope와 channel 사이 연속적인 2D flow domain
- plot/reach/catchment 규모 적용

# 핵심 수문
2D-SWE 질량식에 강우 `r`와 침투 `f`가 직접 들어간다.

```text
∂h/∂t + ∂qx/∂x + ∂qy/∂y = r - f
```

Iber hydrology framework가 rainfall 및 infiltration term을 domain 전체에서 처리한다. 논문 test case에서는 관측된 constant infiltration을 사용한 사례가 있지만, Iber 자체는 infiltration 기능을 가진다.

# 표면/토양 입도 구조
퇴적 또는 느슨한 표층 `loose sediment layer`와 원토양 `original soil matrix`를 분리한다.

- particle class `k = 1...Np`
- original soil mass fraction `g_k`: 사용자 입력
- loose-layer mass fraction `f_k`: **모델이 시간 및 공간적으로 동적 계산**
- loose-layer class mass `M_s,k`: 동적 상태

```text
M_s = Σ M_s,k
f_k = M_s,k / M_s
```

각 particle class에 대해 mass conservation을 풀기 때문에 erosion/deposition에 따라 표층 입도조성이 변한다.

# 침식과 이동
- rainfall-driven detachment
- rainfall-driven redetachment of loose layer
- flow-driven detachment
- flow-driven redetachment
- suspended-load transport
- bed-load transport
- class-specific deposition
- Exner topographic update

rainfall-driven erosion과 flow-driven erosion이 분리되어 있어 고운사의 interrill/rill 계열 구조와 개념적으로 잘 맞는다.

# armour/shield
loose sediment layer가 original soil을 보호하는 shield factor `ε`를 갖는다.

```text
ε = min(M_s / M_s,cr, 1)
```

다만 이 shield factor는 total loose-layer mass에 의해 결정되며, 고운사의 coarse-rock armour처럼 surface rock size/cover/embeddedness를 명시적으로 계산하는 구조는 아니다.

# 시간 구조
- event-scale model
- rainfall intensity는 물리 단위로 입력되고 solver 내부 timestep은 CFL 등에 따라 작게 갈 수 있음
- 2024 논문의 multiclass flume test는 47.5 mm/h의 2 h storm을 사용
- 따라서 1시간 단위 외부 forcing과의 coupling은 가능하나 solver internal timestep 자체가 1시간인 모델은 아님

# 풍화/fragmentation
- **없음**
- parent coarse fragment가 weathering/fragmentation으로 daughter size classes로 변하는 transition은 구현되지 않음

# 표면입도 -> 침투 feedback
- **구현되지 않음**
- infiltration rate/parameters는 GSD state로부터 자동 재계산되지 않는다.
- 따라서 `surface GSD / rock cover -> Ks, suction, infiltration capacity`는 별도 coupling이 필요하다.

# 적용 및 검증
논문 test cases:
- laboratory multiclass rainfall erosion: 7 size classes
- hillslope rainfall erosion field validation
- meso-catchment spatial rainfall test
- river reach bed-load test

# 고운사에 직접 사용할 수 있는 부분
- 최신 genuine 2D rainfall-runoff + multiclass erosion framework
- rainfall-driven와 flow-driven erosion의 분리
- loose surface layer의 particle-class mass conservation
- class-specific transport/deposition
- topographic feedback
- GPU 구현으로 계산비용 절감

# 새로운 coupling이 필요한 부분
- fire-spall PSD input
- coarse-fragment weathering/fragmentation
- surface coarse-fragment cover/geometry
- dynamic GSD -> infiltration/hydraulic-property feedback
- LPJ-GUESS root/litter vegetation resistance
- dry-ravel particle transport

# 한계
- soil erosion 중심이며 large rock-fragment armour model은 아님
- published multiclass validation의 coarse end가 주로 sand-gravel보다 작은 soil particles에 집중
- weathering/fragmentation 없음
- infiltration과 dynamic GSD의 직접 feedback 없음

# 최종 판정
- **고운사의 최신 2D runoff-erosion 엔진 후보 중 가장 직접적인 모델**
- RiverBedDynamics 2025보다 hillslope rainfall erosion + infiltration 구조가 직접적
- RiverBedDynamics는 coarse gravel GSD/active-layer sorting에 더 강하고, Iber+는 rainfall-runoff/interrill-flow erosion에 더 강함
- 단독으로 surface coarse-fragment weathering까지 해결하지는 못함

# 소프트웨어/데이터
Iber+와 네 test case/data는 공개되어 있다.

# 참고 링크 / DOI
https://doi.org/10.1016/j.envsoft.2024.106098
