# 서지정보
Charlier, J.-B., Moussa, R., Cattan, P., Cabidoche, Y.-M., & Voltz, M. (2009). Modelling runoff at the plot scale taking into account rainfall partitioning by vegetation: application to stemflow of banana (Musa spp.) plant. Hydrology and Earth System Sciences, 13, 2151–2168. https://doi.org/10.5194/hess-13-2151-2009

# 이 논문을 찾은 이유
수간유하우가 국지적으로 집중될 때 토양침투능이 높은 사면에서도 지표유출이 시작되는 원리를 수치모형으로 검증했는지 확인.

# 연구 유형
과정 기반 개념적 분할구획 수문모형 + 사건별 유출 실측 검증.

# 공간 구조
수간유하 집중 영역과 나머지 영역의 두 구획을 가진 lumped plot model, MHYDAS 유출 발생 및 diffusive-wave 전달. 2D 유동 아님.

# 적용 환경
과들루프 바나나 포장 3,000 m², Andosol Ks 평균 75 mm/h. 18개 홍수사상, 10~140 mm 사건 강우량.

# 핵심 과정
식생의 줄기기부 강우 재분배, 구획별 infiltration-excess runoff, diffusive-wave 유출 수문곡선. stemflow 전용 계수 도입.

# 식생 입력
stemflow redistribution coefficient, 바나나 줄기 집중 특성. 완전한 3D 관목 생리모델 아님.

# 핵심 식
stemflow 구획화 + 수문 생성/전달 함수. 원문 전문 수식을 이 기록에서 모두 대조하지 않았으므로 임의 식을 발명하지 않음.

# 파라미터와 단위
Ks [mm/h], stemflow coefficient [-], diffusive-wave parameter (개별 정의 원문 참조).

# 원 논문의 구현 범위
수간유하에 따른 국지 침투 및 지표유출 재현, 18건 hydrograph 비교. 토사박리, 토사수송은 미구현.

# 고운사에 직접 사용할 수 있는 부분
동일 총 순강우라도 줄기기부 집중으로 유출 생성이 달라질 수 있다는 published coupling precedent.

# 새로운 coupling이 필요한 부분
TLS 식생구조에서 각 줄기별 SF(t) 및 분포함수, 2D 지표유출 경계조건, raindrop/flow-driven erosion.

# 한계
바나나 단일 재배식생, 2구획, 산지·산불·2D 미검증. 수간유하우가 항상 runoff를 증가시키는 것은 아님.

# 최종 판정
핵심 근거 채택(수간유하우→침투/유출 연결), 최종 침식엔진 아님.

# 참고 링크 / DOI
https://hess.copernicus.org/articles/13/2151/2009/
