# 2026-10-27 19:40 고운사 5~10cm 이제부터 실제로 무엇을 할 것인가
## 이번 세션 결정
관련 `SYSTEM.md`, `MASTER.md`, `INDEX.md`, 기존 SHETRAN 4.7.2 선정/0.648ha 35회 native, 5~10cm 제한/LISEM7.5.2 유사수렴 실패, 스크립트 원본을 읽고 결론. 새로운 모델 열거 중지. **SHETRAN 4.7.2를 20×20m 동일 가상사면 1/0.5/0.2/0.1/0.05m 실제 격자로 시험**하고 시간수지, 물/유사수지, 물리적 토사재고, 공간수렴 여부로 GO/NO-GO 내기로 함.

## 실제 확인한 코드 제한
`experiments/shetran_large_patch_matrix_20261027.py` 는 `NX=17 NY=29 DX=4.0 ACTIVE 405`, 경계 스크립트도 17,29, 80 open boundary count 고정. 단지 DX=0.1 대입하면 5cm/10cm 실험 안 됨. **스케일에 독립적인 격자생성/고도/식생 패치/경계 및 출력 처리**를 새로 작성하되 원본 SHETRAN physics unchanged. 기존 upstream `nclwater/Shetran@cf9cd540...` `NELEE=250000`, 0.648ha 10cm=648000, 5cm=2592000 active. 시험용 20×20m의 5cm 160000, 10cm 40000 active로 capacity를 넘지 않으므로 우선 작은 패치 시험이 적절.

## 우선 행동과 중단기준
- 5cm 및 10cm 작은 패치 정상실행 여부, canopy ON/OFF, bare/grass/oak/mixed, 20/50mm/h 단기 smoke 후 3h event. native TMAX/PMAX 구분.
- Type5 k=50 가상 경계는 평가용이며 현장교정 필요. 네 방향 각각 물/유사배출 diagnostic.
- 간격 절반 비교 총 유출량 변화 5%, 원토양 박리/유사 경계배출 10%, native mass closure 0.1% 사전 엔지니어링 선별기준으로 설정. 현장 타당성 확인을 의미하지 않음. local soil stock finite bound 필수, 141.487mm extreme deposit 설명/검증 전 현장결론 불가.
- 10cm 성공하면 array capacity-only 변경 전후 동일 기존 4m 출력 비교하고 전사면 10cm로 확대. 실패 시 같은 조건 충족했다고 주장하지 않음. 5cm는 별도로 판정, 성공하지 않았다면 10cm 결과로 과장 금지.

## 이번 세션 GitHub 저장
- `decisions/2026-10-27_SUB10CM_SHETRAN_CONCRETE_GO_NOGO_EXECUTION_DECISION.md` 상세 사전등록 실행 설계.
- 본 세션 파일. MASTER/INDEX 연결 성공 여부는 실제 commit으로 확인.
## 아직 실행하지 않은 것
new scale-aware generator, 실제 5cm native simulation, full 0.648ha 10cm compile/run. 계획문을 실제 실행 성공으로 쓰지 말 것.
