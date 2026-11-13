# LORICA–TREED v0.9: rainfall-triggered shallow-landslide audit

v0.9 extends the v0.8 C# → Julia → C# roundtrip test to a process-level test of LORICA's existing shallow-landslide module with TREED-derived root reinforcement.

## Source-level process corrections

The v0.5 LORICA source already contains a rainfall-triggered shallow-landslide routine:

- \`calculate_critical_rain()\` calculates a steady-state critical-rainfall raster from local slope, upslope contributing area, soil transmissivity, saturated bulk density, peak friction angle, soil cohesion, and the root-cohesion raster.
- \`calc_soil_cohesion_factor()\` adds root cohesion to soil cohesion and normalizes it by soil depth and saturated overburden.
- \`calculate_slide_new()\` compares event rainfall intensity with critical rainfall, erodes the soil profile, routes failed material downslope, deposits it where topography permits, and updates soil depth and DEM.
- Failure uses an eight-neighbour slope calculation. The separate \`minimum_slope_for_movement_tan\` parameter controls movement/continuation/deposition; it is not the same as the texture-derived peak friction angle.
- The \`runout_ratio\` parameter controls travel distance relative to eroded vertical thickness.

The v0.9 patch corrects five issues:

1. **Zero critical-rainfall trigger.** LORICA assigns \`crrain_m_d = 0\` to unconditionally unstable cells, but the previous initiation condition required \`crrain_m_d > 0\`. Those cells were excluded. The condition now accepts \`crrain_m_d >= 0\`, while negative NoData values remain excluded.
2. **Rainfall time-series order.** The annual rainfall record was updated in the geomorphic section after the same year's daily water balance. v0.9 updates the annual total and \`rain_m\` raster at the beginning of each timestep, before daily weather preparation, TREED, and LORICA hydrology.
3. **Root-cohesion diagnostic reset.** \`calc_and_write_ls_rasters()\` previously allocated a fresh zero-valued root-cohesion array before writing diagnostics. It now preserves the TREED-provided raster and allocates only when the array is missing or dimensionally inconsistent.
4. **Residual transport double subtraction.** The deposition routine had already removed the deposited fraction from transport arrays. The remaining arrays were then multiplied by the undeposited fraction again before routing, discarding part of the landslide mass. v0.9 routes the residual arrays directly by the downstream distribution fraction in both fully mixed and layer-preserving modes.
5. **Layer-preserving deposition under-withdrawal.** \`deposit_slid_mass_mm2()\` multiplied the global deposition fraction by a second coverage fraction based on the original template-layer thickness. When the remaining transported material was thinner than a template layer, material remained in transport even when the requested deposition fraction was 1. The revised routine derives each transported layer's available thickness from its actual mineral/SOM mass using LORICA's PTF, then withdraws the fraction required to satisfy the requested deposition depth. Source-layer indices are retained when the deposited layers are inserted into the receiving profile.

## Explicit event rainfall

The original LORICA setting remains available:

- \`landslide_event_mode=legacy_fraction_annual\`: event intensity is the selected fraction of annual rainfall, preserving the original interface.

The optional explicit-event mode is:

- \`landslide_event_mode=explicit_event\`
- \`landslide_event_rainfall_mm=<event depth>\`
- \`landslide_event_duration_h=<duration, 0–24 h>\`

Mean event intensity is converted to m/day and compared with LORICA's existing \`crrain_m_d\` threshold. For example, 60 mm over 6 hours is 10 mm/h, or 0.24 m/day.

**Process limitation:** this is event-intensity forcing for the existing steady-state critical-rainfall stability calculation. It is not a transient pore-pressure or Richards-equation landslide model. Event duration is used to calculate mean intensity, not to simulate within-event pressure propagation. Dynamic water storage from the daily water balance is not yet passed into the factor-of-safety calculation.

## Process-level Windows test

The CI extracts the exact v0.5 source bundle, applies the v0.9 patch, compiles the actual LORICA C# project, and executes a synthetic 1-D slope test.

- 5 cells, 10 m cell size, 1 m initial soil depth.
- Ten soil layers using the LORICA geometric layer template.
- Layer texture varies with depth, so the translation-mode test can distinguish source layers.
- PTF-consistent layer masses are generated using LORICA's own \`bulk_density_calc_kg_m3()\` function.
- A 45° upper slope transitions to a depositional footslope.
- Event rainfall is 60 mm / 6 h (10 mm/h = 0.24 m/day).
- Root-cohesion inputs are 0, 4.3, and 7.6 kPa.
- Both user-selectable mixing modes are tested: fully mixed (\`ls_mix_radio_1\`) and layer-preserving translation (\`ls_mix_radio_2\`). The third radio option is disabled in the source UI and is not included.

The process test checks:

- zero-threshold unstable cells initiate;
- intermediate root cohesion produces a finite critical rainfall and event-triggered failure;
- high root cohesion suppresses failure under the same event;
- soil depth and DEM change when failure occurs;
- soil mass plus transported mass closes to numerical tolerance;
- the no-slide case retains its PTF-consistent 1 m soil depth;
- the root-cohesion raster survives diagnostic output;
- annual rainfall is updated before hydrology;
- translation mode retains distinct source-layer composition and ordering at the receiving cells.

## Verified results

The latest completed run is GitHub Actions **#16**, commit \`1473f49e3bc0cfbcba64ff6607a32fa98d2b937e\`.

- Windows LORICA compilation: passed, 0 compiler errors.
- Existing v0.5 Python regression suite: passed.
- Six process cases: passed (three root-cohesion values × two mixing modes).
- Maximum relative mass-closure error: \(2.90 \times 10^{-16}\).
- Initial and final soil mass: approximately 802,959.539 kg in the 5-cell test domain.
- Residual transport mass after the event: 0 kg in all six cases.
- No-slide soil depth: 1.0000000000000002 m.
- Automated layer-order assertions: passed for the translation-mode test.

The first process run reported an 8.333% mass deficit. After correcting residual routing, a separate layer-preserving test exposed a 5.561% deficit caused by the second thickness-fraction scaling. Both corrections are now included in the audit branch and pass the ten-layer, depth-varying-texture test.

Detailed ledgers and the run-by-run diagnosis are in [MASS_BALANCE_AUDIT.md](MASS_BALANCE_AUDIT.md).


## Cross-timestep residual transport verification

The source audit found that the original annual reset cleared the fully mixed transport arrays, while the layer-preserving arrays survived without their runout state being reconstructed. A single-event mass balance therefore did not establish persistence into the next timestep.

v0.9 now uses the layer-resolved landslide arrays as landslide-only persistent storage for fully mixed residuals as well. At the beginning of the next landslide calculation, the stored mass is restored to the selected mixing mode and its runout thickness is reconstructed from the PTF-derived transported mass. This keeps the residual separate from the transient mixed arrays shared with water erosion.

GitHub Actions #27 tested both mixing modes through two successive events, explicitly calling LORICA's \`initialise_every()\` between them:

| Check | Fully mixed | Layer-preserving |
|---|---:|---:|
| Residual after event 1 | 1,252,616.880 kg | 1,252,553.992 kg |
| Residual after \`initialise_every()\` | unchanged | unchanged |
| Residual after event 2 | 1,179,501.647 kg | 1,179,316.162 kg |
| Event 2 deposition depth | 0.500 m | 0.500 m |
| Event 2 relative mass error | \(1.16\times10^{-16}\) | \(2.32\times10^{-16}\) |

This verifies persistence through the annual reset routine and remobilization/deposition in a second event in the synthetic closed-basin test. It does not yet execute the full water-erosion process between events or demonstrate multi-decadal catchment behavior.

## Scope boundary

This is a process-kernel verification on synthetic 1-D and 5×5 2-D terrain, including two sequential events with the annual reset routine between them. It is **not** a catchment validation, a 30-year landscape-evolution run, or field validation. It also does not validate the spatial accuracy of TREED root biomass or the Hwang et al. (2015) biomass-to-cohesion transfer for a specific site.

## Next verification stage

Before a 30-year run:

1. Run the 2-D multi-event test with the actual water-erosion routine enabled between landslide events, not only its annual reset routine.
2. Verify annual TREED root-biomass changes are passed into the same year's landslide calculation and that the persistent residual remains independent of water-erosion transport.
3. Test event rainfall together with the daily water-balance state and document the steady-state transmissivity assumption.
4. Run a short multi-year 2-D LORICA–TREED case; inspect DEM, soil mass, layer composition, root cohesion, and transport ledgers at every event.
5. Only then expand to the 30-year coupling audit.

No taproot geometry, fire module, or unverified root architecture is introduced in v0.9. Root reinforcement remains based on TREED area-normalized fine + coarse root biomass and the Hwang et al. (2015) biomass-to-cohesion relationship.
