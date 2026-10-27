# RDycore — 2026 original native sediment source vs documented Hairsine–Rose

## Search and model status
Existing peer reviewed hydraulic references and open repo https://github.com/RDycore/RDycore ; explicit Hairsine–Rose paper cited by docs/theory/sediment.md is Kim, Ivanov & Katopodes (2013), https://doi.org/10.1002/wrcr.20373. This audit does NOT infer RDycore implements Kim's published full solver merely from equations appearing in documentation.

## Spatial and flow architecture
Current public C / PETSc / libCEED distributed shallow-water 2D and N-class sediment/tracer advection. src/tracer/tracer_roe_flux_petsc.h includes Roe flux; src/operator_sources_petsc.c selects tracer sources with sediment.num_classes>0.

## Actual calculation source verified
- src/tracer/tracer_sources_ceed.h L37–71 implements per-class shear erosion e[j]=kp_constant*(tau_b-tau_critical_erosion)/tau_critical_erosion and deposition d[j]=settling_velocity*c[j]*(1-tau_b/tau_critical_deposition).
- src/tracer/tracer_petsc.c lines 633–636, 701–706 implements same, constants kp0.001, settling0.01, erosion critical0.1, deposition critical1000. This is simpler shear erosion/deposition, not full published 2D H-R rainfall and flow detachment, loose-layer mass state and coupled z evolution proven in code.
- docs/theory/sediment.md DOES list full Hairsine-Rose rain detachment, flow detachment, deposited-layer state and Exner; documentation theory != active compiled model version.
- driver/tests/sediment/sediment.yaml has 5x10 dam-break mesh, two sediment classes, timestep0.01s and no canopy/rain splash.
- No quantitative vegetation LAI throughfall/leaf-drip rain KE source identified in main sources, no exact cm-plot canopy erosion native benchmark confirmed.

## Status
Excellent public 2D water and tracer numerics comparison candidate. Fails original unchanged canopy + raindrop detachment + morphological feedback source proof. Do not propose as ready substitute for tRIBS-FEaST or classic LISEM. Formula missing explicit threshold clipping in inspected source deserves independent tests, but this audit did not run the code.

## Reference
- https://github.com/RDycore/RDycore/blob/main/docs/theory/sediment.md
- https://github.com/RDycore/RDycore/blob/main/src/tracer/tracer_sources_ceed.h
- https://github.com/RDycore/RDycore/blob/main/src/tracer/tracer_petsc.c
- https://github.com/RDycore/RDycore/blob/main/driver/tests/sediment/sediment.yaml
- Related decision: ../decisions/2026-10-28_SINGLE_REFERENCE_4_CORE_MODELS_PRIMARY_PAPER_NATIVE_SOURCE_REAUDIT.md
