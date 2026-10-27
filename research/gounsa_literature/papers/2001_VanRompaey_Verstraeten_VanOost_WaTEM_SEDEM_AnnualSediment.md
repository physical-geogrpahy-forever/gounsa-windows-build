# 서지정보
Van Rompaey, A., Verstraeten, G., Van Oost, K., Govers, G., & Poesen, J. (2001). Modelling mean annual sediment yield using a distributed approach. Earth Surface Processes and Landforms, 26(11), 1221–1236. https://doi.org/10.1002/esp.275

# 이 논문을 찾은 이유
독립 원본 공개 모델 WaTEM/SEDEM을 고운사의 강우사상별 2D 침식·퇴적 후보로 검증한다.

# 연구 유형
동료심사 공간분포형 연평균 침식량 및 유사유출량 모형. KU Leuven 공식 개발자 문서와 현존 Free Pascal 코드를 확인. 원논문 전체 PDF와 보정자료는 이번 세션에 열람되지 않았다.

# 공간 구조
DEM 격자별 경사와 길이를 계산하고, 한두 하류 격자에 유사를 분배하는 다중 흐름방향 알고리즘. 자유로운 2차원 동역학 천수방정식이 아니다.

# 적용 환경
벨기에 농경지와 유역의 연평균 침식 및 퇴적. 5~10cm 산림사면의 6시간 강우 모의가 아니다.

# 핵심 과정
RUSLE로 총침식량을 계산한 다음, 유입 유사량과 격자별 수송능력을 비교하여 순침식, 순퇴적 및 하류 유사송출량 산정.

# 식생 입력
RUSLE의 작물 및 관리 C 계수, 피복도 관련 보정. LAI 기반 수관저류, 통과우 및 낙수 운동에너지 계산은 확인되지 않음.

# 핵심 식
E = R × K × LS × C × P, 연평균 토양손실량 [kg/ha/yr].
S_out = min(S_in + E, TC), 동일 단위로 환산한 후 사용. 공식 문서에서는 내부적으로 격자별 부피로 환산함.

# 파라미터와 단위
R 인자 [MJ mm/(ha h yr)], E [kg/(ha yr)], TC 문서의 격자 전달능력. 실제 발표 5cm 시공간 격자 및 수치수렴 자료 미확보.

# 원 논문의 구현 범위
연평균 공간분포형 유사 송출 및 퇴적 모델. 후속 공개 코드 버전 5.0.1 (2024) https://doi.org/10.5281/zenodo.10997288 은 역사적 2001년 실행코드와 동일하다고 단정하지 않음.

# 고운사에 직접 사용할 수 있는 부분
공개 소스의 격자별 순침식과 퇴적 비교. 강우사상 중 수관차단 변화나 유출속도는 직접 모의하지 못함.

# 필요한 새로운 coupling
동적 수관저류, 초단위 2D 수리계산, 강우충격 박리와 별도 유사연속방정식 도입은 기존 WaTEM/SEDEM에 없는 신규 결합임.

# 한계
유역 연평균모형이며 실제 5cm와 단일 강우사상의 침식수지는 검증되지 않았다. 원논문 상세식 직접 전사 범위 제한. 원본 실행시험 수행하지 않음.

# 최종 판정
장기 공간퇴적 보조근거. 고운사 초고해상도 단일 강우사상 주모델 탈락.

# 참고 링크
https://doi.org/10.1002/esp.275
https://github.com/watem-sedem/watem-sedem
https://ees.kuleuven.be/en/geography/modelling/erosion/watem-sedem
https://watem-sedem.github.io/watem-sedem/watem-sedem.html
