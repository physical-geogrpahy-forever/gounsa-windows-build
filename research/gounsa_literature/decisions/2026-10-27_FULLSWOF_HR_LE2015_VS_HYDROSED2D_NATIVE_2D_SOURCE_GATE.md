# 2026-10-27 Original-source numerical truth audit: HydroSed2D vs Le 2015 FullSWOF-HR

## Scope and existing literature
- User explicitly insists on *code-first* after multiple previously failed model recommendations. OpenLISEM v7.5.2 native repair is assigned elsewhere to Work.
- Read SYSTEM/MASTER/INDEX, latest decisions. Existing [HydroSed2D Fortran source audit](../models/HydroSed2D_Fortran_Original_Source_Audit.md) already in repo; this session **updated canonical rather than duplicated model file**.
- New primary DOI https://doi.org/10.1002/2014WR015690 was NOT in INDEX at start, so [Le et al. 2015 paper canonical](../papers/2015_Le_Cordier_Lucas_Cerdan_FullSWOF_HairsineRose_2D_Sediment_Splitting.md) created.
- New code lineage [FullSWOF base vs Le 2015 study extension audit](../models/FullSWOF_2D_2015_Le_HairsineRose_CodeLineage_And_Numerical_Gates.md).

## What was actually examined in real original code

### HydroSed2D v1.0 PSU official
- https://github.com/psu-efd/HydroSed2D, full GPL Fortran source. `src/swefvm.f90` main L50-76 `init→swe→if(sedimentctl==1&&scalc==1) sediment→output→advance time`, with no rain-effective input preceding flow solve.
- `src/initialization.f90` L47-90 reads prescribed inlet/outlet h,u,v,Q, time step and sediment switch, mesh, terrain and `sediment.dat`. Canopy, LAI, direct rain/rain splash fields absent. Entire 11 .f90 modules in `Makefile` and source keyword probes for `rainfall/canopy/LAI/splash` no active pathways.
- `src/sediment.f90` L23–55 actual calc_shear, Shields, MPM/Grass bedload, edge vector flux divergence and Exner bed elevation. `sediment.f90` L174-199 only 1 median sediment diameter (MPM critical shield or Grass velocity power), and L289-299 Exner `dz= -sedInterval*dt/(1-porosity) * divqb/area`.
- There are **no source terms for rain-impact soil detachment and no Hairsine–Rose multiple suspended sediment classes/settling cycle**. Flow momentum 2D is real (unstructured finite-volume), but bedload for river morphodynamics not appropriate native rainfall vegetation interrill/overland.
- Extra numerical caveat: sediment.f90 `calc_shear` iterates all nFaces without local dry guard before dividing by `Q1(i)^(4/3)`. Can be singular if Q1=0 in dry cells, but hydrology may clamp, **potential not verified bug**. Needs running to prove; do not claim measured stability failure.
- No native compile or simulation: container gfortran available but network cannot resolve GitHub codeload; exact Fortran code retrieved only through GitHub connector, not staged to compiler. **Public availability≠this investigator's successful build**.

### Le et al. 2015 FullSWOF HR genuine 2D scheme
- DOI https://doi.org/10.1002/2014WR015690, Water Resources Research 51,987–1005. Authored Le, Cordier, Lucas, Cerdan. Wiley full HTML sections §2–4.3 read.
- Published single numerical 2D finite-volume shallow water + Hairsine–Rose multiple size classes, actual rain-detachment, flow-entrainment, redetachment and deposition m_i, within-flow advective c_i, changing zbed. This is **scientifically stronger rain-vs-flow and deposited-layer shielding** than HydroSed2D bedload.
- Main numerical result: avoids extra small sediment timestep for nonnegative concentration, by analytic deposition and Strang-splitting, hydrology standard CFL is enough; in their demonstration speedup ≥100x relative to earlier implementation. **Not evidence for other solvers**.
- 2D application 10m×4m V-slope, longitudinal/transverse 1%, 70mm/h 120min in sandy Thiès Senegal field, infiltration Green-Ampt and 10 grain classes.
- Crucial §4.3 **actual stream power too low for runoff-driven detachment; particles principally detached by rainfall and transported by flow**. Consequently demonstration is not 2D steep high-discharge active flow-scour verification.
- Numerically verified 0.05m mesh **not proven**: published web text does not identify precise dx/dy, do not infer from microtopography.
- Native canopy LAI interception/dynamic throughfall/leaf-drip KE **not demonstrated in modified 2015 scheme**.
- Baseline pure water code publicly released: https://github.com/BUCEA/FullSWOF_Rif `README.txt` states 2D v1.07.00 (2016), `Makefile` links libs `librain_infiltration,swe schemes,flux,etc`, **not Hairsine–Rose sediment libraries**. Paper explicitly reports adding erosion to FullSWOF source; exact modified code/runfile release **unavailable in identified public tree**.
- Official https://www.idpoisson.fr/en/fullswof/ lists full open FullSWOF_2D hydraulic and 2021 1D transport branch, but not publicly traceable Le2015 exact full 2D sediment source.

## Comparing scientific code truth
| Requirement | HydroSed2D released source | Le2015 research model + publicly located source |
|---|---|---|
| True 2D xy hydrodynamics | yes Fortran `swe` | yes scientifically, base FullSWOF C++ public |
| Actual rain forcing | no in released Fortran main | yes in paper, FullSWOF base |
| Native LAI interception reservoir / throughfall / leafdrip | no | no evidence |
| Rain-impact sediment detachment | no | yes in paper but exact modified source unlocated |
| Flow-induced detachment and multi-class suspended transport | bedload flow only, no multi-class concentration | published HR implementation; **2015 2D plot stream-power subcritical so active flow detachment negligible** |
| Per-cell deposition and geomorphic elevation update | yes Exner bedload | yes HR layer, paper |
| Identical published full original released source | yes for v1.0 bedload | NO: 2016 FullSWOF base only |
| Actual ≤0.1m spatial mesh and stable strong storm | no | mesh unknown |
| Gounsa native direct main | **NO-GO** | **NO-GO**, method reference only |

## Final decision
**No model promoted**. HydroSed2D's genuine free XY bedload solver fundamentally lacks rain/interception/splash. Le 2015's genuinely developed erosion/deposition 2D model has academically robust nonnegative numerical scheme but exact 2015 final sediment code and canopy do not exist in located public release, and 2D test did not activate flow erosion substantially. Do not confuse publicly released FullSWOF hydraulic base with the research erosion extension. Work handles OpenLISEM separately.

## Provenance
- https://github.com/psu-efd/HydroSed2D/blob/master/src/swefvm.f90
- https://github.com/psu-efd/HydroSed2D/blob/master/src/sediment.f90
- https://doi.org/10.1002/2014WR015690
- https://github.com/BUCEA/FullSWOF_Rif/blob/master/Makefile
- https://www.idpoisson.fr/en/fullswof/
