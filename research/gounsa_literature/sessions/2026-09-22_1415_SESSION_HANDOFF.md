# 2026-09-22 fire-spall / armour / vegetation feedback session handoff

## 이번 세션 목표
사용자가 제안한 다음 모델사슬의 문헌 가능성을 추가 조사했다.

```
fire -> fire spall -> armour -> erosion/hydrology
large spall -> weathering/fragmentation -> mobility/removal
roots + litter -> rill detachment resistance -> soil-depth conservation
soil depth + fragments + hydrology -> soil moisture -> understory
oak resprouting vs kudzu absence
```

## 새로 확인하고 저장한 핵심 논문
- 1987 Poesen: rill flow의 rock-fragment transport와 size-dependent mobility
- 1990 Poesen et al.: resting vs embedded fragments의 반대 hydrological effect
- 1990 Tsugawa et al.: kudzu prostrate stem/root network development
- 1994 Poesen et al.: rock-fragment erosion effects review
- 1995 Takahashi et al.: Mt. Rokko fire-disturbed eroded/compacted steep soil의 natural kudzu stands
- 1999 Susko et al.: kudzu germination, osmotic stress, burial-depth establishment filter
- 2001 Cerdà: surface fragments increase infiltration and strongly suppress interrill erosion
- 2007 Rieke-Zapp et al.: fines removal -> fragment exhumation -> dynamic surface armour -> rill suppression
- 2011 Hwang et al.: Korea postfire oak sprouting on poorly developed mountain soils
- 2012 Jomaa et al.: rock-fragment shielding + hydrology + size-selective erosion model
- 2016 Zhang et al.: rock-fragment hydrology review
- 2020 Kim et al.: 19-year Korean oak resprouting survival/competition
- 2021 Buckman et al.: sandstone wildfire spalling
- 2021 Shtober-Zisu & Wittenberg: 10-year postfire spall breakdown/pulverization and stoniness
- 2022 Li et al.: fragment-size-dependent runoff/soil-loss effect
- 2023 Kato-Noguchi: kudzu invasion/life-history review
- 2024 Huang et al.: rock-fragment content -> soil water -> species/root-trait interaction
- 2025 Pala et al.: thermal spalling fragments boulders and reduces subsequent mobility threshold
- 2026 Song et al.: slope-dependent rock-fragment erosion control

## 가장 중요한 판정 변화
### 1. armour hydrology
기존 단순가설:
`armour -> infiltration 감소`

폐기.

새 구조:
`infiltration = f(cover, size, embeddedness, sealing, soil, moisture, roots, slope)`

surface-resting fragments는 infiltration을 증가시킬 수 있고 embedded fragments는 반대효과가 가능하다.

### 2. fragmentation
기존 단순가설:
`large spall -> smaller -> armour 감소`

폐기.

새 구조:
```
large spall
 -> fragmentation
 -> smaller size class
 -> shielding efficiency 변화
 -> mobility threshold 변화
 -> actual transport/removal
 -> armour 변화
```

작은 fragments가 남아 있으면 오히려 shielding이 강할 수 있다.

### 3. dynamic armouring
Rieke-Zapp 2007에 따라:
```
fines removal -> fragment exhumation -> surface armour increase -> rill incision suppression
```
를 채택한다.

### 4. postfire spall evolution
Buckman 2021 + Pala 2025 + Shtober-Zisu 2021 + Poesen 1987을 연결하면:
```
fire spall production
 -> coarse fragments
 -> postfire breakdown
 -> smaller fragments
 -> size-specific rill/gravity transport
 -> armour gain/loss
```
의 문헌사슬이 성립한다.
각 연결은 하나의 published model이 아니라 새로운 coupling이다.

### 5. oak vs kudzu
`stony/poor soil -> kudzu exclusion`은 채택하지 않는다.

Takahashi 1995는 fire-disturbed, compacted, eroded, steep soil에도 kudzu stands가 성립함을 보여준다.

현재 가설:
```
prefire oak rootstock survival/resprouting
vs
kudzu prefire presence + seed propagule + clonal access + establishment
```
의 priority/disturbance legacy가 핵심이며 환경필터는 그 위에 작용한다.

## 새 모델/결정 파일
- models/Rock_Fragment_Armour.md
- decisions/2026-09-22_FIRE_SPALL_ARMOUR_HYDROLOGY.md

## MASTER 반영
MASTER에 dynamic armour, hydrology sign, size classes, postfire fragmentation/removal, vegetation bridge, oak-vs-kudzu 결론을 추가했다.

## 다음 조사 우선순위
1. 고운사와 유사한 sandstone의 wildfire spall mass/size production equation
2. sandstone postfire 1-100 year fragmentation rate
3. rock-fragment size-class별 entrainment law를 2D rill hydraulics와 연결할 published precedent
4. fragment architecture -> soil hydraulic parameters를 process-based하게 계산할 모델
5. 한국/동아시아 Quercus species-specific resprout traits와 root reserve
6. kudzu clonal spread/propagule limitation을 spatial vegetation model에 구현한 연구
