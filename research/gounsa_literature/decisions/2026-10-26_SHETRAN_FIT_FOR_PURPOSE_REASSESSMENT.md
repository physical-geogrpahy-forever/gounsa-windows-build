# SHETRAN 원형 및 공개 4.7.2: 고운사 유수침식 엔진 채택 적합성 판정 재검토

일자: 2026-10-26. **결정: 고운사 주 유수침식 및 세류 지형발달 엔진에서 SHETRAN을 제외. 유역 수문/출구 유사유출에 관한 보조 검토 대상으로만 유지.** 이는 SHETRAN 전체가 무효한 모델이라는 뜻이 아니다.

## 왜 이 검토를 했는가
종전 작업은 원본 Fortran 컴파일과 임의 강우의 숫자 출력 성공을 과학적 타당성 검증처럼 소개했다. 고운사 연구의 필요조건보다 빌드와 매개변수 민감도 실험을 앞세우고, 약 12시간의 연구 우선순위를 잘못 사용했다. 실험을 추가하지 않고 발표된 검증의 대상변수와 적용환경, 원본 코드 구조, 현대 버전과의 검증 격차를 확인한다.

## 모델 구별
- **SHESED/SHETRAN 모형 계열이 peer-reviewed 유량 및 출구 유사유출 검증을 받은 사실**과, **2026 공개 SHA cf9cd540add78ad3accbaf62b4199d2032887f6b의 상세 수치 구현 검증 완료**는 다른 주장이다.
- 원본 SHESED는 catchment-scale process-based sediment transport/rainfall detachment/overland detachment/channel armouring을 다루며, **hillslope rilling 없음**을 Wicks & Bathurst (1996) 초록 자체가 명시한다.
- 2019년 검증연구 원문도 hillslope flow를 넓은 격자에 평균된 sheet flow로 계산, rill/gully concentrated flow 아님, 유수박리계수 Kf가 sheet와 rill의 미해상 효과를 실효적으로 대표할 수 있음을 명시한다. 실효계수가 rill의 위치/발달을 계산한 것과 동일하지 않다.

## 발표된 실증 결과와 한계
| 문헌 | 데이터와 방법론 | 검증 성과 | 고운사 목적의 한계 |
|---|---|---|---|
| Wicks, Bathurst & Johnson (1992) | 32.54 m² 강우모의 포장, 경운/예취/방목 구분, 박리계수 보정 | 대분류 처리는 반영하나 피복 내 세부 변화 미흡; 건조상태 유출 오차, 유량 보정 중요, 실험실 계수 전이 불신을 저자 언급 | 산불 사암 경사면 및 현장 세류 위치 예측 검증이 아님 |
| Wicks & Bathurst (1996) | 미국 Iowa 5.1ha 및 6.4ha 농업유역 사건 유사유출, Wyoming 3.3km 하도 37일 | 유사유출 시계열 및 크기의 일부 재현, peak 시점 차이 | **rill 미구현**, TLS 기반 격자별 DEM 변화 검증 없음 |
| Lukey et al. (2000) | 프랑스 Draix 86ha 황무지/108ha 재조림 유역 5년 비교 | 두 유역 runoff/rainfall ratio, sediment yield 두 자릿수 규모 차이 재현 | 보정계수 불확실성 큼, 국지 산불 후 세류 발달과 뿌리구조 검증 아님 |
| Op de Hipt et al. (2017) | 부르키나파소 Dano 출구 유사부유량 관측 기반 시기분리 보정/검증 | sediment NSE 0.4(보정), 0.2(검증); KGE 0.3 및 0.01, R² 0.47 및 0.37 | 검증기간 sediment 성능 논문 스스로 불만족, 공간적 박리/퇴적 검증 아님 |
| Escobar-Ruiz et al. (2019) | 영국 농업 Blackwater 18km² 4년 15분 관측 보정 → 인접 Kit Brook 22km² 독립 전이시험 | 유량 NSE 0.78/0.60, 사건별 sediment yield 평균 절대 백분율 차이 106%/298%, sediment peak 86%/438%; DEM 해상도에 event peak와 duration 민감 | 낮은 sediment prediction transferability, rill 미명시 및 식생/토양보호 미동적 |

모든 성능값은 **해당 논문·해당 환경**의 관측변수와 실험 구성을 함께 인용해야 하며, 고운사의 모델 NSE로 사용하면 안 된다.

## 고운사 연구의 필요조건과 판정
| 기준 | SHETRAN 원본 판정 |
|---|---|
| 공개된 Fortran 원본 및 reproducible build | **통과**. 소스와 의존성 고정, native Cobres 시험 성공 |
| 실제 field observed sediment에 대한 학술 검증 이력 | **부분 통과**. 연구는 있으나 유사 예측 오차 큼 |
| 2D 격자별 표면유동 | **통과(제한적)**. 공간격자 4 face 기반 확산파, full 2D SWE 아님 |
| 급경사 산불 후 사암 산림에서 현장 국지 침식량 검증 | **근거 없음** |
| 유량 변화에 따른 rill 자동 발생, 심화, 위치의 지형변화 | **불충족**. 원래 hillslope sheet flow 'without rilling' |
| 식생량(RLD/biomass/litter)에 따라 유수박리가 정량적으로 억제 | **불충족**. 핵심 flow detachment DF에는 직접적 뿌리/피복량 기반 계수 없음 |
| 잔존 토심, bedrock 노출과 암편 공급/피복 자동 모형 | **불충족** |
| 강우사상 내 자율 DEM feedback | **불충족**. 별도 event-boundary integration은 새로운 coupling |
| sediment 성분 전체의 외부 독립 질량수지 검증 | **미확인**. 현 공개 코드 BALSED는 빈 함수 |
| 2026 SHA와 과거 논문 검증 구성의 수치동등성 테스트 | **미확인**. 코드만 맞춰 컴파일한 것은 verification/validation이 아님 |

## Cobres native 실험 판정 정정
- 앞선 [native 5강도 시험](2026-10-26_SHETRAN_472_NATIVE_COBRES_RAIN_QA.md)의 10/20/30/40/50 mm/h 강우는 **원래 1977–1977 Cobres 2 km 격자 예제 파일을 임의 강우로 재구성한 컴퓨팅 테스트**이다. 실제 기록된 현장 유사량과 짝지어 비교한 검증이 아님.
- 20 mm/h 3 h의 `s_v_er` 최대 67.26 mm/day는 순간 박리율, 시간별 coarse HDF5를 적산한 최대 gross source detachment 약 6.77 mm는 정확한 내부 timestep integral이 아님. 출구 순토양유실과 다름. 두 숫자는 모형이 현장에서 성립한다고 입증하지 않는다.
- [process isolation](2026-10-26_SHETRAN_20MMH_DETACHMENT_DECOMPOSITION.md)에서 특정 파라미터를 0으로 만드는 것은 **식을 켜고 끄는 smoke test**다. 물리적 계수 적합성 혹은 모델 유효성 시험이 아니다. 이 실험을 고운사 모델 선정 근거에서 배제한다.
- 2km DEM의 시각별 과장 가능성과 시각 0 sediment 초기화, 첫 step sediment 경계, 적응 timestep 끝시각 overshoot, 2026 소스 BALSED 문제도 별도로 있어 계산 숫자 자체를 관측과 비교하기 전 신뢰할 수 없다.

## 결론과 이후 연구 우선순위
1. **SHETRAN을 고운사의 주 '세류 발생-세류 침식-시간별 국지 지형변화' 엔진 후보에서 제외**한다. 이는 구현 결함을 패치하기만 하면 해결될 일이 아니라 원천 수리/침식 과정 모형의 목적 제한이다.
2. SHETRAN은 canopy interception 및 basin-scale hydrology/sediment routing 비교용으로만 근거 사용 가능. 다만 통합 시 SWEHR와 수문 및 박리 중복을 막을 coupling 분리가 필요하다.
3. 기존 SWEHR 등 다른 후보에도 **모델 적합성 게이트**를 동일하게 적용한다. '실제 오픈소스'+'동일 버전 컴파일'+'국지 산지 검증'+'강우 및 유수박리 분리'+'rill/DEM feedback'+'RLD/litter+rock'+'물/유사수지'를 PASS, PARTIAL, FAIL 구분하고 실제 원문과 원본 함수/시험으로 확인할 것. 검증 안 된 모델에 강우강도 민감도/교정을 먼저 수행 금지.
4. 복잡한 일체형 후보가 없다면 원본의 장점을 활용하는 **새 coupling**인 점을 분명히 하고 과정별 검증/보존법칙을 설계. 원본이 제공하는 기능으로 포장하지 않는다.

## 자료
- https://doi.org/10.1061/(ASCE)0733-9437(1992)118:5(708)
- https://doi.org/10.1016/S0022-1694(96)80012-6
- https://doi.org/10.1016/S0022-1694(00)00260-2
- https://doi.org/10.3390/w9020101
- https://doi.org/10.1002/hyp.13550
- Original pinned code: https://github.com/nclwater/Shetran/tree/cf9cd540add78ad3accbaf62b4199d2032887f6b
- Current source `src/sediment/SYmod.f90`: original detachment `DF = GKF*(1-FCROCK)*max(0,τ-τc)/τc`, vegetation ground cover `FCG` enters rainfall DR directly but flow DF not directly. 2026 `BALSED` placeholder.
- Existing native Cobres source execution archived as *software smoke tests*; field validation not established.
