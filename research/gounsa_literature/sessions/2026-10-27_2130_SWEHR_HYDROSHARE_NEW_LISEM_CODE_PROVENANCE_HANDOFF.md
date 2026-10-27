# 2026-10-27 SWEHR HydroShare 후속 코드 계보 및 신형 LISEM 논문 검증 인계

## 새로운 연구자료 발견
- McGuire, Luke / Kabeer, Aiza 2025-12-10, HydroShare “A numerical model for runoff and debris-flow processes in a recently burned watershed in northern Arizona, USA”, 개발자 [공식 프로필](https://hydroshare.cuahsi.org/user/8128/) 및 검색 인덱스로 확인. 2022 Pipeline Fire 소유역 runoff/debris-flow 재현자료, generic code CSDMS SWEHR 연계 명시. **프로필 페이지 HTTP502/개별 UUID/자료목록/코드 미열람**. 이 정보로 Rutter 최신 소스 획득을 주장하지 않는다.
- 새로운 확인 모델/논문 DOI 등록은 없음. 기존 McGuire 2016 및 Epple 2025 canonical paper 보강, 중복 파일 생성 없음.

## 공개 코드와 논문
- McGuire 2016 원논문 DOI 10.1002/2016JF003867 Rutter canopy eq24–26, 2D SWE/HR sediment, 산지 침식/퇴적 observational comparison. **2.5cm TLS는 37.5cm 실제 계산격자로 aggregation**, 산불후 본 관측 사건 canopy OFF, 별도 식생 회복 가상 시나리오.
- CSDMS SWEHR1.0 코드 `csdms-contrib/swehr/SWEHR.c` blob SHA e8505221a37d245ebb387b3304d8f325addd9ada, 1785 lines. full original 검색: canopy/interception/Rutter/LAI 구현 없음. 기각 판정 2026-10-26 감사와 일치.
- 2025 Epple LISEM 1cm 신규 엔진 수문/유속/DoD 비교는 published, exact model source/inputs 및 1cm canopy ON 실증 미확인. 공개 0.2.3/0.2.5 code fixes missing; 0.2.4 바이너리는 아직 실험하지 않음.
- 다른 이미 탈락한 Wflow (kinematic directed sediment), FeST (network sediment), SEIMS, HydroPol2D 등은 재추천 금지.

## 이번 GitHub 갱신
- [신규 결정문](../decisions/2026-10-27_SWEHR_2025_HYDROSHARE_CODE_PROVENANCE_FOLLOWUP.md)
- [MASTER.md](../MASTER.md) 최신 판정 추가
- [2016 McGuire canonical](../papers/2016_McGuire_SWEHR_Postwildfire_2D.md)
- [2025 Epple canonical](../papers/2025_Epple_Bienert_Grothum_LISEM_1cm_PTV_DoD_Erosion.md)
- 이 인계서
- INDEX 신규 논문 없음 → 변경 없음

## 다음 검증 지점
1. 2025 HydroShare 항목 UUID와 실제 `.c` 소스/설명서 확보 후 Rutter storage C(t), Tc, Smax, rain impact, 2D sediment 및 dx 확인. HTTP502이면 내용 미검증 처리.
2. 신형 LISEM 0.2.4 Windows 배포판을 빌드/설치본 source와 구분하여 실제 OpenCL kernel, integrated canopy path, precipitation splash path 확인. 배포판이 2025 Epple 1cm 논문과 일치하는지 동정.
3. 실제 동일 공개 실행소스로 canopy ON/OFF + 5–10cm + xy 2D flow + erosion/deposition numerical stability **실행시험** 통과 전까지 모델선정 NO-GO.
