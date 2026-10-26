# 2026-10-26 야간 고운사 D+1 모델 구조 제출 인계

## 사용자의 마감
2026-10-27 18:00 (Asia/Seoul). 최소 산출물: 모델선정 + 자료별 입력/활용 + 모듈/변수/시간 결합구조. **현재 완성 통합코드나 현장 검증을 주장하지 않는다.**

## 이번 세션 신규 결론
본 연구의 원칙은 원본 SWEHR V1.0을 완성된 식생 모형이라고 주장하지 않으면서, **SWEHR 공개 C 2D 유출/유사 엔진을 수정 기반으로 삼고, published Rutter 수관저류/적하, LAI/roots/litter, LPJ-GUESS, 사상 간 토양-지형갱신을 새 결합으로 구성하는 공개코드 기반 신규 모형을 설계기준안으로 채택**하는 것이다. 기존 Iber+ 선택은 공개 원본 전체 이용 문제와 동적 수관차단 부재로 연구용 개발 플랫폼으로는 보류한다. 원본 all-in-one 검증통과 후보 없음.

정밀 설계서: [2026-10-26_DEADLINE_GOUNSA_MODEL_ARCHITECTURE_AND_DATA_PLAN.md](../decisions/2026-10-26_DEADLINE_GOUNSA_MODEL_ARCHITECTURE_AND_DATA_PLAN.md).

## 기존 자료 중 반드시 재사용
- [SWEHR original 2017 untouched](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/main/third_party/SWEHR_original_v1_0_2017)
- [SWEHR water/sediment QA modified](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/swehr-water-sediment-closure-20261026/experiments/rainfall_10_50)
- [38-run synthetic spatial fork](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/spatial-vegetation-runoff-erosion-20261026/experiments/rainfall_10_50)
- [original vs article discrepancy](../decisions/2026-10-26_SWEHR_RUTTER_CANOPY_SHIELDING_SOURCE_AUDIT.md)
- [Oct 26 EUROSEM mass failure](../decisions/2026-10-26_EUROSEM_1998_NATIVE_SEDIMENT_LEDGER_RILL_FAILURE.md)
- [Oct 26 OpenLISEM 7.5.2 failure](../decisions/2026-10-26_OPENLISEM_752_NATIVE_2D_STABILITY_FAILED.md)

## 최우선 작업
1. 데이터 인벤토리: 실제 고운사 연구구역 AOI/ground DEM, 억새와 참나무 위치, 토심, Ks, 입도 및 강우사상. 원래 repo의 해당 raster 없는 것으로 보이고 확보 표시 금지.
2. 원본 SWEHR/수정 포크 대조, 공개 C에 Rutter + canopy shielding + leafdrip energy **신규 구현**. 단순 균일 가상 `QA_WFACTOR`는 절대 dynamic canopy라고 주장 금지. 유지 가능한 소스 commit 고정.
3. 동적 canopy standalone 물수지 + 2D water/sediment ledger + dx/dt 수렴 + finite soil cap 검증.
4. 발표용 모델 다이어그램과 입력 자료 및 없을 경우 불확실성 표 제공. '설계됨/원본 검증/수정포크 검증/현장 미검증' 표시.
5. `CURRENT_MODEL_SPEC.md` 수정 시 이전 확정 부분을 훼손하지 않도록 새 결정문과 근거를 표시하고, 최종 주 엔진으로 표기하기 전 엄격 gate 준수.

## 이 세션에서 한 일
GitHub 이전 판단 및 원본/포크 수지 검증 기록 직접 재독. McGuire et al 2016 원문 §3.5와 기상청 AWS/ASOS 분자료 제공 확인. **한 개 설계 결정문을 main에 생성함**. 이 채팅에서 통합 C 소스 수정이나 현장 자료 조회 완료로 과장하지 않음.
