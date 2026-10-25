#!/usr/bin/env python3
"""Use unmodified published engines with their distributed example geometries.
Only rainfall and explicitly tagged exploratory detachment parameters vary."""
from pathlib import Path
import subprocess, shutil, json, csv, traceback, sys
FAST='--fast' in sys.argv
import numpy as np

ROOT=Path(__file__).resolve().parent
OUT=ROOT/"outputs"
OUT.mkdir(exist_ok=True)
DEPTHS=(10,20,30,40,50)
records=[]

def shell(args,cwd,timeout=120,input_text=None):
    p=subprocess.run(args,cwd=cwd,text=True,encoding="latin1",input=input_text,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=timeout)
    return p.returncode,p.stdout[-18000:]

def clone(url,dest):
    if not dest.exists():
        code,log=shell(["git","clone","--depth","1",url,str(dest)],ROOT,120)
        if code: raise RuntimeError(log)
    code,sha=shell(["git","rev-parse","HEAD"],dest)
    return sha.strip()

def arr(path):
    a=np.loadtxt(path)
    return np.asarray(a,dtype=float)

def swehr_run(src,base,rain,detach):
    wd=OUT/f"swehr_{detach}_{rain:02d}"
    wd.mkdir(parents=True,exist_ok=True)
    for f in ("topoin.txt","particlesizein.txt","particlepercentin.txt"):
        shutil.copy(src/f,wd/f)
    original=list(map(float,(src/"input.txt").read_text().split()))
    if FAST:
        coords=list(map(float,(src/"topoin.txt").read_text().split()))
        assert len(coords)==3*51
        short=[v for col in range(3) for v in coords[col*51:col*51+7]]
        (wd/"topoin.txt").write_text(" ".join(map(str,short))+"\n")
        original[1]=7.0  # cropped official example: 3 by 7
    assert len(original)==14
    original[5]=3600.0                # total run [s]
    original[6]=0.0 if detach=="original_zero" else 1.0   # a: original=0
    original[7]=0.0 if detach=="original_zero" else 1.0   # ad: original=0
    original[10]=60.0                 # 60 rainfall samples
    original[11]=60.0                 # interval 60 s
    (wd/"input.txt").write_text(" ".join(map(str,original))+"\n")
    (wd/"rain.txt").write_text(" ".join([f"{rain/3600000:.13g}"]*60)+"\n")
    code,log=shell([str(base)],wd,timeout=24 if FAST else 110)
    (wd/"console.log").write_text(log)
    record=dict(engine="SWEHR native C",scenario=detach,rain_mm_h=rain,run_code=code,
                original_parameters=detach=="original_zero",probe_patch=FAST,workdir=wd.name)
    if code==0:
        topo=arr(wd/"topoin.txt").reshape((int(original[0]),int(original[1]))).T.ravel()  # input i-major; output j-major
        tout=arr(wd/"topoout.txt").ravel()
        mm=arr(wd/"m.txt")
        depth=arr(wd/"depth.txt")
        mxdep=arr(wd/"maxdepth.txt")
        record.update(max_water_depth_m=float(np.nanmax(mxdep)), mean_final_water_depth_m=float(np.nanmean(depth)),
                      max_bed_elevation_change_m=float(np.nanmax(abs(tout-topo))),
                      bed_volume_change_m3=float(np.nansum(tout-topo)*original[2]**2),
                      deposited_sediment_kg_m2_sum=float(np.nansum(mm)))
    return record

def eurosem_run(src,binary,rain):
    wd=OUT/f"eurosem_{rain:02d}"
    wd.mkdir(exist_ok=True)
    par=(src/"test.par").read_text(errors="replace")
    pcp=(src/"test.pcp").read_text(errors="replace")
    assert "30.0         10.0" in pcp
    assert "100.          10.0" in pcp
    pcp=pcp.replace("30.0         10.0",f"60.0         {rain:.1f}")
    pcp=pcp.replace("100.          10.0",f"100.          {rain:.1f}")
    (wd/"test.par").write_text(par)
    (wd/"test.pcp").write_text(pcp)
    (wd/"EUROM.FIL").write_text("\n".join(["dynamic.out","diag.out","","test.par","test.pcp","static.out",""])+"\n")
    try: code,log=shell([str(binary)],wd,timeout=70,input_text="1\nRainfall sensitivity\nn\ny\n")
    except subprocess.TimeoutExpired as e:
        code=124
        log=str(e)
    (wd/"console.log").write_text(log)
    rec=dict(engine="EUROSEM original Fortran",scenario="original_test_parameters",rain_mm_h=rain,run_code=code,workdir=wd.name)
    if (wd/"static.out").exists():
        s=(wd/"static.out").read_text(errors="replace")
        (wd/"static_tail.log").write_text(s[-14000:])
        rec["static_file_bytes"]=len(s)
    if (wd/"dynamic.out").exists():
        s=(wd/"dynamic.out").read_text(errors="replace")
        (wd/"dynamic_tail.log").write_text(s[-14000:])
        rec["dynamic_file_bytes"]=len(s)
    return rec

def main():
    info={}
    swehr=ROOT/"source_swehr"
    euro=ROOT/"source_eurosem"
    info["swehr_commit"]=clone("https://github.com/csdms-contrib/swehr.git",swehr)
    info["eurosem_commit"]=clone("https://github.com/TheSoilman/EUROSEM.git",euro)
    # Diagnostic probe points in the original example are hardwired to y=1,10,...,50.
    # On the 7-row test crop ONLY, map those OUTPUT PROBES to valid grid coordinates.
    # No infiltration, momentum or sediment balance equations are altered.
    swehr_source=swehr/"SWEHR.c"
    if FAST:
        old=swehr_source.read_text()
        new=old
        new=new.replace("outlety2=10;","outlety2=6;")
        for ii,yy in enumerate((1,2,3,4,5,6),start=1):
            import re
            new,ct=re.subn(r"(YPOINT\["+str(ii)+r"\]=)\d+;",r"\g<1>"+str(yy)+";",new)
            assert ct==1, (ii,ct)
        assert new!=old
        swehr_source=ROOT/"SWEHR_compat_probe_points.c"
        swehr_source.write_text(new)
        (OUT/"swehr_compat_changes.txt").write_text("Only output probe positions YPOINT[1..6] and outlety2 changed for 7-row test crop; physical equations preserved.\n")
    code,log=shell(["gcc","-O2","-std=gnu99","-o",str(ROOT/"SWEHR"),str(swehr_source),"-lm"],ROOT)
    (OUT/"swehr_build.log").write_text(log)
    info["swehr_compile_rc"]=code
    if code==0:
        for r in DEPTHS:
            for det in (("exploratory_a1_ad1",) if FAST else ("original_zero","exploratory_a1_ad1")):
                try: records.append(swehr_run(swehr,ROOT/"SWEHR",r,det))
                except Exception as e: records.append(dict(engine="SWEHR native C",scenario=det,rain_mm_h=r,error=repr(e)))
    # Historical Lahey F77 files include DOS Ctrl-Z markers and annotations after fixed column 72.
    # Reformat ONLY legacy source-file encoding/column-72 layout; preserve all calculation statements.
    compat=ROOT/"source_eurosem_fixed72"
    compat.mkdir(exist_ok=True)
    files=[]
    for f in sorted(euro.glob("*.for")):
        lines=f.read_bytes().decode("latin1").splitlines()
        clean="\n".join(ln[:72] for ln in lines if "\x1a" not in ln)+"\n"
        target=compat/f.name
        target.write_text(clean)
        files.append(str(target))
    code,log=shell(["gfortran","-std=legacy","-fallow-argument-mismatch","-fno-range-check",
                   "-o",str(ROOT/"EUROSEM")]+files,ROOT,90)
    (OUT/"eurosem_build.log").write_text(log)
    info["eurosem_compile_rc"]=code
    if code==0:
        for r in DEPTHS:
            try: records.append(eurosem_run(euro,ROOT/"EUROSEM",r))
            except Exception as e: records.append(dict(engine="EUROSEM original Fortran",rain_mm_h=r,error=repr(e)))
    (OUT/"metadata.json").write_text(json.dumps(info,indent=2))
    (OUT/"results.json").write_text(json.dumps(records,indent=2))
    if records:
        keys=sorted({k for d in records for k in d})
        with (OUT/"results.csv").open("w",newline="") as f:
            dw=csv.DictWriter(f,keys);dw.writeheader();dw.writerows(records)
    print("SOURCE_META",json.dumps(info))
    print("SIM_RESULTS",json.dumps(records))
    if info["eurosem_compile_rc"]!=0: print("EUROSEM_BUILD_FAILURE",log[-6000:])

if __name__=="__main__": main()
