#!/usr/bin/env python3
"""Original vs diagnostic one-line drip-weight correction, no other equation edits.
DO NOT describe the corrected executable as native original EUROSEM.
Original gfortran base must be built first by forensic_native_20261026.py.
"""
from pathlib import Path
import shutil, subprocess, re, json, csv
R=Path(__file__).resolve().parent.parent
E=R/"eu"
CASES=R/"eurosem_forensic_cases"
src=E/"eurseml.for"
s=src.read_text(encoding="latin1")
old="If(Rain(IZ) .gt. 0.) DMMSEC = RMMSEC*DRIPD(IZ)/RAIN(IZ)"
new="If(Rain(IZ) .gt. 0.) DMMSEC = RMMSEC"
assert s.count(old)==1,("original formula not identified",s.count(old))
# Instrument-only original function comparison after RDETIN and DRDTIN source calculations.
probe_src="""          IF (K.EQ.2.AND.MOD(L,50).EQ.0.AND.
     1      T(L).GT.900.AND.T(L).LT.2700.) THEN
            WRITE(*,5766) ERODGJ(J),DRIPKE(IZ),DMMSEC,
     1           RDETIN(K),DRDTIN(K),XINDET(K)
 5766       FORMAT('FORENSIC_SPLASH ',6(E14.6,1X))
          ENDIF
"""
needle="         XINDET(K) = (RDETIN(k)+DRDTIN(k))*1.e-6/2.65"
assert needle in s
s=s.replace(needle,needle+"\n"+probe_src)
src.write_text(s,encoding="latin1")
original_code=src.read_text()
# First calculate with *unfixed* original drip factor, with identical write-only probe.
cmd=["gfortran","-std=legacy","-fallow-argument-mismatch","-ffixed-line-length-72",
     "-fno-range-check","-O0","-g","-fcheck=all","-fbacktrace","-w",
     "Euroa.for","emainl.for","eplanel.for","eurozl.for","eurseml.for","eusedl.for"]
def build(binary):
    q=subprocess.run(cmd+["-o",binary],cwd=E,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    if q.returncode:raise RuntimeError(q.stdout[-7000:])
build("orig-probe.exe")
src.write_text(original_code.replace(old,new),encoding="latin1")
build("single-fraction-probe.exe")
records=[]
for cover in (.1,.5,.9):
  for erod in (.1,.9):
    for mcode in (0,1):
      tag=f"R30_C{cover}_H150_E{erod}_M{mcode}".replace(".","p")
      src_case=CASES/tag
      for version,binname in (("original", "orig-probe.exe"),("single_fraction","single-fraction-probe.exe")):
        wd=CASES/(tag+"_"+version);wd.mkdir(exist_ok=True)
        for fn in ("test.par","test.pcp","LAI.PAR","EUROM.FIL"):
            shutil.copy2(src_case/fn,wd/fn)
        shutil.copy2(E/binname,wd/"eurosem.exe")
        p=subprocess.run(["./eurosem.exe"],cwd=wd,input="1\nEUROSEM forensic drip weighting\nn\ny\n",
                         stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,encoding="latin1",timeout=90)
        out=p.stdout;(wd/"stdout.log").write_text(out)
        stat=(wd/"static.out").read_text(errors="replace") if (wd/"static.out").exists() else ""
        splash=re.findall(r"FORENSIC_SPLASH\s+([^\r\n]+)",out)
        samples=[]
        for x in splash:
            try:
                v=[float(q.replace("D","E")) for q in x.split()]
                if len(v)==6:samples.append(v)
            except ValueError:pass
        def nums(pat):
            return [float(t.replace("D","E")) for t in re.findall(pat,stat,re.I)]
        row={"case":tag,"version":version,"cover":cover,"EROD":erod,"MCODE":mcode,"rc":p.returncode,
             "gross_kg":nums(r"GROSS INTERRILL EROSION\s+([-+\d\.EeDd]+)\s+kg"),
             "net_kg":nums(r"NET EROSION/DEPOSITION\s+([-+\d\.EeDd]+)\s+kg"),
             "splash_samples":len(samples),"splash_RDETIN_mean":sum(v[3] for v in samples)/len(samples) if samples else None,
             "splash_DRDTIN_mean":sum(v[4] for v in samples)/len(samples) if samples else None,
             "splash_XINDET_mean":sum(v[5] for v in samples)/len(samples) if samples else None}
        (wd/"summary.json").write_text(json.dumps(row,indent=2))
        records.append(row)
        print("DRIP_PAIR",json.dumps(row),flush=True)
fields=sorted({k for r in records for k in r})
with (CASES/"drip_single_fraction_comparison.csv").open("w",newline="") as f:
   w=csv.DictWriter(f,fields);w.writeheader()
   for z in records:w.writerow({k:json.dumps(v) if isinstance(v,list) else v for k,v in z.items()})
print("DRIP_PAIR_COMPLETE",len(records),"success",sum(z["rc"]==0 for z in records))
