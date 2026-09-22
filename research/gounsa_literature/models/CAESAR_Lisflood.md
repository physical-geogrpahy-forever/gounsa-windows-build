# CAESAR-Lisflood

## 핵심 문헌
Coulthard, T. J., Neal, J. C., Bates, P. D., Ramirez, J., de Almeida, G. A. M., & Hancock, G. R. (2013). Integrating the LISFLOOD-FP 2D hydrodynamic model with the CAESAR model: implications for modelling landscape evolution. *Earth Surface Processes and Landforms, 38*, 1897-1906. https://doi.org/10.1002/esp.3478

## 검토 목적
고운사에서 별도 Iber+ ↔ SSSPAM coupling 없이 하나의 기존 모델로 다음을 동시에 처리할 수 있는지 확인:
- 2D runoff
- multiclass sediment
- active-layer armour
- subsurface grading
- long-term DEM evolution
- rainfall-driven catchment simulation
- vegetation effect

## 실제 구현 확인

### 유동
- LISFLOOD-FP 기반 reduced shallow-water 2D hydrodynamics
- raster DEM
- divergent/convergent flow
- catchment mode에서 rainfall forcing

### 수문
- catchment mode runoff generation은 TOPMODEL adaptation
- 핵심 m parameter가 hydrograph peak/duration을 제어
- 현재 공개 documentation에서 vegetation effect는 m 값 및 별도 vegetation parameterization으로 단순화

### sediment / armour
- 최대 9개 grain-size classes
- suspended load + bedload
- Einstein-Brown 또는 Wilcock-Crowe transport
- surface + multiple active/subsurface layers
- surface D50 출력
- grain-size thickness를 surface 및 아래 여러 layer에 저장
- bed armouring과 제한적 stratigraphy 발달 가능
- erosion/deposition으로 DEM 갱신

### vegetation
공개 documentation의 vegetation tab:
- vegetation maturity 0-1
- growth/maturity rate
- vegetation critical shear
- mature vegetation에서 허용되는 erosion proportion

중요:
- vegetation은 특정 PFT, root biomass, RLD, litter mass를 직접 사용하지 않음
- LPJ-GUESS quantitative vegetation state와 직접 호환되는 published interface가 아님
- root-controlled detachment resistance model이 내부에 없음

### 시간 규모
공식 배포 설명상 hours to thousands of years.

### 공개 코드
- SourceForge에서 executable/source 제공
- Zenodo에 CAESAR-Lisflood 1.9b source archive 존재
- SourceForge project는 2026-03-11에도 업데이트 기록

## 고운사 적합성 판정

| 조건 | 판정 | 이유 |
|---|---|---|
| 2D surface flow | O | LISFLOOD-FP |
| rainfall catchment forcing | O | TOPMODEL catchment mode |
| multiclass sediment | O | up to 9 fractions |
| dynamic armour | O | active-layer grading/armouring |
| subsurface grading | O | multiple sediment layers |
| DEM evolution | O | erosion/deposition morphology |
| 100 yr simulation | O | LEM timescale 충분 |
| steep/mountain precedent | O | mountainous applications 존재 |
| postfire-specific erosion | △ | 직접 postfire root/litter model 아님 |
| quantitative root biomass | X | 없음 |
| quantitative litter mass | X | 없음 |
| PFT-specific vegetation | X | 없음 |
| shallow-soil stony Richards hydrology | X | TOPMODEL 기반 |

## 중요한 장점
Iber+와 SSSPAM을 억지로 연결하지 않아도:
- multiclass sediment
- surface armour
- subsurface sediment layers
- long-term topographic change
를 하나의 기존 model lineage에서 처리할 수 있다는 점은 매우 큼.

## 중요한 단점
고운사의 핵심 연구질문인:
```
LPJ-GUESS root/litter state
 -> erosion resistance
 -> postfire recovery
```
를 기존 CAESAR-Lisflood 내부 vegetation formulation이 직접 해결하지 못함.

또 catchment hydrology가 TOPMODEL 기반이라:
- shallow stony soil
- embedded rock fragments
- explicit theta-h-K
를 직접 모의하지 않는다.

## 최종 판정
**강력한 단일 geomorphic-engine 후보이지만, 고운사 전체 production model로는 현재 조건부 후보.**

특히:
- armour/profile/DEM 쪽은 SSSPAM 계보와 직접 비교할 가치가 매우 높음
- vegetation/root coupling과 stony-soil hydrology에서는 부족

따라서 현재 단계에서:
- 채택 아님
- 탈락도 아님
- **single-engine comparator / strong armour-profile candidate**

## 추가 확인 필요
1. active-layer vertical bookkeeping이 SSSPAM/mARM보다 고운사 embedded gravel에 더 적합한지
2. catchment-mode hillslope erosion에서 rainfall detachment 자체를 계산하는지, 또는 주로 runoff-driven sediment transport인지
3. vegetation erosion suppression을 root/litter state로 바꾸는 기존 산림 extension이 있는지

## 2026-09-22 공식문서 재감사

### hillslope soil erosion
CAESAR-Lisflood 공식 Tab Parameters 문서는 slope-process의 `Soil erosion rate`를 **USLE-type adaptation**으로 설명한다.

핵심:
- slope length는 drainage area의 제곱근으로 근사
- slope와 일련의 계수로 erosion 계산
- 공식 문서가 `no suggested values`라고 명시
- field data에 대해 calibrated/tested되지 않았다고 명시
- saturation `j_mean`에 따라 soil erosion rate를 바꾸는 기능도 experimental/untested

따라서 이 항은 고운사의 process-based rainfall/rill erosion 핵심식으로 사용할 수 없다.

### vegetation
공식 vegetation tab에서 vegetation maturity 0-1, vegetation critical shear, mature vegetation에서 허용되는 erosion proportion을 사용한다.
그러나 문서상 이 vegetation parameterization은 주로 **in-channel lateral erosion과 bank/lateral erosion**을 제한한다.
고운사 hillslope의 root biomass/RLD/litter-controlled detachment를 직접 계산하는 모듈이 아니다.

### active layers
공식 grainfilemaker는 사용자 지정 grain distributions와 **10개 active layers** 생성 기능을 제공한다. 따라서 depth-resolved grain storage는 실재 기능이다.

### 재판정
- multiclass/active-layer/long-term morphology: 강함
- 2D flow: 강함
- hillslope rainfall/interrill/rill process physics: 부적합
- quantitative forest vegetation: 부적합

**고운사 hillslope water-erosion 핵심모델 후보에서는 제외.**
장기 multiclass morphodynamics/armour 비교모델로만 유지.
