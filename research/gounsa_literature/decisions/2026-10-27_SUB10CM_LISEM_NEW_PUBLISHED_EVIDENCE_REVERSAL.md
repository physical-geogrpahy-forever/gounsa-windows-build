# 2026-10-27 긴급 논문재검토: '10cm 이하 + 수관차단 + 침식의 published study 없음' 오판 정정

## 결론 및 번복
**이전 2026-10-27 decisions/2026-10-27_SHETRAN_SUB10CM_CANOPY_EROSION_MODEL_SCREEN.md의 '수관저류/수관차단 + 침식 + 10cm 이하 published model 사례는 확인되지 않았다'는 탐색 결과는 불완전하였다.** 이후 원문 전체를 확인한 **Maggioli et al. (2022)**가 **5cm 격자 LISEM, TLS 기반 LAI 및 수관저류 추정, 강우사상 지표유출 및 침식**을 실제 실행한 학술 선례다. 또한 **Epple et al. (2025)**은 **1cm 격자 LISEM, SfM 실측 DoD 및 PTV 유속 비교, 수문-침식에 의한 DEM 시간별 피드백**을 실제 실행하였다.

이는 기존 'cm급 기능 유무'에 대한 판정을 명확하게 뒤집는 새로운 문헌. 다만 두 논문의 결과를 하나의 동일 SHA/실행 프로그램에서 검증한 '1cm 풀 canopy-2D-sediment all-in-one'으로 단정하면 안 된다.

## A. Maggioli et al. (2022)
https://doi.org/10.3389/fevo.2022.765148
- 25m×15m(375m²) 고해상도 토사노출 스페인 사면, TLS 5cm 두 시기(2014-07/2015-12); 같은 5cm LISEM 계산, 1초 시간격자. 18개 강우사상 개별 모의, 누적 지형변화 기반 총 침식 3.55t 예측 및 17.79% RMSE 보고.
- 식생 포기의 TLS 기반 cover/height→cover에서 LAI 추정→식생 수관저류능력 산정. Green-Ampt 침투, bare/biocrust/vegetation 별 침투 특성과 물의 redistribution, 침식 맵. 가상 시나리오 25cm×25cm 및 50cm×50cm 식생, 15/55mm/h 각 30분. 대상 alpha grass *Macrochloa tenacissima*, 억새 *Miscanthus*와는 별종.
- **중요 한계:** 원문 §Model Selection의 흐름은 **kinematic-wave routing**. 'genuine 2D Navier-Stokes/2D SWE 네 방향 자유유동'을 직접 입증하지 않음. 수관차단 storage와 동일해상도 작동은 논문이 기재했지만, leaf-drip 충돌입력과 각 cell 침식/퇴적 DoD independent validation은 논문에 제시되지 않음. 실행 버전/소스 SHA가 명확하지 않음.

## B. Epple et al. (2025)
https://doi.org/10.1002/esp.70127
- 독일 실제 강우모사 포 4개, 각 약 <3m². LISEM을 1cm 격자로 구동, 0.01/.025/.05/.075/.1m grid sensitivity, L은 사상 시간단계마다 DEM 지형고도 갱신, 실제 PTV 유속/두 시기 SfM DoD (M3C2-PM LoD 사용)와 비교.
- 1cm에서 식별된 일부 세류가 7.5/10cm에서는 사라짐. 실제 SfM DoD의 산재 hotspot 중 일부는 LISEM이 놓침.
- **중요 한계:** 작물/경운 시험포이고, **수관차단-적하를 1cm에서 실제 켜서 검증했다는 근거 없음**. 'LISEM (L 2024)'라고만 표기, 7.5.2 본 실행본과 SHA/코드가 동일하다는 증거 없음. 수문 및 유속/모형 DoD는 비교하지만 사상별 cm 피복 canopy+입경별 유사 수지의 수치 안정성 미검증.

## C. Naranjo et al. (2021): 동일 모형 계열의 수치 위험
https://doi.org/10.5194/hess-25-5561-2021
- OpenLISEM **v4.96**, 1/2/4/8/15m 격자별 유량/유사 민감도 검증. 4m만 유사배출 누계가 **440.9Mg**로 튀는 anomalous behavior를 논문 저자가 주의 명시(1m 191.9Mg, 2m 128.4Mg, 8m 38.1Mg, 15m 39.7Mg). 그래서 과거 자체 7.5.2 5m 유사수송 Δt 비수렴 NO-GO를 **자동 해제 금지**. 두 버전의 구체 결함이 같다고 단정하는 것도 금지.

## D. 다른 후보를 구별
- PSEM_2D 5cm (Nord & Esteves 2005): genuine 2D SWE, 박리/퇴적/지형고도 사상 내부 갱신, 그러나 원문 'No direct vegetation effects (interception, roughness)' 명시. 탈락.
- Iber+ (Cea et al. 2024, DOI 10.1016/j.envsoft.2024.106098): GPU 2D SWE, 다중입도 침식퇴적 및 original soil finite sediment supply, 실험/사면/유역 규모 검증. 적용 120m² hillslope 3300 elements(평균 면적 약0.036m²), 정식 canopy interception native 연동 및 실제 10cm 이하 고운사 유형 검증 **입증 전**. LISEM 문헌 대신 유력하다고 단정 금지.
- SHETRAN 4.7.2: native canopy/flow/sediment 결합 기본 물리식 검증되었지만 0.648ha 전구역 10cm raster를 기존 한계 NELEE=250000 안에 넣을 수 없고 sub10cm 발표 검증 미확인. 'SHETRAN source cap 수정 권장'은 사용자 선행연구 우선 조건 아래 적극 권고 철회.

## E. 현재 판정
- **실제 5cm 수관차단+침식 published precedent = YES (Maggioli2022)**.
- **실제 1cm LISEM runoff, erosion-generated bed change with SfM DoD/PTV validation = YES (Epple2025)**.
- **동일 공개 원본 버전에서 1cm + LAI/수관저류+leafdrip + true 2D 자유유동 + 유사수지 + 임의급경사 mixed canopy + cellwise DoD 엄격검증 = 아직 입증하지 못함**.
- 주모델 선정에서 우선 문헌 계보를 'LISEM의 출판 논문 명시 실행버전'으로 좁혀 연구자 구현/소스/수치 안정성 대조. 2026 v7.5.2 기존 native NO-GO 판정 유효하며 단지 지적 한계를 모른척 넘어가면 안 됨.
- 사용자 연구의 0.648ha vs 5cm => 2,592,000 셀, 1cm => 64,800,000 셀. Maggioli 375m² 5cm=150000 셀, Epple ~2.5m² 1cm~25000 셀 수준. 엄청난 규모 차이 존재. 국지 고해상도 시뮬레이션과 전사면 적용은 구분.

## 새 개별 MD
- ../papers/2022_Maggioli_RodriguezCaballero_LISEM_5cm_TLS_LAI_Interception_Erosion.md
- ../papers/2025_Epple_Bienert_Grothum_LISEM_1cm_PTV_DoD_Erosion.md
- ../papers/2021_Naranjo_OpenLISEM_DTM_1to15m_4m_Sediment_Anomaly.md

## 원문 링크
- https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.765148/full
- https://onlinelibrary.wiley.com/doi/10.1002/esp.70127
- https://hess.copernicus.org/articles/25/5561/2021/index.html
