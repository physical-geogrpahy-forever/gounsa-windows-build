# 서지정보
Liang, W.-L., Kosugi, K., & Mizuyama, T. (2009). A three-dimensional model of the effect of stemflow on soil water dynamics around a tree on a hillslope. Journal of Hydrology, 366, 62–75. https://doi.org/10.1016/j.jhydrol.2008.12.009

# 이 논문을 찾은 이유
수간유하가 확산성 수관통과우와 달리 국지 점유입으로 작용하며 산지 수분장의 이질성을 유발하는지 확인.

# 연구 유형
3D 토양수분 수치모델, 현장 강우사상 관측.

# 공간 구조
개체목 주변의 사면 3차원 토양 수분장. 2D 지표유출-침식 엔진 아님.

# 적용 환경
산림 사면의 한 나무 주변.

# 핵심 과정
throughfall: 상대적으로 확산된 입력; stemflow: 줄기 기부의 집중 입력; 토양수분 이동 및 뿌리 주변 이질성.

# 식생 입력
줄기기부 stemflow 경계유입과 수관통과우, 뿌리-토양 물길의 효과.

# 핵심 식
3D unsaturated soil-water transport; 현재 확인 범위는 저널 원문 초록 및 소개 구간, 지배식 상세는 추가 원문 점검 필요.

# 파라미터와 단위
분포형 강우 공급: [m/s] 등으로 일치시켜야 함. 원문 상세 매개변수는 미확인.

# 원 논문의 구현 범위
stemflow 유무에 따른 산림사면 토양수분 모의. erosion 미구현, 지표유출 검증 별도 필요.

# 고운사에 직접 사용할 수 있는 부분
stemflow를 일반 평균강우로 희석하지 않고 위치별 경계유입으로 두는 근거.

# 새로운 coupling이 필요한 부분
강우 및 수간유하우 생성모형, 2D overland flow, 침식.

# 한계
지표 침식모형 아님.

# 최종 판정
핵심 보조근거(토양침투계의 공간 효과).

# 참고 링크 / DOI
https://doi.org/10.1016/j.jhydrol.2008.12.009
