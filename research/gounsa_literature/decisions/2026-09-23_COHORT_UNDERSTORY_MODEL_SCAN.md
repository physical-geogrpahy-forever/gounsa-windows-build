# Cohort vegetation models with understory and succession

Date: 2026-09-23

## revised target
The vegetation engine should be less complex than an explicit individual-tree model but finer in time and/or space than a conventional forest-landscape model.

Mandatory ecological functions:
1. cohort/PFT vegetation, not explicit individual-tree coordinates
2. understory herbs/grasses and preferably shrubs
3. endogenous succession via recruitment, competition and mortality
4. quantitative live root state
5. litter/dead-root state
6. post-disturbance recovery

Mandatory coupling question:
A geomorphic storm can change DEM, soil depth, moisture, burial and root exposure within hours. Therefore a candidate must eventually allow event-time restart/state replacement even if plant growth itself is slower.

## candidate 1: BiomeE / BiomeEP

### strengths
- cohort vegetation demographic model
- trees, shrubs and grasses
- upper/lower canopy structure via PPA
- fine-root C and litter/SOM
- physiology at hourly scale, growth/phenology daily, demography annual
- recruitment, mortality and resource competition create succession
- 2026 study validated 150 years of succession on three 50x50 m plots with 72 species and five PFTs; shrub PFTs explicitly contributed
- standalone code plus R/Fortran `rsofun` implementation
- user-defined initial cohort and soil state; multi-site parallel execution possible

### weaknesses
- site/tile model rather than native x-y landscape
- no built-in intercell seed dispersal
- mature native wildfire module not confirmed
- arbitrary storm-time state restart and dynamic soil-depth replacement not yet verified

### current role
**Primary lightweight/middle-complexity candidate.**

## candidate 2: ED2 / EDv3

### strengths
- cohort-based Ecosystem Demography framework
- subhourly biophysics and ecohydrology
- grass PFTs; shrub PFT implementations exist
- roots, soil water, biogeochemistry
- recruitment, mortality, disturbance and succession
- soil depth, slope, aspect, elevation and topographic moisture inputs possible
- standalone/open code lineage

### weaknesses
- disturbance patches are spatially implicit fractions with no x,y
- heavier than BiomeE
- a GIS tile wrapper would be needed for fine geomorphic location

### current role
**Primary high-process-fidelity cohort candidate.**

## candidate 3: FATES

### strengths
- PFT- and size-resolved cohorts
- upper canopy and understory canopy layers
- tree, shrub, C3/C4 grass PFTs
- fine roots, fine-root litter, leaf litter, AG/BG CWD
- competition for light, water and nutrients
- seed/recruitment/mortality
- SPITFIRE fire/fuel framework
- subdaily host-land biophysics
- robust restart infrastructure

### weaknesses
- disturbance patches have no geographic x,y location
- not a lightweight standalone executable; normally embedded in CTSM/CLM or ELM
- substantially more implementation complexity than BiomeE

### current role
**Ecologically most complete cohort candidate, technically heavy.**

## candidate 4: LANDIS-II NECN

### strengths
- native raster landscape cells
- species-age/biomass cohorts
- seed dispersal and spatial succession
- trees, shrubs and grass species
- grass-woody regeneration competition
- fine/coarse live root biomass
- dead fine roots, dead coarse roots, leaf litter and woody debris
- fire integration
- much simpler spatial coupling than ED/FATES

### weaknesses
- native ecosystem time step is monthly
- LANDIS succession/demography execution can be much coarser in applications
- standard framework is not designed for soil depth and vegetation state to be changed immediately after every storm
- intended landscape scale is generally much larger than the Gounsa study area

### current role
**Best native-spatial simple cohort candidate, but event-time coupling is the decisive problem.**

## candidate 5: JULES-RED

### strengths
- RED demographic mass/size classes by PFT
- JULES surface carbon/water/energy usually 30-minute timestep
- natural PFTs include multiple tree types, evergreen/deciduous shrubs and C3/C4 grasses
- tree-shrub-grass competitive hierarchy in the JULES vegetation framework
- leaf/root/stem carbon and litterfall
- interactive fire infrastructure exists in JULES/INFERNO

### weaknesses
- RED integration remains a land-surface/ESM framework and is not simpler operationally than BiomeE
- fine spatial landscape location and seed dispersal are not its strengths
- current RED branch/access and feature maturity are less straightforward than BiomeE/ED/FATES

### current role
Secondary candidate, not a priority unless its mass-class simplicity becomes attractive.

## candidates deprioritized

### PnET-Succession
- monthly physiology and good woody cohorts
- but understory herb/shrub representation is weaker than NECN/BiomeE/FATES

### ForClim
- size-cohort/gap approach and succession
- understory largely tree seedlings/saplings; herb/shrub layer insufficient

### LandClim
- 25 m landscape cells and succession/fire
- tree-focused state; quantitative herb/shrub root and litter biology insufficient

### 3D-CMCC-FEM
- daily process model and cohorts
- published remote-sensing work explicitly does not account for undergrowth grass/shrub photosynthesis

### CABLE-POP / ORCHIDEE demographic variants
- cohort demography exists
- recent intercomparison indicates weaker/directly absent between-PFT competition in important configurations; therefore less suitable for postfire grass/shrub-to-tree succession

### standard LPJ-GUESS
- trees plus herbaceous understory and strong physiology
- spatially implicit independent patches remain the known Gounsa problem

## current shortlist for direct technical testing
No final model is selected yet.

### A. BiomeE/BiomeEP
Test first because it is the closest to the desired complexity level.
Required code audit:
- arbitrary-date restart
- export/import cohort state
- update soil depth and soil water after a storm
- root profile and litter outputs
- multiple GIS-cell wrapper
- initial postfire grass/shrub/tree state

### B. ED2/EDv3
Test if BiomeE cannot handle event-time state modification.
Focus:
- per-site restart
- soil-depth update
- shrub/grass PFT implementation
- computational cost for many 10-50 m tiles

### C. FATES
Use if native fire and complete understory/root/litter ecology justify the heavier stack.

### D. NECN
Retain as the spatially cleanest fallback if monthly/event coupling can be modified defensibly.

## key new conclusion
The search target should no longer be framed as 'forest landscape model versus individual-tree model'.

The relevant middle class is:
```
spatially tiled vegetation demographic model
+ cohort/PFT demography
+ tree/shrub/grass competition
+ fine-time physiology
+ externally event-updatable soil/geomorphic state
```

BiomeE, ED and FATES are the strongest examples found. NECN occupies the simpler raster end of this spectrum.
