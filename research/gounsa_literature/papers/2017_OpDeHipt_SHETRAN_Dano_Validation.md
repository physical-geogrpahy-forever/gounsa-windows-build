# 서지정보
Op de Hipt, F., Diekkrüger, B., Steup, G., Yira, Y., Hoffmann, T., & Rode, M. (2017). Applying SHETRAN in a tropical West African catchment (Dano, Burkina Faso)—Calibration, validation, uncertainty assessment. *Water, 9*(2), 101. https://doi.org/10.3390/w9020101

# 이 논문을 찾은 이유
독립적인 유량 및 실제 부유사 관측을 이용한 SHETRAN 유사모형 검증의 정확도가 어느 정도인지 확인.

# 연구 유형
유역 수문 및 침식의 보정, 검증, 관측과 모수 불확실성 분석. **원문 웹 전체/초록과 결과 [A/B] 검토**.

# 공간 구조
분포형 유역 격자, 출구 유량 및 부유유사 관측. 개별 세류 지형변화 고도 차분 검증은 아님.

# 적용 환경
부르키나파소 Dano 지역, 열대 서아프리카. 고운사 급경사 산불 후 사암지와 다름.

# 핵심 과정
수문 보정 후 유사량 분석. 유사량 모델 NSE 보정 0.4, 검증 0.2; KGE 보정 0.3, 검증 0.01, R² 보정 0.47, 검증 0.37(출판사 본문 3.3.2). 논문은 검증기간 품질이 불충분하다고 자체 언급. 수문 보정/검증의 R², NSE, KGE는 0.66–0.79 범위.

# 식생 입력
LULC와 파라미터 대응. 개체목 뿌리량 및 litter 질량의 동적 효과나 미시 세류 발달 검증은 확인되지 않음.

# 핵심 식
SHETRAN 기존 flow erosion, rainfall detachment 및 sediment routing. 논문은 침식량이 kf, kr, BKB, DLSMAX에 민감하다고 보고.

# 파라미터와 단위
k_f, k_r, BKB, DLSMAX 등이 주요 민감도 변수. 연구 논문의 최적 보정값을 고운사에 복사하는 것은 부당.

# 고운사에 직접 사용할 수 있는 부분
독립 침식량 검증을 요구해야 한다는 사례와 반례.

# 필요한 새로운 coupling
세류 및 암편 피복과 기상 작용, 층별 토심, 식생 생체량, 내부 공간별 DEM 차분 검증.

# 한계
입력/관측 오차가 커 보정/검증 자료 불확실성 범위를 넘어서는 예측도 있었음. 종속변수는 출구 중심 SSL. 실제 격자별 침식량 검증을 보장하지 않음.

# 최종 판정
**주의 근거**: SHETRAN 침식이 다른 환경에서는 검증 예측성이 낮음. 최종 엔진 채택 보류가 타당.

# 참고 링크 / DOI
https://doi.org/10.3390/w9020101


## 2026-10-27 SHETRAN 주모델 선정 이후 판정 정정
- SHETRAN 4.7.2는 [이번 결정문](../decisions/2026-10-27_SHETRAN_SELECTED_AS_GOUNSA_SINGLE_STORM_EROSION_ENGINE.md)에 따라 **고운사 단일강우 유수침식 주모델로 선정 완료**. 이 논문의 예전 '최종 모델 채택 보류' 서술은 당시 연구 상황을 기록한 과거 판정이며, 새 결정 이후 모델 미선정의 근거로 사용할 수 없다.
- 이 논문의 실제 검증범위(실험사면/유역 외부 유사량 또는 격자 내 퇴적, 예전 SHESED 및 당대 SHETRAN 버전)는 유지하고, SHETRAN 4.7.2 고운사 현장 검증 완료라는 주장으로 확대하지 않는다.
