#!/usr/bin/env python3
"""Independent native SHETRAN diagnostic timestep refinement, 4m fixed domain.
Native model physics untouched, diagnostic-only SYMAIN WRITE added in workflow.
These are SYNTHETIC closed-boundary tests, NOT Gounsa validation.
"""
import argparse, json, re, subprocess, math
from pathlib import Path
import numpy as np
from shetran_mixed_canopy_native_20261027 import prepare,extract

def run_one(source,exe,out,tmax,on):
    prepare(source,out,canopy_on=on,grid_m=4.,warmup_hr=1)
    frd=out/"input_cob_frd.txt";lines=frd.read_text().splitlines(keepends=True)
    loc=[i for i,v in enumerate(lines[:-1]) if v.strip()=="BASIC TIMESTEP DATA"]
    assert len(loc)==1,loc
    i=loc[0]+1
    # FRmod: READ(FRD,'(4F7.0,L7)') PMAX,PALFA,QMAX,TMAX,BSOFT.
    # Prior QA was WRONG: modified first field PMAX rather than fourth TMAX.
    assert abs(float(lines[i][:7])-1.0)<1e-6,lines[i]
    assert abs(float(lines[i][21:28])-1.0)<1e-6,lines[i]
    assert lines[i][28:35].strip()=="T",lines[i]
    fmt=(f"{tmax:.6f}"[1:] if tmax<1.0 else f"{tmax:.5f}")
    assert len(fmt)<=7,fmt
    lines[i]=lines[i][:21]+fmt.rjust(7)+lines[i][28:]
    assert abs(float(lines[i][21:28])-tmax)<1e-10,lines[i]
    assert abs(float(lines[i][:7])-1.0)<1e-10,lines[i]
    # Disable the first-102-steps soft-start in convergence QA, so varying
    # TMAX does not also change warmup due to the NSTEP-indexed BSOFT rule.
    lines[i]=lines[i][:28]+"      F"+lines[i][35:]
    frd.write_text("".join(lines))
    p=subprocess.run([str(exe.resolve()),"-f","rundata_cob.txt"],cwd=out,
        capture_output=True,text=True,timeout=180)
    (out/"native_log.txt").write_text(p.stdout+"\nSTDERR\n"+p.stderr)
    assert p.returncode==0,{"tmax":tmax,"on":on,"stdout_tail":p.stdout[-1200:],"stderr":p.stderr[-1000:]}
    entries=[]
    for line in p.stdout.splitlines():
        ix=line.find("QA_SED_MASS")
        if ix<0:continue
        tok=line[ix:].split()
        assert len(tok)==7,tok
        entries.append(list(map(float,tok[1:])))
    assert entries, "No native Fortran QA instrumented records"
    row=np.asarray(entries)
    t,prior,supply,following,bound,residual=row.T
    total_supply=float(np.sum(supply));net_b=float(np.sum(bound))
    total_res=float(following[-1]-prior[0]-total_supply+net_b)
    d=extract(out/"output_cob_shegraph.h5")
    depth=np.where(d["mask"],d["loose"][:,:,-1],np.nan)
    output={"tmax_hr":tmax,"on":on,"steps":len(entries),
          "original_source_solid_m3":total_supply,
          "boundary_solid_m3":net_b,"native_mass_residual_m3":total_res,
          "native_mass_relative_to_source":abs(total_res)/max(abs(total_supply),1e-12),
          "mean_final_DLS_active_mm":float(np.nanmean(depth)),
          "peak_snapshot_original_soil_erosion_mm_day":d["peak_erosion_mm_day"]}
    np.save(out/"dls_final.npy",depth)
    (out/"qa_dt.json").write_text(json.dumps(output,indent=2))
    print("QA_DT_CASE "+json.dumps(output),flush=True)
    assert np.isfinite(depth[d["mask"]]).all()
    assert output["native_mass_relative_to_source"]<1e-3,output
    return output,depth,d["mask"]

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--exe",type=Path,required=True)
    a.add_argument("--original-model",type=Path,required=True)
    a.add_argument("--out",type=Path,required=True)
    v=a.parse_args();v.out.mkdir(parents=True,exist_ok=True)
    results=[];arr={};mask0=None
    for t in (1.0,0.5,0.25,0.125):
        for on in (True,False):
            folder=v.out/(f"tmax_{t:g}_"+("on" if on else "off"))
            row,depth,mask=run_one(v.original_model,v.exe,folder,t,on)
            results.append(row);arr[(t,on)]=depth
            if mask0 is None:mask0=mask
            else:assert np.array_equal(mask0,mask)
    fine={o["on"]:o for o in results if o["tmax_hr"]==.125}
    comparisons=[]
    for t in (1.0,.5,.25):
        for on in (True,False):
            r=next(o for o in results if o["tmax_hr"]==t and o["on"]==on)
            q=fine[on];f=arr[(t,on)][mask0]-arr[(.125,on)][mask0]
            comparisons.append({"tmax_hr":t,"on":on,
              "relative_total_detachment_discrepancy":abs(r["original_source_solid_m3"]-q["original_source_solid_m3"])/max(abs(q["original_source_solid_m3"]),1e-12),
              "max_final_DLS_discrepancy_mm":float(np.max(np.abs(f))),
              "rms_final_DLS_discrepancy_mm":float(np.sqrt(np.mean(f*f)))})
    report={"physical_engine":"native SHETRAN with diagnostic WRITE only",
            "comparisons_reference_tmax_hr":.125,"same_4m_0.2816ha_land_grid":True,
            "open_outlet":False,"spatial_dx_convergence_tested":False,
            "results":results,"comparisons":comparisons}
    (v.out/"timestep_convergence.json").write_text(json.dumps(report,indent=2))
    print("QA_DT_FINAL "+json.dumps({"comparisons":comparisons},indent=2),flush=True)
if __name__=="__main__":main()
