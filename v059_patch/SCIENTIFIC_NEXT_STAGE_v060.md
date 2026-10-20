# v0.60 next scientific source gate

The next branch must correct two backbone mechanics before any real 2021/2022 scientific regression is claimed.

1. **Per-cell CF forcing**: the v0.59 lockstep driver currently captures climate from one template cell and applies it to every active cell. Production reduced-grid CF forcing must load the correct `landid` for each raster cell and preserve native CFInput conversions/calendar handling.
2. **Native multi-cell restart initialization**: the v0.59 lockstep driver currently has no `GuessDeserializer` path. Every target gridcell must first be initialized with its native coordinate/soil/landcover structure, then the serialized state must be bulk-deserialized by coordinate.

Additional contracts:

- routing row/col must not be silently treated as NetCDF landid; an explicit `landid` mapping is required.
- LPJ-GUESS remains 365-day; a NetCDF Feb 29 is skipped using native calendar semantics.
- no new climate model, no fuel adjustment, and no BLAZE parameter changes are introduced.
- the restart calendar origin must be explicit and audited; a 2022-only forcing file cannot be paired blindly with historical `state_year=32`.
- synthetic CI proves mechanics only; the 4,454-cell scientific state SHA/day-1/DOY147/365-day gates remain separate.