# 2026-10-27 19:40 고운사 5–10cm 식생수관차단 + 자유 2D 침식 공개 모델 추가조사

## 이번 결정
GitHub `SYSTEM.md` 규정대로 `MASTER.md`, `INDEX.md`, `decisions/2026-10-27_GITHUB_FIRST_SUB10CM_NATIVE_MODEL_FOLLOWUP.md` 및 이전 10cm/LISEM 분기 감사부터 확인. 468편 기존 논문/94개 모델 목록에 없는 후보를 연구한 후 **HydroSed2D, WaNuLCAS, 산림 HEC-RAS 2D 실증**을 추가 대조했다. **필수조건 전체 PASS는 이번에도 없음**. 공개된 원본에서 우선 물리식 연산 경로를 검사하여 기능 명칭만으로 채택하는 오류를 피함.

## 사용자 필수조건
5–10cm 이하 실제 **계산격자**, LAI 또는 동등한 정량 상태 기반 수관저류/차단 및 throughfall/drainage, 경사지 X/Y 자유 유동의 genuine 2D SWE, 강우타격과 유수박리의 구분, 유사 이송 및 국지퇴적, 동일 공개 원본 실행판, 계산 안정성 및 질량수지. 외부모델 수관전처리 뒤 2D 유동만 수행한 연구는 원본 통합모델로 허위 표기 금지.

## (A) HydroSed2D: 새로 감사한 실제 공개 원본
- 펜실베이니아주립대 공식 소개 https://water.engr.psu.edu/liu/hydrosed2d.html , https://github.com/psu-efd/HydroSed2D .
- `src/sediment.f90` SHA `7e6be5983c8f8eee32a5ba919a6347acf425d615` 실제 read. L23–54 계산 `calc_shear → calc_criticalShieldsNumber → calc_sedimentFlux → calc_divSedimentFlux → calc_faceElevChange → updateMeshData`. L176–197 **MPM** 또는 **Grass**의 bedload 양방향 플럭스. Exner dynamic elevation native.
- `swe.f90` SHA `e2b4e3741f72514f33cd4e3dcfc5c4e478ccd96b`, `module.f90`, `initialization.f90`도 확인. 공개 범위에서 canopy/LAI, throughfall, rainfall splash, soil infiltration 구현 및 native event storm test 미확인. 예제 `1DTranscriticalFlow`, `dambreak_over_hump`, `sediment_hump`.
- **탈락**: 강우사상 모델 아닌 경계유입 2D 유동 및 bedload erosion 시험. 수치실행 테스트 하지 않음.
- [원본코드 감사](../models/HydroSed2D_Fortran_Original_Source_Audit.md)

## (B) WaNuLCAS: 정량 식생과 침식은 있지만 자유 2D 아님
- 원저 van Noordwijk et al. (2004) WaNuLCAS3.01 technical manual: canopy max film thickness × LAI, potential ET canopy evaporation priority; ROSE soil loss; zone/vertical-layer agroforestry structure. PDF https://www.cifor-icraf.org/publications/region/sea/publications/softcopy/BK0060-04.pdf (web 원문 텍스트 확인, screenshot 서버 403).
- Onsamrarn et al. (2020) https://doi.org/10.1371/journal.pone.0241689 Thailand mixed cropping WEPP vs WaNuLCAS 현장 runoff/sediment 비교. leaf area, root length density, interception/vegetation sensitivity. **5–10cm 경사지 전방위 유동/국지 DoD가 아니라 농림복합 구획별 계산.**
- modern `degi/wanulcas` Shiny 공개 repo와 원 STELLA WaNuLCAS3.01 완전 실행원본/침식solver 동등성 미확인.
- **탈락**: 자유로운 진정한 2D SWE 및 초고해상도 입증 없음.
- [원본 계보](../models/WaNuLCAS_Interception_Erosion_Strict_2D_Screen.md) | [2020 논문](../papers/2020_Onsamrarn_WaNuLCAS_WEPP_Thailand_Erosion.md)

## (C) 급경사 산림 2D 수관차단 선행연구: Ámon et al. (2024)
Ámon et al. (2024), *Water* 16:750, https://doi.org/10.3390/w16050750 .
- 헝가리 steep-slope forest Hidegvíz Valley 2010/2012 storm runoff hydrograph observations. 수관차단과 낙엽수층 저류를 두 방법으로 전처리/유사토양층 표현하고 **HEC-RAS SWE 2D FVM**으로 유동 모의.
- adaptive mesh 4×4–20×20 m; 직접 강우유수 박리와 같은 시뮬레이션 내 유사수송/격자별 국지퇴적 DoD **모의하지 않음**.
- HEC-RAS 엔진의 별도 sediment capability와 해당 **논문의 실험에서 활성화한 과정** 구별. 수관차단을 독립 전처리했으므로 원본 native canopy 동적처리와 동일시 금지.
- **보조근거 (forest interception & true 2D hydrodynamic application), 주모델 탈락**.
- [논문기록](../papers/2024_Amon_HECRAS_Forest_Canopy_Litter_2D_FlashFlood.md)

## 추가 검색에서 재채택하지 않은 후보
- `CH-Earth/sedhydro`: upstream hydrology model output을 반드시 외부에서 연결받는 hydrology-model-agnostic sediment routing 프레임워크. 원본 단일 수문-침식 모형이 아님 (https://github.com/CH-Earth/sedhydro).
- EROSION-3D는 `jonaslenz/toolbox.e3d` R 래퍼만 GitHub GPL 공개, EROSION-3D full solver와 동일하지 않음 (https://rdrr.io/github/jonaslenz/toolbox.e3d/).
- SPHY 추가 관찰은 PCRaster framework/경로 기반, 최신 공개 sediment에는 hydrological forcing coupling 필요; strict 2D SWE 없음.
- 기존 ASTERIX, TREX, GSSHA, tRIBS-FEaST, SERGHEI-SE, SWEHR, PSEM_2D, LISEM Classic/New, SHETRAN 기존 탈락 또는 제한조건 그대로 유지.

## 남은 문제와 다음 조사 우선순위
1. **논문과 공개 원본의 동일 버전** 검증: Maggioli2022 5cm LISEM, Cuomo2018 10cm LISEM, Epple2025 1cm LISEM의 exact executable & storm input과 source QA 간극 해소. 과거 OpenLISEM7.5.2 sediment timestep nonconvergence를 문헌 존재로 무효화 금지.
2. 진정한 2D flow + rainfall and runoff erosion + canopy within the *same publicly executable* model 존재 여부를 공개 코드에서 탐색.
3. 0.648ha SHETRAN 4m 원본 35 native 실행을 10cm 실증으로 간주하지 말 것.
4. 이번 세션은 소스 read & 문헌 대조이며 **네이티브 컴파일, 테스트, 수관 ON/OFF 5cm 실험 실행은 하지 않음**.

## 판정
**완전 통과 모델 신규확정 없음. 두 공개 모델 HydroSed2D 및 WaNuLCAS 탈락, 산림 HEC-RAS2D 연구는 보조근거만 남음.**
