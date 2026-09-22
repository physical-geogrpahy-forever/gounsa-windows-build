# 서지정보
Morgan, R. P. C., Quinton, J. N., Smith, R. E., Govers, G., Poesen, J. W. A., Auerswald, K., Chisci, G., Torri, D., & Styczen, M. E. (1998). The European Soil Erosion Model (EUROSEM): A dynamic approach for predicting sediment transport from fields and small catchments. *Earth Surface Processes and Landforms, 23*(6), 527-544. https://doi.org/10.1002/(SICI)1096-9837(199806)23:6<527::AID-ESP868>3.0.CO;2-5

# 이 논문을 찾은 이유
고운사에서 많은 매립 석력과 표면 armour가 infiltration, runoff, splash, rill/interrill erosion을 동시에 바꿀 때, 이를 하나의 published erosion model 안에서 자의적 추가식 없이 처리할 수 있는 모델을 찾기 위해 검토했다.

# 연구 유형
- physically based distributed event erosion model
- 수치모델

# 공간 구조
- distributed cascading plane/channel elements
- interrill/rill explicit
- genuine 2D SWE는 아님

# 적용 환경
- fields
- small catchments
- stony soil 적용 가능

# 핵심 과정
- rainfall interception
- infiltration
- Hortonian runoff
- interrill flow
- rill flow
- raindrop detachment
- flow detachment
- transport capacity
- deposition
- stoniness

# 식생 입력
- vegetation cover
- plant height
- basal area
- canopy/interception parameters
- root-reinforced cohesion 입력 가능
- quantitative root biomass model은 아님

# 핵심 식
EUROSEM은 KINEROS 계열 infiltration에서 rock fragments를 다음처럼 처리한다.

토양체적 내부의 석력:
```
B_roc = B (1 - ROC)
```

- ROC: soil volume 중 rock-fragment fraction [0-1]

surface/partially embedded stone이 saturated hydraulic conductivity에 미치는 효과:
```
K_s,roc = K_s (1 - PAVE)
```
for the infiltration-reducing condition,

```
K_s,roc = K_s (1 + PAVE)
```
for the infiltration-enhancing condition.

- PAVE: surface non-erodible/rock-fragment cover [0-1]
- ISTONE: 어느 방향을 사용할지 결정

raindrop detachment shielding:
```
DET_pav = DET (1 - PAVE)
```

# 파라미터와 단위
- ROC: volumetric fraction [-]
- PAVE: areal surface fraction [-]
- ISTONE: +1/-1
- K_s: saturated hydraulic conductivity
- B: saturation deficit/capillary-drive related infiltration parameter
- Manning n
- soil cohesion
- detachability
- D50

# 원 논문의 구현 범위
EUROSEM은 rock fragments의 세 효과를 모델 내부에서 명시적으로 분리한다.
1. soil pore-water storage 감소: ROC
2. exposed fine-earth area 감소: PAVE
3. saturated hydraulic conductivity 변화: PAVE + ISTONE

동시에 rill/interrill erosion, runoff, transport/deposition을 event scale에서 계산한다.

# 고운사에 직접 사용할 수 있는 부분
- 매립 석력의 체적비를 ROC로 직접 넣을 수 있음
- 표면 armour를 PAVE로 별도 처리 가능
- 매립/표면 위치에 따른 infiltration effect 방향을 ISTONE으로 분리 가능
- PAVE가 splash detachment를 줄이는 식이 이미 published model 안에 존재
- 자의적 rock-fragment erosion coefficient를 새로 만들 필요가 없음

# 새로운 coupling이 필요한 부분
- LPJ-GUESS PFT/root/litter를 EUROSEM 식생입력으로 바꾸는 단계
- fire-spall 생산과 ROC/PAVE 시간변화를 갱신하는 장기 coupling
- genuine 2D flow engine과 결합할 경우 그 결합 자체는 새로운 coupling

# 한계
- event model
- plane/channel network이며 genuine 2D SWE가 아님
- ROC/PAVE/ISTONE은 event 동안 동적 coarse-fragment evolution을 계산하지 않음
- high-stoniness unsaturated hydraulic conductivity 전체 곡선을 직접 계산하는 현대 stony-soil physics model은 아님

# 최종 판정
- 핵심 채택: rock-fragment hydrology/erosion interface의 기존 published model
- 전체 최종 엔진으로는 2D 제약 때문에 보류

# 참고 링크 / DOI
https://doi.org/10.1002/(SICI)1096-9837(199806)23:6<527::AID-ESP868>3.0.CO;2-5
