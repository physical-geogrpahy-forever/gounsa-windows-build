# 서지정보
Li, T., Sklar, L. S., & Gasparini, N. M. (2025). Hillslope grain size variation across evolving landscapes linked to climate, tectonics and lithology. Earth Surface Processes and Landforms, 50(8), e70111. https://doi.org/10.1002/esp.70111

# 이 논문을 찾은 이유
2025년 기준 최신 hillslope grain-size production model이 고운사 표면 입도분포 및 풍화 모델에 더 적합한지 확인하기 위해 검토했다.

# 연구 유형
- landscape evolution model coupling
- hillslope grain-size production model

# 공간 구조
- landscape scale
- spatially distributed LEM

# 적용 환경
- bedrock hillslopes
- climate, tectonics, lithology sensitivity experiments

# 핵심 과정
- latent initial grain-size distribution
- weathering-driven grain-size reduction
- erosion-rate/residence-time control
- climate and lithology control
- landscape evolution coupling

# 식생 입력
- 직접적인 dynamic vegetation module 없음

# 핵심 식/구조
Sklar et al. 계열의 두 단계 구조를 사용한다.
1. 기반암 fracture/bedding에 의해 초기 latent grain-size distribution P(D0)를 설정한다.
2. weathering function W가 입자의 residence time, climate, lithology에 따라 초기 입도분포를 변환한다.

# 파라미터와 단위
- initial grain-size distribution
- weathering susceptibility
- temperature
- precipitation
- erosion/uplift rate
- particle residence time

# 원 논문의 구현 범위
hillslope에서 생산되어 하천으로 공급되는 grain-size distribution을 landscape-scale LEM과 연결한다.

# 고운사에 직접 사용할 수 있는 부분
- 기반암 또는 fire-spall로 공급된 초기 암편 PSD가 weathering/residence time에 따라 어떻게 세립화되는지 표현하는 최신 이론 계보
- 장기 풍화와 입도생산 연결에 유용

# 새로운 coupling이 필요한 부분
- event-scale infiltration/runoff
- surface armour
- dry ravel
- LPJ-GUESS vegetation
- fire-spall event supply

# 한계
- 표면 armour와 event erosion을 직접 계산하지 않음
- 고운사의 100년 산불 후 event hydrology보다 장기 hillslope grain-size production에 더 적합

# 최종 판정
- **최신 hillslope grain-size production/weathering 근거**
- 고운사 표면 동적 입도분포 엔진의 본체보다는 weathering/fragmentation 보조근거

# 참고 링크 / DOI
https://doi.org/10.1002/esp.70111
