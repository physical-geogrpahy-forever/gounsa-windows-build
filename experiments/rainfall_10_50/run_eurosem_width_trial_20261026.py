#!/usr/bin/env python3
"""Experimental unit-consistency test only; not original EUROSEM.
Original RDET is tagged m/s, DTRF*CEX has width, so test multiplying
RDET by TW in both SEDCOM input source places. Original and patched
versions separated, no claim patch is physically proven.
"""
import sys,subprocess,json,itertools
from pathlib import Path
root=Path(__file__).resolve().parent
out=root/"eurosem_reaudit_20261026"
out.mkdir(exist_ok=True)
rows=[]
for mcode,erod,fix in itertools.product((0,1),(.1,.9),(False,True)):
    tag=f"widthunit_M{mcode}_E{int(erod*10)}_"+("W_ON" if fix else "W_OFF")
    cmd=[sys.executable,str(root/"verify_eurosem_reaudit_20261026.py"),
         "--rain","30","--tag",tag,"--plant-height","120","--cover",".9",
         "--erod",str(erod),"--mcode",str(mcode),"--trace-splash","--drip-fix"]
    if fix:cmd.append("--test-splash-width")
    res=subprocess.run(cmd,cwd=root,text=True,encoding="latin1",capture_output=True,timeout=90)
    fp=root/f"eurosem_QA_{tag}_r30_rep1"/"qa_result.json"
    if fp.exists():
        q=json.loads(fp.read_text())
        net=sum(q.get("net_erosion_kg",[]))*10/14500
        row={"tag":tag,"mcode":mcode,"erod":erod,"splashwidthfix":fix,
             "status":"PASS" if res.returncode==0 else "FAIL","net_t_ha":net,
             "runoff_mm":q.get("runoff_mm"),
             "sources":q.get("sed_source_diagnostic",[]),
             "splash":q.get("splash_diagnostic",[])}
    else:row={"tag":tag,"status":"ERROR","log":res.stdout[-2500:]+res.stderr[-500:]}
    rows.append(row)
    print("WIDTH_COMPARE",tag,row.get("status"),"net",row.get("net_t_ha"),
          "rainsource",row.get("sources",[])[:1],flush=True)
(out/"width_experiment.json").write_text(json.dumps(rows,indent=2))
print("WIDTH_SUMMARY",len(rows),"pass",sum(z["status"]=="PASS" for z in rows))
if sum(z["status"]=="PASS" for z in rows)!=len(rows):raise SystemExit(2)
