#!/usr/bin/env python3
"""Compare original native model results with strict separate water and sediment validity.
Read downloaded GitHub Actions artifacts, never infer numbers from hypothetical species names."""
import json,sys,math,csv
from pathlib import Path
ROOT=Path(__file__).resolve().parent
PATH=ROOT/"ensemble_inputs"
OUT=ROOT/"species_sensitivity"/"combined"
OUT.mkdir(parents=True,exist_ok=True)
engines={}
for name in ["eurosem","swehr"]:
    p=PATH/name/"results.json"
    engines[name]=json.loads(p.read_text())
    print(name,"total",len(engines[name]),"native_run_pass",sum(x["program_status"]=="run_pass" for x in engines[name]))
report=["# Original EUROSEM/SWEHR 10–50 mm/h sensitivity benchmark",
"","**This is a hypothetical structure and soil-parameter ensemble using original solver equations, not a calibrated Gounsa oak resprout or Miscanthus simulation.**",
"EUROSEM canopy partition is native; its sediment masses lack an independently verified sediment closure.",
"SWEHR has independent water/soil/loose layer/boundary mass closure; its published code lacks per-stem spatial stemflow and canopy drip impact mechanics.",
"","## Five-storm vegetation mechanism comparison",""]
for eng,data in engines.items():
    report += [f"### {eng}","| P (mm/h) | Scenario | I (mm) | Free TF (mm) | Drip (mm) | Stemflow (mm) | Runoff (mm) | Detachment (t/ha) | Native reported net erosion or exported loss (t/ha) | Water QA | Sediment QA |",
               "|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|"]
    for x in data:
        if x["scenario"] not in ["control","oak_canopy","miscanthus_canopy","oak_assumed_soil","miscanthus_assumed_soil"]:
            continue
        c=x.get("canopy",{})
        if eng=="eurosem":
            runoff=x.get("runoff_mm")
            det=sum(x.get("gross_detachment_kg",[]))/14500*10 if x.get("gross_detachment_kg") else None
            sed=sum(x.get("net_erosion_kg",[]))/14500*10 if x.get("net_erosion_kg") else None
            w=x.get("water_pass",False)
            sediment="UNVERIFIED"
        else:
            runoff=x.get("net_boundary_water_out_m3",0)/9.5625*1000 if "net_boundary_water_out_m3" in x else None
            det=x.get("original_soil_detachment_kg",0)/9.5625*10 if "original_soil_detachment_kg" in x else None
            sed=x.get("net_boundary_sediment_out_kg",0)/9.5625*10 if "net_boundary_sediment_out_kg" in x else None
            w=x.get("water_pass",False)
            sediment="PASS" if x.get("independent_layer_pass",False) and x.get("sediment_pass",False) else "FAIL"
        fmt=lambda z:"—" if z is None else f"{z:.7g}"
        report.append("| "+" | ".join([str(x["rain_mm_h"]),x["scenario"],fmt(c.get("interception_mm")),
                  fmt(c.get("free_throughfall_mm")),fmt(c.get("leaf_drip_mm")),fmt(c.get("stemflow_mm")),
                  fmt(runoff),fmt(det),fmt(sed),"PASS" if w else "FAIL",sediment])+" |")
    report.append("")
report+=["## One-at-a-time (OAT) 30 mm/h scans",""]
for eng,data in engines.items():
    report+=["### "+eng,"| Parameter | Min setting | Max setting | Min runoff mm | Max runoff mm | Min reported sediment t/ha | Max reported sediment t/ha |",
             "|---|---:|---:|---:|---:|---:|---:|"]
    groups={}
    for x in data:
        n=x["scenario"]
        if not n.startswith("oat_"):continue
        var=n[4:]
        params=x["parameters"]
        matched=[q for q in params if var.startswith(q+"_")]
        if not matched:continue
        key=max(matched,key=len)
        if eng=="swehr":
            sediment=x.get("net_boundary_sediment_out_kg")
            if sediment is not None:sediment=sediment/9.5625*10
            water=x.get("net_boundary_water_out_m3")
            if water is not None:water=water/9.5625*1000
        else:
            sediment=sum(x["net_erosion_kg"])/14500*10 if x.get("net_erosion_kg") else None
            water=x.get("runoff_mm")
        groups.setdefault(key,[]).append((params[key],water,sediment,x.get("water_pass",False),x.get("independent_layer_pass",False)))
    for k,arr in groups.items():
        v=[a for a in arr if a[1] is not None and a[2] is not None]
        if not v:continue
        v.sort(key=lambda t:t[0])
        fmt=lambda q: f"{q:.8g}"
        report.append("| "+" | ".join([k,fmt(v[0][0]),fmt(v[-1][0]),fmt(min(x[1] for x in v)),fmt(max(x[1] for x in v)),
                                          fmt(min(x[2] for x in v)),fmt(max(x[2] for x in v))])+" |")
    report.append("")
report+=["## Scientific status","",
"- No fitted species-specific parameters or field sediment mass measurements were provided.",
"- Annual interception fractions in the literature cannot be equated to hourly event interception.",
"- Original EUROSEM 'net erosion/deposition' summary must not be silently re-labelled as validated exported sediment.",
"- SWEHR rainfall-only comparator takes post-interception TOTAL uniform ground input; stemflow spatial placement and drip energy are not coupled. This must be resolved before species-scale sediment differences are claimed.",
"- A sensitivity response conditioned on assumed Ksat, roughness, and erodibility is not proof of a species effect."]
(OUT/"summary.md").write_text("\n".join(report))
print("\n".join(report))
