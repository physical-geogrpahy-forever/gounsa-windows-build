#!/usr/bin/env python3
"""Spatial/local event-end Δz convergence under ACTUAL native TMAX.
Fixed PMAX=1mm, BSOFT false, synthetic 0.2816ha two-species 4m closed plot.
Real original SHETRAN water+sediment equations, instrumentation WRITE only.
"""
import argparse,json
from pathlib import Path
import numpy as np
from shetran_net_surface_change_tmax_20261027 import simulate

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--original-model",type=Path,required=True)
    a.add_argument("--exe",type=Path,required=True)
    a.add_argument("--out",type=Path,required=True)
    z=a.parse_args();z.out.mkdir(parents=True,exist_ok=True)
    ts=(.03125,.015625,.007812,.003906)
    results={};summary=[]
    for t in ts:
        for on in (True,False):
            label=f"t_{t:.6f}_{'on' if on else 'off'}"
            d=z.out/label
            grid,report=simulate(z.original_model,z.exe,d,on,tmax_hr=t)
            results[(t,on)]=grid
            summary.append({"tmax_hr":t,**report})
    fin=ts[-1];comparisons=[]
    for t in ts[:-1]:
        for on in (True,False):
            a=results[(t,on)];b=results[(fin,on)]
            assert set(a)==set(b)
            dz=np.array([a[k]["delta_z_event_end_mm"]-b[k]["delta_z_event_end_mm"] for k in sorted(a)])
            es=np.array([a[k]["original_substrate_erosion_mm"]-b[k]["original_substrate_erosion_mm"] for k in sorted(a)])
            early={k for k in a if a[k]["delta_z_event_end_mm"]>0.001}
            late={k for k in b if b[k]["delta_z_event_end_mm"]>0.001}
            comparisons.append({"tmax_hr":t,"on":on,"reference_tmax_hr":fin,
              "mean_abs_cell_net_elevation_change_difference_mm":float(np.abs(dz).mean()),
              "rms_cell_net_elevation_change_difference_mm":float(np.sqrt(np.mean(dz**2))),
              "max_abs_cell_net_elevation_change_difference_mm":float(np.abs(dz).max()),
              "mean_abs_cell_original_erosion_depth_difference_mm":float(np.abs(es).mean()),
              "positive_elevation_cells_tmax":len(early),
              "positive_elevation_cells_finest":len(late),
              "net_deposition_cell_overlap":len(early&late),
              "net_deposition_union":len(early|late),
              "signed_positive_cell_disagreements":len(early^late)})
    output={"true_TMAX_4th_FRD_field_modified":True,"PMAX_1mm_fixed":True,"BSOFT_off":True,
       "plot":"synthetic 0.2816 ha closed 4m 176 cells, not real Gounsa",
       "finest_tmax_hr":fin,"summary":summary,"comparisons":comparisons}
    (z.out/"spatial_native_tmax_convergence.json").write_text(json.dumps(output,indent=2))
    print("QA_NATIVE_SPATIAL_TMAX "+json.dumps({"comparisons":comparisons}),flush=True)
if __name__=="__main__":main()
