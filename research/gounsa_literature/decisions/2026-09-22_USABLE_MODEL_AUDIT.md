# 고운사 기존모델 사용가능성 재감사

날짜: 2026-09-22

## 목적
새 coupling을 먼저 만들지 않고, 기존 published model 자체가 고운사 요구조건을 어디까지 충족하는지 다시 검증한다.

## 1. CAESAR-Lisflood

### 자체 구현
- reduced 2D hydrodynamics via LISFLOOD-FP
- rainfall catchment mode via TOPMODEL
- up to 9 grain-size fractions
- surface and subsurface active layers
- dynamic armouring
- erosion/deposition
- DEM evolution
- hours to millennia
- public source code

### 부족
- quantitative root biomass/RLD 없음
- litter biomass dynamics 없음
- PFT-specific vegetation 없음
- vegetation is maturity / erosion-proportion / critical-shear style
- explicit stony-soil Richards hydrology 없음

### 판정
**강한 single-engine comparator / armour-profile candidate**
하지만 고운사 전체 production model로 바로 채택하지 않음.

## 2. SSSPAM / mARM

### 자체 구현
- particle-size-resolved surface armour
- multilayer embedded PSD
- subsurface resupply
- erosion/deposition profile mass balance
- physical weathering
- soil-depth/profile evolution
- DEM evolution
- mARM5D public source code

### 부족
- fluvial erosion law 자체가 calibrated landscape-evolution relation
- rainfall vs flow detachment 분리 약함
- quantitative root biomass/RLD/litter erosion module 없음
- event-scale genuine 2D hydrodynamics 약함

### 판정
**가장 강한 existing armour/profile/weathering engine 후보**
하지만 단독 water-erosion production model로는 부족.

## 3. 현재 남겨둘 정밀검증 후보
1. CAESAR-Lisflood
2. SSSPAM/mARM
3. Iber+

이 셋을 먼저 완전히 검증한다.
OpenLISEM, PSEM_2D, SERGHEI-SE, Wu 2D, WEPP 등은 특정 기능 비교용으로 두되,
이 세 모델 검증 전에 새 coupling의 중심으로 올리지 않는다.

## 원칙
- 모델 자체 구현과 새로운 coupling을 혼동하지 않는다.
- 적용범위 밖 parameterization을 가져오지 않는다.
- 논문에 없는 vegetation/root relation을 발명하지 않는다.
- 전체 model 채택은 각 후보의 자체 기능 감사가 끝난 후에만 결정한다.


## 3. Iber+ 2024

### 자체 구현
- genuine 2D shallow-water finite-volume hydraulics
- rainfall-driven detachment
- flow-driven detachment
- loose-layer redetachment
- multiclass suspended and bed load
- class-specific deposition
- dynamic loose-layer mass and grading
- shielding
- public software/test cases

### vertical structure
```
loose layer
original soil
non-erodible rock
```

따라서 deep multilayer embedded PSD model은 아님.

### 부족
- quantitative root biomass/RLD/litter state 없음
- physical weathering 없음
- multilayer soil-profile evolution 없음
- stony-soil hydrology는 별도 검증 필요

### 판정
**가장 강한 existing event-scale 2D water-erosion engine 후보.**
하지만 전체 고운사 soil-profile/vegetation model은 아님.

## 현재 세 후보의 역할 차이

| 모델 | 가장 강한 자체기능 | 결정적 부족 |
|---|---|---|
| CAESAR-Lisflood | 2D flow + multiclass + active layers + long-term morphology | quantitative roots/litter, explicit stony-soil hydrology |
| SSSPAM/mARM | multilayer PSD + armour + weathering + soil profile | event 2D hydrodynamics, vegetation erosion state |
| Iber+ | 2D rainfall/flow erosion + multiclass loose layer | deep profile, weathering, vegetation erosion state |

### 현 단계 결론
세 모델 모두 **단독으로 고운사 전체 요구조건을 충족하지 않는다.**

따라서 다음 단계는 새 coupling 설계가 아니라:
1. CAESAR-Lisflood가 hillslope rainfall detachment와 forest/postfire vegetation을 어디까지 자체 처리하는지 추가 확인
2. SSSPAM의 fluvial equation과 spatial routing이 고운사 100년 hillslope에 그대로 쓸 수 있는지 확인
3. Iber+의 stony-soil hydrology와 forest/postfire validation 범위를 확인
후에만 전체 선택을 한다.

## 2026-09-22 결정적 약점 재검증

### CAESAR-Lisflood
공식 문서 확인 결과 hillslope `Soil erosion rate`는 USLE-type adaptation이며 suggested values가 없고 field calibration/test가 되지 않았다고 명시된다. vegetation parameterization도 주로 channel/lateral erosion 억제에 적용된다.

**판정 변경:** 고운사 hillslope water-erosion 핵심후보에서 제외. multiclass active-layer/long-term morphodynamics comparator로 유지.

### SSSPAM
2019 원문은 flow direction/contributing area를 D8로 계산한다. runoff excess와 contributing area로 Q를 계산하고, Zhang et al. flume-derived empirical transport-capacity equation을 사용한다.

**판정 유지:** armour/profile/weathering에는 매우 강함. event genuine-2D erosion engine은 아님.

### Iber+
2024 논문은 laboratory, vineyard hillslope, 20 km² French Alps mountain headwater catchment, river reach까지 적용한다.

**판정 강화:** 산지 event-scale 2D erosion 후보로 실제 적용범위가 충분히 확인됨. 단 root/litter/postfire/stony-profile module은 없음.

## 현재 후보 상태
1. **Iber+**: event-scale 2D water erosion 후보
2. **SSSPAM/mARM**: armour/profile/weathering 후보
3. **CAESAR-Lisflood**: 비교모델, 핵심 hillslope erosion 후보에서는 제외

이 상태에서도 아직 Iber+와 SSSPAM을 연결한다고 결정하지 않는다.


---

## 2026-09-22 정밀검증 추가 결과

### CAESAR-Lisflood
공식 parameter documentation:
- slope soil erosion = USLE-type adaptation
- rainfall/flow detachment 분리형 event model 아님
- vegetation = maturity / critical shear / allowed erosion proportion
- root biomass/RLD/litter/PFT 기반 아님

**판정 변경: primary hillslope water-erosion engine 후보에서 제외.**
active-layer/armour/long-term morphology comparator로 유지.

### SSSPAM
Welivitiya et al. (2019):
- flow direction/contributing area = D8
- transport capacity = Zhang et al. (2011) flume-derived empirical equation
- genuine 2D hydrodynamic event model 아님

**판정: armour/profile/weathering engine 후보로 유지, water-erosion engine으로는 제외.**

### Iber+ 2024
- 2D SWE
- rainfall-driven detachment
- runoff-driven detachment
- multiclass suspended/bed load
- class-specific mass conservation
- open software/test cases
- meso-scale catchment validation

부족:
- quantitative root/litter state
- deep multilayer embedded PSD
- physical weathering

**판정: 현재 existing event-scale water-erosion engine 중 가장 직접적인 후보.**

## 현재 역할구분
- water erosion: Iber+ 우선 검증
- armour/profile/weathering: SSSPAM/mARM 우선 검증
- long-term single-engine comparator: CAESAR-Lisflood
