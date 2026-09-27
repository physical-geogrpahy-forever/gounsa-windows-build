# 서지정보
Kim, S., Jeong, M., Kim, J., & Kim, D.-H. (2023). Effects of Soil Particle Size on Relationship Between Mound-Puddle Type Microtopography Roughness and Soil Erosion Rate on a Hillslope Basin: Hairsine–Rose Model Analysis. *Water Resources Research, 59*(3), e2022WR033879. https://doi.org/10.1029/2022WR033879

# 이 논문을 찾은 이유
고운사에서 실제 2D hillslope에서 multiple particle sizes, dynamic surface shield/armouring, rainfall/runoff erosion을 동시에 처리한 비교적 최근 numerical-model application을 확인하기 위해 검토했다.

# 연구 유형
- physically based numerical experiment
- tRIBS-FEaST / dynamic-wave + Hairsine-Rose model

# 공간 구조
- 1D 및 genuine 2D hillslope-basin domains
- 2D unstructured triangular mesh
- shallow-water dynamic-wave equations

# 핵심 과정
- raindrop detachment
- overland-flow entrainment
- particle-class-specific suspended sediment concentration
- deposition
- redetachment/re-entrainment of deposited layer
- mechanistic deposited-layer development
- particle-size-dependent surface shielding/armouring

# 수문
기반 tRIBS-FEaST framework 자체는 interception, evapotranspiration, infiltration, runoff production, groundwater dynamics와 Saint-Venant surface flow를 결합할 수 있다.

그러나 **이 2023 논문의 특정 수치실험에서는 infiltration loss를 0으로 두고 rainfall intensity를 rainfall excess로 사용했다.** 따라서 이 논문 자체를 `GSD + dynamic infiltration` 검증사례라고 부르면 안 된다.

# 표면 입도/armour
Hairsine-Rose formulation은 여러 soil particle size classes를 추적하며, deposited layer의 class별 mass가 시간에 따라 변한다. 상대적으로 큰 입자에 의해 surface shield가 발달하면서 detachment/transport response가 변할 수 있다.

# 표면입도 -> infiltration feedback
- 이 연구에서는 **없음**
- particle size가 infiltration parameter 또는 hydraulic conductivity를 바꾸는 구조를 검증하지 않음
- hydraulic resistance도 particle size와 독립인 constant Manning value를 사용함

# 풍화/fragmentation
- **없음**
- coarse parent particle의 physical weathering에 의한 daughter-size production은 다루지 않는다.

# 고운사에 직접 사용할 수 있는 부분
- genuine 2D hillslope erosion
- rainfall/flow detachment process separation
- multiple particle sizes
- dynamic deposited-layer shield
- microtopography와 particle-size-dependent erosion interaction

# 새로운 coupling이 필요한 부분
- infiltration feedback
- fire-spall coarse fragments
- large rock-fragment transport
- physical weathering/fragmentation
- LPJ-GUESS vegetation

# 한계
- 2023 application은 impervious surface assumption
- large coarse fragments보다 soil erosion particles 중심
- weathering 없음

# 최종 판정
- 최신 최종 surface-rock model 후보라기보다는 **2D multiclass Hairsine-Rose armour/shield 근거**
- Iber+ 2024가 현재 고운사의 2D rainfall/runoff multiclass erosion 엔진으로 더 직접적이고 최신
- 기반 tRIBS-FEaST는 hydrology까지 폭넓지만 surface GSD -> infiltration feedback은 해결하지 않음

# 참고 링크 / DOI
https://doi.org/10.1029/2022WR033879

# 기반 모델
Kim et al. (2013), *Water Resources Research*, DOI 10.1002/wrcr.20373.
