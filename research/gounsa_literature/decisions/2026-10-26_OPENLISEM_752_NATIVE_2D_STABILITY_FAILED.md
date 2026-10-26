# OpenLISEM 7.5.2 — 2026-10-26 실제 Windows 원본 2D 수치 안정성 재검증, NO-GO

검증 대상: 개발진 원본 OpenLISEM 7.5.2 Windows lisem.exe, 설치 프로그램 SHA256 f8a5722ed0b370f32fb3dae5c55465427abe75b1155b50bf12aa5516d6b4ca79.

## 실제 실행과 재현 자료
- 2026-10-26 원본 2D 전체 모델 12회 실행, exit code 0 및 native totals.csv, soilloss.map 확인. [Actions 실행 40304135775](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40304135775)
- Artifacts: openlisem-native-2d-1ha (artifact ID 12641931977), 622686B, 각 실행의 원본 runfile, totals.csv, soilloss.map, stdout/stderr 등 보존.
- 실행 코드: 실험 브랜치 openlisem-752-virtual-trial-20261023, workflow .github/workflows/openlisem-native-2d-feasibility.yml, SHA b8120b66aa60f3d84e8cecbea3f7c7d446f9bc98.
- 가상 100m ×100m 사면, 5m 격자, 경사 25%, 20mm/h 1시간 후 10분 배수, 억새/참나무 맹아 식생 가상 조건. 원본 2D 동수역학 Routing Kin Wave 2D=2, Flow Boundary 2D=1, Advanced Options=1, Deposition continuous=1, Deposition exponential=1.
- 원본 침전속도 알고리즘 기본식 SettlingVelocity=1 vs 대체식 SettlingVelocity=3. 변경된 포크가 아니라 7.5.2 원본 제공 선택지. 모든 입력 runfile에 정확한 엔진 키와 GUI 키가 모두 기록됐음을 ZIP에서 확인.

## 유사유출량 kg/ha (원본 네이티브 출력)

| 식생 | 원본 침전속도 선택 | Δt=5s | Δt=10s | Δt=20s |
|---|---|---:|---:|---:|
| 참나무 | 기본식 1 | 0.005993 | 123.037727 | 832.588686 |
| 참나무 | 대체식 3 | 0.030954 | 28.707586 | 268.530307 |
| 억새 | 기본식 1 | 0.004050 | 0.007095 | 238.256810 |
| 억새 | 대체식 3 | 0.018893 | 0.044177 | 88.121322 |

참나무 대체식은 5→10초에서 약 927배, 억새 대체식은 10→20초에서 약 1995배 차이. 동일 강우, DEM, 식생, 토양에서 수치시간간격에 따른 비수렴. 원본 대체 침전속도식도 문제를 해결하지 못함. 물 유출량 차이와 비교해 수백~수천 배의 유사유출 변동은 안정적인 연구 결과로 해석 불가.

## 물리적 보존 및 경계 검증
- 모든 12회 강우 출력 20.000mm. 출구/유역경계 물 배출량 참나무 5/10/20초 각각 12.283546/11.432688/10.013130mm, 억새는 11.000058/10.290903/8.961219mm. 즉 배출이 0이라서 침식 결과가 0인 잘못된 이전 시험과는 다름.
- 원본 ZIP에서 12개 totals.csv를 자체 재파싱: 강우−차단−침투−경계배출−지표류저장−침수저장−표면저장 물수지 잔차 절댓값 최대 약 0.0000052mm.
- 원본 집계 유사수지 (낙하박리+흐름박리+퇴적[음수]−잔류−유출) 잔차는 원본 totals.csv 반올림 자릿수 수준에서 0. **유사수지가 닫힌다는 사실은 시간간격 수렴이나 국지 토양저장량 보존을 보증하지 않음.**
- 참나무 기본식 Δt=20초 soilloss.map 최대 격자 순침식 약 5982.901t/ha. 가상 토심 0.25m, 건조 부피밀도 1350kg/m3의 초기 유한 토사저장량 3375t/ha 초과.
- 기존 v7.5.2 와 main_C GetSV 코드 100μm 분기 수식 오류, DetachMaterial 주석 처리 및 SwitchUseMaterialDepth=false도 현재 확인됨. 따라서 단순 공개 브랜치 변경으로 기존 오류가 수정됐다는 근거 없음.

## GO/NO-GO 판정
- 네이티브 실행 / 유역 경계 흐름 / 전역 물수지 / 전역 유사수지: 통과.
- 네이티브 기본 침전속도 100μm 물리적 계산: 실패.
- 원본 기본 및 원본 대체 침전속도 모두 적용한 2D 유사유출량 계산 시간간격 수렴성: **불합격 (세 자릿수 이상의 배수로 달라지는 사례 다수)**.
- 얕은 토심 조건에서 국지 유한 토양저장량: 기본식 20초에서 불합격.
- **고운사 유수침식 주 모델로 원본 OpenLISEM 7.5.2 채택: NO-GO, 제외.** 기능이 존재한다는 이유로 수치 결함을 무시하거나 출력을 연구 결과로 사용하지 않는다. LPJ-GUESS와의 결합 추천도 철회.
- 수정 포크는 원본의 검증된 해결이 아니며, 독립 신규 코드 계보로 다시 검증해야 한다.
- 추가 1/2초 미세시간간격 재시험 [Actions 40304815539](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40304815539), 별도 2m 격자 실행 [40303685346](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40303685346) : 보조 검증으로 실행 중, 종료 확인 후 이 문서에 추기할 것.

자세한 사전등록 판정기준: [numerical GO/NO-GO](2026-10-26_OPENLISEM_NUMERICAL_GO_NOGO_GATES.md).
과거 Windows 실행 실패 이력: [failure recovery](2026-10-26_OPENLISEM_752_PREVIOUS_NUMERICAL_FAILURE_RECOVERY.md).
