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
No dynamic root biomass/RLD erosion-resistance formulation was found in the 2024 erosion paper.

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

---

## 2026-09-21 source-code accessibility audit

### 구현 언어와 계산구조
Iber+ is a reimplementation of Iber in:
- C++
- Nvidia CUDA
- OpenMP for shared-memory CPU parallelism

The erosion implementation keeps most computation on the GPU and minimises CPU-GPU transfers.

### 공개성 재검토
This changes the practical judgment for Gounsa.

The 2024 erosion paper states that the software and test cases are openly available, but the permanent research-data deposit actually distributes:
- Iber+ executables V3.2b for Windows/Linux
- test cases and associated data

It does **not** distribute the C++/CUDA source code.

An independent 2024 NHESS paper using Iber+ states explicitly that:
- the open-source code is accessible only to collaborators
- a compiled Iber+ executable is freely downloadable by general users

Therefore:

```
free software download != public source-code access
```

For Gounsa, where the erosion resistance fields must be updated from LPJ-GUESS during a long simulation, this distinction is decisive.

### consequence for root/litter coupling
The mathematical interface remains attractive:

```
FineRootC / RLD -> K_d or tau_s
SurfaceLitter   -> alpha_d / rainfall protection / roughness
```

but without public source access we cannot presently verify or implement:
- whether `K_d,k`, `alpha_d,k`, `tau_s` are runtime cell-wise arrays in the distributed executable
- where these values are stored on GPU
- whether an external state can update them every event/year without recompiling
- whether a dynamic LPJ-GUESS coupling can be inserted into the public distribution

This is materially worse than SWEHR, whose erosion-resistance arrays and equations were directly inspected in public GPL C source.

### source extensibility judgment
- equations/process structure: **strong**
- GPU engineering: **very strong**
- general executable availability: **strong**
- public source-code accessibility for independent modification: **weak / not verified for general users**
- immediate LPJ-GUESS coupling feasibility: **inferior to SWEHR unless source access is obtained from the Iber team**

### evidence
- Cea et al. 2024: DOI 10.1016/j.envsoft.2024.106098
- Research Data Gouv dataset: DOI 10.57745/UFEK4L, title `Iber+ executables (V3.2b)`
- NHESS 2024, 24, 609: code availability statement says source access is restricted to collaborators while executable is freely available

## 현재 판정
**process-level top candidate, but no longer a first-choice implementation base under the current public-source constraint.**

If direct collaborator/source access is later obtained, Iber+ should be re-evaluated immediately because its numerical/HPC architecture remains stronger than SWEHR in several respects.
