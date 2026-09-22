# 서지정보
Willgoose, G. R., & Sharmeen, S. (2006). A one-dimensional model for simulating armouring and erosion on hillslopes: I. Model development and event-scale dynamics. *Earth Surface Processes and Landforms, 31*(8), 970-991. https://doi.org/10.1002/esp.1398

# 이 논문을 찾은 이유
고운사에서 미세토 선택유실, 표면 조립화, 입도별 이동성, armour 형성을 임의 피복계수가 아니라 기존 동적 모델로 계산할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- 물리기반 수치모델
- ARMOUR model development
- rainfall-simulator calibration/validation

# 공간 구조
- 1D hillslope
- event 및 누적 다중사건

# 적용 환경
- Ranger Uranium Mine의 비점착성 stony sediment
- Northparkes Gold Mine의 점착성 silty sediment

# 핵심 과정
- time-varying runoff
- particle-size selective entrainment
- erosion
- deposition
- source-limited / transport-limited 전환
- dynamic surface armouring

# 식생 입력
- 핵심 모델에는 동적 식생상태 없음

# 핵심 식/구조
여러 입도 class의 transportability와 hiding/armouring을 동적으로 추적한다.
Parker-Klingeman 계열을 포함한 여러 size-selective entrainment formulation을 시험하고 현장자료와 비교한다.
세립분이 우선 제거되면 surface grading이 조립화되고 이후 sediment supply가 제한된다.

# 파라미터와 단위
- particle-size distribution
- runoff/discharge
- slope
- transport/entrainment parameters
- cohesive/non-cohesive soil properties

# 원 논문의 구현 범위
단일 사건부터 수십 년 누적사건까지 surface armour와 erosion/deposition의 동시 변화를 계산한다.

# 고운사에 직접 사용할 수 있는 부분
- `fine removal -> coarse enrichment -> armour strengthening` 전체를 기존 모델로 처리 가능
- 입도별 선택적 entrainment
- armour 때문에 runoff가 있어도 sediment supply가 제한되는 source-limited 상태
- 별도 custom armour factor를 만들 필요가 없음

# 새로운 coupling이 필요한 부분
- genuine 2D hydrodynamics
- embedded-stone soil hydrology
- LPJ-GUESS vegetation
- fire-spall 공급

# 한계
- 1D hillslope
- 원 모델 calibration이 mine spoil 자료에 기반
- 고운사 전체 runoff/erosion engine으로 그대로 쓰기에는 공간구조 한계

# 최종 판정
- **dynamic armour 핵심 원모델로 채택**
- 전체 2D runoff engine으로는 부적합

# 참고 링크 / DOI
https://doi.org/10.1002/esp.1398
