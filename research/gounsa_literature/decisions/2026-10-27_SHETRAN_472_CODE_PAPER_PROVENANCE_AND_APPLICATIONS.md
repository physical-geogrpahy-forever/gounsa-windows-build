# 2026-10-27 SHETRAN 4.7.2 원본 코드의 연구 계보 및 실제 침식 적용 연구

## 질문 및 판정
고운사 0.648ha 합성사면의 SHETRAN 4.7.2 강우사상 모의가 기존 어떤 연구의 원본 코드에 기반하는지, 그리고 유사한 고해상도 사면/산림 연구가 있는지 확인.

**결론:** [nclwater/Shetran, commit cf9cd540](https://github.com/nclwater/Shetran/tree/cf9cd540add78ad3accbaf62b4199d2032887f6b)는 `CMakeLists.txt`에 `project(SHETRAN VERSION 4.7.2.0)`을 명시하는 2026년 공개 원본 Fortran이다. 단일 독자개발 프로그램이 아니라 SHE→SHESED→SHETRAN 장기 개발 계열이다. 현재 (\mathrm{SYmod.f90})에는 침식 코드 개발 이력 1993–1995, 2008년 Fortran90 포팅 및 2026년 리팩터링 기록이 남아 있다. **2026 SHA의 바이너리 그대로를 사용했다고 기록한 출판 논문은 이번 조사에서 확인하지 못했으며, 아래 논문들은 물리식의 원전 또는 구 SHETRAN의 적용 연구**다.

## 원본 확인 경로
- https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/CMakeLists.txt : SHETRAN version 4.7.2.0.
- https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/src/sediment/SYmod.f90 : source `SYOVER`, `SYCOLM`, `SYOVTR`, `SYBC`, `BALSED`, historical header and documented physical module.
- https://github.com/nclwater/Shetran/blob/cf9cd540add78ad3accbaf62b4199d2032887f6b/examples/Cobres/model/input_cob_syd.txt : `SY11` size classes, `SY22 GKR/GKF`, `SY24 XDRIP/DRDRIP/FDRIP`, `SY41 FCG`, `SY42 FCROCK`, `SY51 DLS` etc. Input header `SY02 4.2.7` is legacy data syntax and **is not the 4.7.2 solver version number**.
- [기존 35회 개방경계 검증](2026-10-27_SHETRAN_OPEN_FOUR_SIDES_0P648HA_35_SCENARIOS_NATIVE.md). 원본 물리식 + 진단/배열 수정을 거쳐 수행한 실험이다.

## 논문별 계보와 적용 구분

| 문헌 | 연구/계산 대상 및 방법 | 실제 결과와 한계 | SHETRAN 4.7.2 관계 |
|---|---|---|---|
| Wicks & Bathurst (1996), Journal of Hydrology, doi:10.1016/S0022-1694(96)80012-6 | SHESED: 강우/수관적하/시트류 박리+공간 이송 및 하도수송; Iowa 5.1ha/6.4ha 사건 유사량 | 시간 유사량 재현, 새 rill 형성은 제외 | 현재 SY 침식/이송식의 원형 출처 |
| Ewen, Parkin & O'Connell (2000), J Hydrologic Engineering, doi:10.1061/(ASCE)1084-0699(2000)5:3(250) | SHETRAN Version 4 체계: 3D 수문/다입경 유사/용질 통합 | 통합 모델의 공식 모델설명 근거 | 현재 모델 명칭/핵심 구조 대표 인용 |
| Lukey et al. (1995), Physics and Chemistry of the Earth, doi:10.1016/0079-1946(95)00056-9 | Rimbaud 산불 전후, Laval 침식황무지와 재조림 가상시나리오 | 피복 변동에 따른 유사량 변화와 저항 불확실성 범위 검증 | 식생피복-유수침식 초기 사용 계보 |
| Bathurst et al. (1998), IAHS Publ. 249:129-136, https://iahs.info/uploads/dms/10992.129-136-249-Bathurst.pdf | Draix 0.133ha 단위 골침식 지형 **5m 격자**, 단일셀 모델, 86ha 유역 비교 | 사건 유량/유사량을 오차범위 내 모의, 토양저항의 규모전이에는 재보정 필요 | 고운사 0.648ha/4m와 적용규모가 가장 가까운 사례 |
| Lukey et al. (2000), Journal of Hydrology, doi:10.1016/S0022-1694(00)00260-2 | 프랑스 Laval 86ha 및 Brusquet 108ha의 산림 복원 반사실 비교 | 관측 5년의 유출/강우비와 유사량 두 자릿수 차이를 대체로 재현, 계수 불확실성 잔존 | 산림복원/수관+지표보호 효과 적용 |
| Norouzi Banis et al. (2004), Hydrological Processes, doi:10.1002/hyp.1447 | 3–5ha 2개 경작지의 30년 ^137Cs 공간침식 실측 대비 SHETRAN | 측정 평균 연침식률 6.5 및 10.4t/ha/y; 공간패턴 평가 | 내부 침식량 공간검증 접근의 근거 |
| Adams et al. (2005), Hydrological Processes, doi:10.1002/hyp.5670 | 뉴질랜드 970m² 사면 대형 강우모의, 토양수분/유출수문곡선 검증 | R² 약 0.98 수문곡선, 수리전도도와 마찰계수 보정. 수문 검증이 주결과 | 소규모 사면 수문검증 선례 |
| Adams & Elliott (2006), Hydrological Processes, doi:10.1002/hyp.6050 | 같은 지역 2002–2003 대형 강우실험의 유량/유사유량곡선 및 직접강우/유수박리 계수 보정 | 여름/겨울 계수 차이, 방목 후 직접강우 박리 증가를 설명; 유사는 수문보정에 민감 | 단일 강우 사건 침식 검증에 가장 밀접 |
| Birkinshaw et al. (2011), Hydrological Processes, doi:10.1002/hyp.7900 | 칠레 35ha La Reina 산림/벌채, 50m 141셀, 1997–1999 vs 2000–2001 유량/유사 모의. LAI/CK/Cb/수관저류/지표피복/적하높이 변수 분리 | 산림 3.6, 벌채 8.3t/ha/y 모델 유사유출; 토심과 강우극값에 따라 유량 보호의 상대효과가 달라짐. 유사 실측 부족 | **식생 수관차단과 강우 침식 통합의 가장 직접적 적용 근거** |
| Op de Hipt et al. (2017), Water, doi:10.3390/w9020101 | 부르키나파소 Dano 126km², 2014/2015 관측유량·탁도/부유사 보정, 침식공간지도 | 수문 통계 0.66–0.79 범위, 검증 유사량 NSE 약 0.2; 2014년 유사 공급 약 68% 하도, 32% 사면 | 학술논문에 SHETRAN DR/Dq 코드를 명시하고 공간 E/D 지도 제작; 유사 검증능력 한계도 분명 |
| Escobar-Ruiz et al. (2019), Hydrological Processes, doi:10.1002/hyp.13550 | 영국 농업유역 50m 격자, 15분 자료 및 사건별 유사량/수문곡선 비교 | 유량보다 유사 예측이 취약, 퇴적/유사첨두가 격자 크기에 민감 | 사건별 공간수렴/현장 관측 중요 |
| Sreedevi & Eldho (2021), IJRBM, doi:10.1080/15715124.2020.1767637 | Netravathi 1/2/4km SHETRAN 유출/유사 계산 해상도-매개변수 전이 실험 | 유량 예측은 가능해도 유사량은 재보정 없이 격자 변경에 민감 | 고운사 4m→2m→1m 동일영역 수렴/매개변수 감사 필요 |
| Sreedevi et al. (2022), Catena, doi:10.1016/j.catena.2022.106427 | 인도 서고츠 산지 787km², 1km 격자 및 LULC/기후변화의 유사유출 분석 | 과거 토지이용만 바꿀 때 유사량 −10.4%, 기후만 +1.7% (해당 연구 기간/설정) | 산림 포함 산지 유역 적용 사례. 고운사 미세사면 직접 검증은 아님 |

## 고운사 141mm 퇴적의 물리적 해석
- 강우가 50mm/h×3h면 **사상 총강우 150mm**이며 50mm 총량이나 50m가 아니다.
- 개별 격자에 141.487mm의 느슨한 퇴적층 변화가 발생하는 것은 **국지 유사 집중에 의해 물리적으로 가능**하다. 반드시 강우깊이보다 작아야 할 보존법칙은 없다.
- 4m×4m 격자의 141.487mm는 격자 기하학적 표층 체적 약 `2.2638m³`. 공극률/입경별 DLS 정착 여부에 따라 고체 유사 체적으로 환산할 때 차이가 발생한다.
- 50mm/h 혼재 ON 유사 박리 공급 `25.069872m³ solid`, 경계 배출 `21.404709m³ solid`(현재 실험); 특정격자 최대값이 질량보존에서 바로 탈락하는 값은 아니다. 그러나 그 차이 전체를 퇴적으로 간주하거나, 동적 지표고도 갱신/토양고갈 완전성으로 간주해서는 안 된다.
- DLS 저장량(느슨한 퇴적층) 변화와 실제 안정된 지형고도/토심 변화는 구별할 것. 최대값이 비현실적이라고 선험적으로 단정하지 말고 경계/수송능/지형과 초기 재고의 증거로 판단할 것.

## 논문 인용 및 실험 기록 권고
- 모델 정식인용: Ewen et al. (2000).
- 침식 및 수관적하 물리식: Wicks & Bathurst (1996).
- 수관-산림 변화 사례: Birkinshaw et al. (2011), Lukey et al. (1995, 2000).
- 국지 강우/수문 및 유사 검증: Bathurst et al. (1998), Adams et al. (2005), Adams & Elliott (2006).
- 공간 E/D 도표: Op de Hipt et al. (2017), Norouzi Banis et al. (2004).
- 원본 구현 직접인용: `nclwater/Shetran` SHETRAN 4.7.2.0 원본 commit SHA 와 별도로 진단패치 명시.
