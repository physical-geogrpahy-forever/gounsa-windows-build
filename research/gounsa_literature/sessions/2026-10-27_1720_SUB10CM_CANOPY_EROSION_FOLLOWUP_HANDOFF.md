# 2026-10-27 17:20 고운사 5–10cm 수관차단+2D 침식 단일원본 추가 검증 인계

## 대화 배경 및 필수조건
전 대화가 길이 제한으로 중단되어 연구를 계속함. **5–10cm 이하 실제 published 계산격자, LAI 기반 수관차단과 수관저류 및 throughfall, 강우사상 2D 자유유동, 강우/유수 침식과 수송·국지 퇴적, 완전한 공개 단일 원본 실행코드 및 수치 안정성**을 동시에 요구. 누락된 과정을 외부 신규모듈로 결합하거나 DEM 자료 해상도와 실제 모델 계산격자를 혼동해서는 안 됨.

## 기존 정리와의 중복 점검
- `MASTER.md`와 `decisions/2026-10-27_5CM_10CM_CANOPY_2D_EROSION_NATIVE_MODEL_SCREEN.md`에 Maggioli 2022 5cm LISEM, Nord & Esteves 2005 5cm PSEM2D, Epple 2025 1cm LISEM, tRIBS-FEaST, GSSHA, SERGHEI-SE 및 탈락사유가 이미 상세 정리됨.
- **TREX는 새로운 원본 후보가 아님.** `papers/2008_Velleux_England_Julien_TREX_2D.md`가 2026-10-26에 전체 공개 C 원본을 찾아 감사한 기록이 있음. 새로운 후보처럼 제시했던 설명을 바로잡음.

## 이번 세션 추가 원본 대조
1. **TREX archived original:** https://github.com/WatershedModels/trex_src_csu 원본 저장소 및 `src/Interception-r4.c`를 GitHub connector로 실제 읽음. `interceptiondepth[][]` 잔여수량과 `grossrainrate * dt`를 비교하여 `netrainrate` 산출. LAI 시간변화 기반 canopy reservoir / canopy drainage / drip energy 연산은 해당 코드에서 확인되지 않음. 오래된 모델 개요 문서의 'interception 포함'을 식생정량요구 통과로 간주 금지. 현재 탈락 유지.
2. **Wei & Kinouchi 2014** `Improvement of CASC2D model for rainfall-runoff simulations in a forested catchment`, DOI https://doi.org/10.2208/jscejhe.70.I_157 . 후쿠시마 Kuchibuto River catchment, 2011 calibration storms 4개, 2012 verification storms 7개. 산림 개량판 LAI linked interception, ET, subsurface/groundwater; 주요 검증은 hydrograph, **5–10cm sediment transport/deposition executable/source와 혼동 금지**. 모델 TREX archived C 코드와 2014 modified CASC2D는 동일 SHA가 아님. 논문 단독 `papers/2014_Wei_Kinouchi_CASC2D_Forested_Interception.md`에 기록.
3. **SMODERP2D 최신 public master:** https://github.com/storm-fsv-cvut/smoderp2d . `smoderp2d/core/vegetation.py` leaf area parameter(`ppl`) / `pi` potential interception 배열; `smoderp2d/processes/rainfall.py::current_rain` 에 실제 canopy interception 계산 확인. 그러나 `smoderp2d/processes/rill.py::rill`에는 이전 추정 솔버 대부분 주석 처리되고 반환 유출이 0에서 출발하는 검사 결과가 있었으며 공개 코드 검색에서 sediment mass transport solver 및 deposition grid 미확인. **광고상의 soil erosion model ≠ 동일 공개 코드의 검증된 유사량 격자 수송**. 결정적으로 공식 매뉴얼 권장 계산격자는 **2~20m**이고 매우 작은 격자 사용은 feature width misrepresentation 발생. https://storm-fsv-cvut.github.io/smoderp2d-manual/requirements.html , 따라서 5cm 모델 후보에서 탈락.
4. **GEOtop-SED:** 공식 GEOtop 소개가 https://github.com/TanZiTT/GEOtopSed 링크를 안내하지만, public master root는 `GEOtop/`, `Libraries/`; `GEOtop/geotop.c`, `GEOtop/water.balance.c` 상단에는 GEOtop 1.0 Public 2010 표제. 현재 직접 확인한 파일/파일명 검색만으로 published 2016 sediment coupling 전체 작동 여부 입증 못 함. 유동 자체가 kinematic-wave 계열인 문제도 그대로 남음. 현행 보류/제외 유지.
5. **SERGHEI-SE:** Braga, Martínez-Aranda & García-Navarro (2026), DOI https://doi.org/10.3390/w18151870 는 2D SWE+sediment+Exner dynamic surface을 제공하지만 수관차단의 동일실험 native 검증 없음; 5mm 실험은 erodible-bed dam-break, rainfall + canopy high-resolution test가 아님. 2026 preprint Martínez-Aranda et al. https://doi.org/10.2139/ssrn.7044619 는 SEHS rainfall+runoff erosion closure 명시하지만 초고해상도 수관저류+침식 통합 근거 아님.

## 이번 세션 판정
**고운사 엄격 조건 전부 동시 PASS한 published, released, executable 단일 원본 없음(현 검토 범위).** 무작위 신규 모델이나 조합 제안 금지. 기존 SHETRAN 4.7.2 연구용 주모델 선정은 4m 실험 엔진에 한하며 5–10cm 실증을 뜻하지 않음. Maggioli(2022) LISEM은 canopy+erosion 5cm 발표 근거로만 남음. 신형 LISEM 0.2.4 배포 바이너리와 실제 Epple2025 실행판의 code provenance 미확정, 소스 상 canopy/splash 이슈 별도 추적 필요.

## 이번 세션에 실제 GitHub에 저장한 파일
- `papers/2014_Wei_Kinouchi_CASC2D_Forested_Interception.md`
- `sessions/2026-10-27_1720_SUB10CM_CANOPY_EROSION_FOLLOWUP_HANDOFF.md` (본 파일)
- INDEX와 MASTER에 연결하려는 기록은 후속 commit 실제 성공시에만 완료로 처리.

## 다음 채팅 시작점
이 결정에서 재탈락된 TREX, SMODERP2D, GSSHA, EUROSЕM을 다시 추천하지 말고, **출처/버전이 특정되는 5–10cm native whole-path canopy+full 2D+erosion/deposition 원본**이 있는지를 대상으로 검색/코드 hash 대조. LISEM classic과 Bastian van den Bout 신형 LISEM의 계보 및 2025 실험판을 동일시하지 말 것. 연결부 신규 구현을 원래 모델 기능으로 기록 금지.
