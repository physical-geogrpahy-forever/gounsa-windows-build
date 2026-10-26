#!/usr/bin/env python3
"""Run independently modified *input copies* against the pinned original SHETRAN executable.

No source-code or soil erosion equation changes. This experiment isolates
rainfall-driven DR from flow-driven DF for one 20 mm/h 3h Cobres rainfall.
Results are native HDF5 snapshots; GNU time integral is right-endpoint APPROX.
"""
from __future__ import annotations
from pathlib import Path
import argparse
import csv
import json
import shutil
import subprocess
import numpy as np
import h5py

SCENARIOS = [
    ("baseline", "unchanged", None),
    ("no_rain_detachment", "GKR", 0.0),
    ("no_flow_detachment", "GKF", 0.0),
    ("no_source_detachment", "BOTH", 0.0),
    ("no_canopy_drip_impact", "FDRIP", 0.0),
    ("ground_cover_90pct", "FCG", 0.9),
]
PIN="cf9cd540add78ad3accbaf62b4199d2032887f6b"
def replace_after(lines, tag, editor):
    inds=[i for i,line in enumerate(lines[:-1]) if line.strip().startswith(tag)]
    if len(inds)!=1:
        raise ValueError(f"Expected exactly one {tag}; found {len(inds)}")
    i=inds[0]+1
    lines[i]=editor(lines[i])
def setup_model(source:Path, dst:Path,mode:str,value:float|None):
    shutil.copytree(source,dst)
    frd=dst/"input_cob_frd.txt"
    lines=frd.read_text().splitlines(keepends=True)
    replace_after(lines,":FR6",lambda _: "".join(f"{v:7d}" for v in [1977,10,3,0,0])+"\n")
    replace_after(lines,":FR7a",lambda _: "".join(f"{v:7d}" for v in [1977,10,1,0,0])+"\n")
    frd.write_text("".join(lines))
    rain=dst/"input_wet_prd.txt"
    q=rain.read_text().splitlines(keepends=True)
    assert len(q)>=49
    for i in range(1,49):
        assert len(q[i].split())==5
        q[i]="".join(f"{(20.0 if i<=3 else 0.0):10.4f}" for _ in range(5))+"\n"
    rain.write_text("".join(q))
    syd=dst/"input_cob_syd.txt"
    a=syd.read_text().splitlines(keepends=True)
    if mode in ("GKR","GKF","BOTH"):
        inds=[i for i,line in enumerate(a[:-1]) if line.strip().startswith(":SY22")]
        assert len(inds)==1
        for j in range(inds[0]+1,inds[0]+4):
            f=a[j].split()
            assert len(f)==5,f
            assert float(f[0])==2.5 and float(f[1].replace("D","E"))==1e-5
            if mode in ("GKR","BOTH"): f[0]="0.0"
            if mode in ("GKF","BOTH"): f[1]="0.0"
            a[j]=" ".join(f)+"\n"
    if mode=="FDRIP":
        def set_drip(line):
            f=line.split()
            assert len(f)==3 and float(f[2])==0.5
            f[2]="0.0"
            return " ".join(f)+"\n"
        replace_after(a,":SY24 -",set_drip)
    if mode=="FCG":
        replace_after(a,":SY41c",lambda _:"        0.9\n")
    syd.write_text("".join(a))

def get_native_metrics(root:Path):
    with h5py.File(root/"output_cob_shegraph.h5") as h:
        groups=h["VARIABLES"]
        def get(key):
            matches=[obj for nm,obj in groups.items() if nm.strip().endswith(" "+key) and "value" in obj]
            assert len(matches)>=1,key
            grp=max(matches,key=lambda ob:np.prod(ob["value"].shape))
            return np.asarray(grp["value"],dtype=np.float64), np.asarray(grp["time"],dtype=np.float64)
        g,t=get("s_v_er")
        d,td=get("s_t_dp")
        assert g.shape==d.shape and g.shape[-1]==t.size and np.allclose(t,td)
        good=np.isfinite(g).all(axis=-1) & np.isfinite(d).all(axis=-1) & (d>=0).all(axis=-1)
        good&=(np.abs(g)<1e10).all(axis=-1) & (np.abs(d)<1e10).all(axis=-1)
        gg=g[good];dd=d[good]
        assert gg.shape[0]==176,gg.shape
        dt=np.diff(t)*3600
        gross=np.sum(gg[:,1:]*dt[None,:],axis=1)/(1000*86400)
        delta=dd[:,-1]-30.0
        z_change=delta/1000.0-gross
        return {
          "n_cell":int(gg.shape[0]),
          "last_time_hours":float(t[-1]),
          "maximum_instant_gnu_mm_day":float(np.max(gg)),
          "max_sampled_gross_detachment_mm":float(np.max(gross)*1000),
          "mean_sampled_gross_detachment_mm":float(np.mean(gross)*1000),
          "max_dls_delta_mm":float(np.max(delta)),
          "min_approx_delta_z_mm":float(np.min(z_change)*1000),
          "max_approx_delta_z_mm":float(np.max(z_change)*1000),
          "cells_positive_detachment":int(np.count_nonzero(gross>0)),
          "fine_print":"Source GNU integrated using right-end HDF5 sampling; NOT native internal GNU ledger."
        }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--original-model",required=True)
    p.add_argument("--exe",required=True)
    p.add_argument("--workdir",required=True)
    args=p.parse_args()
    source=Path(args.original_model).resolve();exe=Path(args.exe).resolve();base=Path(args.workdir).resolve()
    assert source.is_dir() and exe.is_file()
    base.mkdir(parents=True,exist_ok=True)
    rows=[]
    for name,mode,value in SCENARIOS:
        folder=base/name
        setup_model(source,folder,mode,value)
        with (folder/"native_stdout.log").open("w") as log:
            done=subprocess.run([str(exe),"-f","rundata_cob.txt"],cwd=folder,stdout=log,stderr=subprocess.STDOUT,timeout=480)
        assert done.returncode==0,(name,done.returncode,(folder/"native_stdout.log").read_text()[-1800:])
        result={"scenario":name,"changed_input":mode,"value":value,**get_native_metrics(folder)}
        rows.append(result)
        print("NATIVE_MECHANISM_CASE",json.dumps(result,allow_nan=False),flush=True)
    for row in rows:
        (base/(row["scenario"]+"_diagnostics.json")).write_text(json.dumps(row,indent=2))
    with (base/"mechanism_summary.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys())
        w.writeheader();w.writerows(rows)
    print("NATIVE_MECHANISM_TESTS_ALL_PASSED",len(rows),flush=True)
if __name__=="__main__": main()
