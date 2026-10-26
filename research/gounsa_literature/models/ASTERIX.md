# ASTERIX — water-flow release vs separate theoretical vegetation/erosion publication

## Original model identification
- Ion, Marinescu, Cruceanu (2025), Environmental Modelling & Software 186, 106336, DOI 10.1016/j.envsoft.2025.106336. Open source **water flow module**, 2D extended Saint-Venant with spatial vegetation porosity and drag, hexagonal raster.
- Authors' 2024 technical source says C program downloadable as `http://www.ima.ro/software/ASTERIX_flow_2D.tar.xz`; code archive not downloaded/compiled in this investigation.

## Process source verification
- Authors' 2024 `ASTERIX: Module for modelling the water flow on vegetated hillslopes`, **Future Extensions** states in unambiguous terms interception and infiltration **not yet implemented**, and the Hairsine–Rose sediment and erosion implementation was **being prepared for future attachment**.
- 2025 peer-reviewed journal article still describes plant-porosity-dependent water-flow solver and no explicit native runoff detachment, splash, leaf-drip or dynamic canopy interception in available verified materials.
- Ion, Marinescu, Cruceanu (2024), preprint arXiv:2408.12465, describes Saint-Venant equations coupled to Hairsine-Rose erosion and numerical experiments; not equivalent to a version-identified, downloadable **full original ASTERIX canopy+sediment** implementation. No 'source proven' claim.

## Vegetation
- Plant obstruction, spatial porosity and drag in momentum flux != LAI-dependent canopy water storage, leaf-drip, RLD, or litter biomass. No evidence native LAI input/leafdrip; reject strict criteria.

## Engineering decision
**Reject** ASTERIX as complete original Gounsa event storm 2D canopy+rain/flow erosion engine. Separate hydrodynamics literature may be educational only. No original erosion full native mass/timestep QA is warranted when functionality gate fails.

## Archival citations
- https://www.sciencedirect.com/science/article/pii/S1364815225000209
- https://www.researchgate.net/publication/381652990_ASTERIX_Module_for_modelling_the_water_flow_on_vegetated_hillslopes
- https://arxiv.org/abs/2408.12465
- [2024 theory note](../papers/2024_Ion_VegetatedHillslope_HairsineRose_Erosion.md)
- [2025 water source](../papers/2025_Ion_ASTERIX_2D_VegetatedFlow.md)
- [Strict decision](../decisions/2026-10-26_STRICT_REJECTION_TREX_IBER_ASTERIX.md)
