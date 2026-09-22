# ARMOUR / mARM / SSSPAM lineage

## 고운사에서 검토한 이유
고운사에서 다음 과정을 임의의 scalar armour factor 없이 기존 published model로 계산하기 위해 검토한다.

```
fine-soil selective erosion
 -> surface coarsening
 -> armour development
 -> particle-size-dependent entrainment
 -> weathering/fragmentation
 -> profile resupply
 -> soil-depth / DEM change
```

## 계보
1. Willgoose & Sharmeen 2006: ARMOUR
2. Sharmeen & Willgoose 2006: armour-weathering interaction
3. Sharmeen & Willgoose 2007: 100-200 yr long-term armour
4. Cohen et al. 2009: mARM state-space formulation
5. Cohen et al. 2010: mARM3D multilayer soil profile
6. Cohen et al. 2015: mARM5D lateral transport/weathering extension
7. Welivitiya et al. 2019: SSSPAM coupled soilscape-landform evolution
8. Welivitiya & Hancock 2022: gully-scale calibration/validation
9. Welivitiya & Hancock 2023: natural-catchment scale evaluation
10. Welivitiya & Hancock 2024: physical-weathering parameter estimation

## ARMOUR
핵심 상태는 particle-size distribution과 surface armour이다.

- 여러 size classes를 동시 추적
- selective entrainment
- hiding/armouring
- erosion/deposition
- event-to-event surface grading evolution

핵심 의미:
```
fine fraction preferential removal
 -> surface coarse enrichment
 -> sediment supply limitation
 -> armour-controlled erosion
```

## armour-weathering extension
Sharmeen & Willgoose 2006은 weathering을 parent-to-daughter particle transition으로 처리한다.

중요:
```
fragmentation != automatic armour loss
```

결과는 daughter-size distribution과 transport capacity에 따라 달라진다.

## mARM
surface grading vector를 state vector로 둔다.

```
g_(t+1) = A g_t
```

여기서 A는 erosion/weathering process에 따른 transition operator이다.

장점:
- mass-conserving size-class transition
- long-term repeated-event calculation
- scalar armour coefficient가 필요 없음

## mARM3D
각 spatial pixel에:
- surface armour layer
- multiple subsurface layers
- multiple particle-size classes
를 둔다.

따라서 고운사의 **매립 석력**을 단순 volumetric scalar가 아니라 depth-resolved PSD로 추적할 수 있다.

과정:
```
surface erosion
 -> surface layer mass deficit
 -> subsurface material resupply
 -> profile grading change
 -> soil depth change
```

weathering도 각 layer에서 size-class transition matrix로 계산된다.

## mARM5D
mARM3D에:
- lateral fluvial transport
- diffusive/creep transport
- aeolian input
- weathering
을 확장한다.

CSDMS 공개 코드:
`csdms-contrib/marm5d/5D_mARM5.6.F90`

소스에서 확인된 주요 상태:
- SurfaceGrad
- ProfileGrading
- WeatheringTrans
- ErosionGrad
- LayerWeatheringM
- TotalErosion
- Depth

## SSSPAM
mARM 계보를 coupled soilscape-landform evolution으로 확장한다.

상태:
- evolving DEM
- surface PSD
- sediment-load PSD
- multilayer soil profile
- soil depth
- armour layer
- weathering

실제 erosion mass `E_a`를 받아 surface grading과 erosion transition matrix를 통해 size-class-specific eroded mass vector로 변환한다.

erosion depth:
```
Delta h_E = E_a / (R_x R_y rho_s)
```

즉 외부 erosion physics가 계산한 **실제 erosion mass**를 SSSPAM의 armour/profile updater에 전달하는 인터페이스가 매우 명확하다.

## 자의성 관점
SSSPAM 전체 fluvial erosion equation을 고운사에 그대로 쓰는 것은 권장하지 않는다.

이유:
- original erosion formulation은 site/laboratory calibration parameters를 사용
- mine-spoil datasets 기반 calibration이 있음
- 고운사에서 같은 parameters를 가져오면 물리적 정당성이 약함

하지만 다음은 그대로 사용할 가치가 높다.
- PSD state vectors
- surface armour layer
- subsurface layers
- erosion transition matrix
- weathering transition matrix
- vertical resupply
- erosion/deposition mass balance
- soil-depth update
- DEM update

따라서:
```
2D event erosion model
 -> actual erosion/deposition mass
 -> SSSPAM/mARM state updater
 -> surface PSD / embedded PSD / armour / soil depth / DEM
```
가 고운사의 최소자의성 구조이다.

## OpenLISEM과의 역할분담
OpenLISEM:
- SWATRE Richards soil water
- measured/effective theta-h-K table
- 2D SWOF surface flow
- splash detachment
- flow detachment
- sediment transport/deposition
- litter interception/splash shielding
- surface stone shielding

SSSPAM/mARM:
- dynamic armour
- embedded PSD profile
- weathering/fragmentation
- surface/subsurface resupply
- long-term soil-depth and DEM evolution

## OpenLISEM의 한계
현재 source에서 확인:
- `StoneFraction`은 static input map
- `SwitchUseMaterialDepth = false`로 강제
- dynamic surface armour update가 production code에서 완결되지 않음
- multiclass sediment 관련 일부 UI/initialization code가 비활성/주석 상태
- root effect는 `cohadd` extra cohesion input이며 quantitative root biomass dynamics가 아님
- litter effect는 interception/splash protection 중심

따라서 OpenLISEM 하나로 100년 armour/profile feedback을 완결한다고 해서는 안 된다.

## 최종 판정
- dynamic armour / embedded PSD / weathering / soil-profile evolution: **SSSPAM/mARM 계보 최우선**
- event hydrology/erosion: **OpenLISEM+SWATRE 우선 비교 후보**
- SSSPAM 자체 hydrology/erosion 전체식: 사용하지 않음
- coupling은 new software coupling으로 명시하되, 새 empirical armour equation은 만들지 않는다.

## 관련 논문
- ../papers/2006_Willgoose_Sharmeen_ARMOUR.md
- ../papers/2006_Sharmeen_Willgoose_ArmourWeathering.md
- ../papers/2007_Sharmeen_Willgoose_LongTermArmour.md
- ../papers/2009_Cohen_mARM.md
- ../papers/2010_Cohen_mARM3D.md
- ../papers/2015_Cohen_mARM5D.md
- ../papers/2019_Welivitiya_SSSPAM_CoupledSoilscapeLandform.md
- ../papers/2022_Welivitiya_SSSPAM_GullyValidation.md
- ../papers/2023_Welivitiya_SSSPAM_Catchment.md
- ../papers/2024_Welivitiya_PhysicalWeatheringRate.md


---

## 2026-09-22 기존모델 사용가능성 재감사

### 실제로 강한 부분
SSSPAM/mARM 계보는 외부 coupling 없이 자체적으로 다음 상태를 관리한다.
- surface armour
- particle-size-resolved surface grading
- multiple subsurface layers
- depth-resolved PSD
- erosion 후 vertical resupply
- deposition 후 profile redistribution
- physical weathering
- soil depth/profile evolution
- DEM evolution

mARM5D는 공개 Fortran90 코드와 GPL v2 배포가 확인된다.
CSDMS/Zenodo source가 존재한다.

### fluvial erosion 자체
SSSPAM의 fluvial erosion은 자체 erodibility factor와 discharge/slope exponents를 사용하는 landscape-evolution erosion law를 사용한다.

대표 형태:
```
E_f = K_e q^alpha1 S^alpha2 T
```

따라서:
- rainfall-driven vs flow-driven detachment를 명시적으로 분리하지 않음
- root biomass/RLD/litter가 erodibility에 직접 들어가는 published dynamic vegetation module 없음
- 고운사 forest/postfire rill-interrill physics를 자체적으로 완결하지 않음
- site calibration된 fluvial parameters를 그대로 이식하면 안 됨

### 판정
**SSSPAM/mARM은 고운사 전체 erosion model이 아니라, 가장 강한 existing armour/profile/weathering engine 후보.**

즉 현재:
- armour/profile/weathering: 강력 후보
- event hydrology: 부족
- quantitative vegetation erosion resistance: 부족
- rill/interrill process separation: 부족

### CAESAR-Lisflood와 비교
SSSPAM/mARM:
- profile depth resolution, PSD, weathering에 강함
- event hydrodynamics 약함

CAESAR-Lisflood:
- 2D hydrodynamics, active layers, multiclass sediment, long-term morphology에 강함
- quantitative root/litter state와 stony-soil hydrology 약함

둘 다 단독으로 고운사 전체 요구를 만족하지 않는다.

## 2026-09-22 원논문 공간구조 재감사

### routing
Welivitiya et al. (2019) 원문은 regular square DEM에서 steepest-slope criterion으로 flow direction을 정하고, contributing area를 **D8**로 계산한다고 명시한다.
따라서 SSSPAM을 genuine 2D hydrodynamic model로 부르면 안 된다.

### runoff/transport
원문:
```
Q = r A_c / omega
```
- r: runoff excess generation
- A_c: contributing area
- omega: flow width

transport capacity:
```
T_c = K1 Q^delta1 S^delta2 d50a^delta3 omega
```
Zhang et al. (2011) flume fit에서 K1=2382.32, delta1=1.26, delta2=1.63, delta3=-0.34.

따라서 event hydrodynamics를 직접 푸는 구조가 아니라 D8 contributing-area + empirical transport-capacity 구조다.

### erosion/profile
실제 장점은 여전히 강하다.
- size-selective erosion transition matrix
- surface armour enrichment
- subsurface-to-surface mass resupply
- resupply propagation through all profile layers
- depth-resolved grading
- physical weathering
- deposition transition matrix
- DEM update

### 추가 한계
- bulk density를 grading/time에 무관한 constant로 가정
- deposition은 transport-capacity excess를 모두 퇴적시키는 단순화가 있음

### 재판정
**고운사 armour/profile/weathering 모델 후보로 유지.**
그러나 D8와 empirical transport-capacity 때문에 event-scale 2D water-erosion engine으로는 사용하지 않는다.
