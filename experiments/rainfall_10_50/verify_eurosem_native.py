#!/usr/bin/env python3
"""EUROSEM v3.2L native F77: single-plane isolation, proper three-point cumulative rainfall,
safe legacy fixed-form compatibility, bounds diagnostics, repeatability and water budget.
Never equate gross detachment with catchment sediment yield.
"""
from pathlib import Path
import subprocess,re,json,argparse,math
ROOT=Path(__file__).resolve().parent
def cmd(argv,cwd,stdin=None,timeout=120):
    p=subprocess.run(argv,cwd=cwd,input=stdin,text=True,encoding="latin1",capture_output=True,timeout=timeout)
    return p.returncode,p.stdout+p.stderr
def main():
    a=argparse.ArgumentParser()
    a.add_argument("--rain",type=int,required=True)
    a.add_argument("--repeat",type=int,default=1)
    args=a.parse_args()
    src=ROOT/"source_eurosem"
    if not src.exists():
        p=subprocess.run(["git","clone","--depth","1","https://github.com/TheSoilman/EUROSEM.git",str(src)],capture_output=True,text=True)
        if p.returncode:raise RuntimeError(p.stderr[-4000:])
    version=cmd(["git","rev-parse","HEAD"],src)[1].strip()
    workspace=ROOT/f"eurosem_QA_r{args.rain:02d}_rep{args.repeat}"
    workspace.mkdir(parents=True,exist_ok=True)
    fixed=ROOT/"eurosem_fixed72"
    fixed.mkdir(exist_ok=True)
    fs=[]
    for f in sorted(src.glob("*.for")):
        # no edits to fixed-form code statements: remove DOS ^Z and trailing col>72
        s=f.read_bytes().decode("latin1")
        lines=[z[:72] for z in s.splitlines() if "\x1a" not in z]
        dst=fixed/f.name
        if f.name=="eplanel.for":
            z="\n".join(lines)+"\n"
            start=z.index(" 1022 Format(")
            stop=z.index("  470 FORMAT",start)
            new_format=""" 1022 Format(3x,'GROSS INTERRILL EROSION',4X,E14.6,' kg',
     - E14.6,' t/ha'//,
     - 3X,'NET EROSION/DEPOSITION',5X,E14.6,' kg',
     - E14.6,' t/ha',/,
     - 3x,'(a minus denotes deposition)',/)
"""
            z=z[:start]+new_format+z[stop:]
            dst.write_text(z)
        else:
            dst.write_text("\n".join(lines)+"\n")
        fs.append(str(dst))
    exe=ROOT/"EUROSEM_QA"
    compile_flags=["-O0","-g","-std=legacy","-fcheck=bounds","-finit-local-zero",
                   "-fallow-argument-mismatch","-fno-range-check"]
    rc,log=cmd(["gfortran",*compile_flags,"-o",str(exe),*fs],ROOT,timeout=120)
    (workspace/"compile.log").write_text(log)
    if rc:raise RuntimeError(log[-7000:])
    par=(src/"test.par").read_text(errors="replace")
    pcp=(src/"test.pcp").read_text(errors="replace")
    # Use one model element; original two are unconnected with warning. No invented routing.
    par=par.replace("    2       0     110.      88.","    1       0     100.      88.")
    assert "    1       0     100.      88." in par
    par=par.replace("       2            2\n","")  # physically remove unused computation order line; READTM counts lines
    # Trim original second plane entry entirely; the first remains unchanged.
    second=par.find("*      potatoes",par.find("*      potatoes")+1)
    assert second>=0
    par=par[:second]
    # Rain hyetograph: 3 pairs (0,0), (60,rain), (100,rain).
    # Keep trailing 28min recession (TFIN 88 min). 3 explicit pair count fixes malformed example.
    pcp="\n".join(ln for ln in pcp.splitlines() if not re.fullmatch(r"\s*2\s+1\s+1\.0\s*",ln))+"\n"  # one active plane: remove second element gauge assignment
    pcp=pcp.replace("         1                 2","         1                 3")
    pcp=pcp.replace("      1                  2","      1                  3")
    pcp=pcp.replace("    30.0         10.0",f"    60.0         {args.rain:.1f}")
    pcp=pcp.replace("   100.          10.0",f"   100.          {args.rain:.1f}")
    assert f"    60.0         {args.rain:.1f}" in pcp
    (workspace/"test.par").write_text(par)
    (workspace/"test.pcp").write_text(pcp)
    (workspace/"EUROM.FIL").write_text("\n".join(["dynamic.out","diag.out","","test.par","test.pcp","static.out",""])+"\n")
    try:rc,log=cmd([str(exe)],workspace,"1\nValidating EUROSEM\nn\ny\n",timeout=95)
    except subprocess.TimeoutExpired:rc,log=124,"TIMEOUT"
    (workspace/"console.log").write_text(log[-150000:])
    stat=(workspace/"static.out").read_text(errors="replace") if (workspace/"static.out").exists() else ""
    dyn=(workspace/"dynamic.out").read_text(errors="replace") if (workspace/"dynamic.out").exists() else ""
    (workspace/"static.log").write_text(stat)
    (workspace/"dynamic.log").write_text(dyn)
    result={"rain_mm_h":args.rain,"repeat":args.repeat,"source_sha":version,"return_code":rc,
            "stat_bytes":len(stat),"dynamic_bytes":len(dyn),
            "bounds_error":bool(re.search("out of bounds|runtime error|segmentation|array bound",log,re.I))}
    for key,pattern in {
         "rain_depth_mm":r"TOTAL RAINFALL DEPTH\s*=\s*([-+]?\d+(?:\.\d+)?)",
         "water_error_pct":r"GLOBAL VOL\. ERROR\s*=\s*([-+]?\d+(?:\.\d+)?)",
         "runoff_mm":r"TOTAL BASIN RUNOFF\s*=\s*([-+]?\d+(?:\.\d+)?)",
         "infil_mm":r"TOTAL INFILTRATION FROM ALL PLANES\s*=\s*([-+]?\d+(?:\.\d+)?)",
         "basin_area_m2":r"BASIN AREA\s*=\s*([-+]?\d+(?:\.\d+)?)",
    }.items():
        m=re.search(pattern,stat+"\n"+dyn)
        if m:result[key]=float(m.group(1))
    sci=r"([-+]?(?:\\d+(?:\\.\\d*)?|\\.\\d+)(?:[EeDd][-+]?\\d+)?)"
    result["gross_detachment_kg"]=[float(x.replace("D","E")) for x in re.findall(r"GROSS INTERRILL EROSION\\s+"+sci+r"\\s+kg",stat)]
    result["net_erosion_kg"]=[float(x.replace("D","E")) for x in re.findall(r"NET EROSION/DEPOSITION\\s+"+sci+r"\\s+kg",stat)]
    result["water_pass"]=bool(rc==0 and not result["bounds_error"] and
       len(result["net_erosion_kg"])==1 and
       abs(result.get("water_error_pct",100)) <= 1 and
       abs(result.get("rain_depth_mm",-999)-args.rain) < 0.3)
    # EUROSEM output lacks independently integrated sediment export/storage/boundary ledger.
    # Do NOT equate its native erosion summary with strict complete sediment mass closure.
    result["sediment_pass"]=False
    result["QA_STATUS"]="HYDROLOGY_ONLY_PASS" if result["water_pass"] else "REJECT"
    (workspace/"qa_result.json").write_text(json.dumps(result,indent=2))
    print("FINAL_QA "+json.dumps(result))
    if rc!=0:print("CONSOLE_LAST "+log[-2800:])
    if not result["water_pass"]:raise SystemExit(2)
if __name__=="__main__":main()
