# 서지정보
Caponi, F., Vetsch, D. F., & Siviglia, A. (2020). *A model study of the combined effect of above and below ground plant traits on the ecomorphodynamics of gravel bars*. Scientific Reports, 10, 17062. DOI: 10.1038/s41598-020-74106-9.

# 이 논문을 찾은 이유
genuine 2D morphodynamics에서 aboveground와 belowground biomass를 동적으로 계산하고, root biomass가 sediment resistance를 직접 바꾸며, 지형변화가 다시 vegetation mortality에 피드백하는 published model이 있는지 확인하기 위해 검토했다.

# 연구 유형
- 2D ecomorphodynamic numerical model
- dynamic vegetation-morphology feedback model

# 공간 구조
- genuine 2D shallow-water equations
- triangular unstructured grid
- Exner bed-evolution equation
- BASEMENT hydromorphodynamic solver

# 적용 환경
- Alpine Rhine
- gravel bars
- fluvial mobile-bed environment
- rainfall-driven hillslope erosion 환경은 아님

# 핵심 과정
- 2D hydrodynamics
- bedload transport
- Exner morphology
- vegetation growth
- above/belowground biomass allocation
- root-depth dynamics
- vegetation-induced roughness
- root-enhanced sediment-motion threshold
- scour uprooting
- burial mortality

# 식생 입력
Vegetation is represented by dynamic total biomass `B`, split into:
- aboveground biomass `B_c`
- belowground biomass `B_r`
- vertical root-density distribution `b_r(z)`
- rooting depth
- canopy height

즉 cover fraction 하나가 아니라 **동적 biomass state**가 모델 내부 상태변수다.

# 핵심 식
Biomass growth:
```
dB/dt = sigma_B B (1 - B/B_max)
```

Belowground biomass directly raises the critical Shields threshold:
```
theta_cr =
theta_cr,g
+ (theta_cr,v - theta_cr,g) * B_r(t)/B_r,max
```

Vegetation also reduces bed shear acting on sediment through canopy-related roughness.

Uprooting is tied to belowground biomass excavated by scour:
```
B_r,cr = integral_0^{zeta_upr} b_r(z) dz
```

# 파라미터와 단위
- `B, B_c, B_r`: dimensionless biomass density in this model
- `theta_cr,g`: bare-bed critical Shields parameter
- `theta_cr,v`: fully vegetated-bed critical Shields parameter
- rooting-depth and allocation parameters
- model example uses `theta_cr,v=0.2`

# 원 논문의 구현 범위
2D flow + bedload + bed elevation + vegetation growth and mortality를 양방향으로 coupled한다.

# 고운사에 직접 사용할 수 있는 부분
매우 중요한 구조적 선례:
```
dynamic belowground biomass
 -> erosion/transport threshold
 -> 2D morphodynamics
 -> scour/deposition
 -> vegetation uprooting/burial
```

즉 “2D morphodynamics + quantitative belowground biomass + two-way feedback” 자체는 이미 published precedent가 있다.

# 새로운 coupling이 필요한 부분
고운사 rainfall hillslope erosion에 사용하려면:
- LPJ-GUESS FineRootC -> Caponi의 dimensionless `B_r`
- gravel-bed Shields threshold -> cohesive soil detachment resistance
- rainfall/interrill detachment 추가
가 모두 새로운 coupling이다.

# 한계
- gravel-bar/fluvial bedload model
- cohesive hillslope soil detachment가 아님
- rainfall-driven/interrill erosion 없음
- root effect가 bedload incipient-motion threshold에 작용하며 WEPP-type soil-detachment `K_r`와 동일하지 않음
- riparian water-table-driven root dynamics가 고운사 산림에 직접 적용되지 않음

# 최종 판정
- **핵심 구조적 선례로 채택**
- 고운사 유수침식 본체를 직접 대체하지는 못함
- “Iber+ + LPJ-GUESS” 새로운 coupling의 novelty를 평가할 때 반드시 인용해야 할 가까운 선행모델

# 참고 링크 / DOI
https://doi.org/10.1038/s41598-020-74106-9
