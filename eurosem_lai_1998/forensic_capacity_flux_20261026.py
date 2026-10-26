#!/usr/bin/env python3
"""Original gfortran EUROSEM sediment source and transport terms internal diagnostics.
Observation WRITE only; no changes to splash, flow erosion, transport, input laws.
Reuses previously prepared native 24 case input cards from forensic_native.
"""
from pathlib import Path
import subprocess,shutil,re,json,csv
R=Path(__file__).resolve().parent.parent;E=R/"eu";CASES=R/"eurosem_forensic_cases"
p=E/"eusedl.for"
s=p.read_text(encoding="latin1")
needle="       SUP(I) = DTRC - CT(I)*DTRF"
assert s.count(needle)==1,(needle,s.count(needle))
src_diag="""       IF(I.EQ.1.AND.LCH.EQ.0.AND.MOD(L,20).EQ.0) THEN
          WRITE(*,7616) REAL(L),RDET(I),DTRF*CEX,
     1       DTRC,DTRF,CT(I),CMX(I),SUP(I)
 7616     FORMAT('FORENSIC_SED_SRC ',8(E14.6,1X))
       ENDIF
"""
s=s.replace(needle,needle+"\n"+src_diag,1)
p.write_text(s,encoding="latin1")
cmd=["gfortran","-std=legacy","-fallow-argument-mismatch","-ffixed-line-length-72",
     "-fno-range-check","-O0","-g","-fcheck=all","-fbacktrace","-w",
     "Euroa.for","emainl.for","eplanel.for","eurozl.for","eurseml.for","eusedl.for",
     "-o","EUROSEM_SED_SRC.exe"]
p1=subprocess.run(cmd,cwd=E,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
if p1.returncode:raise RuntimeError(p1.stdout[-5000:])
rows=[]
for m in (0,1):
 for er in (.1,.9):
  case=f"R30_C0p5_H150_E{er}_M{m}".replace(".","p")
  source=CASES/case
  out=CASES/(case+"_sedflux")
  out.mkdir(exist_ok=True)
  for fn in ("test.par","test.pcp","LAI.PAR","EUROM.FIL"):shutil.copy2(source/fn,out/fn)
  shutil.copy2(E/"EUROSEM_SED_SRC.exe",out/"eurosem.exe")
  p2=subprocess.run(["./eurosem.exe"],cwd=out,input="1\nEUROSEM native sediment source flux probe\nn\ny\n",
                    text=True,encoding="latin1",stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=90)
  (out/"stdout.log").write_text(p2.stdout)
  mat=[]
  for line in p2.stdout.splitlines():
    z=re.search(r"FORENSIC_SED_SRC\s+(.+)",line)
    if z:
      try:
        vals=[float(y.replace("D","E")) for y in z.group(1).split()]
        if len(vals)==8:mat.append(vals)
      except ValueError:pass
  stat=(out/"static.out").read_text(errors="replace") if (out/"static.out").exists() else ""
  n=re.findall(r"NET EROSION/DEPOSITION\s+([-+\d\.EeDd]+)\s+kg",stat,re.I)
  row={"case":case,"mcode":m,"erod":er,"return_code":p2.returncode,"samples":len(mat),
       "net_first_kg":float(n[0]) if n else None}
  if mat:
    names=("rain_detach","capacity_equilibrium","transport_source","settling_removal","concentration","transport_capacity","net_sed_supply")
    for j,k in enumerate(names,1):
      row[k+"_mean"]=sum(a[j] for a in mat)/len(mat)
    row["rain_fraction_of_supply_mean"]=sum(a[1]/a[3] for a in mat if abs(a[3])>1e-20)/len(mat)
  rows.append(row)
  (out/"summary.json").write_text(json.dumps(row,indent=2))
  print("FORENSIC_SOURCE_FLUX",json.dumps(row),flush=True)
with (CASES/"native_sediment_source_capacity.csv").open("w",newline="") as f:
  keys=sorted({x for v in rows for x in v})
  w=csv.DictWriter(f,keys);w.writeheader();w.writerows(rows)
print("FORENSIC_SOURCE_FLUX_COMPLETE",len(rows))
