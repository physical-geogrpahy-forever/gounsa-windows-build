# 2025 AHMS-SED: integrated land canopy/raindrop and 2D grid routed erosion (original Fortran audit)

## Why audited
Other-than-OpenLISEM full public open paper code, with actual canopy storage, separate direct throughfall/leafdrip and sediment transported in directional 2D grid. Source and published output dataset both publicly archived.

## Complete original identified
Article Jiang, Parteli & Shao 2025 DOI 10.1029/2024MS004593, Zenodo model v1.0 DOI 10.5281/zenodo.14494932 and paper input/result DOI 10.5281/zenodo.14983610. Code https://github.com/JiangCong1990/AHMS-SED, repository tree `Offline_AHMS-SED/`.

## Source physically inspected
- `Land_models/NoahMP/Noah/module_sf_noahmplsm.f` blob `ad5ea8eba279f98463589f322cc7fd95faaebb1f` L7063–7072: actual canopy water `MAXLIQ=CH2OP*(ELAI+ESAI)`; time-resolved interception QINTR and partition QDRIPR/QTHROR.
- Same source L1200–1203 **calls** `EROSION(OPT_ERO,...QDRIPR,QTHROR,RUNSRF,...)`; L9719–9731 only for `OPT_ERO=4`: Brandt directfall KE, leaf-height dripping KE, rain-splash DETRAIN.
- `Run/namelist.hrldas` default `erosion_option=1` is **not** leaf-drip-based `OPT_ERO=4`. Need archive experiment configuration to distinguish exact published path from optional original path.
- `Routing/module_rt_rt2d.F` blob `a51aa6748f6b65ba8a7bea976f8185a22fe610c9` L963–75 implicit 8-neighbor head solver, L1821–1948 sediment advection/routing + Settling, L5453 LAI-derived FBARE into USLE C crop factor. Not 2D Saint-Venant inertial momentum solve. Gravity/friction handled by level difference/implicit flow.
- `Routing/module_rt_sed2d.F` blob `73126ffbc63c2f5d087ed5073bf2c5bba3ac815b` includes additional original draft EUROSEM source, **excluded** from official `Routing/Makefile` (OBJS list only `module_rt_rt2d.o`, no `module_rt_sed2d.o`) and **`rt_sed` is not called** from active routing file. Draft is incomplete with non-Fortran orphan identifiers. Cannot call this native shipped compiled module.
- `NoahMP` active rainfall-splash optional output DETRAIN and subsequent separate routed flow-erosion require input-output detailed wiring to conclude both are summed for a given paper run. Current source has 5 options, not all active at once.

## Published actual grid
**20 km DX, 60-minute Δt**, 1979–1987 Yellow River. 30m DEM is preprocessed; **not 30m or 5cm native erosion physics**. Even when 8-neighbor directions allow X/Y movement, it is not equivalent to 2D SWE velocity/inertia solver.

## Verdict
This is the best **new fully open independent code + canopy KE + erosion modules integrated in published architecture** identified this turn, but **fails user's actual <=10cm precedent and strict free 2D SWE**. Do not promote merely by an optional unselected Noah-MP branch. Keep as scientific study and realistic publicly inspectable original, not operational gounsa cm main.
