# SHETRAN 4.7.2 전체 호출경로 코드 감사 인계

검토 소스 SHA: `cf9cd540add78ad3accbaf62b4199d2032887f6b` (nclwater/Shetran). 날짜 2026-10-26.

## 가장 먼저 볼 문서
- `../decisions/2026-10-26_SHETRAN_472_FULL_PATH_SOURCE_AUDIT.md` (이번 완결된 정적 호출경로 검토, A01-A17)
- `../decisions/2026-10-26_SHETRAN_EVENT_BOUNDARY_DEM_STATE_AUDIT.md` (DEM/퇴적층 전달 공식)
- `../models/SHETRAN.md` (기존 모든 발견)
- `../MASTER.md`, `../SYSTEM.md`, `../INDEX.md`

## 새 발견 (원본 코드에서 직접 검증)
1. `SYMAIN`의 첫 호출은 `PASS_symain==1`이라 초기화하고 반환. `run_sim`은 첫 `ETSIM/VSSIM/OCSIM` 후 `SYMAIN` 호출, 그러므로 최초 hydrological interval의 sediment 계산 누락. 심각.
2. `SYOVER`는 물 timestep당 한 번, `SYCOLM`은 `NEPS`회: 중간 퇴적층 `DLS` 변화가 `DLSMAX` 토양보호를 즉시 재평가하지 못함.
3. `SYCOLM`의 원토양 `GNU` → 느슨한 퇴적층 공급변환은 `FETA = (1-THSAT)/(1-PLS)`. 원위치 두께와 퇴적층 두께는 물리적 의미가 다름.
4. 기존 `FRRESP` output #44 초기값/기준시각/기준 DLS 문제 재확인. HDF5 `s_v_er`는 순간 mm/day이므로 native timestep 누적 `Σ GNU DTUZ`로 대조해야 함.
5. `VS08` 토양층고도 `ZLYRBT=ZGRUND-depth`, 고운사 얕은 토층이 DEM 변화만으로 부정확하게 재생성됨. horizon depth와 bedrock position을 보존하며 따로 다시 만들어야 함.
6. `SYBC`, `BALSED` 미구현; native hotstart sediment 상태 `DLS/FBETA/FDEL` 미포함.
7. channel link과 bank `ZGRUND`는 원본에서 separate input/handling; grid DEM 교체만으로 전체 flow geometry 변화 불가.
8. `ET` 0 `CSTCAP`에서 0으로 나누기 우선 수행, snow 경로의 stale forcing, negative STRXX 외부 boundary의 예외조건 등은 수정/실행테스트 전 사용조건에 주의.

## 작업 결과
- GitHub `decisions/2026-10-26_SHETRAN_472_FULL_PATH_SOURCE_AUDIT.md` 생성
- `models/SHETRAN.md`, `MASTER.md`, 기존 `decisions/2026-10-26_SHETRAN_EVENT_BOUNDARY_DEM_STATE_AUDIT.md`에 링크 및 정정 추가.
- 원본 Fortran 코드 자체 수정 **없음**.
- 로컬 실행환경에서 `github.com` DNS 조회 실패. SHETRAN 전체 원본 다운로드/컴파일/실행 **불가**, 원본 실행 성공 또는 수지 통과를 주장하지 않음.

## 다음 일의 순서
1. 원본 SHETRAN 압축파일/소스가 실행환경에 확보될 경우 먼저 **unmodified Cobres** native build + HDF5/log/수지 점검.
2. `SYMAIN` 첫 스텝 누락 재현하는 2-step/3-step native test; 사전 초기화 경로 설계와 A/B.
3. `GNU` dt 누적, `DLS`, `FBETA`, `FDEL` 저장/복구; output #44와 비교.
4. `DLSMAX` 영향 `DTUZ` 및 `NEPS` 독립 민감도.
5. `FR37/OC35/VS08/SY51-53` 교환 + hydro hotstart + water/sediment mass conservation test.
6. 10,20,30,40,50 mm/h 동강우량 조건 및 억새/참나무 맹아 물리적 입력 분리.
