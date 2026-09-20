# 서지정보
Wu et al. (2020). *Two-dimensional rainfall-runoff and soil erosion model on an irregularly rilled hillslope*. Journal of Hydrology, 580, 124346. DOI: 10.1016/j.jhydrol.2019.124346.

# 이 논문을 찾은 이유
고운사 유수침식 엔진이 genuine 2D이면서 interrill/rill을 구분해야 한다는 조건을 만족하는 후보를 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- 2D rainfall-runoff + soil erosion

# 공간 구조
- genuine 2D diffusion-wave overland flow
- raster/2D hillslope
- rill/interrill mask를 공간적으로 구분

# 적용 환경
- irregularly rilled hillslope
- 산림·산불 산지 자체의 검증은 아님

# 핵심 과정
- interrill detachment
- rill detachment
- sediment transport
- 2D runoff routing

# 식생 입력
- root biomass/RLD 직접입력 없음
- 식생모듈 없음

# 핵심 식
Sediment continuity:
```
∂(hc)/∂t + ∂(qx c)/∂x + ∂(qy c)/∂y
= μ Di + (1-μ) Dr
```
`μ=1`: interrill, `μ=0`: rill.

Interrill:
```
Di = Ki p R If Fnozzle
```

Rill:
```
Dr = Kr(τ - τc)(1 - G/Tc)
```

Transport capacity:
```
Tc = kt τ^(3/2)
```

# 파라미터와 단위
- `Ki`: interrill erodibility
- `Kr`: rill erodibility
- `τc`: critical shear stress
- 세부 단위는 원문 표 재확인 시 추가

# 원 논문의 구현 범위
2D runoff와 sediment routing, 고정된 rill/interrill 공간구분.

# 고운사에 직접 사용할 수 있는 부분
- 2D surface-flow/erosion skeleton
- interrill과 rill을 서로 다른 식으로 계산하는 구조
- WEPP 계열 `Ki/Kr/τc`와 수학적으로 가까운 구조

# 새로운 coupling이 필요한 부분
LPJ-GUESS의 FineRootC/LitterC 또는 WEPP 계열 biomass-dependent `Ki/Kr`를 연결하면 **새로운 coupling**이다. 원 Wu 모델에 동적 root biomass 입력은 없다.

# 한계
- rill mask가 미리 주어짐
- rill network가 자발적으로 branching/merging하지 않음
- vegetation/root module 없음
- 산림·산불 산지 검증 자체는 아님

# 최종 판정
**채택 후보: 2D erosion routing skeleton.**
식생-침식 coupling의 단독 해법은 아님.
