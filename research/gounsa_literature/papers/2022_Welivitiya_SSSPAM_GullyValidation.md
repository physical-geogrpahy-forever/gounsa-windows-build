# 서지정보
Welivitiya, W. D. D. P., & Hancock, G. R. (2022). Calibration and validation of the SSSPAM coupled soilscape-landform evolution model for simulating short-term gully development on a post-mining landform. *Earth Surface Processes and Landforms, 47*(11), 2779-2795. https://doi.org/10.1002/esp.5423

# 이 논문을 찾은 이유
SSSPAM이 이론모델을 넘어 실제 gully/rill-forming landform에서 검증됐는지, 그리고 필요한 calibration의 정도를 확인하기 위해 검토했다.

# 연구 유형
- model calibration and validation
- field gully comparison
- laboratory flume parameterisation

# 공간 구조
- evolving raster DEM
- gully-scale landform

# 적용 환경
- active coal-mine waste-rock landforms

# 핵심 과정
- fluvial erosion
- gully development
- armouring
- diffusion
- deposition
- physical weathering

# 식생 입력
- 본 핵심 검증은 vegetation dynamic model이 아님

# 핵심 결과
site-specific erosion parameters와 DEM, daily rainfall을 사용해 두 현장의 gully 위치와 전반적 geomorphic characteristics를 비교적 잘 재현했다.

# 자의성 관점에서 중요한 점
이 연구는 SSSPAM의 erosion parameters를 **실험 flume data로 calibration**한다.
따라서 해당 mine-site의 erosion parameter 값을 고운사에 그대로 가져오는 것은 금지한다.
SSSPAM을 whole erosion engine으로 사용하려면 고운사 보정이 필요하며 사용자가 요구한 최소자의성 원칙과 충돌한다.

# 고운사에 직접 사용할 수 있는 부분
- dynamic armour/profile/DEM architecture의 실제 검증
- model state updater 자체가 작동하는 증거

# 새로운 coupling이 필요한 부분
2D event erosion solver output을 SSSPAM armour/profile state에 전달.

# 한계
mine spoil, site-specific calibration.

# 최종 판정
- architecture는 채택
- SSSPAM 자체 fluvial erosion parameterisation을 고운사에 직접 이식하지 않음

# 참고 링크 / DOI
https://doi.org/10.1002/esp.5423
