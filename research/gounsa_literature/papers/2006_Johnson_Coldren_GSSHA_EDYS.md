# Johnson & Coldren (2006) — GSSHA + EDYS linkage

## 서지정보
Johnson, B. E., & Coldren, C. L. (2006). *Linkage of a Physically Based Distributed Watershed Model and a Dynamic Plant Growth Model*. ERDC/EL TR-06-17. U.S. Army Engineer Research and Development Center, Environmental Laboratory. 95 pp. AD accession: ADA461457.

## 이 논문을 검색한 이유
고운사에서 필요한 핵심 구조인

```text
subdaily distributed watershed hydrology
 <->
 daily dynamic vegetation / roots / uptake
```

의 기존 선례를 찾기 위해 EDYS의 외부 수문모델 coupling 계보를 추적했다.

## 연구 유형
- model-coupling development report
- physically based distributed hydrology + dynamic ecosystem/plant model linkage
- GSSHA + EDYS

## 모델 구성
### GSSHA
- physically based distributed watershed model
- 2-D overland flow
- infiltration / soil moisture
- groundwater-associated hydrologic processes
- sediment / constituent transport lineage

### EDYS
- daily dynamic plant/ecosystem model
- precipitation, interception, evaporation, infiltration, transpiration
- plant water / nutrient / contaminant uptake
- species-level vegetation dynamics

## 핵심 coupling 목적
보고서 abstract가 명시하는 핵심은 **soil moisture linkage**이다.

개념적 자료흐름:

```text
EDYS
  daily vegetation state
  transpiration / ET
  water uptake
  nutrient / contaminant uptake
        |
        v
GSSHA distributed hydrology
  larger-scale surface/subsurface water movement
  groundwater / transport state
        |
        v
EDYS ecological response
```

보고서는 EDYS가 small-scale daily ecological flux를 더 현실적으로 제공하고, GSSHA와 관련 groundwater code가 larger-scale hydrologic/transport estimates를 다시 EDYS에 제공할 수 있다고 설명한다.

## 중요한 해석 제한
이 보고서를 다음처럼 과장해서 인용하지 않는다.

```text
"2006년에 완전히 검증된 operational two-way EDYS-GSSHA coupling이 완성됐다"
```

현재 확보한 abstract의 정확한 표현은 **development effort investigated the linkage of soil moisture**이며, 양방향 자료흐름은 long-term coupling architecture로 설명된다.

다만 후속 McLendon et al. (2009)은 EDYS가 GSSHA, CASC2D, HSPF 및 MODFLOW와 linked되어 integrated watershed-management simulation systems에 사용되었다고 명시한다. 따라서 external distributed-hydrology linkage precedent 자체는 존재한다고 판단한다.

## 고운사에 사용할 수 있는 부분
고운사에서 가장 직접적으로 차용할 수 있는 설계는 시간척도 분리이다.

```text
hourly/subhourly hydrology + geomorphology
 -> daily soil-water / groundwater / transport state
 -> daily vegetation/root uptake and biomass response
 -> ET / interception / uptake / litter / roots
 -> next hydrologic cycle
```

이는 식생모델 자체를 1시간 간격으로 완전히 재작성하지 않고도 폭우 수문과 장기 식생천이를 연결하는 근거가 된다.

## EDYS 자체와의 추가 장점
EDYS는 별도 외부 hydrology coupling뿐 아니라 native하게:
- multilayer soil
- species root biomass by layer
- dynamic root redistribution according to actual uptake
- cell-to-cell runoff
- sediment / litter / nutrient transport
- erosion/deposition-driven soil-layer thickness change
를 갖는다.

따라서 GSSHA-style external hydrology를 사용할 경우에도 vegetation/soil interface state가 비교적 풍부하다.

## 필요한 새로운 coupling
고운사에서는 다음을 추가로 구현하거나 검증해야 한다.
1. storm-event geomorphology가 바꾼 soil-layer thickness를 EDYS/vegetation state에 전달
2. erosion으로 제거된 토층의 root biomass를 보존적으로 절단/remap
3. deposition 시 root burial와 aeration/plant mortality 처리
4. DEM/rill network 변화 이후 distributed hydrology connectivity 재계산
5. vegetation-cell과 finer geomorph-cell 사이 scale exchange

## 한계
- 2006 report는 development study이며 현재 확보된 abstract만으로 완성도와 production robustness를 과장할 수 없음
- EDYS 자체는 woody DBH/age cohort가 아니라 species/stage biomass model
- canopy/understory geometry is much simpler than FATES or LPJ-GUESS SEC/PPA
- modern public EDYS source repository가 확인되지 않음

## 최종 판정
**매우 중요한 coupling precedent.**

특히 고운사에서 `hourly hydrology/geomorphology + daily vegetation` 구조를 채택하는 데 강한 선례를 제공한다.

그러나 이 논문만으로 완성된 현대 two-way coupling software가 공개되어 있다고 주장하지 않는다.

## 후속 근거
McLendon, T., Coldren, C. L., & Price, D. L. (2009). Comparison of Results from the EDYS and EDYS-L Ecological Simulation Models as Applied to Vegetation and Hydrological Dynamics on the Honey Creek Watershed, Texas. ERDC TN-SWWRP-09-7.
