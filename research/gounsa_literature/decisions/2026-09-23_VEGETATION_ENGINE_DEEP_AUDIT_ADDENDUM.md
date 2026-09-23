# 고운사 식생 엔진 심층 감사 추가 기록

업데이트: 2026-09-23

이 문서는 `2026-09-23_VEGETATION_ENGINE_DEEP_AUDIT.md` 이후 추가로 확인된 **소스코드 수준의 결정사항**만 기록한다.

---

# 1. FATES: host-dependent이지만 ELM/CLM 고정은 아님

현재 공개 FATES source의 `FatesInterfaceMod.F90`은 스스로 이를 **FATES public API**라고 정의한다.

핵심 구조:
```text
host land model / driver
 -> fates_interface_type
    -> sites
    -> bc_in(:)
    -> bc_out(:)
    -> bc_pconst
```

`bc_in`은 host/driver가 채우는 boundary/state이고 `bc_out`은 FATES가 host에 반환하는 값이다.

`FatesInterfaceTypesMod.F90`은 host가 결정하는 항목으로 다음을 별도 정의한다.
- soil layer number
- host timestep
- restart status
- seed-dispersal cadence
- nutrient coupling
- plant-hydraulic solver
- regeneration model
- inventory initialization
- fire/land-use options

또한 source comments는 CLM/ALM뿐 아니라 ATS도 host-model 계열로 염두에 둔다.

따라서 이전의 단순 표현:
```text
FATES requires ELM/CTSM
```
은 너무 강하다.

정확한 표현:
```text
FATES requires a host/driver that implements the HLM interface.
ELM/CTSM are mature hosts, but the public API is not conceptually tied to one host.
```

고운사에서 custom thin host를 작성하는 것은 원리적으로 가능하지만, 이는 별도 소프트웨어 개발과 검증이 필요한 작업이다.

---

# 2. FATES: 실제 soil/bedrock rooting boundary interface

현재 source `bc_in_type`에는:
```text
max_rooting_depth_index_col
```
이 있으며 주석은 이를:
`permafrost or bedrock constraints 때문에 roots가 존재할 수 있는 가장 깊은 soil level의 index`
라고 정의한다.

이 값은 실제로 여러 과정에서 `set_root_fraction()`에 전달된다.
- water stress
- photosynthesis
- cohort dynamics
- mortality
- litter / soil BGC

즉 shallow bedrock/soil column 자체를 FATES root calculation에 전달할 명시적 host interface가 있다.

그러나 이것은:
```text
where roots may exist
```
를 제한할 뿐,
```text
erosion physically removes existing live root biomass
```
를 자동으로 처리하지 않는다.

고운사에서는 반드시 별도 root-severing/remapping event가 필요하다.

---

# 3. FATES: inter-grid seed dispersal도 host-coordinated

Current source에는 PFT별:
- `fates_seed_dispersal_fraction`
- `fates_seed_dispersal_max_dist`
- dispersal-kernel parameters
이 존재한다.

그러나 `EDPhysiologyMod.F90`에서는 host land model의 `hlm_seeddisp_cadence`가 활성화되어야 실제 dispersed seed fraction을 사용한다.

따라서:
```text
FATES grid-cell seed dispersal
= native biological machinery + HLM coordination
```
이다.

이것은 custom lightweight host를 만들 때 반드시 구현해야 할 API 항목 중 하나다.

---

# 4. MEDFATE: herb layer는 full demographic cohort가 아님

이전 감사에서 신규 herb recruitment 부재를 확인했다.
추가 source audit는 이를 더 강하게 확정했다.

`growth_day_c.cpp`의 daily mortality section:
```text
bool dynamicCohort = true;
if((ctype[j] == "shrub") && (!shrubDynamics)) dynamicCohort = false;
else if(ctype[j] == "herb") dynamicCohort = false;
```

즉 herb cohort는 tree와 dynamic shrub이 사용하는 daily dynamic-cohort mortality logic에서 명시적으로 제외된다.

따라서 MEDFATE herb의 정확한 판정은:
```text
species-specific herb state: YES
height / cover / root depth: YES
daily physiology and growth: YES
water competition: YES
new herb recruitment: NO
same demographic mortality as woody cohorts: NO
```

고운사에서 산불 직후 초본종의 colonisation, replacement, dieback을 내생적으로 재현하려면 **완전한 herb lifecycle module**이 필요하다.

이는 작은 recruitment helper보다 큰 개발이다.

---

# 5. MEDFATE: woody daily response는 강함

같은 `growth_day_c.cpp`는 woody/dynamic-shrub cohort에 대해 일별로 다음을 갱신한다.
- fine-root biomass
- fine-root area
- fine-root area growth
- rhizosphere conductance
- root hydraulic conductance
- sapwood/leaf growth
- DBH / height
- carbon-starvation / desiccation mortality logic

따라서 extreme storm 이후 다음 날 woody physiological/root response를 표현하기에는 LPJ-GUESS annual allocation loop보다 직접적이다.

---

# 6. JULES-RED: daily demography는 source-level로 확정

현재 public `MetOffice/jules` source:
`src/science/vegetation/veg3_red_dynamic_mod.F90`

확인된 실제 상태방정식:
- reproductive assimilate `P_s`
- structural growth `g`
- first mass class seedling influx
- mass-class-to-class flux
- mortality
- plant number density update

그리고 current host call path에서는:
```text
CALL veg3_red_dynamic(..., rsec_per_day, ...)
```
로 호출한다.

따라서 최신 source path에서 RED mass-class demography는 **실제로 daily timestep**으로 동작한다.

이는 이전 평가보다 강한 장점이다.

---

# 7. JULES-RED: root state는 반대로 더 단순함

RED는 woody vegetation을 mass classes로 나누지만, current JULES state는 mass-class number-density를 합산한 뒤 PFT-level에서:
```text
leafC
rootC
woodC
```
를 계산한다.

즉:
```text
aboveground demographic structure = mass class detailed
belowground root biomass = PFT aggregate
```
이다.

Root vertical weighting은 PFT `rootd_ft_io` 기반 exponential profile을 사용한다.

따라서 고운사의 erosion/root-resistance coupling에는 FATES나 MEDFATE보다 간접적이다.

---

# 8. LPJ-GUESS SEC: event-scale damage hook이 필요

SEC/PPA가 수관과 recruitment 공간구조를 개선했어도 standard LPJ-GUESS의 시간계층을 완전히 바꾼 것은 아니다.

대체로:
```text
daily:
photosynthesis / respiration / phenology / hydrology / soil processes

annual:
allocation / establishment / background mortality and structural demographic updates
```

따라서 6-hour storm이 soil depth와 root biomass를 즉시 제거한다면:
- soil water stress / photosynthesis는 다음 daily step에서 반응 가능
- 그러나 physical root loss와 catastrophic plant damage를 annual demographic loop까지 기다리면 부적절

필요:
```text
geomorphic event damage hook
 -> physically remove roots
 -> optionally reduce structural/plant carbon
 -> apply immediate cohort damage or mortality fraction
 -> resume daily physiology
```

이 기능은 **새로운 coupling**으로 명시한다.

---

# 9. 현재 삼각 구도

심층 감사 후 하나의 절대 1위보다 다음 세 축이 더 정확하다.

## FATES
**생물학 + 시간해상도 + hydraulics 최강**
- tree/shrub/grass genuine demography
- daily demography
- subdaily physiology/hydraulics
- host root-depth boundary
- grid-cell seed dispersal machinery

비용:
- host implementation
- implicit internal patches
- root-severing/soil remap custom

## LPJ-GUESS SEC
**공간 수관/cohort middle-ground 최강**
- cohort, not individual tree
- persistent gap positions
- 0.1 ha nominal patch scale, about 31.6 m square equivalent
- forest-floor light mosaic

비용:
- branch merge with external hydrology
- annual demographic structural timing
- event damage hook
- conservative root/soil remap

## MEDFATE
**engineering / actual GIS / event-loop 최강**
- direct GIS cells
- transparent R/Rcpp state objects
- daily woody/root response
- external hydrology interface
- explicit soil-layer redefinition hook

비용:
- full herb demographic lifecycle must be developed
- root severing and conservative soil-state remap custom

## JULES-RED
**lightweight fallback**
- daily mass-class demography confirmed
- broad tree/shrub/grass succession

비용:
- simplified canopy
- PFT-aggregate roots
- dynamic cell-specific soil geometry intrusive

---

# 10. 다음 판단은 common-event prototype로 한다

모든 후보에 동일한 시험을 적용한다.

```text
T0
postfire state initialization

T1
6-hour extreme rainfall
 -> erosion/deposition
 -> soil depth changes
 -> root mass physically removed/buried
 -> hydrologic state changes

T1 + 1 day
 -> photosynthesis / water stress / root hydraulics response
 -> immediate damage/mortality if appropriate

T1 + 1 season to years
 -> recruitment / mortality / succession
```

이 시험에서 **가장 적은 비문헌 custom biology를 추가하면서 전체 상태를 보존할 수 있는 엔진**을 최종 채택한다.
