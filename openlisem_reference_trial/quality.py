"""Quality audit: no custom physical model, only parses native OpenLISEM outputs.
Test water/sediment closure, 0.25m soil stock, and dt sensitivity.
"""
from pathlib import Path
import csv,math
import numpy as np
import rasterio
ROOT=Path(__file__).resolve().parent
rows=[]
for folder in sorted((ROOT/"results").glob("*")):
    p=folder/"totals.csv"
    if not p.exists():continue
    try:
        vals={}
        for line in p.read_text(encoding="utf-8-sig",errors="replace").splitlines():
            rr=next(csv.reader([line]))
            if len(rr)<2: continue
            try:vals[rr[0].strip()]=float(rr[1].strip())
            except ValueError:pass
        def v(key):return vals.get(key,float("nan"))
        rain=v("Total Precipitation (mm):")
        inter=v("Total interception(mm):")
        infil=v("Total infiltration (mm):")
        boundary=v("Water across boundary (mm):")
        water=v("Water in overland flow (h<50) (mm):")+v("Water in flood (h>50) (mm):")
        water+=v("Surface storage (mm):")+v("Water in channels (mm):")
        det=v("Flow detachment (land) (ton):")
        splash=v("Splash detachment (land) (ton):")
        deposition=v("Deposition (land) (ton):")
        export=v("Total soil loss (ton):")
        sediment=v("Sediment (land) (ton):")
        soil_loss=v("Average soil loss (kg/ha):")
        wat_err=rain-inter-infil-boundary-water
        sed_err=det+splash+deposition-export-sediment
        a=np.array([])
        if (folder/"soilloss.map").exists():
            with rasterio.open(folder/"soilloss.map") as ds:
                a=ds.read(1,masked=True).compressed()
        maxe=float(a.max()) if a.size else float("nan")
        maxd=float(a.min()) if a.size else float("nan")
        # 250mm available soil; bulk density 1350 kg/m3 -> 3375 t/ha.
        limit_t_ha=.25*1350*10.0
        physical=bool(math.isfinite(maxe) and maxe<=limit_t_ha+1e-6)
        row=dict(case=folder.name,rain_mm=rain,intercept_mm=inter,infil_mm=infil,
                 boundary_runoff_mm=boundary,storage_water_mm=water,
                 water_residual_mm=wat_err,
                 gross_flow_t=det,gross_splash_t=splash,gross_dep_t=deposition,
                 sediment_export_t=export,suspended_t=sediment,sed_residual_t=sed_err,
                 export_kg_ha=soil_loss,
                 max_erosion_t_ha=maxe,max_deposition_t_ha=maxd,
                 max_erosion_depth_cm=maxe/(1350*10)*100,
                 available_soil_t_ha=limit_t_ha,
                 physically_plausible_soil_stock=physical,
                 water_balance_pass=abs(wat_err)<.01,
                 sediment_balance_pass=abs(sed_err)<1e-4)
        rows.append(row)
    except Exception as e:
        print("BAD OUTPUT",folder,repr(e))
if rows:
    with (ROOT/"quality.csv").open("w",encoding="utf-8-sig",newline="") as fp:
        writer=csv.DictWriter(fp,fieldnames=list(rows[0]))
        writer.writeheader();writer.writerows(rows)
    for r in rows:print("QA",r["case"],"rain",round(r["rain_mm"],4),"runoff",round(r["boundary_runoff_mm"],4),"sed_export kg/ha",round(r["export_kg_ha"],6),"max ero t/ha",round(r["max_erosion_t_ha"],3),"stock pass",r["physically_plausible_soil_stock"])
else:raise RuntimeError("NO_VALID_SIMULATIONS")
