# LORICA–TREED v0.8: baseline-calibrated roundtrip

v0.8 verifies that the v0.7 event-scale calibration is not merely an algebraic utility: it is generated from an **actual TREED root-carbon raster**, written to the LORICA coupling configuration, and consumed by the C# → Julia TREED → C# bridge.

## Test sequence

1. Build the v0.5 LORICA C# project on Windows.
2. Run the existing 2 × 2 LORICA-to-TREED roundtrip once with the uncalibrated original control configuration.
3. Take the resulting `treed_rootC_areanorm_gC_m2.asc` as the baseline.
4. Run the v0.7 calibrator once using the Hales et al. (2009) Coweeta Wu mean benchmark (7.6 kPa).
5. Replace the coupling config with the generated fixed `Tr_eff` configuration.
6. Run the C# → Julia TREED → C# roundtrip again in a separate work directory.
7. Verify:
   - TREED root-C raster is unchanged by the cohesion-only calibration;
   - LORICA receives the configured effective `Tr_eff`;
   - mean corrected root cohesion is 7.6 kPa within 0.05 kPa;
   - FPC and ET coupling remain within their valid ranges.

The two runs use separate TREED trait directories so the baseline and calibrated runs start from independent, identical initial states. TREED's ECA optimizer is stochastic, so the CI sets `treed_random_seed=20261113` and `JULIA_NUM_THREADS=1` before both runs. This makes the two independent initial-state runs reproducible and lets the CI distinguish a cohesion-only config change from optimizer noise.

## Interpretation

The selected 7.6 kPa value is a literature benchmark for the Coweeta forest root-reinforcement estimate using the Wu method. The inferred `Tr_eff` is an inverse-calibration coefficient for the simplified Hwang Eq. (5), **not a directly measured root tensile strength** and not a universal Korean forest parameter.

A prior unseeded test showed a 0.66% difference in root carbon between independent runs, caused by TREED's stochastic ECA optimizer rather than the Hwang parameter. The fixed seed is therefore an explicit reproducibility control, not a scientific change to the objective function.\n\nThis test validates the software path and calibration reproducibility. It does not yet validate landslide initiation, slope stability, erosion, or a multi-year landscape-evolution run.
