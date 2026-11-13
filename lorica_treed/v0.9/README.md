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

The CI extracts the exact v0.5 source bundle, applies the v0.9 patch, compiles the actual LORICA C# project, and executes a 1-D slope suite plus 5×5 2-D convergent-basin tests.

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

The original one-year deterministic Windows integration gate was GitHub Actions **#77** ([run #77](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/43437639072)), commit `d468661dcc8a0af3d8d5b594001a0e7d763033d7`. It extracts the exact v0.5 source bundle, applies the v0.9 LORICA fixes and per-cell TREED ECA seed patch, compiles the actual C# project, and runs the TREED–LORICA landslide test.

- Windows LORICA compilation: passed.
- Existing v0.5 Python regression suite: passed.
- TREED Julia environment instantiation and module loading: passed.
- Actual TREED root-carbon, FPC, and LAI outputs were read by LORICA; the Hwang Eq. (5), FPC, and ET-factor transfer checks passed.
- Baseline and calibrated root-carbon rasters were byte-identical (SHA-256 `7c69e323337009fe53b247496ad679e3926a4c9ec8571df9fff463a19fdba17e`); mean root C was `1181.40304199 gC/m²`.
- The fixed event-scale effective tensile parameter was `Tr_eff = 1.09678319 MPa`, inverse-calibrated to mean root cohesion of 7.6 kPa. This is a calibration coefficient, not a measured root tensile strength.
- The actual spatial root-cohesion raster had mean 7.6000 kPa, minimum 7.5624 kPa, and maximum 7.7640 kPa.
- Under the same 60 mm / 6 h event, the TREED-root case produced 0 initiations and 0 m summed erosion; the paired bare-root case produced 24 initiations and 24 m summed erosion.
- Relative mass-closure error was 0 for the TREED-root case and `2.38 × 10⁻¹⁵` for the bare-root case.
- The root-cohesion sensitivity scenarios (0, 3.4, 7.6, 9.0, 9.1, 12.9, and 21.6 kPa) showed the expected threshold response: 24 initiations at 0 and 3.4 kPa, and 0 at 7.6 kPa or above.

### TREED ECA reproducibility

The #72 audit exposed a real thread-count dependence in the original ECA call: repeated runs were identical within each fixed thread count, but 1-thread and 4-thread runs produced different root-carbon rasters. The earlier CI-only serialization workaround was therefore superseded.

The v0.9 patch now derives a unique deterministic seed for each grid cell from the run seed and linear cell index, then passes it into `Metaheuristics.Options(seed=...)` for both `fixed_original` and `adaptive_experimental` root-allocation branches. The original `Threads.@threads` loop, ECA objective, iteration count, and TREED ecological equations are retained.

GitHub Actions #77 repeated the 5×5 run twice with 1 thread and twice with 4 threads:

- All 15 TREED output files were byte-identical within each thread count.
- All 15 TREED output files were also byte-identical between 1 and 4 threads.
- Maximum cellwise root-carbon difference across thread counts: **0 gC/m²**.
- Mean root carbon in all four runs: **1181.40304199 gC/m²**.

This establishes deterministic TREED output for the tested 5×5 case across the tested thread counts. It does not by itself establish cross-version or cross-platform bitwise reproducibility.

## Three-year coupling and zero-soil sensitivity (verified November 2026)

GitHub Actions [#85](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/43511920687) verified the 3-year 5×5 synthetic model and fixed the event initiation counter: count a newly initiated landslide only where the slide erodes positive soil thickness; reset event-local counters each year. Its outputs confirm 24 physically eroded cells and 21.226323 m summed erosion thickness in year 1, followed by **zero new landslide erosion** in years 2 and 3. The year-2 10.129850 m summed deposition uses the 1,481,588.137 kg persistent landslide mass from year 1. This is not a new failure event.

Inspection of `TREEDlocalstep.jl` and `TREED_physiological_functions.jl` shows that the local TREED habitat mask checks valid topography and air temperature but does **not** require positive soil depth. Water supply is based on precipitation plus a bounded PAW term; PAW=0 does not set the entire water supply to zero. Consequently the original TREED run still returns positive root carbon on zero-soil cells (16/25 cells at year-2 input; 12/25 at year-3 input). This does not prove plants cannot root in bedrock fractures; it identifies a missing explicit substrate constraint in the coupled experiment.

GitHub Actions **[#88](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/43524227105)**, source commit `9cc0909f3a457b05eb4519161cd74d637f3d3390`, passed a paired 3-year sensitivity run. The **default `treed_bare_bedrock_policy=legacy` remains unchanged**. The optional experimental `treed_bare_bedrock_policy=zero_coupling` sets only the LORICA-transferred effective root carbon and FPC to zero where LORICA's soil depth is at most 1e-6 m (an ASCII-output/numerical-zero tolerance); raw TREED biomass, trait state, ecological equations and optimization are not changed.

| Year | Variable | legacy | zero_coupling |
|---|---|---:|---:|
| 1 | Mean root cohesion (kPa) | 3.331109 | 3.331109 |
| 2 | Mean root cohesion (kPa) | 3.838615 | 1.382962 |
| 3 | Mean root cohesion (kPa) | 3.924336 | 2.042555 |
| 2 | Mean actual evapotranspiration (mm/year) | 421.997 | 435.610 |
| 3 | Mean actual evapotranspiration (mm/year) | 338.891 | 345.226 |
| 2 | Sum of directional overland-flow depths (m) | 4.052938 | 4.052938 |
| 3 | Sum of directional overland-flow depths (m) | 6.626288 | 6.626288 |
| 2–3 | New landslide initiation cells | 0 in each year | 0 in each year |

Raw TREED root-carbon rasters are unchanged across both modes for all three tested years, confirming this is a coupling-side mask rather than a TREED vegetation/mortality model. In both modes, the first-year run is identical and the second-year zero-soil outputs are masked in the sensitivity experiment. Maximum three-year test relative mass-closure discrepancy is 2.93e-7, below the CI criterion of 1e-6.

**Confirmed model limitation:** source audit of `LORICA/Functions/hydro.cs` shows `water_balance()` calls `dailyflow()` to compute and accumulate `OFy_m` from rainfall excess and topsoil `Ks` **before** the monthly `ET0_m × Ra_rcm × veg_correction_factor` and actual ET calculation. Therefore the FPC-dependent ET factor affects reported ET and the residual annual infiltration, but does not directly alter that same year's `dailyflow()` surface runoff. The identical runoff and water erosion in #88 are consistent with this process ordering and must not be misread as evidence that canopy/roots have no physical effect on runoff.

**Scientific scope:** #88 is a synthetic software integration and sensitivity test, not a field or catchment calibration. The zero-soil mode represents an explicit extreme end-member assumption about **local substrate support**, not an assertion that vegetation can never grow on exposed bedrock. TREED mortality, uprooting, succession on newly deposited soil, and intrastorm pore-pressure dynamics are not established by this test. A 30-year physically validated coupled run has not been completed.

## 2-D convergent hillslope and closed-sink tests

The process harness also tests a 5×5, 10 m-cell synthetic basin with eight failed source cells around an internal depression.

| Scenario | Mode | Initiations | Erosion thickness sum | Deposition thickness sum | Residual transport | Relative mass error |
|---|---|---:|---:|---:|---:|---:|
| Convergent basin | Fully mixed | 8 | 8.000 m | 8.785688 m | 0 kg | \(8.12\times10^{-16}\) |
| Convergent basin | Layer-preserving | 8 | 8.000 m | 8.788155 m | 0 kg | \(8.12\times10^{-16}\) |
| Closed sink, runout-limited | Fully mixed | 8 | 8.000 m | 0.219642 m | 1,252,616.880 kg | \(1.39\times10^{-15}\) |
| Closed sink, runout-limited | Layer-preserving | 8 | 8.000 m | 0.219704 m | 1,252,553.992 kg | \(1.33\times10^{-15}\) |

The convergent-basin cases route all material into the central depression. The closed-sink cases use a runout ratio of 20 so that only part of the material deposits during the event; the remaining mass is retained at the central cell as landslide transport rather than being silently cleared. The corresponding raster and mass ledgers are included in the Actions artifact.

## Cross-timestep residual transport verification

The source audit found that the original annual reset cleared the fully mixed transport arrays, while the layer-preserving arrays survived without their runout state being reconstructed. A single-event mass balance therefore did not establish persistence into the next timestep.

v0.9 now uses the layer-resolved landslide arrays as landslide-only persistent storage for fully mixed residuals as well. At the beginning of the next landslide calculation, the stored mass is restored to the selected mixing mode and its runout thickness is reconstructed from the PTF-derived transported mass. This keeps the residual separate from the transient mixed arrays shared with water erosion.

GitHub Actions #27 tested both mixing modes through two successive events, explicitly calling LORICA's \`initialise_every()\` between them:

| Check | Fully mixed | Layer-preserving |
|---|---:|---:|
| Residual after event 1 | 1,252,616.880 kg | 1,252,553.992 kg |
| After \`initialise_every()\` | unchanged | unchanged |
| After daily water erosion | unchanged | unchanged |
| Residual after event 2 | 1,179,501.647 kg | 1,179,316.162 kg |
| Event 2 deposition depth | 0.500 m | 0.500 m |
| Event 1 relative closure error | \(1.39\times10^{-15}\) | \(1.39\times10^{-15}\) |
| Event 2 relative closure error | \(1.16\times10^{-16}\) | \(2.32\times10^{-16}\) |

The test executed LORICA's actual \`calculate_water_ero_sed_daily()\` routine between the two landslide events. A synthetic one-cell overland-flow direction was supplied to isolate the sediment-routing kernel; the full daily hydrology-generated flow field was not yet used.

The water-erosion kernel eroded the source cell by \(6.99\times10^{-7}\) m and deposited \(9.77\times10^{-7}\) m at the receiving cell. Soil-mass closure was zero at the recorded precision. Persistent landslide residual mass was unchanged in both modes. LORICA's transient water-erosion arrays retained 0.113032 kg after the deposition step, but those arrays are reset at the next daily erosion call and are not part of the soil-mass ledger. They were therefore kept separate from the persistent landslide store in the audit.

This verifies annual-reset persistence, separation from water-erosion transport, soil-layer maintenance, and remobilization/deposition in a second event. It uses a controlled synthetic annual climate record with one storm and does not yet test multi-year TREED root updates or catchment-scale behavior.

## Dailyflow-generated runoff and water-erosion test

GitHub Actions **#42** ([run #42](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/43386286575)) adds a separate 5×5 test that calls LORICA's actual \`dailyflow()\` routine to generate \`OFy_m\`, then passes that flow field to \`calculate_water_ero_sed_daily()\`.

- Rainfall excess input: 10 mm over 6 h.
- Source cell: (1,1).
- Only lower neighbour: open-boundary cell (0,0).
- Generated flow direction: \`OFy_m[1,1,1] = 0.01 m\`.
- Source erosion: \(-4.6180190\times10^{-8}\) m.
- Soil mass loss: 0.007464734837 kg.
- Boundary transport mass: 0.007464734956 kg.
- Relative mass-closure error: \(2.94\times10^{-17}\).

This verifies that the actual LORICA daily runoff-routing routine generates a direction array that the daily sediment-erosion kernel can use, and that the resulting sediment export closes the soil-mass ledger in this controlled open-slope test.

The sequential landslide–water-erosion–landslide test in #39 still uses a prescribed flow direction to isolate residual-store independence. The #42 hydrology test is a separate synthetic slope and does not yet run the full annual \`water_balance()\` / 365-day climate sequence.

## Full annual water-balance sequence

GitHub Actions **#47** ([run #47](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/43387264610)) extends the separate dailyflow test to LORICA's full \`water_balance()\` sequence.

- 365-day precipitation, duration, minimum-temperature, mean-temperature, and maximum-temperature arrays were supplied to the existing daily weather generator.
- The controlled annual series contains one 10 mm rainfall event lasting 6 hours; the remaining 364 days are dry.
- \`water_balance()\` generated the annual \`OFy_m\` flow-direction raster.
- The test then followed the model's annual order: \`initialise_every()\`, \`comb_sort()\`, and \`calculate_water_ero_sed_daily()\`.

| Metric | Result |
|---|---:|
| Annual precipitation | 0.010 m |
| Generated source flow direction | 0.010 m |
| Source erosion | \(-4.6180190\times10^{-8}\) m |
| Soil mass loss | 0.007464734837 kg |
| Boundary transport mass | 0.007464734956 kg |
| Relative mass-closure error | \(2.94\times10^{-17}\) |

This verifies the complete annual daily-weather preparation and water-balance routing path on a controlled 5×5 open-slope test. It is not yet a realistic climate-year validation, and the generated flow has not yet replaced the prescribed flow in the sequential landslide-residual test.

## Scope boundary

This is a process-kernel verification on synthetic 1-D and 5×5 2-D terrain. The sequential landslide test includes an annual reset and one daily water-erosion call between events using a prescribed flow direction. A separate 5×5 test generates runoff directions with LORICA's actual `dailyflow()` routine. Neither test is a catchment validation. It is **not** a catchment validation, a 30-year landscape-evolution run, or field validation. It also does not validate the spatial accuracy of TREED root biomass or the Hwang et al. (2015) biomass-to-cohesion transfer for a specific site.

## Next verification stage

1. **Completed in #77:** verify same-year TREED root carbon/FPC transfer, per-cell ECA reproducibility across 1- and 4-thread execution, and the resulting root-cohesion effect in LORICA's critical-rainfall and landslide routines. The same-year climate transfer and vegetation-to-ET coefficient were also checked; a full annual water-balance run with TREED-derived ET remains part of the next gate.
2. Run a short multi-year 2-D LORICA–TREED case with the actual annual order: TREED update, daily water balance, water erosion, and rainfall-triggered landslide. Record DEM, soil depth/mass, layer composition, root cohesion, and transport ledgers at every year.
3. Only after that test passes, expand to the 30-year coupling audit.

No taproot geometry, fire module, or unverified root architecture is introduced in v0.9. Root reinforcement remains based on TREED area-normalized fine + coarse root biomass and the Hwang et al. (2015) biomass-to-cohesion relationship.
