# 서지정보
Shmilovitz et al. (2024). Impacts of Rainstorm Intensity and Temporal Pattern on Caprock Cliff Persistence and Hillslope Morphology in Drylands. Journal of Geophysical Research: Earth Surface, 129(2). https://doi.org/10.1029/2023JF007478

# 이 논문을 찾은 이유
고운사에서 최신 계열의 표면 입도분포, 암편 파쇄, 유출기반 입도선택적 이동, dry ravel, 침투를 하나의 수치모델 안에서 동시에 다루는 사례를 확인하기 위해 검토했다.

# 연구 유형
- Landlab 기반 process-based numerical model
- event-scale hydrology + long-term hillslope evolution

# 공간 구조
- raster grid
- 2D overland-flow routing
- hillslope profile/landscape evolution

# 적용 환경
- 건조지 caprock cliff와 rocky hillslope
- 산림 산불사면과 직접 동일하지 않음

# 핵심 과정
- 시간가변 강우
- Green-Ampt infiltration
- 2D overland flow
- particle-size-dependent runoff-driven transport
- debris-particle fragmentation
- cliff weathering
- cliff-debris dry ravel
- 입도선택적 이동 및 퇴적

# 식생 입력
- 없음

# 핵심 식/구조
각 격자에서 강우, 침투, overland flow를 계산하고, 입도별 임계전단응력과 이동성을 이용하여 size-dependent sediment transport를 계산한다.
입자 파쇄율과 cliff-derived initial grain-size distribution을 통해 시간에 따라 표면 grain-size distribution이 변화한다.

Hydrology:
∂h_w/∂t = -∇q_water + P - I

침투는 Green-Ampt, 유출은 Landlab OverlandFlow, dry ravel은 HyLands sediment runout 계열을 사용한다.

# 파라미터와 단위
- rainfall intensity: 시간가변, 1-min resolution
- debris fragmentation rate ΔF: 1/storm
- debris-layer saturated hydraulic conductivity K_s: m/s
- lower-layer hydraulic conductivity: m/s
- particle-size classes / d50
- critical shear stress
- Manning roughness
- sediment porosity, density

# 원 논문의 구현 범위
표면 grain size가 runoff-driven transport와 sediment sorting에 직접 영향을 주고, fragmentation과 dry ravel이 표면 입도상태를 갱신한다. 다만 침투계수 K_s는 debris layer에 대해 외생적으로 부여되며, 현재 grain-size distribution에서 동적으로 계산되지는 않는다.

# 고운사에 직접 사용할 수 있는 부분
- mARM보다 훨씬 최근의 표면 입도분포 동적 모델 계보
- fire-spall로 생성된 암편을 size classes로 투입한 뒤 fragmentation, runoff transport, dry ravel로 갱신하는 구조에 매우 적합
- Landlab 기반이라 기존 지형 과정과 결합 용이
- event hydrology와 long-term grain-size evolution을 함께 계산하는 구현 선례

# 새로운 coupling이 필요한 부분
- LPJ-GUESS vegetation
- fire-spall initial PSD production
- 현재 surface grain-size/cover/embeddedness에서 Green-Ampt hydraulic parameters를 동적으로 산정하는 단계
- 산림 토양 및 사암 고운사 parameterization

# 한계
- 건조지 암벽 및 talus 중심
- 식생 없음
- infiltration parameter가 grain-size distribution으로부터 직접 동적 산출되지는 않음
- 고운사에 그대로 쓰기보다 surface-grain-size engine의 최신 핵심 후보로 사용

# 최종 판정
- **최신 rocky-hillslope surface grain-size dynamics 핵심 후보**
- ARMOUR/mARM 계열보다 고운사의 runoff + fragmentation + dry ravel 구조에 더 직접적
- 단, infiltration coupling은 별도 필요

# 참고 링크 / DOI
https://doi.org/10.1029/2023JF007478
