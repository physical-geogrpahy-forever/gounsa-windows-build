# LORICA–TREED v1.0: 30-year continuous integration run

This branch advances the current lorica-treed-v1.0-integration code at commit 50482933823b347d23aa184d5b3b8477aa320492.

## Run design

- 30 consecutive annual LORICA timesteps, calling the native every_timestep() method for each year.
- Native annual order: TREED state update → LORICA daily weather and water balance → water erosion/deposition → rainfall-triggered shallow landsliding → soil-layer and DEM update.
- TREED root carbon is converted to root cohesion with Hwang et al. (2015), Eq. (5), and FPC is passed to the existing LORICA ET correction.
- The traits_restart.jld2 state is retained across all 30 annual TREED calls.
- The v1.0 integration choices are retained: treed_bare_bedrock_policy=zero_coupling and treed_ks_refresh_mode=annual.
- The 3.4 kPa published sensitivity level is used as a stress forcing so the 5×5 coupled process domain can exercise the shallow-landslide and residual-sediment pathway. The fixed effective root tensile strength is first calibrated against the existing 7.6 kPa baseline; it is not recalibrated by year.

## Forcing and domain

The pre-Gounsa integration run uses the existing 5×5, 10 m radial-bowl process domain and repeats the already-used three-year forcing sequence ten times:
- annual precipitation: 730, 900, 600 mm;
- mean annual temperature: 10, 11, 12 °C;
- one 60 mm / 6 h event per year, with the remaining annual precipitation distributed over the other 364 days.

This is a controlled 30-year process-integration run, not a Gounsa catchment prediction or a climate validation. Gounsa spatial inputs and site-specific forcing are the next stage; no new fire or other disturbance module is added.

## Required state continuity

Each annual step records and checks:
- TREED input DEM and soil depth against the LORICA state at the start of that year;
- root carbon, FPC, LAI, root cohesion, and ET transfer;
- annual runoff, water erosion, deposition, landslide initiation, erosion and deposition;
- soil mass, layer-resolved soil texture/SOM, persistent landslide sediment, DEM, and soil depth;
- TREED restart presence and size.

ASCII DEM/soil-depth exchange uses six decimal places. State-transfer checks therefore use the file's half-unit rounding tolerance (5.1e-7 m), rather than demanding precision beyond the exchange format.
