> **[연구결과 판정 수정, 2026-10-26]** 이 문서의 38회 모의는 원본 McGuire et al. (2016) SWEHR 식생 모형이 아니라 **외부에서 임의 공간입력 및 임의 식생계수를 연결한 수정 포크**의 공학적 시험이다. 수치 물수지와 유사수지가 통과했다고 원논문의 Rutter 수관차단 또는 독립 강우충격 차폐가 구현되거나 검증된 것은 아니다. 4.2배 등 수치는 억새와 참나무 맹아의 실제 침식률에 관한 연구결과로 채택하지 않는다. [공식 SWEHR V1.0 원본과 구현차이 확인](2026-10-26_OFFICIAL_SWEHR_V1_0_ORIGINAL_CODE_PROVENANCE.md).

# 2026-10-26 실제 공간형 SWEHR 결합모형 38회 검증: 밀생 억새 대 산발 참나무 맹아

## 결론
밀생 억새와 산발 참나무 맹아를 2D 공간별 수문/침식 입력으로 구분하는 **새로운 coupling**을 SWEHR 공개 C 소스의 원래 지배방정식 위에 실제 추가한 뒤, 5개 강우강도(10,20,30,40,50mm/h)×4개 공간배치 20회, SF 기부 집중 10회(그중 기본 30mm/h 2회 포함), 과정별 분리 8회 총 **38회의 서로 다른 실행**을 하였음. 38/38 물수지, 원토양-퇴적층-부유사-경계배출 독립 유사수지, 지형변화-퇴적층 수지 통과. 일부 30mm/h 수간유하우 집중은 기본 20회 이외 2회, 나머지 8회는 과정별 분리와 함께 실행됨.

**이 결과는 실측 고운사 지형/식생/토양 자료 없이 만든 물리적 가상실험이며, 억새 또는 참나무의 실제 토양유실량이거나 검증된 종별 침식 억제율이 아니다.**

## 실행/소스 원형
- 원본 SWEHR C: `csdms-contrib/swehr` Git SHA `4e6f783f335ac6dc1c116ef0d516c2f3d1b911e2`.
- 실험 브랜치: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/spatial-vegetation-runoff-erosion-20261026/experiments/rainfall_10_50
- 실행 스크립트 `spatial_patch_swehr.py`, 소스 변화는 초기조건 명시, 원본 강제 물/유사 유입 경계 제거, 지형 입력, 2D 격자별 강우 및 침투/거칠기/침식계수 연결, 38개 시험 수지 적산.
- 실제 실행 22개 https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40264048008
- 과정별 대조 16개 https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40264354578
- 전수 검증+영구 보존 https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40264757325
- 결과 CSV 영구 저장: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/spatial-vegetation-runoff-erosion-20261026/experiments/rainfall_10_50/spatial_patch_experiments/verified_20261026/summary.csv
- 원본 QA JSON 영구 저장: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/spatial-vegetation-runoff-erosion-20261026/experiments/rainfall_10_50/spatial_patch_experiments/verified_20261026/full_qa.json
- 공간 식생 마스크 ASCII와 요약 Markdown도 동일 디렉터리에 저장.

## 공간조건과 경계조건
- 실제 Gounsa 지형 래스터/종별 포기·그루터기 분포 파일은 검색 가능한 repo main 또는 시험브랜치에 없었음. 그러므로 13×25격자, 0.5m 해상도, 총면적 81.25m²의 **새로운 가상 사면**을 생성. 지형식 z=4+0.25 jdx +0.009 (idx−3m)² [m], 기본 경사 약 14°, y 하류 j=1 투과 경계, 나머지 측면/상류 wall. 네 공간배치 모두 동일 지형.
- 밀생 억새 가상 94.77% 식생격자 vs 산발 참나무 가상 9.23%; 별도 40%/40% 횡방향 식생대 vs 고립 패치에서 식생점유면적을 정확히 같게 고정하여 배치효과를 분리.
- 입력된 soil roughness/erodibility는 실측 뿌리량과 별개; **노출 격자** Ks=1×10⁻⁶m/s, n=0.08, rainsplash a=.25, ad=.25, cohesive stream-power J=30; **식생 격자** Ks=4×10⁻⁶m/s, n=.18, a=.07, ad=.10, J=90. 전부 임의 가정/가상 민감도. Root cohesion, RLD, litter, spall 암편은 정량적으로 직접 구현되지 않음.
- 수관 저장은 식생격자당 최대 0.8mm/event; SF 켤 때는 가상 수관격자 강우의 10%를 가까운 포기/그루터기 기부 격자로 전달하여 질량보존. 이는 본 연구에서 개발한 결합부이지 원본 SWEHR의 SF physics가 아님. Drip KE 없음. SF는 splash detachment source에서 제외.
- 'Flowlength'는 각 종방향 열의 연속 노출격자 길이를 나타내는 간단한 공간구조 지표로, 2D 계산된 실제 runoff pathway나 정량 sediment connectivity와 동일하지 않음.

## 1시간 강우당 경계 토사배출량 [t/ha/event]
| mm/h | 밀생 억새 | 산발 참나무 | 40% 횡방향 연결 | 40% 고립 패치 |
|---:|---:|---:|---:|---:|
| 10 | 0 | 0.0000095562 | 0.0000004867 | 0.0000008005 |
| 20 | 0.0000104196 | 0.000282849 | 0.000122768 | 0.000128012 |
| 30 | 0.000542655 | 0.002290642 | 0.001285687 | 0.001459800 |
| 40 | 0.002587428 | 0.009802719 | 0.005760072 | 0.007753348 |
| 50 | 0.005360528 | 0.024403561 | 0.014772224 | 0.020823571 |

## 1시간 강우당 경계 지표유출수심 [mm/event]
| mm/h | 밀생 억새 | 산발 참나무 | 40% 횡방향 연결 | 40% 고립 패치 |
|---:|---:|---:|---:|---:|
| 10 | 0.0000124 | 2.80008 | 0.14349 | 0.234082 |
| 20 | 1.64108 | 12.04658 | 8.29746 | 8.29993 |
| 30 | 10.08662 | 21.66091 | 17.72646 | 17.68581 |
| 40 | 19.22002 | 31.38584 | 27.32948 | 27.26992 |
| 50 | 28.57346 | 41.15861 | 37.00796 | 36.93633 |

같은 면적 40% 상태라도 50mm/h 고립 패치 유실량은 횡방향 연결형보다 40.96% 큼. 유출수심은 오히려 고립 패치가 약간 적으므로 유출량만으로 침식차이를 환산하면 안 됨.

## 30mm/h에서 한 과정씩 켰을 때
| 변화된 과정 | 밀생 억새 runoff mm | 산발 참나무 runoff mm | 밀생 억새 배출 t/ha | 산발 참나무 배출 t/ha |
|---|---:|---:|---:|---:|
| canopy only | 22.10414 | 22.77018 | 0.002352617 | 0.002638041 |
| hydraulic only (Ksat+n) | 10.76809 | 21.73192 | 0.000674828 | 0.002318150 |
| detachment only (a+ad+J) | 22.84150 | 22.84159 | 0.001258601 | 0.002665953 |
| combined | 10.08662 | 21.66091 | 0.000542655 | 0.002290642 |

**물리적 해석은 실험조건에 종속됨.** 우점종 자체를 의미하는 coefficients가 아니며, 같은 식생 상태에서 root RLD, litter mass를 실제로 넣은 결과도 아님.

## SF 공간 재분배 효과
SF on/off 토사배출은 30mm/h dense grass 0.000542655→0.000542078t/ha, scattered oak 0.002290642→0.002290056t/ha. 수량보존적 SF 재배분 총량은 30mm/h 각각 0.231m³ 및 0.0225m³(두 군락의 가상 수관격자 수 차이). **SF 기부 국지 집중으로 물의 공급위치는 바뀌지만**, 이 조건의 영역 전체 배출량은 거의 달라지지 않았음. 기부 수리전도도, 미세지형, root macropore/실제 SF 및 Drip KE가 미관측인 한 일반적인 stemflow erosion 효과 유무를 결정할 수 없음.

## 수치 검증
38/38 PASS.
- 최대 상대 물수지 오차 `4.15e-11`.
- 최대 원토양 박리-퇴적층-부유사-경계 유사수지 오차 `1.16e-13`.
- 최대 지형고도 변화-퇴적층 유사수지 상대오차 `4.67e-05` (약 0.00467%).
- 질량수지 통과는 수치적 보존이며, 격자크기/시간간격 수렴성이나 현장 관측 정확도를 증명하지 않음. 유사단위 t/ha/event는 boundary exported sediment only. Gross detachment와 혼동 금지.

## 최종 판정과 기존 모델선정
- **밀생 억새와 산발 참나무를 같은 단일 COVER로 처리하는 기존 비교는 폐기**. 실제로 가상 공간지형을 따로 주면 차이를 계산할 수 있는 원본 물리모형 결합구조가 확인됨.
- 밀생 억새가 적은 침식을 보이는 정성 방향은 이 선택한 가상조건에서 지지되지만, 4.2배/4.6배라는 숫자는 현장 식생·토심·수리전도도·암편·입도·실제 강우분배를 보정한 결과가 아니며 **고운사 실제 유실비라고 주장 금지**.
- Iber+ 중심 production 모형선정을 변경하는 내용이 아니다. SWEHR spatial coupling은 engineering process proof of concept임.
- 다음 단계: 고운사 DTM, 식생 포기/맹아 위성/드론/TLS 지도, 식생별 실제 수관차단/적하 KE/SF 기부수문, 뿌리 RLD, litter/rock spall, Ksat/soil depth, mesh refinement, outlet sediment/TLS를 확보한 뒤 site-level simulation 검증.
