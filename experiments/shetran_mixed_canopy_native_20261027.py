#!/usr/bin/env python3
"""Native-only SHETRAN 4.7.2 Cobres 2-species canopy ON/OFF audit.
This script changes *copies* of upstream example INPUT files, not any model equations.
Cobres data, transformed dimensions and canopy parameters are synthetic, not Gounsa.
"""
from pathlib import Path
import argparse
import json
import re
import shutil
import subprocess
import sys
import numpy as np
import h5py

def change_after(lines, marker, replacement):
    hits=[i for i,s in enumerate(lines[:-1]) if s.strip().startswith(marker)]
    assert len(hits)==1,(marker,hits)
    lines[hits[0]+1]=replacement+"\n"

def make_fixed_et_line(plai,storage,clai):
    # Fortran (I7,4F7.0,I7,3F7.0). The last zero is root-depth parameter.
    return (f"{8:7d}{plai:7.3f}{storage:7.3f}{3e-5:7.5f}"
            f"{3.7:7.1f}{20:7d}{clai:7.2f}{0.:7.2f}{0.:7.2f}")

def prepare(src, dest, canopy_on=True, grid_m=2000.0, mmh=30.0):
    shutil.copytree(src,dest)
    f=dest/"input_cob_frd.txt"
    l=f.read_text().splitlines(keepends=True)
    change_after(l,":FR6","".join(f"{x:7d}" for x in (1977,10,1,12,0)))
    change_after(l,":FR7a","".join(f"{x:7d}" for x in (1977,10,1,0,0)))
    j=next(i for i,s in enumerate(l) if "NO. OF MET./RAINFALL STATIONS" in s)
    assert tuple(map(int,l[j+1].split()))==(1,5,1,1,1)
    l[j+1]="".join(f"{n:7d}" for n in [1,5,2,1,1])+"\n"
    j=next(i for i,s in enumerate(l) if "DEFAULT VALUES FOR MET,RAINFALL" in s)
    assert tuple(map(int,l[j+1].split()))==(1,0,1,1)
    l[j+1]="".join(f"{n:7d}" for n in [1,0,0,1])+"\n"
    i=next(i for i,s in enumerate(l) if "COMPUTATIONAL GRID DEFINITION" in s)
    mask=l[i+1:i+30]
    assert len(mask)==29
    grid=[]
    for row in mask:
        a=row.split()
        assert len(a)==2 and len(a[1])==17,(row,a)
        y=int(a[0]); out="".join("0" if ch=="0" else ("1" if (x//2 + y//3)%2==0 else "2")
                                  for x,ch in enumerate(a[1]))
        grid.append(f"{y:7d} {out}\n")
    assert sum(s.count("1") for s in grid)>0 and sum(s.count("2") for s in grid)>0
    j=next(i for i,s in enumerate(l) if s.strip().startswith(":FR52"))
    l[j:j]=[":FR49 - VEGETATION GRID FOR NVC PER CELL\n"]+grid
    if grid_m!=2000.0:
        ratio=grid_m/2000.0
        def replace_spacing(start,end,n):
            nonlocal l
            i=next(i for i,s in enumerate(l) if start in s)
            j=next(i for i,s in enumerate(l) if end in s)
            lines=[("".join(f"{grid_m:7.2f}" for _ in range(min(10,n-k)))+"\n")
                   for k in range(0,n,10)]
            l[i+1:j]=lines
        replace_spacing("GRID SPACING IN X DIRECTION","GRID SPACING IN Y DIRECTION",17)
        replace_spacing("GRID SPACING IN Y DIRECTION","PRINT CONTROL PARAMETERS",29)
        # Ground datum differences scale with the spatial dimensions to maintain original slopes.
        i=next(i for i,s in enumerate(l) if "GROUND SURFACE ELEVATION" in s)
        j=next(i for i,s in enumerate(l) if "RAINFALL STATIONS" in s)
        section=l[i+1:j]
        numbers=[]
        for line in section:
            fields=line.split()
            if len(fields)==1 and fields[0].isdigit():
                numbers.append(("row",int(fields[0])))
            else:
                numbers.append(("vals",[float(x) for x in fields]))
        rows=[]; cur=[]
        for typ,val in numbers:
            if typ=="row":
                if cur: rows.append(cur)
                cur=[]
            else: cur+=val
        if cur: rows.append(cur)
        assert len(rows)==29 and all(len(v)==17 for v in rows),[len(x) for x in rows]
        new=[]
        for rr,vs in enumerate(rows):
            new.append(f"{29-rr:7d}\n")
            vs=[0.0 if v<=0 else 200.+(v-200.)*ratio for v in vs]
            for k in range(0,17,10):
                new.append("".join(f"{v:7.2f}" for v in vs[k:k+10])+"\n")
        l[i+1:j]=new
    f.write_text("".join(l))
    # Duplicate ORIGINAL ET7-through-ET17 vegetation record with a modified 2nd type.
    f=dest/"input_cob_etd.txt"
    l=f.read_text().splitlines(keepends=True)
    i=next(i for i,s in enumerate(l) if s.startswith(":ET7"))
    prefix=l[:i]; block=l[i:]
    # Native Cobres ETD ends with a whitespace-only record. Strip it BEFORE
    # duplicating vegetation blocks: otherwise INET reads the blank record
    # as the second vegetation ET7 heading, and then reads ':ET7' as numeric data.
    while block and not block[-1].strip():
        block.pop()
    block[-1]=block[-1].rstrip(chr(10))+chr(10)
    assert block[1].strip().startswith("F")
    block_oak=block.copy()
    block_grass=block.copy()
    block_oak[2]=make_fixed_et_line(0.85 if canopy_on else 0.0,
                                   1.50 if canopy_on else 1.50, 3.0)+"\n"
    block_grass[0]=":ET7 - SECOND VEGETATION TYPE synthetic Miscanthus\n"
    block_grass[2]=make_fixed_et_line(.65 if canopy_on else 0.0,
                                     .70 if canopy_on else .70,.75)+"\n"
    f.write_text("".join(prefix+block_oak+block_grass))
    # Sediment drip physics for both native vegetation types.
    f=dest/"input_cob_syd.txt"; l=f.read_text().splitlines(keepends=True)
    i=next(i for i,s in enumerate(l) if s.strip().startswith(":SY24"))
    assert len(l[i+1].split())==3
    l[i+1]="    2.0    0.004    0.50\n"
    l.insert(i+2,"    0.8    0.003    0.50\n")
    f.write_text("".join(l))
    # 3h rain, 9h recession; only synthetic test storm.
    f=dest/"input_wet_prd.txt";l=f.read_text().splitlines(keepends=True)
    assert len(l)>13 and "rainfall" in l[0].lower()
    for k in range(1,13):
        l[k]="".join(f"{(mmh if k<=3 else 0.):10.4f}" for _ in range(5))+"\n"
    f.write_text("".join(l))
    # Set measured PET forcing to zero for first 12 h; reduces but does not prove 
    # all transpiration-related effects excluded from native canopy ablation.
    f=dest/"input_wet_epd.txt"
    if f.exists():
        ll=f.read_text().splitlines(keepends=True)
        zeroed=0
        for k in range(1,min(len(ll),13)):
            q=ll[k].split()
            if q and all(re.fullmatch(r"[-+]?\d+(?:\.\d+)?",x) for x in q):
                ll[k]="".join(f"{0.:10.4f}" for _ in q)+"\n";zeroed+=1
        f.write_text("".join(ll))
    meta={"case":"ON" if canopy_on else "OFF","grid_m":grid_m,
          "requested_extent_m2":17*29*grid_m**2, "event_mm_h":mmh,
          "species":["synthetic oak resprout","synthetic Miscanthus patch"],
          "NVC_map":grid,"off_note":"PLAI=0 also affects ET, so ON-OFF is not a pure isolated canopy toggle"}
    (dest/"synthetic_metadata.json").write_text(json.dumps(meta,indent=2))
    return meta

def extract(path):
    with h5py.File(path) as f:
        ds={}
        for key,g in f["VARIABLES"].items():
            if not isinstance(g,h5py.Group) or "value" not in g:continue
            name=key.strip().split(" ",1)[-1]
            if name in ["s_v_er","s_t_dp","net_rain"]:
                arr=np.array(g["value"],dtype=float)
                if arr.ndim==3:
                    ds[name]=arr
                elif name not in ds: ds[name]=arr
    assert "s_v_er" in ds and "s_t_dp" in ds, list(ds)
    E,D=ds["s_v_er"],ds["s_t_dp"]
    assert E.shape==D.shape and E.ndim==3,(E.shape,D.shape)
    valid=np.all(np.isfinite(E)&(np.abs(E)<1e10),axis=-1)
    valid&=np.all(np.isfinite(D)&(np.abs(D)<1e10),axis=-1)
    assert valid.sum()>=1
    return dict(erosion=E,loose=D,mask=valid,n_valid=int(valid.sum()),
                peak_erosion_mm_day=float(np.max(E[valid])),
                final_loose_mm_mean=float(np.mean(D[valid][:,-1])))

def run_one(exe,src,root,label,canopy_on,grid_m):
    dest=root/label
    meta=prepare(src,dest,canopy_on=canopy_on,grid_m=grid_m)
    run=subprocess.run([str(exe),"-f","rundata_cob.txt"],cwd=dest,
                       capture_output=True,text=True,timeout=300)
    (dest/"native_stdout.log").write_text(run.stdout+"\nSTDERR\n"+run.stderr)
    if run.returncode!=0:\n        pri=dest/"output_cob_pri.txt"\n        tail=pri.read_text(errors="replace")[-9000:] if pri.is_file() else "NO_PRI"\n        raise RuntimeError(f"{label}: return={run.returncode}; PRI_TAIL={tail}; STDOUT={run.stdout[-2500:]} STDERR={run.stderr[-1000:]}")
    h=dest/"output_cob_shegraph.h5"
    assert h.is_file(),h
    d=extract(h)
    summary={k:v for k,v in d.items() if k not in ("erosion","loose","mask")}
    summary.update(meta)
    summary.pop("NVC_map",None)
    (dest/"summary.json").write_text(json.dumps(summary,indent=2))
    return d,summary

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--original-model",type=Path,required=True)
    a.add_argument("--exe",type=Path,required=True)
    a.add_argument("--workdir",type=Path,required=True)
    a.add_argument("--grid-m",type=float,default=2000.)
    a.add_argument("--allow-native-failure",action="store_true")
    args=a.parse_args()
    exe=args.exe.resolve()
    src=args.original_model.resolve()
    args.workdir.mkdir(parents=True,exist_ok=True)
    try:
        on,sm_on=run_one(exe,src,args.workdir,"on",True,args.grid_m)
        off,sm_off=run_one(exe,src,args.workdir,"off",False,args.grid_m)
        assert np.array_equal(on["mask"],off["mask"])
        good=on["mask"]
        # Spatial sensitivity is a necessary but not sufficient signal of canopy effect.
        src_diff=float(np.max(np.abs(on["erosion"][good]-off["erosion"][good])))
        dls_diff=float(np.max(np.abs(on["loose"][good]-off["loose"][good])))
        report={"native_executable_original_unmodified":True,"grid_m":args.grid_m,
                "runs":[sm_on,sm_off], "max_snapshot_erosion_difference_mm_day":src_diff,
                "max_loose_depth_difference_mm":dls_diff,
                "canopy_effect_is_not_isolated_from_ET":True,
                "HDF_snapshots_are_not_gross_deposition_or_exact_time_integrals":True,
                "overall_sediment_budget_verified":False,
                "high_resolution_microplot_validated":False}
        (args.workdir/"comparison.json").write_text(json.dumps(report,indent=2))
        print("NATIVE_MIXED_ON_OFF_RESULTS\n"+json.dumps(report,indent=2),flush=True)
    except Exception as e:
        (args.workdir/"failure.json").write_text(json.dumps({"error":repr(e),"grid_m":args.grid_m}))
        if not args.allow_native_failure:raise
        print("NATIVE_CASE_NOT_VALIDATED",repr(e),flush=True)

if __name__=="__main__":
    main()
