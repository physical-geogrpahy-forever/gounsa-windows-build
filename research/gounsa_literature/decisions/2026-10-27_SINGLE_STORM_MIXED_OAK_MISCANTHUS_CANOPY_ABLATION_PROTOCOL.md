# 고운사 1ha 미만 혼재식생 사면의 단일 강우사상 국지 침식·퇴적 연구: 수관차단 유무 대조 설계

작성: 2026-10-27 KST. **2026-10-27 18:00 제출용 범위 고정.**
**우선순위: 이 문서가 전일 `2026-10-26_DEADLINE_GOUNSA_MODEL_ARCHITECTURE_AND_DATA_PLAN.md`의 잘못된 100년 식생천이·장기 풍화 중심을 대체한다.**
상태: 사상 모의 설계/원본 모형 검증 증거는 존재하지만, **LAI-Rutter-수관적하를 2D SWEHR에 결합해 고운사 관측 자료로 실행·검증한 결과는 없음**.

## 연구질문

**고운사 내 1ha 미만 한 개 사면(참나무 맹아와 억새가 실제로 함께 혼재하고 패치 배열이 불균일)에서 동일한 강우사상을 입력했을 때 수관차단 과정을 고려하는가에 따라 어디에서 침식되고 어디에서 퇴적되는가? 국지적인 강우박리·유수박리·퇴적 및 순 지표고도변화가 얼마나 달라지는가?**

연구영역은 동일한 mixed-species DEM 및 관측된 공간배치 그대로 고정. **'전부 억새 사면 vs 전부 참나무 사면' 비교 아님**, 100년 식생천이도 아님, catchment-wide 월·연 유사유출량 비교도 아님. 단일 강우사상 이벤트 스케일에서 셀별 `gross original-soil detachment`, `gross loose sediment redetachment`, `deposition`, `net surface change`와 출구 유사량 및 지표유출 경로를 동시에 계산한다.

## 실험안: 본 실험과 선택적 기작 분리

- **A 수관차단 OFF**: 수관은 물 저류·배수·적하·분리된 강우충격 에너지 계산에 관여하지 않음. 같은 강우가 직접 지표에 공급되고 원시 빗방울 에너지로 강우박리됨.
- **B 수관차단 ON (본 실험)**: 같은 강우에서 격자별 참나무와 억새의 관측 LAI/수관 형태에 따라 시변 `C`, 직접 수관통과 `P_direct`, 수관 배수 및 적하 `P_drip`, 가능하면 부착 위치를 확인한 `P_stem`, 수관증발 `E_c`를 **수량보존적으로 계산**. 지표에 들어온 직접강우와 낙하적하의 운동에너지를 구분하고 침식엔진에 입력한다.
- **C 수문효과만 ON (선택적 진단)**: B의 지표도달 수량과 시각/공간 유출경로는 쓰되, 강우충격 단위에너지 분할은 A와 동일한 가상조건으로 둔다. C는 실제 식생 상태의 물리적 독립예측이 아니라 수문/충격 기여도 **분리 진단**이다.
- 핵심 대비는 **B−A**. 수관의 hydrological storage/throughfall만 따로 보고 싶으면 C−A, leaf-drip/direct-splash energetic separation 효과는 B−C. 반드시 무엇을 켰는지 실험메타데이터에 기록한다.
- 세 실험 모두 **DEM, 경사, 토심, 토성, 표면 암편, 뿌리분포, 낙엽, 지표거칠기, 침투특성, 초기토양수분, 참나무/억새 실제 위치와 강우**를 완전 동일하게 고정한다. 수관 OFF에서 뿌리/낙엽/마찰/식생체를 제거해 버리면 canopy 효과 분리가 불가능하다.
- 추가 대조(선택): 동일 지도에서 `관측 crown LAI`만 변화시키는 민감도와 동일 LAI/수관형질 아래 crown spatial redistribution 실험. 이는 원 연구대상 배치를 대체하는 것이 아니라 보조 분석.

## 공간자료와 격자

- **대상지:** 고운사 경내/주변 연구사면 내부 실제 <1ha polygon, 현장좌표. 현재 본 저장소 main에 확인 가능한 실제 고운사 경계/지면 DEM 파일은 없음.
- **원시 지형:** ground DTM 또는 TLS/UAV photogrammetry ground point cloud에서 수관/얹힌 식생을 구분한 surface, 사상 전후 가능한 동일 기준점 지오리퍼런싱. DSM(수관표면)을 DEM으로 직접 쓰지 않는다.
- **공간표현:** 기존 0.25m SWEHR native narrow demonstration (3×51)은 충분한 mixed vegetation domain을 대표하지 못한다. 지형/포기 크기와 관측 정확도가 허용하면 **0.5m 셀을 출발 격자 후보**로 둔다 (1ha면 최대 약 40,000개 셀, 이 연구는 그 미만). 0.25m/1.0m 수렴 비교. 실제 격자는 자료 지원과 모델 안정성으로 확정하며 임의로 0.5m를 현장 실측해상도라고 하지 않음.
- **식생배치:** 억새 포기 polygon, 줄기/엽군 높이, 각 패치 LAI, tussock 안/사이 gap; 참나무 그루터기 centroid, 맹아 개수·수고·crown polygon, 잔존 rootstock, 낙엽 분포; 같은 셀 여러 수관층 중복 시 canopy water가 두 번 생성되거나 고강도강우가 이중차감되지 않는 계층 계산.
- **토양:** 토심/암반 노출(available original soil mass), 모래·미사·점토(2mm 미만 PSD), 지하석력 Fg와 지표 암편 Rs 분리, 초기 `theta`, 현장 `Ksat`, Green–Ampt suction, roughness, litter, root density/RLD. 연구자는 생물량을 피복률로 **대체하지 않는다**.
- **강우:** 동일 관측 폭우사상 `R(t)` 원시 시계열 (가능하면 1분 또는 그 이하), event start/end와 drydown time; 자료 미확보 시 10–50mm/h 1시간 synthetic pulses는 QA용이고 '고운사 실측 강우'가 아님.

## 활성 계산경로 (한 사건에 한함)

```text
[참나무 맹아+억새가 뒤섞인 단일 사면 지면 DEM] --- fixed z0, H0, soil / root / litter / rock / Ks
                 |
[동일 고해상도 강우사상 P(t)] --------- [식생 현장지도의 LAI, crown geometry, height]
                 |                                  |
                 +---- [OFF A: canopy bypass]       +---- [ON B: canopy C(t), D(t), throughfall]
                 |                                  |
           raw ground rainfall            water: direct TF, canopy drip, optional stemflow
           raw raindrop kinetic energy     energy: original raindrops + leaf-drip kinetic energy
                 |                                  |
                 +----------------+-----------------+
                                  |
                 [동일 2D shallow-water solver]
                       water + infiltration + routing
                        /                    \
              rainfall splash            flow detachment
                        \                    /
                 [size-specific sediment stock + 2D transport + deposition]
                                  |
               [grid local erosion E, deposition D, ∆z, outlet loss]
                                  |
             [B-A difference maps for each variable and source/sink location]
```

### 물리적/보존식 인터페이스
- 한 수관/격자에 대해 이벤트 적산 `gross precip volume = direct TF + canopy drained to ground + stemflow + canopy evap + canopy storage change` [m³]. 식생격자에서 줄기기부 위치로 수간유하우를 재분배했다면 격자별 자기강우와 지면공급은 **서로 달라질 수 있으나**, 전체 domain에서 수관저장과 지면공급은 같아야 한다.
- 수관저류량이 이벤트 종료 시 남아 있다면 손실로 버리지 말고 저장량으로 명시하거나 건조 뒤 배수 종료까지 같은 모의시간으로 추적. A/B 비교 결과 계산 종료 시각 동일.
- `P_direct`는 **원시 강우 운동에너지**를 갖고 `P_drip`는 낙하높이, 입경에 따라 다른 운동에너지를 갖는다. `P_stem`의 수량을 직접 빗방울 운동에너지로 환산 금지. 이미 고에너지 직접강우만 분리했으면 그 위에 `(1−Cv)+Tc Cv` 다시 곱하는 이중 차폐 금지.
- 각 격자 (i)에서 `E_orig,i` = 강우에 의한 새 원토양 박리 + 흐름에 의한 새 원토양 박리 [kg/m²/event]. `E_re,i` = 표면 퇴적층 재박리 (새 원토양 유실과 구분). `D_i` = 누적 총 퇴적 [kg/m²/event]. **E_orig − D만으로 자동 지형변화라고 쓰면 안 됨**: loose deposit layer의 시작/종료 상태와 입도별 재이동을 mass ledger로 정합화하고 각 재료의 건조 벌크밀도로 체적변환.
- 결과 maps: `E_rain`, `E_flow`, `E_orig`, `E_re`, `D`, `∆M_original`, `∆M_loose`, `∆z_surface` (mm/event), `max_h, max_shear, cumulative_runoff, flow connectivity`, outlet Q(t) and sediment export(t).
- 성과지표: 단순 유역 평균이 아닌 **두 시나리오의 같은 셀 차이** `∆E(x,y)=E_ON−E_OFF`, `∆D(x,y)=D_ON−D_OFF`, `∆z_diff=∆z_ON−∆z_OFF`. 식생 종류별 포기/그루터기 내부/바로 옆/패치 사이 노출 지표를 overlay로 분류하되 종별 독립 사면 시나리오 아님.
- 폭우사상 시간 내 모의 고도 피드백이 활성인지 SWEHR 코드 호출경로로 확인하고 구현 상태 기록; event end raster 산출만 가능한 버전을 '동적 rill incision 완전 구현'으로 주장하지 않음. 현재 SWEHR 공개원본 및 기존 fork가 mixed field Gounsa로 검증된 상태는 아님.

## 사용할 엔진과 source provenance

- **설계 후보**: 공개 2017 CSDMS SWEHR V1.0 2D SWE, Green–Ampt, Hairsine–Rose detachment/transport/deposition. 원본 7개 파일은 `main/third_party/SWEHR_original_v1_0_2017`. synthetic 경계 수정 fork 9/9, 38/38 mass closure 확인 (수관 LAI/Rutter/잎적하 energy 미구현); 이 결과는 local species field effect validation 아니며 local dx/dt refinement convergence 미완료.
- 새 수관 모듈: McGuire et al. (2016) DOI 10.1002/2016JF003867 §3.5의 published Rutter canopy storage/drainage와 §3.2 direct rainfall splash shielding을 토대로 **독립 복원/구현**; 그 논문의 실제 original vegetation C executable은 공개 SWEHR 2017과 동일하지 않음. `experiments/gounsa_deadline_20261027/canopy_event.py`는 standalone Python preprototype로서 SWEHR 결합/잎적하 KE 미구현, 자체 단위시험 미실행 또는 파일 존재만으로 통과 주장 금지.
- 원본의 2D 유동 및 침식 계산 안정성이 고운사 mixed-domain 전체에서 보존 + 수렴 시험을 통과하기 전 **최종 validated engine으로 선언 금지**.
- OpenLISEM 7.5.2: 2D 12 native tests severe dt nonconvergence/finite soil exceed; EUROSEM rilled native full sediment ledger residual 14-21% (dt15s) + 1D; SHETRAN dynamic canopy는 있지만 rill formation and local morphodynamics absent: 이 결함을 덮고 all-in-one 대체라고 주장 금지.
- LPJ-GUESS의 수년/수십년 식생천이, 풍화, 사면 creep, 장기 soil profile modelling은 **본 제출의 사건 엔진 필수 구성에서 제외**. 기존 고운사 큰 프로젝트에 필요할 때 연결 가능하나 본 단일사건의 측정된 식생 배치를 LPJ-GUESS 산출 100년 시뮬레이션으로 대체 금지.

## 검증 게이트와 필요한 산출물 (2026-10-27 18:00)

1. **입력 증거표**: 고운사 현장 AOI/ground DTM, oak resprout+tussock mask, LAI/height/Smax, soil/H/Ks/rock/PSD, actual event rain, validation TLS/runoff/sediment의 소유/경로/해상도/결측. 없으면 MISSING, 임의 가상입력은 SYNTHETIC.
2. **원본과 수정본 추적**: SWEHR source SHA, 직접 수정한 function list, Rutter water + direct/drip energy + true x-y boundary route + soil stock; original 기능 vs 신규 coupling.
3. **수관 모듈 QA**: ON/OFF 동일 강우 input과 서로 다른 지표유입 강도; all canopy/soil water stores + infiltration + boundary loss water conservation (rain 10–50mm/h and recession), zero LAI ON=OFF.
4. **침식/퇴적 QA**: all cell nonnegative original soil + deposited stock + suspended stock, both horizontal and vertical boundary flux ledger, mass residual threshold 0.1% or stricter if independently verifiable; material conversion rho and PSD; `∆t/2`, `∆x/2` convergence of local erosion/deposition maps as well as total sediment export.
5. **대상사면 공간 결과**: A and B erosion/deposition/net elevation GeoTIFF + B−A difference GeoTIFF. 차이 도식이 나오지 않았다면 'calculated Gounsa canopy effect'이라고 서술 금지.
6. **보고용 그림**: domain DEM shaded relief, observed vegetation patches, canopy gross/direct/drip/stem maps, streamlines and max h, A/B E and D maps with identical color scale, difference maps, conservation status.
7. 실제 현장강우/DTM 미입수라면 제출은 **구현계획 및 합성사면 검증**으로 명시하며 Gounsa measured site prediction 결과로 위장하지 않는다.

## 채택 근거/이전 오류 기록
- [실제 혼재식생 배치 필요성](2026-10-26_DENSE_MISCANTHUS_SPARSE_OAK_SPATIAL_COMPARISON.md).
- [2016 SWEHR 논문/2017 C 구현차이](2026-10-26_SWEHR_RUTTER_CANOPY_SHIELDING_SOURCE_AUDIT.md).
- [공식 코드 및 이전 synthetic fork 감사](2026-10-26_SWEHR_REPRODUCIBILITY_REMEDIATION.md).
- [38회 synthetic spatial mass closure, 실제 현장 수치로 오해 금지](2026-10-26_SPATIAL_NATIVE_SWEHR_DENSE_MISCANTHUS_SPARSE_OAK_38RUNS.md).
- [OpenLISEM 비수렴](2026-10-26_OPENLISEM_752_NATIVE_2D_STABILITY_FAILED.md).
- [EUROSEM rill sediment 실패](2026-10-26_EUROSEM_1998_NATIVE_SEDIMENT_LEDGER_RILL_FAILURE.md).
