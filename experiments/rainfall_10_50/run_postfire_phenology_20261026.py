#!/usr/bin/env python3
"""Re-run both native model solvers under a controlled seasonal vegetation-state
counterfactual. All values are hypothetical structural endpoints, NOT a field-based
calibration to the 2025 Gounsa fire. NO root-to-Ks empirical mapping.
Published EUROSEM native INTERC handles split. Published SWEHR takes uniform net
rain after EUROSEM storage only; NO spatial SF/drip physics.
"""
import argparse,subprocess,sys,json,csv
from pathlib import Path
R=Path(__file__).resolve().parent
# independent vegetation STATE contrasting site history, not 'species constant':
SCENARIOS={
"oak_leafless": dict(cover=.08,storage=.4,shape=2,angle=80.,plant_height=.3),
"oak_early_leafon":dict(cover=.30,storage=1.,shape=2,angle=80.,plant_height=.8),
"oak_dense_leafon":dict(cover=.70,storage=1.8,shape=2,angle=80.,plant_height=1.6),
"miscanthus_early":dict(cover=.25,storage=1.,shape=1,angle=75.,plant_height=.6),
"miscanthus_dense":dict(cover=.75,storage=1.5,shape=1,angle=75.,plant_height=1.2),
"miscanthus_senescent":dict(cover=.20,storage=.4,shape=1,angle=75.,plant_height=.7),
}
def main():
    p=argparse.ArgumentParser();p.add_argument("--engine",choices=["eurosem","swehr"],required=True);a=p.parse_args()
    results=[]
    for rain in (10,20,30,40,50):
      for name,v in SCENARIOS.items():
        cmd=[sys.executable,str(R/("verify_eurosem_native.py" if a.engine=="eurosem" else "verify_swehr_closure.py")),
           "--rain",str(rain),"--tag","postfire_"+name]
        if a.engine=="eurosem":
            for k,x in v.items():cmd+=["--"+k.replace("_","-"),str(x)]
            folder=R/f"eurosem_QA_postfire_{name}_r{rain:02d}_rep1"
        else:
            # as in the earlier archive, intensity-constant 1h canopy-storage loss.
            # The formula matches the native EUROSEM canopy STORAGE equation;
            # no assumption that the free TF/SF/drip partition has local spatial effect.
            import math
            event_I=v["cover"]*v["storage"]*(-math.expm1(-rain))
            cmd+=["--seconds","3600","--erosion","on","--boundary","open",
                 "--ks","0.000002","--roughness","0.1","--a","0.25",
                 "--ad","0.25","--f","0.004","--canopy-loss-mm",str(event_I)]
            folder=R/"runtime"/f"postfire_{name}_{rain:02d}_3600_on_open_2e-06"
        try:
            run=subprocess.run(cmd,cwd=R,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                               encoding="latin1",text=True,timeout=150)
            result=json.loads((folder/"qa_result.json").read_text())
            result["status"]="pass" if run.returncode==0 else "fail"
        except Exception as e:
            result={"status":"error","exception":repr(e)}
        result.update(engine=a.engine,scenario=name,plant=v,rain_mm_h=rain)
        if a.engine=="swehr" and "net_boundary_sediment_out_kg" in result:
            result["sediment_export_t_ha"]=result["net_boundary_sediment_out_kg"]/9.5625*10
            result["outflow_mm"]=result["net_boundary_water_out_m3"]/9.5625*1000
        if a.engine=="eurosem" and result.get("net_erosion_kg"):
            result["reported_net_erosion_t_ha"]=sum(result["net_erosion_kg"])/14500*10
        results.append(result)
        print("SCENARIO",rain,name,result.get("status"),"runoff",result.get("outflow_mm",result.get("runoff_mm")),
              "SF",result.get("canopy",{}).get("stemflow_mm"),"export",result.get("sediment_export_t_ha"),
              "reported",result.get("reported_net_erosion_t_ha"),flush=True)
    od=R/"phenology_20261026"/a.engine
    od.mkdir(parents=True,exist_ok=True)
    (od/"results.json").write_text(json.dumps(results,ensure_ascii=False,indent=2))
    columns=["rain_mm_h","scenario","status","outflow_mm","runoff_mm","sediment_export_t_ha","reported_net_erosion_t_ha","water_pass","sediment_pass","independent_layer_pass","canopy","plant","water_error_pct"]
    with (od/"results.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,columns);w.writeheader()
        for rec in results:w.writerow({k:json.dumps(rec[k]) if isinstance(rec.get(k),(dict,list)) else rec.get(k) for k in columns})
    print("PASS",a.engine,sum(x.get("status")=="pass" for x in results),len(results))
if __name__=="__main__":main()
