#!/usr/bin/env python3
"""Native source-engine sweeps: mechanistic plant-structure counterfactuals, never a
calibrated Gounsa Miscanthus vs coppice estimate. Keeps all solver laws unchanged."""
import argparse, json, subprocess, sys, math, statistics, csv
from pathlib import Path
ROOT=Path(__file__).resolve().parent
RAINS=[10,20,30,40,50]
# Original EUROSEM shade/drip/stemflow geometry; field means not transferred as event observations.
CANOPIES={
 "control":dict(cover=.15,storage=.90,shape=2,angle=55,plant_height=3.0),
 "oak_canopy":dict(cover=.55,storage=1.5,shape=2,angle=55,plant_height=2.5),
 "miscanthus_canopy":dict(cover=.75,storage=1.5,shape=1,angle=75,plant_height=1.2),
}
# These are *hypothetical* hydraulics / surface states. Assignments are NOT species facts.
EXTRA={
 "oak_assumed_soil":dict(fmin=10,manning=.14,erod=.7,spltex=1.6),
 "miscanthus_assumed_soil":dict(fmin=7,manning=.24,erod=.65,spltex=1.5),
}
EU_BASE=dict(fmin=5.0,manning=.188,erod=.9,spltex=2.0,pbase=.05,slope=.85)
SW_BASE=dict(ks=.000002,roughness=.1,a=.25,ad=.25,f=.004)

def cases_eurosem():
    out=[]
    for rain in RAINS:
        for name in ["control","oak_canopy","miscanthus_canopy","oak_assumed_soil","miscanthus_assumed_soil"]:
            canopy=CANOPIES["oak_canopy"] if name=="oak_assumed_soil" else CANOPIES["miscanthus_canopy"] if name=="miscanthus_assumed_soil" else CANOPIES[name]
            params={**EU_BASE,**canopy,**EXTRA.get(name,{})}
            out.append((rain,name,params))
    oat=[
       ("cover",[0,.3,.55,.75,.9]),("storage",[.5,1.5,3]),("shape",[1,2]),
       ("angle",[35,55,75]),("plant_height",[.5,1.2,3.0]),
       ("fmin",[3,5,10,20]),("manning",[.1,.188,.3]),
       ("erod",[.3,.9,1.8]),("spltex",[1,2,4]),("pbase",[0,.05,.10]),
       ("slope",[.3,.6,.85])]
    for var,vals in oat:
        for v in vals:
            params={**EU_BASE,**CANOPIES["oak_canopy"],var:v}
            out.append((30,"oat_"+var+"_"+str(v).replace(".","p"),params))
    return out
def cases_swehr():
    out=[]
    for rain in RAINS:
        for name in ["control","oak_canopy","miscanthus_canopy","oak_assumed_soil","miscanthus_assumed_soil"]:
            canopy=CANOPIES["oak_canopy"] if name=="oak_assumed_soil" else CANOPIES["miscanthus_canopy"] if name=="miscanthus_assumed_soil" else CANOPIES[name]
            # The published EUROSEM interception capacity equation, computed at event duration.
            c=canopy["cover"];storage=canopy["storage"]
            loss=c*storage*(-math.expm1(-rain))
            state=SW_BASE.copy()
            if name=="oak_assumed_soil":state.update(ks=.000004,roughness=.13,a=.18,ad=.22,f=.003)
            if name=="miscanthus_assumed_soil":state.update(ks=.000002,roughness=.2,a=.12,ad=.17,f=.0025)
            out.append((rain,name,dict(**state,canopy_loss_mm=loss)))
    oat=[
       ("ks",[0,0.000001,0.000002,0.000004,0.000008]),
       ("roughness",[.05,.1,.2,.3]),
       ("a",[.05,.25,.5,1]),
       ("ad",[.05,.25,.5,1]),
       ("f",[.001,.004,.01]),
       ("canopy_loss_mm",[0,.5,1.0,2.0,4.0])]
    for var,vs in oat:
        for v in vs:
            params={**SW_BASE, "canopy_loss_mm":CANOPIES["oak_canopy"]["cover"]*CANOPIES["oak_canopy"]["storage"],var:v}
            out.append((30,"oat_"+var+"_"+str(v).replace(".","p"),params))
    return out
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--engine",choices=["eurosem","swehr"],required=True)
    a=p.parse_args()
    cases=cases_eurosem() if a.engine=="eurosem" else cases_swehr()
    out=ROOT/"species_sensitivity"/a.engine
    out.mkdir(parents=True,exist_ok=True)
    records=[]
    for idx,(rain,name,params) in enumerate(cases):
        tag=f"{idx:03d}_{name}"
        script="verify_eurosem_native.py" if a.engine=="eurosem" else "verify_swehr_closure.py"
        cmd=[sys.executable,str(ROOT/script),"--rain",str(rain),"--tag",tag]
        if a.engine=="eurosem":
            for k,v in params.items():cmd += ["--"+k.replace("_","-"),str(v)]
            folder=ROOT/f"eurosem_QA_{tag}_r{rain:02d}_rep1"
        else:
            cmd+=["--seconds","3600","--erosion","on","--boundary","open"]
            for k,v in params.items():cmd+=["--"+k.replace("_","-"),str(v)]
            folder=ROOT/"runtime"/f"{tag}_{rain:02d}_3600_on_open_{params['ks']:.1g}"
        try:
            done=subprocess.run(cmd,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                                text=True,encoding="latin1",timeout=105)
            summary=json.loads((folder/"qa_result.json").read_text())
            status="run_pass" if done.returncode==0 else "qa_fail"
            output=done.stdout
        except Exception as e:
            summary={}
            status="exception";output=repr(e)
        rec=dict(engine=a.engine,tag=tag,scenario=name,rain_mm_h=rain,
                 parameters=params,program_status=status,**{k:v for k,v in summary.items() if k not in ("scenario","parameters")})
        records.append(rec)
        print("RUN",len(records),len(cases),name,rain,status,
              json.dumps({k:rec.get(k) for k in ["water_pass","sediment_pass","independent_layer_pass","canopy","net_boundary_sediment_out_kg","net_erosion_kg","gross_detachment_kg"]}),flush=True)
        if status=="exception":print("ERROR",output[-3000:],flush=True)
    (out/"results.json").write_text(json.dumps(records,indent=2,ensure_ascii=False))
    rows=[]
    for rec in records:
        row=dict(engine=rec["engine"],rain_mm_h=rec["rain_mm_h"],scenario=rec["scenario"],program_status=rec["program_status"])
        row.update({f"param_{k}":v for k,v in rec["parameters"].items()})
        for k,v in rec.items():
            if k not in ("parameters","scenario","engine","rain_mm_h","program_status"):
                row[k]=json.dumps(v) if isinstance(v,(dict,list)) else v
        if a.engine=="swehr" and "net_boundary_sediment_out_kg" in rec:
            row["export_t_ha"]=rec["net_boundary_sediment_out_kg"]/9.5625*10
            row["gross_detach_t_ha"]=rec["original_soil_detachment_kg"]/9.5625*10
            row["water_outflow_mm"]=rec["net_boundary_water_out_m3"]/9.5625*1000
        if a.engine=="eurosem" and rec.get("net_erosion_kg"):
            row["net_erosion_t_ha"]=sum(rec["net_erosion_kg"])/14500*10
            row["gross_detach_t_ha"]=sum(rec["gross_detachment_kg"])/14500*10
        rows.append(row)
    keys=sorted(set().union(*(r.keys() for r in rows)))
    with (out/"results.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,keys);w.writeheader();w.writerows(rows)
    valid=sum(1 for x in records if x["program_status"]=="run_pass")
    print("TOTAL",a.engine,valid,len(records),flush=True)
    if valid==0:raise SystemExit(2)
if __name__=="__main__":main()
