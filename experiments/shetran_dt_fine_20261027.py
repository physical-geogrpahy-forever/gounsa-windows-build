#!/usr/bin/env python3
"""Original SHETRAN, same closed 0.2816ha land plot, finer native TMAX sensitivity.
Does not imply dx convergence or Gounsa observational validation.
"""
import argparse,json,numpy as np
from pathlib import Path
from shetran_timestep_refinement_20261027 import run_one

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--original-model",type=Path,required=True)
    a.add_argument("--exe",type=Path,required=True)
    a.add_argument("--out",type=Path,required=True)
    z=a.parse_args();z.out.mkdir(parents=True,exist_ok=True)
    all_cases={};summaries=[];mask0=None
    values=[.125,.0625,.03125,.015625]
    for t in values:
        for on in [True,False]:
            name=f"tmax_{t:g}_{'on' if on else 'off'}"
            row,depth,mask=run_one(z.original_model,z.exe,z.out/name,t,on)
            summaries.append(row);all_cases[(t,on)]=depth
            if mask0 is None:mask0=mask
            else:assert np.array_equal(mask0,mask)
    ref=values[-1]
    results=[]
    for t in values[:-1]:
        for on in [True,False]:
            a=next(r for r in summaries if r["tmax_hr"]==t and r["on"]==on)
            b=next(r for r in summaries if r["tmax_hr"]==ref and r["on"]==on)
            q=all_cases[(t,on)][mask0]-all_cases[(ref,on)][mask0]
            results.append({"tmax_hr":t,"on":on,
                "relative_detachment_difference_vs_finest":abs(a["original_source_solid_m3"]-b["original_source_solid_m3"])/max(abs(b["original_source_solid_m3"]),1e-12),
                "max_abs_local_DLS_difference_mm":float(np.max(np.abs(q))),
                "root_mean_square_local_DLS_difference_mm":float(np.sqrt(np.mean(q*q)))})
    full={"native_original_solver_with_only_logging":True,
      "experimental_grid_m":4,"spatial_resolution_not_tested":True,
      "finest_TMAX_hr":ref,"all_cases":summaries,"comparisons":results}
    (z.out/"fine_dt_comparison.json").write_text(json.dumps(full,indent=2))
    print("QA_FINE_DT "+json.dumps(full),flush=True)
if __name__=="__main__":main()
