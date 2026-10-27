# Ouyang 2023 — actual peer-reviewed integrated forest interception → infiltration → 2D shallow-water flow → Hairsine–Rose morphodynamics

Original publication https://doi.org/10.1029/2022JF006846 and publisher-declared archive https://doi.org/10.5281/zenodo.7269322 . 2023 Xiangjiao fire storm case.

## Process integration evidence
Original §§4.2,4.5.1–4.5.5 states LAI from remote sensing; Aston-style cumulative rainfall interception related to canopy density and LAI + Smax; Green–Ampt; five-class Hairsine–Rose E rain- and flow-driven detachment/reentrainment, settled mass/deposited layer and bed elevation; real X/Y SWE u,v solved by MacCormack-TVD FDM; 4.6 sequence canopy + infiltration then runoff+erosion. This is one actually simulated published integrated research model, NOT hypothetical combination. Site mean hillslope 29 degrees and actual postfire debris flow calibrated/field checked. Source DOI in Data Availability; paper itself says code version 1.1 while bibliography says v1.0.0 at same DOI. Do not resolve by assumption.

## Critical gates
DEM input 10m satellite, Landsat 30m; NOT real 5cm simulation. Original source actual bytes inaccessible to current agent via DOI Zenodo error and DNS; source code code paths, compiler, test and exact same-run canopy/SWE/HR call stack NOT verified. No evidence for explicit leafdrip-kinetic-energy mechanism (Aston interception empirical), nor Miscanthus/oak species canopy dynamics; 5–10cm native timestep convergence, all 4-edge open sediment balance and erodible stock not verified. Model includes extreme debris flow phase 47% solids; Gounsa sheet erosion physically distinct.

## Verdict
Highest-priority new *exact paper + author source DOI* lead. Still no direct native reproducibility. No-GO for final use until code archive downloaded/audited and cm benchmark verified. Peer-reviewed paper scientific architecture passes same-study criterion only.

See ../papers/2023_Ouyang_LAI_2D_HR_Postfire_Source_DOI_Audit.md
