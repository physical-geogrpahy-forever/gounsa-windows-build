#!/usr/bin/env python3
"""Render SHETRAN original-physics native 405-cell outputs already produced.
Reads GitHub Actions archived actual output CSV; NO new physical calculations.
Maps are SYNTHETIC, NOT GEOREFERENCED Gounsa locations.
"""
import argparse,csv,json,math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def load_table(root):
    z=list(root.rglob("summary_matrix.csv"))
    assert len(z)==1,z
    with z[0].open(newline="") as f:
        records=list(csv.DictReader(f))
    assert len(records)==35,len(records)
    for o in records:
        for k in ("rain_mm_h","source_detachment_solid_m3"):
            o[k]=float(o[k])
    return records

def load_cells(root,typ,rate,on):
    name=f"{typ}_{rate}mmph_"+("on" if on else "off")
    paths=[p for p in root.rglob("cells.csv") if p.parent.name==name]
    assert len(paths)==1,(name,paths)
    a=np.full((29,17),np.nan)
    species=np.full((29,17),np.nan)
    with paths[0].open(newline="") as f:
        rows=list(csv.DictReader(f))
    assert len(rows)==405,(name,len(rows))
    for p in rows:
        x,y=int(p["x"]),int(p["y"])
        a[29-y,x-1]=float(p["delta_z_mm"])
        species[29-y,x-1]=int(p["species"])
    return a,species

def one_map(a,title,path,clamp):
    fig,ax=plt.subplots(figsize=(7,8),dpi=170)
    cm=plt.get_cmap("RdBu").copy();cm.set_bad("0.88")
    im=ax.imshow(a,cmap=cm,vmin=-clamp,vmax=clamp,interpolation="nearest")
    fig.colorbar(im,ax=ax,label="Event-end net elevation change (mm)")
    ax.set(xlabel="Synthetic 4-m grid column",ylabel="Synthetic 4-m grid row",title=title)
    ax.text(0.5,-.10,
      f"Closed boundary; display clipped +/-{clamp:g} mm; true min {np.nanmin(a):.3f}, max {np.nanmax(a):.3f} mm",
      transform=ax.transAxes,ha="center",fontsize=8)
    ax.text(.5,-.15,"Hypothetical DEM and vegetation. NOT observed or predicted Gounsa deposition.",
         transform=ax.transAxes,ha="center",fontsize=8)
    fig.tight_layout();fig.savefig(path,bbox_inches="tight");plt.close(fig)

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--input",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True);a=ap.parse_args()
    a.output.mkdir(parents=True,exist_ok=True)
    cases=("bare","grass","oak_sparse","mixed")
    labels={"bare":"Bare soil","grass":"Miscanthus cover","oak_sparse":"Sparse oak resprouts","mixed":"Patchy oak + Miscanthus"}
    for rate in (10,30,50):
        for case in cases:
            grid,sp=load_cells(a.input,case,rate,True)
            one_map(grid,f"SHETRAN synthetic {rate} mm/h: {labels[case]}",
                    a.output/f"{rate}mmh_{case}_net_z_ON.png",2 if rate==10 else 10)
        z,sp=load_cells(a.input,"mixed",rate,True)
        q,_=load_cells(a.input,"mixed",rate,False)
        one_map(z-q,f"SHETRAN synthetic {rate} mm/h: mixed canopy ON minus OFF",
                a.output/f"{rate}mmh_mixed_canopy_ON_minus_OFF.png",
                max(0.5,math.ceil(np.nanmax(np.abs(z-q)))))
    # Plot the synthetic vegetation 405-cell case on separate figure.
    _,k=load_cells(a.input,"mixed",30,True)
    fig,ax=plt.subplots(figsize=(7,8),dpi=160)
    plot=np.full_like(k,np.nan)
    plot[k==3]=0;plot[k==2]=1;plot[k==1]=2
    cm=ListedColormap(["#d6c4a8","#9ab66c","#356a40"]);cm.set_bad("#f2f2f2")
    ax.imshow(plot,cmap=cm,interpolation="nearest",vmin=-.5,vmax=2.5)
    ax.set(title="Synthetic patches: 75 bare, 228 Miscanthus, 102 oak",
       xlabel="Synthetic 4m grid column",ylabel="Synthetic 4m grid row")
    ax.text(.5,-.09,"not mapped Gounsa vegetation",transform=ax.transAxes,ha="center")
    fig.tight_layout();fig.savefig(a.output/"mixed_vegetation_patch_layout.png",bbox_inches="tight");plt.close(fig)
    # Aggregate original soil source vs storm intensity.
    rows=load_table(a.input)
    fig,ax=plt.subplots(figsize=(8.6,5.5),dpi=170)
    for case in cases:
        rr=sorted((x for x in rows if x["type"]==case and x["canopy_on"]=="True"),
                  key=lambda x:x["rain_mm_h"])
        assert len(rr)==5,(case,len(rr))
        ax.plot([x["rain_mm_h"] for x in rr],
            [x["source_detachment_solid_m3"] for x in rr],marker="o",label=labels[case])
    ax.set(title="Original SHETRAN synthetic 0.648ha: original-soil detachment supply",
        xlabel="Rain intensity (mm/h), 3h each",ylabel="New sediment source (m3 solid)")
    ax.grid(alpha=.2);ax.legend()
    fig.tight_layout();fig.savefig(a.output/"rain_10to50_original_soil_source.png");plt.close(fig)
    pngs=sorted(p.name for p in a.output.glob("*.png"))
    assert len(pngs)==17,(len(pngs),pngs)
    (a.output/"README_rendered_maps.json").write_text(json.dumps({
       "n_figures":len(pngs),"figures":pngs,
       "all_real_native_case_outputs_used":True,
       "synthetic":True,"closed_boundaries":True,
       "interpretation_note":"Large positive local change at intense rainfall occurs with no outlet; maps are NOT field-predictive."},indent=2))
    print("QA_NATIVE_MAPS "+json.dumps({"n":len(pngs),"files":pngs}),flush=True)
if __name__=="__main__":main()
