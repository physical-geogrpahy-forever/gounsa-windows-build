#!/usr/bin/env python3
"""Real native SHETRAN 4m spatial erosion / deposition-pathway audit.
Source SHETRAN Fortran physical solver equations unchanged. Separate
diagnostic-only print statements expose QSED for every cell and step.
This does not claim a hydrologically OPEN catchment.
"""
import json
import math
import argparse
import subprocess
from pathlib import Path
from collections import defaultdict
import numpy as np
from shetran_mixed_canopy_native_20261027 import prepare

def run_case(source,exe,out,label,on):
    d=out/label
    prepare(source,d,canopy_on=on,grid_m=4.,warmup_hr=1)
    p=subprocess.run([str(exe.resolve()),"-f","rundata_cob.txt"],cwd=d,
                     capture_output=True,text=True,timeout=300)
    (d/"native_spatial_stdout.txt").write_text(p.stdout+"\nSTDERR\n"+p.stderr)
    assert p.returncode==0,(p.returncode,p.stdout[-900:],p.stderr[-900:])
    totals=defaultdict(lambda:{"transfer_m3":0.,"source_m3":0.,"loose_final_m3":0.,
                               "suspended_final_m3":0.,"n":0,"time_last_hr":0.})
    global_steps=[]
    for line in p.stdout.splitlines():
        if "QA_SPATIAL" in line:
            a=line[line.index("QA_SPATIAL"):].split()
            assert len(a)==8,a
            _,x,y,time,delta,src,loose,susp=a
            x,y=int(x),int(y);time,delta,src,loose,susp=map(float,(time,delta,src,loose,susp))
            z=totals[(x,y)];z["transfer_m3"]+=delta;z["source_m3"]+=src
            z["loose_final_m3"]=loose;z["suspended_final_m3"]=susp
            z["n"]+=1;z["time_last_hr"]=time
        if "QA_SED_MASS" in line:
            a=line[line.index("QA_SED_MASS"):].split()
            assert len(a)==7,a
            global_steps.append(tuple(map(float,a[1:])))
    assert len(totals)==176,{"cells":len(totals)}
    assert len(global_steps)>4,len(global_steps)
    assert {v["n"] for v in totals.values()}=={len(global_steps)}
    assert all(math.isfinite(z) for v in totals.values() for z in v.values())
    gt=sum(v["transfer_m3"] for v in totals.values())
    src=sum(v["source_m3"] for v in totals.values())
    rows=np.array(global_steps,dtype=float)
    assert abs(src-rows[:,2].sum())<1e-7,(src,rows[:,2].sum())
    tol=1e-7
    intercell=[(x,y,v) for (x,y),v in totals.items()]
    imports=sorted([q for q in intercell if q[2]["transfer_m3"]>tol],
                   key=lambda q:-q[2]["transfer_m3"])
    exports=sorted([q for q in intercell if q[2]["transfer_m3"]< -tol],
                   key=lambda q:q[2]["transfer_m3"])
    active_source=[q for q in intercell if q[2]["source_m3"]>tol]
    storage_rise_from_transport=[
        q for q in imports if q[2]["loose_final_m3"]>0.336 + q[2]["source_m3"]*0.5
    ]
    # The input uses uniform SY43c porosity 0.3 and SY51c DLS 0.03m.
    # A true positive of (DLS_final - DLS_initial - local source) means
    # sediment solid retained in the local bed in EXCESS of locally
    # detached soil: thus a true transport-related deposition footprint,
    # not merely receiving sediment which may remain suspended.
    syd=(d/"input_cob_syd.txt").read_text().splitlines()
    def card_value(code):
        hits=[i for i,row in enumerate(syd[:-1]) if row.strip().startswith(code)]
        assert len(hits)==1,(code,hits)
        return float(syd[hits[0]+1].split()[0])
    porosity=card_value(":SY43c")
    loose_init_m=card_value(":SY51c")
    ini_solid_m3=(1-porosity)*16.0*loose_init_m
    stored_nonlocal=[]
    cell_budget_err=[]
    last_suspended=[]
    for x,y,z in intercell:
        bed_delta=(z["loose_final_m3"]-ini_solid_m3-z["source_m3"])
        z["net_lateral_bed_storage_gain_m3"]=bed_delta
        cell_budget_err.append((z["loose_final_m3"]+z["suspended_final_m3"])-
             (ini_solid_m3+z["source_m3"]+z["transfer_m3"]))
        last_suspended.append(z["suspended_final_m3"])
        stored_nonlocal.append((x,y,bed_delta))
    bed_gain=sorted([v for v in stored_nonlocal if v[2]>tol],key=lambda v:-v[2])
    bed_loss=sorted([v for v in stored_nonlocal if v[2]<-tol],key=lambda v:v[2])
    assert max(abs(q) for q in cell_budget_err)<1e-3, max(cell_budget_err)
    import_map={(x,y) for x,y,z in imports}
    export_map={(x,y) for x,y,z in exports}
    grid={}
    for x,y,z in intercell:
        grid[f"{x},{y}"]={"source_erosion_m3_solid":z["source_m3"],
             "net_sediment_import_m3_solid":z["transfer_m3"],
             "loose_final_m3_solid":z["loose_final_m3"],
             "suspended_final_m3_solid":z["suspended_final_m3"],
             "bed_stored_sediment_from_nonlocal_transfer_m3_solid":z["net_lateral_bed_storage_gain_m3"]}
    # ASCII map uses actual original Fortran ICMXY locations, no flip guesses.
    map_lines=[]
    for y in range(29,0,-1):
        chars=[]
        for x in range(1,18):
            z=totals.get((x,y))
            if z is None: chars.append(" ")
            elif z["transfer_m3"]>tol: chars.append("+")
            elif z["transfer_m3"]< -tol: chars.append("-")
            elif z["source_m3"]>tol: chars.append("e")
            else: chars.append(".")
        map_lines.append(f"{y:02d} "+ "".join(chars))
    report={"case":label,"run_original_fortran":"Original SHETRAN physical solver plus diagnostic WRITE only",
      "warmup_hr":1,"storm":"30mm/h for 3h after warmup, 12h total",
      "grid_m":4.0,"n_land_cells":len(totals),
      "n_native_internal_sediment_steps":len(global_steps),
      "original_soil_erosion_positive_cells":len(active_source),
      "soil_erosion_source_total_m3_solid":src,
      "net_intercell_sediment_import_cells":len(imports),
      "net_intercell_sediment_export_cells":len(exports),
      "no_significant_net_sediment_transfer_cells":len(intercell)-len(imports)-len(exports),
      "total_positive_net_import_m3":sum(q[2]["transfer_m3"] for q in imports),
      "total_negative_net_export_m3":sum(q[2]["transfer_m3"] for q in exports),
      "net_domain_internal_transport_m3":gt,
      "domain_internal_transport_closure_ok":abs(gt) < 1e-6,
      "initial_native_loose_sediment_m3_solid_per_cell":ini_solid_m3,
      "bed_sediment_gain_beyond_in_situ_erosion_cells":len(bed_gain),
      "bed_sediment_loss_beyond_in_situ_erosion_cells":len(bed_loss),
      "bed_sediment_gain_overlap_with_net_import_cells":len(import_map & {(x,y) for x,y,v in bed_gain}),
      "bed_sediment_loss_overlap_with_net_export_cells":len(export_map & {(x,y) for x,y,v in bed_loss}),
      "bed_sediment_total_positive_nonlocal_gain_m3":sum(v for x,y,v in bed_gain),
      "bed_sediment_total_negative_nonlocal_gain_m3":sum(v for x,y,v in bed_loss),
      "final_suspended_sediment_total_m3_solid":sum(last_suspended),
      "largest_absolute_single_cell_sediment_budget_residual_m3":max(abs(q) for q in cell_budget_err),
      "bed_gain_top_cells":[{"x":x,"y":y,"gain_m3":v} for x,y,v in bed_gain[:8]],
      "bed_loss_top_cells":[{"x":x,"y":y,"loss_m3":v} for x,y,v in bed_loss[:8]],
      "loose_and_suspended_cell_state_available":True,
      "gross_local_deposition_directly_computed":False,
      "local_sediment_import_is_not_always_sediment_deposition":True,
      "is_hydrologically_open_outlet":False,
      "top_import_cells":[{"x":x,"y":y,"net_import_m3":v["transfer_m3"],
         "source_erosion_m3":v["source_m3"]} for x,y,v in imports[:8]],
      "top_export_cells":[{"x":x,"y":y,"net_import_m3":v["transfer_m3"],
         "source_erosion_m3":v["source_m3"]} for x,y,v in exports[:8]],
      "spatial_ascii_legend":"+ net receiving; - net exporting; e local soil stripping no net transfer; blank outside",
      "spatial_ascii":map_lines}
    (d/"qa_spatial_summary.json").write_text(json.dumps(report,indent=2))
    (d/"qa_spatial_cells.json").write_text(json.dumps(grid,indent=2))
    print("QA_SPATIAL_SUMMARY "+json.dumps({k:v for k,v in report.items()
                if k not in ("spatial_ascii","top_import_cells","top_export_cells")}),flush=True)
    print("QA_SPATIAL_MAP\n"+"\n".join(map_lines),flush=True)
    print("QA_SPATIAL_IMPORT_LEADERS "+json.dumps(report["top_import_cells"]),flush=True)
    print("QA_LOCAL_BED_DEPOSITION "+json.dumps({k:v for k,v in report.items() if k.startswith("bed_sediment_") or k.startswith("final_suspended_") or k.startswith("initial_native_") or k.startswith("largest_absolute_")}),flush=True)
    print("QA_SPATIAL_EXPORT_LEADERS "+json.dumps(report["top_export_cells"]),flush=True)
    return report

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--original-model",type=Path,required=True)
    a.add_argument("--exe",type=Path,required=True)
    a.add_argument("--out",type=Path,required=True)
    args=a.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    reports=[run_case(args.original_model,args.exe,args.out,"on",True),
             run_case(args.original_model,args.exe,args.out,"off",False)]
    (args.out/"pair_spatial_summary.json").write_text(json.dumps(
        [{k:v for k,v in r.items() if k not in ("spatial_ascii","top_import_cells","top_export_cells")} for r in reports],indent=2))
if __name__=="__main__":main()
