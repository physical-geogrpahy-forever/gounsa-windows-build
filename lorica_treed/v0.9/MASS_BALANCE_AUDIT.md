# LORICA–TREED v0.9 mass-balance and layer-order audit

## Audit target

- Repository: \`physical-geogrpahy-forever/gounsa-windows-build\`
- Audit branch: \`lorica-treed-v0.9-mass-audit\`
- Tested source: exact LORICA–TREED v0.5 source bundle, patched by \`lorica_treed/v0.9/apply_v09_patch.py\`
- Latest verified commit: \`1473f49e3bc0cfbcba64ff6607a32fa98d2b937e\`
- Latest CI run: [#16](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/43377311998)

The audit branch is deliberately separate from \`lorica-treed-v0.9-30yr-coupling-audit\`. The mass and layer-preservation fixes have not yet been merged into that working branch.

## 1. Initial mass-balance failure: residual fraction applied twice

The first process-level test failed with a relative mass-closure error of:

\[
0.0833333333333333 = 8.3333\%
\]

The source sequence was:

1. The deposition routine subtracted the deposited fraction from the transport arrays.
2. The subsequent downslope-routing code multiplied the already reduced arrays by \`undeposited_landslide_fraction\` again.
3. The same residual fraction was therefore applied twice.

The v0.9 patch removes the second multiplication for all six transported components:

- mixed mineral texture;
- mixed Young SOM;
- mixed Old SOM;
- layer-resolved mineral texture;
- layer-resolved Young SOM;
- layer-resolved Old SOM.

The remaining arrays are distributed only by the downstream \`distribution_fraction\`.

## 2. Second failure: layer-preserving deposition

After the residual-routing correction, the layer-preserving mode was added to the process test. The first one-layer test produced:

- initial soil mass: 650,000 kg;
- final soil mass: 613,852.67815507017 kg;
- final transport mass: 0 kg;
- unaccounted mass: 36,147.32184492983 kg;
- relative closure error: 5.5611264%.

The diagnostic trace located the residual:

| Cell | Residual before cleanup |
|---|---:|
| Row 3 | 65,000.000 kg |
| Row 4 | 36,147.322 kg |

At row 4 the residual transport array was cleared after deposition. The layer-preserving deposition routine had used the original template-layer thickness to calculate a coverage fraction, then multiplied that by the global deposition fraction. This second thickness scaling could leave transported mass even when the requested deposition depth had consumed the available material.

The one-layer test also had an inconsistent initial condition: its nominal layer thickness was 1 m, but its texture mass was set using 1,300 kg m⁻³ while LORICA's PTF recalculated a different bulk density. That test was not suitable as a final soil-profile validation.

## 3. Layer-preserving deposition correction

The revised implementation uses the actual transported mass in each source layer:

1. For each source layer, collect its mineral texture and Young/Old SOM transport masses.
2. Calculate that layer's available thickness with LORICA's \`calc_thickness_from_mass()\`, using the same PTF as the soil-thickness calculation.
3. Allocate the requested deposition depth from the source layers in order.
4. Calculate the withdrawal fraction for each layer as:

\[
f_i =
\frac{\text{deposition thickness allocated to layer }i}
{\text{actual available thickness of transported layer }i}
\]

5. Transfer the corresponding mineral and SOM masses into the receiving profile.
6. Preserve source-layer indices when new layers are inserted. If the receiving profile has fewer available slots than the transported profile, excess lower segments are merged into the bottom layer rather than discarded.
7. Calculate total available transported thickness in mode 2 as the sum of the actual per-layer thicknesses, so the caller and deposition routine use the same quantity.

This avoids multiplying a global deposition fraction by a second fraction based on the original template thickness.

## 4. Final test design

The base process suite uses a five-cell, one-dimensional synthetic hillslope. It is complemented by a 5×5, 10 m-cell convergent basin and a closed-sink residual-storage case.

| Parameter | Setting |
|---|---|
| Grid | 5 cells × 1 cell |
| Cell size | 10 m |
| Initial soil depth | 1.0 m |
| Soil layers | 10 |
| Layer template | 0.10 m, geometric increase 1.1 |
| Upper-slope geometry | 45° |
| Lower slope | Depositional footslope |
| Event rainfall | 60 mm in 6 h |
| Mean event intensity | 10 mm/h = 0.24 m/day |
| Root cohesion | 0, 4.3, 7.6 kPa |
| Mixing modes | Fully mixed and layer-preserving translation |

The soil profile is PTF-consistent. Each layer's mineral mass is calculated using LORICA's own \`bulk_density_calc_kg_m3()\` function. Texture also changes with depth, allowing the layer-preservation test to distinguish source layers:

- top layer: 45% sand, 45% silt, 10% clay;
- deeper layers progressively reduce sand and increase silt/clay;
- the deepest active source layer: 31% sand, 52% silt, 17% clay.

## 5. Final process results

GitHub Actions #16 compiled the Windows LORICA project, ran the existing v0.5 Python regression suite, compiled the process harness, and passed all six process cases.

| Root cohesion | Mode | Critical rainfall (m/day) | Initiation cells | Erosion thickness sum (m) | Deposition thickness sum (m) | Relative mass error |
|---:|---|---:|---:|---:|---:|---:|
| 0 kPa | Fully mixed | 0 | 3 | 3.0000 | 3.2946 | 0 |
| 4.3 kPa | Fully mixed | 0.00552244 | 3 | 2.8268 | 3.1015 | 0 |
| 7.6 kPa | Fully mixed | -9999 (stable sentinel) | 0 | 0 | 0 | 0 |
| 0 kPa | Layer-preserving | 0 | 3 | 3.0000 | 3.2956 | \(2.90\times10^{-16}\) |
| 4.3 kPa | Layer-preserving | 0.00552244 | 3 | 2.8268 | 3.1023 | \(2.90\times10^{-16}\) |
| 7.6 kPa | Layer-preserving | -9999 (stable sentinel) | 0 | 0 | 0 | 0 |

Across the six cases:

- initial soil mass: 802,959.53865146788 kg;
- final soil mass: 802,959.53865146788–802,959.53865146812 kg;
- final transport mass: 0 kg;
- maximum absolute difference: approximately \(2.33\times10^{-10}\) kg;
- maximum relative closure error: \(2.90\times10^{-16}\);
- high-root-cohesion no-slide soil depth: 1.0000000000000002 m.

The depth-varying texture test also writes \`layer_mass_ledger.csv\`. Automated assertions passed:

- row 3 receiving layers 0–6 retain source-layer signatures 0–6;
- row 4 receiving layers 0–1 retain the remaining source-layer signatures 6–7.

This demonstrates that the translation mode preserves distinct layer composition and the tested layer order in this synthetic routing sequence. It does not establish general stratigraphic validity for all terrain geometries.


### 5.1 Two-dimensional convergent basin and closed sink

The 2-D test uses a 5×5 grid with 10 m cells, a central depression, eight source cells, and a 57.5 m spill saddle for the runout-limited closed-sink case.

| Scenario | Mode | Initiations | Erosion thickness sum (m) | Deposition thickness sum (m) | Residual transport (kg) | Relative mass error |
|---|---|---:|---:|---:|---:|---:|
| Convergent basin | Fully mixed | 8 | 8.000 | 8.785688 | 0 | \(8.12\times10^{-16}\) |
| Convergent basin | Layer-preserving | 8 | 8.000 | 8.788155 | 0 | \(8.12\times10^{-16}\) |
| Closed sink, runout-limited | Fully mixed | 8 | 8.000 | 0.219642 | 1,252,616.880 | \(1.39\times10^{-15}\) |
| Closed sink, runout-limited | Layer-preserving | 8 | 8.000 | 0.219704 | 1,252,553.992 | \(1.33\times10^{-15}\) |

The convergent cases deposited the routed material in the central cell and ended with zero transport mass. The closed-sink cases retained the un-deposited mass at the central cell because it had no lower neighbour. This verifies that the material is represented in transport storage rather than being silently deleted.

## 6. Interpretation and remaining limits

**Verified:** the patched LORICA process kernel compiles on Windows; rainfall timing and event-intensity conversion tests pass; root-cohesion values survive diagnostic output; both user-selectable mixing modes close mass to floating-point precision in the tested ten-layer profile; and the tested translation-mode layers retain their source signatures.

**Verified in the expanded synthetic tests:**

- 2-D convergent flow from eight surrounding source cells into an internal depression;
- retention of residual transport when a closed sink has no lower neighbour;
- residual mass persistence through `initialise_every()` in both mixing modes;
- execution of the full annual `water_balance()` / daily-weather sequence between two landslide events;
- actual daily water-erosion source-cell erosion, interior deposition, and boundary export;
- unchanged layer-resolved landslide residual mass during water erosion and soil-layer split/combine;
- second-event remobilization and deposition in both mixing modes;
- correction of the water-erosion outlet-boundary off-by-one condition.

**Not yet verified:**

- TREED-generated root-carbon/FPC maps being applied before the same year's water balance and critical-rainfall calculation;
- more than two successive events and long-run accumulation/remobilization;
- multi-year TREED root-biomass updates in a full LORICA–TREED run;
- 30-year catchment-scale coupling;
- field validation of the root-cohesion transfer or landslide occurrence.

The third radio option (\`ls_mix_radio_3\`) is disabled in the source UI and was not tested. The current tests are synthetic 1-D and 5×5 process tests, not a catchment or field-validation result.


## 7. Cross-timestep residual storage and remobilization

### 7.1 Source-level issue

The original \`calculate_slide_new()\` reset \`remaining_vertical_size_m\` and the fully mixed transport arrays at the beginning of every landslide calculation. In addition, \`initialise_every()\` cleared the mixed transport arrays when the landslide checkbox was active. The layer-resolved arrays were not cleared by \`initialise_every()\`, but their runout state was still reset to zero by \`calculate_slide_new()\`. Thus, residual material could be present in memory but inactive in the next timestep.

### 7.2 v0.9 correction

The patch now uses the existing layer-resolved transport arrays as persistent landslide-only storage for both modes:

- **Fully mixed mode:** after each event, residual mineral and SOM mass is moved into layer 0 of the persistent layer arrays. At the next event, it is restored into the fully mixed transport arrays. This avoids losing the residual when \`initialise_every()\` clears the mixed arrays and avoids passing the landslide residual to water erosion as transient water-erosion sediment.
- **Layer-preserving mode:** residual mass remains in its source-layer arrays.
- **Both modes:** \`remaining_vertical_size_m\` is reconstructed from the actual transported mass using LORICA's PTF-based thickness calculation before the next landslide routing pass.

The persistent arrays remain separate from the transient mixed arrays used by the water-erosion routine. The later #39 test executes the actual daily water-erosion kernel between events, while keeping these stores separate.

### 7.3 Two-event results

GitHub Actions #39 passed the Windows compile, existing v0.5 Python regression suite, process harness compile, and all process tests, including the daily water-erosion bridge.

| Metric | Fully mixed | Layer-preserving |
|---|---:|---:|
| Event 1 residual transport | 1,252,616.880 kg | 1,252,553.992 kg |
| After \`initialise_every()\` | 1,252,616.880 kg | 1,252,553.992 kg |
| Event 2 residual transport | 1,179,501.647 kg | 1,179,316.162 kg |
| Event 2 deposited thickness | 0.500 m | 0.500 m |
| Event 1 relative closure error | \(1.39\times10^{-15}\) | \(1.39\times10^{-15}\) |
| Event 2 relative closure error | \(1.16\times10^{-16}\) | \(2.32\times10^{-16}\) |

For both modes, the event-1 total mass was 4,014,797.693 kg. The same total was retained after the annual reset. Event 2 converted 0.5 m of residual material into soil deposition while conserving total soil plus transport mass to floating-point precision.

The second-event rasters and ledgers are stored under:

- \`landslide_test/residual_persistence_complete/\`
- \`landslide_test/residual_persistence_translation/\`

### 7.4 Interpretation

This is direct evidence that residual mass survives one annual reset, remains unchanged during one daily water-erosion kernel call, and is processed in the next landslide calculation. It is not yet evidence that the complete annual hydrology and water-erosion sequence generates the correct flow field or conserves/routes material over multiple days.


## 8. Daily water-erosion bridge and boundary correction

### 8.1 Source-level boundary defect

The original no-outflow deposition branch in \`calculate_water_ero_sed_daily()\` used:

\`\`\`csharp
(row + i) <= 0
(col + j) <= 0
\`\`\`

The routine uses zero-based array indices. A valid neighbour at row 0 or column 0 was therefore classified as outside the domain. In the synthetic test, the receiver at (1,1) was falsely treated as an outlet because one of its valid diagonal neighbours was (0,0). Sediment was exported instead of deposited.

The v0.9 patch changes the lower-bound checks to \`< 0\`, while retaining the upper-bound checks \`>= nr\` and \`>= nc\`. This is a targeted correction to the test-exposed off-by-one error.

### 8.2 Daily water-erosion process test

After event 1, the test calls LORICA's actual \`initialise_every()\`, then executes \`calculate_water_ero_sed_daily()\` before event 2. The test supplies one synthetic overland-flow direction in \`OFy_m\` from (0,0) to (1,1) so that the sediment-routing kernel can be isolated from the daily hydrology generator.

| Metric | Result |
|---|---:|
| Source-cell erosion | \(-6.9926594\times10^{-7}\) m |
| Receiver-cell deposition | \(9.7677369\times10^{-7}\) m |
| Relative soil-mass closure | 0 |
| Persistent landslide mass, fully mixed | 1,252,616.880 kg before and after |
| Persistent landslide mass, layer-preserving | 1,252,553.992 kg before and after |
| Stale daily water-erosion transport-array content | 0.113032 kg |

The stale daily transport-array content is not included in the physical soil-mass ledger: the water-erosion routine has already added the deposited sediment to the soil profile, but its transient transport arrays are not cleared at the deposition branch. Those arrays are reset at the next daily water-erosion call. The v0.9 landslide residual is stored separately in the layer-resolved arrays and is unaffected.

### 8.3 Sequential event results

The test then executes the model's soil-layer maintenance, cell re-sort, slope initialization, critical-rainfall calculation, and event 2:

| Metric | Fully mixed | Layer-preserving |
|---|---:|---:|
| Event 1 residual mass | 1,252,616.880 kg | 1,252,553.992 kg |
| After annual reset | unchanged | unchanged |
| After daily water erosion | unchanged | unchanged |
| Event 2 residual mass | 1,179,501.647 kg | 1,179,316.162 kg |
| Event 2 deposition depth | 0.500 m | 0.500 m |
| Event 2 relative mass error | \(1.16\times10^{-16}\) | \(2.32\times10^{-16}\) |

The test confirms that the persistent landslide residual survives the annual reset, is not consumed by the water-erosion kernel, and is remobilized in the second landslide event in both mixing modes.

**Limit:** the flow direction in this test is prescribed. The test does not yet run \`water_balance()\` / \`dailyflow()\` to generate the overland-flow field from rainfall, infiltration, and topography. It also does not test multiple daily water-erosion calls or more than two landslide events.

### 8.4 Runoff directions generated by LORICA \`dailyflow()\`

GitHub Actions #42 added a separate 5×5 open-slope test. It calls the actual LORICA \`dailyflow()\` method to generate \`OFy_m\`, then executes \`calculate_water_ero_sed_daily()\`.

| Metric | Result |
|---|---:|
| Rainfall excess input | 0.010 m over 6 h |
| Generated source direction | \`OFy_m[1,1,1]\` = 0.010 m |
| Source-cell erosion | \(-4.6180190\times10^{-8}\) m |
| Soil mass before | 4,014,797.693257332 kg |
| Soil mass after | 4,014,797.685792597 kg |
| Soil mass loss | 0.007464734837 kg |
| Boundary transport mass | 0.007464734956 kg |
| Relative mass-closure error | \(2.94\times10^{-17}\) |

The source cell has one lower neighbour at the open boundary. Other cells are assigned sufficient infiltration capacity so that the test isolates a single runoff path. The resulting sediment is exported at the boundary; soil mass loss and transported export agree to floating-point precision.

This demonstrates that \`dailyflow()\` generates a usable flow-direction raster and that the daily water-erosion kernel routes sediment using that raster. It is separate from the sequential landslide persistence test, which still uses a prescribed flow direction.

**Limit:** this test does not yet run the full annual \`water_balance()\` routine, the daily weather generator, or a multi-day rainfall sequence.

### 8.5 Full annual \`water_balance()\` and daily weather

GitHub Actions #47 tests the actual annual hydrology path rather than calling \`dailyflow()\` directly:

1. The test supplies 365-day \`P_all\`, \`D_all\`, \`Tmin_all\`, \`Tavg_all\`, and \`Tmax_all\` arrays.
2. One 10 mm / 6 h event occurs on day 1; the other 364 days are dry.
3. LORICA's \`create_daily_weather()\` prepares the daily arrays.
4. \`water_balance()\` loops over the annual daily sequence and accumulates the overland-flow directions in \`OFy_m\`.
5. The test follows the model order with \`initialise_every()\`, \`comb_sort()\`, and \`calculate_water_ero_sed_daily()\`.

| Metric | Result |
|---|---:|
| Annual precipitation | 0.010 m |
| Generated source flow direction | 0.010 m |
| Source erosion | \(-4.6180190\times10^{-8}\) m |
| Soil mass loss | 0.007464734837 kg |
| Boundary transport mass | 0.007464734956 kg |
| Relative mass-closure error | \(2.94\times10^{-17}\) |

This confirms that the annual weather-preparation and water-balance routines generate a usable \`OFy_m\` field and that the daily sediment-erosion kernel conserves the soil-loss/export ledger for this controlled case.

**Limit:** the annual series is deliberately sparse and synthetic. The generated annual flow has not yet been used between sequential landslide events, and the test does not include TREED root updates or a realistic climate-year sequence.

## 9. Next verification

The next process test should run a 2-D multi-year case in the actual LORICA timestep order:

1. \`initialise_every()\` and the water-erosion process;
2. daily water balance and TREED root update;
3. landslide critical-rainfall calculation and event routing;
4. soil-layer update and DEM update.

At each timestep, record separate ledgers for soil mass, water-erosion transport, landslide residual transport, and any explicit boundary export. The closure equation should be:

\[
M_{\mathrm{soil},t} + M_{\mathrm{water},t} + M_{\mathrm{landslide},t}
=
M_{\mathrm{soil},t+1} + M_{\mathrm{water},t+1} + M_{\mathrm{landslide},t+1}
+ M_{\mathrm{export},t}
\]

Only after that integrated test passes should the 30-year LORICA–TREED coupling run be expanded.
