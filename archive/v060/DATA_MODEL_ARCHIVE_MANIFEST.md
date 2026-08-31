# Gounsa v0.60 data/model archive manifest

Purpose: freeze the exact inputs, checkpoints, and upstream-model identities required to reconstruct the Gounsa LPJ-GUESS–COPLAS/SIBERIA work before further v0.60 source edits.

## Production/core Gounsa inputs

The current v0.60 core-input set is the following nine files. These are taken from the audited v0.58 source-stage package plus the v0.60 soil-code input.

| file | role |
|---|---|
| `GOUNSA_FOREST4137_DIRECT_STATE_2022_FULL_HISTORY_v0_52.csv` | 4,137 forest/larch full-history direct-state baseline |
| `GOUNSA_FOREST4137_DIRECT_STATE_2022_CURRENT.csv` | current-state companion table |
| `GOUNSA4454_FINAL_EXCHANGE_ACTION_v0_24.csv` | 4,454-cell exchange/action table |
| `GOUNSA4454_INITIAL_DEM_SOILDEPTH_v0_34.csv` | 4,454-cell initial DEM/soil-depth table |
| `gounsa_watershed_grid_30m_5187.csv` | 30 m active-grid geometry/index |
| `gounsa_climate_bilinear_weights_30m_5187.csv` | climate interpolation weights |
| `GOUNSA_RECEIVER_GRAPH_30M_v0_1.csv` | fixed baseline receiver graph / single-outlet routing contract |
| `gounsa_climate_7var_63grid_2021_2030.nc` | reduced-grid 7-variable climate forcing source |
| `gounsa_lpj_soilcodes_30m_5187.txt` | LPJ soil codes |

A deterministic local preservation bundle was generated as `GOUNSA_CORE_INPUTS_v060.tar.xz` with SHA-256:

`da32e14d9e5a4efba5dd2dd9956f3eb86439d8885f64f56b3003ab27567b253d`

The bundle contains an internal `SHA256SUMS.txt` covering every member.

## Project checkpoints and evidence packages

| bytes | SHA-256 | package |
|---:|---|---|
| 28,120,876 | `8520c3ee7f005ae8d488201c9ffafacfee3548fba023219bf32c4d061e7aba01` | `GOUNSA_v0_58_BLAZE_DBH_EXACTFUEL_3D_SOURCE_STAGE.zip` |
| 28,165,433 | `166b4b1fb27b0b1b2465c93adf667dacd39a576b4c85db864b52a4e853ddf5fe` | `GOUNSA_REAL_COUPLED_APP_WINDOWS_v0_52_SOURCE_STAGE_REBUILD_REQUIRED.zip` |
| 90,227,346 | `20a19fbb83af64ec27e62678eb5e53eed8cccf52a0e3791fbcfa5deee5e1445f` | `GOUNSA_2022_COHERENT_NATIVE_v0_33_RESTART_SHARDS.tar.zst` |
| 1,489,867 | `454d609dca620e05dd0fd42f97de2ecd2763971955264971a6ceaddba323858a` | `GOUNSA_2022_COHERENT_NATIVE_v0_33_RESULTS.zip` |
| 18,315,053 | `c970712e8200b81fec7e4e18df11762f6b61dc6b341f5f29413db2e5bb41f350` | `GOUNSA_2023_ACTUAL_FROM_V033_v0_34_RESULTS.zip` |
| 29,213,636 | `64eb360e98ca7be423d570297f0ef3d66b389681a474bd29f57da2e343cc82fc` | `GOUNSA_2024_ACTUAL_FROM_V033_v0_35_RESULTS.zip` |
| 40,557,136 | `f6f268a21e58c19cba47aa4d8002950e95decf87651d354e86b0de276e55c860` | `gounsa-v059-normalized-source-tree.zip` (GitHub Actions artifact digest matches) |
| 3,672,132 | `99c4e90e5b7e1b1a65975f3da2d772c8b5559f303cc9bbd08b341df6477ef461` | `gounsa-v059-normalized-backbone-windows-x64.zip` (GitHub Actions artifact digest matches) |

## v0.60 engineering fixtures/patches

| bytes | SHA-256 | file |
|---:|---|---|
| 29,127 | `be6f5e9cbbcb627870b185085c999126a3a0e40bd6c2d3b07c1eb619dd0bcbee` | `GOUNSA_v060_PER_CELL_FORCING_RESTART.delta.patch` |
| 7,562 | `54138268ddea785a08f21fdc2b9f293001e095ddf48bd10ac5d5f667edde0e2f` | `GOUNSA_v060_PER_CELL_FORCING_RESTART.delta.patch.gz` |
| 114,010 | `797dcf3001158ad8445d7fc2512f0749c664bbd01df36b4a9886ace4c23ebd77` | `GOUNSA_v060_PER_CELL_CF_NATIVE_RESTART.patch` |
| 25,565 | `23744ef5f09230790878d4545bcab178271b9c522f84b4b610dd6ed3b42f1087` | `GOUNSA_v060_PER_CELL_CF_NATIVE_RESTART.patch.gz` |
| 249,916 | `3e783d58e9159ea5f77a53e8a2c88ee7a6ff23d8429a7f9c203a76605d182f31` | `GOUNSA_v060_SYNTH_RESTART_FIXTURE.zip` |

## Geomorphology implementation checkpoint

The exact audited COPLAS/SIBERIA implementation package currently held as project evidence is:

- `coplas_siberia_yongneup_v0.6.29a1_final_audit_implementation.zip`
- bytes: 225,833,658
- SHA-256: `6f967877b054d88a3f445c08a4e84e0c006f0fbc4c9bc44efbb53470c53c57fb`

A source-only preservation derivative (code/tests/config/audit contracts; excluding very large numerical-result directories and excluding redistribution of original SIBERIA source) was generated as:

- `COPLAS_SIBERIA_v0629a1_SOURCE_ONLY.tar.xz`
- bytes: 257,436
- SHA-256: `604d8516baaa412ea926e4aa56d3cd4d14af8da09f6538ef4ead1a385d06d054`

## Upstream model identity

### LPJ-GUESS 4.1.1

Canonical archive:

`https://zenodo.org/records/8065737/files/guess_4.1.1.zip?download=1`

Required SHA-256:

`9d30881c180bd2d291fea0a5d7e7cf22fc33512bf4c99b452722d4d8d3d8f193`

The repository CI must always download this exact archive and verify the hash before applying a Gounsa patch. The upstream bytes are not silently replaced by a fork.

### SIBERIA 8.3.3

Canonical CSDMS/IEDA identity:

- DOI: `10.1594/IEDA/100163`
- version: 8.3.3 / 8.33
- canonical DOI archive URL: `https://csdms.colorado.edu/pub/models/doi-source-code/siberia-10.1594.IEDA.100163-8.3.3.tar.gz`
- official repository used for source cross-checking: `https://github.com/csdms-contrib/siberia`

Important redistribution rule inherited from the audited package: **do not bundle the original SIBERIA source into the Gounsa/COPLAS derivative package.** Keep acquisition and source-identity verification external. A previously verified official-repository snapshot candidate had SHA-256 `b5d0ba05abd2f49a3b69ff81cecacab8555c9edebe725dcc850bd23f2a100457`, but DOI-archive byte identity was explicitly *not* established and must not be claimed.

## Scientific status of this archive

Archiving a file here does not upgrade its scientific status. In particular:

- v0.58 native-BLAZE fuel results remain preliminary until the normalized 1991–2021 → 2022 restart/backbone is rerun.
- physical sediment-mass/DEM evolution remains blocked until the mass bridge and real soil-depth constraints are scientifically closed.
- the 2025 wildfire aggregate percentages are validation context, not cellwise forcing or mortality parameters.

This manifest is intended to prevent loss or silent substitution of project inputs while v0.60 per-cell forcing/native restart work proceeds.