# SEIB-DGVM model lineage

## 현재 판정, 2026-09-23 수정
SEIB-DGVM은 고운사에서 **개별목 공간구조 + 동아시아 냉온대 적용 + subdaily land physics**의 강한 비교모델이지만, 현재의 엄격한 5조건에서는 최상위 후보가 아니다.

가장 큰 이유는 기준 2다.
- woody PFT의 개별목 정착, 생장, 경쟁, 사망 및 교란 후 천이는 강함
- grass layer는 존재하고 광합성/수분/탄소수지는 계산됨
- 그러나 grass/herb를 독립 종자은행→발아→정착→새 cohort로 추적하는 완전한 하층식생 demographic succession은 확인되지 않음

따라서 예전의 `provisional first-choice` 판정은 철회한다.

## 고운사 5조건
| 기준 | 판정 | 설명 |
|---|---|---|
| 1. 공간명시 cohort/개별목 | STRONG | 개별목 x-y, crown competition, establishment mesh |
| 2. 명시적 하층식생 + 천이 | WEAK-PARTIAL | grass layer는 있으나 독립 herb/shrub demographic succession이 약함 |
| 3. 토양-지형 coupling readiness | STRONG | NOAH-LSM 다층 토양수분과 식생 생리 연결. TOPMODEL 계보도 존재 |
| 4. 지형/유역 선례 | STRONG-PARTIAL | TOPMODEL/CTI 지형수분 선례는 강하지만 fine-grid genuine 2D lateral hydrology는 아님 |
| 5. <=1 day | STRONG | NOAH 30 min, 식생 생리/생장 다수 daily. establishment/mortality 등 일부 demography는 annual |

## 기본 계보
### Sato et al. 2007
- 기본 virtual forest 30 m x 30 m
- 1 m establishment mesh
- individual woody PFTs + grasses
- 개별목 위치와 crown competition
- fine-root biomass

### Sato & Ise 2012
- 여러 geographic cell을 계산
- coarse adjacent-grid establishment precedent
- 개별 virtual forest 안의 공간경쟁 유지

### Sato et al. 2023
- Hokkaido cold-temperate conifer-broadleaf mixed forest
- East Asian cold-temperate PFTs
- elevation / terrestrial wetness gradient
- drought와 excessive-soil-moisture tolerance
- catastrophic disturbance 이후 woody succession

### SEIB-DGVM-NSC / SEIB-NOAH
- root NSC / root turnover 계보
- NOAH-LSM subdaily soil heat/water physics

## 최신 공개 코드 상태
2026-09-22 공식 페이지 확인:
- public major version 3.30
- Apache License 2.0
- Fortran90
- gfortran/MinGW-w64 실행 가능
- MPI multi-grid driver 존재

## 공간 구조
v3.30 virtual forest는 정사각형 stand이며 `Max_loc`로 크기를 설정한다.
표준 설정 예에서는 100 m stand를 사용하고 woody/grass establishment 내부격자를 둔다.

강점:
- individual tree x-y
- crown diameter/depth/height
- spatial light competition
- meter-scale establishment mesh

중요한 한계:
- 내부 vegetation mesh와 hydrological mesh는 같지 않음
- 한 stand 안에서는 soil-water state가 세밀한 2 m 공간격자로 분해되지 않음

즉:
```text
fine establishment/light mesh != fine soil-water mesh
```

## 시간 구조
- NOAH-LSM land physics: 30 min
- 대부분 생리: daily
- biomass growth: daily
- litter decomposition: daily
- fire: daily
- mortality: annual
- crown movement: annual
- establishment: annual

따라서 폭우 후 수분상태에 식생 생리가 반응하는 시간해상도는 충분히 짧지만, 구조적 천이는 annual scheduling을 포함한다.

## Plant state
### Woody individuals
- leaf mass / leaf area
- crown diameter and depth
- stem/trunk biomass
- height
- sapwood/heartwood state
- fine-root biomass `mass_root`

### Roots
fine roots는 개별목 biomass로 표현되지만 explicit 3D root geometry는 아니다.

coarse-root biomass는 stem/branch 계통 biomass에 포함되는 구조이며 독립적인 coarse-root state로 쓰기 어렵다.

## Litter / dead biomass
- leaf litter
- fine-root litter
- woody debris
- grass litter
- above/belowground litter input
- daily decomposition

fire가 living vegetation과 litter/fuel을 소비할 수 있다.

## Water and soil
NOAH-LSM 계보:
- subdaily soil heat/water
- 다층 soil water
- soil temperature
- surface/subsurface runoff
- transpiration/evaporation
- snow

토양수분이 daily SEIB physiology에 feedback한다.

## 지형 coupling precedent
### Sato et al. 2020
SEIB + NOAH + TOPMODEL 계열.

```text
topographic wetness / elevation heterogeneity
 -> soil water
 -> drought / over-wet stress
 -> PFT survival and biomass
```

따라서 지형->수문->식생 coupling precedent는 존재한다.

그러나 이는 LiDAR-scale genuine 2D lateral hydrology가 아니라 subgrid/topographic redistribution parameterization이다.

### Sato et al. 2023 Hokkaido
동아시아 냉온대 혼효림에서 elevation과 terrestrial wetness gradient에 따른 woody composition과 post-disturbance succession을 모의했다.

고운사와 생물지리적 적용성 면에서는 FATES, tropical FORMIND보다 장점이 있다.

## 기준 2 재감사: 왜 강등하는가
SEIB의 grass layer가 있다는 사실만으로 `explicit understory succession`이라고 판정하면 안 된다.

현재 확인한 구조에서는 grass PFT가 토양수분과 빛에 반응해 biomass를 바꾸지만, LPJ-GUESS나 완전한 demographic model처럼 다음을 명시적으로 수행하는 구조가 확인되지 않았다.

```text
herb seed bank
 -> germination
 -> establishment
 -> new herb cohorts
 -> mortality / replacement
```

C3/C4 grass의 상대 상태가 환경에 따라 달라질 수 있어도 이것을 종별/코호트별 postfire understory succession과 동일시하지 않는다.

따라서 고운사에서 중요한

```text
산불 직후 초본
 -> 관목
 -> 교목
```

전 과정을 하층식생 demographic state로 직접 추적하려면 추가 구현이 필요하다.

## 고운사 coupling
가능한 구조:
```text
geomorph / hydrology event
 -> soil moisture / soil-layer state
 -> SEIB-NOAH physiology
 -> tree biomass / fine-root biomass / litter
```

그러나 erosion/deposition으로 soil geometry 자체가 바뀌면:
1. NOAH layer thickness/state 재설정
2. water/heat/carbon state remap
3. root distribution 재매핑
이 필요하며 이는 새로운 coupling이다.

## 장점
1. 실제 개별목 공간구조
2. 동아시아 냉온대 혼효림 적용 선례
3. 30-min land physics
4. daily physiology/growth
5. fine-root biomass
6. litter/dead biomass
7. fire
8. 지형성 수분구배 precedent
9. 공개 코드

## 핵심 한계
1. herb/shrub demographic understory succession이 약함
2. within-stand soil water가 fine vegetation mesh와 같은 해상도로 분포하지 않음
3. fine-scale lateral catchment hydrology가 native 핵심은 아님
4. explicit root geometry 없음
5. geomorphic soil-depth 변화는 새 coupling
6. Korea-specific parameterization 필요

## 현재 역할
**보조 상위 비교모델, 최종 shortlist 바로 아래.**

특히 다음의 benchmark로 가치가 있다.
- East Asian forest applicability
- individual-tree spatial competition
- subdaily soil physics
- woody post-disturbance succession

그러나 사용자가 고정한 2번 조건 때문에 현재 shortlist의 LPJ-GUESS spatial-hydrology lineage, FATES, MEDFATE보다 우선하지 않는다.

## Related papers
- `papers/2007_Sato_SEIB_DGVM.md`
- `papers/2012_Sato_Ise_SEIB_Africa_Dispersal.md`
- `papers/2020_Sato_SEIB_TOPMODEL.md`
- `papers/2023_Sato_SEIB_Hokkaido_MixedForest.md`
- `papers/2023_Ninomiya_SEIB_DGVM_NSC.md`
- `papers/2025_Sato_Sumida_SEIB_Crown.md`
- `papers/2025_Sato_Sumida_SEIB_Crown_MixedForest.md`
