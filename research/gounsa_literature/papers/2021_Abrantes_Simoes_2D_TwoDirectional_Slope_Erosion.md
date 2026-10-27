# 서지정보
Abrantes, J. R. C. B., Simões, N. E., de Lima, J. L. M. P., & Montenegro, A. A. A. (2021). Two-dimensional (2D) numerical modelling of rainfall induced overland flow, infiltration and soil erosion: Comparison with laboratory rainfall-runoff simulations on a two-directional slope soil flume. *Journal of Hydrology and Hydromechanics*, 69(2), 140–150. https://doi.org/10.2478/johh-2021-0003

# 이 논문을 찾은 이유
고운사의 다방향 유출(open all boundaries), 국지 세류/비세류 박리와 퇴적을 하나의 물리적 2D 모델에서 실험 검증한 비-LISEM 계열 선행연구를 찾기 위해.

# 연구 유형
- 논문상 2D 유동-침투-침식 통합 수치모형 개발 및 강우모사 토양수로 검증.
- 2026-10-27 저널 공식 초록과 저자/DOI, 공개 전문 PDF 검색 기록 확인. 원 PDF 전문은 외부 서버에서 HTTP 400 octet-stream으로 직접 열람되지 않아 **초록과 색인된 논문 첫 장의 정보까지만 확인**. 전체 수식, 격자·시정수, 관측 정량오차는 미확인. 이 제한을 반영한다.

# 공간 구조
- 2D unsteady flow equations, 2D sediment transport equations. **진정 2차원 유동 방향성을 포함한다고 논문 초록에 명시**.
- 실제 검증 토양 실험수로: 2.00m × 2.00m. x 경사 1%, y 경사 10%.
- 계산 격자 실제 셀크기: **미확인**, 5–10cm 선례라고 단정 금지.

# 적용 환경
- 실험실 노출 토양, 양방향 경사 강우모사.
- 산지 산림, 듬성한 참나무 맹아 또는 억새 혼재피복 실험은 아님.

# 핵심 과정
- Horton-SCS 결합 침투.
- 2D 비정상 지표유출.
- interrill 및 rill 분리, sediment deposition 포함. 별도 지형고도 자동갱신 검증 근거는 확인하지 못함.

# 식생 입력
- 본 연구 초록 및 확인된 방법 설명에 LAI, Smax, Rutter/Gash 수관차단, leaf-drip 충격, stemflow는 나타나지 않음. **수관과정 원본 구현 미검증**, 존재한다고 추정 금지.

# 핵심 식
- 유동: 2D nonstationary depth-averaged flow equations (정확 근사식 및 flux method 미확인).
- 유사: 2D sediment transport conservation (exact coefficient 및 boundary formulation 미확인).
- 침투: 결합 Horton-SCS scheme.
- 수식 전문/파라미터 직접 전사는 하지 않음.

# 파라미터와 단위
- x 경사 0.01(-), y 경사 0.10(-), flume 2.00×2.00 m².
- rainfall intensity, cell size, dt, Ks, erodibility, transport capacity coefficient: 해당 원문 판독 미완료.

# 원 논문의 구현 범위
- 경사가 작은 x방향의 상대적으로 작은 runoff/sediment flux 과소평가; y방향 높은 runoff/sediment flux는 잘 모의; 방향 통합 시계열 대조도 비교적 좋은 성능.
- 강우 및 관측 수로의 표본이 제한적이므로 산림 steep 5cm true2D 유사보존 일반화 금지.

# 고운사에 직접 사용할 수 있는 부분
- 자유로운 xy 두 방향 runoff와 침식/퇴적 검증의 독립 원논문 선례.
- 기존 1D/D8/운동파 식생모델과 대비하는 배출방향 및 보존 체크에 보조근거.

# 새로운 coupling이 필요한 부분
- LAI-based canopy storage, dynamic drip, leafdrop KE 및 산림 지면 거칠기와 침식물리의 연결은 이 연구의 확정 내장모듈이 아님.
- 추가 개발로 만들 경우 **새로운 coupling**이며 기존 논문 단일모델이라고 명명 금지.

# 한계
- **원본 소스코드 및 재현 입력자료 GitHub/Zenodo 공개위치 미발견**. absence proven 이 아니라 현재 검증 미확인.
- 산지 사례 아님. 5cm actual mesh 미확인. Rutter, leaf-drip, 숲 canopy 미확인.
- PDF 원문 및 계수 검증 미완료로 상세 성능수치 인용 금지.

# 최종 판정
**보조근거/주모델 보류.** 기존 INDEX에 없던 genuinely 2D rill/interrill/deposition published case. 고운사 all-native 조건 만족은 아니며 자체 실행 소스 미확보.

# 참고 링크 / DOI
https://doi.org/10.2478/johh-2021-0003
https://reference-global.com/article/10.2478/johh-2021-0003?tab=abstract
https://sciendo.com/2/v2/download/article/10.2478/johh-2021-0003.pdf
