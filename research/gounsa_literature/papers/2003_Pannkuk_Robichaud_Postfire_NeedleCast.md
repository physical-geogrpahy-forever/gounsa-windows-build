# 서지정보
Pannkuk, C. D., & Robichaud, P. R. (2003). *Effectiveness of needle cast at reducing erosion after forest fires*. Water Resources Research, 39(12), 1333. DOI: 10.1029/2003WR002318.

# 이 논문을 찾은 이유
surface litter mass를 cover로 바꾸는 식을 **실제 산불 후 급경사 산림 needle cast**에 적용하고, 그 cover가 rainfall-driven/interrill 및 concentrated-flow/rill erosion을 얼마나 줄이는지 직접 정량화한 연구가 있는지 확인하기 위해 검토했다.

# 연구 유형
- laboratory rainfall simulation
- postfire forest-soil erosion experiment
- empirical erosion-response parameterization

# 공간 구조
- 4 m long soil box
- 40% slope
- rain-only interrill phase
- rainfall + added inflow rill phase

# 적용 환경
- postfire conifer forest
- burned ponderosa pine and Douglas-fir needle cast
- granitic and volcanic burned forest soils
- steep 40% slope

# 핵심 과정
- litter mass -> ground cover
- raindrop/interrill protection
- rill erosion
- stream-power detachment
- flow obstruction and mini-debris dams
- sediment trapping

# 식생 입력
- Ponderosa pine needle mass
- Douglas-fir needle mass
- corresponding surface cover
- cover treatments 0, 15, 40, 70%

# 핵심 식

## 1. needle mass -> surface cover
The paper uses the standard saturating mass-cover relation of the Wischmeier/Gregory lineage:

```
C_lit = 1 - exp(-b_m M_lit)
```

with consistent units for `b_m` and `M_lit`.

The authors independently calibrated the mass-cover relation and obtained:
- ponderosa pine: `b_m = 0.0004` when mass is expressed in kg ha^-1
- Douglas fir: `b_m = 0.0006` when mass is expressed in kg ha^-1

R2:
- ponderosa pine: 0.97
- Douglas fir: 0.80

An earlier pine-needle coefficient cited by the paper was 0.00037 kg^-1 ha.

The difference between needle types demonstrates that litter geometry must be represented by a litter-type-specific coefficient.

## 2. interrill erosion protection
Normalized sediment delivery under rain-only conditions was fitted exponentially to surface cover.

The cover-effect exponent in the paper's surface-cover relation was:
- Douglas fir: 3.2
- ponderosa pine: 1.8

At 50% cover:
- Douglas-fir needles reduced interrill sediment delivery by about 80%
- ponderosa pine needles reduced it by about 60%

## 3. rill / stream-power erosion
Stream power was a better predictor of sediment load than shear stress in this experiment.

Normalized stream-power detachment rate declined exponentially with needle cover.

At 50% cover:
- ponderosa pine reduced stream-power detachment rate by about 40%
- Douglas fir reduced it by about 20%

The contrast is mechanistically important:
- short, straight Douglas-fir needles contact and shield the soil efficiently -> stronger interrill protection
- long, curved ponderosa needles form mini-debris dams -> relatively stronger rill-flow disruption

# 파라미터와 단위
- slope: 40%
- rainfall intensity: 34 mm h^-1
- inflow: 1.5, 2.4, 3.9 L min^-1
- litter cover: 0-70%
- mass-to-cover coefficient `b_m`: reported with mass in kg ha^-1

Unit conversion note:
if mass is instead represented as kg m^-2, the numerical coefficient must be converted consistently.

# 원 논문의 구현 범위
This paper directly establishes the chain:

```
postfire needle mass
 -> measured/calibrated surface cover
 -> interrill erosion reduction

postfire needle cover
 -> reduced stream-power detachment rate
 -> reduced rill erosion
```

This is much closer to Gounsa than agricultural crop-residue evidence alone.

# 고운사에 직접 사용할 수 있는 부분
The **functional architecture** is highly transferable:

```
SurfaceLitter mass by litter type
 -> C_lit
 -> rainfall-impact shielding
 -> flow-detachment modification
```

For conifer needle litter this is a direct postfire mountain/steep-slope precedent.

It also supports keeping litter morphology/type separate instead of using one universal litter coefficient.

# 새로운 coupling이 필요한 부분
Using these cover-response functions inside SWEHR is still a **new coupling**.

In particular, a proposed form such as:
```
E1_Gounsa = (1-H) * f_litter(C_lit) * P_k * ASMASK * R
```
would combine published SWEHR and published litter-cover functions, but this exact combined equation is not an existing SWEHR formulation.

For Korean forest litter, the Ponderosa/Douglas-fir coefficients must not be treated as universal. Broadleaf litter and local conifer litter need local or literature-specific `b_m`/protection values.

# 한계
- two conifer needle types
- laboratory soil boxes
- no dynamic decomposition
- cover was manually distributed uniformly
- coefficients depend strongly on litter morphology
- no LPJ-GUESS coupling in original study

# 최종 판정
- **핵심 채택: exposed postfire litter mass -> cover -> interrill/rill protection bridge**
- resolves much of the previous surface-litter interface problem at the functional-form level
- local litter-type parameterization remains required

# 참고 링크 / DOI
https://doi.org/10.1029/2003WR002318
