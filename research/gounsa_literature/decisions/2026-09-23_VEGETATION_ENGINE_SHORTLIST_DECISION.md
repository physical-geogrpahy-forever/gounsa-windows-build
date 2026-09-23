# 고운사 식생엔진 후보 탐색 종료 및 우선순위 결정

업데이트: 2026-09-23

## 결정
광범위한 신규 식생모델 탐색은 여기서 종료한다.

고운사 생산 식생엔진의 1순위 개발계열은 **LPJ-GUESS**로 고정한다.

정확히는 현재 존재하는 하나의 완성 branch가 아니라 다음 published branches를 우선 통합 검토한다.

```text
LPJ-GUESS SEC/PPA
+ LPJ-GUESS-RE
+ PF-LPJG style external hydrology coupling
```

필요 시 fine-catchment precedent로 LPJ-DH/LPJG-WHyMe-TFM을 참고한다.

## 이유
고운사 고정 기준은 다음과 같다.

1. 개별목보다 단순한 spatial cohort/hybrid structure
2. 명시적 하층식생과 천이
3. 토심/WHC/층별 뿌리 또는 외부 토양-지형 상태 coupling
4. 실제 유역/지형 적용 또는 측방수문 선례
5. 식생-환경 반응이 적어도 일 단위 이하

현재까지 검토한 후보 가운데 LPJ-GUESS 계열만 이 다섯 요구 각각에 대해 직접적인 published branch precedent를 모두 가진다.

### SEC/PPA
- tree age/size cohorts
- persistent canopy gaps 또는 canopy/understory layers
- full individual-tree model보다 계산적으로 가벼움
- shrub/herbaceous competition
- recruitment와 succession

### LPJ-GUESS-RE
- 15개 토층
- configurable layer thickness / total soil depth
- bedrock/aquifer boundary
- Richards equation
- subdaily adaptive vertical water solver

### PF-LPJG
- ParFlow hourly hydrology
- LPJ-GUESS daily vegetation/water exchange
- ParFlow soil-moisture state가 LPJ-GUESS soil water를 overwrite
- explicit lateral groundwater/surface-subsurface hydrology precedent

### LPJ-DH
- 약 50 m fine catchment grid precedent
- DEM-driven lateral water redistribution

## 중요한 제한
다음 조합은 아직 published single codebase가 아니다.

```text
SEC/PPA + RE + PF-LPJG + fine catchment implementation
```

따라서 이를 결합하면 반드시 **새로운 coupling/code merge**라고 기록한다.

동적 erosion/deposition으로 soil-layer thickness가 바뀔 때 다음 상태를 conservative remap하는 기능도 새로 필요하다.
- water
- soil C/N
- root biomass/fractions
- litter/interface state
- hydraulic state

## fallback 순위
### 2순위: FATES + ELM/ParFlow
장점:
- tree/shrub/grass demographic PFT
- seed bank and recruitment
- PPA canopy/understory
- fine-root and plant hydraulics
- half-hourly physiology + daily demography
- published 3-D ParFlow hillslope coupling

약점:
- 내부 disturbance patch가 x-y를 갖지 않음
- host-model stack이 무거움

### 3순위: MEDFATE + medfateland
장점:
- 실제 GIS cells
- tree/shrub cohorts
- existing herb cohorts
- daily water/carbon/growth
- seed dispersal
- lateral hydrology
- one-day restartable interface
- R/sf/terra workflow와 매우 잘 맞음

약점:
- herb seed production -> recruitment -> new herb cohorts의 완전한 demographic loop가 없음

### 4순위: JULES-RED
장점:
- tree/shrub mass cohorts
- grass -> shrub -> tree succession
- half-hourly land surface + daily vegetation update 가능
- TOPMODEL/river-routing precedent

약점:
- canopy/understory competition이 SEC/FATES보다 단순
- standard soil-layer geometry가 공간적으로 고정적

## EDYS의 역할
EDYS는 생산엔진 후보보다 **통합 ecogeomorphic architecture benchmark**로 유지한다.

강점:
- 실제 raster-cell runoff
- sediment/litter/N transport
- erosion/deposition이 soil-layer thickness와 elevation을 직접 변경
- grass/forb/shrub/tree
- seed bank/seedling/adult
- 층별 fine/coarse roots

그러나:
- woody DBH/age cohort 없음
- 수관 구조 단순
- plant/root production이 월 단위
- 현대 공개 source 부재

## 신규 모델 탐색 종료 근거
추가 후보를 찾을수록 대부분 다음 중 하나가 빠졌다.
- explicit shrub/herb succession
- cohort demography
- actual geographic terrain cells
- lateral hydrology
- <= daily vegetation response

따라서 더 많은 모델명 수집의 한계효용이 매우 낮아졌다.

## 다음 단계
신규 모델 탐색이 아니라 LPJ-GUESS 구현 감사를 진행한다.

1. SEC/PPA revision 13221의 canopy/recruitment 수정 파일 파악
2. LPJ-GUESS-RE의 soil/hydrology 수정 파일 파악
3. PF-LPJG의 framework/MPI/state-exchange 수정 파일 파악
4. 세 branch의 source overlap과 merge conflict 산정
5. 고운사 최소 교환변수 확정
   - soil water / water potential
   - soil-layer thickness / active soil depth
   - FineRootC by layer 또는 layer allocation helper
   - leaf/stem/wood biomass
   - litter
   - LAI/interception
   - cohort mortality/recruitment state
6. storm-driven erosion/deposition 이후 conservative state-remapping 설계
7. 10–50 m vegetation grid 계산비용 benchmark

## 최종 판정
**LPJ-GUESS lineage를 고운사 production vegetation engine의 1순위로 채택하고, broad model search를 종료한다.**

FATES는 강한 과학적 fallback, MEDFATE는 구현 친화적 fallback, JULES-RED는 경량 demographic fallback으로 유지한다.
