#!/usr/bin/env python3
"""Original SHETRAN output DIAGNOSTIC only: per-cell event-end elevation change.
The original model does not feed this change back into its flow solver.
IMPORTANT: Synthetic closed 4m microdomain. NOT Gounsa site results.
"""
import argparse, json, subprocess, math
from pathlib import Path
from collections import defaultdict
import numpy as np
from shetran_mixed_canopy_native_20261027 import prepare

def simulate(src,exe,folder,on):
    prepare(src,folder,canopy_on=on,grid_m=4.,warmup_hr=1)
    p=subprocess.run([str(exe.resolve()),"-f","rundata_cob.txt"],cwd=folder,
                      capture_output=True,text=True,timeout=180)
    (folder/"qa_morph_stdout.txt").write_text(p.stdout+"\nSTDERR\n"+p.stderr)
    if p.returncode: raise RuntimeError(f"{folder}: exit {p.returncode} {p.stderr[-800:]} {p.stdout[-1000:]}")
    d=defaultdict(lambda:{"source_m3":0.,"inflow_m3":0.,"erosion_depth_m":0.,
                          "n":0,"loose_m3":0.,"susp_m3":0.,"FETA":float("nan")})
    for line in p.stdout.splitlines():
        j=line.find("QA_SPATIAL")
        if j<0: continue
        q=line[j:].split()
        assert len(q)==10,q
        _,xi,yi,time,inflow,source,loose,susp,erosion_depth,feta=q
        x,y=int(xi),int(yi)
        vals=list(map(float,[time,inflow,source,loose,susp,erosion_depth,feta]))
        assert all(map(math.isfinite,vals))
        time,inflow,source,loose,susp,erosion_depth,feta=vals
        z=d[(x,y)]
        z["source_m3"]+=source
        z["inflow_m3"]+=inflow
        z["erosion_depth_m"]+=erosion_depth
        z["n"]+=1
        z["loose_m3"]=loose
        z["susp_m3"]=susp
        z["FETA"]=feta
    assert len(d)==176,len(d)
    ns={v["n"] for v in d.values()};assert len(ns)==1,ns
    lines=(folder/"input_cob_syd.txt").read_text().splitlines()
    def val(prefix):
        a=[i for i,x in enumerate(lines[:-1]) if x.strip().startswith(prefix)]
        assert len(a)==1,(prefix,a)
        return float(lines[a[0]+1].split()[0])
    p0=val(":SY43c");d0=val(":SY51c");area=16.0
    m0=(1-p0)*area*d0
    tol=1e-8
    results={}
    for (x,y),v in sorted(d.items()):
        loose_end_m=v["loose_m3"]/((1-p0)*area)
        v["delta_loose_depth_mm"]=1000*(loose_end_m-d0)
        v["original_substrate_erosion_mm"]=1000*v["erosion_depth_m"]
        v["delta_z_event_end_mm"]=v["delta_loose_depth_mm"]-v["original_substrate_erosion_mm"]
        v["gain_from_nonlocal_m3"]=v["loose_m3"]-m0-v["source_m3"]
        v["balance_residual_m3"]=v["loose_m3"]+v["susp_m3"]-m0-v["source_m3"]-v["inflow_m3"]
        # Independent physical conversion consistency native FETA = (1-THSAT)/(1-PLS)
        solid_soil_density_fraction=v["FETA"]*(1-p0)
        implied_solid_soil_source_m3=v["erosion_depth_m"]*area*solid_soil_density_fraction
        v["source_consistency_m3"]=implied_solid_soil_source_m3-v["source_m3"]
        results[f"{x},{y}"]=v
    net=np.array([v["delta_z_event_end_mm"] for v in results.values()])
    er=np.array([v["original_substrate_erosion_mm"] for v in results.values()])
    deposit=np.array([v["delta_loose_depth_mm"] for v in results.values()])
    tol_mm=0.001
    pos=[(k,v) for k,v in results.items() if v["delta_z_event_end_mm"]>tol_mm]
    neg=[(k,v) for k,v in results.items() if v["delta_z_event_end_mm"] < -tol_mm]
    selected={"scenario":"ON" if on else "OFF", "model":"Original SHETRAN with diagnostic prints only",
       "is_postprocessed_event_end":True,
       "dynamic_dem_feedback_during_storm":False,
       "actual_Gounsa_observations_used":False,
       "outlet_closed":True,
       "cell_area_m2":16.0, "n_land_cells":176,"n_sediment_substeps":ns.pop(),
       "n_cells_net_elevation_gain_gt_1micrometre":len(pos),
       "n_cells_net_elevation_loss_lt_minus_1micrometre":len(neg),
       "n_nearly_zero":176-len(pos)-len(neg),
       "gross_original_substrate_erosion_total_m3_thickness":float(er.sum()/1000*area),
       "net_domain_surface_volume_change_m3":float(net.sum()/1000*area),
       "min_max_net_elevation_mm":[float(net.min()),float(net.max())],
       "mean_net_elevation_mm":float(net.mean()),
       "max_abs_local_material_residual_m3":max(abs(v["balance_residual_m3"]) for v in results.values()),
       "max_abs_local_erosion_source_unit_consistency_m3":max(abs(v["source_consistency_m3"]) for v in results.values()),
       "top_deposition":[{"cell":k,"delta_z_mm":v["delta_z_event_end_mm"],
                          "loose_change_mm":v["delta_loose_depth_mm"],
                          "substrate_erosion_mm":v["original_substrate_erosion_mm"]}
                         for k,v in sorted(pos,key=lambda a:-a[1]["delta_z_event_end_mm"])[:8]],
       "top_erosion":[{"cell":k,"delta_z_mm":v["delta_z_event_end_mm"],
                          "loose_change_mm":v["delta_loose_depth_mm"],
                          "substrate_erosion_mm":v["original_substrate_erosion_mm"]}
                         for k,v in sorted(neg,key=lambda a:a[1]["delta_z_event_end_mm"])[:8]]}
    (folder/"net_elevation_cells.json").write_text(json.dumps(results,indent=2))
    (folder/"net_elevation_summary.json").write_text(json.dumps(selected,indent=2))
    print("QA_NET_SURFACE_CHANGE "+json.dumps(selected),flush=True)
    return results,selected

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--exe",type=Path,required=True)
    a.add_argument("--original-model",type=Path,required=True)
    a.add_argument("--out",type=Path,required=True)
    args=a.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    x,a=simulate(args.original_model,args.exe,args.out/"on",True)
    y,b=simulate(args.original_model,args.exe,args.out/"off",False)
    assert set(x)==set(y)
    diff={k:x[k]["delta_z_event_end_mm"]-y[k]["delta_z_event_end_mm"] for k in x}
    vals=np.array(list(diff.values()))
    result={"difference":"ON-minus-OFF", "n":len(diff),
            "max_abs_delta_z_diff_mm":float(np.max(np.abs(vals))),
            "mean_delta_z_diff_mm":float(np.mean(vals)),
            "positive_change_cells":int((vals>0.001).sum()),
            "negative_change_cells":int((vals< -0.001).sum()),
            "full_coupled_morphodynamic_reprediction":False}
    (args.out/"on_minus_off_elevation_change.json").write_text(json.dumps(
        {"summary":result,"delta_z_cell_mm":diff},indent=2))
    print("QA_MORPH_DIFFERENCE "+json.dumps(result),flush=True)
if __name__=="__main__":main()
