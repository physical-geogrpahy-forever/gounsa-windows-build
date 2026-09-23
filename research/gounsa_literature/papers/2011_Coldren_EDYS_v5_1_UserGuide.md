# Coldren et al. (2011) — EDYS User's Guide v5.1.0

## 서지정보
Coldren, C. L., McLendon, T., & Childress, W. M. (2011). *Ecological DYnamics Simulation Model (EDYS) User's Guide, Version 5.1.0*. KS2 Ecological Field Services LLC.

## 이 문서를 검색한 이유
1999 EDYS 기능보고서 이후 최신 full-EDYS 계열에서 실제 시간루프, 뿌리, 토양, 식물생산, saturated-root mortality가 어떻게 구현되는지 확인하기 위해 검토했다.

## 핵심 시간구조
EDYS는 여러 nested timestep을 사용한다.

### Annual loop
- end-of-year bookkeeping/output

### Monthly loop
월 시작에:
- seasonal dieback
- seedling -> adult transfer
- seed drop
- potential seed sprout
- potential plant production
- potential transpiration
- saturated-root death 등

### Daily loop
- actual seed germination
- precipitation
- infiltration/percolation
- runoff
- evaporation
- decomposition
- root water/nutrient uptake

### 월말
사용설명서 본문의 명시적 설명상:
- actual plant growth
- downward root growth
- animal population dynamics
- herbivory / management / disturbances such as fire
- reporting
이 수행된다.

따라서 EDYS를 단순히 `daily vegetation model`이라고 부르면 부정확하다.

정확한 판정:
```text
soil water / hydrology / uptake = DAILY
potential growth constraints = daily information accumulated
actual biomass/root production = MONTHLY update
```

이는 고운사 criterion 5에서 중요한 제한이다.

## 식물 구조
종별로 다음 biomass compartments를 추적한다.
- coarse roots
- fine roots
- trunk / crown
- stems
- leaves
- seeds
- standing dead stems/leaves
- seedling roots/shoots
- seed bank

adult tissue는 old/new biomass를 구분한다.

## 뿌리 구조
- root biomass is stored by soil layer
- fine-root downward extension occurs subject to species maximum rooting depth
- new roots are allocated within existing rooted layers and into newly reached deeper layers
- root growth is limited by saturated zones for saturation-sensitive species
- root distribution can shift according to actual water uptake

### saturated-root mortality
포화대가 상승하면 species-specific tolerance에 따라:
- top saturated layer의 일부 roots를 kill
- deeper saturated layers의 roots를 모두 kill 가능
- dead root biomass -> soil organic matter
- root N -> soil organic N
- rooting depth update

이는 external groundwater/hydrology coupling에 유리한 explicit state response이다.

## 토양/수문
- multiple user-defined soil layers
- water content / field capacity / saturation
- infiltration/percolation
- evaporation
- plant uptake
- surface runoff
- groundwater / saturation effects
- nutrients and organic matter transported with water

## erosion / dynamic soil depth
EDYS landscape runoff routines can erode/deposit sediment and alter soil-profile layers. Other EDYS application reports explicitly state:
- deposition increases top layer thickness
- erosion decreases top layer thickness
- complete removal of top layer exposes/erodes the next layer

However, this user-guide audit did **not** find an explicit routine stating that erosion-triggered removal of a layer immediately truncates all root biomass stored in the lost portion.

Therefore:
```text
dynamic soil geometry = native
saturation-driven root death = native
erosion-driven root truncation = not yet demonstrated
```

## canopy / understory limitation
EDYS includes species-to-species light competition and canopy-cover factors, but watershed cells generally average vegetation states within the cell. Later South Texas applications explicitly note that woody clusters and herbaceous interspaces can be spatially mixed inside one cell, making woody-to-herb shading difficult to represent correctly.

Thus EDYS does not provide FATES/LPJ-GUESS-SEC-class multilayer forest canopy geometry.

## 고운사 판정
1. spatial landscape: strong
2. herb/shrub/tree species succession: strong
3. multilayer soil/root and geomorph soil-depth feedback: very strong
4. watershed/topography: strong
5. timestep: **partial**, because hydrology/uptake are daily but plant/root biomass production is fundamentally monthly

## 최종 의미
EDYS는 고운사 통합 구조의 매우 중요한 architectural benchmark이나, 사용자의 strict <=daily vegetation-process requirement에는 완전 합격하지 않는다.

특히 다음 둘을 구분해야 한다.
```text
"daily ecological forcing and water uptake" = YES
"daily demographic/biomass growth update" = NO, monthly in full EDYS v5.1 structure
```
