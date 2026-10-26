# 서지정보
Opedes, H., Fuchs, L. F., Baartman, J. E. M., Mücher, C. A., Kessler, A., & Ritsema, C. J. (2025). Modelling the impact of trenches on soil erosion control using OpenLISEM on Mount Elgon, Uganda. *Earth Surface Processes and Landforms, 50*(6), e70074. https://doi.org/10.1002/esp.70074

확인: Wiley 공개 HTML 원문(2026-10-26). 2025-09-03 별도 정정 공고(https://doi.org/10.1002/esp.70154)가 연결되므로 세부 정정 내용은 추가 확인 대상.

# 이 논문을 찾은 이유
고운사 필수 세 조건 중 특히 (3) 급경사지 실제 OpenLISEM 적용, (1) LAI 기반 식생입력, (2) 직접유출 침식을 동일 연구의 실제 적용 설계에서 검증하기 위함.

# 연구 유형
- 실제 산지 유역의 사건기반 수치모델 적용, 현장 강우 및 하천 수위 관측 기반 유출 보정, 토양유실 시나리오 분석.

# 공간 구조
- 2D Dynamic Wave 지표유동을 **실제로 선택** (원문 3.2 및 3.5). 따라서 해당 적용 자체가 단순 D8 1D routing이라는 주장은 틀림.
- Ukha sub-catchment 44.5 km², ALOS PALSAR DEM 기반 12.5 m 격자, 내부 시간간격 15 s, Green-Ampt 단일 토층 침투.
- 농지의 도랑 구조는 격자보다 작아서 직접 DEM 조각이 아니라 random roughness / micro-depression storage로 매개변수화.

# 적용 환경
- 우간다 Mount Elgon, upper Manafwa, 산지 급경사. 도랑 설치 농지 조사점의 82%가 10–30° 경사, 3%가 >=31°. 이 비율은 **전체 유역 사면의 경사 분포가 아님**.
- 2022-04-28 강우 5시간, 누적 18.6 mm, 최대 25 mm/h, 10분 강우 관측.

# 핵심 과정
- 수관 및 지표 식생 상태 -> 차단/강우 유효도달, Green-Ampt 침투, 2D dynamic-wave 유출, 침식 및 토양유실 시나리오.
- 논문에서는 도랑의 지표저류 효과를 RR로 표현. 출판 연구에서 구현한 식생-침식 계산을 원본 소스 기능과 분리해서 판단해야 함.

# 식생 입력
- LAI: NDVI에서 추정 (원문 식 1: Y=0.0255 exp(6.748x)); 기초 자료는 조사구 추정치.
- vegetation cover (PER): 1 m² 방형구 3회 평균.
- vegetation height (CH, m): 줄자로 측정, 교목은 경사측량 도구로 추정.
- litter cover, plant root extra cohesion COHr (kPa), plant/soil roughness, stone cover.
- 논문 표 2의 LAI 예: grassland 0.69, planted forest 1.38, tropical forest two classes 2.64; 이 수치는 **고운사 억새 또는 참나무 맹아의 생태값이 아님**.
- COHr는 다른 문헌에서 추정하여 입력: 원본이 root biomass/RLD를 자동으로 환산한다는 뜻이 아님.

# 핵심 식
- 논문 trench 저장 시나리오: RR = RR0 + AR, MDS = 0.01 RR^2 + 0.243 RR - 0.012 S RR (원문 식 3–5; S=경사율 0–100).
- 수관 LAI 및 수관저류 원본 구현은 동일 모델 공개 source `hydro/lisInterception.cpp`에 존재하며 별도 모델 계보 문서 참조.
- 논문 자체에 없는 줄기별 수간유하→유동 국지공급 함수 및 식생 코호트 동적 RLD 기능을 이 논문의 구현이라고 쓸 수 없음.

# 파라미터와 단위
- 공간 12.5 m, 계산 dt 15 s, 강우 관측 10 min, 강우 18.6 mm/5 h, 최고 25 mm/h.
- D50 (μm), COH/COHr(kPa), canopy height(m), LAI(m²/m²), Ksat(mm/h), soil depth(mm), stone fraction(-), vegetation cover(-).
- 보정 승수: Ksat 0.38, Manning n 1.2 (논문의 해당 사건). 값의 고운사 전용 전이는 부적절.

# 원 논문의 구현 범위 및 관측 결과
- 단일 관측 강우사상 discharge 보정: NSE 0.72, KGE 0.61.
- 관측된 유사농도 자료를 얻지 못했으며 **침식량 독립 검증 불가**. 시뮬레이션 간 토양유실 차이: 도랑 포기 시 runoff +75.97%, soil loss +35.12%; 전면 도랑 설치 시 runoff -40.45%, soil loss -33.81% (현 상황 대비 시나리오).
- 어떤 동일 지형에서 산불 후 실제 억새 vs 참나무 맹아로 검증한 연구가 아님.

# 고운사에 직접 사용할 수 있는 부분
- 진짜 2D dynamic wave 모형에 LAI, height, litter, cover, root cohesion, rock cover, erosion을 넣은 **급경사지 실증 적용 전례**.
- 공개 원본 자체는 `vjetten/openlisem`, `main_C` 고정 해시 `d894c72428947247ce49eb88353dadf49b3123e8`의 수관/적하우/침식 코드로 별도 확인.
- 본 논문이 사용한 버전이 2026 최신 7.5.2 실행파일과 동일함을 의미하지 않음.

# 필요한 새로운 coupling
- LPJ-GUESS PFT/LAI/height/litter/FineRootC -> spatial maps 변환(원본 입력 변수와 자연과정 식의 연결 필요).
- 개체별 국지 수간유하를 원한다면 별도 conservation interface 구현.
- 사건 간 변화량(침식/퇴적) -> 다음 사건 DEM 및 토양두께 갱신을 추가할 경우 **새로운 coupling**.
- spall/rock fragmentation -> stone cover/fraction 변화는 본 연구와 원본의 독립 기능이 아님.

# 한계
- 자료 검증은 유출곡선 1사상이며 sediment observation이 없고, 12.5 m 격자에서는 줄기별 수문이나 세류 자동발생을 검증하지 못함.
- 급경사 논문이라는 사실 자체가 모든 급경사/아주 얕은 사암토양에서 안정적 성능을 입증하지 않음.
- 2025-09-03 정정공고의 세부 내용 추가 점검 필요.

# 최종 판정
**채택: OpenLISEM의 세 필수 조건을 검토하는 급경사지 적용 핵심 선례.**
단, 발표된 침식 정확도 검증 성공으로 오인하지 않는다. 2026 Windows 최신 7.5.2 네이티브 실행/물수지/유사수지는 아직 별도 검증 필요.

# 참고 링크 / DOI
- https://onlinelibrary.wiley.com/doi/full/10.1002/esp.70074
- https://doi.org/10.1002/esp.70074
- https://doi.org/10.1002/esp.70154 (correction)
- https://github.com/vjetten/openlisem/tree/d894c72428947247ce49eb88353dadf49b3123e8
