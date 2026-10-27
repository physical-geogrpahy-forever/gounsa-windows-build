# 2026-10-27 20:53 Maggioli2022 LISEM 5cm 원논문-당시 공개 코드-재현성 교차검증 세션

## 출발과 확인
고운사 `SYSTEM.md`, `MASTER.md`, `INDEX.md`, 이전 LISEM strict decisions와 실제 native 7.5.2 12회 dt 민감도 실패 읽고 작업.

## 새로운 실제 확인 사항
- Maggioli2022 원문 DOI 10.3389/fevo.2022.765148 : 375m² 실험사면의 5cm DTM과 동일 5cm LISEM 모의, **1s 시계열/맵 해상도**, 운동파(kinematic wave) 유출을 명시. **1s를 반드시 fixed solver dt로 해석 금지**.
- vegetation point / all point ratio→cover, Ramírez empirical LAI→canopy storage. 식생 시나리오 Ksat, cohesion 및 cover도 동시에 변경. **수관차단 ON/OFF만의 통제 비교가 아님**.
- 전체 18개 강우사상 2014~15 aggregate calibration: observed 2.81t vs modeled 3.55t, 보고 RMSE 17.79%. 동일 데이터 이용해 보정 및 비교하여 완전 독립 holdout 검증 아님. cellwise DEM 변화도 미검증.
- Data Availability 일반 문구 only, 정확한 코드 버전, 전체 raster input, storm runfile, reproducibility DOI 확인 안 됨.
- **GitHub historical 공개 snapshot 최초 확인**: `vjetten/openlisem` SHA `3b0264ef557c031fe39fb6d523c3669bf6e1296a`, commit 2022-02-11, `include/version.h` = `6.837 beta`. 이것이 Maggioli **exact 실행판이라는 증거는 없음**. 2026 7.5.2 installer는 2026-10-15 artifact와 명백히 다른 연대.
- 2022 original `lisInterception.cpp` canopy/LAI/drainage (blob571ea...), `lisErosion.cpp` direct and leafdrip splash (blob ffe013...), `lisSWOF2DSediment.cpp` 2D advection/deposition (blob591054...), `lisOverlandflow.cpp` kinematic vs free 2D choice (blob770b99...). 발표 당시 **code capability가 존재**했지만 **paper's actually used 5cm path는 kin wave**.
- 2022 `lisErosion.cpp::GetSV` d>=100μm uses `dm=d/1000` branch, suggests SI discontinuity bug lineage. Maggioli D50 5μm로 해당 증거 하나만으로 논문 문제 주장 금지.
- Previously unresolved extra native 7.5.2 1s/2s trials **404?** 정확 runs **40304815539** 20분 timeout / incomplete, **40303685346** 2m run 30분 timeout + NO_VALID_SIMULATIONS. 논문 1s case가 옛 버전 7.5.2 failure를 없앴다고 해석 금지.

## 수정한 canonical file
`papers/2022_Maggioli_RodriguezCaballero_LISEM_5cm_TLS_LAI_Interception_Erosion.md`, 기존 DOI 파일을 수정하고 세부 감사를 추가, 1s phrase 수정. 중복 paper 새 파일 금지.

## 새로운 결정파일
`decisions/2026-10-27_MAGGIOLI_2022_EXACT_CODE_INPUT_PROVENANCE_AND_VALIDATION_AUDIT.md`

## GO/NO-GO
**Published 5cm canopy/erosion yes, user-required 5cm true 2D free SWE no, matching reproduce package unknown, standalone runnable Gounsa adopted engine no.** SHETRAN subcm speculative enlargement withdrawn. 7.5.2 known sediment dt failure persists.

## 다음 정확한 작업
1. 외부에서 공개된 Maggioli-specific complete raster files/runfile/2021 binary provenance DOI가 나타나는지 **정확히 확인**, 실시간 공개 경로 없으면 재현 불가로 표기.
2. 2022 old snapshot 6.837로 별도 synthetic QA 시에도 source ≠ paper executable 구별, published success로 주장 금지.
3. 엄격 free 2D + LAI canopy + 5~10cm rainfall/flow erosion + deposition + complete code가 필수라면 matching published source를 확인한 후에만 다시 단일모델 선정.
4. 기존 탈락 TREX/SHETRAN speculative 5cm, OpenLISEM7.5.2, 2022 current Bastian LISEM broken canopy/splash 다시 추천하지 않음.

## 근거
https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.765148/full
https://github.com/vjetten/openlisem/commit/3b0264ef557c031fe39fb6d523c3669bf6e1296a
https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40304815539
