# 서지정보
Liu, J.-X., Li, P.-P., Liu, G.-B., & Flanagan, D. C. (2020). *Quantifying the effects of plant litter in the topsoil on the soil detachment process by overland flow in typical grasslands of the Loess Plateau, China*. Hydrological Processes, 34, 2076-2087. DOI: 10.1002/hyp.13713.

# 이 논문을 찾은 이유
incorporated litter의 질량뿐 아니라 형태량을 이용해 process-based erosion model의 Kr를 직접 조정할 수 있는 정량 predictor를 찾기 위해 검토했다.

# 연구 유형
- hydraulic-flume experiment
- process-parameter regression
- numerical model 자체는 아님

# 공간 구조
- topsoil samples
- six imposed shear-stress levels

# 적용 환경
- Loess Plateau grasslands
- four common plant-litter species

# 핵심 과정
- soil detachment capacity
- rill erodibility Kr
- critical shear stress tau_c
- litter-soil contact mechanics

# 식생 입력
Five incorporation rates:
- 0.1, 0.4, 0.7, 1.0, 1.3 kg m^-2

Litter morphology:
- tissue density
- length density
- litter surface area density, LSAD
- volume ratio

# 핵심 식
Measured ranges:
- Dc: 0.043-4.580 kg m^-2 s^-1
- Kr: 0.051-0.237 s m^-1
- tau_c: 2.02-6.83 Pa

Compared with bare control:
- Dc decreased 38-59%
- Kr decreased 32-46%
- tau_c increased 98-193%

Most important:
**LSAD explained litter effect on Kr strongly**
- R2 = 0.93
- NSE = 0.79

The authors explicitly propose LSAD for adjusting rill erodibility in process-based soil-erosion models.

# 파라미터와 단위
- litter mass: kg m^-2
- litter length density: km m^-3
- LSAD: m2 m^-3
- litter volume ratio: m3 m^-3
- Kr: s m^-1
- tau_c: Pa

# 원 논문의 구현 범위
Direct mechanistic experiment linking incorporated litter amount/morphology to concentrated-flow detachment resistance.

# 고운사에 직접 사용할 수 있는 부분
This is currently one of the strongest non-cover litter pathways:
```
incorporated litter mass and morphology
 -> LSAD
 -> Kr adjustment
```

It avoids forcing litter biomass into surface cover.

# 새로운 coupling이 필요한 부분
LPJ-GUESS litter mass does not provide fragment geometry/LSAD directly. Converting litter mass and PFT litter traits into LSAD is a **new coupling** unless an independent morphology model is found.

# 한계
- grassland litter
- Loess soil
- experiment, not a landscape model
- applies to litter incorporated into topsoil, not exposed forest-floor litter

# 최종 판정
- **strong candidate parameterization source for buried/incorporated litter**
- keep separate from exposed-surface litter effect

# 참고 링크 / DOI
https://doi.org/10.1002/hyp.13713
