# 2026-10-27 SWEHR 2025 HydroShare 연구자료와 2016 논문, 2017 공개소스의 동일성 검증

## 이번 조사에서 새로 발견된 사항
- Luke McGuire와 Aiza Kabeer가 2025-12-10에 HydroShare에 공개한 연구자 리소스 **“A numerical model for runoff and debris-flow processes in a recently burned watershed in northern Arizona, USA”**가 공식 개발자 [HydroShare 프로필](https://hydroshare.cuahsi.org/user/8128/)에서 확인됨.
- 설명: 2022 Pipeline Fire로 소실된 북부 애리조나 소유역의 runoff-generated debris flow 모의 자료 및 관련 자료. "A more general version of this model is also available in CSDMS [SWEHR](https://csdms.colorado.edu/wiki/Model:SWEHR)"이라고 명시.
- **중요한 접근 제한:** 공개 프로필의 제목/날짜/초록은 검색 인덱스에 표시되나 2025 해당 리소스의 **고유 HydroShare UUID, 압축파일 목록 및 코드 파일은 이번 도구에서 열람되지 않았음**(프로필 502). 그래서 최신 Rutter/LAI canopy 코드가 해당 패키지에 존재한다고 주장할 근거 없음. 코드 발견이 아닌 재현자료 provenance 신규 단서로만 기록.

## McGuire et al. 2016 논문 다시 대조
- DOI https://doi.org/10.1002/2016JF003867 ; JGR Earth Surface, 121, 2211–2237. **원문 Rutter canopy C(t), drainage D, throughfall Tc, canopy capacity S, 2D SWE/HR detachment/soil-layer conservation = published research**, §3.2,3.5,3.6.
- **실제 모델 계산 해상도 = 37.5cm**. 원 TLS 2.5cm DEM을 계산시간 때문에 37.5cm로 집계(§3.8). 이것을 2.5/5cm **모델** 계산 선례라고 부르지 않는다.
- Station Fire 후 Nov/Dec 관측 두 이벤트에서는 수관 거의 전소로 **canopy interception 비활성**(§3.8).
- 식생 회복 가상 20×5m 경사 실험은 별도로 Rutter Tc 0.35, S 2.2mm, Kc 5e-5mm/s, gc 3.9mm^-1, Cv 0.05–0.95를 사용. canopy enabled 수치사례이지만 실제 5–10cm 계산 아님.

## 2017 CSDMS SWEHR 1.0 실제 소스코드 재감사
- [CSDMS 소개](https://csdms.colorado.edu/wiki/Model:SWEHR), [GitHub 원본](https://github.com/csdms-contrib/swehr/blob/master/SWEHR.c). 원본 `SWEHR.c` **1785행, 77402글자**, Git blob SHA `e8505221a37d245ebb387b3304d8f325addd9ada`.
- 원본 전체 코드 검색 결과 `canop` 0회, `intercep` 0회, `rutter` 0회, `leaf` 0회, `lai` 0회. Rutter 저장/배수/LAI 함수 없음.
- `SWEHR.c` line 814 `R=RAIN[rind]`, line 1338 `E[1]=(1-H)*P[k]*ASMASK*R`, line 1450 `INFL` Green-Ampt. `U[1]` 강우 공급과 rain impact 박리 내장, **수관저류를 통과한 P_eff 별도 공급 아님**.
- CSDMS 페이지 원본 파일 `input.txt`은 3×51 grid, dx=0.25m 간단 테스트; 별도 native canopy 소스 아님.
- 따라서 `SWEHR 1.0` = genuine 2D+HR 토양침식 구성, **Rutter/LAI canopy absent**라는 기존 [2026-10-26 감사](2026-10-26_SWEHR_RUTTER_CANOPY_SHIELDING_SOURCE_AUDIT.md) 판정 유지. 신규 HydroShare 연구용 패키지가 이 결함을 고쳤는지는 **확인할 수 없음**.

## 2025 Epple 1cm 신형 LISEM 코드 접근성과 혼동 금지
- https://doi.org/10.1002/esp.70127 는 독일 1cm 농경지 시험구 LISEM 지형변화/유속 논문; 새 LISEM scripting lineage 추정. 논문/Supporting Information에서 1cm canopy water budget을 함께 켰다는 증거가 없고, 실험 입력/출력 및 코드 SHA 공개로 동일 프로세스 검증할 수 없음.
- 공개 GitHub `bastianvandenbout/LISEM` main 0.2.3, develop 0.2.5 에서 `SCANOPYN=0`/원강우 splash input 0 문제는 이전 감사로 확정. 별도 **0.2.4 SourceForge Windows 바이너리와 Epple 2024 build는 미검증**, 혼동 금지.

## 이번 결과의 GO/NO-GO
1. **새 완성 모델 확인: NO**.
2. McGuire HydroShare 2025 프로필 수준 provenance **새 조사 단서** 확보, 자료 내부 원본/실행/수관모듈은 미확인, 채택 추천 불가.
3. 2016 McGuire 원논문 온전한 published model은 존재하지만 실증 37.5cm 및 burned interception OFF, 그리고 공개 SWEHR 1.0 canopy 없음.
4. 2017 SWEHR 원본 및 Classic OpenLISEM 7.5.2 NO-GO 유지, 2025 Epple는 1cm+canopy 동시 검증 근거 아님.
5. GitHub 2017 old code를 새로운 연구용 2025 파일과 **같다고 단정하지도**, 2025 파일이 더 완성됐다고 **추정하지도** 않는다.

## 다음 검증은 이 자료 자체
- 2025 HydroShare 리소스의 UUID 및 **자료 파일명** 취득 후 `SWEHR.c` / 새로운 Rutter 커널 / `C(t), D(t), LAI` state / 실행 파라미터 / dx를 확인.
- 2024/2025 신형 LISEM 정확 실행판의 source, scripted canopy, timestep sediment convergence 확인.
- 어느 것도 실제 파일을 열지 못했다면 신규 후보 PASS/컴파일 PASS/동일 실행판 PASS를 발행하지 않음.
