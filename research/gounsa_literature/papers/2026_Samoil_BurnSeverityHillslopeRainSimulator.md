# 서지정보
Samoil, M., Owens, P. N., Ali, F., et al. (2026). The effects of soil burn severity and slope steepness on post-wildfire hillslope runoff and soil erosion using a portable rainfall simulator in British Columbia, Canada. *Journal of Soils and Sediments, 26*, article 19. https://doi.org/10.1007/s11368-026-04226-8

# 이 논문을 찾은 이유
강우사상 규모의 실제 g/m² 침식량을 t/ha/event로 올바르게 환산해 원본 침식모델 출력을 선별하기 위해.

# 연구 유형
현장 인공강우. 수치모델 아님.

# 공간 구조
시험구 단위, 불연소 n=5, 중간강도 n=10, 높은 연소강도 n=8; 산지 경사 범주 비교.

# 적용 환경
British Columbia 산불사면. 고운사 사암 및 억새-맹아와 다른 환경.

# 핵심 과정
185±17.1 mm/h 인공강우를 30분 가함(평균 약 92.5 mm 강우), 유출량과 침식량 측정. 비연소 1.78±1.59 g/m², 중간 연소강도 105±129 g/m², 높은 연소강도 529±347 g/m² (0~30분). 무차원 통계 비교 및 토양 표면 노출 등 해석.

# 식생 입력
표면 유기물과 노출 토양/연소강도 상태. 정량 루트 연계 침식모델 아님.

# 핵심 식
1 g/m²=0.01 t/ha이므로 시험구 평균값 각각 0.0178, 1.05, 5.29 t/ha/30-min event. 실측 평균이고 임의 10~50 mm/h의 예측 아님.

# 파라미터와 단위
강우강도 mm/h; 침식 g/m²; 유출 mm; n=5/10/8.

# 원 논문의 구현 범위
실측 강우 및 토사 산출; process model의 절대예측 오차 검증자료 아님.

# 고운사에 직접 사용할 수 있는 부분
모형 침식 단위 검증과 산불강도에 따른 실제 수치 범위 비교.

# 새로운 coupling이 필요한 부분
고운사 DEM/토양/식생 입력과는 독립 현장 대조. 값 재활용 금지.

# 한계
185mm/h 30분의 매우 강한 강우, 타국 토양, 산림 종류, 실제 현장차이. 결과의 유효한 입력범위가 10–50 mm/h 1시간과 같지 않음.

# 최종 판정
현장 대조 기준 채택.

# 참고 링크 / DOI
https://doi.org/10.1007/s11368-026-04226-8
