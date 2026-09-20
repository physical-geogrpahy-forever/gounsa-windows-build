# 서지정보
Lamb, M. P., Scheingross, J. S., Amidon, W. H., Swanson, E., & Limaye, A. (2011). *A model for fire-induced sediment yield by dry ravel in steep landscapes*. Journal of Geophysical Research: Earth Surface, 116, F03006. DOI: 10.1029/2010JF001878.

# 이 논문을 찾은 이유
산불 후 급경사면에서 vegetation sediment-storage capacity가 붕괴하면서 loose sediment가 방출되는 dry-ravel pulse를 정량적으로 모의할 수 있는 모델을 찾기 위해 검토했다.

# 연구 유형
- process-based mass-balance numerical model
- 현장관측 검증
- postfire sediment-storage model

# 공간 구조
- contributing hillslope area 기반 1D mass balance
- steep hillslope storage model
- angle of repose보다 가파른 사면 포함

# 적용 환경
- San Gabriel Mountains, California
- chaparral
- 산불 후 급경사 산지

# 핵심 과정
- dry ravel
- vegetation sediment storage
- fire-induced storage-capacity loss
- postfire sediment pulse
- soil production
- vegetation recovery and storage recovery

# 식생 입력
- vegetation density c [plants m^-2]
- sediment-storage capacity per plant V_ci [m3 plant^-1]
- vegetation recovery timescale t_veg
- trapping efficiency psi
- low branches/litter의 물리적 저장효과

# 핵심 식
Hillslope sediment mass balance:
```
dh/dt = -(1/w) dQ/dx + (rho_r/rho_s) E
```

Vegetation storage capacity:
```
V_c = V_ci c A_b
```

# 파라미터와 단위
- V_c: sediment volume
- V_ci: sediment volume per plant [m3 plant^-1]
- c: plant density [plants m^-2]
- A_b: contributing hillslope area [m2]
- E: soil production rate [length time^-1]
- psi: trapping efficiency [-]
- t_veg: vegetation recovery timescale [time]

# 원 논문의 구현 범위
산불로 vegetation storage capacity가 급감하면서 기존에 식생에 저장되던 loose sediment가 channel 방향으로 빠르게 방출되는 현상을 모의한다.

# 고운사에 직접 사용할 수 있는 부분
- 산불 직후 loose coarse/fine sediment pulse의 storage-release 모듈
- vegetation recovery와 sediment-storage recovery의 timescale 분리
- fire spall, loose gravel, detached mineral soil을 별도 loose-sediment pool로 두는 구조
- spall 등으로 이미 공급된 loose fragments의 redistribution을 설명하는 보조과정

# 새로운 coupling이 필요한 부분
LPJ-GUESS biomass/PFT -> vegetation sediment-storage capacity 또는 thermal spall production -> loose-sediment pool 연결은 **새로운 coupling**이다.

# 한계
- thermal spall production 자체는 계산하지 않음
- 유수침식식이 아님
- chaparral parameter를 고운사 산림에 그대로 사용할 수 없음
- vegetation input은 biomass 자체보다 plant density/storage capacity 중심

# 최종 판정
- 채택
- 역할: postfire loose sediment/dry-ravel/spall redistribution 구조

# 참고 링크 / DOI
https://doi.org/10.1029/2010JF001878
