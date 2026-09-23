# BiomeE / BiomeEP model lineage

## 성격
- cohort-based vegetation demographic model
- 나무, 관목, 초본 PFT
- PPA 계열 수직 canopy layers
- 개체목 좌표를 추적하지 않음
- standalone code 및 R `rsofun` wrapper 사용 가능

## 시간 구조
BiomeE 계보:
- physiology / surface exchange: hourly 계열
- growth and phenology: daily
- demography: annual

BiomeEP:
- BiomeE demography에 P-model photosynthesis를 결합한 경량 변형
- `rsofun`에서 동일한 BiomeE runner 계열로 실행 가능

## 식생 상태
- cohort PFT
- density
- DBH/height/crown area
- leaf C
- fine-root C
- sapwood/heartwood C
- NSC
- reproduction/recruitment

## 하층식생
- tree/shrub/grass PFT를 모두 가짐
- lower canopy/understory layer를 PPA로 표현
- shade/size-dependent mortality 및 resource competition으로 천이

## litter / soil
- leaf and fine-root turnover
- metabolic/structural litter
- soil organic matter
- soil C/N cycle

## succession evidence
Chen et al. 2026:
- 150-year succession
- three 50 m x 50 m plots
- 72 species, five PFTs
- evergreen/deciduous trees and shrubs가 장기 조성변화에 참여

## implementation advantage
`rsofun` provides:
- one-site BiomeE/BiomeEP runs
- user-defined species parameters
- initial cohort state
- initial soil state
- parallel multi-site execution

This makes an external raster wrapper technically simpler than ED/FATES.

## spatial limitation
BiomeE site itself has no native x-y landscape.

Potential Gounsa architecture:
```
geomorph tile/cell
 -> one BiomeE site
 -> cohort state
```

This gives explicit GIS location externally, while BiomeE remains internally non-spatial.

However cell-to-cell seed dispersal would be a new coupling.

## storm/event coupling issue
Potentially promising because initial cohort and soil states are exposed, but current public R outputs emphasize annual cohort states. Before selection, code must confirm whether:
- arbitrary-date restart is possible
- cohort state can be exported/imported after a storm
- soil depth/rooting-volume state can be changed mid-year

Without this, hourly physiology alone does not solve the Gounsa feedback requirement.

## wildfire
Native mature wildfire module was not confirmed in the standard BiomeE/BiomeEP lineage reviewed here.
Observed-fire initialization is possible as new coupling, but repeated endogenous fire is a disadvantage relative to FATES.

## current verdict
**Very strong middle-complexity candidate.**

Major advantages:
- cohort, not individual tree
- shrubs + grasses + trees
- explicit understory layer
- fine roots + litter
- hourly/daily eco-physiology
- century succession
- relatively lightweight R/Fortran implementation

Major gaps:
- native landscape spatiality
- cell-to-cell dispersal
- fire
- event-time restart/state injection not yet verified

## related papers
- `papers/2022_Weng_BiomeE.md`
- `papers/2026_Chen_BiomeE_Succession.md`
- `papers/2025_EckesShephard_DemographyModels.md`
