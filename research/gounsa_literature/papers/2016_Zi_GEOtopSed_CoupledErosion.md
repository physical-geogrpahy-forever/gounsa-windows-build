# Zi et al. (2016), GEOtopSed

Zi, T., Kumar, M., Kiely, G., Lewis, C., and Albertson, J. (2016). Simulating the spatio-temporal dynamics of soil erosion, deposition, and yield using a coupled sediment dynamics and 3D distributed hydrologic model. Environmental Modelling and Software 83, 310-325. https://doi.org/10.1016/j.envsoft.2016.06.004

A numerical study with canopy-aware GEOtop soil-water hydrology, soil erosion and deposition at plot and 15 square kilometre Dripsey catchment scales. Rain and runoff erosion and time-variable sediment deposition are published. Original water solver routes overland runoff along kinematic flow direction, not two-component shallow-water momentum. Published discharge and sediment biases -1.2 and -22.4 percent.

Code availability examination: official model site identifies GitHub TanZiTT/GEOtopSed. Actual tree includes canopy rainfall partitioning in GEOtop/vegetation.c and energy.balance.c. No explicit sediment calculation file, function or active module was identified in inspected master. Therefore full exact coupled published source cannot be declared verified from this tree. No 5cm numerical precedent shown. Verdict: supporting published case, not accepted as fully verified bidirectional fine-mesh published engine. Related ../models/GEOtopSed.md
