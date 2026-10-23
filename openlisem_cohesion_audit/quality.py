"""Read only native LISEM outputs; report mass balances and max concentration."""
from pathlib import Path
import csv
import numpy as np
import rasterio
ROOT=Path(__file__).resolve().parent
rows=[]
for folder in sorted((ROOT/"results").glob("*")):
    fn=folder/"totals.csv"
    if not fn.exists():continue
    data={}
    for line in fn.read_text(encoding="utf-8-sig",errors="replace").splitlines():
        cells=next(csv.reader([line]))
        if len(cells)<2:continue
        try:data[cells[0].strip()]=float(cells[1])
        except ValueError:continue
    key=lambda x:data.get(x,float("nan"))
    with rasterio.open(folder/"soilloss.map") as f:
        layer=f.read(1,masked=True).compressed()
    hydro=folder/"hydrograph_1.csv"
    with hydro.open(encoding="utf8",errors="replace") as inp:
        lines=list(csv.reader(inp))[3:]
    sample=[(float(x[2]),float(x[6])) for x in lines if len(x)>=7]
    active=[(q,c) for q,c in sample if q>.01]
    share=sum(c>=847.99 for q,c in active)/max(len(active),1)
    volshare=sum(q for q,c in active if c>=847.99)/max(sum(q for q,c in active),1e-12)
    loss=key("Total soil loss (ton):")
    out=key("Total outflow (overland+channel) (mm):")
    water=key("Total Precipitation (mm):")-key("Total interception(mm):")-key("Total infiltration (mm):")-out-key("Surface storage (mm):")-key("Water in overland flow (mm):")-key("Water in flood (mm):")-key("Water in channels (mm):")
    sediment=key("Flow detachment (land) (ton):")+key("Splash detachment (land) (ton):")+key("Deposition (land) (ton):")-loss-key("Sediment (land) (ton):")
    row={"case":folder.name,"area_m2":key("Catchment area (m2):"),"rain_mm":key("Total Precipitation (mm):"),"out_mm":out,"soil_loss_kg_ha":key("Average soil loss (kg/ha):"),"flow_detach_t":key("Flow detachment (land) (ton):"),"deposition_t":key("Deposition (land) (ton):"),"max_cell_t_ha":float(layer.max()),"max_conc_g_l":max(c for q,c in sample),"cap_active_fraction":share,"cap_discharge_fraction":volshare,"water_balance_mm":water,"sed_balance_t":sediment}
    rows.append(row)
    print("QA",folder.name, "Q mm",round(out,5), "soil-loss kg/ha",round(row["soil_loss_kg_ha"],3),"cap-frac",round(share,3),"closure",round(water,7))
if not rows:raise RuntimeError("No complete OpenLISEM simulations")
with (ROOT/"quality.csv").open("w",encoding="utf-8-sig",newline="") as fp:
    writer=csv.DictWriter(fp,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
