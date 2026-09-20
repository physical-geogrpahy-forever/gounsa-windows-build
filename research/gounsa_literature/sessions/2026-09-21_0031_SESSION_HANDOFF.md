# 2026-09-21 00:31 세션 인계서

## 이번 세션의 범위
LPJ-GUESS의 동적 천이와 PFT/cohort별 quantitative vegetation state를 고운사의 다음 세 지형과정에 연결할 문헌을 복구했다.

1. 유수침식
2. 사면확산 및 biogenic hillslope transport
3. 풍화 및 soil/regolith production

COPLAS와 MUSLE는 최종 근거에서 제외한다.

## 먼저 확인한 저장소 규칙
- SYSTEM.md 확인
- MASTER.md 확인
- INDEX.md 확인
- papers/models/decisions/sessions 디렉터리 중복 확인

## 이 채팅에서 재확인한 핵심 논문 및 모델

### 유수침식
- Saco & Moreno-de las Heras 2013: absolute biomass density -> SIBERIA erodibility
- Tan et al. 2022 ELM-Erosion: PFT-specific topsoil root biomass effect
- De Baets 2006/2007: RD/RLD와 concentrated-flow detachment
- Burylo et al. 2012: tree와 herb root-trait 차이
- Ma et al. 2022: herb, shrub, tree를 포함한 root-soil detachment modeling
- Ma et al. 2023: grassland와 shrubland root effect
- Wang et al. 2023: grass-shrub mixed plots
- Wang et al. 2024 VED: woodland/grassland/farmland vegetation effect
- Liu et al. 2024: restoration age, RSAD와 detachment
- Zeng et al. 2024: grass/shrub/forest의 Dc, Kr, tau_c 차이
- Zhou et al. 2024: aboveground vs belowground pathway 분리
- Wang et al. 2025: seasonal tap/fibrous-root Kr와 tau_c
- Wang et al. 2026: comprehensive root parameter, diverse land-use detachment
- Zhang et al. 2026: root architecture -> pore network -> runoff/infiltration/erosion
- Yao et al. 2026: stem-leaf vs root contribution 분리

### 사면확산 및 biogenic transport
- Gabet et al. 2003: root mass, turnover, root-depth distribution -> root-growth transport
- Roering et al. 2004: grass/shrub -> forest 전환에 따른 transport efficiency 변화
- Gabet & Mudd 2010: root fracture + tree throw
- Kirwan & Shugart 2008: forest succession + tree throw
- Constantine et al. 2012: tree-size distribution + windthrow sediment flux
- Doane et al. 2021/2023/2024: tree throw, extreme winds, roughness/creep competition
- Adams et al. 2023: fire-produced CWD의 sediment storage/connectivity
- Greenwood et al. 2021: fresh tree-throw displaced sediment
- Godziek & Pawlik 2023: pit-mound automatic detection
- Pawlik et al. 2024: pit/mound soil-hydrology legacy
- Pawlik et al. 2026 및 Šamonil et al. 2026: tree mortality/uprooting와 soil transport

### 풍화 및 soil production
- Pelak et al. 2016: biomass-driven soil production
- Gabet & Mudd 2010: woody mechanical weathering
- Taylor et al. 2012: DGVM NPP/PFT -> process-based chemical weathering
- REWTCrunch 2022: root biomass/exudation -> reactive mineral weathering
- Pawlik et al. 2023/2024: living tree roots의 sandstone/granite bioweathering
- Gurung et al. 2024 SCION-FLORA: dynamic NPP -> biotic weathering enhancement
- Zuo et al. 2024: vegetation erosion shielding이 fresh-mineral supply를 줄일 수 있음
- Billings et al. 2025: deep root-regolith interaction
- Osorio-Leon et al. 2025: deep rhizosphere가 BVZ weathering solute flux의 약 43 ± 3%, chemical weathering 약 1.8 ± 0.1배
- Crutchfield-Peters et al. 2025: deep weathered-bedrock rhizosphere의 C/N dynamics
- Chaibva et al. 2025: parent material penetration root traits systematic review
- Geyman et al. 2025: rock strength가 soil production potential의 핵심 제약
- Bemis et al. 2026: bare rock -> moss -> grass -> shrub -> tree succession과 Critical Zone 생성

## 새로 확인한 핵심 식/구조

### Saco 2013
qs = beta q^m S^n
beta는 plant biomass density가 증가하면서 감소하고 minimum erodibility를 둔다.

### Gabet 2003
q_sx = x r tau / rho_r
root mass, turnover, root-depth distribution을 이용하는 biogenic transport 구조.

### SCION-FLORA 2024
현재 채팅에서 복구:
f_biota = 0.0005 * NPP + f_minbiota * RCO2^r
f_minbiota = 0.32

### Osorio-Leon 2025
deep-root activity가 bedrock vadose-zone chemical weathering에 큰 기여를 한다는 정량제약.

## 이번 세션에서 확정한 결정
- 단일 vegetation cover를 고운사 기본 식생상태로 사용하지 않는다.
- LPJ-GUESS PFT/cohort별 LeafC, FineRootC, WoodC, NPP 및 가능한 구조변수를 보존한다.
- COPLAS는 최종모델 근거에서 제외한다.
- MUSLE는 최종 산지 유수침식식에서 제외한다.
- 사면수송은 q_creep + q_rootgrowth + q_treethrow로 분해하는 방향을 우선한다.
- 산불 후 dead wood는 litter로만 보내지 않고 CWD sediment-storage/connectivity pool을 검토한다.
- 풍화는 hydroclimatic + deep-root chemical + woody mechanical로 분해한다.
- 논문 간 결합은 모두 새로운 coupling으로 명시한다.

## 이번 세션에서 새로 만든 papers 파일
- 2023_Adams_FireCWD_SedimentStorage.md
- 2023_Doane_HillslopeRoughnessExtremeWinds.md
- 2024_Doane_TopographicRoughnessEmergent.md
- 2023_Pawlik_SandstoneRootsSoilProduction.md
- 2024_Pawlik_GraniteBioweatheringSoilFormation.md
- 2024_Gurung_SCION_FLORA.md
- 2024_Zuo_VegetationErosionWeathering.md
- 2025_Billings_DeepRootsRegolith.md
- 2025_OsorioLeon_DeepRootsSilicateWeathering.md
- 2025_CrutchfieldPeters_DeepRhizosphere.md
- 2024_Zhou_NaturalSuccessionRunoffErosion.md
- 2025_Zhou_SedimentSourceSinkSuccession.md
- 2024_Zeng_PlantCommunitiesErosionResistance.md
- 2024_Parhizkar_RootsRillShallowInstability.md
- 2024_Parhizkar_TreeShrubSedimentDetachment.md
- 2024_Dahanayake_EcoEvidencePlantsReduceErosion.md
- 2026_Yao_StemLeafRootContribution.md
- 2026_Pawlik_ForestBiogeomorphicDisturbances.md
- 2021_Greenwood_TreeThrowSedimentGeneration.md
- 2023_Godziek_PitMoundDetection.md
- 2024_Pawlik_PitMoundSoilHydrology.md
- 2026_Samonil_TreeMortalityErosion.md
- 2025_LPJGUESS_PWeathering_CitationUnrecovered.md

## 이번 세션에서 만든 models 파일
- COPLAS.md
- VED.md
- REWTCrunch.md
- SCION_FLORA.md
- Doane_TreeThrow_Roughness.md
- LPJ_GUESS_Weathering.md

## 이번 세션에서 만든 decisions 파일
- 2026-09-21_COPLAS_MUSLE_EXCLUSION.md
- 2026-09-21_LPJGUESS_BIOMASS_COUPLING.md
- 2026-09-21_THREE_PROCESS_GEOMORPH_STRUCTURE.md

## 이미 저장되어 있어 중복 생성하지 않은 주요 논문
Saco 2013, Gabet 2003, Istanbulluoglu 2004/2005, De Baets 2006/2007, Gabet & Mudd 2010, Burylo 2012, Taylor 2012, Pelak 2016, HydroLorica 2020, Hao 2020, Liu 2020, Ding 2020, Doane 2021, Parhizkar 2021, Ma 2022, Wang 2022, COPLAS 2022, REWTCrunch 2022, ELM-Erosion 2022, Ma 2023, Wang 2023, Wang VED 2024, Liu 2024, Chen 2024, Wang 2025/2026, Bemis 2026, Zhang 2026 등.

## 미복구 또는 원문 재검증 필요
- 2025 LPJ-GUESS phosphorus-weathering 논문의 정확한 저자/제목/DOI
- 일부 2024 CATENA land-use detachment 논문의 정확한 저자목록
- 2025 Geoderma grass-stem overland-flow 논문의 정확한 서지정보
- 2026 Environmental Earth Sciences stem-cover velocity 연구의 정확한 서지정보
- Pelak 2016의 원문 식번호 및 정확한 parameter units
- 일부 최근 연구의 세부 회귀계수와 단위

## 다음 채팅 시작점
1. FineRootC -> RMD/RLD/RSAD/SRL 변환을 PFT별 root traits로 구체화
2. genuine 2D 산지 flow solver와 biomass-dependent Dc/Kr/tau_c 연결식 비교
3. WoodC/cohort mortality -> tree throw + CWD pool 정량화
4. deep-root chemical weathering flux를 R/C/Cr mass balance로 변환
5. 1980-2000 문헌 재검색은 이미 별도 archive에 1980-1989 및 1990-1999 audit 파일이 존재하므로 먼저 해당 파일을 읽고 중복 없이 보강
