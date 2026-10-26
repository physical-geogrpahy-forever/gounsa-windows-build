# Gounsa Rutter-type canopy module (design prototype only)

- `canopy_event.py`: separate spatial direct throughfall, canopy drainage/leaf drip, and (optional) water-only stemflow with a retained canopy reservoir.
- `test_canopy_event.py`: 6 Python unittest suites covering zero-LAI, heterogeneous LAI 2D arrays, 1h pulses and subsequent drainage, 10-50 mm/h, partitioned stemflow, negative input errors.
- The provisional `Smax=LAI*smax_per_lai`, `Tc=exp(-k_gap*LAI)` are **new independently constrainable parametrizations**, not calibrated Miscanthus or oak values and not native McGuire 2016/CSDMS SWEHR code. Drainage follows Rutter/Shuttleworth-style `D=Kc exp(gc (C-S))` implicitly integrated.
- `stem_frac_of_drain` is *optional scenario partition* (default zero); actual stemflow spatial delivery not yet coded. No leaf-drip kinetic energy or soil splash attenuation, 2D surface water or sediment physics is implemented here. DO NOT claim coupled 2D erosion results.
- Test parameters are **numerical examples only** not Gounsa measurements. C canopy model not yet integrated into SWEHR.
- Do not mix direct rainfall kinetic energy with canopy drip, do not treat canopy-stored water as permanent water loss.
- Canonical model/data scope: [decision](../../research/gounsa_literature/decisions/2026-10-26_DEADLINE_GOUNSA_MODEL_ARCHITECTURE_AND_DATA_PLAN.md).

Run `python -m unittest discover -s experiments/gounsa_deadline_20261027 -p 'test_canopy_event.py'` (requires numpy).
