# 서지정보
Yetemen, O., Istanbulluoglu, E., Flores-Cervantes, J. H., Vivoni, E. R., & Bras, R. L. (2015). Ecohydrologic role of solar radiation on landscape evolution. *Water Resources Research, 51*, 1127-1157. https://doi.org/10.1002/2014WR016169

# 이 논문을 찾은 이유
실제 biomass continuity를 가진 CHILD가 biomass를 hydraulic roughness와 유수침식에 어떻게 연결하는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- coupled ecohydrogeomorphic LEM

# 공간 구조
- CHILD
- TIN/Voronoi spatial domain
- storm-interstorm time stepping

# 적용 환경
- 반건조 landscape
- grass PFT 중심

# 핵심 과정
- energy balance
- soil water balance
- biomass dynamics
- overland flow
- fluvial detachment and transport
- nonlinear hillslope diffusion
- erosion-induced vegetation loss

# 식생 입력
- live biomass
- dead biomass
- LAI
- total vegetation cover
- vegetation Manning roughness

# 핵심 식
개념적 연결:
`biomass -> LAI -> vegetation cover -> Manning roughness -> effective shear stress -> detachment/transport`

total cover:
`Vt = 1 - exp(-0.75 * LAIt)`

effective shear:
`tau_eff = tau_b * (ns / (ns + nv))^(3/2)`

# 파라미터와 단위
- biomass: g dry matter m-2
- LAI: 무차원
- Manning n: roughness coefficient
- shear stress: Pa
- hillslope diffusivity: L2 T-1 계열

# 원 논문의 구현 범위
energy, water, biomass, elevation continuity를 CHILD 안에서 함께 계산한다. 유수침식이 vegetation을 다시 제거하는 양방향 feedback도 포함한다.

# 고운사에 직접 사용할 수 있는 부분
- 지상부 vegetation structure가 hydraulic resistance를 통해 유수침식에 작용하는 구조
- biomass를 지역별 최대값으로 임의 정규화하지 않고 물리적 중간변수로 변환하는 접근

# 새로운 coupling이 필요한 부분
LPJ-GUESS의 PFT별 LeafC와 실제 geomorphically effective understory/ground structure를 roughness로 바꾸는 식은 원 논문에 없다. 고운사에서는 `새로운 coupling`이다.

# 한계
- 원 모델은 single grass PFT 중심
- 산림 canopy LAI 또는 canopy FVC를 지표 ground cover와 동일시할 수 없음
- 따라서 이 논문의 cover 변환식을 고운사 사면확산 modifier로 곧바로 쓰지 않음

# 최종 판정
- 채택
- 단, 지상부 수리저항 구조만 채택하며 LPJ-GUESS canopy FVC 직접사용은 금지

# 참고 링크 / DOI
https://doi.org/10.1002/2014WR016169
