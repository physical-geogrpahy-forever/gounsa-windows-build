# LORICA–TREED v0.7: explicit event-scale cohesion calibration

v0.7 adds **no new biological or geomorphic process**. It addresses the parameter problem revealed by v0.5/v0.6: applying ordinary mean root tensile strength (about 15–22 MPa for Korean tree roots) directly to Hwang et al. (2015) Eq. (5) can produce unrealistically large root cohesion for the TREED root biomass.

## Principle

Keep Hwang's structure:

`Cr = K * Tr * Br / rho_r`

but distinguish a directly measured ordinary root tensile strength from an **effective event-scale tensile-strength parameter** used by the simplified Hwang/Wu reinforcement equation.

The calibration utility takes:

1. one baseline TREED area-normalized root-C raster;
2. one literature root-cohesion benchmark;
3. one coupling cfg template.

It inverse-solves Eq. (5) for a fixed `Tr_eff`, writes a new cfg using `hwang_root_tensile_profile=manual`, and records hashes and all calibration values in JSON.

The generated `Tr_eff` is then reused unchanged across the scenario matrix. **No scenario is recalibrated independently.** Therefore subsequent changes in root cohesion arise from changes in TREED root biomass, not from hidden retuning.

## Available benchmark profiles

- `hales2009_fbm_mean`: 3.4 kPa
- `hales2009_wu_mean`: 7.6 kPa
- `korea2025_larix_kaempferi`: 4.3 kPa
- `korea2025_pinus_densiflora`: 9.0 kPa
- `korea2025_pinus_koraiensis`: 9.1 kPa
- `korea2025_quercus_mongolica`: 12.9 kPa
- `manual`: user-specified target

Hales et al. (2009) reported vertically integrated mean root cohesion of 7.6 ± 5.4 kPa with the Wu method and 3.4 ± 2.4 kPa with the Fiber Bundle Model at Coweeta. Their paper also notes forest root biomass is commonly about 2–5 kg m⁻². The TREED CI baseline (~3.9 kg dry root biomass m⁻²) is within that biomass range.

The Korean 2025 values are reduction-corrected Wu estimates from a conference study comparing Wu-model and direct-shear reinforcement. They are useful Korean sensitivity/calibration anchors but should not be presented as universal forest values.

## Usage

```
python lorica_treed/v0.7/calibrate_event_cohesion.py \
  BASELINE/treed_rootC_areanorm_gC_m2.asc \
  coupling/TREED_coupling.cfg \
  hales2009_wu_mean \
  calibrated_hales_wu.cfg \
  calibrated_hales_wu.json
```

For the actual study, first run the chosen baseline vegetation/soil state, calibrate once, then copy the resulting fixed `Tr_eff` into every comparison scenario.

## What v0.7 deliberately does not do

- no taproot architecture;
- no fire;
- no automatic per-year or per-scenario recalibration;
- no assumption that `Tr_eff` is a directly measured material property;
- no extrapolation of Hales & Miniat (2017) field VWC regressions to a fictitious soil-moisture value of 1.0.
