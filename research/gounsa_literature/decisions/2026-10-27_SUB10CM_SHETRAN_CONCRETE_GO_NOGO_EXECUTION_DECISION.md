# 2026-10-27 고운사 5–10cm 단일 수관침식 원본: 즉시 실행 GO/NO-GO 절차

## 최종 행동결정
- 신규모델 나열과 동일 연구 재검색은 **일단 중단**. 단일 공개 원본 중 실제 수관/적하+직접우/유수박리+4면 유사이송을 컴파일·실행한 **SHETRAN 4.7.2**, 원본 SHA `cf9cd540add78ad3accbaf62b4199d2032887f6b` 를 **최우선 5–10cm 적합성 시험 엔진**으로 둔다. 이것은 **5cm 사용이 검증되었다는 판정이 아니며, 기존에 확인되지 않은 published 5cm 선례가 생겼다는 주장도 아니다**.
- 이미 수행한 4m/0.648ha 35개 원본 계산은 정상종료/물-유사 경계배출/전역 보존식을 확인했으나 **국지 141.487mm 퇴적, k=50 미보정, 토심 한계, 공간수렴**은 미해결. 10cm 확장에 앞서 이 사항을 실험 기준으로 한다.
- **SHETRAN 5–10cm가 재현성/공간·시간 수렴을 통과하지 못하면 본 모델의 5–10cm 정량 예측 용도를 보류한다.** 미검증 LISEM7.5.2 (대형 dt 비수렴), 현재 깃허브 신형 LISEM 2022 canopy/splash path 문제, TREX/LUCIA/ASTERIX 등을 대신 무검증 채택하지 않는다.

## 1. 원본과 실행환경 보존
- 물리 수식의 편집 금지. upstream 원본과 진단용 출력/array-capacity 만 변경한 파생 build를 모두 고정 SHA로 기록. workflow 및 원본 파일 checksum, compiler, 실행환경, 파라미터의 단위, 데이터 해시 기록.
- 원본 선행 아티팩트: [35회 실행](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40455147463), `experiments/shetran_large_patch_matrix_20261027.py` 및 `experiments/shetran_open_all_sides_native_20261027.py`.
- 현재 생성기는 **NX=17 NY=29 DX=4.0 ACTIVE 405 hard-coded**; 여러 29행/405셀/row split 고정. **DX=0.1만 대입하는 것은 동일영역 초고해상도 모의가 절대 아니다**. 물리적으로 동일한 연속 지형, 물성, 식생 patch 및 강우를 각 resolution에서 rasterize하는 별도 resolution-aware runner가 필수다.

## 2. 단계 A: 20m×20m 작은 패치에서 native 5–10cm 가능성 선판정
- **동일한 실물 20m×20m**의 고정 경사 및 연결지형/식생 경계(연속좌표)와 개방경계 설계.
- DX=1.0/0.5/0.2/0.1/0.05m, 물리 유효셀수 각각 **400/1600/10000/40000/160000**. 바깥 일종의 ghost/경계셀을 포함해도 250,000 NELEE 기본상한 미만인지 반드시 카운트. 강우=20 및 50mm/h (각 3시간) 최소; canopy ON/OFF, bare/grass/oak/mixed 포함. 우선 0.1m와 0.05m는 1분/5분 단기 입력 강우로 네이티브 smoke와 물리단위 검사를 거쳐 통과시 3시간 전사상 모의. `TMAX` 실제 step 한계를 바꿔 시험하고 `PMAX`는 변경하지 않는다.
- 진행 중 출구 물/유사량, native 물-유사 mass ledger, 누적 박리, 표층 이동가능 토사량과 원토양 재고, 최대 국지 퇴적 깊이를 저장.
- SHETRAN에서는 **사상 중 침식 결과가 DEM 유동격자에 즉시 재투입되지 않는다**. 이 한계를 5cm라고 없어졌다고 하지 않는다.

## 3. 사전등록 GO/NO-GO 지표 (engineering screen, field calibration 아님)
**FATAL / NO-GO**
- native crash/nonfinite/음수 불가능 상태; 물/유사수지 시간 내 재구성 불가; 물리적으로 가용한 원토양+공급유사를 초과한 세포별 박리량; timestep 절반으로 줄여도 매번 심한 수치증폭; 출구 없는 오해된 경계; 상승량을 입력원 없는 생성유사로 설명.
**사전 수치 목표 (대상 문제에 맞춰 사전 고정할 진단 기준, 보편적 학술 표준값이 아님)**
- 시간 단계 절반과 비교 시 전체 사상 유출량 차이 **≤5%**, 경계 총 유사배출량 및 총 원토양 박리 차이 **≤10%**, 물·유사 연속방정식 상대 closure **≤0.1%**(매우 작은 거의0 유사량은 분모를 명시해 절댓값 함께 보고). 실패하면 step 추가/재검토. 검증 시 데이터 관측 적합도와 별개.
- 공간격자 수렴 판정은 **같은 연속지형/패치/강우/토양 물성**의 도메인 총량과 aggregation한 `Δz` 패턴을 비교; 셀 최대값 단독 비교는 해상도 효과가 크므로 별도. 특정 5cm/10cm 허용오차는 장기 노이즈 대신 누적 모의총량/지형 모양 비교를 이용해 사전에 추가 등록.
- canopy ON/OFF 실험에서는 LAI 및 수관저류만 toggled, 고정 ground cover/roughness/infiltration/soil erodibility을 유지해 canopy causal effect 분리; vegetation 차이는 별도 팩터 비교.
- 동서남북 Type5 `Q=50h²`의 k=50은 기존 **가상 임의 계수**이므로 그대로 현장결론 쓰지 않는다. 조건을 선행 sensitivity하여 변경물리동일성, 물/유사 export 확인, 정상수심 또는 측정자료에 근거한 경계조건 선정. 사방 자유 배출은 **4방향 각각의 유출을 강제**하는 의미가 아님.

## 4. 단계 B: 10cm 가용성 통과 후 0.648ha 전체 적용
- 6480m² / (0.10m)² = **648000** active cell. 5cm이면 **2592000** active cell. upstream `NELEE=250000`과 ghost/채널 포함 수가 모자라므로 capacity/memory 구조 변경과 필요시 NXEE/NYEE 검증. 단순 배열 확장 자체는 수치검증을 의미하지 않음.
- before capacity change vs after capacity-only change **동일한 4m/1m 테스트의 결과 일치** 필수. 첫 전역 실험은 10cm, 5cm 전역은 해당 수렴/메모리 요구를 따로 검증한 뒤 시도.
- synthetic 먼저, 실측 드론 DEM 및 식생배치, 토양두께/암편/낙엽층, LAI, 강우/유출/DoD 제공 후 관측 적합성 별도 검증. **5cm 모델 실증 선행연구가 SHETRAN에 있다는 근거는 현재 없음**.
- 비용/시뮬레이션시간이 불합리하거나 공간수렴 실패한다면 5cm DEM 관측을 유지하고 계산격자(≤0.5m 등을 가정하지 말고) 유효해상도를 과학적으로 새로 정한다. 5cm 원자료와 coarser 물리격자 출력을 동일해상도 모형결과라고 표기 금지.

## 모델 재선정에 대한 명확한 종료조건
- SHETRAN 단계 A 5cm와 10cm에서 native mass/timestep/soil-stock 기각이면 그날의 답은 **'5~10cm에서 현행 공개 단일모델 사용 불가'**이다. 다른 문제 있는 원본을 채택하지 않고 현재 결과/한계를 공유한다.
- 10cm만 통과 시 10cm부터 stage B 수행, 5cm는 미검증 상태 유지.
- 5cm와 10cm 모두 통과해도 published 5cm SHETRAN precedent가 생기는 것이 아니라 이번 연구의 새 검증 결과다.

## 중요: 이번 기록 자체가 실험 성공은 아님
이 문서는 실행 프로토콜만 작성했으며 **5cm/10cm 실행, 컴파일, 네이티브 mass ledger, 적용 가능 판정 아직 실시하지 않음**. 실제 결과가 나온 후 이 결정문에 링크한 원본 output으로 판정할 것.
