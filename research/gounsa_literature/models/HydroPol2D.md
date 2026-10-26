# HydroPol2D — LAI interception + true 2D water, but pollutant washoff is NOT physical soil erosion

## Identity, original release source
Source: https://github.com/marcusnobrega-eng/HydroPol2D MIT? **No**: GitHub repository license GPL-3.0. Research MATLAB 2D hydrology / hydrodynamics model with local-inertial or cellular-automata overland flow, spatial Green–Ampt or Darcy infiltration, 2D shallow groundwater, pollutant wash-off and water-balance/validation examples; updated 2026-09-18. [Primary repository](https://github.com/marcusnobrega-eng/HydroPol2D).

## Original source actually read on 2026-10-26
- `HydroPol2D_Functions/interceptionModel.m` implements Rutter-style storage-based canopy water with actual raster LAI, `S_max=C*LAI` [mm], storage `S`, throughfall `T=max(S-Smax,0)`, interception evaporation and physical interception mass-balance check; `C` is an example fixed 0.2 mm/LAI and generic, not calibrated for Miscanthus vs oak.
- `HydroPol2D_Functions/interception_module.m` wires `LAI_raster.Z` to `interceptionModel`, passes precipitation & potential ET and stores fluxes; native forest canopy quantity really affects rainfall and surface flow.
- README confirms 2D overland local inertial option, groundwater and pollutant buildup/wash-off. Pollutant dynamics based on pollutant specific `C1` maximum buildup [kg/ha], `C2` buildup [day-1], `C3` empirical mass-washoff and `C4` exponent: this is *not* physically based soil grain detachment, deposition, Hairsine–Rose, sediment concentration, bed slope and 2D finite sediment mass.
- Original default-branch GitHub search `sediment`, `erosion`, `splash` returned zero matches in project files, despite `interception` having many results. A search miss alone is not proof, but original published scope explicitly pollutant (not sediment mass erosion). No sediment test case or original source demonstrated.
- Public source but **MATLAB + toolboxes required**, open source code != free computational toolchain. No native executable/slope sediment convergence test done since essential explicit runoff-erosion process absent.

## Gounsa fit verdict
**Reject original all-in-one Gounsa 2D forest water erosion engine**, despite quantitative LAI canopy and actual native 2D hydrodynamics. Different water quality/washoff chemistry cannot be passed off as soil erodibility/runoff erosion, and no empirical custom erosion coeff patch is justified.

## Distinct role
Useful comparison of Rutter canopy water (LAI inputs) and stable local inertial water when designing clearly labeled **new coupling**, only after a validated 2D sediment engine exists.
