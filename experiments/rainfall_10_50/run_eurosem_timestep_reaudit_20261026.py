#!/usr/bin/env python3
"""EUROSEM 1998 original vs corrected-drip, 60/30/15 s timestep convergence.
Does not equate model's erosion text output to independent outlet sediment mass.
"""
import itertools,json,subprocess,sys,math,csv
from pathlib import Path
root=Path(__file__).resolve().parent
folder=root/"eurosem_reaudit_20261026";folder.mkdir(exist_ok=True)
rows=[]
for mcode,dt,dripfix in itertools.product((0,1),(1.0,.5,.25),(False,True)):
    tag=f"dtcheck_M{mcode}_dt{str(dt).replace('.','p')}_{'dripfixed' if dripfix else 'native'}"
    cmd=[sys.executable,str(root/"verify_eurosem_reaudit_20261026.py"),
         "--rain","30","--tag",tag,"--plant-height","120","--cover",".9",
         "--storage","1.5","--erod",".9","--mcode",str(mcode),"--dt-minute",str(dt)]
    if dripfix:cmd.append("--drip-fix")
    x=subprocess.run(cmd,text=True,encoding="latin1",stdout=subprocess.PIPE,stderr=subprocess.STDOUT,cwd=root,timeout=120)
    fn=root/f"eurosem_QA_{tag}_r30_rep1"/"qa_result.json"
    if fn.exists():
        z=json.loads(fn.read_text())
        row={"name":tag,"dt_s":dt*60,"mcode":mcode,"patched_drip":dripfix,
             "water_pass":z.get("water_pass"),"water_error_pct":z.get("water_error_pct"),
             "runoff_mm":z.get("runoff_mm"),
             "net_erosion_t_ha":sum(z.get("net_erosion_kg",[]))*10/14500,
             "status":"PASS" if x.returncode==0 else "FAIL"}
    else:
        row={"name":tag,"status":"ERROR","log":x.stdout[-1900:]}
    rows.append(row)
    print("DT_NATIVE",json.dumps(row,ensure_ascii=False),flush=True)
for mcode in (0,1):
    for patch in (False,True):
        xx=sorted([x for x in rows if x.get("mcode")==mcode and x.get("patched_drip")==patch],key=lambda z:z["dt_s"])
        if len(xx)<3 or any(z["status"]!="PASS" for z in xx):continue
        a,b,c=xx
        diff_ab=abs(a["net_erosion_t_ha"]-b["net_erosion_t_ha"])/max(abs(a["net_erosion_t_ha"]),abs(b["net_erosion_t_ha"]),1e-12)
        diff_bc=abs(b["net_erosion_t_ha"]-c["net_erosion_t_ha"])/max(abs(b["net_erosion_t_ha"]),abs(c["net_erosion_t_ha"]),1e-12)
        print("DT_CONVERGENCE",mcode,"dripfixed",patch,
              "dt15-vs30",diff_ab,"dt30-vs60",diff_bc,
              "series",[(q["dt_s"],q["net_erosion_t_ha"]) for q in xx],flush=True)
with (folder/"dt_results.json").open("w") as f:json.dump(rows,f,indent=2)
keys=["name","dt_s","mcode","patched_drip","water_pass","water_error_pct","runoff_mm","net_erosion_t_ha","status"]
with (folder/"dt_results.csv").open("w",newline="") as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
 for x in rows:w.writerow({k:x.get(k) for k in keys})
print("DT_TOTAL",sum(z["status"]=="PASS" for z in rows),len(rows),flush=True)
if not all(z["status"]=="PASS" for z in rows):raise SystemExit(2)
