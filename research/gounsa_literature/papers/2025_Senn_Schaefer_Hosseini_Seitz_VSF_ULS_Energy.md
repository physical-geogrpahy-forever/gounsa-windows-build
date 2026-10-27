# 서지정보
Senn, J. A., Schäfer, J., Hosseini, Z., & Seitz, S. (2025). Predicting rainfall kinetic energy under forest canopies—A pilot study using ULS. *Earth Surface Processes and Landforms*, 50(11), e70150. https://doi.org/10.1002/esp.70150

# 이 논문을 찾은 이유
단순 수관저류는 수관 아래 빗방울의 지표 충격력을 나타내지 못한다. 고운사 드론 LiDAR 수관구조를 관측변수로 하여 참나무 맹아/억새 피복 아래 국지 강우 박리 영향을 정량화한 연구의 실제 선례를 찾음.

# 연구 유형
- published Vegetation Splash Factor (VSF) 모델의 처음 현장 자료 기반 pilot validation.
- UAV laser scanning ULS + 지상 TLS 위치 정합 + 모래 채운 splash cups(강우운동에너지 간접 추정) 관측.
- KIT 대학기관 원문 공개 레코드/저자 2025 논문, 해당 open manuscript의 본문 텍스트 검색 확인.

# 공간 구조
- point-cloud voxel canopy geometry -> vertically stratified 3D gap fraction profile -> map of vegetation effect on throughfall kinetic energy.
- 조사 본문: 수직 voxel step 약 0.25m, 가로 0.50m grid. **5–10cm 격자 실증은 아님**.
- forest ULS point density 약 800–1,200points/m². UAV RIEGL miniVUX-1UAV, DJI Matrice 600 Pro, 60–80m 비행고도, 2019 acquisition; 2020 현장 기간 observation.

# 적용 환경
- 유럽 중부 온대산림 pilot; 2020년 여름부터 가을까지 여러 기간별 splash cup comparison.
- 개별 참나무 맹아/억새의 구조 매개변수와 결과를 직접 대입하는 것은 별도 검증 필요.

# 핵심 과정
- vegetation height profile에 따른 throughfall KE의 저감 또는 증폭 효과를 VSF로 공간예측.
- 투과우 KE 증가/감소는 강우량 intercepted water balance와 서로 다른 물리량.
- 실제 토양 interrill/rill detachment / sediment advection / deposition / runoff equation **없음**.

# 식생 입력
- LiDAR에서 얻는 수관 높이, voxel canopy gap fraction, canopy vegetation surface vertical distribution.
- root biomass, RLD, leaf drip volume/drainage and soil erosion 2D coupling unimplemented.

# 핵심 식
- VSF: vegetation layer height/coverage에 따른 throughfall KE multiplier; 2025 manuscript에서 2020 VSF의 conceptual model과 voxel gap fraction 사용.
- 숫자 계수의 정확한 출처 검증 없이 특정 2025식을 재작성하거나 단순 empirical interception과 동일시 금지.

# 파라미터와 단위
- horizontal voxel 0.50m, height step 0.25m.
- UAV density 800–1200 points/m².
- 샘플 TKE J/m², unit TKE J/m²/mm. 정확 단일 validation R²/RMSE 수치 본문 표 검증 미완료여서 기록 안 함.

# 원 논문의 구현 범위
- 예측된 식생 강우 KE 영향과 현장 관측 사이 통계적으로 유의한 상관 확인.
- 관측 KE 변화가 기존 문헌보다 커서 VSF가 에너지 수준을 **체계적으로 과소추정**. 저자들은 지역별 재보정/적용 축척 추가 검증을 권고.
- **TKE field data ≠ 직접 측정한 토사박리량의 함수/침식모델 검증**. 이를 회귀식 침식 엔진으로 홍보 금지.

# 고운사에 직접 사용할 수 있는 부분
- 드론 3D 식생정보로 수관 아래 강우 운동에너지의 2D hotspot 공간패턴을 예측하는 현장 검증 개념.
- 캐노피 조도/잎 높이에 따라 물방울 KE가 직접강우보다 증가할 수도 있어 수관차단 ON 효과가 반드시 토사 감소가 아님을 보여주는 비교근거.

# 실제 소스 확인
- 2025 논문 공개 DOI/공식 대학 기관 기록 및 오픈 PDF 확인. **원본 VSF executable script/GitHub tag, example runnable input은 이번 조사에서 확인되지 않음**.
- model equations/paper existence를 소스공개와 혼동 금지.

# 새로운 coupling이 필요한 부분
- VSF -> splash detachment impact flux; site calibrated relation; x/y hydrodynamics into transport/deposition is new coupling.
- 고운사 5cm actual polygon vegetation/ULS density, 0.5m voxel 발표법의 재격자 시 검증 필요.

# 한계
- rainfall volume/throughfall canopy storage, actual sediment 2D transport, soil mass conservation model 아님.
- 관측-모의 값 과소추정 및 제한된 pilot region.

# 최종 판정
**강우운동에너지-수관구조 우수한 보조근거.** 단일 침식 엔진으로 부적합. field-validated canopy under-rainfall KE mechanism for hotspot hypothesis.

# 참고 링크 / DOI
https://doi.org/10.1002/esp.70150
https://publikationen.bibliothek.kit.edu/1000184451
https://publikationen.bibliothek.kit.edu/1000184451/165081457
https://www.ifgg.kit.edu/english/projects_4275.php
