# 서지정보
Druhan, J. L., & Bouchez, J. (2024). Ecological regulation of chemical weathering recorded in rivers. *Earth and Planetary Science Letters, 641*, 118800. DOI: 10.1016/j.epsl.2024.118800.

# 이 논문을 찾은 이유
균근을 제외한 상태에서 vegetation을 chemical-weathering theory에 직접 넣는 published framework가 있는지, 특히 root water uptake와 nutrient uptake/recycling이 reaction timescale과 solute chemistry를 어떻게 바꾸는지 확인하기 위해 검토했다.

# 연구 유형
- predictive analytical / theoretical model
- ecological reactive-transport framework
- concentration-discharge theory

# 공간 구조
- weathering profile
- root-water/nutrient uptake zone
- subsurface storage-to-stream export

full 2D hillslope geometry는 아니지만 root-controlled hydrology and chemistry를 advection-reaction framework에 직접 넣는다.

# 적용 환경
- generalized terrestrial weathering systems
- river/catchment solute export

# 핵심 과정
- root water uptake
- evapotranspiration
- fluid drainage rate
- reaction timescale
- mineral weathering
- root nutrient uptake
- nutrient discrimination
- litter return / resolubilization
- concentration-discharge relation

# 식생 입력
핵심 ecological states/processes:
- plant water demand / root water uptake
- nutrient demand
- species-specific enrichment, passive uptake, or discrimination against dissolved solutes
- litter return to topsoil

No mycorrhiza is required.

# 핵심 구조

## 1. water uptake pathway
```
root water uptake
 -> lower area-normalized drainage
 -> altered fluid residence / reaction timescale
 -> altered water-rock reaction
 -> solute concentration/export
```

Thus vegetation can modify chemical weathering even without changing intrinsic mineral kinetic constants.

## 2. nutrient uptake pathway
Plants may:
- enrich/select a solute
- passively admit it
- discriminate against it

depending on ecological demand.

```
root nutrient uptake
 -> pore-water solute concentration
 -> plant biomass
 -> litter
 -> topsoil return / partial resolubilization
```

Therefore nutrient uptake is not simply a permanent dissolved-mass loss from the Critical Zone.

## 3. sign of vegetation effect
The model demonstrates ecosystems can both:
```
accelerate
OR
impede
```
water-rock reactions across the weathering profile.

This occurs because plants simultaneously modify:
- water flux
- reaction timescale
- solute removal
- nutrient recycling

# 핵심 식
The paper derives a vegetation-regulated solution of the advection-reaction equation.

The exact full closed-form equation was not reproduced here because accessible metadata/abstract did not expose the complete typeset derivation.

The process structure is confirmed:
```
advection-reaction
+ root water uptake
+ solute/nutrient uptake
+ litter recycling boundary condition
```

Before code implementation, obtain the final article equation set directly and map symbols/units.

# 파라미터와 단위
Required state classes:
- fluid drainage / discharge
- evapotranspiration / root water uptake
- reaction timescale
- solute concentration
- nutrient uptake/selectivity
- litter return

Exact parameter symbols and units require final equation audit before implementation.

# 원 논문의 구현 범위
A generalized theoretical weathering/river-chemistry model.

It is not:
- a 2D evolving hillslope model
- a sandstone-specific reaction network
- a forest succession model

# 고운사에 직접 사용할 수 있는 부분
**매우 강한 vegetation-weathering interface precedent.**

Current Gounsa variables map conceptually:

```
LPJ-GUESS root water uptake
 -> effective drainage / residence time

LPJ-GUESS nutrient demand/uptake
 -> solution nutrient sink

LPJ-GUESS litter turnover
 -> topsoil nutrient return

mineral weathering
 -> nutrient release
 -> LPJ-GUESS-CNP
```

This directly supports the intended two-way nutrient feedback without needing mycorrhiza.

# hillslope extension
Druhan-Bouchez itself is not spatial hillslope topography.

Combine structurally with:
- Anderson 2018
- Xiao 2021
- Stolze 2026
- BioRT

as:

```
topographic flow paths
+
vegetation-regulated root uptake
+
advection-reaction chemistry
```

This combined implementation is a **NEW COUPLING**.

# 새로운 coupling이 필요한 부분
- LPJ-GUESS root uptake to spatial drainage field
- LPJ-GUESS P/CNP demand to solute selectivity/uptake
- litter return to reactive topsoil pool
- 2D hillslope transport and residence-time field

# 한계
- no explicit hillslope geometry
- no dynamic vegetation internally
- no soil-production/front-advance equation
- no sandstone-specific mineral kinetics

# 최종 판정
- **핵심 채택: non-mycorrhizal ecological regulation of chemical weathering**
- B-WITCH와 함께 vegetation interface 핵심 이론근거
- especially strong for root water uptake + nutrient uptake/recycling
- WITCH/BioRT/PFLOTRAN chemistry에 붙이는 spatial implementation은 NEW COUPLING

# 참고 링크 / DOI
https://doi.org/10.1016/j.epsl.2024.118800
