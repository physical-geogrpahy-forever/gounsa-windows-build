# 서지정보
Shmilovitz, Y., Tucker, G. E., Rossi, M. W., Morin, E., Armon, M., Pederson, J., Campforts, B., Haviv, I., & Enzel, Y. (2024). Impacts of Rainstorm Intensity and Temporal Pattern on Caprock Cliff Persistence and Hillslope Morphology in Drylands. *Journal of Geophysical Research: Earth Surface, 129*(2), e2023JF007478. https://doi.org/10.1029/2023JF007478

# 이 논문을 찾은 이유
고운사에서 최신 계열의 표면 입도분포, 암편 파쇄, 유출기반 입도선택적 이동, dry ravel, 침투를 하나의 수치모델 안에서 동시에 다루는 사례를 확인하기 위해 검토했다.

# 연구 유형
- Landlab 기반 process-based numerical model
- event-scale hydrology + long-term hillslope evolution

# 공간 구조
- 80–200 × 3 raster grid를 사용하지만 경계조건 때문에 **실질적으로 1D hillslope profile model**이다.
- Landlab `OverlandFlow` 자체는 2D shallow-water routing component이지만, 이 논문의 실제 실험구성은 genuine 2D hillslope simulation이 아니다.

# 적용 환경
- 건조지 caprock cliff와 rocky hillslope
- 산림 산불사면과 직접 동일하지 않음

# 핵심 과정
- 1-min rainfall intensity를 이용한 event-scale 강우
- Green-Ampt infiltration
- overland-flow routing
- particle-size-dependent runoff-driven transport
- debris-particle fragmentation
- cliff weathering
- cliff-debris dry ravel
- 입도선택적 이동 및 퇴적

# 식생 입력
- 없음

# 핵심 식/구조
표면 debris는 여러 grain-size class의 질량으로 저장된다. 물리적 fragmentation은 mARM 계열 transition matrix를 사용한다.

```text
G_(t+1) = G_t + ΔF A G_t
```

여기서 `G`는 입도별 질량 state vector, `A`는 parent-to-daughter fragmentation matrix, `ΔF`는 fragmentation rate이다.

수문 질량보존:

```text
∂h_w/∂t = -∇q_water + P - I
```

침투는 Green-Ampt:

```text
I = Ks [1 + ((h_w + ψ_f)(φ_sed - θ_i))/F]
```

침투는 Landlab `SoilInfiltrationGreenAmpt`, 유출은 `OverlandFlow`, dry ravel은 HyLands sediment-runout component 계열을 사용한다.

# 시간구조
- 원 논문의 rainfall forcing은 **1분 해상도**이며 개별 storm은 약 15–95분이다.
- 따라서 고운사의 **1시간 외부 forcing을 그대로 사용한 published precedent는 아니다**.
- 내부 numerical substep과 외부 coupling interval은 별개일 수 있으나, 이 논문 자체를 `1-hour model`이라고 부르면 안 된다.

# 파라미터와 단위
- rainfall intensity: 1-min resolution in published experiments
- debris fragmentation rate `ΔF`: 1/storm
- debris-layer saturated hydraulic conductivity `Ks`: m/s
- lower-layer hydraulic conductivity: m/s
- particle-size classes / d50
- critical shear stress
- Manning roughness
- sediment porosity, density

# 원 논문의 구현 범위
표면 grain size가 runoff-driven transport와 sediment sorting에 직접 영향을 주고, fragmentation과 dry ravel이 surface grain-size state를 갱신한다. 다만 `Ks`, `ψ_f` 등 침투계수는 debris/lower layer별 외생 parameter이며 **현재 grain-size distribution에서 동적으로 계산되지 않는다**.

# 고운사에 직접 사용할 수 있는 부분
- 최신 rocky-hillslope 표면 입도분포 모델의 중요한 선례
- fire-spall 암편을 size classes로 공급한 뒤 fragmentation, runoff transport, dry ravel로 갱신하는 구조
- Landlab component 기반이라 다른 Landlab 모듈과 결합이 용이
- 표면 PSD를 mass-conserving state vector로 유지하는 방식

# 새로운 coupling이 필요한 부분
- LPJ-GUESS vegetation
- fire-spall initial PSD production
- 1시간 고운사 forcing과의 coupling
- 현재 surface PSD/cover에서 `Ks`, `ψ_f`, roughness를 동적으로 산정하는 과정
- 산림 토양 및 사암 고운사 parameterization
- genuine 2D hillslope implementation

# 한계
- 실제 논문 실험은 effectively 1D
- 원 강우는 1-min resolution
- 건조지 cliff/talus 중심
- 식생 없음
- infiltration parameter가 grain-size distribution으로부터 직접 갱신되지 않음

# 최종 판정
- **과정구조 참고용 핵심 후보**
- fragmentation + size-selective runoff transport + dry ravel의 결합은 고운사에 매우 유용
- 그러나 고운사 최종 surface-grain-size engine으로 그대로 채택하기에는 `1-min forcing`, `effectively 1D`, `PSD→hydraulic feedback 부재`가 핵심 제약

# 참고 링크 / DOI
https://doi.org/10.1029/2023JF007478
