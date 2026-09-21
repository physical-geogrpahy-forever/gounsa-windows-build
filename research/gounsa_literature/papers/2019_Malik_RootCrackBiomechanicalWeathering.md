# 서지정보
Malik, I., Pawlik, Ł., Ślęzak, A., & Wistuba, M. (2019). A study of the wood anatomy of Picea abies roots and their role in biomechanical weathering of rock cracks. *CATENA, 173*, 264-275. DOI: 10.1016/j.catena.2018.10.018.

# 이 논문을 찾은 이유
살아 있는 spruce roots가 실제로 rock cracks를 widening하는 정량적 증거가 충분한지, root-growth physical weathering을 production에 넣을 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- 현장관측
- root wood-anatomy analysis

# 공간 구조
- individual root / fractured bedrock

# 적용 환경
- steep forested slopes
- Norway spruce
- fractured bedrock

# 핵심 과정
- root growth in cracks
- root deformation
- possible crack widening
- biomechanical weathering

# 식생 입력
- living Picea abies roots
- root diameter/anatomy
- growth history

# 핵심 식
보편적인 annual fracture-rate equation은 없다.

# 파라미터와 단위
root cross-sectional geometry and anatomical indicators.

# 원 논문의 구현 범위
root anatomy로 crack-contact와 sudden additional growth space를 복원한다.

# 고운사에 직접 사용할 수 있는 부분
root wedging을 당연한 deterministic fracture process로 넣으면 안 된다는 중요한 제약.
논문은 root pressure만으로 crack widening이 일어났다는 증거가 inconclusive하다고 판단하며, wind flexing, mass movement, freeze-thaw 등 대안도 제시한다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root growth를 fracture opening rate로 바꾸는 식은 새 coupling이며 현재 직접 근거가 부족하다.

# 한계
- sample size small
- rock type and site specific
- direct force/fracture measurement 아님

# 최종 판정
- 보조근거
- biomechanical root-weathering은 sensitivity/optional process로 유지
- production baseline의 deterministic root-fracture term으로 바로 채택하지 않음

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2018.10.018
