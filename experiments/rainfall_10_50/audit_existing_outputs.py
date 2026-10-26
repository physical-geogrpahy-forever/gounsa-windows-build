#!/usr/bin/env python3
"""Scientific QA of *existing*, immutable GitHub Actions native model outputs.
No model runs or parameter alterations occur in this script."""
import csv,json,re,os
from pathlib import Path
import numpy as np
ROOT=Path(os.environ.get("AUDIT_ARTIFACT_ROOT","qa_inputs"))
OUT=Path("qa_reports")
OUT.mkdir(exist_ok=True)
rows=[]
report=["# Source-run numerical validity audit","",
"All quantities are extracted from ORIGINAL raw output. No invented erosion curves.","",
"Source SWEHR rainfall runs GitHub Actions 40202181315. Original 3×51 demo, dx=0.25m, rain 1 h, F=0.004, Ks=0, a=ad=0 or 1 (sensitivity trial).",
"Because original C updates h using eroded solid volume, h is a mixture-flow variable and should not simply be interpreted as rainwater volume without a sediment/volume budget. No complete groundwater, slope runoff and sediment boundary-integral budget is available in this output.", ""]
def readf(p):
    return np.loadtxt(p, ndmin=2)
for r in [10,20,30,40,50]:
    for scenario in ["original_zero","exploratory_a1_ad1"]:
        p=ROOT/f"swehr_{scenario}_{r:02d}"
        x={"engine":"SWEHR","rain_intensity_mm_h":r,"scenario":scenario,"valid":False}
        if not p.exists():
            x["issue"]="MISSING ARTIFACT"
            rows.append(x);continue
        try:
            inp=list(map(float,(p/"input.txt").read_text().split()))
            nx,ny,dx=int(inp[0]),int(inp[1]),inp[2]
            topoin=np.fromstring((p/"topoin.txt").read_text(),sep=" ")
            assert topoin.size == nx*ny, (topoin.size,nx,ny)
            # C reads i outer, j inner but writes j outer, i inner.
            before=topoin.reshape(nx,ny).T
            after=readf(p/"topoout.txt")
            assert after.shape == (ny,nx), (after.shape,nx,ny)
            depth=readf(p/"depth.txt")
            mass=readf(p/"m.txt")
            delev=before-after
            x.update(nx=nx,ny=ny,dx_m=dx,domain_area_m2=nx*ny*dx*dx,
                     rainfall_volume_m3=r/1000*(nx*ny*dx*dx),
                     mean_final_flow_depth_mm=float(depth.mean()*1000),
                     maximum_final_flow_depth_mm=float(depth.max()*1000),
                     mean_erosion_positive_mm=float(np.maximum(delev,0).mean()*1000),
                     max_local_erosion_mm=float(np.max(delev)*1000),
                     max_local_deposition_mm=float(np.max(-delev)*1000),
                     gross_bed_lowering_volume_m3=float(np.maximum(delev,0).sum()*dx*dx),
                     gross_bed_rise_volume_m3=float(np.maximum(-delev,0).sum()*dx*dx),
                     final_deposited_mass_sum_kg_m2=float(np.sum(mass)),
                     final_deposited_mass_max_kg_m2=float(np.max(mass)),
                     nonfinite=int((~np.isfinite(before)).sum()+(~np.isfinite(after)).sum()+(~np.isfinite(depth)).sum()+(~np.isfinite(mass)).sum()),
                     true_erosion_depth_lt_1m=bool((delev<1).all()),
                     final_flow_depth_falls_below_rainfall=bool(float(depth.mean())<r/1000))
            x["issue"]="Unvalidated original example; no water/solid flux residual; nonzero flow entrainment F and Ks=0"
        except Exception as e: x["issue"]=repr(e)
        rows.append(x)
report+=["## SWEHR original full-grid outputs and checks",
"| Rain (mm/h) | Case | Final mean flow depth (mm) | Maximum cell erosion (mm) | Gross bed lowering (m³) | Gross bed rise (m³) | Units/quality |",
"|---:|---|---:|---:|---:|---:|---|"]
for x in rows:
    report.append(f"| {x.get('rain_intensity_mm_h')} | {x.get('scenario')} | {x.get('mean_final_flow_depth_mm','-')} | {x.get('max_local_erosion_mm','-')} | {x.get('gross_bed_lowering_volume_m3','-')} | {x.get('gross_bed_rise_volume_m3','-')} | {x.get('issue')} |")

for r in [10,20,30,40,50]:
    p=ROOT/f"eurosem_{r:02d}"
    x=dict(engine="EUROSEM",rain_intensity_mm_h=r,scenario="published_test",valid=False)
    if not p.exists():
        x["issue"]="MISSING ARTIFACT";rows.append(x);continue
    try:
        static=(p/"static_tail.log").read_text(errors="replace") if (p/"static_tail.log").exists() else ""
        dynamic=(p/"dynamic_tail.log").read_text(errors="replace") if (p/"dynamic_tail.log").exists() else ""
        results={}
        patterns={
            "rain_depth_mm":r"TOTAL RAINFALL DEPTH\s*=\s*([-+]?\d+(?:\.\d+)?)",
            "infiltration_mm":r"TOTAL INFILTRATION FROM ALL PLANES\s*=\s*([-+]?\d+(?:\.\d+)?)",
            "basin_runoff_mm":r"TOTAL BASIN RUNOFF\s*=\s*([-+]?\d+(?:\.\d+)?)",
            "balance_error_pct":r"GLOBAL VOL\. ERROR\s*=\s*([-+]?\d+(?:\.\d+)?)",
            "basin_area_m2":r"BASIN AREA\s*=\s*([-+]?\d+(?:\.\d+)?)",
            }
        for key,pattern in patterns.items():
            m=re.search(pattern,static,re.I)
            if m:results[key]=float(m.group(1))
        gross=re.findall(r"GROSS INTERRILL EROSION\s+([-+]?\d+(?:\.\d+)?)\s+kg",static,re.I)
        net=re.findall(r"NET EROSION/DEPOSITION\s+([-+]?\d+(?:\.\d+)?)\s+kg",static,re.I)
        results["gross_interrill_kg_per_element"]=[float(z) for z in gross]
        results["net_erosion_kg_per_element"]=[float(z) for z in net]
        x.update(results)
        x["issue"]="Nonempty" if "rain_depth_mm" in x else "No parseable native summary"
        # Note: output success not assumed, even for populated files
    except Exception as e: x["issue"]=repr(e)
    rows.append(x)
report+=["","## EUROSEM native summary and QA","| Rain (mm/h) | Rain depth native (mm) | Infiltration (mm) | Runoff (mm) | Water balance (%) | Gross interrill element masses (kg) | Output status |",
"|---:|---:|---:|---:|---:|---|---|"]
for x in rows:
    if x["engine"]=="EUROSEM":report.append(f"| {x['rain_intensity_mm_h']} | {x.get('rain_depth_mm','-')} | {x.get('infiltration_mm','-')} | {x.get('basin_runoff_mm','-')} | {x.get('balance_error_pct','-')} | {x.get('gross_interrill_kg_per_element','-')} | {x['issue']} |")
report+=["","## Interpretability constraints",
"- A return code of zero is not equivalent to a valid sediment balance or repeatable model result.",
"- SWEHR source uses a transmissive lower boundary and three solid boundaries; all water and particle fluxes must be integrated to validate budgets.",
"- SWEHR initial soil and sediment arrays are not all explicitly initialized by the published initialcondition routine, which can cause undefined behavior; confirm before engineering estimates.",
"- EUROSEM demonstration contains unconnected plan elements and is not a Gounsa hillslope geometry.",
"- The derived result from published native executable is not an observation. Gounsa erosion not quantified here."]
OUT.joinpath("audit_rows.json").write_text(json.dumps(rows,ensure_ascii=False,indent=2))
with OUT.joinpath("audit_rows.csv").open("w",newline="") as f:
    keys=sorted({k for row in rows for k in row})
    w=csv.DictWriter(f,keys);w.writeheader()
    for row in rows:
        row={**row}
        for k,v in row.items():
            if isinstance(v,list):row[k]=json.dumps(v)
        w.writerow(row)
OUT.joinpath("audit.md").write_text("\n".join(report))
print("\n".join(report))
