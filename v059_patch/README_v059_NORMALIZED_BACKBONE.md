# Gounsa v0.59 normalized backbone

This branch moves the reconstructed v0.53/v0.59 scientific backbone into GitHub so that source reconstruction and builds are reproducible before the 2025 wildfire experiment is resumed.

## Source contract

- Upstream: official LPJ-GUESS 4.1.1 ZIP from Zenodo
- Upstream ZIP SHA-256: `9d30881c180bd2d291fea0a5d7e7cf22fc33512bf4c99b452722d4d8d3d8f193`
- Normalized cumulative patch SHA-256: `a4c8a93775b0975db9d3075833f2df83d79844572425e9132ab216dcfc6605b4`
- Gzip-compressed patch SHA-256: `717b0a2c4efbf2e4bbd4997f5f89020750e0a3d90a11125db9e8c480b115cdb5`
- Patch representation in this repository: `part_00.b64` + `part_01.b64`, concatenated in lexical order, base64-decoded and gunzipped.

The official ZIP and the modified LPJ-GUESS source tree are not committed to the repository. CI reconstructs them from the verified upstream archive and the verified cumulative patch.

## Why patch application ignores whitespace

The official LPJ-GUESS ZIP and the reconstructed development source have line-ending/whitespace differences. The current cumulative patch is therefore applied with:

```text
git apply --ignore-space-change --ignore-whitespace --whitespace=nowarn
```

This is an explicit source-reconstruction accommodation, not a scientific change. Patch SHA verification is performed before application, and source-marker/build checks are performed after application.

## Scientific lineage retained

```text
LPJ-GUESS 4.1.x native vegetation/hydrology
    -> daily LeafC / FineRootC / SurfaceLitC / SurfRunoff
    -> Quijano-Baron et al. (2022) COPLAS biomass-process equations
    -> SIBERIA native/source-equivalent predictor-corrector numerical lineage
```

The normalized backbone includes the Gounsa direct-state path, daily native lockstep/run-on hooks, exchange output, cohort output, and lockstep executable required for the v0.53 normalization work.

## Gates that remain in force

- Native BLAZE equations are **not replaced** by a private fire model.
- Do not lower BLAZE `MIN_FUEL` to force ignition.
- Do not modify native BLAZE fireline-intensity, combustion, or mortality equations merely to match the 2025 event.
- The previous 64-cell 2025 pre-fire fuel result is `PRELIMINARY / PRE-NORMALIZED-BACKBONE` until the normalized 2022->2025 trajectory is rerun.
- No arbitrary COPLAS/SIBERIA `mass_scale` is allowed.
- Physical sediment-mass/DEM update remains blocked until the COPLAS beta-to-SIBERIA absolute-mass bridge and actual Gounsa soil depth are resolved.
- 2026 Gounsa NDVI/SEMMA is reserved for independent post-fire validation, not calibration.

## Current reconstruction scope

This GitHub validation step is intentionally limited to:

1. verify upstream LPJ-GUESS 4.1.1 SHA;
2. reconstruct and verify the v0.59 cumulative patch;
3. apply it to fresh upstream source;
4. verify normalized-backbone source markers;
5. build `guess` and `guess_lockstep` on Linux CI.

It does **not** claim that the 4,454-cell 2022 365-day current-lockstep run, DOY147 final callback closure, 2021 state recapture/merge SHA gate, or 2025 native-BLAZE rerun has passed. Those remain subsequent scientific validation steps.
