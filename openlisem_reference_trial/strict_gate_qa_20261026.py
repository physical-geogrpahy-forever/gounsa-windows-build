"""Read ONLY original full-model totals.csv and soilloss.map outputs.
No substitute erosion computation. Conservative Gounsa GO/NO-GO numerical diagnostics.
"""
import csv, math
from pathlib import Path
import numpy as np
import rasterio

ROOT=Path(__file__).resolve().parent
results=ROOT/"results"
labels=[f"GATE_{s}_{v}_dt{d}" for s in ("Oak","Miscanthus") for v in ("default","alt_native") for d in (2,5,10,20)]
rows=[]
for label in labels:
    row={"case":label,"status":"MISSING"}
    folder=results/label
    path=folder/"totals.csv"
    if not path.exists():
        rows.append(row)
        print("GATE_NO_OUTPUT",label)
        continue
    vals={}
    for line in path.read_text(encoding="utf-8-sig",errors="replace").splitlines():
        try:
            x=next(csv.reader([line]))
            if len(x)>1:vals[x[0].strip()]=float(x[1])
        except (ValueError,IndexError,csv.Error):pass
    def val(k):
        return vals.get(k,float("nan"))
    vegetation, scheme, ds=label[len("GATE_"):].rsplit("_",2) if False else (None,None,None)
    # Labels have only single-token vegetation and two-token alt_native names.
    vlabel=label[len("GATE_"):]
    vegetation="Oak" if vlabel.startswith("Oak_") else "Miscanthus"
    scheme="alt_native" if "_alt_native_" in vlabel else "default"
    dt=int(vlabel.rsplit("dt",1)[-1])
    row.update(vegetation=vegetation,scheme=scheme,dt_s=dt,status="READ",
               precip_mm=val("Total Precipitation (mm):"),
               interception_mm=val("Total interception(mm):"),
               infiltration_mm=val("Total infiltration (mm):"),
               water_boundary_mm=val("Water across boundary (mm):"),
               total_outflow_mm=val("Total outflow (overland+channel) (mm):"),
               sediment_export_t=val("Total soil loss (ton):"),
               export_kg_ha=val("Average soil loss (kg/ha):"),
               gross_detachment_t=val("Flow detachment (land) (ton):"),
               gross_splash_t=val("Splash detachment (land) (ton):"),
               gross_deposition_t=val("Deposition (land) (ton):"),
               sediment_residual_t=float("nan"),
               max_erosion_t_ha=float("nan"),
               soil_stock_limit_t_ha=3375.0)
    row["sediment_residual_t"]=(
        row["gross_detachment_t"] + row["gross_splash_t"]+
        row["gross_deposition_t"]-row["sediment_export_t"]-val("Sediment (land) (ton):"))
    soilmap=folder/"soilloss.map"
    if soilmap.exists():
        with rasterio.open(soilmap) as ds:
            arr=ds.read(1,masked=True).compressed()
        if len(arr):
            row["max_erosion_t_ha"]=float(np.max(arr))
    row["nonzero_boundary_water"]=(math.isfinite(row["water_boundary_mm"]) and row["water_boundary_mm"]>0.05)
    row["finite_soil_column"]=(math.isfinite(row["max_erosion_t_ha"]) and row["max_erosion_t_ha"]<=3375.0)
    row["rain_consistent"]=(math.isfinite(row["precip_mm"]) and abs(row["precip_mm"]-20.)<0.05)
    row["outlet_sediment_finite"]=(math.isfinite(row["sediment_export_t"]) and row["sediment_export_t"]>=0)
    rows.append(row)
    print("NATIVE_GATE_CASE",label,"rain",row["precip_mm"],"boundarywater",row["water_boundary_mm"],
          "export kg/ha",row["export_kg_ha"],"max erosion t/ha",row["max_erosion_t_ha"],
          "rain ok",row["rain_consistent"],"outletwater ok",row["nonzero_boundary_water"],
          "finite stock",row["finite_soil_column"])
for vegetation in ("Oak","Miscanthus"):
    for scheme in ("default","alt_native"):
        grp=sorted([r for r in rows if r.get("vegetation")==vegetation and r.get("scheme")==scheme],key=lambda r:r["dt_s"])
        if len(grp)!=4:continue
        pair=[]
        for a,b in zip(grp,grp[1:]):
            out_a,out_b=a["export_kg_ha"],b["export_kg_ha"]
            if all(math.isfinite(x) for x in (out_a,out_b)) and max(abs(out_a),abs(out_b))>1e-6:
                rel=abs(out_a-out_b)/max(abs(out_a),abs(out_b))
            else:rel=float("nan")
            pair.append((a["dt_s"],b["dt_s"],rel))
        # Native export numerical convergence is evaluated on the *finest*
        # interval 2 vs 5s; not exactly a halving pair, hence preliminary.
        pass_case=all(r.get("nonzero_boundary_water") and r.get("rain_consistent") and
                      r.get("finite_soil_column") and r.get("outlet_sediment_finite") for r in grp)
        print("NATIVE_GATE_SERIES",vegetation,scheme,
              "dt2-5-10-20",[(r["dt_s"],r["export_kg_ha"]) for r in grp],
              "adjacent_relative_differences",pair,
              "basic_checks",pass_case,
              "conclusion","NO_GO_OR_INCONCLUSIVE" if not pass_case else "REQUIRE_DT_REFINEMENT_AND_SED_LEDGER")
allkeys=list(dict.fromkeys(k for r in rows for k in r))
with (ROOT/"strict_gate_qa_20261026.csv").open("w",encoding="utf-8-sig",newline="") as out:
    writer=csv.DictWriter(out,fieldnames=allkeys)
    writer.writeheader();writer.writerows(rows)
print("NATIVE_GATE_QA_RESULTS_FILE",ROOT/"strict_gate_qa_20261026.csv")
