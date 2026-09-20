# 서지정보
Waldmann, D. (2010). *Large-Scale Process-Oriented Modelling of Soil Erosion by Water in Complex Watersheds*. Dissertation, Ludwig-Maximilians-Universität München. DOI: 10.5282/edoc.11575.

관련 논문: Waldmann, D., & Mauser, W., *Large-scale modelling of soil erosion by water and potential Global Change impacts in the Upper Danube basin*. 정확한 journal/proceedings 서지는 원문 재검증 필요.

# 이 논문을 찾은 이유
PROMET/DANUBIA 계보에서 dynamic vegetation model이 root length density를 erosion resistance에 실제로 전달하는지, 특히 root state에서 critical hydraulic threshold까지 이어지는 numerical implementation이 있는지 확인하기 위해 검토했다.

# 연구 유형
- process-oriented distributed numerical model
- dissertation/model development

# 공간 구조
- PROMET proxel grid, Upper Danube basin
- erosion component spatial resolution 약 1 km2
- temporal resolution 1 h
- 각 proxel sediment/runoff를 channel network로 전달
- genuine 2D shallow-water surface routing은 아님

# 적용 환경
- Upper Danube basin
- Alpine/mountain watershed 포함

# 핵심 과정
- rainfall/runoff erosion
- distributed hydrology
- dynamic vegetation/root development
- soil shear strength
- critical runoff shear stress
- sediment delivery to channel network
- freeze-thaw modification

# 식생 입력
PROMET biological module dynamically computes:
```
root biomass growth
 -> root length increment
 -> soil-layer root allocation
 -> RLD
 -> root senescence/update
```

The erosion module then uses RLD to modify soil cohesion/root reinforcement.

# 핵심 식과 연결

The exact importance of this thesis is the implemented chain:

```
dynamic RLD
 -> root-reinforced effective soil cohesion
 -> soil shear strength sigma_s
 -> runoff critical shear stress tau_c
```

The root effect follows the Gyssels/De Baets exponential-reduction/root-reinforcement lineage rather than a cover-only formulation.

For the shear-strength to erosion-threshold step, Waldmann applies Léonard & Richard (2004):

```
tau_c = beta * sigma_s
```

with:
```
beta = 2.6e-4
```

The dissertation limits soil shear strength to a maximum of 20 kPa before this conversion.

Critically, the resulting `tau_c` values were still much larger than the erosion-resistance magnitude used for the target model calibration. Waldmann therefore multiplied the resulting `tau_c` by:

```
0.0005
```

to bring it into the empirical erosion-resistance range.

This 0.0005 is a **model-specific calibration**, not a transferable physical constant.

The model also uses a freeze-thaw multiplication factor:
```
f_ft = 0.65
```
under its chosen parameterisation.

# 파라미터와 단위
- RLD: root length density
- effective cohesion / soil shear strength
- `tau_c`: critical shear stress [Pa]
- `beta = 2.6e-4`: Léonard & Richard lineage conversion used by Waldmann
- maximum soil shear strength before conversion: 20 kPa
- final 0.0005 factor: model-specific calibration, **do not transfer**

# 원 논문의 구현 범위
This is an actual numerical implementation of:
```
dynamic vegetation
 -> RLD
 -> mechanical erosion resistance
 -> critical runoff threshold
```

That is substantially stronger than merely reporting a field correlation.

# 고운사에 직접 사용할 수 있는 부분
This closes an important **structural** bridge:

```
LPJ-GUESS FineRootC
 -> RLD
 -> erosion-specific cohesion/soil strength
 -> tau_c
```

It is especially useful if the final 2D erosion closure has a native critical-shear-stress parameter.

# 새로운 coupling이 필요한 부분
1. LPJ-GUESS FineRootC -> RLD remains a new coupling requiring PFT/root-trait conversion.
2. Applying Waldmann/PROMET root reinforcement to SWEHR, SERGHEI-SE or Iber+ is a new coupling.
3. `tau_c -> SWEHR UC` is **not solved** here because SWEHR uses critical stream power, not simply critical shear stress.
4. Waldmann's 0.0005 calibration factor must not be copied to Gounsa.

# 한계
- not genuine 2D surface flow
- 1 km2 proxel scale
- channel-delivery structure differs from local hillslope routing
- the final critical-shear magnitude required empirical rescaling
- therefore this is a structural precedent, not a plug-and-play parameterization

# 최종 판정
**채택: dynamic RLD -> soil strength -> critical-shear numerical precedent.**

This materially strengthens the case for a `tau_c`-native erosion closure, but does not establish a universal RLD -> Hairsine-Rose `J` or `UC` equation.

# 참고 링크 / DOI
https://doi.org/10.5282/edoc.11575
