# 결정: fire-spall / armour / hydrology를 동적 size-class 구조로 처리한다

날짜: 2026-09-22

# 결정 내용
고운사 coarse-fragment module은 단일 고정 `armour fraction`을 사용하지 않는다.

최소한 다음을 분리한다.
- fragment size classes
- surface cover
- soil-matrix fragment content
- resting vs embedded state
- exposed fine-soil fraction
- mobile fragment pool

# 왜 결정했는가
문헌검토 결과 rock fragments는 동시에 다음 상반된 효과를 낼 수 있다.
1. soil detachment와 rill incision을 억제하는 shielding/roughness
2. 위치와 입도에 따라 infiltration을 증가 또는 감소시키는 hydrological effect
3. fines removal로 시간이 갈수록 armour가 강화되는 self-organization
4. weathering/fragmentation과 concentrated-flow entrainment로 armour가 제거되는 효과

따라서 단일 cover coefficient로 이들을 합치면 물리적 방향이 잘못될 수 있다.

# 핵심 근거
- Rieke-Zapp et al. 2007: fines removal -> fragment exhumation -> dynamic armour -> rill suppression
- Poesen et al. 1990: resting/embedded fragment가 infiltration에 반대효과
- Cerdà 2001: surface fragments가 infiltration 증가 및 erosion 감소
- Li et al. 2022: fragment size에 따라 runoff/soil-loss 효과가 달라짐
- Shtober-Zisu & Wittenberg 2021: postfire spalls의 10-year breakdown/pulverization
- Pala et al. 2025: thermal spalling이 boulder size를 줄여 mobilization threshold 감소
- Poesen 1987: rill flow에 의한 coarse-fragment transport
- Song et al. 2026: armour erosion-control efficiency의 slope dependence

# 산불 후 권장 순서
```
fire
 -> fire-spall production
 -> fragment size distribution
 -> surface/mobile coarse-fragment pools

fine-soil erosion
 -> fragment exhumation
 -> armour strengthening

postfire weathering
 -> size-class fragmentation

rill / gravity transport
 -> size-specific removal
 -> armour weakening
```

# 수문 규칙
`armour -> infiltration 감소`를 고정하지 않는다.

```
HydraulicModifier =
f(fragment cover,
  fragment size,
  resting/embedded position,
  fine-earth properties,
  sealing,
  antecedent moisture,
  roots/macropores,
  slope)
```

# 식생 feedback
```
soil depth
+ fine-earth fraction
+ rock-fragment architecture
+ hydraulic modifier
 -> soil moisture
 -> PFT establishment/growth
```
는 새로운 coupling이다.

# kudzu / oak 관련 추가 결정
현재 문헌상 `석력이 많고 토양이 불량해서 kudzu가 배제된다`는 설명은 채택하지 않는다.

근거:
- Takahashi et al. 1995: fire-disturbed Mt. Rokko의 compacted, eroded, steep-slope soil에서도 natural kudzu stands 성립
- Hwang et al. 2011, Kim et al. 2020: 한국 산불 후 oak는 pre-existing stump/root system의 resprouting으로 빠른 우위를 가짐
- Susko et al. 1999: kudzu seed-based establishment는 seed dormancy, water stress, burial depth에 민감
- Tsugawa et al. 1990: kudzu 확장은 prostrate stem/root network의 clonal process가 중요

따라서 고운사 하층식생/초기천이는:
```
environmental filter
+ prefire rootstock legacy
+ seed propagule availability
+ clonal access
+ resprouting ability
```
를 분리한다.

# 제외한 단순화
- armour cover 하나로 infiltration, detachment, transport를 동시에 조절
- fragment가 작아지면 자동으로 armour 감소
- poor/shallow/stony soil이면 kudzu 자동 배제
- 모든 postfire vegetation을 seed-based establishment로 동일 처리

# 아직 해결되지 않은 문제
- 고운사 사암의 burn-severity -> spall mass/size distribution 정량식
- postfire sandstone fragmentation rate
- size-class별 entrainment parameter의 고운사 보정
- fine-earth volume과 fragment architecture를 LPJ-GUESS soil hydraulic parameter로 변환하는 방식
- 현장 oak rootstock / kudzu propagule 상태의 초기화
