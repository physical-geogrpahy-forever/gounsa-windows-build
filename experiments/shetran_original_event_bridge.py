#!/usr/bin/env python3
"""EXTERNAL, non-SHETRAN postprocessor for inter-event hillslope topography.

Works with original SHETRAN FR37-FR39 (Fortran 10G7.0 fields) plus grids
exported from the ORIGINAL HDF5 visualisation outputs:
  s_v_er: instantaneous GNU [mm/day] at explicit sampling times.
  s_t_dp: actual DLS [mm] at start and end of event.
No source code is changed. Strict safeguards:
  * this does NOT constitute an exact GNU time-integral if samples are coarse;
  * SHETRAN hotstart lacks sediment FBETA/FDEL, so restart_ready is FALSE;
  * FR39 seven-character precision must not silently erase erosion increments;
  * rock, soil layer, hydrological/state updates are outside this postprocessor.
Do not run the next event as a 'continuous' simulation without fixing blockers.
"""
from __future__ import annotations
import argparse
import csv
import json
import math
from pathlib import Path

FIELDS = 7
def read_grid_csv(path, nx, ny, value_col):
    with Path(path).open(newline="",encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    grid = {}
    for row in rows:
        k = int(row["iy"]), int(row["ix"])
        if not (1 <= k[0] <= ny and 1 <= k[1] <= nx) or k in grid:
            raise ValueError(f"{path}: invalid/duplicate grid coordinate {k}")
        v = float(row[value_col])
        if not math.isfinite(v):
            raise ValueError(f"{path}: nonfinite {k}")
        grid[k] = v
    expected = {(iy,ix) for iy in range(1,ny+1) for ix in range(1,nx+1)}
    if set(grid) != expected:
        raise ValueError(f"{path}: missing {len(expected-set(grid))} grid cells")
    return grid

def read_frd(text):
    lines = text.splitlines(keepends=True)
    candidates = [i for i,l in enumerate(lines) if l.strip().upper()=="GROUND SURFACE ELEVATION"]
    if len(candidates) != 1:
        raise ValueError("Expected exactly one FR37 GROUND SURFACE ELEVATION title")
    start = candidates[0]+1
    candidates = [i for i,l in enumerate(lines[:start]) if "GRID SQUARES IN X,Y DIRECTIONS" in l.upper()]
    if len(candidates)!=1:
        raise ValueError("Could not establish FRD grid dimensions")
    dim = lines[candidates[0]+1].split()
    nx,ny = int(dim[0]),int(dim[1])
    if not(1<=nx<=100000 and 1<=ny<=100000):
        raise ValueError("Invalid grid shape")
    pos=start
    z={}
    for iy in range(ny,0,-1):
        label=lines[pos].strip()
        if label!=str(iy):
            raise ValueError(f"Expected FR39 row {iy}, found {label!r}")
        pos+=1
        n=0
        while n<nx:
            current=lines[pos].rstrip("\r\n")
            if len(current)%FIELDS:
                raise ValueError(f"FR39 width mismatch on row {iy}: {current!r}")
            chunks=[current[i:i+FIELDS] for i in range(0,len(current),FIELDS)]
            if len(chunks)>10 or n+len(chunks)>nx:
                raise ValueError("More FR39 values than declared")
            for chunk in chunks:
                v=float(chunk.strip().replace("D","E"))
                if not math.isfinite(v): raise ValueError("Nonfinite ZGRUND")
                z[(iy,n+1)]=v;n+=1
            pos+=1
    return lines,start,pos,nx,ny,z

def encode_g7(v, max_abs_rounding):
    candidates=[]
    for decimals in range(6,-1,-1):
        s=f"{v:7.{decimals}f}"
        if len(s)==7:
            err=abs(v-float(s))
            candidates.append((err,-decimals,s))
    if not candidates:
        raise ValueError(f"FR39 G7.0 cannot represent {v} as a fixed-decimal value")
    err,_,s=min(candidates)
    if err>max_abs_rounding:
        raise ValueError(f"FR39 precision would erase {err:.4g}m at elevation {v}; "
            "choose consistent local vertical datum or an explicit residual ledger")
    return s,err

def integrate_rates(path,nx,ny,duration_s):
    r={}
    with Path(path).open(newline="",encoding="utf-8-sig") as handle:
        for row in csv.DictReader(handle):
            k=(int(row["iy"]),int(row["ix"]))
            t=float(row["time_s"])
            val=float(row["rate_mm_day"])
            if not (math.isfinite(t) and math.isfinite(val) and val>=0):
                raise ValueError("Invalid source GNU or time")
            if not (1<=k[0]<=ny and 1<=k[1]<=nx):raise ValueError(f"Invalid {k}")
            r.setdefault(k,[]).append((t,val))
    er={}
    for iy in range(1,ny+1):
        for ix in range(1,nx+1):
            k=(iy,ix)
            a=sorted(r.get(k,[]))
            if len(a)<2 or abs(a[0][0])>1e-7 or abs(a[-1][0]-duration_s)>1e-7:
                raise ValueError(f"{k}: must have endpoints t=0 and t={duration_s}")
            if any(b[0]<=c[0] for c,b in zip(a,a[1:])):
                raise ValueError(f"{k}: duplicate/nonincreasing timestamps")
            # GNU represents native original SOIL detachment, not net elevation change.
            # Trapezoidal integration approximates the real native time-step sum.
            er[k]=sum((b[0]-c[0])*(b[1]+c[1])*0.5 for c,b in zip(a,a[1:]))/(86400*1000)
    return er

def write_grid(path,grid,key):
    with Path(path).open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f);w.writerow(["iy","ix",key])
        for k,v in sorted(grid.items(),key=lambda kv:(-kv[0][0],kv[0][1])):
            w.writerow([*k,f"{v:.12g}"])

def run(args):
    src=Path(args.frd).read_text()
    lines,start,end,nx,ny,z0=read_frd(src)
    soil=read_grid_csv(args.soil_depth_csv,nx,ny,"depth_m")
    d0=read_grid_csv(args.loose_initial_csv,nx,ny,"s_t_dp_mm")
    d1=read_grid_csv(args.loose_final_csv,nx,ny,"s_t_dp_mm")
    gross=integrate_rates(args.erosion_rate_csv,nx,ny,args.event_seconds)
    out=Path(args.output_dir);out.mkdir(parents=True,exist_ok=True)
    newz={};newsoil={};loose={}
    for k,z in z0.items():
        if soil[k]<0 or d0[k]<0 or d1[k]<0:
            raise ValueError(f"{k}: negative initial soil/loose sediment")
        g=gross[k]
        if g>soil[k]+1e-12:
            raise ValueError(f"{k}: soil detachment {g}m exceeds initial depth {soil[k]}m")
        newsoil[k]=max(0,soil[k]-g)
        loose[k]=d1[k]
        newz[k]=z-g+(d1[k]-d0[k])/1000
    newlines=[]
    errs=[]
    for iy in range(ny,0,-1):
        newlines.append(f"{iy:7d}\n")
        for b in range(1,nx+1,10):
            enc=[]
            for ix in range(b,min(nx,b+9)+1):
                ss,error=encode_g7(newz[iy,ix],args.max_rounding_m)
                enc.append(ss);errs.append(error)
            newlines.append("".join(enc)+"\n")
    final="".join(lines[:start]+newlines+lines[end:])
    parsed=read_frd(final)
    for k,v in parsed[-1].items():
        if abs(v-newz[k])>args.max_rounding_m+1e-12:
            raise AssertionError("Reparsed native FR39 exceeds rounding bound")
    (out/"input_next_frd.txt").write_text(final)
    write_grid(out/"next_dem.csv",newz,"elevation_m_unrounded")
    write_grid(out/"next_soil_depth.csv",newsoil,"depth_m")
    write_grid(out/"next_sy51_loose_depth.csv",loose,"s_t_dp_mm")
    summary={
        "source_engine":"original SHETRAN (no source modification)",
        "bridge_type":"EXTERNAL INTER-EVENT POSTPROCESSOR",
        "native_shetran_run_executed":False,
        "nx":nx,"ny":ny,"duration_s":args.event_seconds,
        "erosion_m_total_across_grid":sum(gross.values()),
        "loose_depth_delta_m_total_across_grid":sum((d1[k]-d0[k])/1000 for k in z0),
        "elevation_delta_m_min":min(newz[k]-z0[k] for k in z0),
        "elevation_delta_m_max":max(newz[k]-z0[k] for k in z0),
        "max_native_F7_rounding_m":max(errs),
        "integration":"trapezoid on sampled GNU rates; NOT an exact source internal GNU ledger",
        "restart_ready":False,
        "blocking_missing_initial_states":[
            "SY52 FBETA particle-size composition per cell at end of storm",
            "SY53 FDEL mobile sediment concentration per class unless demonstrably zero",
            "initial hydro state, surface head and canopy storage consistency after DEM change",
            "subsurface vertical layers and phreatic absolute elevations relative to new DEM",
            "source precision/time-step convergence and water/sediment conservation"
        ]
    }
    (out/"QA_AND_RESTART_BLOCKERS.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False))
    return summary

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for flag in ["frd","erosion-rate-csv","soil-depth-csv","loose-initial-csv",
                 "loose-final-csv","output-dir"]:
        p.add_argument("--"+flag,required=True)
    p.add_argument("--event-seconds",type=float,required=True)
    p.add_argument("--max-rounding-m",type=float,default=1e-5)
    a=p.parse_args()
    if a.event_seconds<=0 or a.max_rounding_m<0: p.error("Invalid durations/precision")
    print(json.dumps(run(a),indent=2,ensure_ascii=False))
if __name__=="__main__":main()
