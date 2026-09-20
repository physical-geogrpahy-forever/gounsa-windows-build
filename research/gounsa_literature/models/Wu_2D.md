# Wu 2D erosion lineage

## 핵심 문헌
- Wu et al. (2020), Journal of Hydrology 580, 124346, DOI 10.1016/j.jhydrol.2019.124346
- Wu & Chen (2020), Water Resources Research 56, e2020WR027768, DOI 10.1029/2020WR027768

## 고운사에서 검토한 이유
genuine 2D surface flow에서 interrill과 rill을 명시적으로 분리하고 WEPP/Foster-style erosion equations를 사용할 수 있는 엔진을 찾기 위해 검토했다.

## Wu et al. 2020
- 2D diffusion-wave runoff
- 2D sediment continuity
- rill/interrill spatial mask
- modified WEPP equations

Sediment continuity:
```
∂(hc)/∂t + ∂(qx c)/∂x + ∂(qy c)/∂y
= μ D_i + (1-μ) D_r
```

Interrill:
```
D_i = K_i p R I_f F_nozzle
```

Rill:
```
D_r = K_r(τ-τ_c)(1-G/T_c)
```

## Wu & Chen 2020
- representative rill geometry evolves
- width/depth/orientation/density/number change
- not a fully emergent branching/merging raster network

## vegetation
No dynamic vegetation/root-biomass module.

## 고운사에 쓸 수 있는 부분
- genuine 2D erosion skeleton
- explicit interrill/rill process separation
- `K_i, K_r, τ_c` interfaces structurally compatible with WEPP lineage

## 중요한 제한
This chat already settled that repeating “Wu vs WEPP” is unnecessary. Wu is the 2D-engine lineage; WEPP is the quantitative vegetation-erodibility lineage.

## 새로운 coupling
WEPP/Mao/LPJ-GUESS root-dependent `K_i/K_r` values supplied to Wu are **새로운 coupling**. Do not describe this as an existing published Wu feature.

## 최종 판정
**2D engine candidate / skeleton.**
