# BRIF (Wang et al. 2025) vs public HFDM-GPU CUDA source original audit

## Identity
Article DOI https://doi.org/10.1029/2024EA004076, author Wang/Ouyang/An et al., *Earth and Space Science* 12(7) 2025. Paper data-access links https://github.com/chinafl/HFDM-GPU and https://doi.org/10.5281/zenodo.15613301.

## Exact functional source files in public repo
- README says HFDM high-performance CUDA C++ flood dynamic model; no sediment erosion architecture.
- `test/wind_cuda.cu` blob `4c4d756f3aba141cb03f3ae451d792ba5fd5f500`: allocations for canopy states `V_LAI`, `V_Smax`, `V_K` and per-class storage functions `0.1713*LAI`, `0.59*LAI^0.88` and attenuation `1-exp(-Cover*LAI)`; `test/windmath_cuda.cuh` blob `69444df5ac1438bf60d4c4104f1d326a6d58ceb4`: kernel `Diff_interception` and `Diff_infiltration` declared; `test/main.cu` uses CUDA-based flood data workflow. LAI scientific importance is actual model parameter.
- **Whole source NOT public:** exact /test listing has eight source/test files; no `windmath_cuda.cu` CUDA kernel definitions, `hfdm` at top level is binary (not UTF8 source). Paper shares **part of core code** and data, not full solver. No native end-to-end rebuild/run verified in this audit.
- No sediment transport/detachment/deposition/morphodynamics solver in enumerated public test source, nor erosion validation in original paper.

## Actually published scientific runs
Local-inertial approximated 2D flood solver, NOT full SWE; V-catchment1m, forested Cutou catchment2.5m with 6.32 million active cells, Heishuigou8m. UAV 0.3m DEM is a **survey input**, not computing mesh. Table1 forest LAI10 crown density0.8, grass LAI2 crown0.05, but these are literature/land-use class parameters, not the user's 5cm mapped individual canopy data.

## Verdict
**Reject as Gounsa all-physics original**: a genuine steep-mountain, vegetation interception and two-directional hydrodynamic published model with partial public CUDA source, but **not 5–10cm, no sediment, no full editable code**. Do not promote flood warning model as an erosion model by analogy.
