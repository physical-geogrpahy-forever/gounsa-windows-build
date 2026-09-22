# 2026-09-22 dynamic-armour model-selection handoff

## 사용자 요구
- 고운사에는 매립 석력이 많다.
- 가장 중요한 것은 어떤 기존 model을 가져올지 결정하는 것.
- arbitrary empirical coefficient를 만들지 않는다.

## 이번 조사에서 가장 중요한 발견
dynamic armour와 embedded rock-fragment profile을 이미 다루는 기존 model lineage:
```
ARMOUR
 -> mARM
 -> mARM3D/mARM5D
 -> SSSPAM
```

이 계보는:
- selective fine removal
- armour development
- size-specific transport
- particle weathering
- multilayer embedded PSD
- subsurface resupply
- soil-depth update
- DEM evolution
을 published model로 처리한다.

## OpenLISEM source inspection
현재 source에서 확인:
- SWATRE reads theta-h-K lookup tables directly
- SWATRE solves Richards-equation type vertical soil-water movement
- current OpenLISEM has 2D SWOF flow and sediment detachment/transport
- StoneFraction statically shields splash and flow detachment
- litter affects interception and splash
- plant-root effect enters as extra cohesion input
- StoneFraction is not dynamically updated
- material-depth switch is disabled in current initialization
- some multiclass sediment controls are inactive/commented

따라서 OpenLISEM alone은 100-year dynamic armour/profile model이 아니다.

## 현재 최우선 architecture
```
LPJ-GUESS
 -> vegetation state

OpenLISEM + SWATRE
 -> event soil water
 -> 2D runoff
 -> splash/flow detachment
 -> actual erosion/deposition mass

SSSPAM / mARM
 -> size-class selective state update
 -> surface armour
 -> embedded PSD
 -> physical weathering
 -> soil-depth update
 -> DEM update
```

## 왜 SSSPAM의 자체 erosion equation을 쓰지 않는가
SSSPAM fluvial erosion parameters are calibrated from site/lab data.
고운사에 그대로 가져오면 user requirement인 minimum arbitrariness와 충돌한다.

따라서 SSSPAM에서는 state-update machinery를 쓰고 event erosion mass는 OpenLISEM에서 가져온다.

## 새로 저장한 핵심 papers
- 2006_Willgoose_Sharmeen_ARMOUR.md
- 2006_Sharmeen_Willgoose_ArmourWeathering.md
- 2007_Sharmeen_Willgoose_LongTermArmour.md
- 2009_Cohen_mARM.md
- 2010_Cohen_mARM3D.md
- 2015_Cohen_mARM5D.md
- 2019_Welivitiya_SSSPAM_CoupledSoilscapeLandform.md
- 2022_Welivitiya_SSSPAM_GullyValidation.md
- 2023_Welivitiya_SSSPAM_Catchment.md
- 2024_Welivitiya_PhysicalWeatheringRate.md
- 2016_Zhang_LEPIHM.md

## 새 model/decision
- models/ARMOUR_mARM_SSSPAM.md
- decisions/2026-09-22_DYNAMIC_ARMOUR_MODEL_SELECTION.md

## 현재 남은 가장 중요한 검증
1. OpenLISEM event erosion output을 SSSPAM `E_a` interface에 mass-conserving하게 전달하는 exact variable mapping
2. deposition mass와 sediment PSD의 전달
3. LPJ-GUESS FineRootC -> root detachment resistance without arbitrary fitting
4. SurfaceLitC -> OpenLISEM litter cover with published relation
5. fire severity -> initial fire-spall PSD
6. high embedded stoniness의 theta-h-K를 field measurement or stony-soil hydraulic model로 구성
