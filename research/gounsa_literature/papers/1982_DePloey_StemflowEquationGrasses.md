# 서지정보
de Ploey, J. (1982). A stemflow equation for grasses and similar vegetation. CATENA, 9(1–2), 139–152. https://doi.org/10.1016/S0341-8162(82)80010-6

# 검색 이유 및 연구 유형
[원 논문 초록 확인] 초본 포기형의 수간유하 집중을 설명한 인공강우실험 논문. 수치 침식모형 아님.

# 공간 구조 및 적용 환경
초본 모사 포기와 줄기 기부의 강우 집중; 고운사 억새는 미측정.

# 핵심과정 및 핵심식
강우 모의실험에서 형태계수를 사용하는 수간유하우 식과 stemflow increment ratio를 제시. 전문 식은 이번에 확보하지 못해 재구성하지 않음. EUROSEM 원본 INTERC 구현 식과 출판 원식의 완전한 동일성도 입증되지 않았음.

# 식생 입력
수관 형태계수, 포기 밑동과 줄기 형상.

# 매개변수와 단위
형태계수 무차원, 수간유하우 깊이(mm)/체적(L).

# 원 구현 범위
grass stemflow 실험식, infiltration/erosion numerical engine 미포함.

# 고운사 활용
억새 SF=0 가정은 부적절하다는 근거.

# 새로운 coupling
SF를 포기 위치의 공간 물공급원에 배당하고 침투 및 침식에 연동.

# 한계와 판정
실물 Miscanthus sinensis가 아닌 모사 포기 실험. 원문 수식 미검증. 부분 채택.
