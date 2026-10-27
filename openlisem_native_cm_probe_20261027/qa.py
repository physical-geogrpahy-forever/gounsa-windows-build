#!/usr/bin/env python3
"""Read native LISEM originals, quantify 5/10cm sediment/time-step sensitivity.
Generated source/inputs are synthetic and not Maggioli(2022) exact provenance.
"""
from pathlib import Path
import csv
import json
import math
import os
import sys

ROOT = Path(__file__).resolve().parent
grid = int(sys.argv[1])
manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf8"))["cases"]
cases = [x for x in manifest if x["resolution_cm"] == grid]
assert len(cases) == 4
records = []
for case in cases:
    p = Path(case["outdir"]) / "totals.csv"
    row = {k:case[k] for k in ("name","resolution_cm","user_dt_s","dx_m","cells")}
    row["has_native_totals"] = p.is_file()
    if p.is_file():
        data={}
        for line in p.read_text(encoding="utf-8-sig",errors="replace").splitlines():
            try:
                c=next(csv.reader([line]))
                if len(c)>1:
                    data[c[0].strip()] = float(c[1])
            except (ValueError, StopIteration):
                pass
        for target,key in (
            ("rain_mm","Total Precipitation (mm):"),
            ("outflow_mm","Water across boundary (mm):"),
            ("sed_export_kg_ha","Average soil loss (kg/ha):")
        ):
            row[target]=data.get(key,float("nan"))
        row["finite"]=all(math.isfinite(row[k]) for k in ("rain_mm","outflow_mm","sed_export_kg_ha"))
    records.append(row)
for row in records:
    print("NATIVE_CM_RESULT",json.dumps(row,allow_nan=True),flush=True)
comparison=[]
for cover in ("Oak_sprouts_sparse","Miscanthus_dense"):
    group=[r for r in records if cover in r["name"] and r["has_native_totals"] and r.get("finite")]
    if len(group)==2:
        a,b=sorted(group,key=lambda r:r["user_dt_s"])
        se=max(abs(a["sed_export_kg_ha"]),abs(b["sed_export_kg_ha"]),1e-12)
        we=max(abs(a["outflow_mm"]),abs(b["outflow_mm"]),1e-12)
        q={"cover":cover,"resolution_cm":grid,"user_dt_s":[a["user_dt_s"],b["user_dt_s"]],
           "sediment_dt_relative_diff":abs(a["sed_export_kg_ha"]-b["sed_export_kg_ha"])/se,
           "water_dt_relative_diff":abs(a["outflow_mm"]-b["outflow_mm"])/we,
           "status":"CANDIDATE_ONLY_DO_NOT_ADOPT"}
    else:
        q={"cover":cover,"resolution_cm":grid,"status":"INCOMPLETE_NATIVE_SIMULATIONS"}
    comparison.append(q)
    print("NATIVE_CM_DT_TEST",json.dumps(q,allow_nan=True),flush=True)
out={"grid_cm":grid,"records":records,"comparisons":comparison,
     "engine":"openLISEM official Windows 7.5.2, NOT Maggioli(2022) exact source",
     "numerical_validity_not_claimed":True}
(ROOT / f"qa_{grid}cm.json").write_text(json.dumps(out,indent=2,allow_nan=True),encoding="utf8")
if any(q["status"]=="INCOMPLETE_NATIVE_SIMULATIONS" for q in comparison):
    print("NATIVE_CM_GATE_NOT_PASSED: incomplete native results",flush=True)
    raise SystemExit(2)
if any(q["sediment_dt_relative_diff"]>0.10 or q["water_dt_relative_diff"]>0.05 for q in comparison):
    print("NATIVE_CM_GATE_FAILED: original native timestep sensitivity",flush=True)
    raise SystemExit(3)
print("NATIVE_CM_PRELIM_TIMESTEP_GATE_PASSED_NOT_YET_VALIDATED",flush=True)
