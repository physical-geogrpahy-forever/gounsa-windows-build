# 서지정보
Cea, L., García-Feal, O., Nord, G., Piton, G., & Legoût, C. (2024). Implementation of a GPU-enhanced multiclass soil erosion model based on the 2D shallow water equations in the software Iber. *Environmental Modelling & Software, 179*, 106098. https://doi.org/10.1016/j.envsoft.2024.106098

# 이 논문을 찾은 이유
고운사의 사건단위 2D runoff-rill/interrill erosion에서 particle-size-resolved detachment, redeposition, loose-layer shielding과 mass conservation을 기존 공개모델 그대로 사용할 수 있는지 확인하고, SSSPAM/mARM 장기 armour/profile state와 비자의적으로 연결 가능한지 검토하기 위해 찾았다.

# 연구 유형
- fully distributed process-based numerical model
- 2D shallow-water hydrodynamics
- multiclass soil erosion and sediment transport
- GPU implementation

# 공간 구조
- genuine 2D finite-volume mesh
- plot/hillslope/river/catchment scale
- event scale

# 적용 환경
- laboratory rainfall experiment
- field hillslope
- meso-scale catchment
- river reach

# 핵심 과정
- rainfall infiltration and 2D overland flow
- rainfall-driven detachment
- rainfall-driven redetachment
- flow-driven detachment
- flow-driven redetachment
- suspended load
- bed load
- deposition
- loose sediment layer
- shielding of original soil
- multiclass mass conservation
- Exner topographic update

# 식생 입력
- dynamic quantitative root/litter state는 본 모델의 핵심이 아님
- vegetation-root coupling은 별도 검토 필요

# 핵심 상태변수
원토양 matrix:
- particle-class mass fractions g_k

loose sediment layer:
- class mass per unit area M_s,k [kg m^-2]
- total M_s = sum M_s,k
- class fraction f_k = M_s,k / M_s

water column:
- class suspended concentration C_k

topography:
- bed elevation z_b

# soil vertical structure
```
runoff water + suspended sediment
-------------------------------
loose sediment layer
  M_s,k, f_k
-------------------------------
original soil matrix
  g_k
-------------------------------
non-erodible rock
```

original-soil grading g_k is user-defined input.
loose-layer grading f_k evolves dynamically.

# loose-layer thickness
```
l_d = M_s / (rho_s phi)
```

class-equivalent thickness:
```
l_d,k = M_s,k / (rho_s phi)
```

# suspended-load mass equation
각 class k에 대해:
```
∂(h C_k)/∂t
+ ∂(q_x C_k)/∂x
+ ∂(q_y C_k)/∂y
=
D_rdd,k
+ D_rdrd,k
+ D_fdd,k
+ D_fdrd,k
+ D_dep,k
```

모든 source term은 kg m^-2 s^-1.

구분:
- D_rdd,k: rainfall detachment from original soil
- D_fdd,k: flow detachment from original soil
- D_rdrd,k: rainfall redetachment from loose layer
- D_fdrd,k: flow redetachment from loose layer
- D_dep,k: deposition from water column to loose layer

# loose-layer mass conservation
```
∂M_s,k/∂t
=
-(D_rdrd,k + D_fdrd,k + D_dep,k)
-rho_s(∂q_bx,k/∂x + ∂q_by,k/∂y)
```

즉 loose sediment layer의 class mass는 시간에 따라 직접 보존/갱신된다.

# shielding
```
epsilon = min(M_s / M_s,cr, 1)
```

M_s,cr은 complete shielding에 필요한 critical loose-sediment mass [kg m^-2].

중요:
- published model parameter이지만 site-independent constant가 아님.
- 고운사에서는 erosion-output calibration으로 임의 적합하지 않는다.
- 현장 armour mass/thickness 또는 독립 실험으로 제약해야 한다.

# topography
각 class의 detachment, redetachment, deposition, bed-load divergence를 모두 합산하여 Exner-type mass conservation으로 z_b를 갱신한다.
갱신된 topography는 같은 timestep의 2D hydrodynamics와 coupling된다.

# 고운사에 직접 사용할 수 있는 부분
1. genuine 2D runoff
2. rainfall/flow erosion 분리
3. original soil vs loose sediment 분리
4. particle-class-specific detachment/transport/deposition
5. loose-layer dynamic PSD
6. loose-layer shielding
7. mass-conserving topographic update
8. open executable/test cases

# SSSPAM/mARM과의 중요한 interface
장기 profile depletion에 넘길 때 **total detachment를 그대로 넘기면 안 된다**.

persistent original-soil loss:
```
E_orig,k
=
A_cell ∫(D_rdd,k + D_fdd,k) dt
```

loose-layer recycling:
```
E_redet,k
=
A_cell ∫(D_rdrd,k + D_fdrd,k) dt
```

E_redet,k는 이미 표면에 존재한 loose material의 재이동이므로 deep soil profile을 다시 제거하는 질량이 아니다.

event-end persistent surface state:
```
M_s,k(end)
```
를 그대로 유지해야 한다.

# 자의성 방지
- g_k: 현장 sieve/particle-size measurement
- M_s,k(initial): 현장 surface loose/armour inventory
- rho_s: 측정
- phi: 측정
- M_s,cr: 독립 surface-armour mass/depth 측정
- erodibility/critical shear parameters: independent soil/flume measurement or directly applicable published calibration only
- soil-loss 결과에 맞춘 자유 calibration 금지

# 한계
- original soil matrix g_k는 깊이에 따라 자동으로 바뀌는 multilayer profile이 아님
- long-term physical weathering 없음
- fire-spall production 없음
- dynamic vegetation/root biomass coupling 없음
- M_s,cr 및 erodibility parameters에 독립 자료 필요

# 최종 판정
- **event-scale 2D multiclass erosion engine의 우선후보**
- OpenLISEM보다 particle-class handoff가 명확함
- long-term embedded PSD/weathering은 SSSPAM/mARM과 역할분담

# 참고 링크 / DOI
https://doi.org/10.1016/j.envsoft.2024.106098
