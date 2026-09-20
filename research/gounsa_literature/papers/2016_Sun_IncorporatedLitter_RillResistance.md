# 서지정보
Sun, L., Zhang, G.-H., Liu, F., & Luan, L.-L. (2016). *Effects of incorporated plant litter on soil resistance to flowing water erosion in the Loess Plateau of China*. Biosystems Engineering, 147, 238-247. DOI: 10.1016/j.biosystemseng.2016.04.017.

# 이 논문을 찾은 이유
litter biomass를 surface cover로 변환하지 않고 질량 자체로 rill detachment resistance에 직접 연결할 수 있는 published quantitative relation이 있는지 확인하기 위해 검토했다.

# 연구 유형
- hydraulic-flume experiment
- empirical process parameterization
- numerical erosion model 자체는 아님

# 공간 구조
- undisturbed soil samples
- overland-flow scour tests

# 적용 환경
- Loess Plateau
- plant-litter-incorporated topsoil
- natural vegetation restoration context

# 핵심 과정
- soil detachment capacity
- rill erodibility Kr
- critical shear stress tau_c
- litter-soil mechanical reinforcement

# 식생 입력
- incorporated litter mass rate [kg m^-2]
- litter species
- litter fragment morphology

# 핵심 식
Verified relationships:
- soil detachment capacity decreases exponentially with incorporated litter rate
- rill erodibility `K_r` decreases exponentially with incorporated litter rate
- critical shear stress generally increases with litter incorporation rate
- protection shows a threshold near 0.35 kg m^-2 in the tested soils

# 파라미터와 단위
- litter incorporation rate: kg m^-2
- Kr: s m^-1
- tau_c: Pa
Exact regression coefficients must be retrieved from the full paper before implementation.

# 원 논문의 구현 범위
Direct physical tests of litter mass incorporated in topsoil on detachment resistance.

# 고운사에 직접 사용할 수 있는 부분
Important evidence that **buried/incorporated litter can modify Kr and tau_c directly without converting litter mass to surface cover**.

This provides a possible bridge:
```
incorporated litter mass
 -> Kr modifier / tau_c modifier
```

# 새로운 coupling이 필요한 부분
LPJ-GUESS litter pools must be partitioned into:
- exposed surface litter
- incorporated/buried litter

Using the experimental regression in a 2D erosion engine is a **new coupling**.

# 한계
- experiment, not a full numerical model
- Loess Plateau soils
- litter species-specific morphology
- cannot be applied to exposed surface litter

# 최종 판정
- **채택: direct litter-mass -> concentrated-flow soil-resistance evidence**
- candidate parameterization source for buried litter
- not the surface-litter/interrill solution

# 참고 링크 / DOI
https://doi.org/10.1016/j.biosystemseng.2016.04.017
