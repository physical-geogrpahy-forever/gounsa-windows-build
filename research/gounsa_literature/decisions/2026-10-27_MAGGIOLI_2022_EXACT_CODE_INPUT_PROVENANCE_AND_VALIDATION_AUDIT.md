# 2026-10-27 Maggioli et al. (2022) 5cm LISEM 실제 논문판과 공개 소스 일치성 심층검증

## 1. 결론
**논문에서 타 연구자가 5cm 격자에서 식생 피복→LAI→수관저류+강우유출 및 침식 시뮬레이션을 실제 수행했음은 확인. 그러나 고운사에서 요구한 진정한 X/Y 2D 유동은 해당 연구에서 사용하지 않았고(원문상 운동파), 코드 버전/모의입력 미공개 및 독립적인 사상별 침식/퇴적 검증 부재이므로 사용자 요구를 충족하는 실제 재현용 주모델로 선정할 수 없다.**

핵심은 문헌/소스/실행증거 세 층을 서로 혼동하지 않는 것.

## 2. 2022 원문 (1차자료) 직접 대조
DOI https://doi.org/10.3389/fevo.2022.765148
- **스페인 알메리아 채석장 훼손사면**, 25×15m≈375m², 2014년 7월과 2015년 12월 TLS 지형 관측. 종은 `Macrochloa tenacissima` 등 초본, 참나무 맹아+억새 산림패치 아님.
- §Model Selection 원문: 5cm TLS DTM이며 LISEM 모델도 5cm 실제 계산, 1s **맵 산출 및 모의 시간해상도**. **주의: 이 문장만으로 내부 적응시간스텝 `dt=1s` 고정이라고 확정하면 안 된다.** 유동은 원문 표현 `kinematic wave routine`.
- §Vegetation Related Variables: 분류된 TLS vegetation-point/total-point 비율로 격자 피복 산출; Ramírez et al. (2007) 식으로 LAI 근사, canopy storage capacity 연결. LAI 직접 실측 아님.
- §Infiltration: Green-Ampt, bare Ksat 3mm/h, vegetated Ksat 25mm/h, biocrust Ksat10mm/h.
- §Soil: D50 5μm, vegetated `COHADD=9.48kPa`. 비교 패치는 canopy storage만 ON/OFF한 교차실험이 아니라 Ksat, roughness, cohesion 등의 상태를 함께 달리함. **수관차단의 독립 인과효과는 논문에서 입증 안 됨.**
- §Model Calibration: 동일 2014~15 강우사상 18회와 그 기간 종료 지형 DoD로 보정해 총량 **observed 2.81t vs modelled 3.55t**를 비교. 원문 'RMSE 17.79%'는 독립 holdout 검증이 아니며 **5cm cell-wise erosion/deposition map accuracy도 아니다**. 17.79%가 어떤 분모/표본에 대한 통계인지 원문 확인된 식이 없어 별도 해석 금지.
- §Data Availability: `raw data ... will be made available by the authors, without undue reservation`. 하지만 시계열 input csv / 5cm raster input *.map / runfile / old LISEM binary / SHA / Zenodo or GitHub DOI가 **논문 내 명시되지 않음**. 외부 검색에서도 해당 논문과 직접 연결된 reproducibility bundle 발견 못 함. 원자료가 영원히 비공개라는 추정 금지.
- exact LISEM software version **원문 미기재**. OpenLISEM Classic 계보로 보이나 신형 Bastian van den Bout LISEM0.2.x가 아님(그 모델계열은 이후 개발).

## 3. 동일 발표일 역사적 공개 소스 확인 (GitHub connector direct read)
- `vjetten/openlisem` archived historical Git SHA **3b0264ef557c031fe39fb6d523c3669bf6e1296a**, commit created **2022-02-11** (논문 발표일). `include/version.h` = `6.837 beta` (blob `b590659e30e8429ea27b5b69ff75fc00abf3e33f`). **Maggioli가 이 exact SHA를 실행했다는 증거는 없다!**
- `lisInterception.cpp` SHA `571ea19061c4a81f2cf2696594814f1829180bf8`, L43–93: `CanopyStorage`, `kLAI`, `CStor`, `LeafDrain`, `RainNet`, litter storage.
- `lisErosion.cpp` SHA `ffe013e2bf67ccd816305b5bc1891d6032bb9528`, L121–273: direct rain, leaf-drip KE, separate splash detachment, vegetation and stone masks, `K2D_METHOD_DYN` path.
- `lisSWOF2DSediment.cpp` SHA `591054b501f57b2f7ff7517ba25d3371171665ac` L73–91: 2D sediment detachment/deposition, interpolation/advection.
- `lisOverlandflow.cpp` SHA `770b9942f513547885f053c12cf24a7165a16f93` L46–83: `K2D_METHOD_KIN` / `K2D_METHOD_KINDYN` (kinematic) and `K2D_METHOD_DYN` (FullSWOF) **both branches present in 2022 public code**. Source capability ≠ 5cm study tested solver; paper explicitly selects kin wave.
- `lisErosion.cpp::GetSV` L100–119: d<100μm Stokes, d≥100μm `dm = d / 1000.0` then Zanke instead of converting μm to m; **100μm 경계 수치문제의 계보상 후보가 당시 원본에도 존재**. 하지만 해당 논문 D50=5μm라 이것만으로 논문 모의가 오류라고 단정 금지.
- 2026 현재 OpenLISEM official Github release `v7.5.2` installer asset modified **2026-10-15**; 따라서 2022 논문의 실행판이라는 논리적 연결은 성립하지 않음. 2022 소스 6.837 beta와 2026 7.5.2 동일성 주장 금지.

## 4. 기존 고운사 원본 실행 실패와 1초 판정
- 7.5.2 native 2D 5/10/20s 12회 고운사 실험에서 유사유출량 3자릿수 이상의 시각격자 민감도 및 토사재고 위반. [기존 실패 판정](2026-10-26_OPENLISEM_752_NATIVE_2D_STABILITY_FAILED.md), 성공적 재선정 근거 없음.
- 직접 읽은 GitHub Actions [1/2초 확장 40304815539](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40304815539): job `121511206049` **20min timeout failure**. 로그에 `2D_GATE_MISSING` 1초 및 2초 다수, 표준 dt=1s 고운사 완전 유사수렴 시험 **성공/실패 모두 미판정**. 연구 논문이 1s time resolution이라고 했다고 7.5.2 안정성을 추정할 수 없음.
- [2m grid expanded QA 40303685346](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40303685346): job `121507441094` **30min timeout**, quality.py `NO_VALID_SIMULATIONS`. 이는 2m 원본 물리자체의 불합격 증거가 아니라 **유효 simulation 완료 실패**임. 이전 보고서의 '추후 확인' 조건을 이 결정으로 해소.
- 이 세션에서는 **새 native LISEM 컴파일/실행이나 Maggioli inputs 재현을 수행하지 않았다**.

## 5. 최종 주모델 엄격 선별
| Requirement | Maggioli original 2022 published | 2022 GitHub public source (different provenance) | 7.5.2 native Gounsa |
|---|---|---|---|
| 실제 5cm 계산 | PASS | 실행 사례로 확인하지 않음 | 기존 검증 5m |
| LAI canopy | PASS (input and capacity) | CODE EXISTS | CODE EXISTS |
| direct/leaf drip splash | 기능계보 및 LISEM erosion | CODE EXISTS | CODE EXISTS |
| freely 2D SWE same 5cm run | **NO (kin wave)** | CODE EXISTS but unpublished matching benchmark | 5m native but numerically failed |
| erosional/depositional validation at each cell | **NO** | N/A | gross stock/timestep failure |
| exact program+inputs matching paper downloadable | **NOT FOUND** | public different SHA/snapshot | different 2026 version |
| full requirement PASS | **NO** | **NO** | **NO** |

## 6. 다음 실제 실행방향
원본 사용 우선 기준을 유지한다면, Maggioli는 'published 5cm kinematic+canopy+erosion'의 방법론 레퍼런스로만 사용. 정확 실행판+5cm 입력을 재현할 수 있는지 확인될 때까지 **이 논문을 고운사 fully matching single native engine으로 채택하지 않는다**. Genuine 2D + 5cm + canopy + deposition을 모두 mandatory로 하면 현재 확인된 published/open matching executable 없음.

새로운 원본을 임의 수정/서로 결합/새 매개변수 채움으로써 full-pass로 포장 금지.

## 근거
- [2022 Maggioli canonical paper](../papers/2022_Maggioli_RodriguezCaballero_LISEM_5cm_TLS_LAI_Interception_Erosion.md)
- https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.765148/full
- https://github.com/vjetten/openlisem/commit/3b0264ef557c031fe39fb6d523c3669bf6e1296a
- https://github.com/vjetten/openlisem/releases
- https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40304815539
- https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40303685346
