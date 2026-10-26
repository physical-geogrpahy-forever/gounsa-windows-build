#!/usr/bin/env python3
"""Controlled native EUROSEM 1998 process-source audit, single-plane boundary.
Change only user inputs, and in PATCHED mode remove the duplicated DRIPD/RAIN
factor in DRIPS. NEVER treat the corrected fork as the original executable.
No sediment-ledger PASS claim: native record has no independent budget.
"""
import argparse,sys,subprocess,json,csv,itertools,math
from pathlib import Path
ROOT=Path(__file__).resolve().parent
RESULT=ROOT/"eurosem_reaudit_20261026"
RESULT.mkdir(exist_ok=True)
p=argparse.ArgumentParser()
p.add_argument("--subset",choices=["main","mcode0"],default="main")
args=p.parse_args()
if args.subset=="main":
    cases=list(itertools.product((3,120),(.1,.9),(.1,.9),(False,True)))
else:
    cases=[(120,.9,erod,fix) for erod in (.1,.9) for fix in (False,True)]
rows=[]
for i,(height,cover,erod,fix) in enumerate(cases):
    mcode=1 if args.subset=="main" else 0
    case=f"{args.subset}_H{height}_C{int(cover*100)}_E{int(erod*10)}_{'corrected' if fix else 'original'}"
    cmd=[sys.executable,str(ROOT/"verify_eurosem_reaudit_20261026.py"),
         "--rain","30","--tag",case,"--plant-height",str(height),
         "--cover",str(cover),"--storage","1.5","--shape","2",
         "--angle","55","--erod",str(erod),"--mcode",str(mcode),
         "--trace-splash"]
    if fix: cmd.append("--drip-fix")
    try:
        completed=subprocess.run(cmd,text=True,encoding="latin1",stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT,cwd=ROOT,timeout=95)
        folder=ROOT/f"eurosem_QA_{case}_r30_rep1"
        if not (folder/"qa_result.json").exists(): print("NATIVE_STDOUT",case,completed.stdout[-2800:]); raise RuntimeError("missing qa")
        r=json.loads((folder/"qa_result.json").read_text())
        r.update(status="PASS" if completed.returncode==0 else "FAIL",
                 case=case,height_cm=height,cover=cover,erod=erod,drip_patch=fix,
                 mcode=mcode,source_trace=completed.stdout[-1000:])
        r["net_erosion_t_ha"]=sum(r.get("net_erosion_kg",[]))*10/14500
        r["gross_detachment_t_ha"]=sum(r.get("gross_detachment_kg",[]))*10/14500
        r["splash_diag_count"]=len(r.get("splash_diagnostic",[]))
        q=r.get("energy_probe",{})
        if height==120 and cover==.9 and erod in (.1,.9): print("SPLASH_INTERNAL",case,json.dumps(r.get("splash_diagnostic",[])[:4]),flush=True)
        if height==120 and cover==.9 and erod in (.1,.9): print("TRANSPORT_INTERNAL",case,json.dumps(r.get("sed_source_diagnostic",[])[:4]),flush=True)
        print("NATIVE_AUDIT",case,r["status"],"runoff_mm",r.get("runoff_mm"),
              "net_t_ha",r["net_erosion_t_ha"],"height_m",q.get("effective_drop_height_m"),
              "dripKE",q.get("drip_kinetic_energy"),"rainKE",q.get("free_rain_kinetic_energy"),
              "splash_traces",r["splash_diag_count"],flush=True)
    except Exception as e:
        r={"status":"ERROR","case":case,"exception":repr(e)}
        print("NATIVE_AUDIT_ERROR",case,repr(e),flush=True)
    rows.append(r)
(RESULT/f"{args.subset}.json").write_text(json.dumps(rows,ensure_ascii=False,indent=2))
cols=["case","status","height_cm","cover","erod","drip_patch","mcode","runoff_mm",
      "net_erosion_t_ha","gross_detachment_t_ha","water_error_pct","sediment_pass",
      "splash_diag_count"]
with (RESULT/f"{args.subset}.csv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=cols)
    w.writeheader()
    for r in rows:w.writerow({k:r.get(k) for k in cols})
for height in ((3,120) if args.subset=="main" else (120,)):
    for cover in ((.1,.9) if args.subset=="main" else (.9,)):
        rr=[r for r in rows if r.get("height_cm")==height and r.get("cover")==cover]
        for fix in (False,True):
            compare=sorted((r for r in rr if r.get("drip_patch")==fix),key=lambda z:z["erod"])
            if len(compare)==2 and all(r["status"]=="PASS" for r in compare):
                print("EROD_PAIR",height,cover,fix,compare[0]["net_erosion_t_ha"],
                      compare[1]["net_erosion_t_ha"],
                      "difference",compare[1]["net_erosion_t_ha"]-compare[0]["net_erosion_t_ha"])
        for erod in (.1,.9):
            compare=sorted((r for r in rr if r.get("erod")==erod),key=lambda z:z["drip_patch"])
            if len(compare)==2 and all(r["status"]=="PASS" for r in compare):
                print("DRIP_FIX_PAIR",height,cover,erod,compare[0]["net_erosion_t_ha"],
                      compare[1]["net_erosion_t_ha"],
                      "difference",compare[1]["net_erosion_t_ha"]-compare[0]["net_erosion_t_ha"])
print("AUDIT_RESULTS",args.subset,"n",len(rows),"passed",sum(r["status"]=="PASS" for r in rows))
if sum(r["status"]=="PASS" for r in rows)==0:raise SystemExit(3)
