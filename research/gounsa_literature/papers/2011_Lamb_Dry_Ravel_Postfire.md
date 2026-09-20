# 서지정보
Lamb, M. P., Scheingross, J. S., Amidon, W. H., Swanson, E., & Limaye, A. (2011). *A model for fire-induced sediment yield by dry ravel in steep landscapes*. Journal of Geophysical Research: Earth Surface, 116, F03006. DOI: 10.1029/2010JF001878.

# 이 논문을 찾은 이유
산불 후 steep hillslope에서 vegetation dam이 저장하던 loose sediment가 방출되는 dry-ravel pulse를 정량적으로 모의할 수 있는 모델을 찾기 위해 검토했다.

# 연구 유형
- process-based mass-balance model
- postfire dry ravel

# 공간 구조
- 1D hillslope mass balance
- steep slopes, including slopes steeper than angle of repose

# 적용 환경
- San Gabriel Mountains, California
- postfire steep mountain landscapes

# 핵심 과정
- vegetation sediment storage
- fire-induced storage-capacity loss
- dry-ravel sediment pulse
- vegetation recovery
- soil production and refill

# 식생 입력
- vegetation density c [plants per area]
- sediment-storage capacity per plant V_ci
- vegetation regrowth timescale t_veg
- trapping efficiency ψ
- low branches/litter can contribute physically to storage

# 핵심 식
Hillslope sediment mass balance:
```
dh/dt = -(1/w) dQ/dx + (ρ_r/ρ_s) E
```

Vegetation storage capacity:
```
V_c = V_ci c A_b
```
형태의 storage-capacity framework를 사용한다.

# 파라미터와 단위
- V_ci: sediment volume stored per plant [m3/plant]
- c: vegetation density [plants/m2]
- V_c/A_b: area-normalized vegetation storage capacity [m]
- E: soil production rate [length/time]
- ψ: trapping efficiency [-]
- t_veg: vegetation recovery timescale [time]

# 원 논문의 구현 범위
fire로 vegetation storage capacity가 급감하면서 기존 loose sediment가 빠르게 channel로 방출되는 현상을 모의한다.

# 고운사에 직접 사용할 수 있는 부분
- 산불 직후 loose coarse/fine sediment pulse의 storage-release 모듈
- vegetation recovery와 sediment storage recovery의 timescale 분리
- spall 등으로 공급된 loose fragments가 식생에 저장되거나 방출되는 보조과정 설계의 근거

# 새로운 coupling이 필요한 부분
thermal spall production이나 LPJ-GUESS biomass를 V_ci 또는 c로 변환하면 **새로운 coupling** 또는 추가 문헌식이 필요하다.

# 한계
- thermal spall production 자체는 계산하지 않음
- 유수침식 모델이 아님
- vegetation input은 biomass가 아니라 plant density/storage capacity 중심

# 최종 판정
**채택: postfire dry-ravel/storage 모듈의 핵심근거.**

# 참고 링크 / DOI
10.1029/2010JF001878
