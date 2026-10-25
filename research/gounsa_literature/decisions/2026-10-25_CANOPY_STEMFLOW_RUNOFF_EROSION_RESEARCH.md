# 2026-10-25 수관 강우 재분배와 유출-침식 연결 문헌 판정

## 목적
고운사의 억새형 초본 및 참나무 맹아와 산불 후 산림에서 수관차단, 직접 수관통과우, 수관적하우, 수간유하우가 침투 및 2차원 지표유출과 강우박리/유수박리까지 어떻게 연결되는지 원 논문 기준으로 검토한다. 소프트웨어 탐색이나 작동 모형 가공은 이 문서의 목적이 아니다.

## 논문별 확인된 구현 범위
| 논문 | 차단/수관통과/수간유하 | 국지 SF→침투·지표유출 | 침식/퇴적 | 판정 |
|---|---|---|---|---|
| Morgan et al. 1998 EUROSEM | 명시적 세 성분 및 DT/LD 분리 | 국지 줄기별 공급장 미구현; NR에 합산 | rill/interrill 및 강우/유수박리 | 전과정 baseline; true 2D 아님 |
| Xiao et al. 2007 | 수관저류/통과/줄기 배수계수 | 공간별 단순 수문처리, 줄기기부 산림 검증 아님 | 없음 | 강우→유출 연결 선례 |
| Apip et al. 2008 | DT/SF/LD의 분리 및 NR 합산 | SF 위치별 우선침투 미구현 | DR/DF/수송 | 발표된 연쇄, 1D routing/250m 격자 |
| Charlier et al. 2009 | stemflow redistribution 함수, 전체 상세 수관 생리모형 아님 | 2구획 집중유입, 침투-유출 및 18사상 검증 | 없음 | 핵심 국지 SF→runoff 선례 |
| Liang et al. 2009 | 관측 기반 TF/SF 공간 입력 | 3D 토양수분 반응 | 없음 | 줄기기부 침투 연구 |
| de Wergifosse et al. 2020 HETEROFOR | 시간별 차단/TF/SF/저류 및 토양 수분 | 1시간 pedon 토양 물수지, 지표유출 자체 미구현 | 없음 | 식생-수문 경계 공급 후보 |
| McGuire et al. 2016 SWEHR 계열 | Rutter 수관저류/throughfall 및 drainage; 줄기별 SF 출력 없음 | 침투 Green-Ampt, genuine 2D SWEs | raindrop/flow entrainment, 다입경, deposition 및 형태변화 | 침식 핵심 published 모델, SF 새 결합 필요 |
| Li & Tian 2026 | 자유 통과/수관 튀김/적하 분해에 따른 KE | 미구현 | KE 경계만, 침식량 미구현 | 강우박리 KE 근거 |
| Chen et al. 2026 | SF/TF 실측 | 줄기열내/열간 유출 실측 | 토사유출 실측 | 뿌리와 침투능이 중요한 반례, 모형 아님 |
| Beven & Van Stan 2026; Di Prima et al. 2026 | SF 관측 및 분석 | macropore preferential infiltration 경로 | 없음 | 국지 SF 항상 runoff↑ 가정 반박 |

## 수문/침식 연쇄를 유지하기 위한 기술 조건
1. 수관 입력: incident rainfall P와 canopy storage의 물수지를 맞추고 free TF, drip TF, SF를 서로 중복 없이 분리한다.
2. 경계 공간보존: 각 나무 j의 SF 체적유량 Q_SF,j [m³/s]를 국지 공급 분포 w_j(x,y) [m⁻², 영역 적분 1]와 결합한다. p_ground [m/s] = p_TF(x,y,t) + Σ_j Q_SF,j(t) w_j(x,y,t). **이것은 본 연구에서 제안한 새로운 coupling interface이지 단일 출판모형의 구현이라고 주장하지 않는다.** w_j의 형태 및 면적은 현장자료로 정한다. 임의 반경 고정 금지.
3. 침투 경쟁: 동일 p_ground라도 뿌리 주변 macropore/soil hydraulic conductivity/소수성에 따라 infiltration-excess runoff와 fast preferential flow가 달라진다.
4. 유출: 수심 h와 2D 유량 hu를 갖는 연속식에서 p_ground-f를 순 공급원으로 전달한다.
5. 침식: 자유 통과/적하/튀김방울 KE는 raindrop detachment에, 유출에 의한 전단 및 stream power는 flow-driven detachment에 따로 전달한다. stemflow 체적을 빗방울 운동에너지에 중복 가산 금지.
6. 기존 SWEHR의 원토양/퇴적층 입도별 연속, armoring, 지형변화 방식 유지. 식생 biomass와 마찰/침식저항의 새 mapping은 별도 출판문헌의 근거 필요.
7. 시간해상도: 수관 출력은 hourly보다 높은 사상 내 강도 변동이 필요할 수 있으므로 침식 엔진의 내부 dt와 강우 출력 누적량을 맞추어 질량 보존을 검증한다.

## 이번 판정
- '세 강우 성분을 계산하는 생태수문모형이 없다'는 결론은 틀림.
- '세 성분+침투+유출+침식을 단일 발표 모형이 연결한 선례가 없다'도 틀림: EUROSEM 및 Apip et al. 사례 확인.
- 그러나 '개체별 수간유하 집중 위치와 줄기기부 preferential infiltration을 보존하면서 steep postfire genuine 2D 유동·침식까지 검증한 단일 모형'은 이번에 검토한 문헌들에서는 확인되지 않음. 전세계적으로 존재하지 않는다고 단정할 수 없음.
- 최종 모형 선정/폐기는 이번에 바꾸지 않음. 고운사 핵심 결손은 **공간 보존적 SF/TF 경계조건 및 수관적하 KE의 SWEHR 연동**임.

## 검증 계획
(1) 사건별 상부강우 P 및 저장/증발/DT/LD/SF 물수지
(2) 나무/억새 패치별 SF/TF 공간 맵 및 수관적하 KE
(3) 줄기 기부와 수관 사이의 침투능 및 초기 토양수분
(4) runoff hydrograph/timing/peak
(5) TLS 지형차분과 sediment size/deposition
(6) stemflow을 제거하는 대조 실험과 root macropore 경로를 끄는 대조 실험

## 우선 참고문헌
- Morgan et al. (1998), EUROSEM model 및 v3.6 guide
- McGuire et al. (2016), https://doi.org/10.1002/2016JF003867
- Charlier et al. (2009), https://doi.org/10.5194/hess-13-2151-2009
- Xiao et al. (2007), https://doi.org/10.1002/hyp.6482
- Liang et al. (2009), https://doi.org/10.1016/j.jhydrol.2008.12.009
- de Wergifosse et al. (2020), https://doi.org/10.5194/gmd-13-1459-2020
- Beven & Van Stan (2026), https://doi.org/10.1002/hyp.70556
- Di Prima et al. (2026), https://doi.org/10.1016/j.jhydrol.2025.134723
- Chen et al. (2026), https://doi.org/10.1016/j.still.2026.107362
- Li & Tian (2026), https://doi.org/10.5194/hess-30-3203-2026
