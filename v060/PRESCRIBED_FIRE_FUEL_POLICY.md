# v0.60 prescribed-fuel BLAZE experiment policy

## Decision

The 2025 fire experiment may use a prescribed, literature-based pre-fire surface fuel load when the fire stage is reached. This is an explicit experimental input, not a reconstruction of native LPJ-GUESS fuel.

Scenario label: `PRESCRIBED_FUEL_BLAZE`

## Default prescribed fuel

Use a single Korean mixed-forest surface-fuel reference value:

- dry surface fuel load: **9.17 t ha-1**
- source: Won, M.S., Koo, K.S., Lee, M.B., Lee, S.Y. (2006), *Fuel Type Classification and Fuel Loading in Central Interior, Korea: Uiseong-Gun*, USDA Forest Service RMRS-P-41, pp. 305-319.
- Won et al. report shrub-layer-and-below fuel loads of 7.64 t ha-1 (Pinus densiflora pure), 10.99 t ha-1 (pine middle stratum), 8.62 t ha-1 (pine substratum), 9.17 t ha-1 (mixed forest), and 1.01 t ha-1 (broadleaf forest). The 9.17 t ha-1 mixed-forest value is adopted as the uniform default rather than fitting fuel to the 2025 fire outcome.

For conversion to LPJ-GUESS carbon units, use a **0.45 dry-mass carbon fraction**. This is consistent with Korean Pinus densiflora forest-floor observations summarized by Lee et al. (2019): Namsan 8.10 t ha-1 litter and 3.65 t C ha-1, Seosan 13.38 t ha-1 and 6.02 t C ha-1, Uljin 20.04 t ha-1 and 9.02 t C ha-1 (approximately 45% carbon).

Therefore:

- prescribed fuel carbon = 9.17 t ha-1 × 0.45 = **4.1265 t C ha-1**
- 1 t ha-1 = 100 g m-2
- prescribed fuel carbon = **412.65 g C m-2**

The prescribed value is a **pre-combustion surface-fuel carbon state**, not an `AvailFuelCat0` target. It must be presented to BLAZE as fuel state and BLAZE must calculate available fuel using its native combustion fractions. If represented entirely in the native fine surface litter category, the native category-0 litter combustion fraction 0.6 gives a nominal available-fuel contribution of **247.59 g C m-2**, above the unchanged native `MIN_FUEL = 200 g C m-2` gate.

## What remains unchanged

Do **not** alter any of the following to make the fire run:

- BLAZE `MIN_FUEL = 200 g C m-2`
- native `available_fuel()` equations
- fireline-intensity equations
- FFDI/weather calculations
- combustion fractions
- mortality/survival equations or coefficients
- LPJ-GUESS vegetation/hydrology equations
- same-day lateral run-on routing
- COPLAS/SIBERIA process equations
- physical DEM-update policy
- 3D mortality rendering logic

The prescribed fuel must not be tuned to reproduce the observed 49.57% crown-fire fraction, 97% fire-affected fraction, or any other post-fire aggregate statistic.

## Interpretation

Results from this branch must be described as a **prescribed-fuel BLAZE experiment**. They are not evidence that native LPJ-GUESS reproduced the actual 2025 pre-fire fuel load. The earlier native-fuel audit remains diagnostic/preliminary and is not overwritten by this experiment.

## Execution order

The prescribed fuel is introduced only at the scheduled 2025 fire stage. The v0.60 backbone validation remains otherwise unchanged:

1. per-cell CF forcing
2. native multi-cell restart
3. 3-cell restart regression
4. 4,454-cell day-1 regression
5. DOY147 same-day routing/process closure
6. 2022 365-day lockstep run
7. 2025 scheduled-fire experiment with `PRESCRIBED_FUEL_BLAZE`
8. mortality-to-3D output

## References

Won, M.S., Koo, K.S., Lee, M.B., Lee, S.Y. 2006. Fuel Type Classification and Fuel Loading in Central Interior, Korea: Uiseong-Gun. In: Andrews, P.L.; Butler, B.W., comps. *Fuels Management—How to Measure Success: Conference Proceedings*. USDA Forest Service RMRS-P-41, 305-319.

Lee, S.-H. et al. 2019. Valuation of ecosystem services in the organic carbon of the Pinus densiflora forest at Mt. Namsan, Seoul Metropolitan City. *Journal of Ecology and Environment* 43. https://doi.org/10.1186/s41610-019-0136-1
