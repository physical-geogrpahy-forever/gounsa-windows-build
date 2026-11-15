#!/usr/bin/env python3
"""Independent annual state response comparison of real TREED+LORICA runs.
Do NOT presume soil feedback or adaptive root mode actually changes TREED.
"""
import csv, json, math, pathlib, sys

root=pathlib.Path(sys.argv[1])
out=pathlib.Path(sys.argv[2])
out.mkdir(parents=True,exist_ok=True)
scenarios=[
    ("fixed_off","fixed_original",0.0),
    ("fixed_on","fixed_original",1.0),
    ("adaptive_off","adaptive_experimental",0.0),
    ("adaptive_on","adaptive_experimental",1.0),
]
data={}
errors=[]
for name,mode,strength in scenarios:
    folder=root/("lorica-v14-soil-"+name)
    annual=folder/"annual_state.csv"
    cfg=folder/"TREED_coupling.cfg"
    if not annual.exists() or not cfg.exists():
        errors.append(f"{name}: missing native outputs/config")
        continue
    with annual.open(encoding="utf-8-sig",newline="") as f:
        rows=list(csv.DictReader(f))
    conf=cfg.read_text(encoding="utf-8-sig")
    if f"root_allocation_mode={mode}" not in conf or f"soil_water_coupling_strength={strength:.1f}" not in conf:
        errors.append(f"{name}: effective config mismatch")
    if len(rows)!=3: errors.append(f"{name}: expected 3 actual years, got {len(rows)}")
    for y,r in enumerate(rows,1):
        if int(r["year"])!=y: errors.append(f"{name}: missing year {y}")
        if float(r["mass_closure"])>1e-6: errors.append(f"{name}: mass closure year {y}")
        if float(r["treed_input_soildepth_error_m"])>5.1e-7:
            errors.append(f"{name}: soil depth exchange year {y}")
    data[name]=rows
fields=("FPC_mean","LAI_mean","rootC_mean_gC_m2","root_cohesion_mean_kPa",
        "runoff_sum_m","water_erosion_sum_m","mean_soil_depth_m")
comparisons=[]
for off,on in (("fixed_off","fixed_on"),("adaptive_off","adaptive_on"),
               ("fixed_off","adaptive_off"),("fixed_on","adaptive_on")):
    if off not in data or on not in data:continue
    for i,(a,b) in enumerate(zip(data[off],data[on]),1):
        d={"case_a":off,"case_b":on,"year":i}
        for key in fields:
            av,bv=float(a[key]),float(b[key])
            d[key+"_a"]=av
            d[key+"_b"]=bv
            d[key+"_diff"]=bv-av
        comparisons.append(d)
if comparisons:
    with (out/"three_year_soil_feedback_comparison.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(comparisons[0]))
        w.writeheader(); w.writerows(comparisons)
responses={}
for a,b in (("fixed_off","fixed_on"),("adaptive_off","adaptive_on")):
    subset=[r for r in comparisons if r["case_a"]==a and r["case_b"]==b]
    responses[a+"_vs_"+b]={key:max((abs(r[key+"_diff"]) for r in subset),default=None) for key in fields}
for name,rows in data.items():
    other=next(iter(data.values()))
    for y,(r,base) in enumerate(zip(rows,other),1):
        for k in ("annual_precip_mm","mean_temperature_C"):
            if r[k]!=base[k]: errors.append(f"Climate forcing differs: {name} year{y} field{k}")
summary={"status":"PASS" if not errors else "FAIL","year_count":3,
         "test":"four native Julia TREED plus LORICA 3-year runs under identical synthetic forcing",
         "scenarios":[{"id":n,"root_allocation_mode":m,"soil_water_coupling_strength":s} for n,m,s in scenarios],
         "max_abs_differences":responses,
         "note":"Zero response means no detected feedback, not a successful proof of ecological coupling",
         "errors":errors}
(out/"three_year_soil_feedback_audit.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(summary,ensure_ascii=False,indent=2))
if errors:raise SystemExit("GOUNSA_V14_SOIL_FEEDBACK_AUDIT_FAIL")
print("GOUNSA_V14_SOIL_FEEDBACK_AUDIT_PASS")
