# LORICA–TREED v1.1 formula audit and patch scope

Date: 2026-11-14  
Base commit: `af56a11c84553f741e7f670442e612ecc2594719`  
Base run: [GitHub Actions #5](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/43598845216)

## Findings verified against the extracted source and run configuration

### Correct algebra retained
- Hwang et al. (2015), Eq. (5): the implementation converts root carbon to dry root biomass using (f_C=0.47), then calculates (C_r=K T_r B_r/\rho_r). The unit conversions are internally consistent.
- Claessens et al. (2007), Eqs. (1)–(4): the factor-of-safety and steady-state critical-rainfall expressions match the source formulation. Do not alter the trigonometric term in the critical-rainfall bracket.

### Confirmed source defects
1. **Cell-specific erodibility is applied one cell late in the daily erosion loop.**  
   `calculate_water_ero_sed_daily()` calls `calculate_sediment_dynamics()` before assigning the current cell's `K_fac[row,col]` to the scalar `erodibility_value_m`. The assignment occurs after the cell's routing/erosion work. The first cell therefore uses the prior scalar and subsequent cells use the previous cell's K. The v1.0 5×5 test masked this because it set every K value to (10^{-6}).
2. **The configured scalar K is not used as a fallback.**  
   `advection_erodibility` is read from the UI, while `K_fac` is zero-initialized and has no population path in the extracted source. The 30-year runner manually set both `K_fac` and `erodibility_value_m` to (10^{-6}), bypassing the production parameter path.
3. **Daily vegetation protection ignores the configured scalar.**  
   The daily equation uses `bio_protection[row_sd,col_sd]`, but the array is zero-initialized and has no population path in the extracted source. The UI value is overwritten during routing and is not used by the daily branch. The v1.0 test explicitly set both the array and scalar to zero.
4. **The annual erosion diagnostic is not a sediment-volume total.**  
   `water_erosion_sum_m` is produced by `SumAbs(dz_ero_m)`: the sum of absolute cellwise thickness changes, without cell-area weighting. `landslide_initiations` counts initiating cells, not distinct landslide events.

### Hydraulic and soil-property issues requiring a separate parameterization decision
- The active Wösten PTF uses (0.03252 S); the published equation uses (0.0352 S). The active transmissivity routine also passes the topsoil indicator as 1 for every soil layer. Wösten et al. explicitly caution against applying the PTF outside Europe, so it is not a validated Korean forest-soil Ksat model.
- A Saxton–Rawls Ksat function with a coarse-fragment correction exists in the source but is not called by the active `update_Ks` / transmissivity path. It must be audited before activation.
- `treed_paw_mm()` calculates fine-earth available water and multiplies by full layer thickness without the Saxton–Rawls bulk-soil gravel-volume correction (PAW_b=PAW(1-R_v)).
- The implemented `1.33 + 0.33 \times clay\%` soil-cohesion expression is not the multivariable PTF in Khaboushan et al. (2018), Table 4. That PTF requires clay, coarse sand and very fine sand. The current texture classes do not resolve the latter two variables, so the published PTF cannot be copied directly.
- The soil-depth convention in the Claessens cohesion term needs a final check: transmissivity converts layer thickness with (cos\theta), whereas the cohesion normalization uses uncorrected `soildepth_m`.

## v1.1 patch scope
- Resolve K at the actual source cell for every sediment-capacity calculation.
- Use the UI-configured K when no positive cell-specific K is present.
- Preserve the UI vegetation-protection coefficient separately and use it when no positive cell coefficient is present.
- Apply the existing exponential vegetation-protection term to the current cell's FPC.
- Add unit tests for scalar fallback, cell override, FPC=0 and FPC=1.
- Keep the v1.0 30-year controlled baseline at K=(10^{-6}) and vegetation-protection coefficient 0. This preserves the previous baseline; the new unit test independently checks the active FPC formula.

The v1.1 patch deliberately does **not** change the Ksat PTF, soil-cohesion PTF, soil-depth convention, or annual runoff-to-sediment time aggregation. Those require a documented parameterization decision and independent tests rather than an unverified substitution.
