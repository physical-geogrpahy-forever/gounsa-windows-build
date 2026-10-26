# 서지정보
Holder, A. J., McCalmont, J. P., McNamara, N. P., Rowe, R., & Donnison, I. S. (2018). Evapotranspiration model comparison and an estimate of field scale Miscanthus canopy precipitation interception. *GCB Bioenergy, 10*(5), 353–366. https://doi.org/10.1111/gcbb.12503

# 이 논문을 찾은 이유
참나무 맹아와 억새의 수간유하우, 수관통과우, 수관차단 차이를 검토할 때 근거 없이 억새의 interception/stemflow를 0으로 취급하지 않기 위해서다.

# 연구 유형
영국 웨일스 Miscanthus × giganteus 약 6 ha 포장의 장기간 현장관측, 증발산 모형 비교. 고운사의 Miscanthus sinensis 직접 실측이 아님.

# 공간 구조
포장 강우계 및 내부 수관통과우, 수간유하우 관측; 2D 유출/침식 수치모형 아님.

# 적용 환경
평균 경사 약 7°의 평탄한 에너지작물 경작지, 주로 clay loam 및 sandy/silty clay loam. 고운사 산불 사암 얕은 토심 사면 아님.

# 핵심 과정
2016년 6월~2017년 3월 측정에서 외부 강우 776 mm, 포장 내 순강우 588 mm(통과우 455 mm + 수간유하우 133 mm), 차단 손실 188 mm(24%). 포장 관측 시기와 사건별 값은 다양하며 여름에 interception 높은 경향. 동일 기간 stemflow 비율 133/776≈17.1%, throughfall 455/776≈58.6%.

# 식생 입력
Miscanthus × giganteus의 실물 포장 식생구조 및 계절상태. 사용자 연구의 억새종 Miscanthus sinensis 및 줄기 밀도/각도 실측으로 직접 대체할 수 없음.

# 핵심 식
관측에서 P = TF + SF + interception loss. 776 mm = 455 + 133 + 188 mm. 측정한 장기간 손실 비율을 1시간 10~50 mm/h 폭우에서 즉시 일정 비율로 곱하지 않음.

# 파라미터와 단위
mm, 강우계 30분 집계, interception %; 실측 event-scale 표본 51개 조사.

# 원 논문의 구현 범위
수관 통과우와 수간유하우 실측, 증발산 모형 비교. 2D Green-Ampt/Hairsine–Rose 침식모형이 아님.

# 고운사에 직접 사용할 수 있는 부분
억새 계열 다년생 초본도 상당한 수간유하우를 만들 수 있다는 물리적 근거. EUROSEM의 shape=1 억새형 시나리오 및 SF/TF 비율의 비교 앵커.

# 새로운 coupling이 필요한 부분
줄기별 국지 SF 침투면적, 강우적하 에너지, 2D 수문-침식 공간 공급. 기존 논문으로 구현되었다고 주장하지 않음.

# 한계
종 다름, 완전히 다른 경사/토양/기후, 연평균 비교. 2016~2017 누적 비율을 강한 단일 1h 강우 event 비율로 그대로 이식하지 않음.

# 최종 판정
보조 관측근거. 고운사 억새 식생 매개변수의 직접 보정자료는 아님.

# 참고 링크 / DOI
https://doi.org/10.1111/gcbb.12503
