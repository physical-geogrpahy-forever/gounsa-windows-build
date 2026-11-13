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

The final test is a five-cell, one-dimensional synthetic hillslope.

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

## 6. Interpretation and remaining limits

**Verified:** the patched LORICA process kernel compiles on Windows; rainfall timing and event-intensity conversion tests pass; root-cohesion values survive diagnostic output; both user-selectable mixing modes close mass to floating-point precision in the tested ten-layer profile; and the tested translation-mode layers retain their source signatures.

**Not yet verified:**

- two-dimensional convergent flow from multiple directions;
- closed internal depressions versus open outlet boundaries;
- residual transport where topographic deposition capacity is insufficient;
- multi-event accumulation and remobilization;
- multi-year TREED root-biomass updates entering LORICA in the same timestep;
- 30-year catchment-scale coupling;
- field validation of the root-cohesion transfer or landslide occurrence.

The third radio option (\`ls_mix_radio_3\`) is disabled in the source UI and was not tested. The current test is a 1-D synthetic process test, not a 2-D catchment or field-validation result.

## 7. Next test

The next test should be a 2-D convergent hillslope with an explicitly specified outlet or closed boundary. It must track, per event:

\[
M_{\mathrm{initial}} =
M_{\mathrm{soil,final}} +
M_{\mathrm{transport,final}} +
M_{\mathrm{export}}
\]

Internal depressions must not be treated as open outlets by default. Any material that cannot be deposited or routed must remain represented as transport/storage or be recorded as boundary export; it must not be silently cleared.

Only after that test passes should the 30-year LORICA–TREED coupling run be expanded.
