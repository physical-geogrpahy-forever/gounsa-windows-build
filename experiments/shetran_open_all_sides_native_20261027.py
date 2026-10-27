#!/usr/bin/env python3
"""True outward conditional overland boundary using upstream OC TYPE 5.
NO new hydrology or sediment physics. For 0.648ha synthetic fixed 4m grid.
OC polynomial q_out = k*H^2 (m3/s), H=max(0,z_water-z_ground), for each
perimeter cell on one native NBFACE assigned side. k hypothetical, not measured.
The same OC polynomial is already present in the original SHETRAN source.
"""
import argparse
from pathlib import Path
from shetran_large_patch_matrix_20261027 import setup,ACTIVE,NX,NY

def patch_open_oc(directory,k=50.):
    assert k>0
    p=directory/"input_cob_ocd.txt"
    lines=p.read_text().splitlines(keepends=True)
    key=" GRID ELEMENT BOUNDARIES\n"
    assert lines.count(key)==1
    i=lines.index(key)
    assert lines[i+1].strip()=="0      0      0",lines[i+1]
    lines[i+1]="      0      0      1\n"
    new=[" OC5 TYPE5 PERIMETER POLYNOMIAL BOUNDARY (open: Q=-kH2)\n"]
    hits=0
    for y in range(NY,0,-1):
        chars=[]
        for x in range(1,NX+1):
            isedge=(x,y) in ACTIVE and (x in (2,16) or y in (2,28))
            chars.append("1" if isedge else "0")
            if isedge:hits+=1
        new.append(f"{y:7d} "+''.join(chars)+"\n")
    assert hits==80
    new.append(" OC5 category coefficients A B C D E\n")
    new.append(f"      1       0.0       0.0 {k:12.5f}       0.0       0.0\n")
    # Write after count, BEFORE default channel cross sections.
    lines[i+2:i+2]=new
    p.write_text("".join(lines))
    return {"active_boundary_cells":hits,"polynomial_k_m3_s_m2":k,
            "polynomial_form":"native OCQBC q=-(k*H^2), H water depth; only outward when H>0"}

def setup_open(src,dest,typ,rain,on,dt,k=50.):
    meta=setup(src,dest,typ,rain,on,dt)
    meta.update(patch_open_oc(dest,k))
    meta["hydraulic_boundary"]="Native OC type5, perimeter selected on north south east west"
    meta["physical_erosion_solver_changed"]=False
    meta["sediment_export_requires_native_budget_verification"]=True
    import json
    (dest/"scenario_metadata.json").write_text(json.dumps(meta,indent=2))
    return meta

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--original-model",type=Path,required=True)
    p.add_argument("--exe",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--rain",type=int,default=50,choices=[10,20,30,40,50])
    p.add_argument("--cover",default="mixed",choices=["bare","grass","oak_sparse","mixed"])
    p.add_argument("--k",type=float,default=50.)
    a=p.parse_args()
    import shetran_large_patch_matrix_20261027 as base
    old=base.setup
    base.setup=lambda src,dest,typ,rain,on,dt:setup_open(src,dest,typ,rain,on,dt,a.k)
    try:
        d=a.out;d.mkdir(parents=True,exist_ok=True)
        # Native solid ledger and final elevation QA, output is a preliminary probe.
        result,cells=base.execute(a.exe,a.original_model,d,a.cover,a.rain,True,.015625)
        print("QA_NATIVE_OPEN_RESULT",result)
    finally:
        base.setup=old
