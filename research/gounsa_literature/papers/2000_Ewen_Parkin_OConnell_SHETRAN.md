# 서지정보
Ewen, J., Parkin, G., & O'Connell, P. E. (2000). SHETRAN: Distributed river basin flow and transport modeling system. *Journal of Hydrologic Engineering, 5*(3), 250–258. https://doi.org/10.1061/(ASCE)1084-0699(2000)5:3(250)

# 찾은 이유
SHETRAN이 실존하는 통합 분포형 수문-토양침식-유사이송 모델인지, 진정한 공간적 계산 구조로서의 근거를 원저널에서 확인하기 위해.

# 연구 유형
[A: 출판사 원문 초록 직접 확인] 분포형 수문 및 수질/유사 운송 모델 방법론.

# 공간구조
Distributed catchment surface/subsurface coupled, finite differences, grid-based 2D horizontal surface grid / stacked 3D subsurface. Explicit rill erosion dynamic morphodynamics are NOT evidenced.

# 적용환경
유역규모 하천 및 산지 일반; 고운사 고해상도 TLS 0.5m event erosion 실험 출판선례를 뜻하지 않음.

# 핵심과정
saturated-unsaturated soil movement with surface runoff, vegetation canopy interception, sediment yield, contaminant transport.

# 식생입력
Vegetation state categories including LAI, surface and leaf interception, root extraction via hydrology; not a full cohort dynamic vegetation model itself.

# 핵심식
General distributed continuity on grid cells, original `SYOVER` rain/drip/flow detachment and `ETmod` storage are implemented in current published source version. Do not reconstruct full original water physics from abstract alone.

# 파라미터와 단위
area m2, time s, rain m/s, canopy C mm, sediment transport m3/s across faces.

# 고운사 직접 사용
Published umbrella architecture for public source with real native canopy interception and erosion and overland flow.

# 새로운 coupling
Actual individual oak and grass tussock position and new roots/rock fragmentation/rill-scale effects.

# 한계
Model runtime and site case not verified yet; public source CMake v4.7.2.0 has legacy source with sediment balance BALSED empty; no independent core mass closure evidence.

# 판정
유력 원본모형 대안, pending unchanged executable test.
