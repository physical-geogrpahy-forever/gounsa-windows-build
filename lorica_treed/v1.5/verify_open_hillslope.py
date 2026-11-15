#!/usr/bin/env python3
"""Audit true 3-year native TREED-LORICA open-hillslope A/B results.

Synthetic open boundary, not a field-calibrated Gounsa prediction.
Only beta changes between the two runs. Report zero external flux as a failure
of the intended OPEN-CATCHMENT test rather than silently accepting it.
"""
import csv
import json
import math
import pathlib
import sys

root = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
cases = {}
errors = []
for name, beta in (("beta0",0),("beta2",2)):
    folder = root / ("lorica-v15-open-"+name)
    path = folder / "annual_state.csv"
    marker = folder / "LORICA_TREED_V1_2_ANNUAL_SENSITIVITY_PASS.txt"
    if not path.is_file() or not marker.is_file():
        errors.append(name+": output or completion marker missing")
        continue
    if "topology=open_hillslope" not in marker.read_text(encoding="utf-8-sig"):
        errors.append(name+": wrong topology")
    if "beta="+str(beta) not in marker.read_text(encoding="utf-8-sig"):
        errors.append(name+": wrong treatment beta")
    with path.open(newline="",encoding="utf-8-sig") as f:
        annual = list(csv.DictReader(f))
    if len(annual)!=3: errors.append(name+": expected 3 annual states, got "+str(len(annual)))
    cases[name]=annual
    for i,r in enumerate(annual,1):
        if int(r["year"])!=i: errors.append(name+": missing year "+str(i))
        for field in ("mass_closure","treed_input_DTM_error_m","treed_input_soildepth_error_m","layer_depth_error_m"):
            if not math.isfinite(float(r[field])): errors.append(name+": non-finite "+field)
        if float(r["mass_closure"]) > 1e-6: errors.append(name+": mass imbalance year "+str(i))
        if float(r["treed_input_DTM_error_m"])>5.1e-7 or float(r["treed_input_soildepth_error_m"])>5.1e-7:
            errors.append(name+": current-year state exchange error "+str(i))
        if abs(float(r["unclassified_transient_kg"]))>1e-5:
            errors.append(name+": unexplained sediment transport "+str(i))
    if len(list(folder.glob("year_??/dtm_m.asc"))) != 3:
        errors.append(name+": three annual DEM rasters missing")
if len(cases)==2:
    for i,(a,b) in enumerate(zip(cases["beta0"],cases["beta2"]),1):
        for k in ("annual_precip_mm","mean_temperature_C"):
            if float(a[k])!=float(b[k]):errors.append("Climate mismatch: "+k)
    for k in ("FPC_mean","LAI_mean","rootC_mean_gC_m2","runoff_sum_m","root_cohesion_mean_kPa"):
        if abs(float(cases["beta0"][0][k])-float(cases["beta2"][0][k]))>1e-7:
            errors.append("Initial treatment differed beyond erosion: "+k)
external={}
for name,rows in cases.items():
    external[name]=sum(float(r["explicit_water_export_kg"]) for r in rows)
    if external[name] <= 1e-12: errors.append(name+": no native sediment export detected at open outlet")
    if sum(float(r["water_erosion_sum_m"]) for r in rows) <= 0:
        errors.append(name+": no native water erosion")
    if any(float(r["explicit_water_export_kg"])<0 for r in rows):
        errors.append(name+": negative external export")
summary={
    "status":"PASS" if not errors else "NEEDS_INVESTIGATION",
    "scope":"5x5 10 m synthetic open hillslope, 3 native every_timestep years",
    "comparison":"beta=0 versus beta=2, identical forcing and fixed_original root allocation, soil_water_coupling_strength=1",
    "mass_closure_max":max((float(r["mass_closure"]) for rows in cases.values() for r in rows),default=None),
    "water_erosion_sum_cell_thickness_m":{n:sum(float(r["water_erosion_sum_m"]) for r in rows) for n,rows in cases.items()},
    "external_water_sediment_export_kg":external,
    "landslides":{n:sum(int(r["landslide_initiations"]) for r in rows) for n,rows in cases.items()},
    "errors":errors
}
(out/"open_hillslope_verification.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(summary,indent=2,ensure_ascii=False))
if errors: raise SystemExit("GOUNSA_V15_OPEN_HILLSLOPE_NEEDS_INVESTIGATION")
print("GOUNSA_V15_OPEN_HILLSLOPE_PASS")
