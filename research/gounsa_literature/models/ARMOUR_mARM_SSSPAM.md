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
