#!/usr/bin/env python3
"""Aggregate verified 5 completed original-physics SHETRAN native rain batches.
Save data tables and maps. ALL spatial data here are SYNTHETIC not Gounsa DEM.
"""
from pathlib import Path
import argparse,csv,json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import SymLogNorm
VEGS=("bare","grass","oak_sparse","mixed")
SHORT={"bare":"Bare soil","grass":"Miscanthus","oak_sparse":"Sparse oak resprouts","mixed":"Mixed oak + grass patches"}
ROWS=(10,20,30,40,50)

def load(root):
    cases={}; grids={}
    for p in sorted(root.rglob("intensity_summary.json")):
        z=json.loads(p.read_text())
        rain=z["rain_mm_h"]
        assert rain in ROWS
        assert z["n_native_cases"]==7
        for d in z["runs"]:
            key=(rain,d["type"],d["canopy_on"])
            assert key not in cases,key
            cases[key]=d
        for file in p.parent.rglob("cells.csv"):
            data=list(csv.DictReader(file.open()))
            assert len(data)==405
            case=file.parent.name
            for veg in VEGS:
                for on in (True,False):
                    if case==f"{veg}_{rain}mmph_{'on' if on else 'off'}":
                        key=(rain,veg,on)
                        assert key not in grids
                        grids[key]=data
    assert len(cases)==35 and len(grids)==35,(len(cases),len(grids))
    return cases,grids

def raster(grid,field):
    arr=np.full((29,17),np.nan)
    for d in grid:
        x=int(d["x"]);y=int(d["y"])
        arr[29-y,x-1]=float(d[field])
    assert np.isfinite(arr).sum()==405
    return arr

def plot_event_maps(cases,grids,out,rain):
    fig,axes=plt.subplots(2,4,figsize=(17,11),sharex=True,sharey=True)
    all_arr=[raster(grids[(rain,v,True)],"delta_z_mm") for v in VEGS]
    vmax=max(np.nanmax(abs(x)) for x in all_arr)
    # asinh/symmetric log plot resolves erosion (-mm) even with 400mm boundary pile.
    norm=SymLogNorm(linthresh=0.03,linscale=1,vmin=-vmax,vmax=vmax,base=10)
    for i,v in enumerate(VEGS):
        z=all_arr[i]
        im=axes[0,i].imshow(z,origin="upper",norm=norm,cmap="RdBu_r",interpolation="nearest")
        axes[0,i].set_title(f"{SHORT[v]} | canopy ON")
        axes[1,i].imshow(raster(grids[(rain,v,True)],"substrate_eroded_mm"),
                           origin="upper",cmap="magma",interpolation="nearest",
                           vmin=0,vmax=max(np.nanmax(raster(grids[(rain,v,True)],"substrate_eroded_mm")) for v in VEGS))
        axes[1,i].set_title(f"{SHORT[v]} | gross original erosion")
        axes[1,i].set_xlabel("4 m grid column")
    axes[0,0].set_ylabel("Grid row (N–S)")
    axes[1,0].set_ylabel("Grid row (N–S)")
    fig.colorbar(im,ax=axes[0,:].tolist(),fraction=.014,pad=.025,label="Event-end net surface elevation Δz (mm), signed symlog")
    # Common colorbar for gross erosion with same norm
    sm=axes[1,0].images[-1]
    fig.colorbar(sm,ax=axes[1,:].tolist(),fraction=.014,pad=.025,label="Original soil erosion thickness (mm)")
    fig.suptitle(f"Original SHETRAN, synthetic closed 0.648 ha slope — {rain} mm/h × 3 hours\nNot measured Gounsa terrain, high deposition at blocked slope toe")
    fig.savefig(out/f"synthetic_{rain:02d}mmh_4covers_netZ_erosion.png",dpi=165,bbox_inches="tight")
    plt.close(fig)

def plot_canopy_effect(grids,out,rain):
    fig,axes=plt.subplots(1,3,figsize=(13,6),sharex=True,sharey=True)
    vv=("grass","oak_sparse","mixed")
    arrs=[raster(grids[(rain,v,True)],"delta_z_mm")-raster(grids[(rain,v,False)],"delta_z_mm") for v in vv]
    vmax=max(np.nanmax(abs(x)) for x in arrs)
    for i,v in enumerate(vv):
        im=axes[i].imshow(arrs[i],origin="upper",cmap="RdBu_r",
              norm=SymLogNorm(linthresh=.004,vmin=-vmax,vmax=vmax,base=10))
        axes[i].set_title(f"{SHORT[v]} (ON − OFF)")
        axes[i].set_xlabel("4m grid column")
    axes[0].set_ylabel("grid row")
    fig.colorbar(im,ax=axes.tolist(),fraction=.022,pad=.025,label="Canopy-only change in event-end Δz (mm)")
    fig.suptitle(f"Synthetic original SHETRAN canopy interception ON − OFF | {rain} mm/h × 3 h\nSame ground-protection FCG; no within-storm DEM re-routing")
    fig.savefig(out/f"synthetic_{rain:02d}mmh_canopy_ON_minus_OFF.png",dpi=165,bbox_inches="tight")
    plt.close(fig)

def plot_lines(cases,out):
    fig,ax=plt.subplots(figsize=(9,5))
    for veg in VEGS:
        y=[cases[(r,veg,True)]["source_detachment_solid_m3"] for r in ROWS]
        ax.plot(ROWS,y,marker="o",label=SHORT[veg])
    ax.set(xlabel="Rainfall intensity (mm/h, 3 h)",ylabel="New soil detachment to sediment (m³ solid)",
           title="SHETRAN native source detachment, synthetic 0.648 ha closed hillslope")
    ax.legend();ax.grid(alpha=.3);fig.savefig(out/"gross_original_soil_supply_by_rainfall.png",dpi=170,bbox_inches="tight");plt.close(fig)
    fig,ax=plt.subplots(figsize=(9,5))
    b=np.array([cases[(r,"bare",True)]["source_detachment_solid_m3"] for r in ROWS])
    for veg in VEGS[1:]:
        y=np.array([cases[(r,veg,True)]["source_detachment_solid_m3"] for r in ROWS])
        ax.plot(ROWS,100*(1-y/b),marker="o",label=SHORT[veg])
    ax.set(xlabel="Rainfall intensity (mm/h, 3 h)",ylabel="Soil detachment reduction versus bare soil (%)",
           title="Relative reduction; hypothetical vegetation inputs, not measured effect")
    ax.legend();ax.grid(alpha=.3);fig.savefig(out/"reduction_vs_bare_pct.png",dpi=170,bbox_inches="tight");plt.close(fig)

def main():
    p=argparse.ArgumentParser();p.add_argument("--artifacts",type=Path,required=True);p.add_argument("--out",type=Path,required=True)
    q=p.parse_args();q.out.mkdir(parents=True,exist_ok=True)
    cases,grids=load(q.artifacts)
    summary=[]
    for rain in ROWS:
        bare=cases[(rain,"bare",True)]["source_detachment_solid_m3"]
        for veg in VEGS:
            for on in ([True] if veg=="bare" else [True,False]):
                d=cases[(rain,veg,on)]
                row={"rain_mm_h":rain,"cover":veg,"canopy_on":on,
                  "soil_detachment_solid_m3":d["source_detachment_solid_m3"],
                  "reduction_pct_vs_bare":100*(1-d["source_detachment_solid_m3"]/bare),
                  "net_elevation_gain_cells":d["net_elevation_gain_cells"],
                  "max_net_deposit_mm":d["max_net_deposition_mm"],
                  "max_net_erosion_mm":d["max_net_erosion_mm"],
                  "native_mass_error":d["relative_sediment_mass_error"]}
                summary.append(row)
        plot_event_maps(cases,grids,q.out,rain)
        plot_canopy_effect(grids,q.out,rain)
    plot_lines(cases,q.out)
    with (q.out/"all_35_verified_native_matrix.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(summary[0]));w.writeheader();w.writerows(summary)
    max_resid=max(x["native_mass_error"] for x in summary)
    outcome={"n_native_runs":len(summary),"all_artifacts_loaded":True,"max_relative_sediment_budget_residual":max_resid,
      "maps":["synthetic_10mmh_4covers_netZ_erosion.png","synthetic_50mmh_4covers_netZ_erosion.png"],
      "limitations":["Synthetic topography and vegetation","Closed outlet artificially piles sediment",
        "12h simulation, 3h storm","DEM not feedback during storm","2m/1m spatial convergence not verified"]}
    (q.out/"postprocess_QA.json").write_text(json.dumps(outcome,indent=2))
    print("QA_AGGREGATE_MAPS "+json.dumps(outcome),flush=True)
if __name__=="__main__":main()
