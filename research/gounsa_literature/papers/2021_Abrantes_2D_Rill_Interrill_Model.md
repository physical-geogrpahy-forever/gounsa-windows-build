# 서지정보
Abrantes, J. R. C. B., Simões, N. E., de Lima, J. L. M. P., & Montenegro, A. A. A. (2021). *Two-dimensional (2D) numerical modelling of rainfall induced overland flow, infiltration and soil erosion: comparison with laboratory rainfall-runoff simulations on a two-directional slope soil flume*. Journal of Hydrology and Hydromechanics, 69(2), 140-150. DOI: 10.2478/johh-2021-0003.

# 이 논문을 찾은 이유
genuine 2D flow에서 interrill/rill을 명시적으로 분리하면서 fixed rill mask 없이 flow condition으로 rill detachment를 활성화하는 모델이 있는지 확인하기 위해 검토했다.

# 연구 유형
- 2D numerical rainfall-runoff-erosion model
- laboratory proof-of-concept validation

# 공간 구조
- genuine 2D unsteady Saint-Venant equations
- infiltrating surface
- spatially distributed rainfall
- two-dimensional sediment transport equation

# 적용 환경
- 2 m x 2 m laboratory soil flume
- slope 1% in x direction and 10% in y direction
- forest/postfire application 없음

# 핵심 과정
- rainfall-runoff
- infiltration
- interrill erosion
- rill erosion
- sediment deposition
- 2D advective sediment transport

# 식생 입력
없음.
원문에서 vegetation/root/litter state는 사용하지 않는다.

# 핵심 식
2D sediment continuity:
```
∂(hc)/∂t + ∂(v_x h c)/∂x + ∂(v_y h c)/∂y
= e_i + e_r - d
```

여기서:
- `e_i`: interrill erosion
- `e_r`: rill erosion
- `d`: deposition

Interrill erosion is rainfall driven and includes:
- rainfall intensity
- sediment density
- settling velocity
- water-depth damping parameter `eta`

Rill erosion is activated only when dimensionless flow shear stress exceeds the critical Shields value:
```
theta > theta_c
```
and is controlled by calibration parameter `xi`.

Deposition is controlled by concentration difference and parameter `alpha`.

# 파라미터와 단위
- `eta`: rainfall/interrill damping calibration parameter
- `xi`: flow/rill erosion calibration parameter
- `alpha`: deposition calibration parameter
- `theta_c`: critical Shields parameter
- particle diameter and settling velocity

Exact formula symbols/units must be copied from the original paper when coding.

# 원 논문의 구현 범위
The model solves 2D hydraulics and sediment continuity without assigning a prior rill map.
Flow-driven rill erosion is activated hydraulically through the Shields threshold.

# 고운사에 직접 사용할 수 있는 부분
1. genuine 2D flow without fixed rill geometry
2. explicit rainfall/interrill and flow/rill separation
3. threshold-controlled concentrated-flow erosion
4. simpler erosion closure than full Hairsine-Rose

# 새로운 coupling이 필요한 부분
Any LPJ-GUESS root/litter effect on:
- `eta`
- `xi`
- `theta_c`
is a **new coupling**.

# 한계
- no quantitative vegetation state
- single/limited sediment representation compared with multiclass HR/Iber implementations
- laboratory scale
- no explicit original-soil versus deposited loose layer
- no postfire forest validation

# 최종 판정
- **2D engine comparison candidate**
- better than fixed-rill-mask approaches for dynamic concentrated flow
- less structurally suited than Hairsine-Rose for postfire loose/deposited-layer dynamics

# 참고 링크 / DOI
https://doi.org/10.2478/johh-2021-0003
