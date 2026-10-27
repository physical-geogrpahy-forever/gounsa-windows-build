# Long & He (2009–2010) 2D Gash-canopy water erosion model — lineage and executable availability

## 실제 확인
References:
- Long & He (2009), *Journal of Information and Computational Science* 6(6):2349–2356: 2D SWE FVM + Green–Ampt + modified Gash interception + separate erosion/deposition + evolving rills.
- Long & He (2010), *Journal of System Simulation* 22(2):348–352: 2D SWE + Green–Ampt + modified Gash interception + empirical erosion/deposition + dynamic microtopography + point-implicit friction.
- Long & He (2009), IEEE ICIECS DOI 10.1109/ICIECS.2009.5363863: separate GPU HLLC 2D SWE/erosion/bed update but its abstract does **not** mention canopy.
- Long (2017) *Journal of System Simulation* DOI 10.16182/j.issn1004731x.joss.201703007: later GPU CA erosion paper cites 2010 study, but later CA code is **not** demonstrated equivalent to earlier 2D-Gash finite-volume solver and lacks native canopy in abstract.

## Original source availability direct audit
- Actual original public Gounsa repo `INDEX.md` had no canonical record.
- Public web targeted exact English/Chinese model title and authors and code, coupled `modified Gash` and `rill`. Only publication pages, citation by 2017 journal and proceedings abstracts found.
- Connected GitHub repository searches `"Mansheng Long" erosion`, `"ManshengLong"`, `"Dongjian He" erosion`, `"rill evolution"`, `"modified Gash" shallow water` -> no model source repository.
- Connected GitHub code search `"rill evolution" "Gash"` -> zero results; `"modified Gash" "erosion"` yielded unrelated corpus text, not original solver. Search absence is **not proof** that privately held or independently archived code doesn't exist.
- Full original 2009/2010 PDF and particular **published cell width**, time step, mass-balance figures **not obtained**. Cannot claim verified 5–10cm or release-ready.

## Scientific requirement evidence
| Required | 2009/2010 published abstract | Released executable audit |
|---|---|---|
| Truly 2D SWE | YES | no source |
| Canopy interception | modified Gash YES | LAI input/source not proved |
| Green-Ampt infiltration | YES | no code |
| rainfall / runoff erosion | empirical erosion and deposition YES, **separate splash and flow detachment terms not verified** | no code |
| Local deposit / morphodynamic feedback | YES, abstract | no cell DoD benchmark |
| 0.05–0.10m native mesh | **unknown** | unknown |
| Public matching original software | **not found** | FAIL for current operational decision |
| forest Miscanthus/oak canopy effect | **not proven** | unknown |

## Decision
**Important new paper-level physical match but NO-GO for immediate original-only simulation** until verifiable same-source code and actually published cm-size convergence. This advances the literature (the complete physics has been published at equation/model level), not the implementation availability.

## Reference DOI
https://doi.org/10.1109/ICIECS.2009.5363863
https://www.china-simulation.com/CN/abstract/abstract1200.shtml
https://eurekamag.com/research/099/685/099685317.php
