#!/usr/bin/env python3
"""Native SHETRAN v4.7.5 input-isolated sediment/canopy sensitivity.
Use ONLY developer-provided Cobres model inputs and official Windows executable.
This is a software process-response test; it does not represent Gounsa site.
"""
from __future__ import annotations
import argparse,csv,json,math,shutil,subprocess,sys,time
from pathlib import Path

PARSER=argparse.ArgumentParser()
PARSER.add_argument("--exe",type=Path,required=True)
PARSER.add_argument("--source",type=Path,required=True)
PARSER.add_argument("--out",type=Path,default=Path("shetran_trial"))
ARGS=PARSER.parse_args()
exe=ARGS.exe.resolve()
source=ARGS.source.resolve()
root=ARGS.out.resolve()
root.mkdir(parents=True,exist_ok=True)
assert exe.is_file() and (source/"input_cob_syd.txt").is_file()

# Validated source field definitions:
# ET8 row 2: NF, PLAI, CSTCAP, CK, CB, NRD, CLAI, VHT.
# SY22: GKR, GKF, RHOSO, FPCLAY, BKB.
# SY24: XDRIP, DRDRIP, FDRIP.
variants=[
 ("control",None,{}),
 ("rain10",10,{}),("rain30",30,{}),("rain50",50,{}),
 ("rain30_clai0p2",30,{"clai":0.2}),
 ("rain30_clai1",30,{"clai":1.0}),
 ("rain30_clai4",30,{"clai":4.0}),
 ("rain30_plai0p1",30,{"plai":0.1}),
 ("rain30_plai0p9",30,{"plai":0.9}),
 ("rain30_cstcap0p2",30,{"cstcap":0.2}),
 ("rain30_cstcap3",30,{"cstcap":3.0}),
 ("rain30_gkr0",30,{"gkr":0.0}),
 ("rain30_gkr5",30,{"gkr":5.0}),
 ("rain30_gkf0",30,{"gkf":0.0}),
 ("rain30_gkf2e5",30,{"gkf":2e-5}),
 ("rain30_fcg0",30,{"fcg":0.0}),
 ("rain30_fcg0p8",30,{"fcg":0.8}),
 ("rain30_rock0p6",30,{"rock":0.6}),
 ("rain30_fdrip0",30,{"fdrip":0.0}),
 ("rain30_fdrip1",30,{"fdrip":1.0}),
]
def edit_section_line(p:Path,section:str,transform):
    s=p.read_text(errors="replace").splitlines()
    idx=[i for i,x in enumerate(s) if x.strip().startswith(section)]
    assert len(idx)==1,(p.name,section,idx)
    line_i=idx[0]+1
    words=s[line_i].split()
    assert words,(p.name,section)
    s[line_i]=" ".join(transform(words))
    p.write_text("\n".join(s)+"\n")

def edit_et8(case:Path,cfg:dict):
    p=case/"input_cob_etd.txt"
    lines=p.read_text().splitlines()
    # Two value rows follow :ET7 title; locate unique NF=8 / baseline PLAI=.85.
    matches=[i for i,l in enumerate(lines) if len(l.split())==8 and
             l.split()[0]=="8" and abs(float(l.split()[1])-.85)<1e-8]
    assert len(matches)==1,matches
    i=matches[0]
    t=lines[i].split()
    if "plai" in cfg:t[1]=f"{cfg['plai']:.3f}"
    if "clai" in cfg:t[6]=f"{cfg['clai']:.3f}"
    if "cstcap" in cfg:t[2]=f"{cfg['cstcap']:.3f}"
    # Use 7-column ET8 fields: I7, 4F7.0, I7, 2F7.0 in its second record.
    fields=[f"{int(t[0]):7d}",f"{float(t[1]):7.3f}",f"{float(t[2]):7.3f}",
            f"{float(t[3]):7.5f}",f"{float(t[4]):7.3f}",f"{int(t[5]):7d}",
            f"{float(t[6]):7.3f}",f"{float(t[7]):7.3f}"]
    # Critical: Fortran original uses CK=.00003, needs >= 5 decimals.
    lines[i]="".join(fields)
    p.write_text("\n".join(lines)+"\n")

def prepare_case(label,rate,cfg):
    p=root/label
    shutil.copytree(source,p,dirs_exist_ok=False)
    if rate is not None:
        rain=p/"input_wet_prd.txt"
        lines=rain.read_text().splitlines()
        idx=240 # Oct 11 1977, verified dry in 5 source gauges for multiple hours
        assert len(lines)>idx+15
        for j in range(idx-5,idx+10):
            vals=[float(x) for x in lines[1+j].split()]
            assert len(vals)==5 and max(abs(x) for x in vals)<1e-10,(j,vals)
        lines[1+idx]=" ".join(f"{float(rate):10.4f}" for _ in range(5))
        rain.write_text("\n".join(lines)+"\n")
    if any(k in cfg for k in ("plai","clai","cstcap")):edit_et8(p,cfg)
    if any(k in cfg for k in ("gkr","gkf")):
        fp=p/"input_cob_syd.txt"
        lines=fp.read_text().splitlines()
        isec=next(i for i,x in enumerate(lines) if x.lstrip().startswith(":SY22"))
        for j in range(1,4):
            t=lines[isec+j].split()
            assert len(t)==5
            if "gkr" in cfg:t[0]=f"{cfg['gkr']:.6g}"
            if "gkf" in cfg:t[1]=f"{cfg['gkf']:.9g}"
            lines[isec+j]="   ".join(t)
        fp.write_text("\n".join(lines)+"\n")
    if "fcg" in cfg:edit_section_line(p/"input_cob_syd.txt",":SY41c",lambda _: [f"{cfg['fcg']:.4f}"])
    if "rock" in cfg:edit_section_line(p/"input_cob_syd.txt",":SY42c",lambda _: [f"{cfg['rock']:.4f}"])
    if "fdrip" in cfg:edit_section_line(p/"input_cob_syd.txt",":SY24",
       lambda t: [t[0],t[1],f"{cfg['fdrip']:.4f}"])
    (p/"scenario.json").write_text(json.dumps(dict(label=label,rain_event_mm_per_hour=rate,modifiers=cfg),indent=2))
    return p

def numeric_table(path:Path):
    if not path.exists() or path.stat().st_size<100:
        raise AssertionError("missing/empty: "+str(path))
    rows=list(csv.reader(path.open(errors="replace",newline='')))
    # Official v4.7.5 CSV: descriptive line, field-name line, hourly samples.
    assert len(rows)>4 and len(rows[0])==1 and len(rows[1])>=3,(path,rows[:3])
    heading=[x.strip() for x in rows[1]]
    assert heading[1]=="Time(hours)" and "kg/s" in heading[2],(path,heading)
    points=[]
    for row in rows[2:]:
        if len(row)<3:continue
        try:
            hour=float(row[1])
            discharge=float(row[2])
        except ValueError:
            raise AssertionError((path,row))
        if not math.isfinite(hour) or not math.isfinite(discharge):
            raise AssertionError((path,"NaN/Inf",row))
        if discharge < -1e-10:raise AssertionError((path,"negative sediment discharge",row))
        points.append((hour,discharge))
    assert len(points)>100,(path,len(points))
    integration=0.0
    for (start,q),(end,_) in zip(points,points[1:]):
        dt=end-start
        assert 0 < dt <=24,(path,start,end)
        integration+=max(0.0,q)*dt*3600.0  # hourly mean kg/s -> kg
    return {"file":path.name,"header":heading,
            "numeric_rows":len(points),
            "nonzero_positive":sum(q>0 for _,q in points),
            "max_field_value":max(q for _,q in points),
            "cumulative_sediment_export_kg":integration,
            "last_time_hour":points[-1][0]}

def report_result(p:Path,label:str,rate,cfg,elapsed):
    balance=p/"output_cob_mb.csv"
    assert balance.exists()
    rows=list(csv.reader(balance.open(errors="replace",newline='')))
    assert len(rows)>3 and "Cumulative_Precipitation" in rows[1],rows[:2]
    hdr=[x.strip() for x in rows[1]]
    last=[x.strip() for x in rows[-1]]
    assert len(last)==len(hdr),(label,len(hdr),len(last))
    values={k:float(v) for k,v in zip(hdr,last)}
    assert all(math.isfinite(x) for x in values.values())
    sed=numeric_table(p/"output_cob_sediment_all.csv")
    fine=numeric_table(p/"output_cob_sediment_fine.csv")
    result=dict(case=label,rain_added_mm=rate,elapsed_seconds=round(elapsed,2),
      precip_mm=values.get("Cumulative_Precipitation"),
      canopy_evap_mm=values.get("Cumulative_Canopy_Evaporation"),
      canopy_storage_mm=values.get("Canopy_Storage"),
      discharge_mm=values.get("Cumulative_Discharge"),
      subsurface_storage_mm=values.get("Subsurface_Storage"),
      land_storage_mm=values.get("Land_Surface_Storage"),
      sed_all_max_field=sed["max_field_value"],sed_all_positive_fields=sed["nonzero_positive"],
      sed_all_numeric_rows=sed["numeric_rows"],
      sed_all_export_kg=sed["cumulative_sediment_export_kg"],
      sed_fine_max_field=fine["max_field_value"],sed_fine_positive_fields=fine["nonzero_positive"],
      sed_fine_export_kg=fine["cumulative_sediment_export_kg"])
    (p/"audit.json").write_text(json.dumps({"summary":result,"all_sediment":sed,"fine_sediment":fine},indent=2))
    print("SHETRAN_NATIVE_RESULT",json.dumps(result),flush=True)
    return result

summaries=[]
for label,rate,cfg in variants:
    case=prepare_case(label,rate,cfg)
    print("SCENARIO_START",label,rate,cfg,flush=True)
    t0=time.monotonic()
    with (case/"shetran.stdout.log").open("w",encoding="utf8",errors="replace") as log:
        proc=subprocess.run([str(exe),"-f","rundata_cob.txt"],cwd=case,stdout=log,
                            stderr=subprocess.STDOUT,timeout=120,check=False)
    elapsed=time.monotonic()-t0
    if proc.returncode:
        print("FAILED",label,proc.returncode,(case/"shetran.stdout.log").read_text(errors="replace")[-2000:],flush=True)
        raise RuntimeError(f"Native {label} exited {proc.returncode}")
    summaries.append(report_result(case,label,rate,cfg,elapsed))
with (root/"all_cases.csv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(summaries[0]))
    w.writeheader();w.writerows(summaries)
print("SUCCESS_TOTAL",len(summaries),flush=True)
