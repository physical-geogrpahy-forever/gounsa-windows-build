# 서지정보
De Baets, S., Denbigh, T. D. G., Smyth, K. M., Eldridge, B. M., Weldon, L., Higgins, B., Matyjaszkiewicz, A., Meersmans, J., Larson, E. R., Chenchiah, I. V., Liverpool, T. B., Quine, T. A., & Grierson, C. S. (2020). *Micro-scale interactions between Arabidopsis root hairs and soil particles influence soil erosion*. Communications Biology, 3, 164. DOI: 10.1038/s42003-020-0886-4.

# 이 논문을 찾은 이유
RLD와 root micro-traits를 직접 soil cohesion field로 변환하고, hydraulic shear와 비교하여 erosion을 계산하는 mechanistic model이 존재하는지 확인하기 위해 검토했다.

# 연구 유형
- controlled root-trait experiment
- concentrated-flow erosion experiment
- mechanistic soil-mechanics erosion model

# 공간 구조
- soil-root block
- spatially heterogeneous root-reinforced cohesion
- full hillslope/catchment 2D routing model은 아님

# 적용 환경
- Arabidopsis thaliana
- clay-loam soil
- 28-degree water-flume erosion
- shear stresses approximately 13-24 Pa

# 핵심 과정
- overland-flow shear
- root-soil cohesion
- erosion threshold
- root-hair reinforcement
- root-architecture spatial heterogeneity

# 식생 입력
- true root length density RLD_T
- root-system geometry
- rooting depth
- root-hair phenotype/micro-trait parameters

# 핵심 식
EUROSEM-based back-calculation of soil cohesion:
```
C = (-1/0.85) ln(beta/0.79)
```

Mechanical erosion condition is represented by a Coulomb-type criterion:
```
tau = -mu N + c
```

Root-reinforced cohesion depends directly on RLD.

Maximum:
```
c_Max = c_Bare [1 + gamma(RLD_T) R]
```

Minimum:
```
c_Min = c_Bare [1 + gamma(RLD_T) r]
```

Saturating RLD effect:
```
gamma(x) = M_max tanh(M1 x / M_max)
```

Cohesion varies spatially between c_Min and c_Max according to root architecture. Erosion occurs where hydraulic shear exceeds local root-reinforced soil resistance.

# 파라미터와 단위
- RLD: km m^-3
- soil/root cohesion: kPa
- hydraulic shear: Pa
- root-system geometry/depth: mm in experiment
- gamma: mm^-1
- M1, Mmax: root-trait reinforcement parameters

Measured root-reinforcement regressions were approximately:
- wild type: 1.23 ln(RLD+1), R2=0.70
- hairless mutant: 0.50 ln(RLD+1), R2=0.40
- hair-overproducing mutant: 0.86 ln(RLD+1), R2=0.51

At RLD around 19 km m^-3, inferred cohesion increases were approximately 3.7, 1.5, and 2.6 kPa for the respective phenotypes.

# 원 논문의 구현 범위
The model integrates:
```
flow shear
+ root architecture
+ RLD
+ spatially varying cohesion
+ erosion/debris entrainment
```

Experimental erosion decreases exponentially with RLD at lower root densities, then can saturate depending on root-hair traits.

# 고운사에 직접 사용할 수 있는 부분
This is a major mechanistic bridge for:
```
LPJ-GUESS-derived RLD
 -> root-specific cohesion field
 -> hydraulic erosion threshold
```

It gives a mechanistic reason to let roots influence an erosion-threshold/cohesion term, not only erodibility Kr/Kd.

# 새로운 coupling이 필요한 부분
- LPJ-GUESS FineRootC -> RLD
- forest PFT root traits -> M1/Mmax or equivalent cohesion-response parameters
- applying this local soil mechanics model inside a catchment-scale 2D HR/Iber solver
are all **new couplings**.

# 한계
- Arabidopsis, not forest species
- local flume block, not a distributed landscape engine
- root-hair parameter values are not transferable to Gounsa
- this model addresses concentrated-flow/shear resistance, not rainfall splash shielding

# 최종 판정
- **채택: mechanistic RLD -> erosion-specific cohesion/threshold precedent**
- not a final 2D engine
- high-value candidate for the root-resistance interface

# 참고 링크 / DOI
https://doi.org/10.1038/s42003-020-0886-4
