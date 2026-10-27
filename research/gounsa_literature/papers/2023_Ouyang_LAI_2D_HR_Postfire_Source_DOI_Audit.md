# Ouyang et al. (2023) — LAI interception, genuine 2D runoff and HR sediment integrated study

Ouyang, C., Xiang, W., An, H., Wang, F., Yang, W., & Fan, J. (2023). Mechanistic analysis and numerical simulation of the 2021 post-fire debris flow in Xiangjiao catchment, China. *JGR: Earth Surface, 128*, e2022JF006846. https://doi.org/10.1029/2022JF006846

## Search reason and study type
Single peer-reviewed study that has actually coupled LAI-informed canopy interception, Green–Ampt infiltration, 2D x/y shallow-water runoff, raindrop and flow erosion, sediment deposition, morphodynamics. Steep postfire mountain catchment study with field comparison and author source archive DOI.

## Native published processes and methods
Section 4.2: LAI from remote sensing NDVI and land use. Section 4.5.1: Aston (1979) canopy interception with cumulative canopy storage, maximum capacity, canopy density and LAI (NOT a published Rutter or explicit leafdrip KE). Section 4.5.2: Green–Ampt infiltration. Section 4.5.3: Hairsine–Rose five grain classes, independent splash/flow detachment and reentrainment, suspended transport and settling/deposition with deposited shielding. Section 4.5.4–5: genuinely bidirectional x/y 2D shallow-water and finite difference MacCormack–TVD second-order coupled runoff, sediment and debris flow. Section 4.6: models are activated first canopy+infiltration then runoff+erosion and continue through event. Original fire-disturbed 4-cm surface layer initialized as deposited loose sediment (NOT computational grid size). Specific soil and canopy c0=0.5, throughfall Tc=0.35 are site parameters, not Gounsa oak/grass physical constants.

## Actual environment, inputs, verification
Steep Xiangjiao mountain basin, mean slope 29deg; burned forest and July 5 2021 debris flow. 10m Ziyuan-3 DEM and 30m Landsat spectra, 0.98m optical images; NOT published 5–10cm actual simulation, nor an established 10cm compute mesh. Inundated area modeled 59.8ha versus observed 50.1ha, erosion depth local comparators (2.32/1.25/1.91m simulated, 2/1.2/1.4m field). Actual late debris-flow solid fraction up to 0.47, not typical mild sheet flow. High-resolution site patches/canopy-on vs off ablations NOT independently validated at cm.

## Exact source citation and access integrity
Publisher Data Availability explicitly says author model source code version 1.1 deposited at Zenodo https://doi.org/10.5281/zenodo.7269322 and rainfall/soil input data https://doi.org/10.5281/zenodo.7269648. **Same paper references code release as version 1.0.0 at identical DOI**; version mismatch unresolved. This session Zenodo record and API cannot be opened (DOI redirect fails in web, container cannot DNS resolve Zenodo). **No manifest, no actual source archive bytes read, no native compile/run, no original code implementation verified.** Paper claiming source release is not equivalent to actual successful download. No 5/10cm convergence, all-four open boundaries and finite soil stock proof.

## Model application and verdict
The published integrated model has probably the closest process scope among source-archived mountain studies not already rejected, but exact published code source unverified until Zenodo archive inspected. Original 10m DEM means cannot treat as published 5cm precedent. ASTON canopy empirical storage not canopy-drip drop-size kinetic energy; original erosion model multi-class HR valid at their site only. **Final: highest-priority source DOI lead, experimental adoption HOLD, not fully verified source or fine grid.**

## 2026-10-28 follow-up: numerical scale and source retrieval checked (correction)
- Publisher §6.1 states simulations used **10m spatial resolution**, not merely a 10m input DEM. This establishes paper's COMPUTATIONAL scale at 10m, not 5cm. Primary https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2022JF006846 .
- DOI https://zenodo.org/api/records/7269322 / `https://zenodo.org/records/7269322` tried via web and container. Web inaccessible, container requests raise DNS resolution error. No original archive bytes opened; source remains paper-declared not retrieved. This access error does NOT prove the archive was deleted.
- Compared Kim et al.2023 DOI10.1029/2022WR033879 real 0.1m 2D erosion mesh. The latter explicitly uses BARE soil and no canopy or infiltration; one must not treat complementing its 2D grid evidence with Ouyang canopy paper as a single already-tested 10cm forest model.
