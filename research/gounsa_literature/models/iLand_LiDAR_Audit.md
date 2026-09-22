# iLand LiDAR-scale audit

## 목적
이전 검토에서 iLand가 공간적으로 세밀해 보이지만 고운사 LiDAR geomorph coupling에 실제로 맞는지 scale별로 재검증한다.

## multi-scale structure
iLand is spatially heterogeneous, but different processes use different resolutions.

- individual trees: explicit
- light influence field: 2 m
- regeneration cohorts: 2 m
- seed availability: 20 m
- dominant height: 10 m
- resource unit: 100 m x 100 m = 1 ha

## processes at resource-unit scale
The iLand documentation states that many stand-level processes operate at the 1-ha resource-unit level, including:
- NPP production
- water cycle
- soil/environment conditions
- soil/deadwood carbon inputs and pools

Thus:
```
2 m tree/light grid
!=
2 m ecohydrology / soil biogeochemistry
```

## LiDAR implications
LiDAR-derived tree positions and canopy structure fit the aboveground representation well.

But if the geomorph model runs at 1-5 m:
- local soil depth change
- local soil moisture
- root-zone environment
- erosion-driven substrate redistribution
cannot be passed to iLand at the same scale without restructuring the resource-unit logic.

## verdict
Under a 30 m landscape criterion iLand remained plausible.
Under a 1-5 m LiDAR geomorph criterion, the fixed 1-ha resource-unit scale is a major mismatch.

Therefore:
- retain as a forest-landscape comparator
- do not choose as the primary Gounsa vegetation engine unless resource-unit hydrology/production is rewritten
