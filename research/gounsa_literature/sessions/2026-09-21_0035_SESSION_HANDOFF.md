# 2026-09-21 00:35 SESSION HANDOFF

## 세션 목적
이 채팅에서 검토한 고운사 관련 문헌과 모델결정을 채팅 밖에 영구보존하기 위해 GitHub 문헌저장소로 복구했다.

저장소:
`physical-geogrpahy-forever/gounsa-windows-build`

기준경로:
`research/gounsa_literature/`

SYSTEM.md를 먼저 읽고 그 규칙에 맞춰 정리했다.

## 이번 세션에서 새로 복구한 문헌
1. Nyssen et al. (2001): 표면 석력 제거 현장실험, 석력 감소 시 soil loss 증가
2. Yoo & Mudd (2008): PDZ와 CAZ를 분리한 soil-formation framework
3. 박경, 임주훈, 이영근 (2009): 국내 대형산불지 암석 flaking과 지표지질 변화
4. Zavala et al. (2010): simulated rainfall에서 surface rock-fragment cover와 runoff, interrill erosion 관계
5. 김재환 등 (2011): 400°C와 600°C 가열에 따른 암석 물성 변화
6. Byun et al. (2015): 대관령의 CRN 기반 soil production function
7. Pawlik et al. (2016): tree-root biomechanical and biochemical weathering review
8. Shtober-Zisu et al. (2018): fire spall의 장기 ash/fine-sediment trap 기능
9. Welivitiya et al. (2019): SSSPAM 기반 soilscape-landform evolution
10. van der Meij et al. (2020): HydroLorica, 다층 soil composition과 hydrology 결합
11. Buckman et al. (2021): fire-induced rock spalling 생성량과 장기 erosion relation
12. 김만일, 추창오 (2023): 산불피해지 토층 광물학적 변화
13. van der Meij et al. (2023): ChronoLorica particle-history tracing
14. Lapides et al. (2024): LPJ-GUESS weathered-bedrock water storage
15. Pala et al. (2025): fire spall의 postfire debris-flow 이동

## 이번 세션에서 갱신한 기존 논문
- Istanbulluoglu & Bras (2005): vegetation cover fraction V와 hillslope diffusivity 관계를 고운사 식생 coupling 관점에서 갱신
- Gabet & Mudd (2010): root fracture와 tree throw를 C/Cr->AB 후보과정으로 정리
- Pelletier et al. (2013): R->C/Cr weathering front와 고운사 두 층 shielding 확장을 구분
- Quijano-Baron et al. (2022): COPLAS 정규화 문제와 최종근거 탈락을 명시

## 이번 세션에서 새로 확인한 핵심식

### Pelletier 원식
```text
P = P0 exp[-h cos(theta) / h0]
P0 = a exp(b EEMT)
```

### 고운사 R->C/Cr 제안
```text
P_R_to_C = P0(EEMT) exp[-(H_AB + H_C) cos(theta) / h0_R]
```
새로운 coupling이다.

### Istanbulluoglu & Bras vegetation cover
```text
K_d = K_b exp(-alpha V)
```

LPJ-GUESS LAI에서 V 또는 FPC를 계산해 연결하는 것은 새로운 coupling이다.

### COPLAS 정규화
```text
Rhat = ((R - Rmean) / Rstd) / 5 + 0.5
```
leaf, litter, soil carbon도 유사한 site-specific 정규화를 사용한다. 이 때문에 다른 지역으로 직접 이전하기 어렵다고 판단했다.

### fire spall 사건단위 제안
```text
Delta M_sp = rho_r A_exposed d_sp f_sp
```
Buckman의 thickness와 affected-area 개념을 고운사 mass balance로 변환한 새로운 coupling이다.

### spall reservoir 제안
```text
M_sp(t+1) = M_sp(t) + P_sp - E_sp - B_sp
```
새로운 coupling이다.

### surface armour 제안
```text
K_fine,eff = K_fine g(CF_surface),  g' < 0
```
함수형태와 계수는 미확정이다.

## 이번 세션에서 확정된 결정

### 1. COPLAS 제외
COPLAS는 고운사 최종모델 근거에서 제외한다. biomass-pool 분리라는 아이디어만 기록으로 보존한다.

### 2. MUSLE 제외 유지
SYSTEM.md의 기존 결정대로 MUSLE를 최종 산지 유수침식식으로 사용하지 않는다.

### 3. vertical profile
```text
R -> C/Cr -> AB
```
를 기준구조로 둔다.

### 4. root-accessible depth
고운사 현장관찰을 반영해
```text
Z_root > H_AB
```
를 허용한다.

### 5. coarse fraction
최소한
```text
CF_surface
CF_AB
CF_C
```
를 분리한다. 가능하면 fine/coarse mass pool 자체를 추적한다.

### 6. fire spall
기존 석력과 합치지 않고 별도 provenance의 coarse reservoir로 둔다. 생성, 이동, 잔류/armour를 분리한다.

### 7. 최종 erosion engine
이번 세션에서는 확정하지 않았다. SYSTEM.md의 기준인 genuine 2D, steep forest, quantitative vegetation state, interrill/rill 또는 rainfall/flow separation을 계속 적용한다.

## fire spall 문헌의 현재 결론

### Buckman et al. (2021)
생성 근거.
```text
E = W A / t
```
장기 평균식이므로 2025 고운사 단일사건에 직접 사용하지 않는다.

### Shtober-Zisu et al. (2018)
잔류와 trap 근거. 일부 spall이 장기간 재와 세립질 물질을 포획한다.

### Pala et al. (2025)
이동 근거. 산불 후 debris-flow deposit에서 형태적으로 spall로 판정된 암편이 1.3–36.6%. 일부는 syn-flow fragmentation일 수 있다.

### Nyssen et al. (2001), Zavala et al. (2010)
일반 surface rock-fragment armour 근거. fire-spall 자체의 실험은 아니다.

### 문헌공백
현재 확인 범위에서는 산불피해 사면에서 spall 유지와 제거를 직접 비교해 runoff와 fine-soil loss 변화를 정량화한 연구를 찾지 못했다.

## coarse fraction 핵심결론
현재 표면에 석력이 많다는 사실은 다음의 합성결과일 수 있다.
```text
prefire coarse fragments
+ exposed C/Cr
+ selective fine loss
+ fire spall addition
- coarse export
+ deposition
```

따라서 현재 20 cm 내외가 석력 위주라는 관찰만으로 산불 후 fine soil 20 cm가 전부 제거되었다고 해석하지 않는다.

## LPJ-GUESS 핵심결론
Lapides et al. (2024)을 근거로 mobile soil thickness와 root-accessible water depth를 분리한다. 상부 soil water와 C/Cr rock moisture를 분리하는 방향이 현재 기준안이다.

## 현장자료 주의
고운사 조사에서 사용된 soil depth 21.6 cm, surface gravel ratio 48%, bedrock exposure 28%는 자료의 prefire/postfire 성격이 완전히 확정되지 않았다. prefire initial condition이라고 단정하지 않는다.

## GitHub에 저장한 파일

### Papers
- papers/2001_Nyssen_RockFragmentRemoval.md
- papers/2005_Istanbulluoglu_Bras_VegetationLandscapeEvolution.md
- papers/2008_Yoo_Mudd_PDZ_CAZ.md
- papers/2009_Park_LargeWildfireSurfaceGeology.md
- papers/2010_Gabet_Mudd_RootFractureTreeThrow.md
- papers/2010_Zavala_RockFragmentCoverHydrology.md
- papers/2011_Kim_TemperatureRockPhysicalProperties.md
- papers/2013_Pelletier_Coevolution_Vegetation_Soils_Topography.md
- papers/2015_Byun_KoreanSoilProduction.md
- papers/2016_Pawlik_Roots_Rock_Regolith.md
- papers/2018_ShtoberZisu_FireSpallsAshTraps.md
- papers/2019_Welivitiya_SSSPAM_SoilscapeLandform.md
- papers/2020_vanderMeij_HydroLorica.md
- papers/2021_Buckman_FireInducedRockSpalling.md
- papers/2022_QuijanoBaron_Biomass_Pools_Erosion_COPLAS.md
- papers/2023_Kim_Choo_ForestFireSoilMineralogy.md
- papers/2023_vanderMeij_ChronoLorica.md
- papers/2024_Lapides_LPJGUESS_BedrockVadoseZone.md
- papers/2025_Pala_ThermalSpallingDebrisFlows.md

### Models
- models/COPLAS.md
- models/LORICA_HydroLorica_ChronoLorica.md
- models/LPJ_GUESS_BedrockHydrology.md

### Decisions
- decisions/2026-09-21_CURRENT_GOUNSA_ARCHITECTURE.md
- decisions/2026-09-21_SOIL_REGOLITH_COARSE_FRAGMENT_ARCHITECTURE.md
- decisions/2026-09-21_FIRE_SPALL_AND_ARMOUR_DECISION.md
- decisions/2026-09-21_COPLAS_EXCLUSION_AND_REPLACEMENT.md

### 통합파일
- MASTER.md
- INDEX.md
- sessions/2026-09-21_0035_SESSION_HANDOFF.md

## 원문 재검증 필요
- 김재환 등 (2011)의 DOI와 페이지 범위
- Byun et al. (2015)의 soil-production 식 표기와 오차를 구현 직전 원문 표에서 재확인
- Pelletier et al. (2013)의 c, d 및 사면수송 관련 exact parameter units
- Istanbulluoglu & Bras (2005)의 alpha 부호와 구현관례를 실제 코드 적용 전에 원문/코드에서 재확인
- SSSPAM 세부 weathering과 particle-transfer equation
- 고운사 coarse-fraction hydrologic pedotransfer relation

## 다음 채팅이 바로 시작할 지점
1. SYSTEM.md, MASTER.md, INDEX.md와 최신 decisions를 먼저 읽는다.
2. 최종 erosion engine 탐색은 기존 기준을 그대로 유지한다.
3. root quantitative state -> erodibility와 litter mass/cover -> flow resistance에 대해 published numerical model을 우선 탐색한다.
4. coarse fraction이 infiltration, storage, runoff에 미치는 정량관계를 산림 또는 산지 조건에서 찾는다.
5. fire spall의 entrainment와 armour 함수는 기존 sediment/coarse-fragment 문헌에서 찾되, published fire-spall equation인 것처럼 쓰지 않는다.
6. 모든 새 연결은 기존 모델 기능인지 새로운 coupling인지 반드시 표시한다.

## APA 참고문헌
전체 목록은 MASTER.md의 이번 세션 APA 참고문헌 절을 참조한다.
