# 2026-10-27 단일 레퍼런스 기반 다중 엔진 모델 재분류

## 1. 정정
기존 '단일 모델 = 단일 계산 엔진/한 개 실행파일' 기준은 잘못되었다. 사용자가 요구한 '단일'은 **한 편의 원논문에서 실제 연결·실행·검증한 통합모델**의 뜻이다. 논문 하나에서 tRIBS+OFM+Hairsine-Rose 또는 ELM+TELEMAC+GAIA 등 여러 엔진을 결합했어도 단일 레퍼런스를 충족한다. 단, 서로 다른 논문을 새로 결합한 경우 새로운 coupling으로 분류한다. 각 논문 내 실증, 공개 소스 대응, 실제 5~10cm 격자 및 native 수치안정성은 별도로 확인한다.

## 2. 연구 제약
고운사 1ha 미만의 급경사 사면, 드론 DEM 5~10cm, 나지·억새·참나무 맹아·혼합 패치, 10~50mm/h의 단일 강우사상. 나머지 피복/조도/침투 등의 조건을 고정하고 수관차단 ON/OFF의 독립 기여를 비교해야 한다. 강우박리·유수박리·공간 침식/퇴적·경계유사·지형변화·물질수지, 가능한 실제 2D X/Y 흐름 필수. 피복률만으로 식생량·LAI·root를 대체하지 않는다. COPLAS 및 MUSLE 금지.

## 3. 기존 자료 기반 전수 분류 범위
2026-10-27 main GitHub tree: 기존 논문별 MD 508, 모델별 MD 110, decisions MD 108 (본 파일 추가 전). 과거 감사와 관련 후보 원논문 웹 비교를 수행했다. 이 숫자가 이번 세션에 PDF 508개 모두 재독했다는 의미는 아니다.

## 4. 물리/논문 일치성 우선 후보

### A. Kim, Ivanov & Katopodes (2013), tRIBS–OFM–Hairsine–Rose / Kim, Han & Cho (2014) tRIBS-FEaST
- https://doi.org/10.1002/wrcr.20373 ; https://doi.org/10.9798/KOSHAM.2014.14.5.351
- 동일 발표 통합모델: tRIBS Rutter 수관저류/수문 + OFM 2D Saint-Venant Roe FVM + HR 다입경 강우/유수박리, 재박리, 퇴적 및 원토양/퇴적층·지형갱신.
- 2013 실험 §4.1/4.2에서는 실제 삼각격자 면적 0.005m2, 약 7.1cm 정사각 환산; **두 시험은 사실상 1D이고 hydrology OFF**라고 §4.3 명시. 실제 유역 2D 통합사례 Lucky Hills는 coarsest 50m2 triangles, finest 9분의1 규모로 7cm 아님. 수관차단-침식이 7cm 동시 검증됐다는 주장은 부정확.
- 현재 https://github.com/tRIBS-Model/tRIBS 에는 Rutter interception 구현 확인되지만 **2013/2014 발표판의 HR sediment solver 미발견**, LAI→적하충격 native 연결 증거 미확보.
- 판정: **논문 물리 첫째 후보, 바로 재현가능 실행판은 미확보**.

### B. Maggioli et al. (2022), classic LISEM
- https://doi.org/10.3389/fevo.2022.765148 : 25x15m, 실제 5cm 계산격자, TLS vegetation→LAI→canopy capacity와 Green-Ampt, runoff/erosion. 논문은 **kinematic wave** 사용, free 2D SWE 검증 아님.
- 18 events, 관측 2.81t vs 예측 3.55t, 17.79% RMSE는 5cm cellwise 독립 침식/퇴적 검증 아님. 단독 canopy ON/OFF 분리 실험도 아님.
- https://github.com/vjetten/openlisem 공개 2026 7.5.2와 2022 실제 논문 SHA 미확인, 이전 Native 7.5.2 sediment dt/stock 불합격. 복구는 별도 Work 담당.
- Cuomo(2018) 10cm LISEM, Epple(2025) 1cm LISEM 선례는 서로 다른 모델계보/검증범위로 분리.
- 판정: **실제 5cm 식생 수관침식 선행연구 최상위, 현 공개판 직접 실행 보류**.

### C. Long & He (2009, 2010)
- 2009 Journal of Information and Computational Science 6(6) 2349–2356; 2010 Journal of System Simulation 22(2) 348–352.
- **한 논문에서** modified Gash interception + 2D SWE + Green-Ampt + independent erosion/deposition + rill morphology evolution을 제시. 2010 포인트 implicit friction 포함.
- matching original code, cm 계산격자, LAI/leafdrip KE, field mass convergence 미확보. 별도 2009 GPU 연구코드와 함부로 동일시하지 말 것.
- 판정: **물리과정 첫째군이지만 연구판 실행소스 확인 안 됨**.

### D. Wei et al. (2017), forest TREX
- https://doi.org/10.1016/j.jher.2017.09.003
- 2014 산림 수관저류 개선 계보, 2017 forest model 2D diffusive overland runoff, rain splash/flow erosion and sediment, deposition.
- 연구 실제 90m, 오래된 공개 generic TREX C 코드가 저자 2017 통합 forest code와 동일하다는 근거 없음. leafdrip energy explicit model 미확인.
- 판정: **단일 산림 interception+침식 published precedent, native 5cm/public exact code 미확보**.

### E. Jiang et al. (2025), AHMS-SED
- https://doi.org/10.1029/2024MS004593 ; https://github.com/JiangCong1990/AHMS-SED ; https://doi.org/10.5281/zenodo.14494932
- Noah-MP throughfall/leafdrip + 침식옵션과 CASC2D-SED 계열, 여러 engine을 **한 논문**에서 통합, 원본공개.
- 그러나 실제 계산 20km; module_rt_sed2d.F는 Routing Makefile 경로에 미연결, raindrop-option 선택된 실행 확인 없음. true free SWE 아니라 2D routing.
- 판정: **공개 구현 참고, 직접 5cm 엔진은 불가**.

### F. Feng et al. (2026), ELM–TELEMAC–GAIA
- https://doi.org/10.1029/2025WR042040 ; https://zenodo.org/records/18331808
- **단일 레퍼런스 자격 충족**. ELM hourly runoff/hillslope sediment flux→TELEMAC free 2D hydraulics→GAIA multi-class deposition/bed Exner. 저자 수정 GAIA/TELEMAC 소스와 결과 공개.
- 실제 최소 30m mesh. **원문은 upland soil erosion에 따른 사면 지형고도 변화를 bed evolution에 포함하지 않는다고 명시**. Exner 반영은 하천/범람원 GAIA 계산에서 수행. 고운사 전사면의 직접 강우박리로 생긴 DEM lowering를 native feedback한다고 주장하면 오류. 수관 interception ablation 없음.
- 판정: **엔진3개라는 이유로 탈락 철회**, 하지만 5cm 경사면 cellwise full-process fit 낮음.

### G. Cea et al. (2024), Iber+
- https://doi.org/10.1016/j.envsoft.2024.106098 ; 정확 저자 배포 바이너리 https://doi.org/10.57745/UFEK4L
- true 2D SWE, rain & overland flow detachment, loose layer, multiclass suspended/bed transport, deposition, morphodynamic conservation. Soil erosion test T1 DOI10.57745/2WH9AL 에서는 **5cm along-slope x 2m cross-slope quasi-1D mesh**, 5cm x 5cm 자유 2D 검증 아님. T2 평균 면적 약 0.036m2이지만 cell 최소 길이 미확인.
- dynamic LAI canopy storage / leafdrip 강우침식 native 미입증; 공개 데이터+실행 바이너리 != GPU 계산 소스 (일부 코드는 공동연구자 한정).
- 판정: **가장 강한 별도 2D erosion/Exner 재현 benchmark, 단일 canopy-hydro-erosion 모델로는 부족**.

## 5. 기타 기존 모델
SHETRAN은 canopy+erosion native지만 5~10cm 논문 적용 및 수치시험 미확인; 0.648ha 전체10cm는 native NELEE 제한. EUROSEM original은 canopy throughfall/leafdrip KE 있으나 1D slope-channel 및 이전 수지 문제. Wflow.jl은 LAI/Gash/Rutter/leafdrip KE 강하지만 sediment는 방향망 라우팅. DHSVM original native code에도 leafdrip/sediment 있지만 현재 공개 C판의 나지 raindrop detachment 조건문/식생 맵 참조 문제와 D8 routing 존재. PSEM 2005 실제 5cm true 2D erosion이지만 interception 제외. FullSWOF 2015 HR 2D는 canopy 및 정확 수정 code 미확보. SWEHR 원본에 canopy-Rutter new coupling 필요. SEIMS 동적 LAI/leafdrip 미연결, directional route, unit concerns. CASC2D-SED base C는 forest 2014 canopy improved paper exact engine 아님. SMODERP2D native sediment-exner code 미확인.

## 6. 최종 분리 판정
- **단일 논문 물리의 완성도**: Kim2013 > Maggioli2022 > LongHe2009/2010 > Wei2017.
- **실제 저자 통합코드/테스트 자료 확보**: Feng2026/Jiang2025/Iber+2024가 강하지만 공간해상도 또는 필수 과정에서 실패. LISEM 자체는 Work가 오류검증 중.
- **아직 단일 동일 논문/동일 공개 실행판에 '수관 ON + 5~10cm true free-XY + rain/flow erosion & percell deposition + sediment/bed stock stability' 검증이 끝난 후보는 없다.** 이를 기성판 실패 전체 또는 개발불가능의 증명으로 확대하지 않는다.
- 우선순위: (1) Kim tRIBS-FEaST exact research solver 존재 여부 (2) Long-He published exact solver and native mesh (3) Wei 2017 forestry release (4) separate Work classic LISEM QA. 반대로 이미 탈락한 SHETRAN sub10cm 임의 확대를 최선책이라 반복하지 않는다.

## 7. 관련 기존 파일
- ../models/tRIBS_FEaST.md
- ../models/Iber.md
- ../models/Long_He_2D_Gash_Morphodynamics_Code_Audit.md
- 2026-10-27_MAGGIOLI_2022_EXACT_CODE_INPUT_PROVENANCE_AND_VALIDATION_AUDIT.md
- 2026-10-27_WEI_2017_FOREST_TREX_CANOPY_SPLASH_2D_INTEGRATED_90M_NO_CODE.md
- 2026-10-27_LAST_CHANCE_2026_FENG_ELM_TELEMAC_GAIA_30M_SOURCE_VS_SINGLE_NATIVE_GATE.md
