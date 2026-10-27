# 서지정보
Maggioli, L., Rodríguez-Caballero, E., Cantón, Y., Rodríguez-Lozano, B., & Chamizo, S. (2022). Design Optimization of Biocrust-Plant Spatial Configuration for Dry Ecosystem Restoration Using Water Redistribution and Erosion Models. *Frontiers in Ecology and Evolution*, 10, 765148. https://doi.org/10.3389/fevo.2022.765148

# 이 논문을 찾은 이유
고운사의 필수조건 10cm 이하 + LiDAR DTM + LAI 관련 수관저류 + 강우사상별 지표유출 + 침식모의를 하나의 published model에서 결합한 실증사례를 검증하기 위해. 2026-10-27의 'cm급 수관차단/침식 선례 미확인'이라는 기존 결론을 직접 반박한다.

# 연구 유형
스페인 건조지역 사면 현장 TLS 변화관측(2014-07 및 2015-12) + 이벤트 LISEM 매개변수 보정 및 침식량 비교 + 가상 식생패치/biocrust 분포 시나리오. 원문 전체 HTML 본문을 직접 검토.

# 공간 구조
25m×15m = 약375m² 실험사면. 현장 TLS 5cm DTM, **LISEM 계산도 5cm 격자**, 강우사상 내부 **1초 시간간격**. 논문 명시: 유출은 **kinematic-wave routing**이며 이것만으로 full 2D SWE/4방향 자유유출 구현을 입증하지 않음. 격자맵의 2D 공간분포와 2D 유체 수치해석을 엄격히 구분.

# 적용 환경
남부 스페인 알메리아 석회암 채석 훼손사면. 자생식생은 주로 거친 포기 형태의 alpha grass (Macrochloa tenacissima)와 관목; bare soil, vegetation, biocrust 패치. 고운사의 억새(Miscanthus)와 **종이 다르므로 동일 매개변수 직접 전용 불가**.

# 핵심 과정
강우사상별 수관저류 관련 LAI, 침투(Green-Ampt), 비피복/식생/생물토양피막 별도 침투특성, kinematic-wave 지표 유출, LISEM 침식 및 유사 이동, 식생 패치별 runoff source/sink. 18개 유출발생 강우사상을 개별 모의, 18개월 총 지형변화(DoD)로 침식 총량 비교.

# 식생 입력
TLS 5cm 셀의 식생점/전체점 비율로 식생 피복 파악, LAI는 실제 잎점 직접 광학역산 아닌 **피복도에서 경험식으로 추정**해 모델 수관 수분저장능력 계산. 식생높이 TLS 수직 범위, 보호 피복/식생 패치 25×25cm 및 50×50cm, 뿌리 기여 토양점착력과 거칠기 변화. LAI와 canopy interception parameter의 구현체/버전별 상세 원본 경로 **논문에 기재되지 않음**; 모델 기재는 LISEM, 특정 OpenLISEM 실행 버전 태그가 아님.

# 핵심 식
LAI vs cover: Ramírez et al. (2007) 계열 경험식 사용; 원문 수식이 HTML에서 이미지 처리되어 정확 계수 전체 미전사, LAI 계산의 명시된 1.99 계수만 확인. Green-Ampt 침투. 흐름은 kinematic wave. 심층 SWEs나 자동 DEM 업데이트가 이 논문 5cm 실험에서 입증된 건 아님.

# 파라미터와 단위
DTM/input 0.05m, event timestep 1s; 원강우 5분 강우계; 가상 강우강도 15, 55mm/h 각30분; 식생 군집 0.25×0.25m/0.50×0.50m. 초기 토양 3cm biocrust 및 아래 3–30cm 층 설정. 원문 보고 18개 강우사상 총 침식예측 3.55t, 총 침식량 비교 오차 RMSE 17.79%(논문의 성능표현). 정확 DOF/오차식은 본문 표 정의 이상으로 해석하지 않음.

# 원 논문의 구현 범위
**5cm+수관차단 LAI 추정+침투/유출+침식의 실증 일체는 참**. 실험 결과의 검증은 18개월 전체 침식량에 대한 사후 TLS와 비교이고 5cm 격자별 국지 침식·퇴적 및 18회 각 이벤트 후 DoD 검증은 아님. 5cm 계산 시간간격 수렴/유사질량수지는 본문에서 미확인.

# 고운사에 직접 사용할 수 있는 부분
초고해상도 TLS의 지형/식생점 분류, LAI 및 식생높이 산출, 사면 식생 패치 2차원 구성, 단일모델 사상별 유출-침식의 유력한 **직접 선행연구**. 현재 고운사 SHETRAN 주모델만 고집하는 근거를 해제하되 별도의 LISEM 소스버전 안정성 감사 필요.

# 새로운 coupling이 필요한 부분
원본 분포형 routing이 4면 수리학적 2D 흐름인지 검증, 현장 수관 적하/수관저류 매개변수와 지표 식생/암편 및 부피밀도 현장 입력 제약, 원본 버전 고정과 time/dx convergence, cm급 DoD 격자별 비교.

# 한계
Maggioli(2022)의 버전과 OpenLISEM 7.5.2는 같다고 주장 불가. 기존 7.5.2 원본 고운사 2D 5m 유사수송 대규모 시간간격 비수렴 NO-GO는 그대로 유지. kinematic wave가 네방향 자유유출의 genuine 2D hydrodynamics을 만족한다고 말할 수 없음.

# 최종 판정
**채택: 핵심 published 5cm 연구 선례. 주모델 코드 선정은 보류(원본 실행버전 미확인, 수리학 2D와 7.5.2 수치결함 미해결).**

# 참고 링크 / DOI
https://doi.org/10.3389/fevo.2022.765148
https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.765148/full

## 2026-10-27 개발 계보 확인
원문 https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.765148/full 의 `Model Selection` 절은 모델을 `LISEM (Limburg Soil Erosion Model)`로 표기하고 `Jetten and De Roo 2001` 및 초기 LISEM 연구를 인용하며 **kinematic-wave routing**을 설명한다. 따라서 **고전 LISEM / OpenLISEM classic 계열** 사용 가능성이 높다. 하지만 **어떤 classic 실행 버전**(200x LISEM, 201x OpenLISEM 등)인지는 원문 미기재이므로, 실제 `v7.5.2` 또는 신형 `LISEM v0.x`를 썼다고 단정 불가.


## 2026-10-27 원문+당시 GitHub 원본 상세 재감사 (이전 결론 보완)

### 실제 원문 방법론 검증
- Maggioli et al. (2022), Frontiers 본문 §Model Selection: **LISEM은 5cm DTM을 동일한 5cm 계산격자로 사용**, 1초 단위 시사상 유출 및 침식 맵 생성. 유동은 저자가 명시한 **kinematic wave routine**. 따라서 자유로운 X/Y 2D SWEs에서 모의했다는 이전 해석은 원문에 위배.
- §Vegetation Related Variables: TLS 5cm 픽셀의 식생 classified point 비율을 cover로 산출, Ramírez et al. (2007) 피복 기반 경험식으로 LAI 추정, 수관저류용량에 사용. 실측 LAI가 아니라 **피복 유래 간접추정**. 해당 논문에서 canopy ON/OFF만 바꾸고 Ksat, cohesion, cover/roughness를 동일하게 통제하는 수관차단만의 인과실험은 제시되지 않음.
- §Calibration: 원시 48개 이벤트 중 유출을 발생시킨 **18개**를 계산, 2014~2015년 사면의 18개월 TLS 변화에 기반한 **총침식량**으로 PSI(건조/습윤 초기조건 90/20cm) 보정. 다음 동일 기간 총량으로 예측 3.55t vs 관측 2.81t 비교, 논문은 'RMSE 17.79%' 보고. **다른 강우사상 독립 holdout validation이나 매 격자 DoD RMSE가 아님**. RMSE 17.79%의 분모·정의는 식/표에서 직접 확인되지 않았으므로 우리가 새로 정확도 계산했다고 주장 금지. `validation`이라는 원문 표현만으로 독립 검증으로 격상하지 않음.
- §Soil Surface: under-plant D50=5 μm, root extra cohesion 9.48kPa, Ksat vegetation25mm/h vs bare3mm/h (biocrust10mm/h). **식생 시나리오의 침식 차이는 수관차단만의 효과가 아니라 침투, 토양강도, 조도/피복 효과가 중첩**.
- §Data Availability: 저자들이 요청시 원자료 제공 가능하다고 기술하지만, **논문에 DOI/공개 GitHub/즉시 다운로드하는 5cm runfile, *.map inputs, original executable/commit 링크 없음**. 광범위 public search에서도 matching dataset 발견하지 못함. 이는 존재하지 않는다고 증명한 것은 아님.

### 2022-02-11의 실제 OpenLISEM GitHub 소스 독립검증
- 같은 **논문 발표일 2022-02-11**의 `vjetten/openlisem` public commit `3b0264ef557c031fe39fb6d523c3669bf6e1296a`: `include/version.h` **6.837 beta** (blob b590659e30e8429ea27b5b69ff75fc00abf3e33f).
- 역사적 `lisInterception.cpp` blob `571ea19061c4a81f2cf2696594814f1829180bf8`: `CanopyStorage`, `kLAI`, `LeafDrain`, `CStor`, `RainNet`, litter storage 구현.
- `lisErosion.cpp` blob `ffe013e2bf67ccd816305b5bc1891d6032bb9528`: `cell_SplashDetachment` separates directrain, canopy leaf throughfall, plant height KE; `SwitchKinematic2D==K2D_METHOD_DYN` selects 2D sediment input.
- `lisSWOF2DSediment.cpp` blob `591054b501f57b2f7ff7517ba25d3371171665ac`: `SWOFSedimentDetNew → SWOFSedimentFlowInterpolation → SWOFSedimentSetConcentration`; `lisOverlandflow.cpp` blob `770b9942f513547885f053c12cf24a7165a16f93` independently shows `K2D_METHOD_KIN` LDD branch **and** `K2D_METHOD_DYN` FullSWOF branch. **소스에서 두 solver 존재**와 **Maggioli 5cm 실험에서 2D solver 사용**은 전혀 다름.
- **과거 코드에도 settling velocity 분기 문제 후보:** `lisErosion.cpp::GetSV` d<100 μm에서 Stokes, d≥100 μm에서 `double dm=d/1000.0` 계산. 미터 변환 `d/1e6`과 다르고 100μm 경계에서 비정상적 velocity jump 발생할 수 있음. 2026년 7.5.2의 고운사 100μm 오류와 계보상 일치하는 취약점이다. **하지만 Maggioli 원문 D50=5 μm이므로 이 사실만으로 2022 논문 시뮬레이션이 잘못되었다고 결론내리지 않는다.**
- 공식 공개 `vjetten/openlisem` release의 `openLisemSetup_7.5.2.exe` asset 갱신일은 **2026-10-15**이고 v7.5.2 label 자체는 2026 계열. 발표일의 GPL 소스는 6.837 beta, 고운사 native Windows 7.5.2는 별도 구현시점/실행판. **6.837 또한 Maggioli가 직접 사용한 정확한 SHA라는 증거는 없음**. 재현하려면 저자 당시의 원본 프로그램/설정 및 입력 데이터 확인 필수.

### 추가 확인한 2026년 7.5.2 1초 재검증 작업 상태
- [GitHub Actions 40304815539](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40304815539) 의 1/2/5/10/20초 확장 재시험: GitHub job `121511206049` 은 **20분 timeout, 실패**. 해당 로그에서 일부 10/20초 결과를 복구했으나 `2D_GATE_MISSING` 1초/2초 다수. 그러므로 **1초에서 비수렴이 해결되었다거나 1초에서 실패가 입증되었다고 양쪽 모두 주장 금지**.
- [2m reference run 40303685346](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40303685346) 도 **30분 timeout 및 `RuntimeError: NO_VALID_SIMULATIONS`**. 이는 2m 비수렴이 성립한다는 판정이 아니라 **완전한 유효 native QA 미확보**를 뜻함.

### 원본 재현 및 주모델 채택에 대한 엄격 결론
- 5cm+LAI canopy+rain/erosion published example **확인**. 그러나 **운동파 유동, 사상 간 독립검증 없음, 사용자 요구 free 2D 미달, exact version/input archive 없음, 과거 수정판 7.5.2에서 실제 dt nonconvergence**.
- 고운사 단일 원본모델로 지금 즉시 **채택 불가**. 2022 snapshot 6.837에는 full 2D 코드가 있지만, 저자 사례의 5cm free 2D 검증으로 인용하면 안 됨.
- 다음 단계는 (1) 해당 연구판 유래 자료가 실제 별도 공개되었는지 특정 또는 (2) 별도 공개된 published genuine 2D+canopy+5cm erosion benchmark 검증이지, 기존 탈락 실행판을 논문 존재만으로 재승인하는 것 아님.

### 확인한 원본 및 근거 URL
- https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.765148/full
- https://github.com/vjetten/openlisem/commit/3b0264ef557c031fe39fb6d523c3669bf6e1296a
- https://github.com/vjetten/openlisem/blob/3b0264ef557c031fe39fb6d523c3669bf6e1296a/include/version.h
- https://github.com/vjetten/openlisem/blob/3b0264ef557c031fe39fb6d523c3669bf6e1296a/lisInterception.cpp
- https://github.com/vjetten/openlisem/blob/3b0264ef557c031fe39fb6d523c3669bf6e1296a/lisErosion.cpp
- https://github.com/vjetten/openlisem/blob/3b0264ef557c031fe39fb6d523c3669bf6e1296a/lisSWOF2DSediment.cpp
- https://github.com/vjetten/openlisem/releases
