# 2026-10-27 20:39 시작 세션: OpenLISEM 7.5.2 기존 원본 시험/소스 재감사 인계

## 새 문헌
- 없음. 기존 Maggioli(2022) 5cm LISEM 운동파 선례, Cuomo(2018) 10cm, Epple(2025) 신형 LISEM 1cm 선례의 원래 모델 계보를 재확인했다.

## 이번 세션 소스 검증
- official `vjetten/openlisem`의 `v7.5.2` 태그와 `main_C` branch 직접 대조. 총 8커밋 증가, 2D SWE cpp에만 비교변경 확인. canopy, splash, sediment, settling velocity, 2D boundary core source blob 동일.
- 실행 함수 `fullSWOF2openMUSCL()`는 active. `fullSWOF2open()`는 obsolete.
- native canopy water balance + effective rainfall + leaf drip splash + 2D SWE + suspended sediment detachment/advection/deposition 모두 존재하지만 고운사 정량검증은 별개.
- Source risk: `GetSV` 100µm에서 142배 불연속, 유한 토사층 검토 `DetachMaterial`/농도상한 일부 주석, user min timestep으로 CFL 위반 가능, shared OpenMP neighbor += data race 가능성(미입증).

## 기존 네이티브 실험 검증
- https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40304135775 job 121508937649 Windows native full original 12 runs `success`; 보고서 숫자 확인: Oak SV1 외부 timestep 5/10/20s에서 유사 배출 0.005993/123.037727/832.588686 kg/ha; gross sediment mass balance 폐합에도 불구하고 수치 수렴 실패 및 국지 초기토사량 초과.
- https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40304815539 job 121511206049 FAILED (1s Miscanthus SV1, SV3 each 480s timeout, 20min run timeout).
- https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40303685346 job 121507441094 FAILED (2m 시험 개별 100초 timeouts 및 30min action timeout).
- 위 두 실패를 **숫자 수렴시험 결과**로 묘사하지 말 것.

## 판정
**Classic OpenLISEM 7.5.2 original => NO-GO**, 반복 추천 금지. 5cm Maggioli LISEM 논문은 LAI canopy + sediment의 **운동파** 모델이지 5cm full 2D SWE 입증이 아님.
현재 아직 모든 요구(5–10cm native precedent, LAI canopy, rainfall/flow detachment, deposition, genuine 2D free flow, same public source compiled numerical accuracy)를 동시 통과한 기성 단일 모델은 확인하지 못했다.

## 금번 GitHub 커밋
- [decisions 원본 재감사](../decisions/2026-10-27_OPENLISEM_752_SOURCE_NATIVE_REAUDIT_NO_GO.md)
- [MASTER.md](../MASTER.md) 최신 상단 기록
- [models/OpenLISEM.md](../models/OpenLISEM.md) 재감사 추가
- 이번 sessions 인계서
- 새 논문 파일 없음, INDEX 수정 불필요.

## 다음 과제
- 이미 실패한 original classic 7.5.2를 다시 시험하자고 반복 권유하지 말 것.
- 신형 LISEM 0.2.4 Windows 별도 바이너리와 Epple 2025 사용판 exact build/source provenance, 실제 canopy state update, rain splash 연결을 **원본 수준에서 입증한 후** genuine 2D 및 cm 침식 numeric QA.
- 저자 공개 산지 canopy/sediment 5–10cm full2D **동일 실행본이 확인되는 경우**에만 채택 판단.
- 임의로 SHETRAN 5cm 확대/새 침식식 개발을 사용자 동의 없이 기성 published model 대체안으로 취급하지 말 것.
