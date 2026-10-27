# 2026-10-28 단일 레퍼런스 4대 모델 원문·현재 소스 깊이 재검증
- [4대 후보 정밀 감사 및 RDycore 코드 비교](decisions/2026-10-28_SINGLE_REFERENCE_4_CORE_MODELS_PRIMARY_PAPER_NATIVE_SOURCE_REAUDIT.md). Kim2013 tRIBS-FEaST는 한 논문의 실제 3-engine coupled 2D Roe-SWE-Hairsine–Rose+Rutter interception; 작은 0.005m² 삼각격자 두 시험에서 hydrology OFF, full basin smallest triangle ~5.56m², hydrology3.75min/erosion0.01s, 908셀 3시간 사상 264min wall. Table5 실제 canopy water store/throughfall coefficient 있음, 그러나 §4.3.5의 vegetation contrast는 Ksat/Manning 바꾼 실험이지 canopy-only ablation 아님. 현대 공식 tRIBS 원본은 Rutter 있으나 FEaST sediment source 미발견.
- Maggioli2022 LISEM 실제 5cm+LAI→canopy storage는 원문 §Model Selection 확인; 동일 테스트 kinematic wave 명시, 특성별 Ksat와 roughness/cohesion도 함께 달라져 canopy-only causal result 불명. vjetten main_C에는 interception, leafdrip rain KE, 2D runoff+sediment native code 있으나 논문 정확 빌드 미확인, 기존 7.5.2 네이티브 5m 12시도 dt/soil stock NO-GO 유지.
- Long&He2010 원초록은 modified Gash+Green–Ampt+true2D shallow-water+erosion/deposition+microtopography 동시 프레임워크이고 원본 cm 실행판/소스 못 찾음; 2017 same-author GPU-CA는 별개. Wei2017 forest TREX 실제90m, 2D diffusive-wave with qx,qy and splash/flow sediment; 과거 generic TREX 공개 소스가 modified2017 exact source라는 증거 없음.
- Feng2026 한 레퍼런스의 ELM+TELEMAC+GAIA 3-engine 통합으로 재포함. 8.2GB author modified source Zenodo 메타 확인, 실제 최소30m, GAIA Exner 산하 river/floodplain만; original hillslope erosion 지형변화는 계산하지 않는다고 논문에 명시.
- [신규 RDycore native vs docs](models/RDycore.md): 2D Hairsine–Rose 전체 이론식은 문서에 있으나 native tracer C/PETSc/CEED는 단순 shear erosion-deposition과 advection, canopy/rain splash/loose-bed Exner 구현은 확인 안 됨. 우선 모델 아님.
- 본 감사에서는 모형 원본 코드 컴파일/5~10cm 실행을 수행하지 않았으며 모든 필수 조건을 통과했다고 인정된 공개 원본 없음. OpenLISEM 별도 Work QA 통과 전 채택 금지.

# 2026-10-27 단일 레퍼런스 기준 정정 — 다중엔진 통합도 허용
- [상세 재분류 결정](decisions/2026-10-27_SINGLE_REFERENCE_MULTI_ENGINE_FULL_RECLASSIFICATION.md): 하나의 발표 논문에서 tRIBS+OFM+Hairsine–Rose 또는 ELM+TELEMAC+GAIA처럼 3엔진을 실제로 결합한 통합 모델은 단일 레퍼런스 조건을 충족한다. 엔진 개수만으로 제외한 이전 판단을 철회한다.
- 연구/논문상 물리과정 우선 후보: (1) Kim et al.(2013) tRIBS–OFM–HR, (2) Maggioli et al.(2022) classic LISEM 실제 5cm, (3) Long & He(2009/2010) modified Gash 2D rill, (4) Wei et al.(2017) forest TREX. 공개 통합 원본/실제 cm 격자 동시 실행여부는 별도 게이트.
- 실제 연결 코드 또는 저자배포 실행본 자료가 강한 Feng2026, Jiang2025, Iber+2024도 후보로 재분류하되 각각 hillslope bed feedback/해상도, 20km 원본 및 라우팅, canopy 미연결 문제를 분리한다.
- **중요 정정**: Kim2013 0.005m² 삼각요소(정사각 변7.07cm)는 hydrology OFF인 사실상 1D 두 시험의 크기이며, 실제 2D 유역 canopy+hillslope erosion을 7cm에서 시험한 것이 아니다. Feng2026은 GAIA 하천/범람원 bed feedback은 있으나 ELM hillslope soil erosion의 지형고도 변화는 포함하지 않는다.

# Gounsa Literature Master

## 2026-10-27 최종 독립검증: Feng et al.(2026) 원본 수정 TELEMAC/GAIA Zenodo 8.2GB 발견, 실제 수치격자30m·3중 결합으로 고운사 조건 탈락
- [신규 Feng et al.(2026) 논문 기록](papers/2026_Feng_Tan_Xu_Li_Bisht_ELM_TELEMAC_GAIA_Harvey_Sediment.md) DOI10.1029/2025WR042040, [최종 소스 일치 판정](decisions/2026-10-27_LAST_CHANCE_2026_FENG_ELM_TELEMAC_GAIA_30M_SOURCE_VS_SINGLE_NATIVE_GATE.md). 2026-05 WRR: ELM land rainfall/runoff/hillslope erosion + TELEMAC 2D hydrodynamics + GAIA multiclass deposition/Exner one-to-one shared mesh. Author GAIA custom ELM erosion source code and simulation outputs openly archived [Zenodo v2 DOI10.5281/zenodo.18331808](https://zenodo.org/records/18331808): **8.2GB source+results ZIP, md5 efdf94753cd7f29cd8476bf71abb9ff6**, file listing explicitly src/ revised TELEMAC/GAIA code. **압축내부 미열람, 네이티브 실행 미실시**. Real computational mesh **min30m** (tributary90m, periphery1000m), ELM forcing hourly; actual 3 distinct models coupled, not native 5cm single-engine. User strict criteria **FAIL**.
- 기존 [Braga et al.(2026)](papers/2026_Braga_SERGHEI_SE_Finite_Volume_Evaluation.md) DOI10.3390/w18151870은 실제 침식성 댐붕괴 시험에서 **5mm**, 강우사면/V형 유역은 **1m** 격자. 식생 interception/leafdrop future work, existing INDEX 문헌이므로 신규로 중복 생성하지 않음. 5mm 수치사례를 5mm 강우 수관침식 사례라 속이지 말 것.
- 결과: 발표된 논문, 공개된 변경코드, 5~10cm 실제 수관ON 유수침식 수치안정성 조건을 **동시에** 충족했다고 확인된 기성 단일원본 여전히 없음. Classic OpenLISEM 7.5.2 수치 오류 복구는 사용자 명시대로 별도 Work 담당, 실제 시험통과 전 승인 금지.

## 2026-10-27 DHSVM Doten 2006 소스 실물 발견: 수관저류→잎적하 강우충격→지표/하천 유사수송 동일 C 실행원본, 나지·패치 코드 결함 확인
- **핵심 기존 오류 정정**: [Doten et al. (2006)](papers/2006_Doten_DHSVM_Mountain_Forest_Sediment.md) DOI10.1029/2004WR003829 침식소스는 `pnnl/DHSVM-PNNL`에서는 미확보였으나 별도 [**jhamman/DHSVM 공개 유서깊은 C 소스**](https://github.com/jhamman/DHSVM)의 `makefile` 실제 `InterceptionStorage.o`, `MassEnergyBalance.o`, `RouteSurface.o`, `InitSedTables.o`, `RouteChannelSediment.o`, `CalcBagnold.o`가 **동일 DHSVM 실행판에 링크**됨. [파일별 실제 소스 SHA 및 함수추적](models/DHSVM_Doten_2006_Original_Open_C_Sediment_Canopy_Execution_Path_2026.md), [엄격 GO/NO-GO 결정](decisions/2026-10-27_DHSVM_DOTEN_LEAFDRIP_SEDIMENT_ORIGINAL_C_RECOVERED_BUT_BARE_PATCH_FAIL.md), [세션 인계](sessions/2026-10-27_2302_DHSVM_DOTEN_C_SOURCE_RECOVERY_AND_HARD_FAILURES_HANDOFF.md). 기존 '침식원본 못찾았다'는 판정은 **과거 검색범위 부족**으로 수정한다.
- **실제 양의 기능 경로 확인**: `InitNewMonth.c:114–116`에서 `Smax=LAI×Fract×LAI_WATER_MULTIPLIER` 원본 계산. `MassEnergyBalance.c:270–274`에서 `InterceptionStorage` 실제 호출, 수관저장/강우분할 및 `MomentSq` 적하-직달 빗방울 충격 계산, `RouteSurface.c:259–331`에서 `DR=KIndex×Fw×MomentSq` 및 흐름 침식/수송능/하천 유출, `RouteChannelSediment.c` 입경별 퇴적/이송. **진짜 단일 C 프로젝트 산림침식 모델 공개코드 발견**.
- **하지만 사용자가 요구한 나지·억새·참나무 패치에서 심각한 원본 조건문 4개 확인**: (1) `RouteSurface.c:293–295` 식생없음→`DR=0`, 나지 raindrop 박리 사라짐, (2) `RouteSurface.c:261–273` 모든 강우박리는 이미 `sedoutflow>0, h>1mm, stream power>0.004`일 때만 계산, (3) `RouteSurface.c:284–292` rain detach가 `VType->` = **first vegetation class**를 사용하고 `VegMap[y][x].Veg`는 사용하지 않아 패치별 나지/억새/참나무 값 오적용; (4) `MassEnergyBalance.c:215–220` 강우강도 `I>10`를 첫 분기로 먼저 검사해 `10≤I<100` 다음 분기가 정확히 10만 포착. **원본 조건문 오류의 코드증거**, 실제 전체 모의의 숫자오차 계산 아님.
- **중대한 기존 한계 불변**: `SedimentFlag`는 퇴적/침식 켜지면 **kinematic flow** 강제, 하류 `TopoMap.Dir[n]/TotalDir`에 물/유사를 나눠 전달, free XY SWE가 아님. Doten 2006 Rainy Creek 표면침식 **실제 30m 49,085 cells와 수문 3h**, mass-wasting용 별도 고해상도 DEM을 5cm 유수침식 격자로 착각하지 않는다. 원논문은 soil available for detachment 무한 가정. 이 역사적 공개 root는 원논문 Apr2006보다 늦은 Oct2006 `makefile` 주석, **해당 논문 정확 SHA/빌드/입출력 유사수지 미재현**. 따라서 **고운사 5–10cm 기존 단일모델 주엔진은 여전히 부적합**.
- 이번 세션에서는 새 논문을 중복으로 추가하지 않고 기존 canonical 보강, 모델감사1, 결정1 기록. 상세 source path는 위 별도 audit에 보존한다.

## 2026-10-27 최종 원본 일치성 엄격 확인: SRH-W 2009 발표 침식 vs 2007 공식 배포판 유출 전용, 네이티브 5cm ALL-PASS 없음
- [**최종 하드게이트 감사**](decisions/2026-10-27_FINAL_STRICT_ORIGINAL_SINGLE_MODEL_SOURCE_GATE_SRH_W_AND_RECENT.md): 기존 500여 문헌과 각 코드감사를 재대조한 결과, **출판된 같은 원본 소스 + 5–10cm 실제 격자 + 동적 LAI canopy-throughfall/drip + 자유 X/Y water/sediment + rain and flow detach + local deposition numerical closure** 전부 통과 **0건**. 이것은 모든 현존 모델의 부재를 증명하는 게 아니라 현재 근거로 **채택 승인할 수 있는 프로그램 없음**을 뜻한다.
- **신규 [Lai (2009) SRH-W 혼합격자 강우유출/침식 논문](papers/2009_Lai_SRH_W_HybridMesh_2D_Watershed_Erosion.md)** DOI10.1061/(ASCE)1084-0699(2009)14:1(15): 발표된 2D finite-volume source/erosion research. 그러나 미국 Bureau of Reclamation [공식 SRH-W v1.1 2006/2007 매뉴얼](https://www.usbr.gov/tsc/techreferences/computer%20software/models/srh2d/downloads/SRH-W%20v1.1%20User%20Manual%20June2007.pdf) §1.3은 공개 그 버전은 **flow/runoff only, erosion/sediment not yet released** 명시. 2009 논문 뒤 해당 기능이 만들어졌을 가능성까지 부정하지 않되, **2007 문서버전과 2009 연구판 동일 실행판이라고 거짓 주장 금지**. LAI dynamic canopy도 저 버전에서 static depth이고 5cm 실제 sediment 사례 미확인. 현재 별도 SRH-2D 3.3.1 river binary도 SRH-W 원본이 아님.
- 신규 GitHub [Daishubinghydraulic shallow-water+Hairsine–Rose](https://github.com/Daishubinghydraulic/Shallow-water-equations-with-Hairsine-Rose-soil-erosion-equations) README에는 VBA Excel hillslope **roll-wave**와 Water Resources Research **제출**만 기재. 발표 DOI, actual XY 2D source/canopy 불확정이므로 peer-reviewed 기존 실행판으로 취급 금지.
- 사용자 요구에 가장 근접하게 기능상/실행판상 확인된 Wflow의 LAI+leafdrip+rain/flow erosion은 **LDD 유사이송 때문에** 탈락, 실제 FullXY HR 2015는 **논문 수정 소스 누락 및 canopy 부재**, HydroSed2D는 **rain/splash absent**, SHETRAN은 **cm peer-reviewed native stability 부재**, Classic LISEM은 **과거 2D 침식수치 실패로 다른 Work가 검증 중**. 아무 후보도 '원래 모델 그대로 된다'고 주장하지 않음.

## 2026-10-27 23:02 원본 C++ 실제 호출망 추적: SEIMS 강우/유수박리 및 수송능 mm→m 누락 의심
- **[새 심층 실제 코드 감사](models/SEIMS_2026_Storm_Source_Callgraph_Canopy_And_Sediment_Unit_Audit.md)**, [GO/NO-GO](decisions/2026-10-27_SEIMS_STORM_SOURCE_BUILDTARGET_LAI_AND_TRANSPORT_Q_UNITS_NOGO.md), [세션 인계](sessions/2026-10-27_2302_SEIMS_SOURCE_BUILD_CANOPY_UNITS_AUDIT_HANDOFF.md). 별도 Work가 담당하는 OpenLISEM을 제외한 공개 원본 `lreis2415/SEIMS` **dev** CMake, `api.cpp`, `Execute()`, C++ hydrology/splash/sediment source를 actual source blob+line 검토.
- **원본 연결 확인:** `SPLASHERO_PARK`와 `KinWavSed_OL` 둘 다 실제 CMake shared library targets. `SPLASHERO_PARK/api.cpp`의 `VAR_NEPR` (interception net precipitation mm) → `VAR_DETSPLASH` (kg) 및 `KinWavSed_OL/api.cpp`의 `D_DETSplash` (kg) 입력 연결, `KinWavSed_OL.cpp::GetSedimentInFlow` `m_Sed_kg += (Df+Dsp)` 및 수송능 이상 퇴적 `m_SedDep=Dep*Vol` 실제 존재. 반면 `D_LeafDrain` 메타데이터는 주석, 식생효과는 **USLE-C와 순강우**이고 `PI_SVSC`의 canopy 저장은 계절 `INTERC_MIN/MAX`이지 직접 LAI 입력/수관적하 KE 아님. 유사수송은 `FLOWIN_INDEX` 방향망이지 자유 XY SWE가 아님.
- **구체적 소스 단위 불일치 발견:** `KinWavSed_OL.cpp::CalcuVelocityOverlandFlow`와 `WaterVolumeCalc`이 수심 `m_WH`를 **mm**라 하고 `/1000` 적용. 그러나 `GetTransportCapacity` L299 `q=m_V*m_WH*60` (주석 q m²/min)은 변환 없이 곱함. 수치상 1000배 q 차이가 있고 q=0.046 고·저 함수분기를 변경할 수 있음. **[C++17 독립 격리 계산](code_audits/SEIMS_TransportCapacity_UnitProbe.cpp)** 실제 컴파일로 예시 v0.1m/s h5mm에서 q30 vs0.03 및 TC1.765045 vs0.339683 확인 ([결과](code_audits/SEIMS_TransportCapacity_UnitProbe_Output.txt)). **SEIMS 전체 원본을 컴파일/실행한 것은 아님**. 전 수문-유사 결과 오류가 항상 1000배라고 주장 금지.
- `PI_MCS` `STORM_MODE` 내부에는 `m_P`(header에 없고 `m_pcp`만 선언)와 `data`(SetValue 인자는 `value`) 잘못된 식별자 사용이 있어 그 옵션 빌드 시 컴파일 장애로 의심됨. `PI_SVSC` 별도 옵션까지 전부 실패한다고 확대 금지.
- **판정:** SEIMS 공개원본은 실제 강우/유수박리와 퇴적 루틴을 갖지만, 사용자 필수 동적 LAI 수관저류→잎 적하운동에너지, 자유 XY 2D 동역학 유사수송, published 5–10cm 계산격자 결합실증을 못 충족. **주모델 불합격 유지**. 현재 `INDEX.md` papers506, models109, decisions106. 추가 신문헌 없이 기존 원본의 새로운 컴파일/단위 근거만 아카이브.

## 2026-10-27 엄격한 실제 실행코드/학술판 대조: HydroSed2D Fortran과 Le et al.(2015) FullSWOF-HR
- **[두 모델의 동작 코드/학술 구현 비교 결정](decisions/2026-10-27_FULLSWOF_HR_LE2015_VS_HYDROSED2D_NATIVE_2D_SOURCE_GATE.md)**: 기존 [HydroSed2D 원본 코드 감사](models/HydroSed2D_Fortran_Original_Source_Audit.md) **최신 후속 보강**, 동일 기존 모델 문서 중복생성 없음. `psu-efd/HydroSed2D/src/swefvm.f90` main `init→swe→if(sedimentctl&&scalc)sediment→output`; `sediment.f90` Shields→MPM/Grass **유속 기반 2D 소류사 플럭스**, Exner `dz=-dt_s/(1-porosity)divqb/area`. 전 Fortran 컴파일 경로에서 **LAI/canopy water/rain impact detachment 강우 공급 함수 없음**. `calc_shear`의 Q1^(4/3) dry divide potential은 **실제 실행으로 미검증**, 수치결함 확정 표현 금지. gfortran 설치는 확인됐으나 컨테이너 GitHub 다운로드 DNS 차단, 컴파일·강우시험 성공 기록 없음.
- **신규 [Le, Cordier, Lucas & Cerdan(2015)](papers/2015_Le_Cordier_Lucas_Cerdan_FullSWOF_HairsineRose_2D_Sediment_Splitting.md)** DOI10.1002/2014WR015690 Wiley WRR 51:987–1005 원문 전체 방법/결과 직접 판독. [연구용 full2D HR 소스와 공개 FullSWOF baseline 계보 감사](models/FullSWOF_2D_2015_Le_HairsineRose_CodeLineage_And_Numerical_Gates.md): 진정 xy shallow-water + 다입경 HR rain splash/flow entrainment/재박리/퇴적/지표형상, 비음수 수심·토사농도를 **SW CFL 조건만으로 보장하는 Strang 수치 분할**과 문헌 기준 ≥100배 계산시간 절약 (다른 엔진 적용 성능아님). 실험 V자 사면 **10m×4m, 종/횡 1%, 70mm/h×2h**. 결정적 원문 §4.3에서는 **유수전단 power 임계 미달이라 2D 시험 flow entrainment 거의 없고 강우박리만 토사원**, 'flow 박리 현장 검증 완료'로 과장 금지. 계산 셀 dx/dy, LAI 수관저류/낙수 KE 및 2015 수정된 전체 HR C++ 원본 미확인. 확인된 [BUCEA/FullSWOF_Rif](https://github.com/BUCEA/FullSWOF_Rif) Makefile은 **순수 2D 수리 라이브러리만** 링크, 침식 HR 모듈 없음. 논문과 baseline 동일 코드로 주장 금지.
- **판정:** true XY + Exner bedload source available인 HydroSed2D, true XY + HR 다입경 강우침식 연구논문인 Le2015 모두 5~10cm dynamic LAI canopy 및 해당 발표 전체 자유 2D 원본 유사계산 **all-PASS 실패**. 새 coupling을 이미 발표된 원본 실행판으로 부르지 않음. Classic openLISEM 수정/실험은 별도 Work 담당.


## 2026-10-27 23:55 신규 Aksoy 2020, WASH123D 1998, PIHM 2007 원본 실체 검증
- **[원본별 엄격 결정문](decisions/2026-10-27_2355_NEW_AKSOY_WASH123D_PIHM_STRICT_PUBLISHED_SOURCE_SCREEN.md)** [인계서](sessions/2026-10-27_2355_NONLISEM_AKSOY_WASH123D_PIHM_SOURCE_HANDOFF.md): 사용자 지시에 따라 OpenLISEM 디버깅 제외하고 비LISEM 독립 원본/실제 계산격자/기능 동시 활성/코드 공개여부 조사.
- **[Aksoy et al. (2020)](papers/2020_Aksoy_Gedikli_Yilmaz_2D_Rill_Interrill_Lab_Validation.md)** DOI10.1016/j.jhydrol.2019.124391: 6.50×1.36m 사전 세류와 세류간 나지 모래실험에 45–105mm/h 강우, 종/횡 경사5–20%. 모델은 2D erosion/sediment continuity로 소개되지만 **원문 공개 Introduction은 기반 유출해법이 '2D control volume에서 유도됐지만 종방향 유동만 고려'한다고 명시**, 완전 자유 X/Y 2D 동역학 해석기라는 근거 부족. 원본 native5cm 계산격자, 수관 LAI/drip 미확인; matching 공개 solver 확보 못함. 종방향 세류 및 세류간 박리실험 보조문헌, 고운사 주모델 제외.
- **[Yeh et al. (1998) WASH12D/123D](papers/1998_Yeh_Cheng_WASH123D_2D_Overland_Sediment_TechReport.md)** USACE CHL-98-19: 2D overland + sediment/transport and kinematic/diffusive/dynamic wave 선택판 논문/보고서 존재. [모델 원본 감사](models/WASH123D_1998_2D_Flow_Sediment_Source_Availability_Audit.md)에서 CSDMS는 'As code' 표기도 하지만 **실제 source URL이 없고 페이지 category 'Source code not available'**임 확인. 맞는 Fortran GitHub 원본 없음, LAI 수관저류/적하와 5cm native 적용 발표 증거 없음. **실물 공개원본 요건 탈락**.
- **[Qu & Duffy (2007) PIHM](papers/2007_Qu_Duffy_PIHM_Canopy_ODE_FVM_Watershed.md)** DOI10.1029/2006WR005752: original vegetation canopy 저장량 ODE 및 triangular hydrologic element 연구. 현재 [MM-PIHM 원본감사](models/PIHM_MM_PIHM_2007_LAI_Canopy_Source_And_PIHMSed_Lineage_Audit.md)에서 GitHub `PSUmodeling/MM-PIHM/src/is_sm_et.c` **L86 `intcp_max=lc.cmcfactr*lai*lc.shdfac` 수관저류**, `read_lai.c` 시간별 LAI 읽기 및 canopy evaporation 확인. 그러나 현재 공개빌드 `pihm/flux-pihm/flux-pihm-bgc`만 지원하며 transport 파일은 4개 **용질** 모듈. *PIHMSed* 프로젝트 문헌의 수목전도, 풍화, 토양 이동과 **실제로 동일 배포된 5cm 강우세류 유사량 해석기인 근거 없음**. 수관 원본 자체는 확실하나 유수침식 단일모델 불가.
- 전체 **published original 5–10cm + LAI canopy active + 자유 XY SWE + raindrop/overland erosion/deposition + matching openly released source** 신모델 PASS는 **0건**. 이번의 새 근거는 [INDEX](INDEX.md) 기준 **논문504건, 모델107건, 결정104건**. 이미 검토한 모델을 단순 새이름으로 재등재 금지.

## 2026-10-27 새 독립 논문 2편: Jia 2023 진정 2D 빗방울-유수침식/지형변화와 Adiprana 2026 산지 식생-LiDAR 침식 (모두 완전 원본 고운사 FAIL)
- **[엄격 비교 결정](decisions/2026-10-27_JIA_CCHE2D_2023_AND_ADIPRANA_SIMWE_2026_SOURCE_VEGETATION_HIGHRES_SCREEN.md)** 및 [CCHE2D 연구용 코드 배포 계보감사](models/CCHE2D_2023_Jia_Raindrop_Morphodynamics_Source_Release_Audit.md). **[Jia et al. (2023)](papers/2023_Jia_Wells_Momm_Zhang_Bennett_CCHE2D_Raindrop_Rill_Gully_Morphology.md)** DOI10.1016/j.jhydrol.2023.129419: Journal of Hydrology 620:129419; NCCHE CCHE2D 수정판으로 2D 동수역학 h,u,v, raindrop soil detachment, sheet/rill/gully erosion+sediment transport, 직접 **UAV SfM 관측 지형변화/유사량/배수망** 대조. 실험 강우30→105mm/h after360min; grain0.05mm. Publisher 'high-resolution mesh'지만 **실제 격자 크기未확인**. NCCHE는 legacy free 32bit GUI와 64bit 제한 trial 실행판만 제공, **완전기능 상용 연구원본** https://www.ncche.olemiss.edu/downloads/ 명시; 2023 수정 patch/full source/runfiles 및 LAI canopy interception/drop KE 미확보. 5cm published native 원본 채택 금지.
- **[Adiprana & Samodra (2026)](papers/2026_Adiprana_Samodra_SIMWE_Lidar_Vegetated_Landslide_Erosion.md)** DOI10.1002/esp.70329: ESPL 51(7) e70329, Java Kalisari **실제 산사태급경사 식생지/나지**, UAV-LiDAR DEM + SIMWE 2D stochastic runoff+erosion/deposition maps, 84mm/h 30분 vs38.2mm/h 65분, field infiltration vegetation72/bare30mm/h and **reverse infiltration** to isolate effect; observed video water depths vegetation ~1cm/bare~4cm under 84mm/h. **식생효과는 침투능/거칠기, LAI 수관저류·통과·낙수 KE가 아님**. Publisher original paper admits steady-state approximation and absolute sediment erosion rates uncertainty, source GRASS GIS public but case input/GRASS scripts only author request and actual 5cm computing mesh unproven. [기존 SIMWE 모델 기록](models/GRASS_SIMWE_RSimTerrain.md) 후속 보강.
- **결론:** 실제 2D rain+flow morphodynamics 및 실제 식생지 산지침식 선행연구 강화, **한 공개 원본 동일 빌드 5~10cm + 동적 LAI 수관 + direct/drip KE + 자유 2D 유사이송+퇴적 수치안정성** 조건 완전 충족 모델 미확보. OpenLISEM fork 수치수정은 다른 Work 담당으로 유지.


## 2026-10-27 신규 공식 공개 WaTEM/SEDEM 원본: 연평균 순침식·퇴적, 6시간 초고해상도 수관차단 엔진은 불가능
- [두 신모델 실물소스 비교 판정](decisions/2026-10-27_SMODERP2D_AND_WATEM_SEDEM_PUBLIC_SOURCE_COMPLEMENTARY_GAPS.md), [KU Leuven WaTEM 공식 Pascal 소스](https://github.com/watem-sedem/watem-sedem), [Van Rompaey et al.(2001)](papers/2001_VanRompaey_Verstraeten_VanOost_WaTEM_SEDEM_AnnualSediment.md) DOI10.1002/esp.275, [코드 모델감사](models/WaTEM_SEDEM_2024_Pascal_Native_Annual_RUSLE_Sediment_Audit.md). RUSLE 연평균 E=R·K·LS·C·P, 격자별 수송능력 TC, **하류 1~2 격자**로 유사배분 및 순침식/퇴적량 계산 실제 구현. [2024 Zenodo release](https://doi.org/10.5281/zenodo.10997288) 실행판과 소스 공식 공개.
- **단일 6시간 강우사상 동적 수관수지, 자유 X/Y SWE, 초단위 강우/유수 토사박리의 동일 실행판은 아님**. 식생 C 보호계수는 LAI 캐노피 저류/수관낙수 KE가 아니며 5~10cm 발표 강우사상도 확인되지 않음. **고운사 주모델 탈락**.
- SMODERP2D의 공개 프로그램은 반대로 강우사상 중 단순 잎면적 기반 interception과 sheet/rill 유출을 계산하나 진짜 sediment 질량 박리/퇴적 active routine 미확인. 설명서의 'erosion model' 표현을 성능 검증으로 취급하지 않음.


## 2026-10-27 23:45 비LISEM 독립 Wang2023 2D 강우침식 연구 및 Iber+ 2024 실제 논문판 5cm 착시 검증
- **[엄격 원본 및 실제 격자 판정](decisions/2026-10-27_2345_WANG_2023_SLOPE_EROSION_AND_IBER_EXACT_BENCHMARK_CODE_GATE.md)**, [세션 인계](sessions/2026-10-27_2345_NEW_WANG_2D_EROSION_AND_IBER_EXACT_BINARY_CASE_HANDOFF.md): OpenLISEM은 사용자 요청대로 다른 Work 담당, 비LISEM 선행연구만 조사.
- [**Wang et al.(2023) CATENA 232 107387**](papers/2023_Wang_Hou_Catena_TwoDimensional_Loess_Slope_Erosion.md), DOI10.1016/j.catena.2023.107387: 황토사면 강우실험에서 유사수송능식을 정량 보정한 독립 2D runoff/erosion 모델, 사면 중하부의 침식기여도 지도 생성. 2022 저자선행 EGU DOI10.5194/egusphere-egu22-1885 reported 유출 NSE0.83, 유사농도 NSE0.66, **2023 최종판 독립검증이라 주장 금지**. 논문 본문 제한으로 정확 2D SWE PDE, 5cm 셀, canopy LAI/throughfall/leaf drip code와 공개 matching executable 미확인. 공동연구자의 공개 HiPIMS-CUDA 수문코드를 이 논문 침식프로그램과 동일시 금지. **주모델 보류**.
- [**Cooper et al.(2012) 기존 canonical 강화**](papers/2012_Cooper_Wainwright_MAHLERAN_MiC_30cm_Interception_Drip.md), DOI10.1029/2012JF002499: 원문 실제 **식생 있을 때 수관차단 손실, 수관통과, 적하에 따라 rain KE 조절** 선언. 그러나 공개 검증실험은 **나지 13.75×6.5m, 60mm/h 20min, 네이티브 0.30m 계산격자**, cardinal max-steepest descent **kinematic wave** (full XY SWE 아님). 사상말 `137Cs` 추적퇴적 공간분포 NSE0.98 및 수문곡선 NSE0.93, 580L vs534L 증거. **0.05m 두께 모래는 원토층 두께, 5cm 계산격자 아님**. 수관식 존재를 수관 활성 5cm 실험이라고 재분류 금지.
- [**Iber+ 기존 모델 canonical 원본패키지 정확성 보강**](models/Iber.md): 저자 공개 [v3.2b 바이너리 DOI10.57745/UFEK4L](https://doi.org/10.57745/UFEK4L)와 같은 논문 [실험 T1 DOI10.57745/2WH9AL](https://doi.org/10.57745/2WH9AL), [Pradel T2 DOI10.57745/J2A44Q](https://doi.org/10.57745/J2A44Q), [Galabre T3 DOI10.57745/NOHRHJ](https://doi.org/10.57745/NOHRHJ), [Ullion T4 DOI10.57745/VFBGFR](https://doi.org/10.57745/VFBGFR) 각각 확인. **T1 5cm 길이×2m 폭 한줄 격자=quasi1D**, T2 120m²/3300셀 √평균면적 약0.19m (unstructured min unknown), Galabre 20km². 원논문에 대응하는 **실행 프로그램과 자료는 공개**지만 **C++/CUDA 전체 소스는 collaborator-only**, native LAI dynamic canopy/drip 검증 없음. 따라서 **재현 가능한 실물 바이너리 원본 침식 벤치마크라는 장점**을 새로 확보했지만 Gounsa 단일 공개코드 5cm 식생 free2D 원본으로 승인하지 않음.
- 기록: 신규 paper1, decision1, 기존 paper Cooper 및 model Iber 문헌 갱신. `INDEX.md` **papers497 / models103 / decisions101**. 기존 거절 반전 없이 새 독립 문헌을 기록함.

## 2026-10-27 독립 신규 공개 원본: SMODERP2D 실질 구현범위 검증 (강우사상 세류 모의는 PASS, 토사량 자체는 미구현)
- **[원본 소스 기능 판정](decisions/2026-10-27_SMODERP2D_ACTUAL_SOURCE_RILL_RUNOFF_NOT_SEDIMENT_NATIVE_NO_GO.md)**, [소스 blob 및 함수 감사](models/SMODERP2D_2019_2026_Native_Interception_Rill_Without_Sediment_Source_Audit.md). Czech Technical University 공개 [SMODERP2D GitHub](https://github.com/storm-fsv-cvut/smoderp2d) GPL. 연구 **[Landa et al.(2019)](papers/2019_Landa_Jerabek_Pesek_Kavka_SMODERP2D_OpenSource_Parallel.md)** DOI10.5194/isprs-archives-XLII-4-W14-143-2019, **[Kavka et al.(2022)](papers/2022_Kavka_Jerabek_Landa_SMODERP2D_SheetRill_ThreeScaleValidation.md)** DOI10.3390/w14030327.
- `processes/rainfall.py::current_rain` 실제 `interc=ppl*rainfall` + 최대 차단 `pi` [mm]로 순강우 산정. 식생 잎면적 계열 비율은 있으나 Rutter/Gash canopy storage drain, LAI dynamic C(t), 낙수충격 KE **없음**.
- `core/kinematic_diffuse.py`는 `Mfda if Globals.mfda else D8` 형태, 2D raster에서 유동 방향 분산/변경하지만 **full 2D SWE 운동량·자유 유사 플럭스 아님**. `time_step.py` 전체 629행은 sheet/rill runoff/infiltration/rill width 계산, sediment detachment/concentration/transport/deposition **활성함수 검색 없음**. 2019 논문 제시된 Eqs 1–6은 water/manning rill 뿐임.
- 2022 논문 actual spatial mesh **5m×5m** field 36.6ha; 2×8m rainfall60mm/h plot과 약50m² monitored hydrograph, 5m field grid 세류 분포 비교. **세류 발생 위치 관측을 유사박리·퇴적 질량 검증으로 착각하지 말 것**. [**Neumann(2022) 박사학위논문**](papers/2022_Neumann_SMODERP_Sediment_Transport_PhD_Experimental_Evaluation.md)은 450회 이상 4~34°/40~160mm/h 실험으로 Kilinc–Richardson류 토사이송 추가식 연구; 이 연구가 2026 현재 공개 프로그램의 작동하는 유사루틴이라고 주장할 수 없음.
- **고운사 현재 결론:** native event runoff/rill open source **YES**, dynamic LAI canopy KE and highres freely XY rain+flow erosion/dep **NO**. 원본 한정 고운사 단일 유수침식 주모델 탈락, 참고 수문세류 모델 보존. OpenLISEM 코딩/수치검증은 사용자 지정 Work가 별도 담당.

## 2026-10-27 23:30 국내 산림 수관차단 침식 실측과 Wflow 2026 EUROSEM 원본 단위오류 공식 수정
- **[검증 결정문](decisions/2026-10-27_2330_KOREA_CANOPY_FIELD_AND_WFLOW_EUROSEM_SOURCE_REGRESSION_SCREEN.md)** [세션 인계](sessions/2026-10-27_2330_KOREA_FOREST_CANOPY_WFLOW_NATIVE_FIX_HANDOFF.md): 비LISEM 독립문헌 조사. 전체 PASS 5–10cm canopy+freeXY+direct/flow erosion+deposition 동종 원본은 계속 미발견; 그러나 고운사 실측 검증에 직접 기여할 기존 연구와 수정된 실제 공개 소스 찾음.
- **[Kim et al.(2009) 한국 안성 산림](papers/2009_Kim_Yang_Kim_Onda_Korean_Forest_Canopy_Interrill_Erosion.md)** DOI10.3178/hrl.3.36: 자연강우, 수관아래/나지 0.45×0.40m **실제 6개 침식 관측구**, 경사 10/20/30°, 수관아래 interrill soil loss 더 낮고 3h 강우강도 및 수관통과우 구간 변동과 관련. 원 표토 실트점토4%, 모래76%, 자갈20%, 편마암. **수치격자 5cm 모델이 아니라 관측논문**.
- **[Thompson et al.(2016) 참나무/유칼립투스 산림](papers/2016_Thompson_Davis_Oliphant_Oak_Eucalyptus_Litter_Soil_Erosion_Field.md)** DOI10.1002/esp.3881, 대학서버 9쪽 원 PDF p2/p6 **스크린샷 직접 확인**. 8 paired oak/eucalyptus plots, oak 5cm vs eucalyptus 10cm 평균 낙엽두께 (모형 격자 크기 아님), 2008년 1월 큰 비 이후 참나무 조사구 유사량 더 큼 (ANOVA p0.019), 이전 해에는 eucalyptus 유출량 더 큰 경향. **수관과 유사 관계는 낙엽층/발수성/침투와 결합됨**, LAI 차단 ON/OFF만으로 순 침식량 예측 금지. 공개 [iGISc/iGIScData tidy_eucoak.rda](https://github.com/iGISc/iGIScData/blob/master/data/tidy_eucoak.rda) 180×12 실제 강우/수관아래 강우/유출자료를 DOI 논문과 비교할 수 있으나 유사량 변수 없음. 관측용 참고자료, 원본 자유2D/5cm 해석기 아님.
- **[Wflow 기존 원본 감사 갱신](models/Wflow_Sediment.md)**: **공식 upstream [Deltares/Wflow.jl PR #939](https://github.com/Deltares/Wflow.jl/pull/939)** merged **2026-06-15** (commit `b9de064dda8027dfd5567af1b5ccef8c35d0c869`), **v1.0.3 2026-06-23** 반영. EUROSEM의 **total rainfall kinetic energy에 잘못 곱했던 0.001 제거**, 강우박리 수면차폐식에 넣는 육상수위는 **m→mm 단위전환** 필요해 교정. Native test 단일 셀값 0.012323→12.323은 **내부 회귀시험에서 1000배 증가한 예**이고 고운사 예측 아님; 잔여 피복수심 효과는 감소방향이어서 최종 비율은 상황 의존. 수정 전 버전의 강우박리 수치를 무비판적 인용 금지. **그러나 Wflow native sediment routing은 directed network, free X/Y 2D sediment 불충족이라 주모델 기각 유지**.
- 현재 `INDEX.md` 계산상 **papers496 / models103 / decisions100**, 새 실증 논문2 + decision1, Wflow canonical 기존 파일 업데이트. 같은 모델 새 이름으로 재등재하지 않음.

## 2026-10-27 22:00 비LISEM 추가 논문 Raff2005 완전 2D + Wang2025 산지 BRIF LAI 수관차단 원본 감사
- **[신규 논문 및 원본 공개 엄격 판정](decisions/2026-10-27_2200_NONLISEM_FURTHER_RAFF_BRIF_SOURCE_REAL_CELL_SCREEN.md)** / [세션 인계](sessions/2026-10-27_2200_MORE_NONLISEM_RAFF_BRIF_2D_CANOPY_SOURCE_HANDOFF.md). OpenLISEM 수치오류는 사용자 지정 별도 Work가 담당하고 본 조사에서는 비LISEM 신규 선례/실제 계산격자/일치 공개 소스를 검토.
- **[Raff & Ramírez (2005)](papers/2005_Raff_Ramirez_Fully_Coupled_2D_Hillslope_Hydrology_Erosion.md)** DOI10.1002/fld.1016: Wiley 공식 초록에서 소규모 사면의 **full 2D SWE+1D Richards 침투+침식/유사수송** 동일 원본 과학설계 확인. **해당 paper Δx=5/10cm, LAI 수관저류 및 공개 소스는 아직 미확보**. 같이 조사한 [2003 Ramírez & Raff 연구요약](papers/2003_Ramirez_Raff_Evolution_Landscapes_Hillslopes_Project_Synopsis.md)의 '식생/나지 토양 경계'는 수관차단 구현이라는 증거가 아님.
- **[Wang et al. (2025)](papers/2025_Wang_Ouyang_An_BRIF_2D_Mountain_Interception_Flash_Flood.md)** DOI10.1029/2024EA004076: 급경사 쓰촨 산지 BRIF **LAI 기반 수관차단+침투+2D local-inertia 유동**, 22km² Cutou 유역 **실제 Δx=2.5m, 632만 계산셀**, V자 집수역 1m, 다른 유역8m. 0.3m UAV DEM은 관측입력이고 500m LAI는 자료격자, 초고해상도 native가 아님. **침식/국지 퇴적 원본 없음**.
- [**BRIF/HFDM-GPU CUDA 원본 감사**](models/BRIF_HFDM_GPU_2025_LAI_2D_Interception_No_Sediment_Code_Audit.md): 공식 `chinafl/HFDM-GPU` GitHub의 `test/wind_cuda.cu`는 수종/피복별 `V_Smax=f(LAI)`와 `V_K=1-exp(-Cover*LAI)`를 계산, `test/windmath_cuda.cuh`에 `Diff_interception` 선언. **실제 계산 CUDA kernel 정의를 포함하는 `windmath_cuda.cu`가 public tree에 없고 최상위 `hfdm`은 binary**이므로 전체 소스 재현이라고 할 수 없음. 논문 저자도 data availability에서 **일부 핵심코드** 제공으로 표현. 국지 침식/유사수송 source 없음. 사용자 단일 5cm 침식 엔진 기각.
- 기존 [2010 Waldmann PROMET](papers/2010_Waldmann_PROMET_Large_Scale_Erosion.md) 및 [2026 Braga SERGHEI-SE](papers/2026_Braga_SERGHEI_SE_Finite_Volume_Evaluation.md)는 검색에서 재발견했으나 이미 INDEX에 있어 신규파일 추가하지 않음. PROMET 1km/EROSION2D 내부1m, SERGHEI-SE 2026 vegetation 추가는 **미래과제**로 저자가 기술. 현재 새 fully published 5–10cm canopy+full2D+sediment 동일 공개빌드 all-PASS는 여전히 미발견.

## 2026-10-27 신규 SPHY-MMF: 실제 LAI 수관저류+낙수/통과우 KE+강우/유수박리+퇴적 모두 한 오픈소스 모델 연구, 그러나 200m/일별 LDD
- **[엄격 새 비-LISEM 모델 판정](decisions/2026-10-27_SPHY_MMF_LAI_DRIP_KE_EROSION_SOURCE_VERSIONS_AND_200M_DAILY_NO_GO.md)** 및 [**버전별 C/Python 원본 검사**](models/SPHY_MMF_2018_2026_LAI_Canopy_LeafDrip_Sediment_Original_Code_Audit.md): **[Eekhout et al.(2018)](papers/2018_Eekhout_Terink_deVente_SPHY_MMF_LAI_LeafDrain_Erosion.md)** DOI10.5194/esurf-6-687-2018은 **실제 하나의 통합 발표모델**에서 NDVI/LAI→Smax dynamic canopy store→P_eff→DT vs leaf-drain LD의 KE→F splash vs H flow detachment→within-cell/deposition plus sediment transport를 별도 계산. **[2018 exact original Zenodo v2.1.1](https://zenodo.org/records/1344534)** archived 15.1MB source, md5 `3b3368227b9bac0b1ddd68e7b74b0bb7`; 이번 runtime ZIP download 실패로 exact binary test 미실시. 최신 [FutureWater/SPHY](https://github.com/FutureWater/SPHY) 실제 `dynamic_veg.py,sphy.py,mmf.py,sediment_transport.py` SHA 추적 확인.
- **버전 다름**: 2018 발표식 `KE_DT=DT(8.95+8.44log10I)` Marshall–Palmer와 2026 master 현재 활성식 `KE_DT=DT*.29*(1-.72exp(-.05I))*100` Brown–Foster **서로 다름**. 2026 SHA를 2018 재현 실행판으로 소개하지 말 것. `Smax(mm)=.935+.498LAI−.00575LAI²`, `KE_LD=LD(15.8√PH−5.87)` if PH≥.15m, `LD=P_eff CC` native 활성경로 확인. 2026 current default examples SedFLAG=0 are *sample defaults*, published 2018 actual erosion run was ON.
- **결정적 적용장벽**: 2018 실제 **200m 계산격자**, 기초 DEM 30m resampled, model **일별**, 저자 권장200m–1km, `FlowDir`/PCRaster directed/LDD routing, **not free XY 2D SWE**. 6시간 10–50mm/h + cm 단일사면 정량모델로 **NO-GO**, but high-value canopy KE benchmark literature/source.
- **[Eekhout et al.(2021)](papers/2021_Eekhout_MillaresValenzuela_SPHY_Erosion_FiveModel_Ensemble.md)** DOI10.1002/ldr.3920 publishes DHSVM/HSPF/INCA/MMF/SHETRAN 5 **alternative** soil erosion equations inside SPHY, not 5 dynamically coupled independent 2D simulators. Actual daily Spain catchment and none is 5cm SWE.
- 독립 과학조사만, OpenLISEM 수정 및 컴파일은 Work 담당 유지. **Native 전필수 조건 PASS 단일모델 미확보**.

## 2026-10-27 22:05 비LISEM 신규 원본: AHMS-SED 2025과 Juez 2018 정밀 원문 감사
- **[비LISEM 엄격 결정](decisions/2026-10-27_2200_NONLISEM_AHMS_SED_SOURCE_ACTIVE_CANOPY_KINETIC_NO_GO.md)**, [인계](sessions/2026-10-27_2200_AHMS_SED_FORTRAN_CANOPY_DRIP_AND_2D_SED_HANDOFF.md): 사용자가 OpenLISEM 검증을 Work에 맡겨 본 흐름은 독립적으로 다른 원본만 조사.
- **[Jiang, Parteli & Shao (2025) AHMS-SED](papers/2025_Jiang_Parteli_Shao_AHMS_SED_Yellow_River_Open_Source.md)**, DOI10.1029/2024MS004593: 논문 정식 모델 **공개 Fortran** https://github.com/JiangCong1990/AHMS-SED, 원본 보존 https://doi.org/10.5281/zenodo.14494932, 논문 입력과 결과 https://doi.org/10.5281/zenodo.14983610. [코드 경로 감사](models/AHMS_SED_2025_NOAHMP_CASC2D_NATIVE_CANOPY_SEDIMENT_AUDIT.md): 실제 `NoahMP/Noah/module_sf_noahmplsm.f`의 `CANWATER`는 `MAXLIQ=CH2OP*(ELAI+ESAI)` 후 `QDRIPR/QTHROR`를 계산하고 `EROSION`에 전달; `OPT_ERO=4`에서 직접우와 수관적하의 KE가 박리에 적용됨. **하지만 저장소 예제 `erosion_option=1`(USLE)이고 논문 실제 그 옵션 선택은 별도 확증 안 됨**. `Routing/module_rt_sed2d.F`는 `Routing/Makefile` 빌드 대상에서 제외된 **비활성 초안**이다. 실제 main `module_rt_rt2d.F`는 8방향 implicit head-routing, LAI→USLE C factor 및 부유/퇴적 토사경로 계산, **full 2D SWE 운동량 풀이는 아님**. published 실제 **20km, 1h 계산**, 5cm 고운사 주모델 탈락.
- **[Juez et al. (2018)](papers/2018_Juez_Tena_FernandezPato_2D_SWE_HEM_Algars_Erosion.md)**, DOI10.18172/cig.3320: 26쪽 전체 publisher PDF 및 screenshot과 §4.1/4.3 원본 확인. 실제 **full 2D SWE dynamic wave + SCS + 2D HEM storm erosion**, 158000 삼각형 요소, **최소 면적 150m², 최대 600m²** (5~10cm 셀 아님). 원문 §4.3은 **퇴적에 따른 지형변화 미구현**을 명시; LAI 수관저류/적하 및 공개 일치 원본 확인 안 됨. calibrated hydro-sedigraph는 published paper evidence, 고운사 필수조건 FAIL.
- **총평:** 신규 공개 코드에서 canopy storage→QDRIPR/throughfall→drop KE→splash detachment의 **실제 활성 선택 경로**를 발견한 것은 의미 있음. 그러나 이 모델을 `5cm native published full 2D SWE validated canopy erosion source`라고 바꿔 부를 수 없음. 다른 Work의 OpenLISEM 논의와 섞지 않는다.

## 2026-10-27 Wei et al.(2017) 동일 산림모델 수관차단 + 2D rain/flow 침식 실증 발견, 정확 격자 90m와 코드 부재
- **[2017 후쿠시마 산림 TREX 모델 원논문 검증 결정](decisions/2026-10-27_WEI_2017_FOREST_TREX_CANOPY_SPLASH_2D_INTEGRATED_90M_NO_CODE.md)**. [**Wei et al.(2017) JHER**](papers/2017_Wei_Kinouchi_Velleux_Fukushima_TREX_Forest_Interception_2D_Erosion.md) DOI10.1016/j.jher.2017.09.003 본문 §4.1: **2014 Wei & Kinouchi가 개량한 산림 수문 TREX** 기반 interception/ET, subsurface/groundwater, full XY **2D diffusive wave**, **별도 splash rain source e_s + flow net erosion/deposition e_h**, 입경별 sand/silt/clay conservative equation 및 국지 순침식/퇴적 맵을 동일 **published model 연구 안에서 적용**. 발표 자체는 진실하므로 구형 CASC2D-SED 소스에 LAI가 없다는 이유로 개량 2017 논문 기능까지 부정 금지.
- **정확 실제 계산 격자**: 137km² Fukushima Kuchibuto forested basin, **90m DEM/landuse 90m**, 강우1km, 2011–2014 강우사상/관측 및 SSC/유사 질량비교. canopy storage water Rutter/Gash eq, leafdrop KE, 5cm actual cell 계산 없음. **2D 확산파이지 full dynamic SWE 모멘텀 아님**.
- [**같은 해 Cs 동반 연구**](papers/2017_Wei_Kinouchi_Yoshimura_Velleux_Forested_Cesium_TREX.md) DOI10.1016/j.jenvrad.2017.01.017: forest **137Cs canopy wash-off**는 수관 강우차단 C(t)과 구분. 기존 2008 CSU TREX 원본 복제소스 `Interception-r4.c` 고정저류형으로 **2017 연구용 exact modified original source/binary/runfiles 미확보**. DOI 논문만 가지고 5cm 실행 주모델로 추천 불가.
- 최신 현재 결론: **실제 다른 학자들이 canopy/interception+2D diffusion water+separate rain/flow sediment/deposition을 published single modified TREX에서 모의한 2017 선례 확인**. 그러나 user's full pass = native open full-source, <=10cm 2D, leafdrop and canopy, all-edge boundary, sediment time/mesh convergence **여전히 미확보**.

## 2026-10-27 비-OpenLISEM 독립 CASC2D-SED 원본 C 공개저장소 발굴 및 2000/2008/2014/2025 기능대조
- [**신규 CASC2D-SED 원본 확보와 엄격 판정**](decisions/2026-10-27_NEW_CASC2D_SED_SOURCE_ARCHIVE_DEEP_2D_CANOPY_GATE.md), [소스 전체 핵심 함수감사](models/CASC2D_SED_C_Original_Independent_Code_Audit_2026.md): CSU 2003 model 자료 복제 GitHub [wy7980/CASC2D-SED](https://github.com/wy7980/CASC2D-SED), `casc2d_sed.c`, `OvrlRout.c`, `RoutSedOvrl.c`, `Fcts_sed.c`, `Settling.c`, `intercept.c` 등 계산 C 및 Makefile 실물 확인. Clone README에서 `rint→wrint` 심볼 수정 명시, CSU 원래 byte-identical release라고 주장 금지, **native build 아직 미실시**.
- **[Johnson et al.(2000)](papers/2000_Johnson_Julien_Molnar_Watson_CASC2D_SED.md)** DOI10.1111/j.1752-1688.2000.tb04246.x: genuine bidirectional XY **diffusive-wave** overland, Green-Ampt, sand/silt/clay sediment, 현장유량/유사 검증. 경계는 `RoutOutlet.c` **단일 `jout,kout`**, 4개 면 자유출구 안 됨.
- **결정적 canopy 결함:** `ReadControlFile.c` landuse별 `retention[i]`[mm], `InitializeVars.c`에서 초기값, `intercept.c` 22행에 강우를 그 저장량만큼 순차 차감 후 0. **LAI/C(t)/drainage/leafdrip KE 없음**. `Fcts_sed.c` KR capacity~q^2.035 slope^1.66 and USLE C/K/P, `RoutSedOvrl.c`은 nonzero flow에서만 source; **직접 rainfall splash separate detachment 없음**.
- **[Rojas et al.(2008)](papers/2008_Rojas_Velleux_Julien_Johnson_CASC2D_SED_GridScale.md)** DOI10.1061/(ASCE)1084-0699(2008)13:9(793): 실제 모델 계산격자 **30–330m**, 5–10cm 실행 실증 없음.
- 기존 [Wei & Kinouchi(2014) 산림 LAI 개량본](papers/2014_Wei_Kinouchi_CASC2D_Forested_Interception.md)은 이 확보한 옛 C 침식엔진과 동일 원본 실행판이 아님. 논문 두 기능을 임의 합성해 기성 단일모델이라 주장하지 않는다.
- **[Jiang et al.(2025)](papers/2025_Jiang_Parteli_Shao_AHMS_SED_20km_Original_Code.md)** DOI10.1029/2024MS004593: CASC2D-SED의 후속 현대 AHMS-SED [Zenodo 코드](https://zenodo.org/records/14494932)/[GitHub](https://github.com/JiangCong1990/AHMS-SED) 실제 공개 확인. 다만 **20km 황하 지역모델**로 routing 재구성됨. 5cm 전방향 2D LAI 수관 + 강우/유수박리 선례 아님.
- **고운사 전체 PASS 원본 여전히 미확보.** Work 수행중인 Classic OpenLISEM 수정과 이번 독립 연구조사는 별개. CASC2D-SED = 역사적 소스 확보 성공, 고운사 주엔진 **탈락**.

## 2026-10-27 별도 담당 문헌조사: OpenLISEM 제외 2D 수관차단과 침식 모형 재검증
- **WASA-SED LAI 실제 계산식 재확인:** `src/Hillslope/soilwat.f90` L945, L976, L996에서 `maxintc = lai_act(...) * intcfc(i_ce)` 활성 연산으로 **수관저류 [mm] = LAI × 단위 LAI당 저류계수**가 구현됨. 개발 주석에 0.25mm/LAI 기준을 언급하나 현장보정값이 아님. 저장량 및 증발 포함. **LAI 기반 수관차단 원본 PASS, 자유 2D SWE 및 5–10cm 세류침식 원본 FAIL.**
- **[독립 문헌조사 판정](decisions/2026-10-27_NON_LISEM_2D_CANOPY_EROSION_LITERATURE_FOLLOWUP.md)** 및 [세션 인계](sessions/2026-10-27_2100_NONLISEM_2D_CANOPY_EROSION_RESEARCH_HANDOFF.md): OpenLISEM 원본 수정/검증은 사용자가 Work에 위임했으므로 **그와 별개로 다른 연구만 조사**. 신규 논문 원문과 실제 코드가 입증하는 범위만 남김.
- **[Abrantes et al. (2021)](papers/2021_Abrantes_Simoes_2D_Experimental_Two_Direction_Erosion.md)** DOI10.2478/johh-2021-0003: 실제 2×2m 두 방향 사면 X1%/Y10%의 runoff+sediment 실측비교, 2D flow, Horton-SCS infiltration, rill/interrill detachment/deposition. X방향 미소유출 과소추정, Y방향/총량 성능 양호. **실제 Δx=5cm 여부 및 LAI canopy/same-public-code 확인 불가**. 출판사 PDF 확보 제약 때문에 세부 수식·격자 폭 원문 미열람 명시.
- **[Hinsberger & Yörük (2025)](papers/2025_Hinsberger_Yoruk_HydroAS_2D_Rill_Erosion_025m.md)** DOI10.1007/s40710-025-00797-9: HydroAS Full SWE 2D + Govers erosion + Exner DEM feedback, field rill calibration. 실제 해상도 0.25m/1m(원 DEM cm와 구분), **infiltration과 rain splash 제외**, LAI canopy 미구현 실증. 공식 [유료 소프트웨어](models/HydroAS_Govers_2D_Sediment_NonOpen_Canopy_Audit.md) 별도 license와 등록 제한 download, 공개 editable solver source 없음. **탈락**.
- **[Mueller et al. (2010) WASA-SED](papers/2010_Mueller_Guntner_WASA_SED_Dryland_Sediment.md)** DOI10.5194/gmd-3-275-2010: [원본 Fortran 직접 감사](models/WASA_SED_2026_Public_Fortran_Canopy_Erosion_Source_Audit.md). `TillF/WASA-SED/src/Hillslope/soilwat.f90`에 LAI/interception 실제 존재; `sedi_yield.f90`은 USLE/Onstad-Foster/MUSLE/MUST 선택 + LU/TC/SVC 구획별 한방향 유출. **완전 공개 소스지만 자유 X/Y 2D SWE와 5cm 그리드유사 플럭스 부재**, 주모델 탈락.
- **[Downer et al. (2014 online/2015 print)](papers/2014_Downer_Pradhan_Ogden_Byrd_GSSHA_Sediment_Transport_Limits.md)** DOI10.1061/(ASCE)HE.1943-5584.0001104: GSSHA/CASC2D-SED 교정강우보다 큰 사상에서 유사량 과대 예측이 일어나는 원본 formulation 문제와 detachment limit 처리 연구. 5cm 같은 실행판 근거 아님. **[Raza et al. (2021)](papers/2021_Raza_Ahrends_Field_Erosion_51_Model_Review.md)** DOI10.3390/land10040422: 51개 모델에 대한 canopy / field patch / free-2D 부족 리뷰, 실행가능 코드 자체는 아님.
- **전체 판정:** 현 단계에서도 **5~10cm 실제 계산 + LAI native canopy interception/drip + 자유 2D 유동 + direct rain/overland detachment + local sediment deposition + 전체 공개 동일 원본** all-PASS 신규모델은 확인하지 못함. 하지만 2D 실제 실험 근거(Abrantes), 25cm geomorphic feedback(HydroAS), canopy 공개 Fortran(WASA)은 각각 **직접 사용한 선행연구**로 검증됨. 본 문헌조사를 OpenLISEM Work 진행과 혼동하거나 이미 기각된 코드를 복구했다고 주장 금지.

## 2026-10-27 Work와 독립적으로 확인한 신규 2D 침식, 물방울 수관차단, 수관 낙수 운동에너지 연구 4편
- **[4편 개별논문 검증 결정문](decisions/2026-10-27_INDEPENDENT_NEW_2D_EROSION_AND_CANOPY_PHYSICS_PAPERS.md)**: OpenLISEM 수정/재실행은 Work 담당이며 이 조사에서는 시행하지 않음. `INDEX.md` 검토 후 기존 Long & He 2009/2010 2D SWE+Gash 논문은 중복 발견으로 제외.
- **[Abrantes et al.(2021)](papers/2021_Abrantes_Simoes_2D_TwoDirectional_Slope_Erosion.md)** DOI10.2478/johh-2021-0003: 2×2m x1% y10% 양방향 경사 토양수로 실험으로 **genuine 2D unsteady flow + Horton-SCS 침투 + rill/interrill erosion + deposition**를 논문/현장 검증. x 유사량 과소추정, y 비교적 우수. 그러나 LAI 수관차단과 공개 원본 동일실행판 미확인, 계산 격자 크기 미확인.
- **[Li & Tian(2025)](papers/2025_Li_Tian_Microphysical_Canopy_Interception_Python.md)** DOI10.1029/2024WR038296: LAI, 피복도, 잎 투영, 물방울 잔류율, 부착률로 **층별 충돌-저류-수관통과** 계산, 강우20/80mm/h 실험. [Zenodo v2](https://doi.org/10.5281/zenodo.15045577)에서 Python `model_runrun_basic.py`/`model_runrun_simplified.py` 및 검증자료 공개 파일목록을 실제 확인. **수관 단독모델로서 오픈 소스 유효, 2D runoff/erosion 없음**. Python 파일 원문 네이티브 재실행은 미실시.
- **[Senn et al.(2025)](papers/2025_Senn_Schaefer_Hosseini_Seitz_VSF_ULS_Energy.md)** DOI10.1002/esp.70150: UAV LiDAR voxel 0.5m×0.25m canopy gap profile로 VSF를 산출하고 온대림 splash cup TKE 관측 검증. 통계적으로 유의한 관계이나 **운동에너지를 체계적으로 과소예측**. 토사이송 모델 아님, 5cm 실행사례 아님.
- **[Katayama et al.(2023)](papers/2023_Katayama_Nanko_Jeong_Canopy_Drip_Kinetic_Hotspots.md)** DOI10.5194/esurf-11-1275-2023: 일본 너도밤나무 **단일 집중 낙수점** TKE 일반수관 아래보다15.2배, freefall보다49.7배, throughfall 양도 일반보다11.4배. 수관 저장량 감소가 곧 국지 박리 감소가 아니라는 실측 근거. 이를 전체 참나무 격자의 일괄침식배율로 전용 금지.
- **결론:** new published research/Zenodo source 발견은 사실이지만, 5–10cm + freely spreading 2D 유출 및 유사+ LAI 수관 물수지 + erosion/deposition + identical runnable public engine을 전부 충족하는 **새 단일모델은 확보하지 못함**. 세부 물리의 새 coupling은 기성 발표 모델이라고 부르지 않는다.

## 2026-10-27 2025 SWEHR HydroShare 연구자료의 새로운 출처 단서, 원본 공개코드 문제는 미해결
- **[2025 HydroShare 실증자료 vs SWEHR1.0 원본 비교 결정문](decisions/2026-10-27_SWEHR_2025_HYDROSHARE_CODE_PROVENANCE_FOLLOWUP.md)**: Luke McGuire / Aiza Kabeer가 2025-12-10 북부 Arizona Pipeline Fire runoff/debris-flow modeling 자료를 [HydroShare 프로필](https://hydroshare.cuahsi.org/user/8128/)에 게시한 사실 새로 확인. 설명에 CSDMS SWEHR generic version 명시. **자료 UUID/파일 목록/코드 내부 미열람**이므로 새로운 Rutter canopy 구현이라는 추론 금지.
- McGuire et al.(2016)은 Rutter interception + SWEHR/HR 2D + 토사원/퇴적 published architecture지만 실증 **2.5cm TLS→37.5cm 계산**, 실제 산불후 두 사상 canopy OFF. 5–10cm canopy ON 실증 아님. 2017 [공개 SWEHR.c](https://github.com/csdms-contrib/swehr/blob/master/SWEHR.c) 1785행 Git blob `e8505221a37d245ebb387b3304d8f325addd9ada`, canopy/Rutter/LAI 관련 코드 0개로 이전 탈락 판정 재확인. 신규 모델 채택 없음.
- Epple(2025) LISEM 1cm 농경지 실험에 canopy ON 검증/정확 원본 SHA 공개 근거 없음; 공개 신형 LISEM 0.2.3/0.2.5 GUI water canopy/rain splash 문제 및 별도 0.2.4 실행판 미검증 판정 그대로. 핵심 다음 업무: 새 HydroShare의 실제 자료/코드 동정 또는 사용 실행판 일치 확인, 이미 기각 모델 반복 추천 금지.


## 2026-10-27 21:00 새로운 2D SWE + Gash 수관차단 + 침식/퇴적 + 세류 지형변화 선행연구 발견
- **[신규 모델 엄격 판정](decisions/2026-10-27_2100_NEW_LONG_HE_2009_2010_2D_GASH_EROSION_SOURCE_VERDICT.md)** 및 [후속 작업 인계](sessions/2026-10-27_2100_NEW_GASH_2D_EROSION_LONG_HE_HANDOFF.md): **Long & He (2009, 2010)** 논문 2편에서 기존 모델 목록에 없던 **2D SWE Godunov FVM + modified Gash 수관차단 + Green–Ampt 침투 + 침식/퇴적 + 지형변화/세류 발달**의 **같은 논문 모델** 물리과정 발표 확인. Maggioli2022 5cm 실증 (운동파)보다 모형기능상 사용자 요구에 가까움.
- [**2009 JICS FVM 논문**](papers/2009_Long_He_Rill_Evolution_FVM_Modified_Gash.md) (6(6):2349–2356), [**2010 Journal of System Simulation 논문**](papers/2010_Long_He_2D_Gash_Rill_Erosion_Morphodynamics.md) (22(2):348–352), [**2009 GPU 논문**](papers/2009_Long_He_GPU_2D_SWE_Hydraulic_Erosion.md) (IEEE DOI10.1109/ICIECS.2009.5363863) 및 [**원본 공개경로 감사**](models/Long_He_2D_Gash_Morphodynamics_Code_Audit.md) 별도 보존.
- **핵심 제한:** 두 paper abstract에서 실제 **5–10cm computational mesh 불명**, **LAI 활성 저장용량/leaf-drip KE 세부 불명**, exact source code / input / executable GitHub 검색 **미발견**. 2009 GPU 논문은 그 자체에 Gash canopy를 명시하지 않으므로 동일 실행판이라고 연결 금지. 초록 단계 연구를 공개 실행 가능한 고운사 주엔진으로 선정 불가.
- 2024 Perrini *WRR* DOI10.1029/2023WR036421의 LAI interception + genuine 2D SWE는 DREAM+Iber 두 모형 연계며 5cm 유수침식 단일실행판이 아님(기존 `papers/2024_Perrini_RunoffOnGrid_DREAM_Iber.md` 확인). 타 탈락 Iber+, TREX, SHETRAN5cm 무선례, LISEM7.5.2 수치문제 결론 유지.
- **진실한 전체 PASS 실행모델은 여전히 확인 안 됨.** 새로운 것은 **학술선례가 존재한다는 부분적 반증**이며, 실행 가능한 전체코드 확보 및 5cm 실증이라고 기록하면 안 됨.

## 2026-10-27 7.5.2 원본 소스 및 과거 native 수치검증 교차감사: 기존 NO-GO 유지
- **[원본 재감사 결정문](decisions/2026-10-27_OPENLISEM_752_SOURCE_NATIVE_REAUDIT_NO_GO.md)**: Classic openLISEM `v7.5.2` 태그와 `main_C` (태그보다 +8 commits)를 직접 비교. 원본 `GetSV`·`SedimentSSContinuous`·수관차단·낙수 함수는 동일 blob; 2D SWE 함수만 차이. 브랜치 최신이라는 이유로 수치 오류 해결 주장은 금지.
- 기존 Windows Actions [원본 native 12회](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40304135775) job success 확인. 5m 2D 1ha, 20mm 강우 조건에서 참나무 SV1 유사배출 외부 Δt=5/10/20초 각각 0.005993 / 123.037727 / 832.588686 kg/ha, 각격자 침식 유한토층 초과 → 원본 고운사 정량엔진 불합격. 전역질량수지 폐합은 수렴 증거 아님.
- 1/2초 [추가 실행](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40304815539) 및 2m [추가 실행](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40303685346)은 **정상 수치 결과가 아니라 TIMEOUT**. 성공으로 기록 금지.
- 원본 `GetSV(100µm)` 큰 분기 불연속, `DetachMaterial`/detachment 농도상한 비활성화, 최소 CFL timestep 하한, 2D 유사이송 OpenMP 공유 버퍼 += 데이터 경쟁 **가능성(미입증)** 등을 확인. 근본인과는 전부 독립적으로 입증한 게 아님.
- 따라서 이전 채택 권고 철회. Maggioli(2022) 5cm는 **운동파 LISEM**, freely spreading 2D SWEs와 다름. 전 필수조건 만족 검증된 원본은 미확보; 새 맞춤 coupling/SHETRAN cm 확대를 기존 5cm 선행실증인 양 권고 금지.

## 2026-10-27 20:53 Maggioli 2022 원논문-실제 당시 OpenLISEM GitHub SHA 교차검증
- **[엄격 결정문](decisions/2026-10-27_MAGGIOLI_2022_EXACT_CODE_INPUT_PROVENANCE_AND_VALIDATION_AUDIT.md)**, [원 논문 canonical 보강](papers/2022_Maggioli_RodriguezCaballero_LISEM_5cm_TLS_LAI_Interception_Erosion.md), [세션 인계](sessions/2026-10-27_2053_MAGGIOLI_2022_EXACT_CODE_AUDIT_HANDOFF.md): 원문에서 LISEM **실제 5cm 계산과 1초 시간해상도, 식생피복→LAI→수관저류, 강우/침식** 재확인. 단 실제 지표수 이동은 원문에 **kinematic wave routine**으로 명시, 완전 XY 동역학 2D는 사용하지 않음. 1초는 모의 맵 시간해상도로 기술돼 있으며 solver 내부 fixed dt 1초라고 단정 금지.
- **2001–2022 공개 소스 계보:** 논문 발표일과 같은 **2022-02-11** `vjetten/openlisem` historical commit `3b0264ef557c031fe39fb6d523c3669bf6e1296a` 실제 버전 **6.837 beta**, 당시 `lisInterception.cpp` canopy LAI/drainage, `lisErosion.cpp` direct/leafdrip splash, `lisSWOF2DSediment.cpp` free XY 유사수송, `lisOverlandflow.cpp` kin vs FullSWOF 둘 다 구현됨. **Maggioli에 실제 사용된 SHA/버전이라는 증거 없음, 논문에서는 kin 선택**, 2026 v7.5.2 동일시 금지.
- **검증 범위 정정:** 18개 이벤트 기간 총 TLS 침식으로 PSI를 보정 후 동일 기간 총량 모델3.55t vs 실측2.81t 비교한 연구. 보고 RMSE=17.79%는 완전 독립적인 holdout 검증/5cm 격자별 DoD 정확도가 아님. 식생 시나리오도 LAI 수관차단만 바꾼 실험이 아니라 Ksat/토양강도/피복 조건을 같이 변경, canopy isolated effect 미입증. Data Availability에 데이터 제공 약속만 있으며 정확한 binary/runfile/raster input 아카이브 위치 미확인.
- **수치문제 근거도 확인:** 2022 `lisErosion.cpp::GetSV` 이미 100μm에서 `d/1000` 단위 처리의 비정상 분기 후보(논문 D50=5μm라 결과오류 추정 금지). 과거 7.5.2 1/2초 재실행 [40304815539](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40304815539)은 **20분 타임아웃으로 검증 미완료**, 2m 보조 실행 [40303685346](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40303685346)은 **30분 타임아웃 및 NO_VALID_SIMULATIONS**. 이미 완료한 7.5.2 5/10/20초 수치 비수렴 NO-GO를 지우지 못함.
- **결정:** 타인의 published 5cm canopy+erosion **선례로 인용 가능**, 사용자의 genuine 2D+국지 퇴적+matching original reproducible code를 통과한 고운사 주모델로 **채택 불가**. LISEM 기능 존재와 5cm에서 논문이 검증한 solver를 혼동 금지. SHETRAN 5cm 확대 철회 결정 유지.

## 2026-10-27 정책 정정: 선행 실증모델 우선, SHETRAN 5cm 임의 확장안 철회
- **[수정 결정](decisions/2026-10-27_WITHDRAW_UNPRECEDENTED_SHETRAN_SUB10CM_PREFER_PUBLISHED_LISEM_LINEAGE.md)**: 선행된 SHETRAN 4m 가상사면 35회 실행은 유지하되 5~10cm 새로운 확대를 우선 추진하자는 계획은 철회. 사용자는 타 연구자가 실제 5~10cm에서 수행한 단일 수관/침식 모델을 우선 원함.
- **문헌상 5~10cm**: Maggioli et al.(2022) classic LISEM 5cm LAI canopy storage+rain/erosion kinematic routing, Cuomo(2018) LISEM 10cm vegetated splash/runoff. 진정 자유로운 2D SWE 입증 및 exact reproducible code unresolved; 7.5.2 native 2D timestep sediment nonconvergence NO-GO 그대로 유지. Epple2025 1cm new LISEM canopy same-run 미검증.
- **다음 단계**: 실제 논문의 LISEM exact executable/source, full configs/data provenance 먼저 확인. 원저 연구의 운동파/2D 차원 엄격 분리하고 과거 native QA 실패와 다른 버전임이 입증되기 전까지 SHETRAN 또는 LISEM을 5cm 주모델로 승인하지 않음. 전 조건 동시 만족 공개 원본은 아직 미발견.

## 2026-10-27 실행 결정: 5~10cm SHETRAN 네이티브 검증으로 전환
- **[진행 순서와 중단기준](decisions/2026-10-27_SUB10CM_SHETRAN_CONCRETE_GO_NOGO_EXECUTION_DECISION.md)** [인계서](sessions/2026-10-27_1940_SUB10CM_NATIVE_GO_NOGO_ACTION_HANDOFF.md): 신규모델 반복 검색을 중단하고 이미 수관+2D 유사수송 전체 연결 검증된 SHETRAN 4.7.2부터 **동일 20×20m 물리영역 1/0.5/0.2/0.1/0.05m** 단계별 native 실행으로 판정. 소영역 5cm=160000 active, 10cm=40000 active여서 원본 NELEE250000 아래; 0.648ha 전체 10cm=648000, 5cm=2592000은 capacity 확장 필수. 기존 실험 생성기는 NX17 NY29 DX4m, 고정 row length 및 boundary 80개이므로 **숫자만 DX=0.1로 수정 불가**. 같은 연속 경사/패치와 4방향 실제 BC/물-유사 mass/시간·공간수렴/가용토심 확인한 뒤 전체영역 10cm로 확대한다.
- **중요:** 현 단계는 실행 설계이며 **5cm/10cm 네이티브 계산을 수행했다는 근거가 아직 없음**. SHETRAN 5cm published precedent 없음, 4m 35개 native 결과를 cm 실증으로 과장 금지. 불합격 시 현재 공개 단일모형의 필수해상도 적용 불가를 인정하고, 기각된 LISEM7.5.2 등을 근거 없이 대체채택하지 않음.

## 2026-10-27 19:40 GitHub 우선: 산림 수관차단과 2D 유사수송 새 코드 대조
- [**엄격 원본 기능 판정문**](decisions/2026-10-27_1940_GITHUB_FIRST_2D_CANOPY_SEDIMENT_SOURCE_SCREEN.md) 및 [세션 인계서](sessions/2026-10-27_1940_GITHUB_FIRST_2D_CANOPY_SEDIMENT_HANDOFF.md): 기존 INDEX/MASTER를 확인한 뒤 새로운 이름 두 종의 공개 코드 및 급경사 산림 2D 연구를 조사. **전 조건 만족 5–10cm 공개 원본 아직 미발견**.
- **[HydroSed2D 실제 Fortran 소스감사](models/HydroSed2D_Fortran_Original_Source_Audit.md)**: Penn State `psu-efd/HydroSed2D/src/sediment.f90` SHA `7e6be598...`에서 진정한 X/Y 2D SWE + MPM/Grass 기반 bedload + Exner dynamic topography 실제 구현 확인. 그러나 **강우, LAI 수관차단, 침투, 빗방울 박리 부재**. **탈락**.
- **[WaNuLCAS (v3.01 문헌 + v5.0 배포 계보 구분)](models/WaNuLCAS_Interception_Erosion_Strict_2D_Screen.md)**: LAI × 물막두께로 최대 canopy 저장고, Rose soil loss 실제 존재. 다만 수평 구획(zone)과 일별 처리이지 **genuine 2D SWE 라우팅 아님**. [Onsamrarn et al. (2020)](papers/2020_Onsamrarn_WaNuLCAS_WEPP_Thailand_Erosion.md) 태국 산지 관측 유사량 비교도 동일 한계. **탈락**.
- **[Ámon et al. (2024)](papers/2024_Amon_HECRAS_Forest_Canopy_Litter_2D_FlashFlood.md)** DOI 10.3390/w16050750: 헝가리 급경사 산림의 수관차단과 낙엽저류 반영 HEC-RAS FVM SWE 2D 강우사상 실제 수문 검증, 계산격자 4–20m. canopy는 별도 유효강우/유사토양층 처리이고 **침식/퇴적은 논문에서 계산하지 않음**. **보조근거**에 그침.
- 새 후보 SedHydro는 외부 수문 결합을 전제로 하는 framework, EROSION-3D GitHub 공개 R wrapper는 executable solver source가 아님. 이미 탈락 판정 TREX, SMODERP2D, GSSHA, classic/new LISEM, SHETRAN cm-gap 등을 다시 신규모델로 추천 금지.

## 2026-10-27 GitHub 우선 대조한 10cm 수관차단 및 침식 독립 연구
- [**이번 엄격 모델 판정 및 소스감사**](decisions/2026-10-27_GITHUB_FIRST_SUB10CM_NATIVE_MODEL_FOLLOWUP.md), [인계서](sessions/2026-10-27_1800_GITHUB_FIRST_NATIVE_SUB10CM_HANDOFF.md): MASTER/INDEX/SHETRAN/LISEM 분기 및 기각 SHA를 먼저 확인한 뒤 신규 논문/원본을 검색함.
- **Cuomo (2018)** [새 논문](papers/2018_Cuomo_LISEM_10cm_LAI_Vegetated_Erosion.md), DOI 10.19199/2018.3.0557-1405.31: **실제 LISEM 0.1m 격자**에서 나지 및 35% 초본 피복과 LAI=6 기반 수관저류, runoff/sediment concentration 실험 비교. 약 0.02s 시간간격. 이는 Maggioli(2022) 5cm 외 독립 선행사례지만 동일 자유 XY 2D SWE, 원본 버전 SHA, 격자별 국지 퇴적 DoD, 공개 원본 유사수지/수렴을 입증하지 않아 단일모델 채택 불가.
- **LUCIA SustainSahel** [최초 공개 원본코드 감사](models/LUCIA_SustainSahel_Code_Audit_2026.md): `src/erodep/erodepModule.py` 실제 free/canopy throughfall splash detachment + 모래/실트/점토별 유사퇴적이 있음. 하지만 `self.LDD` 및 `accufractionflux(self.LDD,...)`로 유출 및 유사이송; genuine 2D SWE가 아니고 공식 재현 격자 6,30,100m라 엄격 탈락.
- CCHE2D(Jia2023)은 2D raindrop erosion+UAS high-resolution이 있지만 canopy native 미확인, NCCHE 현재 정식 모델은 상용 배포; Feng2026은 ELMv3+TELEMAC-GAIA 이중모델 약30m로 대상 외. 기존 엄격 5–10cm 전체 PASS 공개 모델 **여전히 미확인**. 이전 OpenLISEM Classic7.5.2 sediment nonconvergence, 신형 LISEM 0.2.3/0.2.5 source bugs, SHETRAN 4m native 성적은 그대로 유지.

## 2026-10-27 17:20 원본 소스 재검증 및 모델스크린 정정
- [**채팅 길이 제한에 대응한 이번 추가 소스검증 인계**](sessions/2026-10-27_1720_SUB10CM_CANOPY_EROSION_FOLLOWUP_HANDOFF.md): 엄격한 5–10cm LAI canopy+genuine 2D+강우·유수박리와 유사수송/퇴적+동일 공개실행본 PASS는 **여전히 미확인**. 4m SHETRAN 연구용 주모델 판정과 구분함.
- **TREX 후보성 철회**: [기존 2008 TREX 코드감사](papers/2008_Velleux_England_Julien_TREX_2D.md)에 독립 archived C source `WatershedModels/trex_src_csu/src/Interception-r4.c`가 있으며 고정 차단저류량 차감은 구현, native LAI 동적 저류/배수·leaf drip impact 미입증. 신규 모델로 다시 추천하지 않음.
- **Wei & Kinouchi (2014)** [논문별 신규기록](papers/2014_Wei_Kinouchi_CASC2D_Forested_Interception.md), DOI 10.2208/jscejhe.70.I_157: Fukushima 산림 CASC2D 수관/지하수/수문 개량과 hydrograph 검증은 실제 있으나 5–10cm canopy+sediment executable source 미확인. 별도 2014년 modified version을 archived TREX origin과 혼동 금지.
- **SMODERP2D** 본체 `core/vegetation.py` + `processes/rainfall.py` canopy 코드 확인. 그러나 유사퇴적 native mass solver 불확실하고 **공식 권장 격자 2–20m**로 5–10cm 후보에서 배제(https://storm-fsv-cvut.github.io/smoderp2d-manual/requirements.html). **SERGHEI-SE** full SWE+erosion 장점 인정하지만 subcm 실증은 dam-break, canopy-on-rainfall 검증이 아님. **GEOtop-SED** 공개 리포지터리 연구판 전체 퇴적모듈 동일성 미입증, kinematic 경로 제약 유지.

## 2026-10-27 5–10cm 식생 수관차단+2D 지표유출/유사 단일 공개모델 재탐색
- [**선행연구 계산격자/식생물수지/완전원본 공개 여부 엄격 판정**](decisions/2026-10-27_5CM_10CM_CANOPY_2D_EROSION_NATIVE_MODEL_SCREEN.md): 5cm LISEM Maggioli2022 canopy/침식 진실이나 kinematic routing; PSEM_2D 5cm true SWE/침식이지만 canopy 없음. **조건 전부 동시 PASS 원본 모델 확인되지 않음**.
- **Kivva & Zheleznyak (2005)** [새 논문](papers/2005_Kivva_Zheleznyak_2D_Runoff_Interception_Sediment.md), DOI 10.1615/InterJFluidMechRes.v32.i6.50: canopy interception + true 2D SWE + 침식재퇴적까지 논문 초록에 통합모델 명시. 단 mesh size 및 원본코드/LAI 세부 공개 안 됨.
- **Cooper et al. (2012)** [새 논문](papers/2012_Cooper_Wainwright_MAHLERAN_MiC_30cm_Interception_Drip.md), DOI 10.1029/2012JF002499: interception loss, throughfall & leaf drip KE 물리 개념, marker-in-cell 퇴적; 13.75×6.5m 시험 **30cm 격자**, **나지** 실험, flow는 steepest-descent 1-way 기저; 저자 연락 필요 source, strict 기각.
- **Kim et al. (2013) tRIBS-FEaST** 0.005m² (~7cm 상당) 10×1m 삼각메시 유사수송 시험은 **수관/강우 수문모듈 비활성**. 본문 Rutter 및 full 2D HR 일체는 실제 존재하지만 현행 공개 tRIBS v6에서 FEaST sediment source 없음.
- **Braga et al.(2026) SERGHEI-SE** 5mm 퇴적/bed migration lab 검증이나 rain+canopy 테스트가 아니며 **저자 미래과제로 vegetation coverage 제시**; 엄격 기각.
- **GSSHA** 원모형 canopy interception+2D runoff+erosion deposition native 아키텍처 공식자료 확인, 그러나 발표 10cm 이하 원본 침식 canopy 사상 실증 미확인.
- 이전 탈락한 SWEHR/Eurosem/OpenLISEM 7.5.2는 기존 source QA verdict 유지. cm LiDAR 관측 해상도와 계산 격자 따로 평가.

## 2026-10-27 신형 LISEM 모든 GitHub 브랜치 SHA 대조 완료
- [**3개 브랜치 전수 및 커널 원본 비교 보고**](decisions/2026-10-27_LISEM_ALL_PUBLIC_BRANCHES_CODE_AUDIT.md): `main` 0.2.3 SHA 6a5ef17d87bab4227d48673c95c12c61462114dd (2022-08-10), `develop` 0.2.5 SHA 1e55e6c0bfda28d56a9e1d37e1c21c616820c6a1 (2022-12-12), `website` docs only SHA 09c9f060324c85cb83ff33e02644816169293d54 (2022-09-22); release tag `source` points **main 0.2.3**, despite name Beta0.2.4.
- `model_hydrology.cl`, `model_evapotranspiration.cl`, `model_sediment.cl`, `modelruncompile.cpp` have **exact same Git blob SHA on main and develop**. So canopy Smaxc unused and stored SCANOPYN=0, erosion input rain_m=0.0 in integrated GUI are not fixed on develop.
- `model_flow.cl` is different: develop fixed x/y edge water outflow `qfout` ternary-parenthesis and changed rainfall timestep factor main `rain*dt_hydro/dt` vs develop `rain*dt/dt_hydro`; exact rainfall conservation implications **not native tested**. **`model_sediment.cl` analogous qfsout precedence bug remains.**
- SourceForge standalone **0.2.4 Windows installer**, officially described 0.2.3 rain bug fixed in 0.2.4: **not yet binary/embedded OpenCL kernel tested**; cannot generalize failures to this exe. Epple2025 1cm verified run unspecified exact source SHA.
- **Decision**: public main/develop native integrated canopy+rain splash missing per code, 0.2.4 separate binary and later 2025 paper's actual executable not yet resolved. This corrects earlier categorical statements on entire LISEM software.

## 2026-10-27 신형 LISEM 버전 대응 오류 정정
- 앞서 git main 소스의 canopy 및 rain_m=0 문제를 공식 **0.2.4 바이너리에도 적용**한 듯 서술한 것은 부정확함. 실제 main `version.h`는 **0.2.3**(2022-08), 누락했던 develop은 **0.2.5**(2022-12)이며 두 공개 브랜치에서 canopy/rain_m 문제 계속 관찰됨. **공식 SourceForge 0.2.4 바이너리는 미시험**. 개발자는 2022-07-09 0.2.4 공지에서 0.2.3 강우 입력 오류를 수정했다고 주장. **0.2.4의 소스 해시-실행판 연결은 미확인**. 최신 판정 [정정문](decisions/2026-10-27_NEW_LISEM_PUBLIC_SOURCE_NOT_SUITABLE_CANOPY_SPLASH.md).

## 2026-10-27 신형 LISEM 원본 GitHub 코드를 직접 확인한 NO-GO
- [**소스 진단 및 최종 판정**](decisions/2026-10-27_NEW_LISEM_PUBLIC_SOURCE_NOT_SUITABLE_CANOPY_SPLASH.md), [상세 코드 감사](models/LISEM_Integrated_VanDenBout_Source_Audit.md).
- 공식 신형 LISEM 0.2.4 Windows 배포, Github `bastianvandenbout/LISEM` 공개 소스는 **2022년 main SHA 6a5ef17d…**, `version.h`는 0.2.3 표기. 2025 Epple 논문에서 사용한 2024 LISEM 코드와 동일성 없음.
- 공개본 `model_hydrology.cl`과 `model_evapotranspiration.cl`: `Smaxc`를 읽지만 수관저류/차단에 사용하지 않음, `SCANOPYN=0`. `model_flow.cl`에는 원강우가 지표로 직접 유입됨. **동적 LAI 기반 canopy water balance 미구현/미연결**.
- `model_sediment.cl`에 빗방울 충격/유수박리/퇴적식 자체는 있으나 `modelruncompile.cpp` 및 `modelrun.cpp`의 `m_CLProgram_Erosion->PlaceArgument(81,0.0)` 때문에 **GUI 통합사상경로 빗방울 박리 입력 rain_m가 0으로 전달**됨. 독립 `rasterflow.h::AS_SplashErosion`은 이 문제를 자동 해결하지 않음.
- x/y 2D 지표유동, sediment transport and DEM update present; 하지만 source-level missing native canopy+rain splash이므로 **고운사 단일모델은 공개 2022 신형 LISEM으로는 NO-GO**. 실제 바이너리 컴파일/실행/시간간격 수렴은 수행하지 않았음.
- 이전 5cm Maggioli(2022) classic LISEM 선례 및 1cm Epple(2025) 신형 LISEM 선례 존재는 유지. 단 2025 논문 사용본 소스/바이너리는 별도 필요.


## 2026-10-27 긴급 LISEM 계보 및 cm격자 연구 정정
- **[개발 계열 차이](models/OpenLISEM.md)**: 고전 LISEM original(1990s)→ Victor Jetten `OpenLISEM Classic` v7.5.2; 이와 별개인 Bastian van den Bout **신형 LISEM**(`bastianvandenbout/LISEM`). 공식 https://lisemmodel.com/docs/home/ 는 서로 다른 실행 소프트웨어임을 명시.
- **Epple et al.(2025) 1cm LISEM**은 `LISEM 2024 https://lisemmodel.com/` 인용, Bastian van den Bout 지원 명시, scripting 사용 → **신형 LISEM 계열**로 판정. **우리가 돌렸던 OpenLISEM Classic 7.5.2의 수치문제를 이 1cm 사례 또는 신형 LISEM 프로그램 전체에 전가해서는 안 됨**. 반대로 Epple 1cm 실험에서 canopy active/leafdrip validated라고 단정하면 안 됨.
- **Maggioli et al.(2022) 5cm LISEM**은 De Roo/Jetten classic LISEM의 kinematic wave 구조를 사용한 것으로 원문 판단, 정확 실행버전 미기재.
- 신형 LISEM https://lisemmodel.com/docs/hydrology/ 에 **LAI와 clumped grass/broadleaved forest 수관최대저류식** 및 셀별 canopy 입력이 명시되어, 새 계열의 필수식생 기능이 문서상 존재. **추가 필요한 것은 신형 LISEM 동일 executable의 canopy + 1cm 격자 + native sediment balance/2D/DoD 검증**.
## 2026-10-27 긴급 정정: 5cm LAI 수관저류+LISEM 침식 및 1cm LISEM 모의 논문 확인
- [**정정 결정문**](decisions/2026-10-27_SUB10CM_LISEM_NEW_PUBLISHED_EVIDENCE_REVERSAL.md): 과거 '10cm 이하에 수관차단과 침식 동시에 있는 연구가 미확인'이라는 결론은 새 문헌 조사로 **철회**한다.
- **Maggioli et al. (2022)** [paper](papers/2022_Maggioli_RodriguezCaballero_LISEM_5cm_TLS_LAI_Interception_Erosion.md), [DOI](https://doi.org/10.3389/fevo.2022.765148): 스페인 25×15m 사면, TLS 5cm, LISEM 5cm, 1초, TLS 식생피복으로 LAI 추정해 수관저류 계산, 18개 강우사상 유출-침식, 18개월 누적 지형변화량 비교. 단 유출은 kinematic wave, 실제 전방위 full 2D SWE 및 5cm 국지퇴적 DoD 검증 아님.
- **Epple et al. (2025)** [paper](papers/2025_Epple_Bienert_Grothum_LISEM_1cm_PTV_DoD_Erosion.md), [DOI](https://doi.org/10.1002/esp.70127): 독일 3m² 미만 4개 강우모사 실험포, **LISEM 1cm** 격자, 시간별 지형고도 업데이트, PTV 관측 지표유속과 SfM DoD 모델 비교. 해당 실험에서 LAI 수관차단 활성 검증은 없음.
- **Naranjo et al. (2021)** [paper](papers/2021_Naranjo_OpenLISEM_DTM_1to15m_4m_Sediment_Anomaly.md): OpenLISEM v4.96, 4m 격자에서 유사량 이상치 보고. 다른 버전 7.5.2의 원인과 동일하다고 단정할 수 없으나 수치안정성 위험 독립 근거.
- 과거 Gounsa OpenLISEM **7.5.2 원본 5m 2D 12회 시뮬레이션 Δt 유사량 비수렴 NO-GO**는 문헌 존재만으로 무효화되지 않음. **정확 실행 소스코드 버전과 구현 수리경로 추적 후 재검토**.

## 2026-10-27 10cm 이하 수관차단+유수침식 단일모델 엄격 재탐색
- **[cm급 단일모델 문헌 및 원본 상한 평가](decisions/2026-10-27_SHETRAN_SUB10CM_CANOPY_EROSION_MODEL_SCREEN.md)**: SHETRAN 기존 4m native 통과, `NELEE=250000`으로 0.648ha 전면 10cm(648000 지표셀) 현재 배열상한 초과; 코드 확장 및 cm급 수지/수렴 검증을 하지 않은 상태. 수관/침식 코드 기능 자체는 기존 검증됨.
- OpenLISEM 개발자 README 1cm(2m²) 시험기록은 있으나 과거 고운사 7.5.2 원본 5m 2D 유사수송 시간격자 비수렴/토양재고 위반 기록으로 NO-GO 유지. PSEM_2D Nord & Esteves(2005)의 **5cm 실증**은 확인됐지만 수관차단 및 식생피복 효과가 원문에서 명시적 미구현이라 탈락. SMODERP2D는 공식 권장 2–20m 격자. **문헌 정정: 5cm LISEM의 LAI 관련 수관저류 및 유출과 침식 통합 계산은 Maggioli et al. (2022)에서 확인했고, 1cm LISEM의 유동·지형변화와 DoD 비교는 Epple et al. (2025)에서 확인했다. 다만 동일 공개 원본에서 수관적하+전방위 2D+유사수지까지 함께 검증한 근거는 부족함. [정정 결론](decisions/2026-10-27_SUB10CM_LISEM_NEW_PUBLISHED_EVIDENCE_REVERSAL.md)**. 기존 SHETRAN 10cm 배열상한 수정은 논문선례 없는 확장으로 우선 권고하지 않으며, LISEM의 2022·2025 논문 실행버전과 수문·유사 안정성 검증을 우선 추적한다.
- 관련 새 문헌: `papers/2005_Nord_Esteves_PSEM2D_5cm_BareSoil.md`.

## 2026-10-27 최신 SHETRAN 사용 논문 조사: 2022~2026
- 2026 Tafesse et al. (2025-12-30 online, Geocarto International 2026): GRACE+SHETRAN 5km×5km 지표·지하수 저장량 대조. 침식모듈 검증은 아님.
- 2025 Sayers et al. (J Flood Risk Management): 영국 전국 산림/홍수관리 SHETRAN 시나리오에서 수관차단수 잠재 증발을 산림 피복비율과 연동. 유사침식 계산 근거 아님.
- 2025 Oyarmoi et al. (Ecohydrology): 우간다 파피루스 습지에서 관개와 유역 습지유입 시계열 수문계산.
- **2024 Adams & Johnston (Nature-Based Solutions, 100118)**: 북아일랜드 버드나무/초지 비교. SHETRAN CLAI=0.2–1.2 vs1.0, CSTCAP=5mm vs1mm, RD1.6 vs1.0m, 조도 다르게 입력. 수관차단 증발 163→209mm와 모의 유출수고 569→560mm. 직접 SHETRAN sediment 모델을 검증한 것은 아님.
- 2024 Smith et al. (Frontiers in Water 1468855): 698 영국 유역 수문 보정, 중앙 NSE0.82; 기후/자연홍수관리/산림 시나리오. 수문중심.
- 2023 Barnes et al. (Hydrological Processes e14920): SHETRAN 100% 산림 vs 100% 초지, Irthing 큰첨두 4.4% 감소, 평균 20첨두17.7% 감소(일반화를 피할 것). 수문중심.
- **2022 Escobar-Ruiz et al. (Hydrological Processes e14474)**: **84 강우사상**, 2개 영국 농경유역의 피복 공간배치/완충대 변화, 유사량 사건별 차이. 산림 완충대 일부 사상 유사량 최대 20% 감소.
- **2022 Sreedevi et al. (Catena 106427)**: 인도 서고츠 Vamanapuram 787km², 수문과 유사수송(토지피복변화와 기후) 통합. 과거 토지피복 변화 유사량 -10.4% 모의.
- **2026-10-18 Rehman et al.**: SHETRAN+NSGA-II 자연홍수관리 최적화 preprint, 미동료심사. 저널 출판 연구로 혼동 금지. https://doi.org/10.31223/X51V57 .
- 신규 개별 기록 `papers/2026_Tafesse_GRACE_SHETRAN_Ethiopia_WaterStorage.md`, `2025_Sayers_National_NFM_SHETRAN_Woodland.md`, `2025_Oyarmoi_Papyrus_SHETRAN_Flow_Regime.md`, `2024_Adams_Johnston_SHETRAN_SRC_Willows_Phosphorus.md`, `2024_Smith_Birkinshaw_UK_698_SHETRAN_Climate.md`, `2023_Barnes_Bathurst_Afforestation_LeakyDams_SHETRAN.md`.
- 중요: 최신 논문에서 명시적 SHA `cf9cd540...` SHETRAN 4.7.2 사용 입증하지 못함. 학술적 계보와 정확 코드버전 인용을 구분한다.

## 2026-10-27 SHETRAN 4.7.2 코드-논문 계보 및 실제 적용 연구 조사
- **[원본 버전과 13편의 주요 연구를 연결한 기록](decisions/2026-10-27_SHETRAN_472_CODE_PAPER_PROVENANCE_AND_APPLICATIONS.md)**: SHETRAN4.7.2 원본 `nclwater/Shetran` commit `cf9cd540`(2026-10-12), 정식모델 Ewen et al.(2000), 침식물리식 Wicks & Bathurst(1996), 기존 식생/침식 적용 Lukey(1995,2000), Birkinshaw(2011), 소사면 Bathurst et al.(1998) 0.133ha/5m, Adams(2005) 970m² 및 Adams & Elliott(2006) 토사량, Dano(2017) 공간 E/D 지도를 구분 정리. **과거 논문이 2026 commit을 그대로 이용한 것은 아님**.
- **141mm 국지 퇴적은 150mm 누적 강우와 모순되지 않음**. 외부 유사 유입/사면내 집중에 따라 국지 퇴적이 발생할 수 있으므로 물리적 불가능이라고 단정하지 않는다. DLS 느슨한 표면층 체적, 실제 토심/안정 퇴적, 고체체적은 구별한다.

## 2026-10-27 SHETRAN 실제 적용 연구 7편 추가 확인 및 문헌보강
- **[소규모 사면 강우침식 직접검증](papers/2006_Adams_Elliott_SHETRAN_LargeRainfallSimulator.md)**: 뉴질랜드 약 970m² 인공강우 사면에서 강우충격/유수박리계수 및 유사량 대조. 단일 강우사상 고운사 연구와 가장 근접.
- **[산림과 벌채 유사배출 및 극한강우](papers/2011_Birkinshaw_Bathurst_Iroume_SHETRAN_ForestCover_Chile.md)**: 칠레 La Reina 35ha 모의 숲 3.6 대 벌채 8.3t/ha/년, 1000년 합성강우에서 고강우 조건 상대 수문효과 감소와 침식저감 지속. 관측된 유사량의 독립 전수 검증은 아님.
- **[84개 강우사상 피복시나리오](papers/2022_EscobarRuiz_SHETRAN_EventScale_LandCover.md)**: 전체사상 통계효과와 특정 강우사상 식생저감 효과 구분.
- **[상류/하류 산림 패치 배치](papers/2006_Birkinshaw_Bathurst_SHETRAN_SedimentYield_BasinArea.md)**: 산림 및 작물 피복의 위치, 사면/하안 유사공급 원천에 따라 하류 토사유출 면적 의존성이 역전 가능.
- **[인도 습윤 산림산지](papers/2022_Sreedevi_Eldho_Jayasankar_SHETRAN_HumidTropical.md)**: 서고츠산맥 유역에서 토지피복/기후/유사량을 동시 모의.
- **[알프스 산사태 모듈](papers/2005_Bathurst_SHETRAN_Valsassina_Landslides.md)**: SHESED 지표유출 침식과 다른 shallow-landslide 유사공급 별도 연구.
- **[하안침식 식생 모듈의 연구자 개선형](papers/2017_Janes_SHETRAN_Riverbank_Vegetation.md)**: 원본 4.7.2와 새롭게 수정된 bank erosion 처리를 구분.
- 기존 1992 Wicks, 1996 Wicks & Bathurst, 2000 Lukey, 2017 Op de Hipt, 2019 Escobar-Ruiz 파일에 2026-10-27 주모델 선정 이후 판정 정정 추가.
- 이번 문헌의 공통 교훈: SHETRAN은 단일 강우사상 수관/유수 침식 적용 근거가 있으나, **유량검증과 유사량검증, 유역 유사량과 4m 격자 국지 퇴적고 검증을 분리**해야 한다. **141.487mm 국지 퇴적은 물리적으로 불가능하다고 판단할 수 없으며** 각 격자 유사 유입, 유출, 느슨한 퇴적층과 공극률을 검토하는 것이 올바르다.

## 2026-10-27 결정 확정: 단일 강우사상 유수침식 주모델 SHETRAN 4.7.2 선정
- **[공식 모델 선정 결정문](decisions/2026-10-27_SHETRAN_SELECTED_AS_GOUNSA_SINGLE_STORM_EROSION_ENGINE.md)**. 고운사 참나무 맹아 및 억새 혼재 사면의 **수관차단 ON/OFF, 강우사상별 2D 국지 침식 및 퇴적, 네 방향 경계 물과 유사배출** 분석을 위해 **SHETRAN 4.7.2를 단일 유수침식 주모델로 채택**. EUROSEM 및 OpenLISEM 등의 주엔진 재탐색은 중단하고 SHETRAN 자체 검증과 실제 입력자료 구축에 집중한다.
- 선정 근거: 공개 Fortran 원본의 수관저류/수관적하/직접강우 및 유수박리/4면 유사수송 연계, 합성 0.648ha 사면 **35/35 실제 실행**, 네 방향 Type 5 개방경계의 물과 유사배출 및 최대 상대 이동가능 유사수지 잔차 5.84668e−14.
- **연구용 주모델 선정과 현장 정량 검증은 별개:** 가상 개방계수 k=50 미보정, 혼재 50mm/h 최대 국지 퇴적 141.487mm 물리적 타당성 미확인, 4m→2m→1m 공간수렴 및 실측 DEM/LAI/식생배치/토심/토양자료 필요. 이전 보고서에 적힌 '주모델 채택 보류'는 **이번 사용자 결정으로 연구용 엔진에 한하여 변경**되나, '고운사 현장 침식량 검증 보류'는 유지.
- 다음 우선순위: **경계배출계수와 방향별 배출량 → 극단 국지 퇴적 원인/물질수지 → 공간수렴 → 현장보정 및 ON/OFF 차분**. 지표고도는 사상 내 유동 계산에 자동 재투입되지 않음.

## 2026-10-27 완료: SHETRAN 0.648ha 참나무 맹아 및 억새 4피복 × 강우10–50mm/h 네이티브 35시나리오
- **[최종 35회 결과 및 한계](decisions/2026-10-27_SHETRAN_LARGER_HILLSLOPE_35_NATIVE_RESULTS.md)**. 한 모델 SHETRAN 4.7.2 원본 물리식, static `NOCTAB 20→80` 배열상한 확장/진단출력 추가만 실행. 405개 육상4m 셀=0.648ha, 17×29 격자 경계 포함0.7888ha, 10/20/30/40/50mm/h×3h; 나지, 억새 전면, 참나무 맹아102/나지303, 참나무102+억새228+나지75 패치; canopy ON/OFF 별도 35 조합.
- **원본 물리식 엔진 35/35 성공, 유사고체체적 native mass ledger 각 0.1% 이내 통과, 순차 35회와 독립 병렬 35회 source 및 ∆z 총계가 소수점까지 완전 동일 재현**. [순차 결과 CSV](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40448419992/artifacts/12710245614), [5강우 독립 시험](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40448993167).
- 수관 ON의 원토양 박리 공급 `m³ solid`, 강우10→50: 나지 1.439→28.371, 억새 0.993→27.607, 참나무 드문 패치 1.300→27.920, 억새+참나무혼재 1.053→27.681. **10mm/h 억새 vs 나지 감소31.0%**, 50mm/h 감소2.7%, 가상 파라미터에만 해당.
- **중대한 현실성 미검증:** 50mm/h의 무유출구 폐쇄 가상사면에서는 최대 국지 순상승 **+406.5mm**가 발생, 20mm/h에서도 +102.3mm. 물/유사 출구가 막힌 조건에서 퇴적량이 과도하게 축적될 수 있으므로 **실제 고운사의 국지 퇴적량 정량 주장 절대 금지**. 원본은 강우 중 진단 ∆z를 수문 DEM으로 재투입하지 않으며 토심재고 한계도 미구현. 실제 고운사 DEM/LAI/수관 적하/강우/토심/토성 및 open-outlet 검증, 2m 이하 dx 민감도 필수.
- [405격자 실제 SHETRAN 결과로 만든 합성 2D 지도17장](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40450170885/artifacts/12710256837): 10/30/50mm/h×4피복 순고도지도 12장, 혼재수관 ON−OFF 차분3장, 패치맵1장, 강우별 원토양 박리 곡선1장. 폐쇄경계의 극단 퇴적값은 colorbar 제한하고 실제 max를 그림에 따로 표기. **Gounsa 현장지도 아님**.
- 이전 `PMAX/TMAX` 입력 필드 오독은 [중대 정정문](decisions/2026-10-27_SHETRAN_TIMESTEP_ROOT_CAUSE_CRITICAL_CORRECTION.md) 참조. 원본의 시간간격 nonconvergence 이유로 탈락했던 잘못된 판단은 철회 유지. **단일모델 SHETRAN의 식생 수관차단 및 2D 국지 침식퇴적 기능 시험은 통과, 고운사 현장 검증 최종 채택은 보류**.



## 2026-10-27 SHETRAN 0.648ha 네 방향 개방경계 35개 실행 모두 검증 (최신)
- [동서남북 80개 가장자리 격자 native Type5 polynomial open boundary 전체 35개 ON/OFF 실제 실행 + 물과 유사 경계배출 검증보고서](decisions/2026-10-27_SHETRAN_OPEN_FOUR_SIDES_0P648HA_35_SCENARIOS_NATIVE.md). [GitHub Actions 40455147463](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40455147463) 강우 10/20/30/40/50mm/h×3h, 4 피복 나지/억새/참나무 맹아 소군집/참나무+억새 혼재패치, 식생 3조건 canopy ON/OFF 총 35/35 원본 계산식 native PASS.
- 기존 폐쇄형 0.648ha 실험의 경계 유사배출 0이었던 문제를 해결. 원본 SHETRAN native OC Type5 `Q_out=50 h²` 가상 계수 설정. 원본 `SYCOLM` 경계 `QSED` 처리 때문에 `SYBC` (time-varying sediment inlet metadata stub)이 비어 있어도 **경계 밖 유사배출이 가능**함을 native 유사수지 실측으로 확인. 모든 35개 케이스 water export>0 and sediment export>0. 전 케이스의 native 상대 이동가능 유사수지 최대 잔차 5.84668e−14. static BC 배열 `NOCTAB=20→180` 확장만 물리식과 별도로 적용. 기존 Type1 불투수와 Type5 중복 오류는 FRD 타입을 바로잡아 해결.
- 수관 ON native **경계 유사배출** [나지, 억새, 듬성한 참나무, 혼재] m³ solid: 10mm/h [0.041621,0.021589,0.032156,0.022436], 20mm/h [2.990695,2.853339,2.927945,2.858082], 30mm/h [7.935353,7.752950,7.855421,7.760990], 40mm/h [14.531496,14.309311,14.432845,14.316509], 50mm/h [21.630846,21.396716,21.528775,21.404709]. 반드시 원토양 **새 박리 공급량과 구분**.
- 50mm/h 혼재 ON 최대 국지 순퇴적: 폐쇄 경계 약405.89mm→네방향 개방 경계 **141.49mm** (약65% 감소). 여전히 synthetic hypothetical high, 실제 고운사 DEM/LAI/토양/토심/경계관측 자료가 아니라 연구 결론으로 사용 불가. Type5 배출계수 k 민감도, 각 방향 outflow 실제 공간위치, 동일 영역 세밀 dx 수렴 미검증. [원본 405셀 지도 재생성](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/.github/workflows/shetran_render_405cell_open_4edges_20261027.yml).

## 2026-10-27 SHETRAN 실제 시간격자 14초까지 재검증 완료: 총량과 국지 퇴적위치 안정성 개선 (최신)
- **중요 정정: [원본에서 발견한 PMAX/TMAX 입력 위치 오해](decisions/2026-10-27_SHETRAN_TIMESTEP_ROOT_CAUSE_CRITICAL_CORRECTION.md)**. 원본 `FRmod.f90`은 `(4F7.0,L7)` 순서 `PMAX,PALFA,QMAX,TMAX,BSOFT`를 읽는다. 이전 시간간격 실험 도구는 실제로 **첫 필드 PMAX**(강우량 기반 시간간격 제한)만 바꾸고 **넷째 필드 TMAX는 1h 그대로** 유지했으므로 **종전 "SHETRAN TMAX 수렴성 불합격" 판정을 철회한다**. 그 1~6% 차이는 PMAX 민감도이며 원본 TMAX 수렴 실패가 아니다.
- **원본 실제 TMAX 14초 및 176셀 국지 순고도 검증 성공:** [원본 8회 450→56초](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40445638896), [원본 8회 112.5→14.06초](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40446202523), [원본 176셀 ∆z 수렴 비교](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40446161132). 진짜 네 번째 `TMAX` 필드만 변경, 첫 `PMAX=1mm` 고정 및 `BSOFT=F`. 28초 vs14초 누적 박리량 차이 **ON 0.4639%, OFF 0.3608%**, 셀별 순고도 변화 평균절대차 **ON .0000942mm, OFF .0000871mm**, 국지 순퇴적 `∆z>0.001mm` 핫스폿 일치 **ON 5/6, OFF 4/4**. 전체강우 90mm, 비수관 증발산 0, 유사수지 보존 통과. **기존 'TMAX 수치수렴 실패'는 전임 QA가 PMAX를 오변경한 결과이므로 폐기**, 실제 시간간격 안정성은 크게 개선됨. 다만 아직 현장 DEM/LAI/강우, 개방 유출구, 실제 0.5~2m 같은영역 공간수렴, 토심 고갈 검증이 없어 고운사 최종 정량예측 엔진으로 확정하지 않음. [전면 정정 및 원본 증거](decisions/2026-10-27_SHETRAN_TIMESTEP_ROOT_CAUSE_CRITICAL_CORRECTION.md).

## 2026-10-27 SHETRAN 엄격 실제실행 결과 및 모델 선정 보류 (최신)
- [단일모델 SHETRAN 원본 4m 사면 및 수관차단 ON/OFF 검증 전체 보고서](decisions/2026-10-27_SHETRAN_STRICT_NATIVE_SMALL_PLOT_VALIDATION_VERDICT.md). 연구질문은 **1ha 미만 동일 사면의 참나무 맹아+억새 혼재, 한 강우사상, 수관차단 ON/OFF, 2D 국지 순침식 및 순퇴적**이며 장기 LPJ-GUESS나 다른 침식모형 결합은 제외.
- 원본 `nclwater/Shetran` 4.7.2 SHA `cf9cd540add78ad3accbaf62b4199d2032887f6b`, 별도 진단용 Fortran `WRITE`만 삽입. 4m×176 셀(2816m²) **가상 사면**에서 NVC 2유형 원본 네이티브 ON/OFF 성공. 수관 물수지 최대 9.77e−15 mm, PET=0 조건 뿌리흡수/토양증발 ON/OFF 교란 0 [Actions 40443924320](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40443924320).
- 토사수지 ON 0.000406%, OFF 0.001575% [Actions 40441094575](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40441094575). 격자별 유입/유출과 비국지 표층저장 증가 ON 74/OFF 72셀 [Actions 40442738443](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40442738443). 실제 격자 고도 후처리 `∆z=∆DLS−ΣGNU∆t`에서 ON 상승 5, 하강 161개, OFF 상승 4, 하강 166개. ON−OFF 최대 같은 셀 ∆z 차 0.00684mm [Actions 40443359926](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40443359926). **사상 중 유동 DEM 갱신 기능은 없음.**
- 초기 mobile DLS=0/1/10/30mm native 8/8 실행 통과, 원토양 박리량 등 거의 변화 없음 [Actions 40444030737](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40444030737). **중요 수정:** 2026-10-27의 소위 TMAX 관련 ON 4.8888%, OFF 2.1253% 차이는 실제 `PMAX` 강우량시간분할 파라미터 변경 결과. **TMAX 비수렴 증거로 사용 금지.** 원본시간간격 실험 재실행 중이며 결과를 확인해 판정한다.
- 폐쇄형 경계로 유사 배출 0, 동일 영역 2m/1m/0.5m `dx` 수렴 미검증, 원토양 H finite limit 없음, 실제 Gounsa DEM/LAI/강우/토양자료 및 현장 침식검증 없음. **최종 현장 연구용 주모델 채택은 여전히 보류/NO-GO**. 수관 자체 구현과 국지 유사축적 존재는 코드 기능 시험에서 통과했음. EUROSEM은 1D이며 세류수지 실패로 고운사 2D 주모델 제외 유지.


## 2026-10-27 긴급 단일모델 코드 심층감사: SHETRAN vs EUROSEM
- [2026-10-27 원본 코드 감사와 엄격 판정](decisions/2026-10-27_SHETRAN_EUROSEM_SINGLE_MODEL_NATIVE_CODE_AUDIT.md): 수관저류 → 직접강우/잎적하 → 2D 흐름 → 강우/유수박리 → 입경별 4면 이송과 퇴적의 **원본 함수**를 실제 GitHub 파일에서 새로 읽어 확인. 새 빌드/모의 실행 없이 기존 2026-10-26 GitHub Actions 원본 실행/질량수지 기록과 대조.
- **EUROSEM 1998:** `INTERC`는 `COVER,DINT` 누적강우 기반 저장 및 `DRIPD/STEMD/TFALL` 존재, 그러나 원본 LAI 상태 미구현 및 `PLANE`의 1D 연결 사면구조. `KINET`→`DRIPS`의 적하분율 이중 가중, 특정 첫 강우간격 저장량 초과 가능, 세류 유사수지 dt15s 잔차 14.32–21.48% 확인(기존 24-run 실험). **동일 1ha 미만 혼재식생 2D 국지 E/D 지도용으로 구조적 탈락**. 1D 작동 부분은 별도 문헌 참조 가치 있음.
- **SHETRAN 4.7.2:** `ETSIM→ETIN→ET`는 `CSTORE/CSTCAP/CK/CB/DRAIN/PNETTO/DRAINA`; `SYMAIN→SYWAT→SYOVER→SYCOLM`는 직접강우와 적하, 강우/유수박리, 4방향 유사교환, 국지 `DLS` 갱신; `NVC(IEL)`로 식생유형별 셀 구분 가능. 하지만 `CPLAI=MIN(CLAI,1)*PLAI`의 LAI 포화, 별도 수관저장능 입력, 0 저장능 분기 divide risk, 첫 sediment step 초기화만 수행, `GNU` substep 일정, 퇴적-토심 stock 제한 미구현, `BALSED` 빈 함수, 2D 확산파(완전 운동량 방정식 아님), 사건 내 DEM 변화 유동 반영 안함을 **중대한 검증조건**으로 표시. 기존 원본 Cobres 2km 6회 native 성공은 0.5m 혼재 사면 수렴/보존/현장 검증 근거가 아님.
- **단일모델 판정:** SHETRAN만 조건부 코드기능 후보로 유지, **최종 선정/고운사 결과 재현은 아직 불합격 보류**. 기존 장기 LPJ/풍화 중심 제출용 설계 및 Rutter+SWEHR 신규 coupling 권고는 이 단일 강우사상·단일모델 목적에 사용하지 않는다.


> **2026-10-27 18:00 제출용 범위 정정 (최신):** [동일한 1ha 미만 고운사 혼재식생 사면의 단일 강우사상 수관차단 OFF/ON 국지 침식·퇴적 공간차분 연구](decisions/2026-10-27_SINGLE_STORM_MIXED_OAK_MISCANTHUS_CANOPY_ABLATION_PROTOCOL.md). 대상은 참나무 맹아+억새의 **동일 실측 공간배치**이며 결과는 격자별 원토양 박리, 퇴적, 순 지표고도변화 및 B−A 차분. 2026-10-26의 장기 LPJ/풍화 중심 '마감용 설계'는 사용자가 명시적으로 부정했으며 [해당 초안은 폐기 표시](decisions/2026-10-26_DEADLINE_GOUNSA_MODEL_ARCHITECTURE_AND_DATA_PLAN.md)됨. LPJ-GUESS·장기 풍화/천이는 이 **단일 사건 목적에 필수 아님**. SWEHR 공개 C의 수관차단 미구현 및 현장 검증 부재는 계속 명시.\n\n
> **2026-10-26 EUROSEM 낮은 식생 민감도 기존 폐기근거 정정:** 개인 Library의 원래 729행 CSV와 원래 `eurosem-single-model-lai-20261025` 실험 코드를 추적한 결과 (1) PLANTH=3cm여서 원본 leaf-drip KE 0, (2) LAI는 원본 변수가 아니라 **새 LAI.PAR 패치**로 넣은 상태량, (3) 원본 `eurseml.for`은 `DRIPD/RAIN`을 kinetic energy와 drip-rate에 각각 곱해 leaf-drip 박리항에 **비율 제곱 오류**, (4) `eusedl.for` 원토양 박리 source와 수송능력 항 간 수량 단위 및 폭 처리 불일치 의심이 확인됨. **원본 기반 20회 추가 native Fortran 시험 및 8회 폭 가설 시험**에서 높이 120cm, EROD 0.1→0.9 및 leaf-drip 비율 수정 시 내부 `RDET`는 ×9 혹은 ×1.5로 바뀌지만 최종 순침식량은 그대로였고, `DTRF*CEX`가 수치상 압도. 이는 **기존 '식생 자체가 무효' 결론이 부당**하다는 뜻이나 원본이 genuine 2D가 되거나 유사수지가 검증됐다는 뜻은 아님. **EUROSEM 1D 산림 수관-침식 보조식 진단모델로 재평가, 고운사 2D 주 엔진 선정 아님.** [새 정밀 감사](decisions/2026-10-26_EUROSEM_729_LOW_VEGETATION_SENSITIVITY_ROOT_CAUSE_REAUDIT.md) / [모델 계보](models/EUROSEM.md).

> **2026-10-26 EUROSEM 식생 민감도 반례 재검증, 기존 결론 정정:** 2025년 `LAI.PAR` 추가 포크의 729회 실제 CSV를 복구한 뒤 원본 `TheSoilman/EUROSEM` SHA `8652944...`와 모델 브랜치 비교. LAI2.5 때 실험용 `SKLAI=min(COVER,.046 LAI)=.115`가 피복률 .5/.9에서 동일 유효강우를 생성, 그 당시 높이 입력3은 3m 아닌 **3cm**이므로 적하 KE가 0. 원본 `KINET`와 `DRIPS`에서 적하비율이 **제곱 적용**되는 추가 코드 문제 발견. **새 24회 전체 native 실행 통과**(3 COVER×2 높이×2 EROD×2 MCODE), 150cm KE 양수에도 총침식 거의 무반응, EROD .1→.9 무반응, MCODE0=Govers ↔1=Everaert은 첫 요소 37,829.734→44,036.523kg(16.4%) 반응. 진단 한 줄 DRIPS 수정 포크 12쌍 **총24회 완료**, 내부 drip detachment 2.65–28.12배 상승하나 최종 source-reported net 동일. Native `eusedl.for` 소스-수송능력 표본에서는 `DTRF*CEX`가 `RDET`보다 >5×10⁵배 커서 이번 시험의 박리항이 사실상 수송능력 관련 공급에 압도됨. **따라서 'EUROSEM 원래 식생 무영향' 기각 근거는 잘못된 시험 설정의 산물이며 철회**. 그러나 EUROSEM은 **진정한 2D 아님**, 독립 sediment closure 안 됨, 고운사 주 엔진 탈락 유지; 원본 수관 및 splash 기준식 참고만. [전체 소스 감사](decisions/2026-10-26_EUROSEM_PREVIOUS_LOW_VEGETATION_SENSITIVITY_FORENSIC.md), [원본 24 실행](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40319063481), [drip A/B 24 실행](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40319799767), [원본 수송항 계측](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40320553800).

> **2026-10-26 신규 독립 공개 원본 엄격 소스 감사:** 과거 탈락 Classic OpenLISEM 7.5.2를 재추천하지 않고, [별개 LISEM Integrated C++/OpenCL](models/LISEM_Integrated_VanDenBout_Source_Audit.md)의 실제 `SMAX Canopy` 입력 무효화(`SCANOPYN=0`, `h+=store_canopy`, `throughfall=vegcover×rain`)를 확인해 LAI 수관물수지 부재로 **탈락**. [SEIMS](models/SEIMS.md) C++에는 splash+flow detachment가 나뉘지만 실제 유사수송은 KinWav upstream graph라 2D conservative sediment가 아니며 동적 LAI canopy/leafdrip도 원본 구현 입증 못해 **탈락**. [SERGHEI-SE](models/SERGHEI_SE.md)는 이미 기록된 2D 수치 침식모델이며 native LAI canopy store→drip 검증 없으므로 **주모델 제외, 독립 2D 검증 근거 유지**. [GRASS SIMWE/r.sim.terrain](models/GRASS_SIMWE_RSimTerrain.md)는 2D stochastic overland sediment와 DEM 변화, Fort Bragg LiDAR 세류 검증 선례가 있지만 canopy LAI 및 leafdrip 미검증이라 **주모델 제외, TLS 지형비교 후보**. 새 [SW2D 2026](papers/2026_FinaudGuyot_SW2D_Porosity_ShallowWater.md)도 수류 2D 원본이지만 sediment 원본 미확인이라 **탈락**. 5종 중 전 조건 원본 통과 후보 **0종**, 컴파일 및 시간간격 수렴성은 실행하지 않음. 근거 [최신 결정](decisions/2026-10-26_POST_TIMEOUT_NEW_2D_ENGINES_SERGHEI_LISEM_SEIMS.md).

> **2026-10-26 전송 시간 초과 이후 원본 소스 재검증:** 공개 MIT tRIBS 6.0은 Rutter 수관차단은 구현하지만 과거 김 등(2013) FEaST의 Hairsine–Rose 2D 유사계산 코드가 공식 저장소에 없음(모델 별도). 공개 wflow_sbm + wflow_sediment는 `Cmax=Sl*LAI+Swood`, `exp(-Kext LAI)`, direct/leafdrip 운동에너지와 유수박리까지 native 확인되지만 sediment 이송이 PCRaster `accucapacityflux` LDD/kinematic routing으로 진정한 2D 유사연속방정식 아님. HydroPol2D는 LAI 기반 2D 수문 원본만 있고 침식소스 없음. **SWAT+ 2026 공개 원본의 `ero_ovrsed.f90`은 subdaily에서 MUSLE 대신 직접강우/잎적하 분리+유수침식을 구현했지만 `canopy_cover=min(1,LAI)`로 LAI≥1 차이를 소거하고 HRU 기반이지 진정한 2D 유사이송 엔진이 아님.** 모두 주 엔진 후보 탈락 유지. 신뢰도 높은 새로운 수관하 침식에너지 보조근거: Li & Tian (2026) HESS DOI 10.5194/hess-30-3203-2026, 9개 현장자료로 LAI·잎경사에 따른 수관하 직접/적하 운동에너지 검증, 유수침식 원본 모델 아님. [소스 검증 결정](decisions/2026-10-26_TIMEOUT_RECOVERY_SWATPLUS_SOURCE_GATE.md); [SWAT+ 소스 계보](models/SWAT_PLUS_Subdaily_Erosion.md); [Li & Tian 2026](papers/2026_Li_Tian_UnderCanopyKineticEnergy.md).

> **2026-10-26 추가 소스 선별: HydroPol2D 등 통합 침식 후보 아님.** HydroPol2D GPL MATLAB 원본은 `interceptionModel.m`의 `Smax=C×LAI`, `interception_module.m`의 LAI/throughfall, 실제 2D local-inertial 유동이 확인됐지만 오염물질 `build-up/wash-off`는 **물리적 강우박리 및 유사퇴적 모델이 아니므로 제외**. HydroSed2D는 2D SWE와 sediment GPL 원본 프로젝트나 LAI 식생차단/leaf-drip 없음, WASA-SED는 semi-distributed, ParFlow는 식생수문을 고려하지만 공식 소스에서 침식과 유사수송 구현 확인 안 됨. 모두 완전한 고운사 주모델에 미달. [추가 후보 엄격 감사](decisions/2026-10-26_WFLOW_TRIBS_FEST_SSEM_STRICT_SOURCE_GATE.md), [HydroPol2D 원본 확인](models/HydroPol2D.md).

> **2026-10-26 신규 모델 4계열 원본 소스 재검색(Wflow.jl, tRIBS-FEaST, FeST, 한국 SSEM):** **Wflow.jl/wflow_sediment**는 Deltares 공개 Julia 원본에서 LAI→수관저류와 공극률, Rutter/Gash 수관통과, EUROSEM 직접강우/수관적하 박리, ANSWERS 지표유출 박리를 모두 확인한 중요한 *부분 충족* 모델. 그러나 유사 사면수송은 `accucapacityflux_rate!` 유향망 기반이므로 **genuine 2D sediment advection 주 엔진 탈락**. **tRIBS-FEaST**의 Kim et al.(2013) 및 Kim·Han·Cho(2014) 논문에는 진정한 2D Saint-Venant + Hairsine–Rose 결합이 실재하지만 2026 공식 `tRIBS-Model/tRIBS` 공개 C++에는 Rutter 수관차단만 확인, 발표된 FEaST Hairsine–Rose 침식 소스 **없음** → 실제 재현 가능한 완전 공개 원본 주 엔진에서 탈락. **FeST** 공식 Fortran은 LAI 기반 수관차단과 interrill 침식이 있지만 유사는 flow-direction 및 Muskingum–Cunge 하도 중심으로 **사면 2D 침식 불충족**. **Song et al.(2024) 내린천 SSEM**은 한국 급경사 90% 이상 산림유역 실제 논문이지만 250m 격자의 **1D 운동파 및 유향망**, LAI 수관적하 부재 및 원본 계산소스 미확인으로 탈락. *완전히 통과한 새 원본 없음. 기존 탈락 엔진 재추천 금지.* [원본감사 결정문](decisions/2026-10-26_WFLOW_TRIBS_FEST_SSEM_STRICT_SOURCE_GATE.md), [Wflow 모델](models/Wflow_Sediment.md), [tRIBS-FEaST 모델](models/tRIBS_FEaST.md), [FeST 모델](models/FeST.md).

> **2026-10-26 사용자 지시 '의심이 되면 버려' — 신규 후보 엄격 탈락:** TREX **실제 공개 원본 미러 발견** (`WatershedModels/trex_src_csu` 233 src entries, 2018 version 101017), `Interception-r4.c`은 지정 저류심 차감 방식, native LAI 상태저류 및 leafdrip KE 없음 → 탈락. Iber+는 2024 NHESS Code/Data 문구에서 소스는 **협업자만 접근**, public V3.2b 파일은 실행 바이너리, native LAI/leafdrip도 미확인 → 탈락. ASTERIX는 2024 원저자 Future Extensions에서 **수관차단 미구현, Hairsine–Rose 침식 모듈 개발 예정**이라 했고 2025 발표도 유동모듈 → 탈락. OpenLISEM 원본 비수렴, SHETRAN 주세류 모형 부적합, SWEHR 원본 canopy 부재, DHSVM 공식 sediment source 부재, SMODERP sediment 미확인, EUROSEM 비2D, WEPP 비2D 등 과거 제외 유지. **최종 선정된 완전 원본 통합 엔진 없음.** 더 조사하더라도 완전한 원본 함수 및 native 수치 QA가 발견되지 않으면 주모델로 올리지 않는다. [근거 전체](decisions/2026-10-26_STRICT_REJECTION_TREX_IBER_ASTERIX.md).

> **2026-10-26 OpenLISEM 폐기 후 신규 소스 선별:** SHETRAN은 앞선 fit-for-purpose 감사에 따라 주 세류 침식 엔진 탈락 유지, DHSVM/Doten(2006)은 산지 forest canopy+leafdrip+runoff erosion published 논문이 있으나 현재 PNNL 공식 소스에는 침식 엔진이 없어 runnable 통합모형으로 추천 불가. **TREX/Velleux(2008)** 는 진정한 2D overland+sediment+한국 내성천/일본 후쿠시마 산림 적용 선례와 CSU 원본 C source/예제 제공 안내를 찾았지만 소스 ZIP 현행 접근 및 **LAI 기반 동적 canopy/leafdrip 계산을 아직 검증하지 못함**. **Iber+/Cea(2024)** 는 2D multi-size rainfall and flow erosion, loose-layer mass shielding, Exner, 프랑스 알프스 사례가 강하고 **Windows/Linux 검증용 실행파일과 실험입력 데이터가 실제 DOI 10.57745/UFEK4L에 공개됨**. 그러나 온전한 공개 소스와 native canopy LAI는 확인 안 됨. **SMODERP2D** 에는 LAI 비례 차단 코드가 있지만 독립 유사질량 및 강우/유수박리 전모형 확인 실패; SPHY는 일별 D8로 strict 2D 아님. *오늘 검토한 후보 중 필요조건을 전부 통과한 새 단일 원본은 아직 없음.* [새 결정](decisions/2026-10-26_POST_OPENLISEM_CANDIDATE_SOURCE_SCREENING.md), [TREX 모델](models/TREX.md), [Doten 논문](papers/2006_Doten_DHSVM_Mountain_Forest_Sediment.md), [Velleux 논문](papers/2008_Velleux_England_Julien_TREX_2D.md).

> **2026-10-26 실제 원본 Windows 2D 재시험 최종 판정: OpenLISEM 7.5.2 고운사 침식 주모델에서 제외(NO-GO).** 공식 원본 lisem.exe로 2D 계산 12회 성공, 강우 20mm, 양의 경계 유출, 전역 물/유사수지 폐합까지 확인했으나 유사유출량은 참나무 기본식 5/10/20초 각각 0.005993/123.037727/832.588686kg/ha, 참나무 개발진 제공 대체 침강식도 0.030954/28.707586/268.530307kg/ha로 극심하게 비수렴. 억새 대체식도 0.018893/0.044177/88.121322kg/ha. 20초 참나무 원본 기본식 최대 격자 순침식 5982.9t/ha로 가상 25cm 토층 3375t/ha 초과. 과거 실패가 **재현**됐으므로 LAI 기반 차단 및 2D 흐름 구현과 별개로 원본 버전은 고운사 침식 계산용으로 불합격. [새 Windows 원본 시험 보고](decisions/2026-10-26_OPENLISEM_752_NATIVE_2D_STABILITY_FAILED.md), [Actions](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40304135775). 

> **2026-10-26 OpenLISEM 최종 GO/NO-GO 판단 규칙:** 과거 원본 Windows 7.5.2 전체 실행은 가능했으나 계산 시간간격 의존성 및 100μm 침전속도 오류, 유한 토층 제한 부재로 침식 결과 **이미 FAIL baseline**. 이번 `v7.5.2` 및 `main_C` 공개 소스 재확인 결과 두 계보의 `GetSV` 원식이 동일하고 `main_C`의 `DetachMaterial()` 호출은 여전히 주석 처리, `SwitchUseMaterialDepth=false`. LAI/interception/2D 기능만으로 채택 금지. **원본 지원 옵션으로 경계/설정 정상화 후 2D 시간간격 수렴, 토사저장량, 침강, 물/유사수지가 통과하지 못하면 고운사 유수침식 엔진으로 폐기.** 수정 포크 성공은 원본 통과로 간주하지 않음. [사전 등록 검증 게이트](decisions/2026-10-26_OPENLISEM_NUMERICAL_GO_NOGO_GATES.md).

> **2026-10-26 중대 정정(운영 판정 우선):** OpenLISEM `v7.5.2` 원본 Windows 실행은 **2026-10-23 실제로 성공**했다(공식 `lisem.exe` headless 전체 모델, Actions runs `39928519655`, `39929498985`). 그러나 합성 고운사 사면의 침식 출력은 **시간간격 수렴성 실패**(운동파 참나무 유사유출 0.25→10초에서 19.714→853.798 kg/ha), **2D 격자별 과도한 순침식**(참나무 10초에서 200,566.703 t/ha ≈ 14.86m 토층), **원본 GetSV 100μm 분기 침전속도 오류**(1.27226m/s, 99.9μm 대비 141.8배), `DetachMaterial()` 비활성 등 문제가 확인됐다. 10월25일 factory 시험에는 `Advanced Options` 입력 생성 오류, GUI/엔진 설정 키 불일치, 유출구 배치 미검증도 중첩. **따라서 OpenLISEM이 LAI 차단+2D 직접유출 침식+산지 적용 세 조건을 기능 차원에서 갖춘 사실은 유효하지만, 원본 7.5.2를 바로 고운사 유수침식 주 엔진으로 재선정해서는 안 된다.** 정확한 이유와 QA 상태: [실패 원인 복구](decisions/2026-10-26_OPENLISEM_752_PREVIOUS_NUMERICAL_FAILURE_RECOVERY.md). 


> **2026-10-26 신규 확인(OpenLISEM, 기존 미확정 판정 유지):** 원본 `vjetten/openlisem` `main_C` SHA `d894c72428947247ce49eb88353dadf49b3123e8`의 `lisInterception.cpp` LAI 저장/수관통과, `lisErosionSplash.cpp` 직접강우와 잎 적하 에너지 분리, `lisSWOF2DSediment.cpp` 원본 2D 유출박리/수송 확인. **Opedes et al. (2025, DOI 10.1002/esp.70074)** 는 Mount Elgon Ukha 44.5km² 산지, 12.5m, 15s, 실제 2D dynamic wave와 LAI/height/litter/rock/root extra cohesion 입력을 사용했고 유출 NSE .72/KGE .61이나 침식 관측 검증은 없음. 코드는 stemflow input 주석 처리, 자동 개체별 SF 및 RLD 변환 없음. Windows 7.5.2 실행과 코드 hash 일치/물유사수지도 아직 미검증. **세 사용자 우선 조건에 매우 유망하나 stricter native dynamic root criterion 및 최종 실행 QA를 통과한 엔진으로 간주하지 않는다.** 기록: [원본 소스 + 급경사지 판정](decisions/2026-10-26_OPENLISEM_THREE_CRITERIA_SOURCE_AND_STEEP_SLOPE_AUDIT.md), [Opedes 2025](papers/2025_Opedes_OpenLISEM_MountElgon_Trenches.md), [OpenLISEM model lineage](models/OpenLISEM.md).

> **2026-10-26 긴급 정정: 고운사 유수침식 모형 채택 상태 = 미확정.** 이전 채팅에서 제안된 "SHETRAN 제외 → SWEHR이면 된다"는 결론을 명시적으로 철회한다. 원본 SWEHR 2017 공개 C에는 2016 연구논문의 Rutter 수관차단과 수관충격 차폐가 구현되었다고 입증되지 않으며, 기존 38개 사례는 임의 계수를 넣은 수정 포크일 뿐 원본 식생 모델이나 현장 결과가 아니다. SHETRAN 4.7.2의 native 강우사상 실행 성공은 고운사 세류 침식과 공간별 DEM 변화의 검증이 아니다. EUROSEM은 본질적 2D 유동 요구조건을 충족하지 않는다. Iber+는 학술 검증 연구가 있지만 연구자의 요구인 온전한 공개 소스 및 필요한 식생 결합 인터페이스가 확인되지 않아 오늘의 채택 판정을 내릴 수 없다. **유효한 단일 주 엔진이 확보되었다고 주장 금지.** 근거: [SWEHR 원본 코드 부재 확인](decisions/2026-10-26_OFFICIAL_SWEHR_V1_0_ORIGINAL_CODE_PROVENANCE.md), [SHETRAN 적합성 재검토](decisions/2026-10-26_SHETRAN_FIT_FOR_PURPOSE_REASSESSMENT.md), [Iber+ 등 기존 비교](decisions/2026-10-26_EUROSEM_SWEHR_IBERPLUS_COMPARISON.md).


업데이트: 2026-10-26

이 문서는 고운사 산불 후 식생-지형 상호작용 모델 문헌검토의 **단일 통합 요약본**이다.

세부 서지, 식, 적용환경, 한계는 `papers/`의 논문별 파일과 `models/`의 모델 계보 파일을 우선한다.
채택/탈락/새로운 coupling의 경계는 `decisions/`가 최우선 기록이다.

---

# 1. 프로젝트 목표

고운사 산불 이후 약 100년 동안 다음 과정을 함께 모의한다.

```
산불
 -> 식생 소실 및 회복
 -> 유수침식 변화
 -> 사면 토사이동
 -> shallow landslide
 -> tree throw / root bioturbation
 -> soil production / weathering
 -> fire-spall 및 coarse-fragment supply
 -> 지형 변화
 -> 다시 식생에 feedback
```

식생 동태는 LPJ-GUESS를 중심으로 하고, 지형과정에는 가능한 한 기존 published equations를 그대로 사용한다.

---

# 2. 고정 원칙

1. COPLAS는 최종모델의 식, 철학, parameterization 근거에서 제외한다.
2. MUSLE는 최종 산지 유수침식식에서 제외한다.
3. vegetation cover 하나로 모든 식생효과를 표현하지 않는다.
4. root biomass, live/dead root mass, RLD, litter biomass, PFT biomass처럼 정량 상태량을 우선한다.
5. interrill/rill 또는 rainfall-driven/flow-driven 침식을 분리한다.
6. distributed 또는 raster라는 이유만으로 D8 routing을 genuine 2D라고 부르지 않는다.
7. field regression과 실제 numerical-model implementation을 구분한다.
8. 논문에 없는 모델 간 연결은 반드시 **새로운 coupling**이라고 기록한다.
9. 유수침식 root effect와 shallow-landslide root cohesion을 같은 parameter로 합치지 않는다.
10. 이미 결정된 Wu-vs-WEPP 갈림길을 다시 열지 않는다. 둘은 역할이 다르다.

관련 결정:
- `decisions/2026-09-21_STRICT_2D_QUANTITATIVE_VEGETATION.md`
- `decisions/2026-09-21_EXCLUSIONS.md`
- `decisions/2026-09-21_COUPLING_BOUNDARY.md`
- `decisions/2026-09-21_PROCESS_ARCHITECTURE.md`

---

# 3. 가장 중요한 현재 결론

현재까지 검토된 범위에서 다음 네 조건을 **동시에** 만족하는 단일 published model은 확인되지 않았다.

```
genuine 2D
+ mountain / steep forest or postfire applicability
+ quantitative vegetation state
+ interrill/rill or rainfall/flow process separation
```

문헌은 두 계열로 분리된다.

## 3.1 genuine 2D erosion-engine 계열

| 모델 | genuine 2D | process separation | quantitative root state | 산지/산불 선례 | 현재 역할 |
|---|---:|---:|---:|---:|---|
| Wu et al. 2020 | O | interrill/rill | X | 제한적 | 2D erosion skeleton |
| PSEM_2D | O | rainfall/flow | X | 제한적 | 2D 비교엔진 |
| Iber+ 2024 | O | rainfall/flow | X | catchment scale | 핵심 현대 2D 후보 |
| McGuire 2013 | O | emergent rill | X | 실험 hillslope | rill-network benchmark |
| OpenLISEM | O/공간분포형 | splash/flow | external root cohesion, cover weighted | O, burned forest | postfire comparison |
| SERGHEI-SE | O | hydro-erosive source terms | X | catchment framework | 최신 HPC 비교엔진 |

## 3.2 quantitative vegetation -> erosion resistance 계열

| 모델 | quantitative vegetation | interrill/rill | genuine 2D | 현재 역할 |
|---|---:|---:|---:|---|
| WEPP | live/dead roots, residue | O | X | 핵심 Ki/Kr 근거 |
| Mao 2010 VIC-WEPP | roots/residue dynamic adjustment | O | X | published coupling precedent |
| Gould 2016 | WEPP-based wildfire mountain application | O | X | 산불 산지 선례 |
| DANSAT | plant/root/residue dynamics | O | X | dynamic Ki/Kr precedent |
| PROMET/Waldmann | dynamic RLD | 부분/과정별 | X | RLD -> resistance precedent |
| ELM-Erosion | PFT root biomass | rainfall/runoff | X | PFT biomass bridge |

따라서 최종 고운사 모델이 두 계열을 결합하면 그것은 **새로운 coupling**이다.

---

# 4. WEPP에서 확정된 식생-침식 연결

WEPP는 cover-only 모델이 아니다.

## 4.1 interrill erodibility

채팅과 공식 Chapter 7에서 확인한 root multipliers:

```
CKidr = exp(-0.56 * dr)
CKilr = exp(-0.56 * lr)
```

- `dr`: dead root mass
- `lr`: live root mass

이 항들은 adjusted interrill erodibility `Ki`에 들어간다.

## 4.2 rill erodibility

```
CKrbr = exp(-0.4 * br)
CKrdr = exp(-2.2 * dr)
CKrlr = exp(-3.5 * lr)
```

- `br`: buried residue mass
- `dr`: dead root mass
- `lr`: live root mass

## 4.3 주의

현재 복구에서 확정된 root effect는 `Ki`와 `Kr`이다.

```
root biomass -> tau_c
```

를 같은 방식으로 자동 확장하지 않는다. 별도 문헌근거 없이 biomass-dependent `tau_c`를 만들지 않는다.

## 4.4 vegetation pools

WEPP 공식 문서는 다음을 분리한다.

- above-ground biomass
- live root biomass
- dead root biomass
- root depth
- LAI
- canopy
- standing residue
- flat residue
- buried residue
- coarse fragments

이 구조는 LPJ-GUESS output도 가능한 한 하나의 cover로 합치지 않아야 한다는 근거가 된다.

관련:
- `models/WEPP.md`
- `papers/1995_Alberts_WEPP_Soil_Component.md`
- `papers/1995_Arnold_WEPP_Plant_Growth_Component.md`
- `papers/1995_Stott_WEPP_Residue_Component.md`
- `papers/1995_Foster_WEPP_Hillslope_Erosion_Component.md`
- `papers/2022_Lee_WEPP_Erodibility_Critical_Shear.md`

---

# 5. 2D 유수침식 엔진

## 5.1 Wu et al. 2020

Sediment continuity:

```
∂(hc)/∂t + ∂(qx c)/∂x + ∂(qy c)/∂y
= μ D_i + (1-μ) D_r
```

Interrill:
```
D_i = K_i p R I_f F_nozzle
```

Rill:
```
D_r = K_r (τ-τ_c)(1-G/T_c)
```

장점:
- genuine 2D
- explicit interrill/rill
- WEPP/Foster-style parameter interface

한계:
- root biomass/RLD module 없음
- rill location fixed in the 2020 irregular-rill paper

WEPP-derived dynamic `Ki/Kr`를 Wu에 넣으면 **새로운 coupling**이다.

## 5.2 PSEM_2D

Nord & Esteves 2005.

- genuine 2D Saint-Venant
- rainfall detachment
- runoff detachment
- deposition/redetachment
- natural nonplanar surface

식생모듈은 없다.

## 5.3 Iber+ 2024

Suspended sediment:

```
∂(h C_k)/∂t + ∂(q_x C_k)/∂x + ∂(q_y C_k)/∂y
= D_rdd,k + D_rdrd,k + D_fdd,k + D_fdrd,k + D_dep,k
```

Rainfall-driven:
```
D_rdd,k = α_d,k r (1-ε) f_d g_k
```

Flow-driven:
```
D_fdd,k = K_d,k max(τ-τ_s,0)(1-ε)g_k
```

`K_d`는 kg s^-1 N^-1이며 WEPP/Foster-style `Kr`와 차원과 구조가 매우 잘 맞는다.

그러나 WEPP root dependence를 Iber `K_d`에 넣는 것은 **새로운 coupling**이다.

Iber+의 장점:
- GPU finite volume
- genuine 2D
- multiclass sediment
- rainfall/flow separation
- loose-layer shielding
- 2D Exner topography update

현재 현대 2D engine의 핵심 비교후보이다.

---

# 6. vegetation -> erosion resistance의 published precedents

## 6.1 Mao et al. 2010

VIC + WEPP-HE coupling.

Full WEPP를 통해:
- ground cover
- live root biomass
- dead root biomass
- residue

를 erosion-parameter adjustment에 사용하는 구조가 있다.

중요한 의미:
```
dynamic vegetation/soil state
 -> erosion erodibility
```
는 이미 published coupling precedent가 존재한다.

## 6.2 Gould et al. 2016

VIC-WEPP lineage를 Salmon River Basin, northern Rockies에 적용.

따라서:
```
wildfire mountain watershed
+ WEPP-based erosion parameterization
```
의 실제 적용 선례가 있다.

## 6.3 DANSAT

Cho & Mostaghimi 2009.

- dynamic plant growth
- live/dead root states
- residues
- interrill
- rill
- channel detachment
- continuous watershed simulation

강한 vegetation-erodibility precedent이나 agricultural watershed이며 genuine 2D는 아니다.

## 6.4 PROMET/Waldmann

```
root biomass growth
 -> root length increment
 -> soil-layer allocation
 -> RLD
 -> erosion resistance
```

동적 RLD를 사용하는 실제 model implementation precedent.

Upper Danube와 alpine/mountain context는 장점이나 1 km proxel routing이며 genuine 2D는 아니다.

## 6.5 ELM-Erosion

PFT-specific topsoil root biomass를 erosion resistance에 사용한다.

LPJ-GUESS PFT/FineRootC와 개념적으로 가장 가까운 선례 중 하나이나 global/land-model scale이다.

---

# 7. 실험/리뷰에서 확인한 root effect

이 자료는 최종 numerical model 그 자체가 아니라 parameterization 검증용이다.

## Ghidey & Alberts 1997

root density/RLD와 interrill erodibility의 exponential relation을 실험으로 제시.

## Gyssels et al. 2005

공통 synthesis:

```
SEP = exp(-b RP)
```

평균 `b`:
- splash: 약 0
- interrill: RD 0.1195, RLD 0.0022
- rill: RD 0.5930, RLD 0.0460

따라서 roots의 상대적 영향은 concentrated/rill erosion에서 더 강한 경향을 보인다.

이 평균값을 그대로 고운사 모델 계수로 넣는 것은 자동 정당화되지 않는다. sensitivity/validation reference로 우선 사용한다.

---

# 8. OpenLISEM 판정

OpenLISEM source code에서 확인:

```
CohesionSoil
= COHCalibration * (Cohesion + Cover * RootCohesion)
```

`cohadd.map`은 plant-root extra cohesion input이다.

그러나:
- root cohesion is externally supplied
- cover weighting remains
- root biomass/RLD from vegetation model is not dynamically converted internally

따라서 strict quantitative-vegetation 조건을 만족하지 않는다.

장점:
- burned Mediterranean forest catchment application exists
- spatial/2D hydro-erosion framework
- postfire calibration precedent

현재 역할은 비교/검증계보이다.

---

# 9. rill network

## McGuire 2013
- genuine 2D
- rill incision/branching/merging emergent
- vegetation module 없음
- fine microtopographic scale

대표 지형식:
```
∂z/∂t = β∇²z + (D-E)/(1-φ)
```

이 `β∇²z`는 storm-time rain-splash/colluvial process이다.
Pelletier-style long-term hillslope diffusion과 동일시하지 않는다.

McGuire output을 단순 Wu rill-mask generator로 사용하는 것은 **새로운 coupling**이다.

## RillGrow
- cellular automaton
- emergent rill network
- splash, flow erosion/deposition, sidewall slumping
- multi-grain
- bare-soil/plot scale
- D8 local routing

비교계보로 유지한다.

---

# 10. 산지 distributed erosion: WiMMed / HEMINGS

강점:
- mountain/semi-arid basin applications
- raindrop erosion
- rill erosion
- gully erosion
- headcut migration
- long-term sediment transport

그러나 후반 재검증 결과:
- genuine 2D SWE가 아님
- vegetation quantity direct coupling은 충분히 확인되지 않음
- plant residue/cover representation이 남음

따라서 산지 적용성의 근거로 유지하되 strict 최종 solution은 아니다.

---

# 11. shallow landslide

유수침식 erodibility와 별도 모듈로 둔다.

권장 architecture:

```
LPJ-GUESS FineRootC
 -> root vertical distribution / architecture
 -> RAR / diameter / tensile properties
 -> root reinforcement or c_r
 -> factor of safety
 -> shallow landslide
```

Hales 2018은 biome-scale root reinforcement의 주요 근거이다.

Istanbulluoglu 계열은 postfire vegetation loss/recovery와 slope stability/sediment response를 함께 생각하는 구조적 근거이다.

중요:
```
erosion Ki/Kr root effect != shallow-landslide root cohesion
```

---

# 12. biogenic hillslope transport와 soil profile

다음 과정은 서로 합치지 않는다.

## lateral transport
- root growth/decay disturbance
- tree throw
- organismal soil displacement

관련 계보:
- Gabet
- Gabet & Mudd
- Constantine
- Doane
- Kirwan/Shugart

## vertical/profile mixing
- LORICA
- HydroLorica
- related soil-profile evolution models

vertical mixing을 lateral downslope sediment flux와 동일 diffusion coefficient로 처리하지 않는다.

## long-term landscape/soil evolution
- Pelletier 2013
- Pelak 2016
- related soil-production/weathering studies

100-year 고운사에서는 장기항의 실제 크기를 sensitivity로 확인한다.

---

# 13. postfire dry ravel

Lamb et al. 2011.

Mass balance:
```
dh/dt = -(1/w) dQ/dx + (ρ_r/ρ_s) E
```

Vegetation storage:
```
V_c = V_ci c A_b
```

핵심:
```
fire
 -> vegetation sediment-storage capacity collapse
 -> stored loose sediment release
 -> dry-ravel pulse
 -> vegetation recovery and storage recovery
```

이 과정은 fire-spall production 자체가 아니다.

---

# 14. fire spall

현재 가장 중요한 unresolved gap 중 하나.

필요한 것은:
```
fire severity / heating
 -> rock spall production
 -> coarse-fragment supply
```

Lamb dry ravel은 공급된 loose material의 이동/저장을 설명할 수 있지만 thermal spall 생산량을 계산하지 않는다.

따라서:
```
spall production module
+ dry-ravel/storage module
```
을 합치면 **새로운 coupling**이다.

---

# 15. coarse fragments / armour

고운사에서는 coarse fragments를 단순 고정 cover로만 두지 않는 방향을 유지한다.

가능 source:
- prefire gravel
- fines removal로 노출된 residual fragments
- fire-spall fragments

가능 효과:
1. mobile loose sediment supply
2. surface armour로 splash/interrill suppression

WEPP와 EUROSEM lineage에 coarse-fragment treatment 선례가 있으나 최종 상태변수식은 추가 문헌 검증 후 확정한다.

---

# 16. 현재 잠정 전체 architecture

```
LPJ-GUESS
 ├─ PFT
 ├─ AGB
 ├─ FineRootC
 ├─ dead-root state
 ├─ litter
 └─ root depth/distribution
       |
       +--> water erosion interface
       |      ├─ interrill / rainfall-driven
       |      └─ rill / flow-driven
       |               |
       |               v
       |        genuine 2D hydro-erosion engine
       |
       +--> root mechanics
       |      -> c_r / reinforcement
       |      -> shallow landslide
       |
       +--> biogenic transport
       |      -> root disturbance / tree throw
       |
       +--> soil production / weathering
       |
fire --+--> spall production [UNRESOLVED]
              |
              v
       coarse-fragment state
              |
              +--> mobile supply
              +--> armour

fire
 -> vegetation storage loss
 -> dry ravel (Lamb)
```

---

# 17. 현재 유수침식 implementation 선택 문제

이 문헌 아카이브는 아직 특정 2D engine을 최종 확정하지 않는다.

현재 주요 비교:

### Wu 2020
장점:
- explicit interrill/rill
- direct Ki/Kr interface
단점:
- fixed rill mask
- older 2D formulation

### Iber+ 2024
장점:
- modern finite volume/GPU
- rainfall/flow detachment
- multiclass + Exner
단점:
- no root state
- mapping WEPP Ki/Kr biology requires new coupling

### PSEM_2D
장점:
- clean 2D rainfall/runoff erosion
단점:
- plot/bare soil orientation

### SERGHEI-SE
장점:
- latest HPC/catchment architecture
단점:
- no quantitative root state

최종 선택은 구현 가능성, 산지 DEM resolution, computational cost, vegetation-interface defensibility를 함께 평가한 뒤 결정한다.

---

# 18. 절대 되돌아가지 않을 결론

- COPLAS를 다시 최종후보로 올리지 않는다.
- MUSLE를 최종 유수침식식으로 쓰지 않는다.
- Wu vs WEPP를 양자택일 문제로 다시 검토하지 않는다.
- OpenLISEM의 external root cohesion을 dynamic root biomass model이라고 부르지 않는다.
- WiMMed D8 routing을 genuine 2D라고 부르지 않는다.
- McGuire를 단순 rill-mask generator라고 부르지 않는다.
- field root regressions를 “완성된 erosion model”이라고 부르지 않는다.
- root effect on Ki/Kr를 tau_c에도 자동 적용하지 않는다.

---

# 19. 미해결 문제

우선순위 순:

1. fire-spall production의 정량식/수치모델
2. LPJ-GUESS FineRootC -> erosion-model root mass/RLD의 단위와 depth mapping
3. dead-root pool의 fire mortality 후 시간변화
4. litter biomass -> rainfall/interrill protection을 cover로 축약하지 않는 가장 방어적인 published interface
5. 2D engine 최종선택: Wu vs Iber+ vs SERGHEI-SE 등 구현 비교
6. coarse-fragment supply vs armour dynamics
7. shallow-landslide root architecture conversion
8. 100-year scale에서 long-term creep/weathering 항의 실제 중요도

---

# 20. 핵심 모델 계보 파일

- `models/WEPP.md`
- `models/VIC_WEPP.md`
- `models/DANSAT_ANSWERS2000.md`
- `models/Wu_2D.md`
- `models/PSEM_2D.md`
- `models/Iber.md`
- `models/OpenLISEM.md`
- `models/PROMET_DANUBIA.md`
- `models/WiMMed_HEMINGS.md`
- `models/McGuire_RillNetwork.md`
- `models/RillGrow.md`
- `models/SERGHEI_SE.md`
- `models/ELM_Erosion.md`

---

# 21. 문헌 사용 원칙

개별 manuscript/model implementation에서 수식이나 계수를 사용할 때:
1. 해당 `papers/` 파일을 확인한다.
2. original paper/technical documentation을 다시 연다.
3. units와 domain of calibration을 확인한다.
4. LPJ-GUESS variable과 의미가 동일한지 확인한다.
5. 동일하지 않으면 conversion을 별도 coupling으로 문서화한다.

이 MASTER는 방향과 판정을 보존하기 위한 통합본이지, 원 논문의 식/표를 대체하지 않는다.


---

## 2026-09-21 LPJ-GUESS biomass-geomorph 복구

이번 채팅에서 유수침식, 사면확산/biogenic transport, 풍화/soil production을 LPJ-GUESS의 동적 PFT/cohort biomass와 연결하는 문헌을 복구했다.

### 현재 확정 원칙
- COPLAS는 최종 고운사 모델 근거에서 제외한다. 비교대상으로만 보존한다.
- MUSLE는 최종 산지 유수침식식에서 제외한다.
- 단일 vegetation cover 대신 PFT/cohort별 quantitative vegetation state를 우선한다.
- root-access depth는 AB soil thickness와 동일시하지 않는다. C/Cr까지 root access를 허용한다.
- 현장실험 회귀식과 실제 수치모델을 구분한다.
- 서로 다른 published model의 결합은 모두 `새로운 coupling`으로 표시한다.

### 유수침식
핵심 모델근거:
- Saco & Moreno-de las Heras 2013: biomass -> SIBERIA erodibility의 직접 선례
- Tan et al. 2022 ELM-Erosion: PFT별 topsoil root biomass effect
- Wang et al. 2024 VED: detachment capacity와 transport capacity에 vegetation effect를 별도 적용

최신 실험근거의 방향:
- FineRootC 자체보다 RMD, RLD, RSAD, SRL, root architecture가 Dc/Kr/tau_c 설명에 더 직접적
- grass, shrub, forest 또는 fibrous/tap root를 동일 계수로 처리하지 않는다
- forest biomass 증가가 erosion resistance의 단조증가를 의미하지 않는다

### 사면확산 및 biogenic transport
현재 작업구조:
`q_hill = q_creep + q_rootgrowth + q_treethrow`

근거:
- Gabet et al. 2003: root mass, turnover, rooting-depth distribution
- Gabet & Mudd 2010: root fracture와 tree throw
- Doane et al. 2021/2023/2024: tree throw와 hillslope roughness 계보
- Adams et al. 2023: post-fire CWD sediment storage/connectivity

산불 후 dead wood는 SurfaceLitC로만 보내지 않고 CWD 상태를 별도 검토한다.

### 풍화 및 soil/regolith production
현재 작업구조:
`W_total = W_hydroclimatic + W_deep_root_chemical + W_woody_mechanical`

근거:
- Pelak et al. 2016: biomass-driven soil production의 최소모델
- Gabet & Mudd 2010: woody mechanical weathering
- REWTCrunch 2022: root biomass/exudation -> reactive weathering
- Pawlik et al. 2023/2024: living tree roots와 soil formation의 최근 현장근거
- Osorio-Leon et al. 2025: deep roots가 bedrock-vadose-zone silicate weathering을 정량적으로 강화
- Billings et al. 2025: deep root-regolith interaction의 biome-scale 근거
- Bemis et al. 2026: bare rock -> moss -> grass -> shrub -> tree succession과 Critical Zone 생성

### 최신 결정 파일
- [COPLAS/MUSLE 제외](decisions/2026-09-21_COPLAS_MUSLE_EXCLUSION.md)
- [LPJ-GUESS quantitative biomass coupling](decisions/2026-09-21_LPJGUESS_BIOMASS_COUPLING.md)
- [세 지형과정 구조](decisions/2026-09-21_THREE_PROCESS_GEOMORPH_STRUCTURE.md)

### 남은 핵심 gap
1. FineRootC -> RMD/RLD/RSAD/SRL의 PFT별 변환
2. genuine 2D 산지 flow solver와 biomass-dependent detachment 식의 최종 결합
3. WoodC/cohort mortality -> tree throw/CWD의 정량 변환
4. deep-root chemical weathering flux -> R/C/Cr mass or thickness production 변환
5. 2025 LPJ-GUESS P-weathering 논문의 정확한 서지정보 재복구


---

## 2026-09-22 fire-spall / rock-fragment armour / postfire vegetation 추가 결론

### 1. dynamic armour
coarse fragments를 고정 cover로 두지 않는다.

```
fine-soil removal
 -> buried fragments exhumed
 -> surface armour increases
 -> rill incision / sediment yield decrease
```

Rieke-Zapp et al. 2007은 concentrated flow 아래에서 이 transient armouring을 직접 관찰했다.

### 2. armour hydrology
`armour -> infiltration 감소`를 고정 규칙으로 사용하지 않는다.

Poesen et al. 1990과 Cerdà 2001에 따르면:
- surface-resting fragments는 sealing을 억제하고 infiltration을 증가시키며 runoff를 줄일 수 있다.
- embedded fragments는 infiltration을 감소시키고 runoff를 증가시킬 수 있다.

따라서 hydrological effect는 cover뿐 아니라 fragment size, embeddedness/position, fine-earth properties, sealing, antecedent moisture 및 slope의 함수로 둔다.

### 3. fragment size classes
Li et al. 2022에서 fragment size에 따라 runoff와 soil-loss response가 크게 달랐다.
따라서 armour state에는 grain-size distribution이 필요하다.

중요:
```
fragmentation != armour loss
```

작은 fragments가 제자리에 남으면 shielding과 flow resistance가 오히려 강화될 수 있다.

### 4. fire-spall -> long-term fragmentation -> removal
- Buckman et al. 2021: wildfire-induced spalling의 sandstone 현장근거
- Pala et al. 2025: thermal spalling이 existing boulders를 작게 만들어 이후 mobilization에 필요한 shear stress를 낮춤
- Shtober-Zisu & Wittenberg 2021: 산불 10년 뒤 large spalls/flakes의 breakdown 및 pulverization 관찰
- Poesen 1987: rill flow에 의한 size-dependent rock-fragment transport

따라서 권장 구조:
```
fire
 -> spall production(size)
 -> large/coarse surface fragments
 -> postfire weathering/fragmentation
 -> smaller size classes
 -> size-specific entrainment/removal
 -> armour change
```

### 5. armour와 erosion의 상충효과
hydrology와 detachment shielding을 분리한다.

```
fragment architecture
 -> hydrological modifier
 -> infiltration / runoff / rill hydraulics

fragment architecture
 -> exposed fine-soil fraction / roughness
 -> detachment and transport resistance
```

따라서 runoff가 커져도 armour가 강하면 sediment yield가 낮을 수 있다.

### 6. soil water -> vegetation
Huang et al. 2024는 rock-fragment content가 soil-water profile을 바꾸며 plant species/root traits에 따라 response가 다름을 보였다.

고운사에서는:
```
soil depth
+ fine-earth volume
+ fragment cover/size/position
+ roots/macropores
 -> soil hydraulic state
 -> soil moisture
 -> PFT establishment/growth
```
를 새로운 coupling으로 검토한다.

### 7. oak vs kudzu
현재 문헌은 `stony/poor soil -> kudzu exclusion`을 지지하지 않는다.

- Takahashi et al. 1995: fire-disturbed Mt. Rokko에서 compacted, eroded, steep soils에도 natural kudzu stands가 발달
- Hwang et al. 2011: 한국 poorly developed mountain soil의 postfire oak sprouting
- Kim et al. 2020: oak resprouts가 pre-existing stump/root resources를 이용해 초기 경쟁우위를 가짐
- Susko et al. 1999: kudzu seed establishment는 dormancy, water stress, burial depth에 민감
- Tsugawa et al. 1990: kudzu는 prostrate stem/root network에 의한 clonal expansion이 중요

따라서 초기천이 필터:
```
environmental suitability
+ prefire rootstock legacy
+ seed propagule availability
+ clonal access
+ resprouting ability
+ light competition
```

참나무와 칡을 동일한 seed-based PFT establishment로 처리하지 않는다.

### 8. 최신 결정/모델
- `models/Rock_Fragment_Armour.md`
- `decisions/2026-09-22_FIRE_SPALL_ARMOUR_HYDROLOGY.md`

### 9. 남은 핵심 gap
1. 고운사 사암에서 burn severity -> spall mass 및 initial size distribution
2. postfire sandstone의 1-100 year fragmentation rate
3. size-class별 rill/dry-ravel entrainment 및 removal parameter
4. fragment architecture -> LPJ-GUESS soil hydraulic parameter 변환
5. oak rootstock 및 kudzu propagule/clonal state의 현장 초기화


---

## 2026-09-22 매립 석력 다량 조건에서의 모델 선택

현장 전제: 고운사 토양에는 **매립된 rock fragments가 많다**.

### 자의성 최소화 원칙
고운사에서는 다음과 같은 임의 보정식을 만들지 않는다.

```
K_eff = K_fine * arbitrary_stone_factor
soil_water = soil_water * arbitrary_armour_factor
erosion = erosion * custom_armour_factor
```

대신 각 과정에 대해 기존 published model의 원식과 상태변수를 사용하고, 모델 사이에서는 동일한 물리량과 단위를 전달한다. 모델 간 연결 자체는 새로운 coupling으로 명시하되 새로운 경험계수를 만들지 않는다.

### 1. 매립 석력의 수문: GEM / Naseri 계열
**Naseri et al. 2020 General Effective Medium (GEM)**을 high embedded-stoniness의 우선 hydraulic-property model로 둔다.

입력:
- volumetric rock-fragment fraction
- fine-earth hydraulic conductivity
- rock-fragment hydraulic conductivity
- fragment shape/orientation
- matric potential

출력:
- effective hydraulic conductivity `K(h)`

장점:
- saturated/unsaturated conductivity
- permeable/impermeable fragments
- fragment interaction
- 높은 석력함량을 직접 다루는 physically based model

soil-water retention은 Naseri et al. 2023의 volume-mixing framework를 우선 검토한다.

```
theta_mix(h)
= (1-f) theta_soil(h)
+ f theta_rock(h)
```

따라서 매립 석력의 효과를 임의의 infiltration multiplier로 만들지 않는다.

### 2. 표면/부분매립 석력과 seal: EUROSEM
EUROSEM은 다음을 이미 분리한다.
- `ROC`: 토양체적 내 rock-fragment fraction
- `PAVE`: surface non-erodible/stone cover
- `ISTONE`: surface/seal 조건에 따른 infiltration effect 방향

대표 published relations:
```
B_roc = B (1 - ROC)
DET_pav = DET (1 - PAVE)
```

Ksat의 PAVE 효과는 surface seal/structural porosity 조건에 따라 증가 또는 감소식을 선택한다.

중요:
**'embedded'라는 이유만으로 infiltration 감소를 부여하지 않는다.**
surface seal, macroporosity 및 fragment position을 함께 판정한다.

EUROSEM은 stony steep hillslope 적용 선례가 있지만 plane/channel cascade이므로 genuine 2D production engine으로는 사용하지 않는다.

### 3. 2D runoff / erosion / sediment transport: Iber+ 2024
현재 production erosion engine의 우선 구조는 **Iber+ 2024**이다.

기존 구현:
- genuine 2D shallow-water finite volume
- rainfall-driven detachment
- flow-driven detachment
- multiclass sediment
- suspended load / bed load
- loose low-cohesion sediment layer
- mass-conserving class fractions
- shielding of original soil by loose layer
- size-specific transport / hiding
- 2D Exner topographic update

따라서 새 2D erosion equation이나 custom armour erosion coefficient를 만들 필요가 없다.

### 4. 현재 권장 published-model chain
```
LPJ-GUESS
       |
       | vegetation/root/litter state
       |
       +------------------------------+
                                      |
embedded rock-fragment soil           |
hydraulic properties                  |
GEM 2020 + Naseri 2023                |
       |                              |
       | K(h), theta(h), Ksat         |
       v                              v
                Iber+ 2024
       genuine 2D runoff + erosion
       multiclass sediment + shielding
                 |
                 v
      soil depth / sediment redistribution
```

surface/seal 특수효과가 필요할 때만 EUROSEM의 ROC/PAVE/ISTONE published relation을 사용한다.

### 5. 단일모델과 모듈결합의 trade-off
현재까지 확인한 범위에서:
- **EUROSEM 하나**를 쓰면 stoniness + infiltration + erosion을 한 published model 안에서 가장 많이 해결하지만 genuine 2D와 dynamic multiclass armour 조건을 잃는다.
- **Iber+ 하나**는 genuine 2D와 multiclass erosion/loose-layer shielding을 해결하지만 high embedded-stoniness의 soil hydraulic-property physics가 부족하다.
- 따라서 기존의 모든 요구를 유지하면서 자의적 경험식을 피하려면 **GEM/Naseri -> Iber+**가 가장 방어적인 published-model chain이다.

이 연결은 하나의 기존 published model이 아니므로 새로운 coupling으로 명시한다. 그러나 연결부에서 새 fitted equation을 만들지 않고 `K(h)`, `theta(h)`, `Ksat`, sediment fractions 같은 동일 물리량을 전달하는 것을 원칙으로 한다.

### 6. 후순위
- KINEROS2: ROC/PAVE 계열과 event hydrology 강점은 있으나 genuine 2D 아님
- OpenLISEM: postfire 2D 비교에는 강하지만 stoniness는 주로 surface/splash 항이며 high embedded-stone hydraulic-property model이 아님
- Ma & Shao NDPM: embedded-stone infiltration 상세검증/민감도용
- HYDRUS 2D/3D stony-soil studies: hydraulic benchmark용

### 7. 최신 관련 파일
- `models/Stony_Soil_Hydraulics_GEM.md`
- `models/EUROSEM.md`
- `models/Rock_Fragment_Armour.md`
- `models/Iber.md`
- `decisions/2026-09-22_STONY_SOIL_MODEL_SELECTION.md`

### 8. 남은 검증
1. Iber+ loose-layer/original-soil class에 fire-spall coarse classes를 넣을 수 있는 원 구현 범위 재검증
2. GEM effective hydraulic properties를 Iber+ infiltration parameter에 전달할 때 사용할 published transformation 확인
3. 고운사 sandstone fragment 자체의 `K(h)`, `theta(h)` 또는 실측
4. fire severity -> spall mass/initial size distribution의 published quantitative model


---

## 2026-09-22 dynamic armour 최종 모델 선택 보완

### 핵심 계보 발견
고운사에서 필요한 dynamic armour와 embedded rock-fragment profile을 이미 구현한 published model lineage가 확인되었다.

```
ARMOUR
 -> mARM
 -> mARM3D / mARM5D
 -> SSSPAM
```

이 계보가 기존 모델로 처리하는 과정:
- selective fine removal
- surface coarsening
- armour formation
- particle-size-specific entrainment
- parent-to-daughter weathering
- multilayer embedded PSD
- subsurface resupply
- soil-depth update
- DEM evolution

따라서 고운사에서 custom armour coefficient를 새로 만들 필요가 없다.

### event hydro-erosion과 long-term armour의 역할분담
현재 우선 구조:

```
OpenLISEM + SWATRE
 -> actual event erosion/deposition mass
 -> SSSPAM/mARM state updater
 -> surface PSD / embedded PSD / armour / soil depth / DEM
```

OpenLISEM+SWATRE:
- measured/effective theta-h-K direct input
- Richards-equation soil water
- 2D SWOF surface flow
- splash / flow detachment
- erosion/deposition

SSSPAM/mARM:
- dynamic armour
- embedded PSD
- weathering/fragmentation
- profile resupply
- long-term soil-depth/DEM evolution

### OpenLISEM 소스 검증에서 확인된 한계
- StoneFraction은 static input
- material-depth evolution switch는 현재 비활성
- dynamic armour가 production code에서 완결되지 않음
- 일부 multiclass sediment UI/initialization은 비활성/주석 상태
- root effect는 extra cohesion input
- litter effect는 interception/splash protection 중심

따라서 OpenLISEM 단독으로 100년 armour/profile feedback을 완결한다고 주장하지 않는다.

### SSSPAM 자체 침식식은 쓰지 않는 이유
SSSPAM의 fluvial erosion parameterisation은 site/laboratory calibration을 필요로 하므로 고운사에 그대로 이식하면 자의성이 남는다.

따라서 SSSPAM에서는:
- grading transition
- armour
- weathering
- profile resupply
- mass balance
- soil-depth/DEM update
를 사용하고,
actual event erosion/deposition mass는 OpenLISEM에서 받는다.

### 핵심 결정
현재 최우선 구조:
**OpenLISEM+SWATRE for event hydro-erosion + SSSPAM/mARM for long-term armour/profile evolution**

관련:
- `models/ARMOUR_mARM_SSSPAM.md`
- `decisions/2026-09-22_DYNAMIC_ARMOUR_MODEL_SELECTION.md`


---

## 2026-09-22 Iber+ ↔ SSSPAM exact mass interface 및 event-engine 변경

### 1. event erosion engine
Primary event erosion engine을 **Iber+ 2024**로 변경한다.

이유:
- genuine 2D SWE
- particle-class-specific suspended/bed load
- original-soil detachment와 loose-layer redetachment 분리
- class별 deposition
- loose-layer mass `M_s,k`의 active mass conservation
- dynamic loose-layer grading
- shielding
- Exner topographic update

OpenLISEM은 SWATRE hydrology benchmark/postfire comparison으로 유지한다.

### 2. Iber+ persistent states
Original soil:
```
g_k
D_rdd,k
D_fdd,k
```

Loose surface layer:
```
M_s,k [kg m^-2]
f_k = M_s,k/M_s
D_rdrd,k
D_fdrd,k
D_dep,k
```

### 3. long-term profile handoff
embedded soil profile에서 실제로 제거해야 하는 class-k mass:

```
E_orig,i,k
=
A_i ∫(D_rdd,i,k + D_fdd,i,k) dt
```

반면:
```
E_redet,i,k
=
A_i ∫(D_rdrd,i,k + D_fdrd,i,k) dt
```
는 이미 loose layer에 있던 material의 재이동이므로 deep profile에서 다시 제거하지 않는다.

### 4. event-end state
다음 상태를 그대로 보존한다.

```
M_s,k(end)
f_k(end)
z_b(end)
```

Iber+ relation:
```
l_d,k = M_s,k / (rho_s phi)
```

따라서 loose-layer mass-to-thickness에 custom equation을 만들지 않는다.

### 5. SSSPAM/mARM 역할
사용:
- depth-resolved embedded PSD
- vertical profile resupply
- weathering transition
- inter-event profile restructuring

사용하지 않음:
- SSSPAM 자체 calibrated fluvial erosion equation
- Iber+ event result 위에 SSSPAM erosion/deposition을 다시 계산하는 것

### 6. double counting 금지
- redetachment를 deep profile erosion으로 재계산 금지
- Iber+ Exner elevation change와 SSSPAM event elevation change 중복 금지
- Iber+ class-selective deposition 뒤 SSSPAM deposition sorting 재적용 금지
- Iber shielding 외 별도 custom armour factor 동시 적용 금지

### 7. surface-layer mismatch
Iber+ variable-thickness loose layer와 SSSPAM armour/profile layer는 동일한 정의가 아니다.

따라서:
- surface authoritative state = Iber+ `M_s,k`
- deeper authoritative profile = SSSPAM/mARM
- surface/deep exchange는 mass conservation과 기존 SSSPAM vertical-resupply rule만 사용
- fitted exchange coefficient 금지

### 8. Hairsine-Rose 계보
Iber+의 original-soil / deposited-layer 구조는:
- Hairsine & Rose 1991 rainfall detachment/deposition
- Hairsine & Rose 1992 sheet flow
- Hairsine & Rose 1992 rill flow
계보에 기반한다.

이 계보는 original cohesive soil과 deposited noncohesive layer를 분리하고, deposited layer가 original soil을 shield하는 구조를 이미 갖는다.

### 9. 자의성 없는 parameter policy
다음 값은 output fitting으로 정하지 않는다.

Iber hydrology:
- Ksat
- porosity
- initial saturation
- soil depth
- wetting-front suction

Iber erosion:
- original-soil PSD `g_k`
- initial loose-layer mass `M_s,k`
- critical shield mass `M_s,cr`
- rainfall detachability
- flow detachability `K_d,k`
- critical shear stress `tau_s`

우선순위:
1. 현장 직접 측정
2. 독립 rainfall/flume detachment experiment
3. published physically based transformation
4. 직접 측정 불가능 시 literature-constrained uncertainty range

**soil-loss 결과에 맞춘 자유 calibration은 production parameter source로 사용하지 않는다.**

### 10. 현재 production architecture
```
LPJ-GUESS
    |
    v
measured / independently constrained soil state
    |
    v
Iber+ 2024
2D runoff
multiclass detachment / redetachment
deposition / transport
dynamic loose-layer mass
event topography
    |
    | E_orig,k ; M_s,k(end) ; z_b(end)
    v
SSSPAM / mARM
embedded multilayer PSD
vertical resupply
weathering
inter-event profile evolution
    |
    v
next-event g_k / soil depth / profile state
```

관련 결정:
- `decisions/2026-09-22_IBER_SSSPAM_EVENT_PROFILE_INTERFACE.md`


---

## 2026-09-22 LiDAR vegetation-engine reassessment

사용자가 vegetation-geomorph coupling에 30 m보다 세밀한 LiDAR 지형을 사용할 수 있음을 명확히 하여 식생모델 기준을 수정했다.

### revised criterion
- LiDAR individual-tree/crown initialization
- 1-10 m 이하 공간상태와의 결합성
- 100-year succession
- seed production/dispersal/regeneration
- quantitative fine-root and litter state
- hourly/daily ecohydrology where possible
- postfire recovery
- modifiable implementation

### current provisional primary engine
**HETEROFOR + spatial helper models**

HETEROFOR current documentation confirms:
- adult tree x,y,z and crown geometry initialization
- configurable cell size for radiation/regeneration/ground vegetation
- hourly meteorology and water balance
- optional tree-level water balance
- fine-root allocation, vertical root proportion and turnover
- structural roots
- annual litter cohorts / soil-carbon dynamics
- seed-bank regeneration
- 2022 Capsis seed approach with global/local seed dispersion and seed rain
- temperate mixed-forest calibration and century-scale application

### root spatialization
**ChaMRoots (Mao et al. 2015)** is now the preferred helper from LiDAR/HETEROFOR trees to 3-D root-density fields.

```
tree x,y, DBH, species
 -> ChaMRoots
 -> RID by horizontal position, diameter class and depth
```

For shallow landslides:
```
spatial root distribution
 -> Schwarz spatial Root Bundle Model
 -> root reinforcement field
```

Do not use this landslide reinforcement as water-erosion resistance.

### litter spatialization
Use HETEROFOR tree litterfall plus LiDAR crown footprints and the Sánchez-López et al. 2023 spatial litter approach to create 1-5 m surface-litter maps.

### main HETEROFOR gaps
1. no documented native wildfire/fire-spread module in HETEROFOR 1.2
2. early postfire herb/shrub **root biomass and turnover** are not yet established as strong HETEROFOR states
3. intended stand scale is roughly 0.5-5 ha; larger-domain performance and inter-stand coupling need testing
4. Korean species/PFT parameterization required

### secondary candidates
1. **SEIB-DGVM**: retains major advantage if endogenous repeated wildfire is required; native wildfire/SPITFIRE lineage, grasses, roots and litter.
2. **SORTIE-ND 7.06**: excellent spatial tree/recruitment/substrate framework and postfire applications, but no standard dynamic root-biomass/root-water-uptake state.
3. LANDIS-II + NECN: landscape fallback, but coarse coupling relative to LiDAR/event geomorph.
4. iLand: 1-ha resource-unit ecohydrology is a scale mismatch.
5. LPJ-GM: solves migration but published local vegetation resolution is too coarse for this LiDAR objective.
6. standard LPJ-GUESS: retains good physiology but not preferred as spatial engine.

### current Gounsa-specific order
For an observed initial wildfire with fine-scale LiDAR and quantitative root/litter geomorphic coupling:

1. HETEROFOR + ChaMRoots + spatial litter helper
2. SEIB-DGVM
3. SORTIE-ND + root helper
4. LANDIS-II + NECN
5. iLand
6. LPJ-GM
7. standard LPJ-GUESS

This is not a generic ranking of forest models.

Latest decision:
- `decisions/2026-09-22_LIDAR_VEGETATION_ENGINE_SELECTION.md`


---

# 2026-10-25 신규 확인: 수관 강우 분배 → 침투/유출 → 침식의 연쇄

**신규 판정 문서:** [수관-수간유하-유출-침식 문헌 점검](decisions/2026-10-25_CANOPY_STEMFLOW_RUNOFF_EROSION_RESEARCH.md)

- **세 강우성분을 모두 계산하는 모형은 이미 존재**: EUROSEM(Morgan et al. 1998)은 직접 통과우/잎 배수/수간유하와 차단저류를 계산하여 infiltration, runoff, rainfall detachment, flow detachment와 연결함. Apip et al. (2008)도 같은 연쇄를 계승. 단, 두 연구는 SF를 유효강우로 합산하여 나무별 국지 집중의 효과가 지표 격자에서 유지되지 않으며 genuine 2D 지표유동을 구성하지 않음.
- **국지 SF → runoff 검증 선례**: Charlier et al. (2009)은 수간유하 집중 구획을 따로 두어 18개 사건 수문곡선을 검증. 단, 침식 및 자유로운 2D 없음.
- **식생 생태수문**: de Wergifosse et al. (2020)의 HETEROFOR는 canopy storage/throughfall/stemflow와 층별 토양수분 1시간 계산을 제공하지만 **지표유출을 구현하지 않음**.
- **산불 후 2D 침식**: McGuire et al. (2016)은 Rutter 기반 차단, Green-Ampt 침투, 2D shallow-water, rainfall/flow detachment 및 size-selective sediment transport를 결합했지만 **줄기별 SF 집중과 수관적하 운동에너지는 별도 구현이 확인되지 않음**. 원 연구의 산불 직후 실제 사상에서는 수관이 전소하여 interception 자체를 끄고 검증함.
- **반대 경로 중요**: Liang et al. (2009), Beven & Van Stan (2026), Di Prima et al. (2026)은 줄기 기부의 preferential infiltration을 강조. Chen et al. (2026)은 줄기열 내부 SF 공급은 크지만 inter-row 침식이 더 큰 관측을 보고. SF 증가를 항상 유출과 침식 증가로 환산하는 것은 부당함.
- **강우박리 에너지**: Li & Tian (2026)은 자유통과/튀김/적하 빗방울의 KE를 구분. 자유 TF와 적하 TF를 합산한 체적 하나만으로 rainfall detachment를 정하지 말 것.
- **미해결 결합**: 나무/초본 패치별 시간별 물수지와 위치별 TF·SF·drip KE를 2D 침투-유출-침식 엔진에 질량보존으로 전달. 이는 **새로운 coupling**이며 출판된 단일 모형 기능이라고 표기하지 않음. LPJ-GUESS 뿌리량과 침식저항의 별도 결합 문제는 종전대로 유지.


---

# 2026-10-26 실제 원본 실행 침식량 물리적 타당성 점검

최신 판정: [강우 10~50 mm/h 침식량 유효성 감사](decisions/2026-10-26_RAINFALL_EROSION_PHYSICAL_VALIDITY_AUDIT.md)

- **SWEHR 공개코드 3×51 원본 예제**: 0.25m 격자, 초기 Ks=0, a=ad=0, F=0.004. 강우 10~50 mm/h 1시간 재실행에서 격자 높이 감소 총 약 0.0191 m³ vs 높이 증가 약 0.549~0.553 m³; 10~50 강우에 사실상 같은 최대 약 100.61mm 국지 고도 감소. 지형 전처리, 초기조건, 경계유사수지 검증 불가로 **모두 결과 기각**, McGuire et al. 2016 원 논문 자체의 모델 검증 결과와 구별.
- **EUROSEM 원본 2-element test**: 10mm/h gross erosion 0, 20mm/h gross 383.9kg / net 각 1.511kg, global water balance -0.0299%; 30mm/h gross 53,224.3kg / net 합 52,987.3kg, water balance 12.8593%; 40mm/h first element만 15,305kg, water error 28.8924%; 50mm/h segfault. Gross detachment vs delivered sediment **구분 필수**. 30, 40 모두 기각, 20도 반복성 문제. 시험 경사 S=0.85, 피복 COVER=0.15는 고운사 입력값이 아님.
- **실측 비교**: Johansen et al. 2001(60mm/h burned 76kg ha^-1 per mm rainfall), Samoil et al. 2026(185mm/h 30min unburned 0.0178 / moderate burn 1.05 / high burn 5.29t/ha), Kinner & Moody 2008(20/35/50mm/h infiltration response), 한국 Shin et al. 2024(RUSLE 0.07–94.9 / SEMMA 0.24–83.6t/ha/storm **모형 예측**). 극심한 침식은 실제 가능하지만 어느 숫자도 고운사 허용범위 상한이 아님.
- **기존 HETEROFOR, Charlier, Rutter/Gash**는 interception / SF / runoff 중 일부를 산출하지만 독립적으로 erosion mass를 직접 생성하지 않음. **WEPP/OpenLISEM/Apip**은 erosion 가능한 기성 구조지만 10~50 실험은 이번에 수행하지 않음.
- **현재 결론**: 검증된 고운사 t/ha/event 숫자는 아직 없음. 본문에 임의 곡선을 넣지 않는다. source archive는 다음 수행에서 물수지, 유사수지 및 단위를 확인하는 토대로만 사용.


---

## 2026-10-26 원본 수문-침식 모형 보존시험: 검증된 결과와 한계

- [실제 원본 SWEHR 및 EUROSEM 재검증](decisions/2026-10-26_SWEHR_EUROSEM_SOURCE_CLOSURE_VERIFICATION.md). **SWEHR는 원본 예제의 강제 외부 물/토사 유입 제거, 초기 U[1]/M/SOLID/TOTM 정의 후 9/9 물수지 및 원토양-퇴적층-부유사-경계유사량 독립 수지 검증 통과**. 10~50mm/h×1h에서 단위면적당 경계유실량은 시험조건 0.0000024~0.0694 t/ha/event. **고운사 현장 예측값 아님**.
- **EUROSEM**은 불연결 2사면 및 누적우량 자료의 세 지점 수 불일치 해소 후 10~50mm/h 수문 물수지 5/5 통과(잔차 -0.0333~+0.0088%), 하지만 유사수지 독립 검증은 아직 없음. 모델이 출력한 수만~수십만kg 규모의 총박리량 및 순침식량을 고운사 연구값으로 사용 금지.
- 기존 2026-09-22 잠정 Iber+ / SSSPAM/mARM 생산 구조는 유지하며 SWEHR/EUROSEM은 실행환경 및 방정식 검증 기준으로만 사용. 고운사의 수간유하 집중 위치와 수관적하 에너지, 뿌리 우선침투에 의한 2D 침식 효과는 새 결합 및 현장 매개변수 검증이 아직 필요.
- 코드 및 raw output: [swehr-water-sediment-closure-20261026 실험 브랜치](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/swehr-water-sediment-closure-20261026/experiments/rainfall_10_50).


---

## 2026-10-26 참나무 맹아형과 억새형 원본 SWEHR/EUROSEM 전과정 민감도 결과

최신 결정: [식생구조, 침투, 유출 및 침식 원본모형 조건부 민감도 110개 실행](decisions/2026-10-26_OAK_MISCANTHUS_NATIVE_MODEL_SENSITIVITY.md).

- SWEHR 원본 방정식 유지, 가상 수관 유효강우와 다양한 원본 침투/유수박리 매개변수로 50개 실행. **50/50 물수지 및 독립 유사수지 통과**. 그러나 줄기별 SF 집중, leaf-drip KE 미구현이므로 실제 억새 대 참나무 맹아 침식 우열 주장 불가.
- EUROSEM 원본 INTERC의 수관저류, 직접 TF, leaf drip, SF를 실제 기록하며 60개 실행. **59/60 물수지 통과, 1개 SPLTEX 1 실패, 독립 유사수지 미검증**. 같은 토양조건 30 mm/h 참나무형 runoff 3.708mm, 억새형 3.491mm; 식생 구조에 따른 차이가 존재하지만 SF 위치별 공급이 합산되므로 stemflow 공간 집중이 침식에 미치는 효과는 이 모형에서 직접 검증 불가.
- 30 mm/h에서 SWEHR canopy-only export 참나무형 0.004025, 억새형 0.003784 t/ha; 가상 Ks/roughness/erodibility를 바꾸면 경향이 반전되거나 값 차가 커짐. 현장자료 없이 species ranking은 식별 불가능.
- EUROSEM 30 mm/h 원본 출력 net erosion 26~29t/ha(수관형) 수준은 독립적인 sediment closure 없는 **미검증 숫자**이며 논문의 토양유실량으로 직접 사용 금지. 범위는 고운사 사이트가 아닌 원본 사면 테스트 조건에 한정.
- 생산모형 선택 **Iber+ 중심 event erosion + SSSPAM/mARM**을 SWEHR로 바꾸는 결정이 아님. 필요한 새 결합은 공간보존적 stemflow/leaf drip forcing, 토양수분과 root macropore, 수관 및 뿌리 상태 각각이다.

산출물: [네이티브 민감도 종합 Actions](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40258842917), [소스 스크립트](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/swehr-water-sediment-closure-20261026/experiments/rainfall_10_50).


## 2026-10-26 종별 생태 특성과 PLANTH 단위 오류 정정

[식생 특성 재검증](decisions/2026-10-26_OAK_MISCANTHUS_REAUDIT.md): 참나무 맹아의 줄기와 기존 뿌리, 억새의 포기별 지하경 및 가는뿌리 차이, 생육기와 비생육기의 차이를 원문으로 재검토함. 이전 EUROSEM에 2.5m라고 입력한 PLANTH=2.5는 원래 **2.5cm**였으며 원본 input routine은 /100으로 내부 m 변환. 구 수치 중 적하 운동에너지 관련 해석 오류를 폐기함. 6개 계절별 가상 구조×강우 5강도×두 엔진을 다시 실행함. EUROSEM은 TF/drip/SF 분리하지만 SF 국지침투 공간 집중 미구현, SWEHR는 canopy interception으로 차감한 유효강우를 균일하게 공급함. 두 식생 침식 억제 우열을 현장 수치 없이 주장 금지. 수정 실행: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40261338013


## 2026-10-26 밀생 억새와 산발적인 참나무 맹아 비교의 공간구조 오류 정정

[핵심 결정: 실제 배치가 다른 두 식생을 평균피복과 균일 유효강우로 동일 취급하지 않는다](decisions/2026-10-26_DENSE_MISCANTHUS_SPARSE_OAK_SPATIAL_COMPARISON.md). 진짜 고운사 식생 대조는 밀생 Miscanthus tussock/roots/litter와 떨어진 Quercus oak stump/sprouts 사이의 **노출토양 연결성 및 runon/runaround/유사수송 경로**이다. 기존 110회+60회 native SWEHR/EUROSEM 균일사면 실험은 이 핵심 공간변수가 없었으므로 실제 두 식생의 침식량 유사성 또는 우열을 입증하지 않는다. Mayor et al. 2008 WRR DOI 10.1029/2007WR006367의 6 plot/3 catchment Flowlength 검증, Crompton et al. 2023 GRL DOI 10.1029/2022GL101801의 2D Saint-Venant runon/runaround 역학이 신규 직접근거. 비교는 UAV/TLS 기반 2D 지형과 포기/그루터기별 뿌리/낙엽/토양수리/암편 및 SF 위치를 모형입력으로 구성해야 하며 관련 통계는 10–50 mm/h 1시간마다 물수지와 유사수지를 통과해야 한다. Iber+ 주연산 모형 선택은 그대로 유지.


## 2026-10-26 고운사 밀생 억새와 산발 참나무 맹아 2D 공간형 SWEHR 38회 실험

[원본 source 기반 가상사면 물수지 및 독립 유사수지 검증](decisions/2026-10-26_SPATIAL_NATIVE_SWEHR_DENSE_MISCANTHUS_SPARSE_OAK_38RUNS.md). GitHub에서 실제 고운사 DTM/식생 분포 원자료가 확인되지 않아, 13×25 cell, dx=0.5m, 81.25m² **가상** 경사에 밀생 억새(94.77%), 산발 참나무(9.23%), 정확히 동일 면적 40%의 횡방향 식생대 및 고립 식생패치를 분리해 10~50mm/h×1h 20회 모의. 공간적 SF 재분배 10회 및 원래 수관/수리/박리 과정별 추가 8회로 총 38회 실행. **38/38 물수지와 원토양-퇴적층-부유토사-경계 유사수지 통과**. 최대 물수지 상대오차 4.15e-11, 원토양 독립 유사수지 최대 1.16e-13. 30mm/h 산발 참나무 예시 유출 21.661mm, 유사 배출 0.002291t/ha; 밀생 억새 예시 유출 10.087mm, 유사 배출 0.000543t/ha. 동일 40% 피복 50mm/h 고립 패치가 횡방향 연결형보다 유사 배출 1.410배. **이는 식생 공간배치에 따른 가능성 검증이지 고운사 실제 종별 침식량 계량 예측이 아님**. 노출/식생 격자의 Ks, 거칠기, 박리 저항과 차단저류 및 SF 분율은 가상 설정; 루트 RLD 및 litter, 암편, 수관적하 KE는 미연동. 이전의 단일 평균 COVER 비교를 현장 근거로 재사용 금지. Iber+ 본 생산 선택 유지.

실험 원본 및 영구 결과 [공간형 SWEHR branch](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/spatial-vegetation-runoff-erosion-20261026/experiments/rainfall_10_50/spatial_patch_experiments/verified_20261026), [38-run Actions](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40264757325).


## 2026-10-26 EUROSEM vs SWEHR vs Iber+

[세 모형 원본/소스/API 검증](decisions/2026-10-26_EUROSEM_SWEHR_IBERPLUS_COMPARISON.md): EUROSEM(1998)은 canopy interception/direct throughfall/leaf-drip KE/stemflow 및 ROC/PAVE/ISTONE에 강하지만 kinematic wave connected slope planes이며 DT+LD+SF가 NR로 다시 합쳐짐. SWEHR(2016)은 postfire steep hillslope TLS, 2D SWE Green-Ampt Hairsine-Rose 입경별 original/deposited detachment/redeposit에 강하고 소스 C 코드 개조 가능; 원문 Rutter canopy와 실제 공개 C 구현은 동일시 금지. Iber+(2024)는 2D SWE GPU, class-specific suspended+bedload, rainfall/flow detachment, loose-layer Ms,k, Exner, Alps headwater 20km² 사례(해당 시뮬레이션은 rainfall-driven only)에 강하여 prior Iber+ event erosion first choice 유지. 다만 개별 줄기 SF 위치, 분리된 leaf-drip KE와 root/litter RLD 및 rock spall/weathering에는 어느 원본모형도 완결되어 있지 않으며 독립 공간적 coupling이 필요. SWEHR spatial native 38/38 budget pass; EUROSEM 59/60 water budget and no independently checked sediment closure; Iber+ **현장대조 코드 실측 재현 실행 전무**, 공개 Iber+ V3.2b Windows+Linux original reproducibility binaries 존재. 서로 다른 시험환경의 침식량을 3-way model numerical verification이라고 부르지 말 것. 2D rainfall impact source와 stemflow water-only source 분리 필수.


## 2026-10-26 SWEHR 수관차단과 강우충격 저감 원문/소스 정밀 확인

[원본 논문 vs 실제 C 코드 검증](decisions/2026-10-26_SWEHR_RUTTER_CANOPY_SHIELDING_SOURCE_AUDIT.md), [model 기록](models/SWEHR.md), [McGuire 원논문 추가 해설](papers/2016_McGuire_SWEHR_Postwildfire_2D.md): **McGuire et al. (2016)은 Rutter 수관차단 §3.5 식24–26과 강우박리/재박리에 곱하는 별도 canopy splash shielding `(1−Cv)+TcCv` §3.2 식3–4를 각각 구현했지만, CSDMS 공개 단일 `SWEHR.c`에는 어느 과정도 그대로 구현되어 있지 않다.** 코드에서는 직접 원시 강우 `R=RAIN[rind]`를 지표수 `U[1]+=dtR`와 강우박리 `E1,E2∝R`에 사용한다. 소스에 기존 보호항으로는 표면 퇴적층 H, 수심의 빗방울충격 감쇠 및 Manning 수심마찰만 확인된다; `SF`는 수간유하우 아닌 friction slope. 원 논문 단기 실측 사건에서는 수관 연소로 interception을 의도적으로 제외, 식생회복 가상사면에서는 Cv0.05–0.95와 Tc0.35 등으로 민감도 분석. 원래 Rutter 1975에는 별도 stemflow 저류모형이 있지만 2016 논문의 간략형과 공개 C에는 독립 줄기기부 SF 공급이 없음. 기존 고운사 spatial 38-run branch `QA_WFACTOR`/`QA_DFACTOR`는 신규 정적 저류/강우충격 분리 입력이며 **Rutter의 동적 C(t), 배수 D(t), 계절별 수관저류 및 실제 leaf-drip KE는 미구현**. 특히 논문은 E=0 가정하므로 1시간 차단저류를 영구 수문 손실로 취급하지 않고 종료 후 배수와 수관 저장을 물수지에 계상해야 한다. 우선 원본 논문 두 분리항 복구한 후 10–50mm/h 수지 재검증. 공간 식생 피복을 뿌리와 동일시하지 말 것.


## 2026-10-26 최종 정정: 공식 SWEHR 1.0 원본 코드 별도 보존

[원본 코드 및 원논문 차이 검증](decisions/2026-10-26_OFFICIAL_SWEHR_V1_0_ORIGINAL_CODE_PROVENANCE.md): 저자 등록 CSDMS SWEHR V1.0 (2017-07 최초 커밋 4e6f783f3...) 7개 원본 파일을 `main/third_party/SWEHR_original_v1_0_2017/`에 바이트 **7/7 동일**하게 보존. 수정하지 않은 원본 C/입력 예제 GCC 컴파일 및 실행 success (GitHub Actions 40272368386). 그러나 2016 논문 원식 `Rutter C(t),D(t)` + `(1-Cv)+TcCv` canopy direct-rain shield는 공식 C 버전에 없음. 연구에 꼭 필요한 것은 **저자가 실제 논문 실험에 사용한 수관 모듈 포함 원 구현 버전**으로, 현재 공개자료에서 확보되지 않았음. 기존 38회 공간민감도 및 110/60회 가상 식생 모의는 원본 vegetation physics 재현이 아닌 modified fork 민감도임을 명시하고, 고운사 억새/참나무의 차이가 4.2배라는 결론 등 이전 정량연구 주장을 철회. 기존 모든 가상 실행을 원본 프로그램 실행 결과처럼 취급하지 않는다. [원본 7파일](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/main/third_party/SWEHR_original_v1_0_2017), [원본 무수정 컴파일 실행](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40272368386).


## 2026-10-26 SWEHR 연구결과 신뢰성 전수감사 및 공식 정정

[종합 정정 보고서](decisions/2026-10-26_SWEHR_REPRODUCIBILITY_REMEDIATION.md) 및 [결과 상태 CSV](decisions/2026-10-26_SWEHR_EVIDENCE_STATUS_MATRIX.csv): 2016년 논문에 기술한 Rutter 수관저류 §3.5와 독립 수관 강우충격 차폐 §3.2는 공식 SWEHR V1.0의 C 소스에 없음. 2017 V1.0은 바이트 동일 7/7로 보존하고 기본 예제 무수정 컴파일/실행 확인함. 본 연구가 실행한 38회 SWEHR synthetic mask 공간 실험과 기타 억새/참나무 식생 사례는 **2016 SWEHR original published vegetation model reproduction이 아니며, 4.2배 수치는 실제 종별 효과로 사용하면 안 된다**. 논문 데이터는 교신저자 요청을 통해 입수한다는 2016년 원문 안내를 확인했고, Luke A. McGuire 논문 게재 연락처 `lmcguire@email.arizona.edu`를 정정 보고서에 명시함. 원논문의 해당 코드 버전과 Figure 9/10 입력자료를 확보해 최초 상태 그대로 재현하는 것이 이전 실험 복원보다 우선임. 저자 문의는 발송하지 않은 초안이며 응답이나 코드 확보를 주장하지 않음.


## 2026-10-26 공개 원본 전체 소스 기반 후속 침식모형 재선정

[완전 공개 소스 감사](decisions/2026-10-26_FULL_OPEN_SOURCE_NATIVE_2D_VEGETATION_EROSION_MODELS.md) 및 [SHETRAN 계보](models/SHETRAN.md), [수정된 openLISEM 계보](models/OpenLISEM.md): SWEHR 공식 V1.0에서 누락된 수관차단/수관적하 충격을 실제 소스에 구현한 두 후보기술 확인. **SHETRAN** `nclwater/Shetran` GNU GPLv3 current version CMake 4.7.2.0 실제 `ETmod.f90` dynamic `CSTORE,CSTCAP,CK,CB,DRAIN,DRAINA`, `SYmod.f90` `SYWAT` 직접강우/적하 분리, `SYOVER` 빗방울+잎적하 momentum, 지표 초본 및 표면 암편 저감, flow detachment, 퇴적층의 원토양 보호, 유사 입경 7종, 2D 4방향 유동 및 완전한 `Cobres` SYD 유사 입력 예제 확보. 현재 공식 코드의 **`BALSED`가 빈 함수**이고 미세 rill 자동 발달은 Wicks & Bathurst 1996 원문에 `without rilling` 명시. Windows ifx/VS2026, Linux gfortran 및 CMake, 세 dependency tarball이 코드에 제공되지만 **현재 직접 컴파일/모델 실행/수지검증하지 않음**. **openLISEM** original GPLv3 `vjetten/openlisem` `hydro/lisInterception.cpp` actual canopy/litter, `erosion/lisErosionSplash.cpp` direct rain/leafdrip kinetic energy, stone/grass suppression, `lisSWOF2DSediment.cpp` actual dynamic 2D SWOF sediment transport source confirmed. 이전 Linux Qt6/QWT build blocked, fixed라고 주장하지 말 것. DHSVM 공식 source는 canopy 있으나 별도 Doten 2006 sediment extension 미확인, GEOtopSed github archive에는 sediment routines not found. **기능만 설명된 논문 또는 공개되지 않은 2016 SWEHR 식생 코드를 원래 있다고 하지 않음**. 1차 새 원본 실행 우선순위 SHETRAN의 Cobres 유사 시뮬레이션, 다음 openLISEM Windows native 기능 및 version/build identity 감사. 두 모델 모두 실제 현장 root biomass→erosion link, 개별목 SF, fire-spall rock weathering and explicit evolving rills에는 한계.


## 2026-10-26 SHETRAN 4.7.2 원본 Fortran 구현의 실제 호출경로 감사

[원본 source, 호출순서, 수식, 누락 기능 정밀 기록](decisions/2026-10-26_SHETRAN_472_NATIVE_IMPLEMENTATION_CALLGRAPH_AUDIT.md): 코드 2026 최신 버전 commit cf9cd540. 실제 원본에서 `run_sim: ETSIM→VSSIM→OCSIM→SYMAIN`; `SYMAIN: SYWAT→SYOVER→SYCOLM/SYLINK→SYBED`. `ETmod` 는 time-varying CSTORE,CSTCAP,CK,CB,DRAIN,PNETTO,DRAINA, `SYWAT` 는 FCC,LRAIN,DRDROP, QOC and tau, `SYOVER` 는 직접 빗방울 운동량 GMR 및 수관 적하운동량 GMD separately. 강우박리 DR은 `(1-FCG-FCROCK)`, 유수박리 DF는 `(1-FCROCK)`에 비례하므로 지표 초본 FCG는 유수박리를 직접 감소시키지 않음. DLS>=DLSMAX에서 모든 원토양 새 박리가 stepwise 0. SHETRAN 수문은 2D 4면 연결이지만 `OCmod2/OCQGRD`는 Manning-Strickler head-gradient `Q=C√(|Δz|/L)` 형태 **확산파 근사**로, 2D 완전 천수방정식 동압력/관성 해법 아님. `SYMAIN` `ZGRUND INTENT(IN)`이므로 사면 고도 업데이트, rill incision 없음. `RDF`는 수분흡수만, sediment inputs GKF/GKR keyed soil class not vegetation root RLD; 개별 수간유하우 미구현; 암편 FCROCK은 피복값이지 시간변화 풍화/파쇄 아님. 유사수지 `BALSED`는 empty stub; 원본 실제 실행/수치 검증 아직 없음. 고운사 시나리오 결과라고 주장하지 말 것.


## 2026-10-26 SHETRAN 강우사상별 DEM 갱신 입출력 완전 추적

[원본 SHETRAN HDF5, FR39, SY51–SY53 및 hotstart 제약 검증](decisions/2026-10-26_SHETRAN_INTEREVENT_DEM_UPDATE_NATIVE_OUTPUT_AUDIT.md): 본 연구는 **원본 내부에 사상별 지형갱신이 없음**을 모델 탈락사유로 삼지 않는다. original `s_v_er=GNU×86400000`[mm/day] (원토양 강우/유수 박리), `s_t_dp=DLS×1000`[mm] (표면 퇴적층 두께), `s_dis`[kg/s]가 공식 V4 HDF5에서 확인됨. `SYCOLM`은 입경별 수송, 재퇴적, DLS와 FDEL 업데이트 원형 포함. `FRmod.f90`의 과거 출력 id44는 `GNUCUM − (DLS−DLSSRT)×1000`[mm] 원형 순유실량을 계산하지만 **PREVTM과 GNUCUM 초기화 보장 없음**으로 원 출력 수치 신뢰 금지. 다음 강우의 DEM은 외부 `z[n+1]=z[n]−∫GNUdt+(DLS_end−DLS_start)`로 갱신 가능하며, 원본 terrain FR37–FR39 `ZGRUND` 입력, 유사 초기상태 SY51 DLS, SY52 FBETA, SY53 FDEL이 존재. **원본 hotstart에 FBETA/FDEL/DLS 부재**, 따라서 단순 DEM 편집으로 보존적인 완전 다사상 재시작이 된다고 주장 금지. FR39 native `10G7.0` 고정 7글자 입력은 mm 이하 갱신값 손실 위험. 원본은 바꾸지 않고 **독립 event-to-event postprocessor** `experiments/shetran_original_event_bridge.py` 및 4개 unit test를 실제 구현, GitHub Actions 통과: [CI](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40280065364). Sampled GNU 적분이므로 정확한 sediment substep-integrated native ledger를 재현한 것은 아님. 출력은 new FRD, next DEM/depth/DLS와 `restart_ready=false` 오류진단. 아직 unmodified native SHETRAN Cobres 실행 또는 실제 출력 기반 사상 연결 검증은 없음.


## 2026-10-26 SHETRAN 강우사상별 DEM 갱신 검토
- 원본 Fortran 및 공식 출력 검증: 침식 `GNU`와 표층 퇴적 `DLS`를 구분, 다음 사상 DEM에 `delta z = -sum(GNU * dt) + DLS_end-DLS_start`를 외부 신규 결합으로 전달하는 구조는 조건부 가능.
- 원본 `FRRESP` 출력 44번에 초기화/기준시각 문제가 있으므로 단독 지형갱신량으로 사용 금지. `SY51/52/53` 초기 `DLS/FBETA/FDEL`과 수문 hotstart 정합성 및 미구현 `BALSED` 외부 감사 필요.
- 상세 근거: `decisions/2026-10-26_SHETRAN_EVENT_BOUNDARY_DEM_STATE_AUDIT.md` 및 `models/SHETRAN.md`. 원본 예제 실행과 수지 검증 아직 미실시.


### 2026-10-26 SHETRAN 전체 실행경로 감사 추가
[SHETRAN 4.7.2 원본 전체 호출경로 감사](decisions/2026-10-26_SHETRAN_472_FULL_PATH_SOURCE_AUDIT.md)를 최신 상세 근거로 우선한다. 검토한 공식 Fortran: FRINIT/INFR/VSIN/ETIN/TMSTEP/OCQDQ/SYMAIN/SYCOLM/SYBED/FRRESP/HDF5/Hotstart. 확인된 필수 검증: 최초 유사계산 시간간격 누락, `GNU`의 `DLSMAX` threshold lag, 기존 output44 초기화 및 시간 재설정 오류, 외부 sediment boundary 미구현, BALSED 빈 함수, 수문 hotstart의 sediment 미포함, VS08 재생성으로 잔존 토심 소실 미표현. **SHETRAN 후보 유지, 최종채택 및 수치검증 주장 보류.**


## 2026-10-26 실제 SHETRAN 4.7.2 native 실행 (정적 검토 이후 갱신)
- [원본 SHETRAN Cobres 0,10,30,50 mm/h 강우사상 실행](decisions/2026-10-26_SHETRAN_472_NATIVE_COBRES_RAIN_QA.md)은 upstream SHA cf9cd540add78ad3accbaf62b4199d2032887f6b Fortran 4.7.2.0 실제 빌드/실행 로그에 근거. 원본 방정식과 코드 수정 없이 2 km 원본 Cobres 입력 복사에 강우 3시간, 48시간 사건으로 설정했다.
- s_v_er 최대 0,2.708,105.330,430.591 mm/day; HDF5 시계열 오른쪽 끝 적산 최대 총침식 0,0.143,15.724,29.702 mm (내부 정확 적산이 아니라 근사). 초기 DLS=30mm, HDF5 t=0=0mm 출력 오류 주의. 종료시간 48h 초과 18.9~37.9분.
- 20/40mm/h 추가 자동 native 실험은 진행 중이며, 완결 전까지 통과로 쓰지 않는다.
- **고운사 final model 채택 X**: native erosion/sediment budget, 일관된 sediment restart, VS08 잔존토심, grid-link-bank DEM event coupling은 미검증.


### 2026-10-26 원본 SHETRAN 강우 5강도 native 시험 종결
- [native QA 결정 기록](decisions/2026-10-26_SHETRAN_472_NATIVE_COBRES_RAIN_QA.md): 실제 pinned SHETRAN Fortran 4.7.2.0 빌드 및 건조, 10,20,30,40,50 mm/h 3시간 강우 + 건조 후속 실행, HDF5 sediment 기록 분석이 [CI run 40287116566](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40287116566)에서 전부 성공. 이전 문서의 '20,40 진행 중' 기록은 이 최신 판정으로 대체.
- 강우강도 10/20/30/40/50 mm/h 최대 침식률 각각 2.708/67.260/105.330/133.284/430.591 mm/day. 시간별 HDF5 근사 최대 누적 원토양 박리 각각 0.143/6.770/15.724/23.506/29.702 mm. 이는 native 내부 exact GNU 적산이 아님.
- 원본 초기 SY51 DLS 30mm인데 native HDF5 t=0 DLS=0mm로 출력되는 초기화 이전 snapshot 확인. 원본 종료시각 48h를 최종 시간이 18.90~51.73분 초과. 정확한 외부 사상 경계 연동에서 해결 필수.
- SHETRAN native 침식 계산 구동 성공과 **원본 유사질량수지 폐합, 정확한 강우사상 종료, 퇴적층 상태 전체 재시작, DEM/토심 재입력에 따른 유동 피드백 검증은 별개**. 고운사 최종 모델 확정 불가.


> **EUROSEM 2026-10-26 원본 dt 수렴 확인:** 12회 GNFortran 실제 재시험(15/30/60s)에서 합성 단일 사면 30mm/h, H1.2m 원본 수송계열의 출력 침식량은 15vs30초 Govers .272%, Everaert .228% 차이만 보이고 12회 수문 물수지 통과. OpenLISEM7.5.2와 달리 이 시험 조건에서 침식출력이 시간간격에 따라 안정적으로 수렴하는 경향. **원본 EUROSEM을 수치불안정 모델이라고 단정할 근거 없음**, 다만 원본 LAI 미구현, 1D 공간구조, 독립 유사보존 실패/미검증, 빗방울 중복분배와 박리항 단위 문제는 계속 존재. [전체 판정](decisions/2026-10-26_EUROSEM_729_LOW_VEGETATION_SENSITIVITY_ROOT_CAUSE_REAUDIT.md), [12회 Actions](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40324676949).


> **2026-10-26 EUROSEM 1998 원본 독립 유사수지 실제 검증 완료:** [결정문](decisions/2026-10-26_EUROSEM_1998_NATIVE_SEDIMENT_LEDGER_RILL_FAILURE.md) 원본 Fortran eplanel.for에는 기존에 놓쳤던 inrlbal/rillbal 내부 질량수지 항이 존재. 실제 24개 강우30/50×dt15/30/60초×세류 유무×Govers/Everaert 실행과 Q×CT 출구 유사량 독립적분 비교는 모두 성공. **세류 없는 계산만 9/12에서 유사수지 0.1% 이내**, 15초 모든 no-rill 통과. **세류 있는 원본 12/12 불합격**, 15초에서도 전체 사면 유사수지 잔차 14.32%,21.48%,16.99%,20.50%(4조건). [측방 공급 실계측](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40326648315)은 세류간 유사 배출과 세류 측방 유입 일치, 결함 범위는 세류 내부 원토양 침식/퇴적 및 미기록 저장량 또는 수지 집계로 좁혀짐. **시간간격 수렴은 유사 질량보존을 증명하지 못한다.** EUROSEM은 원본 1D이며 LAI 자체는 native가 아니므로 고운사 주 2D 침식엔진으로 탈락 유지. 식생 민감도 이전 폐기근거 오류 정정은 유지하되, 세류 대량 질량불일치를 무시한 재선정 금지.


## 2026-10-26 제출용 개발 모형/자료 구조 설계기준안 (2026-10-27 18:00 마감)
- [고운사 통합모형 및 자료 사용 설계서](decisions/2026-10-26_DEADLINE_GOUNSA_MODEL_ARCHITECTURE_AND_DATA_PLAN.md), [인계서](sessions/2026-10-26_2230_DEADLINE_ARCHITECTURE_HANDOFF.md). **검증된 현장 생산모형으로 확정한 것이 아니라 제출용 설계기준안이다.**
- 제안 신규 coupling: LPJ-GUESS PFT/cohort vegetation → published Rutter canopy storage/direct throughfall/drainage와 rain-impact shielding → 수정 SWEHR C V1.0 2D SWE + Green-Ampt + Hairsine–Rose rainfall/flow detachment + original/loose soil sediment stocks → inter-event DEM/soil/armour/weathering/hillslope flux → LPJ-GUESS feedback.
- 공식 SWEHR 공개 C에 Rutter dynamic canopy, root-linked detachability, leafdrip energy 미구현 확인; 반드시 새 코드라고 표시. 원본 7/7 보존. modified branch 9/9 + 38/38 synthetic water/sediment closure는 있음, 그러나 현장검증 및 새 Rutter coupling 수치검증은 **아직 없음**.
- 원본 Iber+는 published full 2D SWE + multiclass erosion 강점이 있지만 공개 binary와 편집가능 source가 다르고 LAI dynamic interception native 미확인. 2026-09-22 Iber+ 원형 채택 잠정안은 이번 엄격 original source 요건에서 **실제 개발 플랫폼으로는 보류**. OpenLISEM7.5.2/SHETRAN/EUROSEM 엄격 탈락 유지.
- 실측 도메인 DEM, 포기/맹아 분포, 실제 LAI/뿌리량, 깊이, rock fractions, Ksat, 고해상도 강우, 유사검증자료는 main repo에서 실파일 검증되지 않음. 기상청 AWS/ASOS 분강우, 국토정보플랫폼 DEM, 고운사 UAV/TLS, 실측토양, LPJ-GUESS 출력을 각각 구분하여 투입하고 결측을 관측으로 꾸미지 않음.
