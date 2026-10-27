#!/usr/bin/env python3
"""Audit canopy water closure and ET confounding for original model at 4m.
All figures SYNTHETIC, NO Gounsa observations; diagnostic prints only.
"""
import argparse,subprocess,json,math
from pathlib import Path
from collections import defaultdict
from shetran_mixed_canopy_native_20261027 import prepare

def run(src,exe,dir,on):
    prepare(src,dir,canopy_on=on,grid_m=4.,warmup_hr=1)
    p=subprocess.run([str(exe.resolve()),"-f","rundata_cob.txt"],cwd=dir,
        capture_output=True,text=True,timeout=250)
    (dir/"qa_canopy_stdout.txt").write_text(p.stdout+"\nSTDERR\n"+p.stderr)
    if p.returncode:raise RuntimeError(f"{on}: {p.returncode}: {p.stdout[-900:]}")
    summary=defaultdict(lambda:{"rain_mm":0.,"ground_mm":0.,"e_can_mm":0.,
        "storage_delta_mm":0.,"max_step_abs_residual_mm":0.,"root_mm":0.,
        "soil_mm":0.,"evap_other_mm":0.,"total_abs_residual_mm":0.,"n":0})
    hits=0
    for line in p.stdout.splitlines():
        k=line.find("QA_CANOPY")
        if k<0:continue
        a=line[k:].split()
        assert len(a)==12,a
        _,iel,*vals=a
        num=list(map(float,vals))
        time,dt,r,c0,c1,g,e,root,soil,other=num
        assert dt>0 and all(math.isfinite(v) for v in num)
        ie=int(iel);z=summary[ie]
        gross_mm=r*dt*1000
        ground_mm=g*dt*1000
        canopy_evap_mm=e*dt*1000
        resid=gross_mm-ground_mm-canopy_evap_mm-(c1-c0)
        z["rain_mm"]+=gross_mm;z["ground_mm"]+=ground_mm
        z["e_can_mm"]+=canopy_evap_mm;z["storage_delta_mm"]+=c1-c0
        z["max_step_abs_residual_mm"]=max(abs(resid),z["max_step_abs_residual_mm"])
        z["total_abs_residual_mm"]+=abs(resid)
        z["root_mm"]+=root*dt*1000
        z["soil_mm"]+=soil*dt*1000
        z["evap_other_mm"]+=other*dt*1000
        z["n"]+=1;hits+=1
    assert len(summary)==176,(len(summary),hits)
    assert all(v["n"]>1 for v in summary.values())
    maxstep=max(z["max_step_abs_residual_mm"] for z in summary.values())
    water_total=sum(abs(z["rain_mm"]-z["ground_mm"]-z["e_can_mm"]-z["storage_delta_mm"]) for z in summary.values())
    summary_out={"case":"on" if on else "off","n_active_cells":176,"n_element_steps":hits,
      "max_single_canopy_step_mass_error_mm":maxstep,
      "sum_abs_cell_final_canopy_mass_error_mm":water_total,
      "gross_rain_total_cell_mm":sum(z["rain_mm"] for z in summary.values()),
      "ground_supply_total_cell_mm":sum(z["ground_mm"] for z in summary.values()),
      "canopy_evap_total_cell_mm":sum(z["e_can_mm"] for z in summary.values()),
      "canopy_storage_delta_total_cell_mm":sum(z["storage_delta_mm"] for z in summary.values()),
      "root_uptake_total_cell_mm":sum(z["root_mm"] for z in summary.values()),
      "soil_evap_total_cell_mm":sum(z["soil_mm"] for z in summary.values()),
      "total_other_evap_cell_mm":sum(z["evap_other_mm"] for z in summary.values()),
      "no_snow_no_irrigation_assumed":True,
      "canopy_water_budget_pass":maxstep<1e-5 and water_total<1e-3}
    (dir/"canopy_water_summary.json").write_text(json.dumps(summary_out,indent=2))
    (dir/"canopy_water_cells.json").write_text(json.dumps(summary,indent=2))
    print("QA_CANOPY_WATER "+json.dumps(summary_out),flush=True)
    assert summary_out["canopy_water_budget_pass"],summary_out
    return summary_out
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--original-model",type=Path,required=True)
    p.add_argument("--exe",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    on=run(a.original_model,a.exe,a.out/"on",True)
    off=run(a.original_model,a.exe,a.out/"off",False)
    comp={"ON":on,"OFF":off,
      "root_uptake_ET_difference_mm_cell_total":on["root_uptake_total_cell_mm"]-off["root_uptake_total_cell_mm"],
      "soil_evap_ET_difference_mm_cell_total":on["soil_evap_total_cell_mm"]-off["soil_evap_total_cell_mm"],
      "other_evap_difference_mm_cell_total":on["total_other_evap_cell_mm"]-off["total_other_evap_cell_mm"],
      "canopy_ablative_ET_effect_is_zero":
         abs(on["root_uptake_total_cell_mm"]-off["root_uptake_total_cell_mm"])<1e-5 and
         abs(on["soil_evap_total_cell_mm"]-off["soil_evap_total_cell_mm"])<1e-5 and
         abs(on["total_other_evap_cell_mm"]-off["total_other_evap_cell_mm"])<1e-5}
    (a.out/"pair_qa_canopy.json").write_text(json.dumps(comp,indent=2))
    print("QA_CANOPY_ABLATION_ET "+json.dumps({k:v for k,v in comp.items() if k not in ["ON","OFF"]}),flush=True)
if __name__=="__main__":main()
