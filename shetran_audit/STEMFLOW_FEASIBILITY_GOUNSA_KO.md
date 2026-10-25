# SHETRAN v4.7.5: oak coppice vs. dense Miscanthus stemflow feasibility

**Status: architecture feasible, full in-model scientific implementation NOT yet complete.**

Official source verified at commit cf9cd540add78ad3accbaf62b4199d2032887f6b.

1. ETmod.f90 combines free-throughfall and canopy drainage; no dedicated spatial stemflow flux or trunk storage.
2. run_sim.f90: ETSIM precedes VSSIM, OCSIM and SYMAIN, permitting redistribution inside this single model before infiltration and runoff; revise ET surface-evap timing if necessary.
3. VSmod.f90 uses PNETTO for infiltration. A stem receiving **grid cell** can be supplied with routed rainfall but within-cell near-stem infiltration hotspots are NOT resolved by this alone. Dense grass culms and clustered coppice stems require subgrid two-area infiltration or suitably fine local mesh.
4. SYmod.f90: SYWAT computes direct raindrop intensity from PNETTO - DRAINA. Separately routed stemflow MUST be excluded from rainfall kinetic-energy calculations, but included as actual water input to shear-producing runoff.
5. FRmod.f90: BALANC(13) records CSTORE. Add trunk storage there, including hotstart and water ledger, to prevent apparent losses.
6. ETmod.f90 and SYmod.f90 use MIN(CLAI,1)*PLAI, saturating interception/shelter area response above CLAI=1. Couple effective canopy cover and capacity to actual LAI with validated equations.
7. Sediment mass balance routine BALSED is empty and needs replacing with an independent diagnostic.

## Verified candidate algorithm

The files stemflow_spatial_core.f90 and test_stemflow.f90 are **independently compiled and unit-tested only**, not integrated with official SHETRAN. Native gfortran passed:
- donor/recipient water-volume balance residual = 0 m3.
- illustrative equal-stemflow water source, infiltration footprints grass 0.40 m2 versus oak 0.02 m2: local intensities 4 versus 80 mm/h.
- trunk storage delayed discharge after input rainfall ends.

These 4 and 80 mm/h numbers are hypothetical illustrative diagnostics, NOT actual input to SHETRAN-VS and NOT model predictions. Structural stem-capture fractions and infiltration footprints require actual Miscanthus and Quercus measurements.

## Next gates before claiming the project is solved

1. Integrate stemflow state/flux **inside** SHETRAN and prove hydrologic mass balance with evaporation and snow/hotstarts.
2. Implement subgrid dual-domain near-stem infiltration and root macropore flow, or use defensible fine mesh.
3. Correct sediment coupling to exclude SF from splash KE but retain its water for runoff-flow detachment.
4. Verify hillslope detachment, transport, deposition and mass conservation with no channel influence.
5. Re-run 10,20,30,40,50 mm/h one-hour events on a small hillslope, not on the multi-month Cobres catchment.

Sources:
https://github.com/nclwater/Shetran/blob/master/src/evapotranspiration/ETmod.f90
https://github.com/nclwater/Shetran/blob/master/src/subsurface/VSmod.f90
https://github.com/nclwater/Shetran/blob/master/src/driver/run_sim.f90
https://github.com/nclwater/Shetran/blob/master/src/sediment/SYmod.f90
https://github.com/nclwater/Shetran/blob/master/src/frame/FRmod.f90
https://doi.org/10.1002/hyp.70556
https://doi.org/10.3389/ffgc.2020.00061
