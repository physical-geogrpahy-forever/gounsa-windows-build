# Gounsa v0.59 Windows source/build gate

GitHub Actions run: `32467555520`  
Head commit: `8fb16d534a00f47add9c1d7c2e2403eef2c1a863`

## Result

- official LPJ-GUESS 4.1.1 download/SHA verification: **PASS**
- cumulative v0.59 patch reconstruction/SHA verification: **PASS**
- patch application on clean upstream: **PASS**
- MSVC/NetCDF configure: **PASS**
- `guesscmd.exe` build: **PASS**
- `guess_lockstep.exe` build: **PASS**
- Windows artifact upload: **PASS**

Artifact: `gounsa-v059-normalized-backbone-windows-x64`  
Artifact id: `9441509053`  
Artifact digest: `sha256:99c4e90e5b7e1b1a65975f3da2d772c8b5559f303cc9bbd08b341df6477ef461`

Binary hashes inside artifact:

- `guesscmd.exe`: `7b83263aebef23034f6ba596e5aafdfd497b8921cc6162a69495893ed7bf5bee`
- `guess_lockstep.exe`: `f618d92aeff315bc7182dd3b7068f69250d0c6f1813c43da1e3692324faef22f`

## Scope of this PASS

This is a **source reconstruction and platform build gate only**. It does not claim that the following scientific gates have passed:

- 2021-12-31 state recapture/merge SHA
- 4,454-cell day-1 restart regression
- DOY147 final predictor/corrector closure
- 2022 365-day current lockstep
- 2025 native-BLAZE rerun

Native BLAZE equations and thresholds are not modified by this gate. Physical sediment-mass and DEM update remain blocked.