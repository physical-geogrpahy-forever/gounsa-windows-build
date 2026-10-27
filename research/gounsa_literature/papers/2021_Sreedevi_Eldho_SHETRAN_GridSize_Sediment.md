# 서지정보
Sreedevi, S., & Eldho, T. I. (2021). Effects of grid-size on effective parameters and model performance of SHETRAN for estimation of streamflow and sediment yield. *International Journal of River Basin Management, 19*(4), 535–551. https://doi.org/10.1080/15715124.2020.1767637 (온라인 선행 게재 2020)
# 이 논문을 찾은 이유
4m/2m/1m 격자 검증의 필요성과 매개변수 해상도 의존성을 SHETRAN 자체 연구에서 확인.
# 연구 유형
인도 Netravathi 유역의 1km, 2km, 4km 격자 SHETRAN 유출/유사 검증, 해상도별 모수 전이 및 재보정 실험. 학술지 초록 확인.
# 공간 구조
분포형 유역 모형, 1km/2km/4km 격자 비교(고운사 m 단위 사면보다 훨씬 조대함).
# 적용 환경
인도 습윤열대 유역.
# 핵심 과정
2km에서 보정한 매개변수를 1km/4km에 전이하고 월 유량 및 유사량 모형성능을 검사, 보정을 반복하여 격자에 따른 침식계수 민감도 분리.
# 식생 입력
토지피복/유역 입력; 개별 나무 LAI 시나리오 확인 아님.
# 핵심 식
SHETRAN 동일 수문/유사 계산식에 입력 격자와 유효 매개변수 변화 실험.
# 파라미터와 단위
1km/2km/4km; 격자 세분화시 overland/channel erodibility 보정값 감소; 유사량은 모수 재보정 없으면 악화. 해당 유역은 1km가 최선의 실용 해상도라고 보고.
# 원 논문의 구현 범위
인도 Netravathi 유역의 1km, 2km, 4km 격자 SHETRAN 유출/유사 검증, 해상도별 모수 전이 및 재보정 실험. 학술지 초록 확인.
# 고운사에 직접 사용할 수 있는 부분
상세 격자를 쓰기만 해서는 예측이 자동 개선되지 않으며 공간수렴과 parameter portability를 따로 검사해야 함을 입증.
# 필요한 새로운 coupling
고운사 4m→2m→1m 동일 영역 수치/출력 안정성과 관측보정 분리 실험.
# 한계
유역과 공간해상도가 고운사의 4m급 사면과 다르므로 최적 1km 결과를 그대로 대입하지 않음.
# 최종 판정
**고운사 격자 민감도 실험 설계의 직접방법론 근거**.
# 참고 링크 / DOI
https://doi.org/10.1080/15715124.2020.1767637

## 원본 코드 계보 관련 주의
이 문헌은 기존 SHE/SHESED/SHETRAN 물리식의 논문 또는 응용 사례로서, 2026-10-12 GitHub 원본 SHETRAN 4.7.2 commit cf9cd540add78ad3accbaf62b4199d2032887f6b와 **바이너리/소스 동일한 버전을 사용했다는 뜻이 아님**.
