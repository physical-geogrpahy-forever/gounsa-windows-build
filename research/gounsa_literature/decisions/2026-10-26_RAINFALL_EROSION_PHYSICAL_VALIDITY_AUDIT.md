# 2026-10-26 강우 10–50 mm/h 조건 원본 모형 침식량 물리적 타당성 감사

## 결정 요약
**이전 10–50 mm/h 1시간 수치 실험의 SWEHR 및 EUROSEM 토양유실량을 고운사 결과로 채택하지 않는다.**
단위 오류뿐 아니라 유동/침식경계, 물수지/유사수지, 초기조건, 코드 재현성 문제다. 논문 저자의 본래 검증 결과까지 폐기하는 것은 아니다.

## 원본 실행과 소스
- SWEHR: https://github.com/csdms-contrib/swehr, `4e6f783f335ac6dc1c116ef0d516c2f3d1b911e2`. 원본 source code 3x51 cells dx=0.25 m F=0.004 a=ad=0 Ks=0, rainfall source input originally zero; 10–50 intensity 3600s separately 재실행.
- EUROSEM: https://github.com/TheSoilman/EUROSEM, `8652944da6e1e8436495aa0c08765e2399830dd7`, Lahey F77 code formatting fixed without changing physical equations. Test case 2 plane elements, 100m*145m + 10m*145m =15950m², slopes S=0.85, cover=0.15, FMIN=5mm/h, G=400mm, source TFIN=88min (60min of rainfall + 28min recession).
- Experiment branch: rainfall-sensitivity-original-models-20261025; archived native simulations https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40202181315 and https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40203485045 ; independent postprocessing https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40253018836.

## SWEHR 원본 3×51 정렬 수정 후 비교
| 강우(mm/h) | 지표고도감소 양수 체적(m³) | 지표고도상승 양수 체적(m³) | 최대 단일셀 고도감소(mm) | 비고 |
|---:|---:|---:|---:|---|
|10|0.0190675|0.5492899|100.61| 원본 example a=ad=0, F=0.004, Ks=0 |
|20|0.0190680|0.5503770|100.61| |
|30|0.0190677|0.5518571|100.61| |
|40|0.0190679|0.5518155|100.61| |
|50|0.0190683|0.5527363|100.61| |

일관되게 총고도증가 체적이 감소체적의 약 29배. 토사 유입 경계 적산, 초기 지형 처리, 고정 경계/수면 변화 검토 없이는 물리적 토양침식으로 인정 불가. 특히 원 코드에서는 `U[1]`, `SOLID`, `M`의 명시적인 initialcondition 설정이 확인되지 않았음. C 런타임 메모리 0 초기화를 기대해서는 안 됨. 원본 코드 j=1 유동 유출(transmissive), 나머지 세 경계 solid. 유사농도 및 외부유입 검증 필수.

**중요 정정:** 예제 a=ad=0이라도 흐름박리 F=0.004가 살아 있으며, 단순 '침식이 0이어야 함' 검사는 옳지 않다. 또한 지표고도 차이에는 초기 지형 전처리 효과가 섞일 수 있으므로 독립적인 침식 유출물질 적산 없이는 고도변화를 전부 '토사수송'으로 단정하지 않는다.

## EUROSEM native per-event audit
| Rain (mm/h) | Gross interrill detachment (kg, available plane outputs) | Net erosion/deposition (kg, available plane outputs) | Basin runoff (mm) | Native water balance error (%) | 판정 |
|---:|---:|---:|---:|---:|---|
| 10 | 0 | 0 | 0 | 0 | 조건부 설명 가능; 현장 예측 아님 |
| 20 | 349.739 + 34.168 = 383.907 | 1.511 + 1.511 = 3.022 | 0.00020 | -0.0299 | 수지 가능 범위, 그러나 native 반복 실패 경험 |
| 30 | 47,294.051 + 5,930.220 = 53,224.271 | 47,063.613 + 5,923.694 = 52,987.307 | 0.48426 | 12.8593 | **reject** |
| 40 | 15,305.124 (first plane only) | 15,291.573 (first plane only) | 1.26776 | 28.8924 | 불완전 결과, **reject** |
| 50 | result missing | result missing | missing | missing | segmentation fault(-11) |

30mm/h gross detachment normalized to area = 33.3694 t/ha/event. **이 값은 exported sediment yield가 아님**. 만일 두 요소 net 52,987.307kg을 유출구 밖 exported yield로 *가정*하면, runoff 0.48426mm*15,950m² ≈7.724m³이므로 ≈6,860 kg of solids/m³ of runoff water가 요구됨. 입자밀도 2600kg/m³를 사용하면 고형물의 혼합물 체적비가 약 72.5%이며, 일반적인 dilute sheet flow로 볼 수 없음. 이는 '이 값이 실제 sediment yield라는 주장'에 대한 조건부 반증이지, gross detachment나 net erosion의 실제 배출량이 곧 그만큼이라는 증거는 아님. 평탄한 범람원 같은 외부 유사 집중/토석류를 모형이 해석하는 상황도 아님.

30mm/h 수지오차 12.86%, 40mm/h 28.89%은 보정 파라미터 선택 수준을 넘어 기각 사유. 테스트 사면 경사 0.85(약 40.36도)는 고운사 미관측 경사이고 15% 피복은 두 식생 시나리오로 확정한 값이 아님. 20mm/h run error -0.03% 하나만으로 안정적 결과라 할 수 없음.

## 침식량 실측 논문과 비교: 해석 기준을 엄격히 분리
1. Johansen et al. (2001) DOI 10.1002/hyp.384: 60 mm/h artificial rainfall, severe burned forest sediment yield 76 kg ha⁻¹ mm-rain⁻¹, unburnt 3kg ha⁻¹ mm⁻¹. Burnt about 25x; 120mm cumulative applied across repeated tests. 조건 특정 실측, 고운사 10–50 mm/h 예측곡선 아님.
2. Samoil et al. (2026) DOI 10.1007/s11368-026-04226-8: 185±17.1mm/h 30min artificial rainfall; mean sediment yield unburned 1.78g/m² =0.0178t/ha, moderate burn 105g/m²=1.05t/ha, high 529g/m²=5.29t/ha (different sample sizes). 현장 실측. 비슷한 피복/경사/강우 아님.
3. Shin et al. (2024) DOI 10.3741/JKWRA.2024.57.6.421: Gangneung WUI RUSLE 0.07–94.9t/ha/storm, SEMMA 0.24–83.6t/ha/storm. **모형 예측값**이지 현장 실측 아님. 시험지역 토심 0.70±0.22m, 벌크밀도 0.89±0.09g/cm³, 급경사와 암편이 많은 고운사 사암 사면으로 전이 불가.
4. Kinner & Moody (2008) DOI 10.3133/sir20075211: burnt hillside 1m² experiments, about 20,35,50mm/h, 50mm/h에서 steady infiltration 약 20–35mm/h. 강우가 10mm/h면 무조건 유출 없음/50mm/h면 특정 runoff량이라는 법칙이 아님.

## 단위 및 범위 판정
- erosion 1 t/ha/event = 0.1 kg/m², dry soil bulk density rho_b=1300kg/m³ 가정 시 균일 침식두께 0.0769mm.
- 1mm 균일 침식은 rho_b=1300kg/m³에서 13t/ha.
- 1mm runoff over 1ha = 10m³ water/ha. 면적당 유사량과 물량의 단위 비교에서 gross detachment vs delivered sediment must be separated.
- 기후/복원 차이 및 공급토심 차이를 무시한 고정 t/ha 임계치를 만들지 않음.
- 3 t/ha/y 연평균 산림 침식 비교값은 single-event t/ha/event와 직접 비교할 수 없음.

## 전체 후보 모형별 원본 출력 여부 및 토사량 판정
| 원 논문/모형 | 식생에서 강우분배 | 침투 및 runoff | erosion | 10~50 고운사 침식량 판정 |
|---|---|---|---|---|
| Rutter / Gash | YES interception and canopy paths | NO | NO | 원래 직접 산출 불가 |
| Xiao 2000 / 2007 | YES | Xiao 2007 일부 수문 처리 | NO | 원래 직접 산출 불가 |
| de Wergifosse 2020 HETEROFOR | hourly SF/TF/evaporation | soil horizon flux, **no surface runoff** | NO | 직접 침식 불가 |
| Charlier 2009 (MHYDAS stemflow) | SF 집중 유출 함수 | plot runoff YES | NO | 직접 침식 불가 |
| Apip 2008 | DT/SF/LD effective rainfall | distributed/lumped hydrology | YES rainfall/flow-driven, 1D | 원본 실행값 없음 |
| EUROSEM 1998 | canopy partition incl SF | infiltration+1D routed runoff | YES | 실행출력 numerical QA reject |
| McGuire 2016 SWEHR | source example no stemflow | 2D + infiltration, example Ks=0 | YES | 실행출력 numerical QA reject |
| WEPP | interception/plant growth, root erodibility | YES | YES hillslope rill/interrill | 이번 실험 미실행 |
| OpenLISEM | interception and throughfall hydrology | YES raster | YES | 이번 실험 미실행 |
| Li & Tian 2026 KE | drop-energy partition | NO | rain detachment KE forcing only | 직접 토양유실량 불가 |
| Wischmeyer 2024 LiDAR canopy | drainage pathways | NO | NO | 직접 침식 불가 |
| SEMMA/RUSLE comparison | statistical vegetation cover/NDVI | NO event runoff flux | YES by empirical index | 다른 강릉지역 모형 범위만 있음 |

## 고운사 다음 단계 품질 통과 요구
1. 사상별 incident P = storage change + interception evaporation + TF + SF exact water budget; 단위 m 또는 kg.
2. 줄기별 SF에 대한 공간 집중과 infiltration vs preferential flow 분리.
3. 격자별 2D 물수지 rainfall - infiltration - outgoing + incoming - final water, 수치 오차 진단. 권장 수치 정확도 목표 상대오차 1% 이내(연구용 시험 임계치, 문헌의 보편 허용치가 아님).
4. gross soil detachment, redeposition and delivered suspended+bedload separately [kg] and volume [m³], sediment budget relative residual recommended ≤5% in quality-check prototype (출판모형 내장 허용치 아님).
5. 0 rainfall/0 erosion/flat slope/convergent hillslope/control and mesh/time resolution convergence.
6. bulk density, rock fragment, depth, slope, root/litter/stem structure measured inputs. 네 후보 식생조건(억새, 참나무 맹아, 뿌리 조건, 통제 조건) 비교에서 식생 피복 15% 고정 예제값을 사용하지 않음.

## 최종 결정
이전 시뮬레이션으로 생산한 t/ha/event 및 그림을 고운사 정량 연구결과에 재사용하지 않음.
소스 및 문헌은 여전히 후보지만 '모든 모델에서 10–50 mm/h 침식량 검증' 달성이라 기술하지 않는다.
결합 시 기존 published equations를 유지하고, 줄기수간유하 물공급 위치와 2D 유수침식 연결은 새로운 coupling으로 별도 명시한다.
