# 서지정보
Cea, L., García-Feal, O., Nord, G., Piton, G., & Legoût, C. (2024). *Implementation of a GPU-enhanced multiclass soil erosion model based on the 2D shallow water equations in the software Iber*. Environmental Modelling & Software, 179, 106098. DOI: 10.1016/j.envsoft.2024.106098.

# 이 논문을 찾은 이유
Wu/PSEM_2D보다 현대적인 genuine 2D finite-volume erosion engine에서 rainfall-driven과 flow-driven erosion을 분리할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- GPU/HPC finite-volume model

# 공간 구조
- genuine 2D
- Iber+ 2D shallow-water equations
- fully distributed finite-volume solver
- plot에서 meso-scale catchment까지

# 적용 환경
- laboratory
- Mediterranean hillslope
- meso-scale catchment
- river reach
- 산림 산불 전용 모델은 아님

# 핵심 과정
- rainfall-driven detachment/redetachment
- flow-driven detachment/redetachment
- suspended load
- bed load
- deposition
- loose sediment layer
- 2D Exner topography update
- multiclass sediment

# 식생 입력
- 동적 root biomass/RLD 직접입력 없음
- vegetation은 core erosion-resistance state로 구현되지 않음

# 핵심 식
Suspended-load source:
```
∂(h C_k)/∂t + ∂(q_x C_k)/∂x + ∂(q_y C_k)/∂y
= D_rdd,k + D_rdrd,k + D_fdd,k + D_fdrd,k + D_dep,k
```

Rainfall-driven detachment:
```
D_rdd,k = α_d,k r (1-ε) f_d g_k
```

Flow-driven detachment:
```
D_fdd,k = K_d,k max(τ-τ_s,0)(1-ε)g_k
```

# 파라미터와 단위
- `α_d,k`: rainfall erodibility coefficient
- `K_d,k`: flow-driven detachability, kg s^-1 N^-1
- `τ_s`: critical bed shear stress
- `ε`: loose-layer shielding factor
- `g_k`: particle-class fraction

중요: `K_d`의 차원은 WEPP rill erodibility `Kr`와 직접 비교 가능한 Foster 계열 구조다.

# 원 논문의 구현 범위
2D SWE + rainfall/runoff erosion + sediment transport + morphodynamics.

# 고운사에 직접 사용할 수 있는 부분
- 현재까지 확인된 가장 강한 현대 2D erosion-engine 후보 중 하나
- rainfall-driven과 flow-driven을 독립 source term으로 둠
- flow-driven detachment가 WEPP/Foster 계열과 수학적으로 잘 맞음

# 새로운 coupling이 필요한 부분
WEPP/Mao/PROMET/LPJ-GUESS의 root-dependent erodibility를 `K_d` 또는 `α_d`에 연결하면 **새로운 coupling**이다.

# 한계
- root biomass/RLD 직접입력 없음
- 산불 산림용 식생회복 모듈 없음

# 최종 판정
**채택 후보: 2D 유수침식 엔진.**

# 참고 링크 / DOI
10.1016/j.envsoft.2024.106098
