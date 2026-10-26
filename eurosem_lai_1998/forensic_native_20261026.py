#!/usr/bin/env python3
"""EUROSEM 1998 Fortran + explicitly labeled 2026-10-25 LAI INTERC fork.
Controlled A/B forensic rerun of the prior 729-run near-zero canopy/EROD sensitivity.
Only inputs, original fixed-form compatibility, and diagnostic WRITE change.
Original erosion/flow transport equations are unchanged. 2D site validation is not claimed.
"""
from pathlib import Path
import subprocess,shutil,itertools,re,csv,json,math
R=Path(__file__).resolve().parent.parent
E=R/"eu"
CASES=R/"eurosem_forensic_cases"
CASES.mkdir(parents=True,exist_ok=True)
def run(cmd,cwd,stdin=None,timeout=150):
    q=subprocess.run(cmd,cwd=cwd,input=stdin,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                     encoding="latin1",text=True,timeout=timeout)
    if q.returncode:raise RuntimeError(f"COMMAND {cmd} EXIT={q.returncode}\n{q.stdout[-6500:]}")
    return q.stdout
if not E.exists():run(["git","clone","--depth","1","https://github.com/TheSoilman/EUROSEM.git",str(E)],R,timeout=100)
sha=run(["git","rev-parse","HEAD"],E).strip()
for f in E.glob("*.for"):
    f.write_bytes(f.read_bytes().replace(bytes([26]),b""))
# Existing provenance-tested legacy compiler uninitialized-variable repair:
p=E/"eplanel.for";s=p.read_text(encoding="latin1")
for old,new in (
    ("      INTRT = 0\n      LCH = 0\n      contrib = 1.","      INTRT = 0\n      LCH = 0\n      NKIR = 0\n      contrib = 1."),
    ("        MM=NB(JJ)-1","        MM=NB(JJ)-1\n        MB=NI+1")
):
    assert s.count(old)==1, (old,s.count(old))
    s=s.replace(old,new)
p.write_text(s,encoding="latin1")
p=E/"test.par";lines=p.read_text(encoding="latin1").splitlines()
pos=[i for i,x in enumerate(lines) if x.split()==["2","0","0","0","0","0","0"]]
assert len(pos)==1,pos
lines[pos[0]]=" 2      1         0        0        0        0       0"
p.write_text("\n".join(lines)+"\n",encoding="latin1")
# Reuse exact LAI extension whose 729-run interpretation is now being audited.
run(["python3",str(R/"eurosem_lai_1998"/"patch_interception.py")],E)
# Observation-only diagnostic. No equation edits.
p=E/"eplanel.for";s=p.read_text(encoding="latin1")
needle="        CALL KINET(J)"
assert s.count(needle)==1,s.count(needle)
s=s.replace(needle,needle+"""
        WRITE(*,5765) PLHGT(J), DRIPKE(1), RAINKE(1)
 5765 FORMAT('FORENSIC_KE ',3(E15.7,1X))
""",1)
p.write_text(s,encoding="latin1")
build=run(["gfortran","-std=legacy","-fallow-argument-mismatch","-ffixed-line-length-72",
           "-fno-range-check","-O0","-g","-fcheck=all","-fbacktrace","-w",
           "Euroa.for","emainl.for","eplanel.for","eurozl.for","eurseml.for","eusedl.for",
           "-o","EUROSEM_FOR.exe"],E)
print("FORENSIC_COMPILED",sha,flush=True)
records=[]
for rain,cover,height,erod,mcode in itertools.product((30,),(0.1,0.5,0.9),(3,150),(0.1,0.9),(0,1)):
    label=f"R{rain}_C{cover}_H{height}_E{erod}_M{mcode}".replace(".","p")
    d=CASES/label;d.mkdir(exist_ok=True)
    par=(E/"test.par").read_text(encoding="latin1")
    veg="0.15        2      55.0      0.05       3.0      5.0    1"
    assert par.count(veg)==2,(veg,par.count(veg))
    par=par.replace(veg,f"{cover:.3f}        2      55.0      0.05       {height:.1f}      5.0    1")
    sed="25.      .9       2.     1.00    2.6    0.0    0.00     1"
    assert par.count(sed)==2,(sed,par.count(sed))
    par=par.replace(sed,f"25.      {erod:.4f}       2.     1.00    2.6    0.0    0.00     {mcode}")
    # Set original model's separate time-step field only, if needed future runs.
    (d/"test.par").write_text(par,encoding="latin1")
    pcp=(E/"test.pcp").read_text(encoding="latin1")
    # Fix original example's 2 listed rain pairs though 3 present.
    pcp=pcp.replace("         1                 2","         1                 3")
    pcp=pcp.replace("      1                  2","      1                  3")
    assert "    30.0         10.0" in pcp
    pcp=pcp.replace("    30.0         10.0",f"    60.0         {rain:.1f}")
    pcp=pcp.replace("   100.          10.0",f"   100.          {rain:.1f}")
    (d/"test.pcp").write_text(pcp,encoding="latin1")
    (d/"LAI.PAR").write_text("1 2.5 0.2 0.046\n2 2.5 0.2 0.046\n")
    (d/"EUROM.FIL").write_text("\n".join(["dynamic.out","diag.out","","test.par","test.pcp","static.out",""])+"\n")
    shutil.copy2(E/"EUROSEM_FOR.exe",d/"eurosem.exe")
    try:
        out=run(["./eurosem.exe"],d,stdin="1\nEUROSEM forensic experimental conditions\nn\ny\n",timeout=90)
        status="OK"
    except Exception as e:
        out=str(e);status="FAIL"
    (d/"stdout.log").write_text(out)
    stat=(d/"static.out").read_text(errors="replace") if (d/"static.out").exists() else ""
    diag=(d/"diag.out").read_text(errors="replace") if (d/"diag.out").exists() else ""
    row={"case":label,"rain_mm_h":rain,"cover":cover,"LAI":2.5,"input_height_cm":height,
         "EROD_g_J":erod,"MCODE":mcode,"source_sha":sha,"run_status":status}
    def nums(pat,src):
        return [float(x.replace("D","E")) for x in re.findall(pat,src,re.I)]
    row["runoff_mm"]=next(iter(nums(r"TOTAL BASIN RUNOFF\s*=\s*([-+\d\.EeDd]+)",stat)),None)
    row["water_error_pct"]=next(iter(nums(r"GLOBAL VOL\. ERROR\s*=\s*([-+\d\.EeDd]+)",stat)),None)
    row["net_erosion_kg"]=nums(r"NET EROSION/DEPOSITION\s*([-+\d\.EeDd]+)\s+kg",stat)
    row["gross_detachment_kg"]=nums(r"GROSS INTERRILL EROSION\s*([-+\d\.EeDd]+)\s+kg",stat)
    m=re.search(r"FORENSIC_KE\s+([^\r\n]+)",out)
    if m:
        v=[float(s.replace("D","E")) for s in m.group(1).split()]
        if len(v)==3:row.update(internal_height_m=v[0],dripKE=v[1],directKE=v[2])
    (d/"summary.json").write_text(json.dumps(row,indent=2,ensure_ascii=False))
    records.append(row)
    print("NATIVE_FORENSIC",json.dumps(row,ensure_ascii=False),flush=True)
keys=sorted({k for r in records for k in r})
with (CASES/"summary.csv").open("w",newline="") as f:
    wr=csv.DictWriter(f,keys);wr.writeheader()
    for row in records:
        wr.writerow({k:json.dumps(v) if isinstance(v,list) else v for k,v in row.items()})
(CASES/"README.md").write_text("Original TheSoilman/EUROSEM Fortran with fixed-form compiler compatibility and prior optional LAI.PAR patch. Height in cm. MCODE0=Govers, MCODE1=Everaert. Output gross/net sediment not independent sediment ledger. Cases compared only one input at a time.\n")
print("FORENSIC_SUMMARY",len(records),"runs OK",sum(x["run_status"]=="OK" for x in records),flush=True)
