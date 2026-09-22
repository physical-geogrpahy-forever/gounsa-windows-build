# Rock-fragment armour / fire-spall dynamics

## 고운사에서 조사한 이유
산불 뒤 fire spall과 기존 석력이 토양표면의 armour를 만들고, 이 armour가 infiltration, runoff, rill incision, soil loss, soil moisture 및 식생회복과 상호작용하는 과정을 동적 상태로 구현하기 위해 문헌계보를 정리한다.

## 핵심 결론
rock-fragment 효과는 단일 `armour cover` 계수로 표현하면 안 된다.

최소 상태변수:
- surface fragment cover
- soil-matrix rock-fragment content
- fragment size distribution
- resting / partially embedded / embedded fraction
- exposed fine-soil fraction
- mobile coarse-fragment pool
- fragment weathering/fragmentation state

## 생산과정
### wildfire -> fire spall
- Buckman et al. 2021: wildfire-induced spalling을 독립 physical-weathering process로 제시하며 quartz sandstone 사례 포함.
- Pala et al. 2025: fire가 exposed rock 및 pre-existing boulders를 파쇄해 3 mm-13 cm scale fragments를 만들고 postfire flow가 이를 재이동함.
- fire severity, exposed rock geometry, lithology/fracture state가 핵심 제약.

현재 quantitative spall-production rate의 고운사 parameterization은 unresolved이며 새로운 coupling이다.

## 장기 fragmentation/weathering
Shtober-Zisu & Wittenberg 2021:
- 10년 뒤 대부분의 large flakes/spalls가 사라지거나 파쇄 및 pulverization
- fire-induced surface stoniness는 장기간 증가 가능
- 따라서 spall size distribution은 시간에 따라 진화해야 함

## dynamic armour formation
Rieke-Zapp et al. 2007:
```
fine removal
 -> buried fragments exhumed
 -> surface fragment cover increases
 -> hydraulic roughness / shielding increases
 -> rill incision and sediment yield decrease
```

따라서 armour는 고정 초기조건이 아니라 erosion 자체에 의해 강화될 수 있는 state이다.

## armour hydrology
부호는 고정하지 않는다.

Poesen et al. 1990:
- resting fragments -> sealing 억제, infiltration 증가, runoff 감소
- embedded fragments -> infiltration 감소, runoff 증가

Cerdà 2001:
- 자연토양의 surface-resting fragments가 infiltration을 증가시키고 interrill erosion을 크게 줄일 수 있음.

Zhang et al. 2016:
- hydrological effect는 positive/negative 양쪽 모두 가능하며 fragment architecture가 핵심.

따라서:
```
I = f(soil, moisture, surface cover, size distribution, embeddedness, sealing, roots)
```
로 두며 `armour -> infiltration 감소`를 고정 규칙으로 두지 않는다.

## armour erosion shielding
Poesen et al. 1994, Rieke-Zapp et al. 2007, Jomaa et al. 2012:
- exposed fine-soil area 감소
- raindrop detachment 감소
- concentrated-flow detachment 및 transport capacity 감소
- armour가 충분하면 runoff가 있어도 sediment supply가 제한될 수 있음

고운사에서는 hydrological effect와 detachment shielding effect를 분리한다.

## fragment size effect
Li et al. 2022:
- <12 cm fragments는 실험조건에서 대체로 runoff/soil loss 감소
- >=12 cm fragments는 runoff/soil loss를 증가시킬 수 있음
- 작은 fragments는 같은 cover에서 flow-path tortuosity와 barrier density가 증가

따라서 `fragmentation -> armour 감소`로 직접 연결하지 않는다.

정확한 구조:
```
large fragment
 -> fragmentation/weathering
 -> smaller size class
 -> shielding efficiency changes
 -> size-specific mobility threshold changes
 -> actual entrainment/removal
 -> armour cover changes
```

## coarse-fragment mobility
Poesen 1987:
- field rill flow가 관측사건에서 최대 약 9 cm diameter fragments를 운반
- interrill competence는 훨씬 낮음
- mobility는 size, rill slope, flow energy에 의존

Pala et al. 2025:
- thermal spalling이 boulder size를 줄여 subsequent mobilization에 필요한 shear stress를 낮춤

따라서 armour loss는 fragmentation 자체가 아니라 **fragmentation + transport/removal**로 계산한다.

## steep-slope correction
Song et al. 2026:
`C = a exp(-b Rc)`에서 erosion-control coefficient b가 slope 증가와 함께 감소.
급경사에서는 low-cover armour의 보호효과가 약해지거나 runoff/sediment response가 일부 역전될 수 있음.

## soil moisture / vegetation bridge
Huang et al. 2024:
rock-fragment content가 10-50 cm soil water를 변화시키며 species/root traits에 따라 효과가 달라짐.

고운사:
```
fragment architecture
 + soil depth
 + fine-earth volume
 + root/macropore state
 -> soil hydraulic properties
 -> soil moisture
 -> LPJ-GUESS PFT stress / establishment
```
는 새로운 coupling이다.

## 고운사 권장 상태방정식 구조
```
Fire
 -> SpallProduction(size)
 -> MobileFragment(size) + SurfaceFragment(size)

SurfaceFragment(size, embeddedness)
 -> ShieldingFactor
 -> exposed fine-soil fraction
 -> interrill/rill detachment resistance

SurfaceFragment + SoilMatrixFragment
 -> HydraulicModifier
 -> infiltration / runoff / soil moisture

Erosion of fines
 -> fragment exhumation
 -> armour increase

Weathering/fragmentation
 -> transition among fragment size classes

2D rill hydraulics
 -> size-specific fragment entrainment/removal
 -> armour decrease
```

## 최종 판정
- dynamic armour module: 채택
- size-class tracking: 채택
- resting/embedded distinction: 채택
- universal `armour -> infiltration decrease`: 탈락
- universal `fragmentation -> armour decrease`: 탈락
- fragmentation + size-specific removal -> armour decrease: 채택 구조
- 모든 모델간 연결부는 **새로운 coupling**으로 명시

## 관련 논문
- ../papers/1987_Poesen_RockFragmentRillTransport.md
- ../papers/1990_Poesen_RockFragmentPositionHydrology.md
- ../papers/1994_Poesen_Torri_Bunte_RockFragmentErosionReview.md
- ../papers/2001_Cerda_RockFragmentInfiltrationErosion.md
- ../papers/2007_RiekeZapp_RockFragmentsConcentratedFlowArmour.md
- ../papers/2012_Jomaa_RockFragmentHydrologyErosionModel.md
- ../papers/2016_Zhang_RockFragmentsHydrologicalProcessesReview.md
- ../papers/2021_Buckman_FireSpallingSandstone.md
- ../papers/2021_ShtoberZisu_WildfireRockWeatheringStoniness.md
- ../papers/2022_Li_RockFragmentSizeErosion.md
- ../papers/2024_Huang_RockFragmentSoilWaterVegetation.md
- ../papers/2025_Pala_ThermalSpallingPostfireDebrisFlow.md
- ../papers/2026_Song_SlopeDependentRockFragmentErosion.md
