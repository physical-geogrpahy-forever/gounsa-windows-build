# LORICA–TREED v0.9: rainfall-triggered shallow-landslide audit

v0.9 moves from the v0.8 C# → Julia → C# data roundtrip to the first process-level test of the existing LORICA shallow-landslide module with TREED root reinforcement.

## What the source audit established

The v0.5 LORICA source already contains a rainfall-triggered shallow-landslide routine:

- calculate_critical_rain() calculates a steady-state critical rainfall raster from local slope, upslope contributing area, soil transmissivity, saturated bulk density, peak friction angle, soil cohesion, and the TREED root-cohesion raster.
- calc_soil_cohesion_factor() adds root cohesion to soil cohesion and normalizes it by soil depth and saturated overburden.
- calculate_slide_new() compares event rainfall intensity with critical rainfall, erodes the soil profile, routes failed material downslope, deposits it where topography permits, and updates soil depth and DEM.
- The failure calculation uses an eight-neighbour steepest-descent slope. The separate minimum_slope_for_movement_tan parameter (default 0.7) controls movement/continuation/deposition; it is not the same thing as the texture-derived peak friction angle.
- The existing runout_ratio (default 0.4) controls travel distance relative to eroded vertical thickness.

## Three defects corrected in v0.9

1. **Zero critical-rainfall trigger:** LORICA assigns crrain_m_d = 0 to unconditionally unstable cells, but the initiation condition previously required crrain_m_d > 0. Such cells were therefore excluded from failure. The condition now accepts crrain_m_d >= 0 while still excluding negative NoData values.
2. **Rainfall time-series order:** the annual rainfall record was being updated in the geomorphic section after the same year's daily water balance. v0.9 updates the annual total and rain_m raster at the beginning of each timestep, before daily weather preparation, TREED, and LORICA hydrology.
3. **Root-cohesion diagnostic reset:** calc_and_write_ls_rasters() previously allocated a fresh zero-valued root-cohesion array before writing diagnostics. It now preserves the TREED-provided raster and only allocates it if missing or dimensionally inconsistent.

## Explicit event rainfall

The original LORICA setting remains available:

- landslide_event_mode=legacy_fraction_annual: event intensity is the selected fraction of annual rainfall, preserving the original interface.

A new optional mode is available:

- landslide_event_mode=explicit_event
- landslide_event_rainfall_mm=<event depth>
- landslide_event_duration_h=<duration, 0–24 h>

The mean event intensity is converted to m/day and compared with LORICA's existing crrain_m_d steady-state threshold. For example, 60 mm over 6 hours is 10 mm/h, or 0.24 m/day.

**Important process limitation:** this is an event-intensity forcing for the existing steady-state critical-rainfall stability calculation. It is not a transient pore-pressure or Richards-equation landslide model; the duration is used to calculate mean event intensity, not to simulate within-event pressure propagation. The existing daily water balance still runs, but its dynamic water storage is not yet passed into the landslide factor-of-safety calculation.

## v0.9 process-level CI

The Windows CI extracts the exact v0.5 source bundle, applies the v0.9 patch, compiles the actual LORICA C# project, and executes a synthetic 1-D slope test with:
- 1 m soil depth and 10 m grid spacing;
- a 45-degree upper slope transitioning to a depositional footslope;
- the same soil profile and event rainfall (60 mm / 6 h) across root-cohesion cases;
- 0, 4.3, and 7.6 kPa root-cohesion inputs.

The test checks:
- the zero-threshold unstable case initiates;
- intermediate root cohesion produces a finite critical rainfall and event-triggered failure;
- higher root cohesion stabilizes the same synthetic slope;
- soil depth and DEM change when failure occurs;
- soil mass plus transported mass closes;
- diagnostic output preserves the TREED root-cohesion raster;
- annual rainfall time-series values are updated before hydrology.

This is a process-kernel test, not yet a 30-year catchment simulation or field validation.

## What remains before a 30-year landscape-evolution run

- Run the 1-D/2-D synthetic slope test and inspect erosion, deposition, and mass closure.
- Verify that annual TREED root biomass changes are passed to the same year's landslide calculation.
- Check the daily water-balance / event-intensity consistency and the assumption of steady-state transmissivity.
- Run a small 2-D multi-year case with water erosion and landsliding enabled, then expand to 30 years only after state and mass closure pass.
- Keep the inverse-calibrated Tr_eff fixed across all scenarios; do not recalibrate it separately by year or scenario.

No taproot geometry, fire module, or unverified root architecture is introduced in v0.9. Root reinforcement remains based on TREED area-normalized fine + coarse root biomass and the Hwang et al. (2015) biomass-to-cohesion relationship.
