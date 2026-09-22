# 서지정보
Zhang, Y., Slingerland, R. L., & Duffy, C. J. (2016). Fully-coupled hydrologic processes for modeling landscape evolution. *Environmental Modelling & Software, 82*, 89-107. https://doi.org/10.1016/j.envsoft.2016.04.014

# 이 논문을 찾은 이유
Richards/groundwater/overland-flow 수준의 수문과 landform evolution을 한 기존 모델로 처리해 OpenLISEM-SSSPAM 결합보다 자의성을 더 줄일 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- fully coupled hydrologic-morphodynamic model
- LE-PIHM

# 공간 구조
- TIN/control-volume
- lateral surface and groundwater flow
- evolving land surface and bedrock interface

# 적용 환경
- theoretical/catchment landscape evolution

# 핵심 과정
- infiltration
- vadose-zone storage
- groundwater flow/exfiltration
- 2D lateral surface runoff
- hillslope/channel sediment transport
- bedrock weathering/regolith formation
- creep/tree-throw lumped lateral flux
- landscape elevation evolution

# 식생 입력
- evapotranspiration included
- dynamic PFT/root erosion coupling 없음

# 핵심 식
land surface elevation과 bedrock elevation을 mass conservation으로 동시에 갱신한다.
regolith thickness는 surface-bedrock elevation difference로 계산한다.

# 고운사에 직접 사용할 수 있는 부분
- subsurface hydrology와 landscape evolution을 같은 control volume에서 푸는 강한 precedent
- soil moisture/runoff/groundwater-topography feedback

# 결정적 한계
- particle-size-resolved surface armour/weathering transition이 핵심 state로 들어가 있지 않음
- 고운사의 embedded rock-fragment PSD와 dynamic armour 문제를 해결하지 못함
- bedrock weathering은 soil-thickness-dependent production function 계열이며 fire-spall PSD evolution과 다름

# 최종 판정
- integrated hydro-morphodynamic comparison model
- **고운사 최종 기반으로는 SSSPAM armour/profile 기능 부족 때문에 탈락**
- subsurface hydrology architecture 참고

# 참고 링크 / DOI
https://doi.org/10.1016/j.envsoft.2016.04.014
