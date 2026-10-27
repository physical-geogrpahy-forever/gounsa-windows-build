#!/usr/bin/env python3
"""Render synthetic SHETRAN source-native 4m grid net change/soil detachment.
NOT georeferenced Gounsa data; x/y are just local grid indices.
"""
import csv,json
from pathlib import Path
import argparse,numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def makegrid(d,field):
    a=np.full((29,17),np.nan)
    for key,v in d.items():
        x,y=map(int,key.split(","))
        a[29-y,x-1]=float(v[field])
    assert np.isfinite(a).sum()==176
    return a

def draw(a,title,path,vlim,cmap="RdBu_r"):
    fig,ax=plt.subplots(figsize=(9,8),dpi=165)
    cm=plt.get_cmap(cmap).copy();cm.set_bad("0.9")
    im=ax.imshow(a,origin="upper",interpolation="nearest",vmin=-vlim,vmax=vlim,cmap=cm)
    fig.colorbar(im,ax=ax,label="Event-end net elevation change (mm)")
    ax.set(xlabel="synthetic grid column",ylabel="synthetic grid row",title=title)
    ax.text(0.5,-.115,"Synthetic terrain and vegetation, closed slope; not Gounsa observations",
           transform=ax.transAxes,ha="center",fontsize=8)
    fig.tight_layout()
    fig.savefig(path,bbox_inches="tight");plt.close(fig)

def main():
    p=argparse.ArgumentParser();p.add_argument("--out",type=Path,required=True)
    z=p.parse_args().out
    on=json.loads((z/"on"/"net_elevation_cells.json").read_text())
    off=json.loads((z/"off"/"net_elevation_cells.json").read_text())
    assert set(on)==set(off)
    a=makegrid(on,"delta_z_event_end_mm")
    b=makegrid(off,"delta_z_event_end_mm")
    diff=a-b
    maxv=max(abs(np.nanmin(a)),abs(np.nanmax(a)),abs(np.nanmin(b)),abs(np.nanmax(b)))
    draw(a,"SHETRAN synthetic 4m: canopy ON event-end net elevation",z/"on_net_elevation.png",maxv)
    draw(b,"SHETRAN synthetic 4m: canopy OFF event-end net elevation",z/"off_net_elevation.png",maxv)
    dv=max(abs(np.nanmin(diff)),abs(np.nanmax(diff)))
    draw(diff,"SHETRAN synthetic 4m: ON minus OFF net elevation",z/"on_minus_off_net_elevation.png",dv)
    with (z/"synthetic_native_cellwise_erosion_deposition.csv").open("w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["x","y","original_soil_erosion_on_mm","original_soil_erosion_off_mm",
            "delta_mobile_layer_on_mm","delta_mobile_layer_off_mm",
            "net_elevation_on_mm","net_elevation_off_mm","net_elevation_on_minus_off_mm"])
        for key,v in sorted(on.items(),key=lambda t:tuple(map(int,t[0].split(",")))):
            x,y=map(int,key.split(","));q=off[key]
            w.writerow([x,y,v["original_substrate_erosion_mm"],q["original_substrate_erosion_mm"],
                v["delta_loose_depth_mm"],q["delta_loose_depth_mm"],
                v["delta_z_event_end_mm"],q["delta_z_event_end_mm"],
                v["delta_z_event_end_mm"]-q["delta_z_event_end_mm"]])
    print("QA_MAPS_GENERATED "+json.dumps({"png":["on_net_elevation.png",
          "off_net_elevation.png","on_minus_off_net_elevation.png"],
          "csv":"synthetic_native_cellwise_erosion_deposition.csv",
          "crs":None,"real_site_data":False}))
if __name__=="__main__":main()
