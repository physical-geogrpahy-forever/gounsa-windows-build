#!/usr/bin/env python3
"""Run original SHETRAN with additive QA logging (no physics source changes).
Tests native active 4m 2D mixed oak/Miscanthus, 30mm/h x3h.
"""
import argparse, sys, json, subprocess, re
from pathlib import Path
from shetran_mixed_canopy_native_20261027 import prepare

def run(exe,source,root,label,on,grid):
    d=root/label
    prepare(source,d,on,grid)
    p=subprocess.run([str(exe.resolve()),"-f","rundata_cob.txt"],cwd=d,
        capture_output=True,text=True,timeout=300)
    (d/"qa_native_stdout.log").write_text(p.stdout+"\nSTDERR\n"+p.stderr)
    if p.returncode:
        spr=d/"output_cob_spr.txt"
        tail=spr.read_text(errors="replace")[-5000:] if spr.exists() else "NO SPR"
        raise RuntimeError(f"QA original-engine diagnostic failed {label} exit {p.returncode} / {tail}")
    entries=[]
    for line in p.stdout.splitlines():
        if "QA_SED_MASS" not in line:continue
        line=line[line.index("QA_SED_MASS"):]
        ss=line.split()
        assert ss[0]=="QA_SED_MASS" and len(ss)==7,line
        _,*parts=ss
        t,bef,source,after,boundary,res=map(float,parts)
        entries.append({"t_hr":t,"before_m3_solid":bef,"new_erosion_m3_solid":source,
                        "after_m3_solid":after,"signed_boundary_m3_solid":boundary,
                        "residual_m3_solid":res})
    assert entries,"No diagnostic records - verify FORTRAN patch compiled into executable"
    import math
    assert all(all(math.isfinite(float(x)) for x in e.values()) for e in entries)
    arr=[x["residual_m3_solid"] for x in entries]
    b=max(abs(x["before_m3_solid"]) for x in entries)
    total_added=sum(x["new_erosion_m3_solid"] for x in entries)
    total_border=sum(x["signed_boundary_m3_solid"] for x in entries)
    initial=entries[0]["before_m3_solid"]
    final=entries[-1]["after_m3_solid"]
    total_mass_res=final-initial-total_added+total_border
    sum_abs=sum(abs(v) for v in arr)
    max_abs=max(abs(v) for v in arr)
    denom=max(abs(total_added),1e-12)
    outcome={"test":label,"grid_m":grid,"engine":"SHETRAN original physics+diagnostic WRITE statements only",
             "n_steps":len(entries),"initial_solid_m3":initial,
             "final_solid_m3":final,"new_soil_erosion_solid_m3":total_added,
             "boundary_net_outflow_solid_m3":total_border,
             "max_step_residual_m3":max_abs,"sum_abs_residual_m3":sum_abs,
             "total_residual_m3":total_mass_res,
             "mass_relative_to_detachment":abs(total_mass_res)/denom,
             "mass_conservation_criterion_pass":max_abs<1e-7*max(1,b) and abs(total_mass_res)/denom<1e-3}
    (d/"mass_ledger.json").write_text(json.dumps(outcome,indent=2))
    (d/"mass_steps.json").write_text(json.dumps(entries,indent=2))
    print("QA_NATIVE_SEDIMENT_LEDGER "+json.dumps(outcome),flush=True)
    assert outcome["mass_conservation_criterion_pass"],outcome
    return outcome

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--original-model",type=Path,required=True)
    ap.add_argument("--exe",type=Path,required=True)
    ap.add_argument("--workdir",type=Path,required=True)
    ap.add_argument("--grid-m",type=float,default=4.0)
    args=ap.parse_args();args.workdir.mkdir(parents=True,exist_ok=True)
    o=run(args.exe,args.original_model,args.workdir,"on",True,args.grid_m)
    p=run(args.exe,args.original_model,args.workdir,"off",False,args.grid_m)
    (args.workdir/"pair_summary.json").write_text(json.dumps({"on":o,"off":p},indent=2))

if __name__=="__main__":main()
