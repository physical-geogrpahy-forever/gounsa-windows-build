#!/usr/bin/env python3
"""Seven SHETRAN original-model physical runs at one rain intensity with all
four perimeter edges using native TYPE5 open boundary, plus original native
QOC/QSED independently diagnosed. Matrix: 5 rain intensities x 7 =35.
"""
import argparse,json,csv
from pathlib import Path
import shetran_large_patch_matrix_20261027 as m
from shetran_open_all_sides_native_20261027 import setup_open

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--original-model",type=Path,required=True)
    a.add_argument("--exe",type=Path,required=True)
    a.add_argument("--out",type=Path,required=True)
    a.add_argument("--rain",type=int,choices=[10,20,30,40,50],required=True)
    a.add_argument("--polynomial-k",type=float,default=50.)
    args=a.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    original=m.setup
    m.setup=lambda src,dest,typ,rain,on,dt:setup_open(src,dest,typ,rain,on,dt,args.polynomial_k)
    out=[];cells={}
    try:
        for typ in m.VEG_CASES:
            for on in ([True] if typ=="bare" else [True,False]):
                row,c=m.execute(args.exe,args.original_model,args.out,typ,args.rain,on,.015625)
                # HARD REQUIREMENT: genuinely outgoing sediment and water
                # should be documented separately; a zero is a valid result
                # only if the native values really give zero.
                assert row["native_water_border_net_export_m3"] is not None
                out.append(row);cells[(typ,on)]=c
    finally:
        m.setup=original
    contrasts=[]
    bare=next(q for q in out if q["type"]=="bare")
    for typ in ("grass","oak_sparse","mixed"):
        aon=next(q for q in out if q["type"]==typ and q["canopy_on"])
        aoff=next(q for q in out if q["type"]==typ and not q["canopy_on"])
        same=[cells[(typ,True)][key]["delta_z_mm"]-cells[(typ,False)][key]["delta_z_mm"] for key in cells[(typ,True)]]
        contrasts.append({"type":typ,"rain_mm_h":args.rain,
         "fraction_original_soil_erosion_vs_bare":aon["source_detachment_solid_m3"]/max(bare["source_detachment_solid_m3"],1e-12),
         "canopy_ON_minus_OFF_erosion_source_m3":aon["source_detachment_solid_m3"]-aoff["source_detachment_solid_m3"],
         "canopy_ON_minus_OFF_border_sediment_out_m3":aon["native_sediment_border_net_export_m3_solid"]-aoff["native_sediment_border_net_export_m3_solid"],
         "canopy_ON_minus_OFF_border_water_out_m3":aon["native_water_border_net_export_m3"]-aoff["native_water_border_net_export_m3"],
         "max_abs_cell_ON_minus_OFF_delta_z_mm":max(abs(q) for q in same)})
    q={"rain_mm_h":args.rain,"n_runs":len(out),"four_sides_open_native_OC_type5":True,
       "coefficient_k":args.polynomial_k,"native_original_physics_unchanged":True,
       "boundary_capacity_only_NOCTAB_180":True,"hypothetical_inputs":True,
       "max_relative_native_mass_residual":max(d["relative_sediment_mass_error"] for d in out),
       "native_water_export_positive_cases":sum(d["native_water_border_net_export_m3"]>1e-9 for d in out),
       "native_sediment_export_positive_cases":sum(d["native_sediment_border_net_export_m3_solid"]>1e-10 for d in out),
       "cases":out,"comparisons":contrasts}
    (args.out/"open_intensity_results.json").write_text(json.dumps(q,indent=2))
    cols=["type","rain_mm_h","canopy_on","source_detachment_solid_m3",
         "native_water_border_net_export_m3","native_sediment_border_net_export_m3_solid",
         "relative_sediment_mass_error","net_elevation_gain_cells",
         "max_net_deposition_mm","max_net_erosion_mm","mean_net_event_z_mm"]
    with (args.out/"open_intensity_summary.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=cols);w.writeheader()
        for x in out:w.writerow({k:x[k] for k in cols})
    print("QA_OPEN_ALL_FOUR_BORDERS_COMPLETE "+json.dumps(q),flush=True)
    assert q["max_relative_native_mass_residual"]<1e-3
    assert q["native_water_export_positive_cases"]>=1,"No native water export: openness not proven"
    assert q["native_sediment_export_positive_cases"]>=1,"No native sediment export: sediment openness not proven"
if __name__=="__main__":main()
