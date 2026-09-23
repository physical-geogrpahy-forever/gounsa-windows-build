# EDYS / TerreSIM lineage

업데이트: 2026-09-23

## 현재 판정
EDYS는 고운사 ecogeomorphic architecture와 매우 가까운 **scientific top-tier comparator**이다. 특히 actual raster landscape, species-level vegetation, layer-specific roots, runoff/sediment transport, erosion/deposition-driven soil-depth change를 한 모델에 넣은 점은 매우 드물다.

그러나 최신 v5.1 시간루프를 감사한 결과, `수문/식물 water uptake는 daily`지만 **actual plant biomass and downward root growth는 monthly update**이다. 따라서 strict criterion 5에는 완전 합격하지 않는다. 또한 woody DBH/age cohort와 multilayer canopy geometry가 없다.

최종 역할:
**통합 ecogeomorphic architecture benchmark + 조건부 후보.**

---

## 1. 식생 구조
EDYS는 종별 또는 composite species별 biomass population을 계산한다.

생활형:
- annual/perennial grass
- annual/perennial forb
- shrub
- tree
- deciduous/evergreen woody

주요 상태:
- coarse roots
- fine roots
- trunk/crown
- stems
- leaves
- seeds
- standing dead
- seedling roots/shoots
- seed bank

stage structure:
```text
seed bank
 -> germination / seedlings
 -> adult species biomass
```

따라서 static cover model은 아니지만, FATES/LPJ-GUESS/RED처럼 woody plants를 DBH/age/height cohort로 세분하는 demographic cohort model도 아니다.

정확한 분류:
**species-level stage-structured biomass population model**.

---

## 2. postfire succession
Mata-González et al. (2007) sagebrush-steppe fire application:
- burned/unburned field data로 검증
- 50-year simulations
- 초기 annual Bromus tectorum 우점
- 약 13-15년 후 perennial herb/shrub species로 replacement
- 주요 후속종에 Chrysothamnus, Artemisia, Agropyron 포함
- fire가 annual dominance persistence를 연장

즉 fire 이후 herbaceous -> perennial herb/shrub replacement를 실제 published simulation으로 보여준다.

산림/woodland 적용 계보도 존재한다:
- ponderosa pine forest
- lodgepole pine forest
- subalpine fir/alpine tundra
- pine-oak woodland
- pinyon-juniper-oak woodland
- riparian shrubland
- Texas oak/juniper/mesquite systems

---

## 3. soil and roots
EDYS soil profile은 여러 user-defined layers를 갖는다.

layer states:
- thickness
- water content
- field capacity / saturation
- nutrients
- organic matter
- salinity / contaminants

root state:
- coarse/fine root biomass
- species × soil-layer root biomass
- rooting depth
- maximum potential root depth
- species root uptake capacity

### dynamic root distribution
초기 root profile은 species-specific distribution으로 설정되지만 고정되지 않는다.

실제 water uptake가 발생한 soil depths에 new root biomass가 우선 배분되고, `RootReallocation`은 이전 기간 uptake distribution을 이용해 layer별 root allocation을 조절한다.

또한 fine roots can grow downward subject to maximum rooting depth and saturated-zone constraints.

### saturation-root mortality
water table/saturated zone 상승 시 species tolerance에 따라:
- roots in newly saturated layers are killed
- rooting depth is updated
- dead roots -> soil organic matter
- root N -> soil organic N

이 구조는 external groundwater coupling에 매우 유리하다.

---

## 4. dynamic soil depth and geomorphology
EDYS runoff/erosion procedure는 actual landscape grid에서 sediment를 이동시킨다.

응용문서가 명시하는 soil-profile response:
- deposition -> top soil layer thickness increases
- erosion -> top layer thickness decreases
- if top layer is removed completely, erosion proceeds into the next layer

1999 pseudocode에서도 runoff routine은:
```text
cell runoff
 -> sediment/litter carrying capacity
 -> mobilization/deposition
 -> erosion loss/gain
 -> revise soil/quadrat profile
```
를 수행한다.

따라서 `erosion/deposition -> dynamic soil-layer geometry`는 native concept이다.

### 아직 미확인
현재 문서 감사로는:
- saturation-driven root death = explicit
- erosion-driven soil-layer loss = explicit
- **erosion-driven immediate truncation/remapping of root biomass = not explicitly demonstrated**

고운사 직접 사용 시 반드시 source/executable test가 필요하다.

---

## 5. spatial landscape and hydrology
EDYS spatial landscape는 vegetation/community, elevation, management 및 soil information을 raster/cell 구조로 사용한다.

plot/quadrat ecological calculations을 representative states로 계산한 뒤 actual cells에 적용하고, landscape-level processes는 cell topology에서 수행한다.

native/lineage hydrologic processes:
- precipitation/interception
- infiltration/percolation
- evaporation
- plant uptake
- surface runoff
- subsurface lateral flow lineage
- groundwater/saturation influence
- sediment/litter/nutrient/contaminant transport

즉 internal statistical disturbance patches만 가진 ED/FATES와 달리 geographic raster landscape가 실제 존재한다.

---

## 6. GSSHA and external hydrology coupling
Johnson & Coldren (2006), ERDC/EL TR-06-17, ADA461457는 GSSHA + EDYS의 soil-moisture linkage를 개발/검토했다.

개념적 자료흐름:
```text
EDYS
  ET / transpiration
  plant water, nutrient, contaminant uptake
       ->
GSSHA distributed hydrology
  larger-scale surface/subsurface/groundwater state
       ->
EDYS
```

중요한 해석 제한:
- 보고서 abstract는 `development effort investigated the linkage`라고 표현한다.
- 따라서 2006 보고서만으로 fully validated production two-way coupling이 완성됐다고 과장하지 않는다.

그러나 McLendon et al. (2009)은 EDYS가 MODFLOW, GSSHA, CASC2D, HSPF와 linked되어 integrated watershed-management systems에 사용됐다고 명시한다.

따라서 **external distributed-hydrology linkage precedent 자체는 강하다.**

고운사에 가장 유용한 architecture:
```text
hourly/subhourly hydrology + geomorphology
 -> daily soil-water/groundwater state
 -> EDYS-style vegetation water uptake
 -> slower biomass/successional update
```

---

## 7. canopy and understory limitation
EDYS has species-to-species light competition matrices and biomass-to-canopy-cover factors.

하지만 forest canopy geometry는 SEC/FATES보다 훨씬 단순하다.

South Texas watershed applications explicitly note a spatial averaging problem:
- a cell may contain woody clusters plus herbaceous interspaces
- EDYS averages them across the cell
- applying woody shading uniformly would over-suppress herbs outside woody crowns
- later applications therefore limited some woody->herb shading while retaining woody-woody and herb-herb shading

즉:
```text
species-specific shading = YES
explicit vertical multilayer canopy / within-cell crown geometry = NO
```

이 점은 산림 고운사에서 큰 약점이다.

---

## 8. timestep audit: important correction
Full EDYS v5.1 uses nested annual, monthly and daily loops.

### daily
- precipitation
- infiltration/percolation
- runoff
- evaporation
- decomposition
- plant/seedling water uptake
- soil water/nutrient dynamics

### monthly/end-of-month
- potential/actual biomass production accounting
- downward root growth / root allocation update
- some seedling/phenology processes
- animal population dynamics
- fire/management/disturbance scheduling in the standard sequence

The v5.1 User Guide explicitly states plant growth and downward root growth are calculated when the daily loop for the month is complete, based on accumulated water uptake.

Therefore the correct classification is:
```text
hydrology / root uptake = DAILY
plant/root biomass production = MONTHLY
```

This downgrades criterion 5 from STRONG to **PARTIAL** under the user's strict requirement of vegetation processes <= daily.

---

## 9. software availability
Historical implementation:
- EDYS v2: Turbo Pascal 7
- extensive pseudocode/data structures published

Later lineage:
- full EDYS User Guide v5.1.0 (2011)
- watershed applications continued through at least the late 2010s
- 2026 Texas Tech profile still describes long-running EDYS research

Official availability remains request/executable-oriented.
No maintained public GitHub source repository was identified in the 2026-09-23 search.

Thus:
**scientific fit high, modern software accessibility/maintenance risk high.**

---

## 10. TerreSIM
TerreSIM was described as a next-generation/successor lineage with:
- spatial terrestrial ecosystem simulation
- soil/water/plant/animal modules
- surface/subsurface material transport
- species-level plant dynamics
- ability to represent explicit individual plants/trees where desired

But it is associated with a proprietary MFG Inc. lineage and no modern public source was identified.
It is therefore less practical than using EDYS as an architectural benchmark.

---

## 11. 고운사 5조건 final audit
| 기준 | 판정 | 이유 |
|---|---|---|
| 1 spatial cohort/hybrid | **STRONG spatial / PARTIAL cohort** | actual raster landscape + seedling/adult species stages, but no woody DBH/age cohorts |
| 2 explicit understory + succession | **VERY STRONG** | grass/forb/shrub/tree species, seed bank/seedling/adult, demonstrated postfire succession |
| 3 soil depth / WHC / geomorph | **VERY STRONG** | multilayer soil, layer roots, dynamic root distribution, erosion/deposition changes layer thickness |
| 4 watershed/topography | **VERY STRONG** | raster runoff/sediment plus MODFLOW/GSSHA/CASC2D/HSPF linkage lineage |
| 5 <=daily vegetation timestep | **PARTIAL** | daily hydro/uptake but monthly biomass/root production |

---

## 12. shortlist position
EDYS does **not** replace LPJ-GUESS SEC/PPA or FATES as the best modern demographic forest engine because:
- no woody size/age cohorts
- no multilayer canopy geometry
- monthly biomass/root production
- public modern source unavailable

However EDYS is currently the strongest architectural precedent for:
```text
species vegetation
+ layer roots
+ actual landscape runoff
+ sediment transport
+ dynamic soil depth
+ long-term succession
```

Therefore the most promising Gounsa design may borrow complementary strengths:

```text
LPJ-GUESS SEC/PPA or FATES
  -> modern tree/shrub/herb demography and canopy structure

EDYS + Quijano-Baron et al. architecture
  -> root/litter/soil-state to runoff/erosion/deposition coupling

external hourly geomorph/hydrology
  -> storm-scale terrain change
```

## next checks
1. full EDYS source/executable access and license
2. erosion-driven root truncation
3. whether later EDYS versions implemented within-cell woody/herb spatial heterogeneity
4. direct GSSHA-EDYS implementation details beyond the abstract
5. computation at 1-10 m landscape cells

## 핵심 문헌
- Childress et al. (1999), CERL TR 99/55.
- Childress et al. (2002), Ecological Modelling 153:97-108, DOI 10.1016/S0304-3800(01)00504-X.
- Johnson & Coldren (2006), ERDC/EL TR-06-17, ADA461457.
- Mata-González et al. (2007), Journal of Arid Environments.
- McLendon et al. (2009), ERDC TN-SWWRP-09-7.
- Coldren et al. (2011), EDYS User's Guide v5.1.0.
- South Texas EDYS watershed reports, 2012-2019.
