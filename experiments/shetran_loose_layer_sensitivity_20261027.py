#!/usr/bin/env python3
"""Original native SHETRAN sensitivity to 0/1/10/30 mm initial mobile soil.
Same synthetic 4m 0.2816ha mixed vegetation, no flow equation modifications.
Not field calibrated and no finite original soil depth gate in original model.
"""
import argparse,json,subprocess
from pathlib import Path
import numpy as np
from shetran_mixed_canopy_native_20261027 import prepare,extract

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--exe",type=Path,required=True)
    a.add_argument("--original-model",type=Path,required=True)
    a.add_argument("--out",type=Path,required=True)
    z=a.parse_args();z.out.mkdir(parents=True,exist_ok=True)
    r=[]
    for loose_mm in (0.,1.,10.,30.):
        for canopy in (True,False):
            label=f"loose_{loose_mm:g}mm_"+("ON" if canopy else "OFF")
            d=z.out/label
            prepare(z.original_model,d,canopy_on=canopy,grid_m=4.,warmup_hr=1)
            f=d/"input_cob_syd.txt";ls=f.read_text().splitlines(keepends=True)
            k=next(i for i,v in enumerate(ls) if v.strip().startswith(":SY51c"))
            ls[k+1]=f"{loose_mm*0.001:10.7f}\n"
            f.write_text("".join(ls))
            p=subprocess.run([str(z.exe.resolve()),"-f","rundata_cob.txt"],cwd=d,
                             capture_output=True,text=True,timeout=150)
            (d/"native_log.txt").write_text(p.stdout+"\nSTDERR\n"+p.stderr)
            row={"initial_loose_mm":loose_mm,"canopy_on":canopy,"native_exit":p.returncode}
            if p.returncode==0:
                e=extract(d/"output_cob_shegraph.h5")
                row.update({"native_output_ok":True,"peak_instant_erosion_mm_day":e["peak_erosion_mm_day"],
                   "mean_DLS_final_mm":e["final_loose_mm_mean"],
                   "net_mean_DLS_change_mm":e["final_loose_mm_mean"]-loose_mm})
                time=[];source=[];res=[]
                for ln in p.stdout.splitlines():
                    i=ln.find("QA_SED_MASS")
                    if i<0:continue
                    q=ln[i:].split()
                    assert len(q)==7,q
                    vals=list(map(float,q[1:]))
                    time.append(vals[0]);source.append(vals[2]);res.append(vals[-1])
                assert len(time)>0,label
                row.update({"n_substeps":len(time),"eroded_original_soil_m3_solid":sum(source),
                     "max_abs_substep_residual_m3":max(abs(v) for v in res),
                     "total_abs_sediment_ledger_residual_m3":abs(sum(res))})
            else:
                row.update({"native_output_ok":False,"problem":"see per-case native log; don't infer numerical failure from input errors"})
            (d/"one_case.json").write_text(json.dumps(row,indent=2))
            r.append(row)
            print("QA_INITIAL_LOOSE_LAYER "+json.dumps(row),flush=True)
    (z.out/"all_initial_loose_layer_tests.json").write_text(json.dumps(r,indent=2))
    assert all(v["native_output_ok"] for v in r),"One or more original native runs did not complete: see QA_INITIAL_LOOSE_LAYER"
if __name__=="__main__":main()
