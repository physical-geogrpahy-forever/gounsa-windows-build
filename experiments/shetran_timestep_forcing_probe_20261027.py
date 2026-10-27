#!/usr/bin/env python3
"""Diagnostic native precipitation integration under different SHETRAN TMAX.
Checks whether prior nonconvergent sediment reflects unequal storm totals.
"""
from pathlib import Path
from collections import defaultdict
import subprocess,argparse,json,math
from shetran_mixed_canopy_native_20261027 import prepare
def run_case(exe,src,out,tmax,on):
    prepare(src,out,canopy_on=on,grid_m=4.,warmup_hr=1)
    p=out/"input_cob_frd.txt";lines=p.read_text().splitlines(keepends=True)
    i=next(i for i,s in enumerate(lines) if s.strip()=="BASIC TIMESTEP DATA")+1
    lines[i]=f"{tmax:7.5f}"+lines[i][7:];p.write_text("".join(lines))
    process=subprocess.run([str(exe.resolve()),"-f","rundata_cob.txt"],
                           cwd=out,capture_output=True,text=True,timeout=150)
    (out/"original_ET_diagnostics_stdout.txt").write_text("NATIVE ET DIAGNOSTICS LAST 15000 CHARS ONLY\\n"+process.stdout[-15000:]+"\\nSTDERR\\n"+process.stderr[-2000:])
    if process.returncode:raise RuntimeError(process.stdout[-2000:])
    q=defaultdict(lambda:{"p":0.,"net":0.,"e":0.,"ds":0.,"n":0,"otherET":0.})
    for line in process.stdout.splitlines():
        ix=line.find("QA_CANOPY")
        if ix<0:continue
        toks=line[ix:].split()
        assert len(toks)==12,toks
        elt=int(toks[1])
        t,dt,p,c0,c1,net,e,root,soil,other=map(float,toks[2:])
        assert dt>0 and all(math.isfinite(a) for a in [dt,p,c0,c1,net,e,root,soil,other])
        z=q[elt];z["p"]+=p*dt*1000.;z["net"]+=net*dt*1000.
        z["e"]+=e*dt*1000.;z["ds"]+=c1-c0;z["n"]+=1
        z["otherET"]+=(root+soil+other)*dt*1000.
    assert len(q)==176
    vals=list(q.values());rain=[v["p"] for v in vals]
    canopy_bal=max(abs(v["p"]-v["net"]-v["e"]-v["ds"]) for v in vals)
    result={"on":on,"TMAX_hr":tmax,"n_cells":len(q),
            "native_steps_per_cell":vals[0]["n"],
            "rain_min_mm":min(rain),"rain_max_mm":max(rain),"rain_mean_mm":sum(rain)/176,
            "max_p_integral_deviation_from_90mm":max(abs(v-90.) for v in rain),
            "ground_net_mean_mm":sum(v["net"] for v in vals)/176,
            "final_canopy_storage_mean_mm":sum(v["ds"] for v in vals)/176,
            "maximum_cell_canopy_budget_error_mm":canopy_bal,
            "total_other_ET_mm":sum(v["otherET"] for v in vals)}
    (out/"forcing_probe.json").write_text(json.dumps(result,indent=2))
    print("QA_FORCE_TMAX "+json.dumps(result),flush=True)
    return result

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--original-model",type=Path,required=True)
    a.add_argument("--exe",type=Path,required=True)
    a.add_argument("--out",type=Path,required=True)
    args=a.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    res=[run_case(args.exe,args.original_model,args.out/(f"{t:g}_"+("ON" if on else "OFF")),t,on)
         for t in [0.125,0.03125,0.015625] for on in (True,False)]
    (args.out/"forcing_by_dt.json").write_text(json.dumps(res,indent=2))
if __name__=="__main__":main()
