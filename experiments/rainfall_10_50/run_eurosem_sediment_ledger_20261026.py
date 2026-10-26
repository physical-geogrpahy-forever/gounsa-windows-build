#!/usr/bin/env python3
"""Read independent high-precision original F77 sediment accounting diagnostics.

The 1998 original eplanel.for ALREADY computes:
 inrlbal = sumqirr + sumdir + suspir
 rillbal = stout + sumdrl + susprl - sedin.
Observe those terms and independently integrate time-resolved outgoing Q*C.
Native comments: positive sumdir = deposition, negative = erosion.
Native sediment emitted volume m3; rho_s*1000 converts to kg.
This is NOT a new erosion model, nor certification of finite soil depth.
"""
import subprocess,sys,json,itertools,math,csv
from pathlib import Path
HERE=Path(__file__).resolve().parent
OUTPUT=HERE/"eurosem_reaudit_20261026"
OUTPUT.mkdir(exist_ok=True)
series=[]
for rain,dt,rills,code in itertools.product((30,50),(1.0,.5,.25),(False,True),(0,1)):
    tag=f"ledger_R{rain}_dt{str(dt).replace('.','p')}_rills{int(rills)}_mcode{code}"
    cmd=[sys.executable,str(HERE/"verify_eurosem_reaudit_20261026.py"),
         "--rain",str(rain),"--dt-minute",str(dt),"--tag",tag,
         "--cover",".9","--storage","1.5","--plant-height","120",
         "--erod",".9","--mcode",str(code),"--trace-sediment-ledger"]
    if rills:cmd.append("--rilled-geometry")
    try:
        run=subprocess.run(cmd,cwd=HERE,text=True,encoding="latin1",
                           stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=95)
        fp=HERE/f"eurosem_QA_{tag}_r{rain:02d}_rep1"/"qa_result.json"
        if not fp.exists():raise RuntimeError("No QA. native log "+run.stdout[-1300:])
        native=json.loads(fp.read_text())
        summaries=native.get("sediment_ledger_native_trace",[])
        steps=native.get("sediment_step_trace",[])
        if len(summaries)!=1:raise ValueError("Expected one final native ledger, got "+str(len(summaries))+" values "+repr(summaries))
        # Legacy Fortran progress display appends carriage-return spinner text to the last numerical line.
        parts=summaries[0].split()[:18]
        names=["T_s","interrill_export_m3","interrill_net_deposition_m3","interrill_suspended_m3",
               "interrill_native_balance_m3","sediment_out_total_m3","rill_net_deposition_m3",
               "rill_suspended_m3","external_sediment_in_m3","rill_native_balance_m3",
               "sediment_out_total_kg","rill_width_m","slope_length_m","slope_width_m",
               "soil_porosity","sediment_density_Mg_m3"]
        assert parts[0]=="SED_LEDGER_NATIVE"
        assert len(parts)==len(names)+2,(parts,names)
        d=dict(zip(names,[float(x.replace("D","E")) for x in parts[2:]]))
        # Independently derive the event boundary sediment export from each
        # original solver step: trapezoidal Q*C*dt*rho, **not** sedtot variable.
        integrated_m3=0.
        maximum_step_discrepancy=0.
        for line in steps:
            nums=[float(x.replace("D","E")) for x in line.split()[1:]]
            if len(nums)!=8:raise ValueError(("Bad numeric row",line))
            ts,seconds,q_now,q_prev,c_now,c_prev,rho,sedtot=nums
            integrated_m3+=.5*(q_now*c_now+q_prev*c_prev)*seconds
        if not steps:raise ValueError("No outlet time history")
        downstream_volume=d["sediment_out_total_m3"]
        calculated_balance=(d["interrill_export_m3"]+
                            d["interrill_net_deposition_m3"]+
                            d["interrill_suspended_m3"])
        if rills:
            # interrill + rill balances are separate stages; assess both
            all_balances=(d["interrill_native_balance_m3"],d["rill_native_balance_m3"])
            relevant=[d["interrill_export_m3"],d["interrill_net_deposition_m3"],
                      d["interrill_suspended_m3"],d["sediment_out_total_m3"],
                      d["rill_net_deposition_m3"],d["rill_suspended_m3"],
                      d["external_sediment_in_m3"]]
        else:
            all_balances=(d["interrill_native_balance_m3"],)
            relevant=[d["interrill_export_m3"],d["interrill_net_deposition_m3"],
                      d["interrill_suspended_m3"]]
        scale=max(1e-9,*[abs(x) for x in relevant])
        native_residual=max(abs(x) for x in all_balances)
        # Original event output uses calibrated kg conversion separately.
        self_consistency=abs(integrated_m3-downstream_volume)
        outlet_rel=self_consistency/max(1e-9,abs(integrated_m3),abs(downstream_volume))
        # Native soil thickness user input DERO=5m is not guaranteed to be finite-stock
        # physical limit under distinct erosion modules. Native max DIRNET needs
        # separate independent per-grid test, not silently count mass closure as cap.
        summary={
            "case":tag,"rain_mm_h":rain,"timestep_s":dt*60,"has_rills":rills,
            "mcode":code,"native_return_code":native.get("return_code"),
            "water_pass":native.get("water_pass"),
            "net_erosion_reported_kg":native.get("net_erosion_kg"),
            "native_ledger":d,
            "independent_outlet_m3":integrated_m3,
            "outlet_volume_delta_m3":self_consistency,
            "outlet_relative_mismatch":outlet_rel,
            "native_ledger_residual_m3":native_residual,
            "native_relative_balance_residual":native_residual/scale,
            "balance_check":bool(native_residual<=max(1e-6,0.001*scale)),
            "outlet_check":bool(outlet_rel<1e-4),
            "step_count":len(steps)}
        summary["status"]="PASS" if run.returncode==0 and summary["balance_check"] and summary["outlet_check"] else "FAIL"
        print("SEDIMENT_LEDGER",json.dumps({k:v for k,v in summary.items() if k!="native_ledger" and k!="net_erosion_reported_kg"}),flush=True)
        print("SEDIMENT_NATIVE_TERMS",tag,json.dumps(d),flush=True)
    except Exception as e:
        summary={"case":tag,"status":"ERROR","error":repr(e)}
        print("SEDIMENT_LEDGER_ERROR",tag,repr(e),flush=True)
    series.append(summary)
(OUTPUT/"sediment_ledger_results.json").write_text(json.dumps(series,indent=2,ensure_ascii=False))
keys=["case","rain_mm_h","timestep_s","has_rills","mcode","native_return_code","water_pass",
      "independent_outlet_m3","outlet_volume_delta_m3","outlet_relative_mismatch",
      "native_ledger_residual_m3","native_relative_balance_residual","balance_check",
      "outlet_check","status","step_count","error"]
with (OUTPUT/"sediment_ledger_results.csv").open("w",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=keys)
    writer.writeheader()
    for s in series:writer.writerow({k:s.get(k) for k in keys})
for rain in (30,50):
 for rills in (False,True):
  for mcode in (0,1):
   aa=sorted([x for x in series if x.get("rain_mm_h")==rain and x.get("has_rills")==rills and x.get("mcode")==mcode],key=lambda x:x["timestep_s"])
   if len(aa)==3 and all(x["status"]=="PASS" for x in aa):
    def sediment(x):return x["independent_outlet_m3"]
    fine,med,coarse=aa
    print("LEDGER_CONVERGENCE",rain,rills,mcode,[(x["timestep_s"],sediment(x)) for x in aa],
          "finest_relative_diff",abs(sediment(fine)-sediment(med))/max(abs(sediment(fine)),abs(sediment(med)),1e-12))
print("LEDGER_TOTAL",len(series),"PASS",sum(z["status"]=="PASS" for z in series),
      "ERROR",sum(z["status"]=="ERROR" for z in series))
# Preserve all original outputs for diagnosing bad balances; require no missing
# native instrumentation rather than silently claim failure/success.
if any(z["status"]=="ERROR" for z in series):raise SystemExit(2)
