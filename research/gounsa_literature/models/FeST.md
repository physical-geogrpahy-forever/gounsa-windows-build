# FeST (Politecnico di Milano): LAI canopy and sediment routing but not hillslope true 2D

## Identity
Politecnico di Milano Real Time Hydrology Group FeST official code repository launched March 26, 2024 at https://chiselapp.com/user/giovanni.ravazzani/repository/fest/doc/trunk/README.md. Dynamic LAI canopy source docs https://www.fest.polimi.it/reference/canopy.html ; publicly FORD-generated source documentation https://www.fest.polimi.it/doc/module/sediment.html . Code license stated GNU GPL in FORD.

## Native quantitative canopy
Official reference canopy storage `C_t=Cmax*LAI/LAImax`, evolves canopy store per timestep; throughfall for vegetation fraction `R_eff=f_v*T+(1-f_v)*R`. Canopy state real and LAI quantitative. Stemflow mentioned conceptually, not proven explicit native per-stem.

## Native sediment module
Official `Sediment.f90` described in FORD under procedures `InterrillDetachmentRate`, `SedimentRouting`, `ComputeSlopeFactor`, `ChannelDetachmentRate`. Soil erosion follows Sun et al. (2002) EROSET-style USLE/RUSLE `C,K` factors and storm runoff, **sediment follows `sedFlowDirection` and channelized Muskingum–Cunge transport**, not a conservative 2D surface sediment-advection PDE. FORD descriptions note interrill raindrop detachment and channel erosion, not explicit hillslope cell-scale 2D overland flow entrainment/rill incision. `SedimentRouting` doc describes hillside with water-flow rate not defined (Flow Routing code 0).

## Verdict
**Reject strict Gounsa complete native 2D surface erosion engine**. Fully maintained hydrologic component does not compensate for routing dimensionality and empirically RUSLE-derived erosion source. Do not claim a numeric Gounsa build/stability pass; none performed.

## Primary official sources
https://www.fest.polimi.it/fest-official-code-repository/
https://www.fest.polimi.it/reference/canopy.html
https://www.fest.polimi.it/doc/module/sediment.html
