# Gounsa v0.60 preservation status

Updated after the upstream-model archive gate completed successfully.

## A. Already preserved on GitHub / GitHub Actions

### Reproducible source identity
- Official LPJ-GUESS 4.1.1 acquisition URL and pinned SHA-256 are versioned in the repository.
- `v059_patch/**` reconstructs the audited normalized Gounsa source from the official LPJ-GUESS archive.
- Linux and Windows source/build workflows are versioned in GitHub.

### GitHub Actions artifacts
- `gounsa-v059-normalized-source-tree`
  - digest: `sha256:f6f268a21e58c19cba47aa4d8002950e95decf87651d354e86b0de276e55c860`
- `gounsa-v059-normalized-backbone-windows-x64`
  - digest: `sha256:99c4e90e5b7e1b1a65975f3da2d772c8b5559f303cc9bbd08b341df6477ef461`
- `gounsa-v060-upstream-model-archive`
  - digest: `sha256:a4e759537a79781dcc5467de30ca6265137e7640c2280f6973f836660f8d3ef3`
  - contains the official LPJ-GUESS 4.1.1 ZIP after SHA verification and the SIBERIA provenance/acquisition record.
  - retention configured to 90 days.

### Exact data/package inventory
`archive/v060/DATA_MODEL_ARCHIVE_MANIFEST.md` pins names, byte sizes, SHA-256 hashes, scientific roles, and source-identity rules for the current Gounsa inputs and project checkpoints.

## B. Original SIBERIA package

The Gounsa audited COPLAS/SIBERIA package contains an explicit no-redistribution contract for the original SIBERIA source. Therefore the repository does **not** silently copy or republish original SIBERIA source bytes.

Instead GitHub records:
- version 8.3.3 / 8.33
- DOI `10.1594/IEDA/100163`
- canonical CSDMS/IEDA archive URL
- official `csdms-contrib/siberia` repository identity

This is intentional provenance preservation, not a missing-file oversight.

## C. Exact local project binaries not yet physically transferred into GitHub storage

The following are hash-pinned in the GitHub manifest but, at this checkpoint, their unique local bytes are not yet physically stored in the repository or a new GitHub Actions artifact:

- `GOUNSA_CORE_INPUTS_v060.tar.xz` — 1,456,960 B — `da32e14d9e5a4efba5dd2dd9956f3eb86439d8885f64f56b3003ab27567b253d`
- `GOUNSA_v0_58_BLAZE_DBH_EXACTFUEL_3D_SOURCE_STAGE.zip` — 28,120,876 B — `8520c3ee7f005ae8d488201c9ffafacfee3548fba023219bf32c4d061e7aba01`
- `GOUNSA_REAL_COUPLED_APP_WINDOWS_v0_52_SOURCE_STAGE_REBUILD_REQUIRED.zip` — 28,165,433 B — `166b4b1fb27b0b1b2465c93adf667dacd39a576b4c85db864b52a4e853ddf5fe`
- `GOUNSA_2022_COHERENT_NATIVE_v0_33_RESTART_SHARDS.tar.zst` — 90,227,346 B — `20a19fbb83af64ec27e62678eb5e53eed8cccf52a0e3791fbcfa5deee5e1445f`
- `GOUNSA_2022_COHERENT_NATIVE_v0_33_RESULTS.zip` — 1,489,867 B — `454d609dca620e05dd0fd42f97de2ecd2763971955264971a6ceaddba323858a`
- `GOUNSA_2023_ACTUAL_FROM_V033_v0_34_RESULTS.zip` — 18,315,053 B — `c970712e8200b81fec7e4e18df11762f6b61dc6b341f5f29413db2e5bb41f350`
- `GOUNSA_2024_ACTUAL_FROM_V033_v0_35_RESULTS.zip` — 29,213,636 B — `64eb360e98ca7be423d570297f0ef3d66b389681a474bd29f57da2e343cc82fc`
- `coplas_siberia_yongneup_v0.6.29a1_final_audit_implementation.zip` — 225,833,658 B — `6f967877b054d88a3f445c08a4e84e0c006f0fbc4c9bc44efbb53470c53c57fb`
- `COPLAS_SIBERIA_v0629a1_SOURCE_ONLY.tar.xz` — 257,436 B — `604d8516baaa412ea926e4aa56d3cd4d14af8da09f6538ef4ead1a385d06d054`

Reason: the connected GitHub Contents/Git Data interface available in this session accepts UTF-8/base64 payloads but does not expose a local-file → Release/LFS/Actions-artifact upload operation. Large local binary archives must not be falsely reported as uploaded merely because their hashes are versioned.

## D. Current archive gate result

`Archive upstream models for v0.60` run `32487414412`: **SUCCESS**.

Artifact `9448408657` (`gounsa-v060-upstream-model-archive`) was created successfully.

## E. Integrity rule before further model edits

Further v0.60 scientific implementation must reference this manifest rather than silently substituting an input/model version. Any newly materialized data archive must be checked against the SHA-256 recorded here before it is used as a production input.
