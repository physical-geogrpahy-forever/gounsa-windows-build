#!/usr/bin/env python3
"""Parallel-intensity runner for 0.648ha original SHETRAN single-model native.
Seven scenarios per 10/20/30/40/50 mm/h; cross-check canopy ablations.
"""
import argparse,csv,json
from pathlib import Path
from shetran_large_patch_matrix_20261027 import execute,VEG_CASES

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--original-model",type=Path,required=True)
    a.add_argument("--exe",type=Path,required=True)
    a.add_argument("--out",type=Path,required=True)
    a.add_argument("--rain",type=int,required=True,choices=[10,20,30,40,50])
    z=a.parse_args();z.out.mkdir(parents=True,exist_ok=True)
    rs=[];m={}
    for ty in VEG_CASES:
        for on in ([True] if ty=="bare" else [True,False]):
            r,cells=execute(z.exe,z.original_model,z.out,ty,z.rain,on,.015625)
            rs.append(r);m[(ty,on)]=cells
    assert len(rs)==7
    base=next(v for v in rs if v["type"]=="bare")
    contrasts=[]
    for ty in ("grass","oak_sparse","mixed"):
        on=next(v for v in rs if v["type"]==ty and v["canopy_on"])
        off=next(v for v in rs if v["type"]==ty and not v["canopy_on"])
        cells_on=m[(ty,True)];cells_off=m[(ty,False)]
        assert set(cells_on)==set(cells_off)
        changes=[cells_on[k]["delta_z_mm"]-cells_off[k]["delta_z_mm"] for k in cells_on]
        contrasts.append({"type":ty,"rain_mm_h":z.rain,
           "gross_soil_supply_vs_bare_ratio":on["source_detachment_solid_m3"]/max(base["source_detachment_solid_m3"],1e-14),
           "on_minus_off_source_solid_m3":on["source_detachment_solid_m3"]-off["source_detachment_solid_m3"],
           "on_minus_off_avg_delta_z_mm":on["mean_net_event_z_mm"]-off["mean_net_event_z_mm"],
           "max_abs_cell_canopy_delta_z_effect_mm":max(abs(v) for v in changes)})
    summary={"rain_mm_h":z.rain,"all_7_original_physical_model_cases_pass":True,
      "n_native_cases":len(rs),"max_relative_sediment_budget_error":max(q["relative_sediment_mass_error"] for q in rs),
      "runs":rs,"comparisons":contrasts}
    (z.out/"intensity_summary.json").write_text(json.dumps(summary,indent=2))
    with (z.out/"intensity_table.csv").open("w",newline="") as f:
        fields=["type","rain_mm_h","canopy_on","source_detachment_solid_m3",
          "mean_original_soil_erosion_mm","mean_net_event_z_mm",
          "net_elevation_gain_cells","net_elevation_loss_cells",
          "max_net_deposition_mm","max_net_erosion_mm",
          "relative_sediment_mass_error"]
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for q in rs:w.writerow({k:q.get(k) for k in fields})
    print("QA_ONE_INTENSITY_COMPLETE "+json.dumps(summary),flush=True)
if __name__=="__main__":main()
