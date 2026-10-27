# 서지정보
Escobar-Ruiz, V., Smith, H. G., Blake, W. H., & Macdonald, N. (2019). Assessing the performance of a physically based hydrological model using a proxy-catchment approach in an agricultural environment. *Hydrological Processes, 33*(24), 3119–3137. https://doi.org/10.1002/hyp.13550

# 이 논문을 찾은 이유
SHETRAN 침식모형의 **독립 유역 전이 예측성능**, 유사유출 예측오차, 격자 크기와 명시적인 세류 처리 여부를 실제 원문에서 검증.

# 연구 유형
수치모형의 농업 유역 현장 관측 보정 및 독립 proxy-catchment 검증. **전체 공개 HTML 원문 [A] 확인**.

# 공간 구조
영국 Blackwater 유역 18 km²에서 보정, 인근 Kit Brook 22 km²에서 별도 평가, 50×50m 격자, 15분 관측자료 4년. 인공강우 계산시험 아님. SHETRAN 자체는 grid sheet flow, 하도 link.

# 적용 환경
농업 토지피복: Blackwater 대략 초지 60%, 경작지 27%, 낙엽활엽림 12%, 도시 1%. 산불 후 산림 토양 깊이 감소 검증 아님.

# 핵심 과정 및 검증 결과
유량 NSE 보정 Blackwater 0.78, 독립 유역 Kit Brook 0.60.
사건별 관측 대비 평균 절대 백분율 차이: Blackwater Q volume 30%, Q peak 41%, sediment yield 106%, sediment peak 86%; 독립 Kit Brook Q volume 48%, Q peak 66%, sediment yield **298%**, sediment peak **438%** (원문 abstract).
논문은 유량 재현은 상대적으로 낫고 퇴적물 플럭스 예측이 약하다고 평가; 홍수 및 sediment 사건 peak/duration이 DEM grid size에 매우 민감함.
SHETRAN 지표유출은 rill이나 gully 같은 concentrated flow가 아니라 **격자 평균 sheet flow**로 계산한다고 원문 2.1 명시. K_f가 sheet+rill 효과를 합쳐 나타내는 empirical effective parameter 성격임.

# 식생 입력
LULC별 canopy와 soil properties, soil cover 및 parameters. 내장된 동적 뿌리량 기반 박리 저항 또는 수관하층 집락 천이 표현은 논문에서 입증되지 않음.

# 핵심 식
원본 연구 계열 K_f, K_r 기반 박리 및 격자 표면수 transport. K_f의 임의 수치 보정을 고운사 적용 가능 근거로 삼을 수 없음.

# 파라미터와 단위
문헌에서 K_r ≈ 0.05–70 J^-1, K_f ≈ 5×10^-7–2×10^-5 kg m^-2 s^-1 범위 보고. 이 범위는 여러 적용 연구의 차이이며, 고운사의 검증된 현장 입력 범위는 아님.

# 고운사에 직접 사용할 수 있는 부분
유역 유량 수문모의와 유사유출 검증의 분리 기준. 원본 SHETRAN의 검증 한계 정량적 근거.

# 필요한 새로운 coupling
rill network 형성/발달, 실제 지형 고도 feedback, 표층 토심, 암편, 뿌리 생체량에 따른 detachment 저감 및 sediment-state restart.

# 한계
원문은 현장 검증을 갖지만 land-use transfer 시 유사예측 정확도 불량. 검증 내용이 수문/출구유사 중심이라 국지 지형변화를 입증하지 않음. 2019 버전의 결과를 2026 공개 4.7.2에 그대로 동일시 금지.

# 최종 판정
**주요 반증근거**: SHETRAN은 보편적으로 정확한 침식 엔진이라고 주장할 수 없음. 특히 고운사 세류 지형발달 주엔진 사용에 부적합.

# 참고 링크 / DOI
https://doi.org/10.1002/hyp.13550


## 2026-10-27 SHETRAN 주모델 선정 이후 판정 정정
- SHETRAN 4.7.2는 [이번 결정문](../decisions/2026-10-27_SHETRAN_SELECTED_AS_GOUNSA_SINGLE_STORM_EROSION_ENGINE.md)에 따라 **고운사 단일강우 유수침식 주모델로 선정 완료**. 이 논문의 예전 '최종 모델 채택 보류' 서술은 당시 연구 상황을 기록한 과거 판정이며, 새 결정 이후 모델 미선정의 근거로 사용할 수 없다.
- 이 논문의 실제 검증범위(실험사면/유역 외부 유사량 또는 격자 내 퇴적, 예전 SHESED 및 당대 SHETRAN 버전)는 유지하고, SHETRAN 4.7.2 고운사 현장 검증 완료라는 주장으로 확대하지 않는다.
