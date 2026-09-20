# SERGHEI-SE lineage

## 핵심 문헌
- Martínez-Aranda et al. (2025 preprint), *SERGHEI-SE: An Open-Source High-Performance-Computing Model for Soil Erosion and Sediment Transport Processes in Catchments*
- Martínez-Aranda et al. (2026 preprint), *An open-source High-Performance-Computing physics-based model for high-resolution soil erosion simulation*
- Braga, Martínez-Aranda & García-Navarro (2026), Water 18(15), 1870, DOI 10.3390/w18151870
- Caviedes-Voullième et al. (2023), SERGHEI-SWE v1.0, Geoscientific Model Development 16, 977-1008

## 고운사에서 검토한 이유
latest open-source high-performance genuine 2D catchment-scale erosion framework.

## 공간구조
- 2D shallow-water equations
- 2D solid transport
- finite volume
- bed evolution
- HPC/high-resolution catchment computation
- Cartesian distributed grids
- MPI domain decomposition
- Kokkos performance portability

## vegetation
The original SERGHEI-SE description uses a modification factor accounting for:
- vegetation protection
- land management
- bedrock exposure

The demonstrated factor was derived from Sentinel-2 information.

Dynamic root biomass/RLD is not a core erosion-resistance state.

The 2026 evaluation likewise does not solve the quantitative root/litter-state gap.

## erosion structure
SERGHEI-SE couples:
- 2D shallow-water runoff
- 2D depth-averaged solid transport
- bed erosion/deposition
- bed-elevation update

The 2026 evaluation includes calibration-sensitive erosion/deposition coefficients `alpha_e` and `alpha_d`, sediment transport capacity and a critical shear stress based on the Shields criterion.

The SEHS closure includes rainfall-induced and runoff-induced erosion components.

## 강점
- genuine 2D
- conservation-oriented finite-volume formulation
- catchment-scale HPC
- explicit surface evolution
- UWBU bed-update scheme designed to suppress non-physical oscillation
- open-source project and test infrastructure
- performance portability beyond Nvidia-only CUDA

## 한계
- quantitative root/litter state missing
- root recovery after wildfire not represented mechanistically
- published vegetation factor is not equivalent to LPJ-GUESS root/litter state
- not specifically validated against steep postfire TLS erosion in the McGuire 2016 sense

## 고운사에 쓸 수 있는 부분
Modern 2D-engine comparison and implementation architecture.

## 새로운 coupling
LPJ-GUESS root/litter states linked to erosion parameters are **new coupling**.

---

## 2026-09-21 source-code accessibility audit

### public repository and license
SERGHEI is publicly hosted at:
`https://gitlab.com/serghei-model/serghei`

The project and papers identify a:
- 3-clause BSD license
- public Git repository
- developer/user wiki
- public test-suite group

The 2026 SERGHEI-SE evaluation explicitly states that the SERGHEI-SE model used in the paper is available from the same GitLab repository under the 3-clause BSD license.

This is a fundamentally different accessibility situation from Iber+.

### source architecture
The verified SERGHEI implementation is:
- C++
- Kokkos-based
- MPI domain-decomposed
- designed around spatial arrays for conserved variables, parameters and forcing data
- compiled across multiple backends

The SERGHEI-SWE paper explicitly describes Kokkos `View`-derived arrays as the storage for spatially distributed:
- conserved variables
- model parameters
- forcing data

and cell kernels are implemented with `Kokkos::parallel_for`.

Thus the software architecture is intrinsically compatible with distributed cell-wise parameter/state fields.

### hardware portability
The public project has evolved beyond the original CUDA/OpenMP combination.
Current project history documents support or development for:
- OpenMP
- CUDA
- HIP
- SYCL

This avoids the Nvidia-only lock-in of Iber+.

### test infrastructure
A separate public `serghei-tests` group contains:
- analytical SWE cases
- laboratory/experimental cases
- field cases
- sediment-transport test cases
- continuous-integration reference solutions

This is a major advantage for modifying an erosion closure while checking regressions.

### coupling significance for Gounsa
At software-architecture level, a plausible path is:

```
LPJ-GUESS state
   -> spatial parameter/state array
   -> SERGHEI-SE erosion closure
   -> Kokkos cell kernels
```

Unlike Iber+, we can legally and technically modify the public code base.

However, this does **not** mean a published root/litter coupling already exists.

Still unresolved:
- which SEHS parameter is the most defensible receiver for root reinforcement
- whether root effect should enter `alpha_e`, a threshold term, or another resistance state
- how surface litter should enter rainfall detachment without collapsing it to cover
- postfire loose-layer memory and shielding are not yet demonstrated to match Hairsine-Rose/SWEHR structure

### source extensibility judgment
- public source accessibility: **very strong**
- license permissiveness: **very strong**
- HPC architecture: **very strong**
- spatial-field infrastructure: **strong**
- existing root/litter quantitative coupling: **absent**
- postfire process match: **weaker than SWEHR**
- modification effort: **larger conceptual erosion-closure work than SWEHR, but much safer software base than Iber+**

## 현재 판정
**SERGHEI-SE is promoted from a secondary comparison model to a serious implementation candidate.**

The source audit produces a three-way distinction:

```
SWEHR
= strongest postfire/process match + simplest inspected coupling hooks

SERGHEI-SE
= strongest open-source modern HPC/software architecture

Iber+
= very strong numerical/HPC erosion engine, but public source access is the practical blocker
```

Final engine selection still depends on the root-resistance and exposed-litter interfaces.
