# v0.7 scientific decision

The recommended production workflow is now:

1. Run one **baseline TREED state** with the chosen starting climate/soil/vegetation setup.
2. Save `treed_rootC_areanorm_gC_m2.asc`.
3. Choose a documented root-cohesion benchmark appropriate to the scientific question.
4. Use `calibrate_event_cohesion.py` to infer one fixed event-scale `Tr_eff`.
5. Freeze that `Tr_eff` across all experimental scenarios.
6. Let Hwang Eq. (5) translate subsequent TREED root-biomass changes into dynamic root-cohesion changes.

This is preferred over using ordinary mean tensile-strength profiles directly, because v0.6 demonstrated that those profiles produce ~170–190 kPa for the current TREED baseline biomass, whereas Coweeta and Korean reinforcement benchmarks are generally in the single- to low-tens-of-kPa range.

`Tr_eff` is an inverse-calibration coefficient for a simplified reinforcement model. It must never be described as a measured species tensile strength.
