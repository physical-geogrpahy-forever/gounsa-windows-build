# 결정: 매립 석력이 많은 고운사에서는 published model chain으로 처리한다

날짜: 2026-09-22

## 현장 전제
고운사 토양에는 매립 석력이 많다.

## 결정 원칙
자의적 경험계수나 임의 함수식을 새로 만들지 않는다.

금지:
```
K_eff = K_fine * fitted_armour_factor
soil_water = soil_water * arbitrary_stone_factor
erosion = erosion * custom_armour_factor
```

허용:
- 기존 published model의 원식 그대로 사용
- 모델 사이에서는 동일한 물리량과 단위를 전달
- site parameter는 현장측정 또는 문헌범위로 제약
- 연결 자체가 기존 단일 published model이 아니면 명시적으로 `새로운 coupling`이라고 기록

## 1. 매립 석력의 수문
### 기본 선택: GEM
Naseri et al. 2020의 General Effective Medium theory를 우선한다.

입력:
- volumetric rock-fragment fraction
- fine-earth hydraulic conductivity
- rock-fragment hydraulic conductivity
- fragment shape/orientation
- matric potential

출력:
- effective hydraulic conductivity K(h)

채택 이유:
- high volumetric rock-fragment content를 명시적으로 목표로 함
- fragment interaction을 고려
- permeable/impermeable rock fragments 모두 가능
- 산지/산림 stony soil에 적합
- arbitrary scalar multiplier가 아님

### soil water retention
Naseri et al. 2023의 published volume-mixing framework를 사용한다.

```
theta_mix(h)
= (1-f) theta_soil(h)
+ f theta_rock(h)
```

RF water storage를 무시할 수 있을 때만 nonporous simplification을 쓴다.

## 2. surface stone / partially embedded stone
### EUROSEM
EUROSEM의 published rock-fragment terms를 사용한다.

```
B_roc = B (1 - ROC)
DET_pav = DET (1 - PAVE)
```

surface-seal condition에서 infiltration-reducing:
```
K_s,roc = K_s (1 - PAVE)
```

surface resting / infiltration-enhancing condition:
```
K_s,roc = K_s (1 + PAVE)
```

단, `embedded`라는 말만으로 ISTONE을 정하지 않는다.
surface seal, structural porosity/macroporosity와 fragment position을 함께 판정한다.

## 3. 2D runoff / erosion / sediment movement
### 기본 engine: Iber+ 2024
Iber+는:
- genuine 2D SWE
- rainfall-driven / flow-driven erosion 분리
- multiclass sediment
- loose sediment layer
- shielding factor
- size-specific suspended load / bed load
- hiding effect
- 2D Exner update
를 이미 published implementation으로 제공한다.

따라서 고운사에서는 새 2D erosion equation을 만들지 않는다.

## 4. dynamic armour
Iber+의 multiclass loose-sediment mass conservation과 size-specific transport를 최대한 그대로 사용한다.

관측/보조근거:
- Rieke-Zapp et al. 2007: fines removal -> fragment exposure -> armour
- Poesen 1987: size-dependent coarse-fragment rill transport
- Li et al. 2022: fragment size-dependent erosion effect
- Pala et al. 2025: fire-spall fragmentation lowers later mobility threshold

현재 남은 문제는 fire-spall-generated coarse fragments를 Iber+의 sediment classes/loose layer로 초기화할 수 있는 범위를 원 구현과 대조하는 것이다.
원 구현 밖의 별도 non-erodible armour coefficient는 만들지 않는다.

## 5. vegetation/root/litter
기존 결정 유지:
- LPJ-GUESS provides quantitative PFT/cohort state
- WEPP published root/residue modifiers는 erosion-resistance 근거
- Liu et al. litter equations/experiments는 litter detachment/transport 근거

다만 Iber+에 직접 전달하는 parameter mapping은 반드시 published-variable equivalence가 확인된 경우만 허용한다.
새 fitted biomass coefficient를 만들지 않는다.

## 모델 선택 요약
```
LPJ-GUESS
   |
   | soil/root/litter state
   v
[stony-soil hydraulic properties]
GEM 2020 + Naseri 2023
   |
   | K(h), theta(h), Ksat, moisture state
   v
Iber+ 2024
   |
   | genuine 2D runoff
   | multiclass erosion/transport
   | loose-layer shielding
   v
soil depth / sediment redistribution

surface stone/seal special case:
EUROSEM ROC/PAVE/ISTONE published relations
```

## 중요한 의미
이 구조에서 새로 만드는 것은 **경험식**이 아니라 software coupling이다.
각 process equation은 기존 문헌/모델에서 가져오고, 모델 사이에 전달되는 것은 동일한 물리상태량이다.

## 탈락/후순위
### full EUROSEM
- stony soil에는 매우 강함
- 하지만 genuine 2D가 아니므로 전체 engine으로는 탈락

### KINEROS2
- volumetric Rock와 Pave를 이미 가짐
- 그러나 1D/tree-like routing이며 현재 요구의 genuine 2D를 만족하지 않음
- EUROSEM의 stoniness formulation과 계보상 중복

### OpenLISEM
- current 2D/event/postfire precedent 강함
- stone cover input은 확인되지만 stoniness가 주로 splash detachment에 작용하고 high-volume embedded-rock hydraulic property model은 아님
- production main engine보다 benchmark/postfire comparison으로 유지

### Ma & Shao NDPM
- stony-soil infiltration에는 강함
- erosion/2D engine이 아니므로 GEM sensitivity/benchmark로 유지

## 아직 확인할 사항
1. Iber+ original-soil / loose-layer sediment classes에 coarse fire-spall class를 넣을 때 원 논문 범위를 벗어나지 않는지 source/testcase 수준 재검증
2. Iber+ Green-Ampt 등 infiltration input에 GEM-derived effective properties를 전달하는 가장 직접적인 published implementation 경로
3. sandstone fragment 자체의 K(h), theta(h) 측정 또는 sandstone-specific literature
4. fire severity -> spall mass/size distribution의 정량 published model
5. LPJ-GUESS soil-water module에 effective WRC/HCC를 넣는 방식에서 기존 기능을 우선 탐색
