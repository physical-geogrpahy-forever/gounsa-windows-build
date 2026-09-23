# Verbruggen et al. 2025 - LPJ-GUESS-RE v1.0

## Bibliography

Verbruggen, W., Wårlind, D., Horion, S., Meunier, F., Verbeeck, H., Wieckowski, A., Tagesson, T., & Schurgers, G. (2025). Implementing a process-based representation of soil water movement in a second-generation dynamic vegetation model: application to dryland ecosystems (LPJ-GUESS-RE v1.0). *Geoscientific Model Development, 18*, 6623-6645. https://doi.org/10.5194/gmd-18-6623-2025

## Why searched

고운사에서 LPJ-GUESS를 사용할 때 얕은 토심, 기반암 경계, 다층 soil water, 침식 후 토심 변화가 실제로 표현 가능한지 확인하기 위해 검토했다.

## Study type

LPJ-GUESS hydrology model development and evaluation.

## Spatial structure

LPJ-GUESS grid cell - stand - patch - cohort/PFT 구조를 유지한다. 논문의 soil hydrology는 각 patch의 1-D vertical soil column이다. lateral hillslope routing은 제공하지 않는다.

## Applied environment

Sudan-Sahel drylands and Dahra flux-tower site. 고운사와 기후환경은 다르므로 검증결과를 직접 이전하지 않고 model architecture를 이용한다.

## Core processes

- LPJ-GUESS v4.1 baseline
- 15 soil layers
- individually adjustable layer thickness
- 1-D Richards equation
- mass-conservative soil-water movement
- explicit soil water content, water potential and hydraulic conductivity by layer
- plant uptake from multiple soil layers
- free drainage, impermeable bedrock, aquifer bottom boundary conditions
- adaptive sub-daily ODE solver inside a daily LPJ time step

## Vegetation inputs

Plant transpiration depends on layer soil water, PFT root fraction, patch water demand, cohort water stress, FPC and PFT `emax`.

Vertical root distribution follows a PFT-specific cumulative root function. Critically, if the cumulative root fraction has not reached 1 at the bottom of the simulated soil, the missing fraction is assigned to the bottom layer.

## Key equations/processes

Water-potential form of the 1-D Richards equation is used with plant uptake as a sink. Layer water flux is based on water-potential gradients plus gravity. The bedrock lower boundary sets bottom flux to zero.

## Parameters and units relevant to Gounsa

- soil layer thickness `Delta z`: m
- volumetric water content `theta`: m3 m-3
- soil water potential `psi`: m
- hydraulic conductivity `K`: m s-1
- transpiration sink by layer: expressed from water uptake, with daily LPJ coupling
- PFT root distribution parameter

## What can be used for Gounsa

1. Variable soil depth rather than fixed 1.5 m.
2. Impermeable bedrock lower boundary appropriate as a first-order representation for shallow soil above sandstone.
3. Layer-specific water state required for post-erosion remapping.
4. Sub-daily internal hydrological integration while vegetation remains on its native daily/annual clocks.
5. A direct architectural basis for `soil depth -> vegetation water stress -> succession` feedback.

## Required new coupling

The paper does not erode soil layers dynamically. Gounsa therefore needs a new coupling that changes layer geometry after erosion/deposition and conservatively remaps water, soil C/N and roots.

For erosion-generated shallow soil, the native rule that places otherwise unrepresented root fraction in the bottom layer must not be interpreted as physical survival of roots. Roots occupying removed soil volume must be removed first, with surviving root mass then remapped.

## Limitations

- 1-D vertical hydrology, no explicit hillslope lateral flow.
- Tested primarily in drylands rather than humid temperate mountain forest.
- Bedrock sensitivity was not the main evaluation target.
- Root distribution is parameterized rather than a mechanically explicit root architecture.
- Does not include geomorphic soil removal/deposition.

## Final decision

**ACCEPTED AS THE SOIL-HYDROLOGY BASE FOR THE FIRST LPJ-GUESS GOUNSA IMPLEMENTATION.**

Use for variable soil depth, layer water state and bedrock boundary. Couple to an external event hydrology/geomorphology engine during storms. Do not claim that LPJ-GUESS-RE itself is a hillslope erosion model.
