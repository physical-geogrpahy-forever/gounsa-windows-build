# 서지정보
Di Prima, S., et al. (2026). Trees control hillslope subsurface flow: Insights from stemflow and throughfall experiments, geophysical surveys, and numerical modeling. Journal of Hydrology, 665, 134723. https://doi.org/10.1016/j.jhydrol.2025.134723

# 이 논문을 찾은 이유
수간유하 집중이 줄기 주변 수리전도도를 초과해 지표유출로 이어진다는 단순 가정의 반례 검증.

# 연구 유형
인공 stemflow/throughfall 침투시험, GPR/ERT, 수문 수치 역산, dual-permeability model.

# 공간 구조
점-나무-시험구-사면; 다중 스케일 현장 및 수치 분석.

# 적용 환경
나무가 있는 산림사면.

# 핵심 과정
throughfall→토양 matrix 침투; stemflow→줄기기부 macropore/균열 통한 빠른 침투; 심부 측방류/수위 변동.

# 식생 입력
줄기기부와 수관하 강우공급 위치, 뿌리주변 우선유동 경로.

# 핵심 식
Dual-permeability 수문모형(초록 검증 단계). 상세 구성 원문 전문 추가 점검 필요.

# 파라미터와 단위
줄기사이 Ks 평균 177.8~237.4 mm/h, 줄기 기부 인공 stemflow 침투 정상상태 약 1031.9 mm/h; 수치 역산 fast-flow 영역 Ks 1047.4 vs matrix 217.5 mm/h. 해당 사이트 조건의 결과이지 고운사 기본값 아님.

# 원 논문의 구현 범위
줄기기부 집중강우와 토양 내 우선침투의 연계. 지표 침식 수송 미구현.

# 고운사에 직접 사용할 수 있는 부분
stemflow 주변의 infiltration capacity 및 preferential flow를 식생/토양 상태에 따라 달리 둘 필요성.

# 새로운 coupling이 필요한 부분
각 줄기의 집중 SF 공급, 침투-2D 지표유출-침식의 경쟁 경로.

# 한계
침식모형이 아님.

# 최종 판정
핵심 반례 근거(수간유하 항상 유출증가 아님).

# 참고 링크 / DOI
https://doi.org/10.1016/j.jhydrol.2025.134723
