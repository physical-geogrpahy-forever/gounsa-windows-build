# 서지정보
Welivitiya, W. D. D. P., Willgoose, G. R., & Hancock, G. R. (2019). A coupled soilscape-landform evolution model: model formulation and initial results. *Earth Surface Dynamics, 7*, 591-607. https://doi.org/10.5194/esurf-7-591-2019

# 이 논문을 찾은 이유
mARM3D의 armour/profile evolution에 erosion, deposition, soil-depth와 DEM evolution까지 기존 모델로 연결할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- coupled soilscape-landform evolution model
- SSSPAM

# 공간 구조
- regular square raster DEM
- D8 flow routing
- multilayer soil profile per pixel
- particle-size state vector per layer

# 적용 환경
- stony mine-spoil grading을 사용한 초기 model experiments

# 핵심 과정
- fluvial erosion
- sediment transport/deposition
- size-selective entrainment
- dynamic surface armour
- physical weathering
- vertical soil-profile evolution
- soil-depth evolution
- DEM elevation change

# 식생 입력
- 없음

# 핵심 식/구조
actual erosion mass `E_a`를 계산한 후, surface grading vector와 erosion transition matrix `A`를 사용해 size-class별 eroded mass vector `G_e`를 계산한다.

```
psi_out = psi_in + G_e
```

erosion depth:
```
Delta h_E = E_a / (R_x R_y rho_s)
```

fine-rich material이 선택적으로 제거되면 subsurface layer에서 같은 질량을 surface armour layer로 resupply해 mass conservation을 유지한다.
이 resupply가 profile 아래까지 전달된다.

# 파라미터와 단위
- grid resolution R_x, R_y [m]
- bulk density rho_s [kg m^-3]
- particle-size grading vector
- armour layer depth
- profile layer thickness
- erosion/weathering transition matrices
- erosion/transport parameters

# 원 논문의 구현 범위
surface PSD, sediment-load PSD, soil profile, soil depth와 DEM을 동시 갱신한다.
surface armour layer를 명시적으로 갖는다.

# 고운사에 직접 사용할 수 있는 부분
- 매립 석력의 깊이별 PSD
- fine loss -> coarse armour
- weathering -> class transition
- erosion/deposition mass balance -> soil-depth/DEM update
- `E_a`를 size-class transition으로 바꾸는 published interface

# 매우 중요한 한계
- 흐름방향이 D8이므로 고운사에서 요구하는 genuine 2D hydrodynamics는 아님.
- 자체 fluvial erosion/transport relation은 site parameterisation이 필요.
- 따라서 전체 runoff-erosion engine으로 단독 채택하지 않음.

# 새로운 coupling 가능성
SSSPAM의 state-space armour/profile updater는 `E_a`라는 총 erosion mass를 받아 size-class-specific removal로 바꾸는 구조다.
따라서 modern 2D event model이 계산한 erosion/deposition mass를 SSSPAM state updater에 전달하는 방식은 **새로운 software coupling**이지만 새로운 armour 경험식을 만드는 것과는 다르다.

# 최종 판정
- **장기 dynamic armour + soil-profile + soil-depth/DEM updater의 최우선 후보**
- 2D event flow engine으로는 탈락

# 참고 링크 / DOI
https://doi.org/10.5194/esurf-7-591-2019
