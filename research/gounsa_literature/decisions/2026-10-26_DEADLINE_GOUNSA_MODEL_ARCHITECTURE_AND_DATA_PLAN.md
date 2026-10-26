# 고운사 2026-10-27 18:00 제출용 연구모델 구조 및 자료 활용 방안

작성: 2026-10-26 (Asia/Seoul). 상태: **설계 기준안 고정, 통합코드 및 고운사 현장 검증은 미완료**.
이 문서는 `CURRENT_MODEL_SPEC.md`를 거짓으로 확정판으로 덮어쓰지 않고, 익일 모형선정 및 자료흐름/구조 제출을 위한 구체적인 실행 설계서다. 새 결합 모델이 이미 완성되었다고 주장하지 않는다.

## 0. 결정과 검증된 범위

**개발할 모형: Gounsa Vegetation–Soil–Landscape Model (GVS-LM; 임시 작업명)**.
- 식생동태: **LPJ-GUESS**, 기존 결정 유지. PFT/cohort별 잎, 목질부, fine root, litter, 생장, 고사와 천이 담당. 실제 억새 포기 및 참나무 맹아의 공간 표현과 PFT 매개변수는 별도 공간매핑 작업으로 간주.
- 강우사상 수관수문: **Rutter형 수관저장-배수 식**을 독립 모듈로 신규 구현. 잎면적지수(LAI), 수관저장능, 직접 수관통과, 수관적하, 증발, 저장량으로 구성. 각 강우사상에 수분보존 적용; 수간유하우는 자료 없을 때 독립 변수 및 민감도 시나리오이며 임의 기본값으로 고정하지 않음.
- **2D 사상별 지표유출-침식 계산 엔진 설계기준: SWEHR 2017 CSDMS 공개 C V1.0의 2D SWE + Green–Ampt + Hairsine–Rose**. 강우박리와 흐름박리, 유사수송 및 재퇴적의 원본 엔진 기능을 원형으로 활용. 단 `SWEHR.c`에 논문의 Rutter 수관저장 및 canopy shielding이 없으므로 새 모듈로 **명시적 보완**. 2016년 논문 수관과 공개 소스를 동일 기능으로 표기 금지. 원본 외부 고정 물/유사 경계조건은 강우단독 검증 시 무효화해야 함.
- 사상 간 사면 및 토양 발달: `CURRENT_MODEL_SPEC.md`의 depth-dependent background creep + root-driven transport + dry ravel + SSSPAM/mARM 토양내 입도분포/풍화 및 표면 암편 저장량 구상 유지. 장기 profile engine의 실행 가능 여부는 미검증; 아래 결합 인터페이스는 새로 작성할 예정.
- 산불: 외부 사건, 각 식생 저장량, litter, 지표 보호, 수리전도도 변화와 기반암 fire spalling 암편 공급에 작용.
- **판정**: 본 결합은 '기존 논문에 이미 존재하는 단일 완성 모형'이 아니라 독립 공개 원본과 published equations를 결합하는 **새로운 연구모델**. SWEHR를 무수정 all-in-one 최종모델로 선전하지 않음. 고운사 관측자료를 이용한 유사량 예측 성공도 주장하지 않음.

### 왜 이 엔진인가
1. McGuire et al. (2016) JGR-ES DOI 10.1002/2016JF003867은 실제 산불 후 급경사 사면과 TLS 지형차분을 2D 물-유사 모델과 함께 분석하고 rain/flow mechanism을 분리한 **현장 근거**.
2. CSDMS SWEHR 1.0 원본 2017 C 코드 7개 파일을 `main/third_party/SWEHR_original_v1_0_2017/` 에 7/7 보존, GNU C 컴파일 및 기본사례 실행 재현.
3. 원본 C를 기반으로 외부 강제 유입 BC 및 초기조건을 명시적으로 정정한 **연구자 수정 포크**에서 9/9 native water/sediment independent closure, 38/38 synthetic spatial coupling mass closure 통과. **이는 modified fork 수지검증만** 입증, 동적 Rutter, leaf-drip KE, WEPP root, field calibration, dt/dx 수렴 및 장기 지형갱신 검증이 아님. 따라서 이 관측 범위 밖 수치 주장은 금지.
4. 경쟁 모델: OpenLISEM 7.5.2 원본 2D 12회 침식 시간간격 비수렴 및 토사재고 초과로 NO-GO; EUROSEM 원본 세류 포함 0/12 0.1% 유사수지 기준 실패 및 1D; SHETRAN 원본 canopy 실제 구현됐으나 수치 수지와 rill/DEM 피드백이 부족하고 sheet flow 성격, 강우사상별 상세 재시작 검증 미완; SWEHR는 dynamic canopy 미구현이므로 그대로 채택 불가. Iber+ 공개 실행파일과 원본 소스 공개 범위 다름, native LAI canopy 없음. SERGHEI-SE는 2D 수문-유사 공개 대조용이지만 native LAI 저장/적하 입증 없음.

**대체 선택**: SWEHR 확장 엔진이 동적 canopy 결합 후 아래 물/유사 예산 또는 공간/시간 수렴 기준에 실패하면 현장 정량결과 작성 중단. 원형 Iber+ 또는 SERGHEI-SE를 조건 없이 '검증된 대체 본엔진'이라고 전환하지 않는다. 두 모델은 독립 benchmark와 후속 개발 플랫폼으로만 남긴다.

## 1. 반드시 구현할 계산 흐름

```text
기후 (강우 분/시간, 기온, 복사, 습도, 풍속, CO2)
                  |                                 산불 사건 시각/강도
                  v                                     |
       LPJ-GUESS [일별 또는 엔진 고유 생장 step] <------+
       cohort/PFT LeafC WoodC FineRootC litter
       LAI, canopy height, woody density, root profile
                  |
       [새 공간화 인터페이스: 각격자/포기/그루터기]
                  |
       +----------+-------------------+
       |                              |
       v                              v
  Rutter dynamic interception     토양 상태 인터페이스
  LAI -> Smax, Cstore, D          H, texture, soil coarse-fragment Fg
  direct TF + leaf-drip + SF      Rs, litter, theta, Ksat, n, root/RLD
       |                              |
       +------------+-----------------+
                    v
      modified SWEHR 2D storm engine (sub-minute adaptive dt)
      rain water supply -> Green-Ampt infiltration -> 2D shallow flow
      direct raindrop energy + leafdrip energy -> splash detachment
      shear/stream-power -> flow detachment
      original soil finite stock -> deposited sediment -> transport
                    |
               per-event QA ledger
         water, original soil, deposited/suspended sediment, boundaries
                    |
                    v
        event-end delta z, H, theta, loose-layer PSD, Rs
                    |
     inter-event depth-dependent creep / roots / dry ravel
     inter-event weathering, rock spalling, armour, SOC/litter
                    |
                    v
            next DEM, soil-depth and PSD
                    |
       LPJ-GUESS soil-water capacity, root access feedback
```

원칙: LPJ-GUESS의 일별 수문과 storm 2D infiltration을 독립적으로 중복 수행하여 저장량을 이중차감하지 않는다. 한 번의 storm 물수지와 잔여 토양수분 상태를 authoritative로 넘기고, 일별 토양-식생 인터페이스를 보정식이 아닌 단위 일치 상태 전달로 정의한다. LPJ-native soil-layer state와 Green–Ampt wetting-front는 물리적으로 다른 표현이므로 단순 동등시 금지.

## 2. 계산 순서 및 식 (모형 내부와 신규 coupling 구별)

### 2.1 수관 및 지표 강우 예산 [신규 결합]
- 각 셀의 총 강우량 `P` [m]을 직접 수관통과 `P_direct`, 수관에 닿은 강우, 수관배수 `P_drip`, 수간유하우 `P_stem`, 증발량 `E_canopy`, 수관저장 증감 `ΔC`로 시간 적산하여 **P = P_direct + P_drip + P_stem + E_canopy + ΔC**; 이 식의 각 항은 **배타적인 수량 flux**로 정의한다.
- 실제 직접 적하 에너지는 물량 `P_direct`와 독립적, 수관으로부터 떨어진 `P_drip`에는 잎적하 낙하높이/입경 에너지별 계산이 추가되어야 함. 수간유하우는 지표 수량으로 공급하지만 **직접 빗방울 운동에너지로 환산하지 않음**.
- LAI에서 수관 점유, 저장능의 관계식은 Rutter 원형/선정된 published allometry로 제한하고, 억새/참나무의 LAI만 동일하면 canopy height, 저장능, drip diameter, stemflow 위치가 동일하다고 놓지 않는다.
- 겨울 낙엽 및 산불 직후 leaf C가 줄면 canopy storage/throughfall도 바뀌어야 한다. 수관/초본층 중복수관 통과에서 한 물방울을 2번 계상하지 않음.

### 2.2 강우사상 중 유수침식 [원본 SWEHR + 신규 식생 인터페이스]
- 2D 물 지배식 (참고형): `∂h/∂t + ∇·(h u) = R_ground − I` [m/s]; 수관-잔가지 저장은 source boundary에 선행 계산. original SWEHR momentum/friction/Green-Ampt 함수 보존하면서 동일 water flux를 사용.
- Hairsine–Rose 원토양과 퇴적층의 **강우박리 E_rain**과 **유수박리 E_flow**를 별도 source로 보유. 이전 포크의 일정 `QA_DFACTOR`를 동적 식생모형으로 오인하지 않음.
- WEPP의 live/dead root biomass→interrill/rill erodibility, PROMET RLD relation 등은 물리적 인자 연동의 **참고 문헌**. SWEHR의 `a,ad,J`와 WEPP의 `K_i,K_r`는 **단위와 함수구조가 달라 무조건 곱하거나 동등시 금지**. 특히 유수저항과 강우차폐, litter와 surface rocks 및 기저의 deposited-layer protection이 중복되지 않는 매핑을 별도로 명시하고 검증할 것.
- finite available soil `M_orig,k >= 0` 제약: 계산 step의 원토양 박리량 `D_orig,k A Δt`는 해당 셀 이동가능한 세토 질량 초과 불가. 암반 표면의 원토양 박리량 0. 모래/미사/점토 PSD는 <2mm 세토와 >2mm coarse-fragment를 분리.
- 입경별 보존: `M_orig,k(t+Δt) + M_loose,k(t+Δt) + M_susp,k(t+Δt) + M_export,k(t+Δt) = initial combined mass + incoming boundary mass + weathering/spall supplies`. 다른 과정에서 증가/제거된 부분은 ledger에 명시. SWEHR native Hairsine–Rose 두 입경군을 다중 입경 SSSPAM PSD와 **자동으로 동일시 금지**; 우선 2-class 실험, 변환 시험 후 확대.

### 2.3 사건 간 지형-토양 갱신 [새 결합]
- bedrock elevation `z_r` [m], mobile soil thickness `H` [m], land elevation `z_s = z_r + H + loose-layer thickness`를 명시적으로 구별한다. 토양/퇴적층 재고와 지표고도를 독립적으로 두 번 올리거나 낮추지 않는다.
- event 침식, 퇴적과 지형변화는 원토양 밀도 및 퇴적층 건조밀도/공극률에 맞추어 환산; **침식된 암편을 토성 clay/silt/sand로 즉시 치환하지 않음**.
- 사상 후 `z_s,H,Rs,theta,loose sediment`를 보존하고 다음 사건 전에 depth-dependent background creep + root-driven mass movement + dry ravel + 토양생산/풍화 + weathered fragment supply를 계산.
- background creep: `q_bg = - K H_*(1-exp(-H/H_*)) grad(z_s)` (해당 published family; `K,H_*` 단위와 의미 원문 확인). root-driven transport와 dry ravel은 동일 플럭스 두 번 계상 금지.
- fire spalling -> surface-rock storage Rs -> lateral redistribution / burial -> Fg 변화. 바로 Fg 증가로 매핑하지 않는다.
- 층별 profile PSD, weathering 관련 `SSSPAM/mARM`는 장기 profile 역할만. SWEHR의 event erosion을 별도 SSSPAM erosion으로 한 번 더 계산하지 않는다.

## 3. 입력자료 명세: 현실 자료와 없는 자료를 구분

| 자료 | 원자료 또는 출처 | 입력변수 및 단위 | 공간/시간 처리와 제한 | 상태 |
|---|---|---|---|---|
| 지면 DEM/DTM | 고운사 드론 LiDAR/TLS 우선, 국토지리정보원 공개 DEM 차선 | `z_s, z_r` m, x/y m, 경사 | 수관 높이가 포함된 DSM을 지면 DEM으로 사용 금지; 실제 수평해상도 및 정확도 확인 후 0.5–5m 실험격자 결정 | **고운사 원본 미확보** |
| 강우사상 | 기상청 AWS/ASOS **분** 관측 (data.kma.go.kr), 가능하면 현장 우량계 | `R(t)` mm/분→m/s, QC, 누적강수 | 사건 시각 및 결측처리 명시, 인접 관측소 지형 차이 민감도. CHELSA 월자료로 폭우 분별 강우 생성 금지 | **미확보** |
| 기온/복사/바람/습도 | 기상청 ASOS 및 AWS 제공 항목 | degC, W/m², m/s, % | 관측값 없는 복사는 ASOS 또는 다른 독립 제공원; 장기 기후 필요 시 CHELSA downscaling을 분별 강우와 분리 | **미확보** |
| 식생 2D 분포 | UAV 정사영상/현장 억새포기 및 참나무 맹아 위치, 산림청 임상도 보조 | PFT id, height m, canopy crown mask, stems per cell | 위성/임상도 정보로 개별 포기/그루터기 분포를 '관측'했다고 주장 금지; 고해상도 관측 없으면 시나리오 마스크 | **미확보** |
| LAI 및 식생 생물량 | 현장 LAI/LeafC/root/litter, LPJ-GUESS cohort 출력 | LAI m²/m², fine root gC/m², litter g/m², crown height m | LPJ의 LeafC를 SLA를 통해 LAI로 변환할 때 SLA PFT별 정의 필요, carbon-to-dry-mass conversion 명시 | **LAI 현장값 미확보** |
| 토심 및 암반 | 현장 토심탐침/GPR/토양단면, 배경 토양도 | H m, z_r m, cell별 soil stock kg/m² | `H >=0`, 지하 암반 깊이 독립 측정. 토심 없는 곳은 ensemble 추정, 확정 관측으로 표시 금지 | **미확보** |
| 토성/암편/입도 | 토양입도 분석 및 2mm 체분리, 표면 암편 사진과 중량 | sand/silt/clay fraction (<2mm), Fg volume frac, Rs kg/m², particle diam m | 토성≠coarse rock; surface cover≠buried coarse fragments; PSD 합계 1 | **미확보** |
| 유효 포화수리전도도 및 초기수분 | 현장 침투시험/토양수분계, 실내 보수곡선 | Ks m/s, theta_i m³/m³, psi m, n s/m^(1/3) | Green–Ampt Ks는 coarse-fragment 보정된 실측 유효치 우선; roughness 현장 상태별 | **미확보** |
| erosion 계수 | 소규모 강우모의/TLS 반복측량/수집유사량 및 사전에 선택한 peer-reviewed bounds | HR a/ad/J 및 soil/loose density | WEPP Ki/Kr 수치를 원본 SWEHR a/J 값으로 그대로 입력 금지 | **미확보** |
| 검증 | 강우 전후 TLS DEM of difference, 현장 유출량/퇴적포집, 강우계 | ∆z m, runoff m³, sediment kg | water calibration과 sediment validation을 분리; t/ha/event는 출구 배출량과 gross detachment 구분 | **미확보** |
| 장기 강제 | CHELSA 또는 연구실 기후자료 및 CO2 | 일/월 기온 및 물수지 관련 요소, CO2 ppm | 단기 2D 격자와 월/일 강제의 역할 구분, 월자료를 실제 1분 관측이라고 대체 금지 | **기존 별도 프로젝트 보유 여부 재점검 필요** |

자료 우선순위: (1) 연구대상 영역 폴리곤+DEM+관측된 식생 지도, (2) 폭우사상 분별 강우, (3) 토심/토성/석력/Ks, (4) LAI/뿌리 및 litter, (5) 유출/침식 검증 관측. **고운사 실제 data 파일의 존재와 범위는 main 저장소에서 확인되지 않았음**. 본 표는 '입력계획'이지 데이터 수집 완료 목록이 아님.

## 4. 통합 파일 사양

공간 기준: 모든 래스터의 CRS, transform, pixel centers, nodata 및 셀 면적을 통일. 시간은 ISO 8601 Asia/Seoul, 변환 후 UTC 내부 타임스탬프 및 이벤트 상대초로 함께 기록.

- `site/domain.geojson`: study polygon, catchment, outlet, areas.
- `site/dem_ground.tif`: 지면고도 m; `site/soil_depth.tif`: 토심 m; `site/bedrock_elevation.tif`: 암반고도 m (없을 때 불확실성 범위).
- `site/soil_texture_{sand,silt,clay}.tif` (<2mm): 합 1; `site/rock_{embedded_fraction,surface_mass}.tif` (각각 fraction, kg/m²).
- `site/soil_{ksat,theta_i,psi}.tif` [m/s, m³/m³, m].
- `site/vegetation_{pft,lai,height,leafC,finerootC,litter,density}.tif`: 시간/코호트 축 필요 시 NetCDF 저장.
- `forcing/storm_<event_id>.csv`: `timestamp_utc,pr_mm_interval,t_air_C,source_station_id,qc`. 단위 누적 강수량은 시간간격 길이와 함께 보존.
- `coupling/<event_id>_canopy.nc`: `storage_m, direct_m_s, drip_m_s, stem_m_s, evap_m_s, direct_ke, drip_ke`; water budget.
- `results/<event_id>_hydro_sed.nc`: h m, vx/vy m/s, original soil/loose/suspended kg/m² per class, boundary water m³ and sediment kg.
- `results/<event_id>_state_after.nc`: z, H, theta, Rs, PSD, litter, cohort state and mass ledgers.
- `qa/<event_id>.json`: original SHA and modified fork diff hash, soil capacity, CFL, timestep, dx, water mass residual, sediment residual, nonnegative checks, input hash, proof-of-observation status.

**서로 다른 자료가 없는데 모든 셀에 임의 일정값을 채우는 경우 반드시 '가상 시나리오' 배지를 명시**하고 고운사 현장 예측이라 부르지 않음.

## 5. Gate, 제출물, 불가 주장

### 우선 계산 QA
- 0 mm/h 건조: 수관배수/기저저장 반응 및 mass closure.
- 10, 20, 30, 40, 50 mm/h 강우 각 1h + 강우 중단 후 저장수 배수: canopy/net-input balance, whole-domain water/sediment independent ledgers.
- `Δt` 1/2, 1/4 및 `Δx` 1/2로 정량 output 수렴성 검증; CFL < 1만으로 안정성 증명 금지.
- 총 초기 이동가능 세토량/암편 질량 상한; 폭우 후 셀 H≥0; 초기 soil + import vs erosion+loose+susp+export closure.
- SWEHR의 원래 강제 외부 물/유사 경계조건을 제거한 case에서 외부 inflow=0 명시; otherwise ledger external flux 포함.
- infiltration/evap/soil moisture remaining 저장; canopy drip 종료 후 C reservoir 기록/다음 사건으로 carry.
- plant canopy only, litter only, roots only, Ks only, storm routing only 시험을 분리하여 식생 영향과 임의 계수 중복 확인.

### 익일 제출용으로 확정할 수 있는 것
- **모형명과 과정별 published anchor**, 원본 소스 버전, 신규 coupling의 범위, 모듈 다이어그램, 데이터 명세, 시간/공간 결합 경계, QA 기준.
- **확정할 수 없는 것**: 이 시점에 없는 고운사 관측자료의 수치, 현장 침식량, 억새 대 참나무의 실제 유출/유사비, 통합모형 실행완료 및 장기 100년 예측 정확도.
- 연구방법에는 “일부 핵심 결합부를 개발 및 검증할 계획”을 명시한다. 이미 완성되어 현장 검증된 모델이라는 표현을 금지한다.

## 6. 기존 연구 및 소스 (기록 링크)

- [현재 고운사 모델 정본](../CURRENT_MODEL_SPEC.md).
- [SWEHR C 원본 7/7와 공개기능 차이](2026-10-26_OFFICIAL_SWEHR_V1_0_ORIGINAL_CODE_PROVENANCE.md).
- [SWEHR 원문 Rutter vs 실제 C](2026-10-26_SWEHR_RUTTER_CANOPY_SHIELDING_SOURCE_AUDIT.md).
- [modified SWEHR 물/유사수지 9회](2026-10-26_SWEHR_EUROSEM_SOURCE_CLOSURE_VERIFICATION.md).
- [modified SWEHR 38회 가상공간실험 및 제한](2026-10-26_SPATIAL_NATIVE_SWEHR_DENSE_MISCANTHUS_SPARSE_OAK_38RUNS.md).
- [OpenLISEM 7.5.2 native No-Go](2026-10-26_OPENLISEM_752_NATIVE_2D_STABILITY_FAILED.md).
- [EUROSEM native rill sediment fail](2026-10-26_EUROSEM_1998_NATIVE_SEDIMENT_LEDGER_RILL_FAILURE.md).
- [SHETRAN 목적 적합성 불합격](2026-10-26_SHETRAN_FIT_FOR_PURPOSE_REASSESSMENT.md).
- [기존 Iber+ 및 SSSPAM 역할 분리](2026-09-22_IBER_SSSPAM_EVENT_PROFILE_INTERFACE.md), 이번 새 개발안은 2026-09-22의 잠정 `Iber+` 유수침식 엔진 선택을 개발시범기 기준으로 **대체 제안**하며 2026 strict full-source 판정에 의해 Iber+ 원본을 선호하지 않음.
- [McGuire et al. 2016](https://doi.org/10.1002/2016JF003867); [CSDMS SWEHR 1.0](https://doi.org/10.5281/zenodo.824087).
- [기상청 AWS 분자료](https://data.kma.go.kr/data/grnd/selectAwsRltmList.do); [ASOS 분자료](https://data.kma.go.kr/data/grnd/selectAsosRltmList.do).
- [Copernicus 300m LAI v2](https://land.copernicus.eu/en/products/vegetation/leaf-area-index-v2-0-300m): regional reference only, NOT single-stem or tussock canopy map.
