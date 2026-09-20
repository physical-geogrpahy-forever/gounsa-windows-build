# Iber+ multiclass erosion lineage

## 핵심 문헌
Cea, García-Feal, Nord, Piton & Legoût (2024). Environmental Modelling & Software 179, 106098. DOI 10.1016/j.envsoft.2024.106098.

## 고운사에서 검토한 이유
modern GPU finite-volume genuine 2D erosion engine that separates rainfall-driven and flow-driven detachment.

## 공간구조
- 2D shallow-water equations
- fully distributed finite volume
- GPU/HPC
- plot to meso-scale catchment

## erosion structure
```
∂(h C_k)/∂t + ∂(q_x C_k)/∂x + ∂(q_y C_k)/∂y
= D_rdd,k + D_rdrd,k + D_fdd,k + D_fdrd,k + D_dep,k
```

Rainfall-driven:
```
D_rdd,k = α_d,k r (1-ε) f_d g_k
```

Flow-driven:
```
D_fdd,k = K_d,k max(τ-τ_s,0)(1-ε)g_k
```

## vegetation
No dynamic root biomass/RLD erosion-resistance formulation was found in this chat.

## critical connection
`K_d` has units kg s^-1 N^-1 and a Foster-style shear-excess form closely comparable to WEPP `K_r`.

This makes Iber+ a mathematically clean target for a root-dependent flow-erodibility coupling, but that coupling is **not already implemented in the 2024 paper**.

## 고운사에 쓸 수 있는 부분
- modern genuine 2D hydraulics
- rainfall vs flow detachment separation
- multiclass sediment
- loose-layer shielding
- Exner morphology

## 새로운 coupling
WEPP/Mao/PROMET/LPJ-GUESS vegetation-state effects supplied to `K_d` or `α_d` are **새로운 coupling**.

## 최종 판정
**현재 핵심 2D-engine 후보 중 하나.**
