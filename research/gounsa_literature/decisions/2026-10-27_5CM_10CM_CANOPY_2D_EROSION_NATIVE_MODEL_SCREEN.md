# 2026-10-27 고운사 5–10cm 수관차단 + 2D 유동 + 침식/퇴적 단일 공개 원본 문헌 재탐색

## 사용자 핵심 요구조건
- 5–10cm 이하 실제 계산한 **published** 강우사상 침식 사례 (DEM 관측 1cm라고 계산 1cm 아님).
- LAI 관련 강우 수관저류 및 배수/수관통과/적하 실제 수문 물수지 계산.
- X/Y 자유로운 2차원 유동 및 격자 간 유사수송과 국지 퇴적 (2D DEM 위 D8 또는 단일 steepest-descent kinematic routing으로 대체 불가).
- 단일 모델, 실제 공개 원본 코드, 계산 안정성/유사수지, forest/grass canopy 공간비교. LiDAR 관측 cm원해상도 유지하되 모델 5–10cm 가능.
- 과거 기각 OpenLISEM Classic7.5.2 source 2D sediment Δt 불안정, SWEHR native Rutter 누락, new LISEM git 0.2.3 main/0.2.5 develop canopy·rain_m 연결 문제는 부정하지 않음.

## 현재 매우 직접적인 문헌
1. **Maggioli et al. 2022**, DOI https://doi.org/10.3389/fevo.2022.765148: LISEM **5cm**, TLS DTM 및 초본 패치 cover→LAI→canopy storage, 1s, 375m², 18 강우사상, 침식물량/식생배치 비교. 논문의 **kinematic-wave routing**은 자유로운 2D SWE 입증 아님. 공개 7.5.2의 계산 문제가 자동으로 해결되는 것도 아님. **초고해상도 canopy+erosion 실증 최고 근거지만 full native 조건 부족**.
2. **PSEM_2D Nord & Esteves 2005**, https://doi.org/10.1029/2004WR003690: true 5cm 2D SWE + 강우/유수박리+퇴적, 하지만 저자가 'No direct vegetation effects (interception, roughness)' 명시. **탈락**.
3. **Epple et al. 2025**, https://doi.org/10.1002/esp.70127: 새로운 LISEM 1cm 실제 유동과 DoD 검증, 3m² 미만 경운 시험포. 실제 수관저류 활성 증거 없음. 본 프로젝트는 cm급 유속 microbenchmark를 필수로 요구하지 않아 우선순위 낮음.
4. **Cooper et al. 2012 MAHLERAN-MiC**, https://doi.org/10.1029/2012JF002499: 원문 실제 **0.3m** (13.75×6.5m), marker-in-cell soil transport, vegetation 있다면 interception loss/throughfall/leaf drip KE 스케일식 존재. 0.3m 시험은 실제 나지 모래판이라 canopy 효과를 현장에서 함께 검증하지 않음. 유출 2D 기하격자라도 각 셀 single-steepest cardinal kinematic routing, 자유로운 SWE 아님. 원본 다운로드 대신 개발자에게 요청: https://draem.webspace.durham.ac.uk/software/ . **탈락**.
5. **McGuire et al. 2016 SWEHR**, https://doi.org/10.1002/2016JF003867: paper Rutter canopy와 shielding/2D Hairsine-Rose, **2.5cm TLS 원 DEM을 실제 37.5cm 계산격자로 집계**. CSDMS 공식 C 소스에는 논문 Rutter canopy/영향식이 누락. 2026-10-26 기존 소스감사와 동일 **탈락**.
6. **Kim, Ivanov & Katopodes 2013 tRIBS-OFM/FEaST**, https://doi.org/10.1002/wrcr.20373: Rutter canopy water cycle/true 2D FV SWE+Hairsine Rose original/deposited layer, published Lucky Hills 10 events. **10m×1m 0.005m² 삼각형 (~7cm 상당)** 유사수송 benchmark 있음, 그러나 **그 시험은 hydro/vegetation off, prescribed upstream water/sediment** (paper §4.2). 현장 Lucky Hills 풀모듈 격자 <=10cm 근거 없음. 현행 공개 https://github.com/tRIBS-Model/tRIBS v6는 Rutter interception 원본 C++ src/tHydro/tIntercept.cpp 있지만 Hairsine-Rose/sediment solver 검색 0. 완전체 저자 당시 source **미확보**. 이미 archive `papers/2013_Kim_Ivanov_Katopodes_tRIBS_OFM_HairsineRose.md`/models/tRIBS_FEaST.md에 별도 상세 기록 존재. **탈락(공개완전체)**.
7. **Kivva & Zheleznyak 2005**, https://doi.org/10.1615/InterJFluidMechRes.v32.i6.50: 초록 직접 canopy interception + 2D nonstationary shallow water + infiltration + wash-off sediment deposition, Butenya flood verification. 본문 전체/격자 크기/LAI formulation/코드 다운로드 **확인되지 않음**. 새로운 `papers/2005_Kivva_Zheleznyak_2D_Runoff_Interception_Sediment.md`. **탈락(10cm/source)**.
8. **USACE GSSHA** https://www.erdc.usace.army.mil/Media/Fact-Sheets/Fact-Sheet-Article-View/Article/476714/gridded-surface-subsurface-hydrologic-analysis/ : 공식 canopy interception + diffuse-wave 2D overland runoff + raindrop runoff detachment + sediment deposition **same available executable**. 그러나 published GSSHA applications typically 10m or more and **<=10cm sediment plus canopy scientific example not confirmed**. canopy parameters initial vegetation storage/fraction vs explicit LAI leafdrip energy different; full source identity and <=10cm original QA not established. **탈락 현재 해상도 선례 기준**.
9. **SERGHEI-SE Braga, Martínez-Aranda & García-Navarro (2026)** https://doi.org/10.3390/w18151870 : recently published **0.005m=5mm** lab erodible dam-break, valid 2D SWE + deposition + dynamic bed feedback; authors explicitly identify vegetation coverage as **future extension**; rainfall runoff benchmarks are 1m, not 5mm. Thus 5mm is NOT proof 5mm interception and rain-induced erosion simultaneously. Existing archive paper 2026_Braga_SERGHEI_SE_Finite_Volume_Evaluation.md requires note that this is incompatible native canopy model. **탈락**.

## Final defensible answer
검색/원문 및 공개 source 감사 범위 안에서는 **5–10cm 이하를 실제 실행한 논문 + native dynamic canopy LAI water budget + free 2D XY SWE + sediment detachment/transport/deposition + reproducible matching open original**을 **모두 동시에** 만족한 사례 미확인. 모델이 물리적으로 불가능하다는 뜻 아님. 침식 5cm 사례(PSEM)와 canopy+erosion 5cm (Maggioli) 존재하지만 원래 코드/수리차원 검증 미완결.
추가 문헌보다 과거 검증불일치의 원인 해결 없이는 모델 채택 불가. 원래 코드 가용성 있는 단일모델 표준 우선.
현재 논문구현 간극이 가장 큰 후보는 `Maggioli 2022 실제 LISEM 실행버전`, `Kim 2013 저자 FEaST 전체코드`, `Kivva 2005 저자 코드`; 모두 공개 경로 확인 없으므로 **실행 가능 모델 추천 아님**.

## 2026-10-27 추가 종합 판단 주의
- MAHLERAN 30cm 시험의 식생 수관차단은 **같은 시험에서 입증되지 않았음**. 2D mapped grid와 genuine 2D SWE를 구별.
- Kim2013 0.005m² 삼각셀은 대표 길이 약7.1cm이나 **hydrology disabled boundary forced benchmark**임.
- SERGHEI-SE 5mm 격자는 dam-break erodible flume이고 canopy not present, **rain event + canopy 5mm 실증 아님**.
- GSSHA 공식 전체 hydrology and sediment architecture 존재를 새로운 코드 QA/10cm native success로 치환 금지.

## 관련 신규 문헌 기록
- ../papers/2005_Kivva_Zheleznyak_2D_Runoff_Interception_Sediment.md
- ../papers/2012_Cooper_Wainwright_MAHLERAN_MiC_30cm_Interception_Drip.md
- 기존 ../papers/2013_Kim_Ivanov_Katopodes_tRIBS_OFM_HairsineRose.md
- 기존 ../papers/2026_Braga_SERGHEI_SE_Finite_Volume_Evaluation.md
