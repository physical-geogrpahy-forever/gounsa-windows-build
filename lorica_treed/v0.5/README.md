# LORICA + TREED v0.5 CI package

This directory stores the reproducible source bundle for the Gounsa LORICA–TREED coupling experiment.

- Source bundle: `LORICA_TREED_v0.5_source.tar.xz`
- LORICA: C# / .NET Framework 4.7.2
- TREED: Julia 1.11.6
- Root reinforcement: Hwang et al. (2015) biomass-to-root-cohesion equation
- No fire/disturbance module has been added.
- Original TREED control and experimental adaptive-root modes remain separate.

The GitHub Actions workflow `.github/workflows/lorica-treed-v05-ci.yml`:
1. extracts this bundle,
2. runs all Python static/numerical coupling tests,
3. instantiates and loads TREED,
4. executes a 2 x 2 local-grid TREED coupling smoke test using the original fixed-root control,
5. restores MathNet.Numerics and compiles the modified LORICA project on Windows.

The 2 x 2 test is a runtime bridge gate, not a scientific calibration or production simulation.
