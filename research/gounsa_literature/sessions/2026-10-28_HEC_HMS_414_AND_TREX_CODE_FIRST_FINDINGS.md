# 2026-10-28 고운사 실제 원본 프로그램 HEC-HMS/TREX 소스 우선 재검증 — handoff

## New important finding
USACE HEC-HMS 4.14 (2026-09-28 final) is a RELEASED, FREE, single-existing-executable program with Gridded Simple Canopy storage, 2D Diffusion Wave rain-on-mesh routing, and separate 2D Sediment Transport (rain splash/sheet + hydraulic-flow entrainment, 2D non-equilibrium sediment advection, bed gradation and elevation). Official manual explicitly says 2D transform works with all canopy/surface/loss methods, so this is NOT a multi-study imaginary hybrid.

## Key caveat cannot gloss over
Full original engine source has NOT been obtained and HEC official software distribution policy discourages source distribution, although binaries are freely downloadable Windows/Linux/macOS. Native LAI parameter is a per-cell canopy-storage input raster derived from measured LAI via published external relation; no native dynamic LAI canopy model or canopy leafdrip KE documented. 5cm DEM terrain inside HEC-RAS subgrid tables IS NOT a computational 5cm grid. No 5/10cm genuine computational mesh/running same-canopy-sediment experiments performed. No guarantee that default 2D sediment splash uses only net throughfall; this requires native run/source unavailable. Version 4.14 release notes correct sediment output indexes and flux totals; don't claim built-in correctness at cm.

## Actual external C source read
Connected GitHub original https://github.com/WatershedModels/trex_src_csu READ 2010-2017 C files and Makefile. WaterTransport-r4.c invokes Rainfall; Interception; Infiltration; OverlandWaterRoute; solids source SolidsTransport.c invokes deposition, advection, transport capacity and erosion; Interception-r4.c is water storage threshold; OverlandSolidsErosion.c is shear stress/bare fraction and finite available soil, no splash raindrop/LAI leafdrip code in grep. Older public CSU source not exact 2017 Wei forest-improved release. Do NOT treat TREX as full published canopy+rain/flow erosion.

## Saved files and decisions
- models/HEC_HMS_2D_Sediment.md
- decisions/2026-10-28_HEC_HMS_414_SINGLE_PROGRAM_NATIVE_CANOPY_2D_SEDIMENT_GATE.md
- models/TREX.md updated with exact source code links
- MASTER.md updated; INDEX.md regenerated actual main tree now papers511, models114, decisions114 including .gitkeep.

## Next validation
Source-public strict: HEC-HMS NO-GO as source, though best newly confirmed native binary near-match. If user permits official original executable, download HEC-HMS 4.14, find a genuine 2D Sediment example (published upper North Bosque workshop is MUSLE and not genuine 2D), build one reproducible unstructured HEC-RAS 2D mesh and 2D canopy+erosion smoke, check rainfall gross/net splash, all-boundary flux, sediment/surface maps, then fine-grid numerical convergence and local finite soil. No native test in this session. Do not reassign original OpenLISEM rescue from other Work or promise fixing.

## Official sources
https://www.hec.usace.army.mil/software/hec-hms/downloads.aspx
https://www.hec.usace.army.mil/confluence/hmsdocs/hmsum/4.14/subbasin-elements/selecting-a-canopy-method
https://www.hec.usace.army.mil/confluence/hmsdocs/hmstrm/transform/2d-diffusion-wave-model
https://www.hec.usace.army.mil/confluence/hmsdocs/hmsum/4.14/erosion-and-sediment-transport/subbasin-sediment
https://www.hec.usace.army.mil/SOFTWARE/distribution_policy.aspx
https://github.com/WatershedModels/trex_src_csu