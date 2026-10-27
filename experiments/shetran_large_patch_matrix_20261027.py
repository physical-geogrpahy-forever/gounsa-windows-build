#!/usr/bin/env python3
"""Four vegetation mosaics x 10-50mm/h, original SHETRAN 4.7.2 single engine.
Synthetic 0.648ha active land inside a 0.7888ha 17x29 bounding grid, 4m cells.
Native physics unchanged; only diagnostic Fortran statements in instrumented build.
All vegetation properties are HYPOTHETICAL and must not be presented as field data.
"""
import argparse,sys,math,csv,json,re,subprocess
from pathlib import Path
from collections import defaultdict
import numpy as np
from shetran_mixed_canopy_native_20261027 import prepare,make_fixed_et_line
from shetran_plot_native_net_change_20261027 import makegrid

NX,NY=17,29
DX=4.0
AREA=DX**2
ACTIVE={(x,y) for x in range(2,17) for y in range(2,29)}
assert len(ACTIVE)==405 and len(ACTIVE)*AREA==6480
VEG_CASES=("bare","grass","oak_sparse","mixed")
RAIN_CASES=(10,20,30,40,50)

def patch_id(x,y,typ):
    if (x,y) not in ACTIVE:return 0
    if typ=="bare":return 3
    if typ=="grass":return 2
    oakcenters=((4,5,2.2),(13,7,2.5),(7,12,2.0),(13,18,2.3),(4,23,2.3),(12,26,2.0))
    oak=any((x-cx)**2+(y-cy)**2<=r*r for cx,cy,r in oakcenters)
    if typ=="oak_sparse":return 1 if oak else 3
    if typ=="mixed":
        if oak:return 1
        # connected tussock patches (deterministic, not random pixel noise).
        grass=(math.sin(x*.78)+math.cos(y*.61)+.25*math.cos((x+y)*.57))>-.83
        return 2 if grass else 3
    raise ValueError(typ)

def gridrows(typ):
    return [f"{y:7d} "+''.join(str(patch_id(x,y,typ)) for x in range(1,NX+1))+"\n"
            for y in range(NY,0,-1)]

def maskrows():
    return [f"{y:7d} "+''.join("1" if (x,y) in ACTIVE else "0" for x in range(1,NX+1))+"\n"
            for y in range(NY,0,-1)]

def swap_region(lines,start,end,new):
    i=next(i for i,row in enumerate(lines) if start in row)
    j=next(i for i,row in enumerate(lines[i+1:],i+1) if end in row)
    lines[i+1:j]=new

def modify_frd(dest,typ,tmax_hr=.015625):
    p=dest/"input_cob_frd.txt";l=p.read_text().splitlines(keepends=True)
    # Same 17x29 bounding box, 405 active cells, 4m: 0.648ha active, total 0.7888ha
    swap_region(l,"COMPUTATIONAL GRID DEFINITION","EAST TO WEST FLOW CODES",maskrows())
    e2w=[f"{y:7d} "+''.join(
        "." if (x,y) in ACTIVE and (x+1,y) in ACTIVE else "I"
        for x in range(1,NX+1))+"\n" for y in range(NY,0,-1)]
    swap_region(l,"EAST TO WEST FLOW CODES","NORTH-TO-SOUTH FLOW CODES",e2w)
    n2s=[f"{y:7d} "+''.join(
        "." if (x,y) in ACTIVE and (x,y-1) in ACTIVE else "I"
        for x in range(1,NX+1))+"\n" for y in range(NY+1,0,-1)]
    swap_region(l,"NORTH-TO-SOUTH FLOW CODES","GROUND SURFACE ELEVATION",n2s)
    elevation=[]
    for y in range(NY,0,-1):
        elevation.append(f"{y:7d}\n")
        row=[]
        for x in range(1,NX+1):
            if (x,y) not in ACTIVE:row.append(0.)
            else:
                # Sloping (about 0.18-0.30 m/m) and convergent, low-slope toe,
                # not extracted from any Gounsa DEM.
                height=200.+4.*(.18*(y-1)+.12*max(y-8,0)) + .025*(x-9)**2
                height+=.09*math.sin(x*.8+y*.3)
                row.append(round(height,2))
        for i in (0,10):
            elevation.append(''.join(f"{v:7.2f}" for v in row[i:i+10])+"\n")
    swap_region(l,"GROUND SURFACE ELEVATION","RAINFALL STATIONS",elevation)
    i=next(i for i,v in enumerate(l) if "VEGETATION GRID FOR NVC PER CELL" in v)
    assert len(l[i+1:i+30])==29
    l[i+1:i+30]=gridrows(typ)
    i=next(i for i,v in enumerate(l) if "NO. OF MET./RAINFALL STATIONS" in v)
    assert list(map(int,l[i+1].split()))==[1,5,2,1,1]
    l[i+1]=''.join(f"{v:7d}" for v in (1,5,3,1,1))+"\n"
    i=next(i for i,v in enumerate(l) if "BASIC TIMESTEP DATA" in v)+1
    assert abs(float(l[i][:7])-1.)<1e-8 and abs(float(l[i][21:28])-1.)<1e-8
    # Real 4th field TMAX, NOT PMAX, which must stay 1mm.
    tim=f"{tmax_hr:.6f}"[1:]
    assert len(tim)==7 and abs(float(tim)-tmax_hr)<1e-9
    l[i]=l[i][:21]+tim+"      F"+l[i][35:]  # BSOFT off
    p.write_text(''.join(l))

def modify_etd(dest,on):
    p=dest/"input_cob_etd.txt";ls=p.read_text().splitlines(keepends=True)
    markers=[i for i,s in enumerate(ls) if s.startswith(":ET7")]
    assert len(markers)==2,markers
    base=ls[markers[0]:markers[1]]
    bare=base.copy()
    bare[0]=":ET7 - THIRD VEGETATION TYPE synthetic bare ground\n"
    bare[2]=make_fixed_et_line(0.,.05,0.)+"\n"
    ls+=bare
    p.write_text(''.join(ls))

def modify_syd(dest,typ):
    p=dest/"input_cob_syd.txt";l=p.read_text().splitlines(keepends=True)
    i=next(i for i,z in enumerate(l) if z.strip().startswith(":SY24"))
    l.insert(i+3,"    0.0    0.003    0.00\n") # third bare species: zero canopy-drip energy
    i=next(i for i,z in enumerate(l) if z.strip().startswith(":SY41 -"))
    j=next(i for i,z in enumerate(l) if z.strip().startswith(":SY42 -"))
    # FCG is a SECOND, distinct physical factor from LAI: bare, tussock ground
    # protection and oak ground protection. Does not replace canopy LAI.
    cmap={1:3,2:2,3:1,0:0}
    cgrid=[f"{y:7d} "+''.join(str(cmap[patch_id(x,y,typ)])
          for x in range(1,NX+1))+"\n" for y in range(NY,0,-1)]
    l[i:j]=[":SY41 - NCAT spatial ground cover categories\n",
            "        3\n",":SY41c - ground protection fraction bare grass oak\n",
            "        0.0\n","        0.55\n","        0.12\n",
            ":SY41e - category per active element\n"]+cgrid
    # Initial mobile sediment layer = 10mm (tested 0–30mm previously)
    i=next(i for i,z in enumerate(l) if z.strip().startswith(":SY51c"))
    l[i+1]="        0.01\n"
    i=next(i for i,z in enumerate(l) if z.strip().startswith(":SY52e"))
    l[i+1:i+30]=[f"{y:7d} "+''.join("2" if (x,y) in ACTIVE else "0"
                          for x in range(1,NX+1))+"\n" for y in range(NY,0,-1)]
    p.write_text(''.join(l))

def setup(source,dest,typ,rain,on,dt):
    assert typ in VEG_CASES and rain in RAIN_CASES
    prepare(source,dest,canopy_on=on,grid_m=DX,mmh=rain,warmup_hr=1)
    modify_frd(dest,typ,dt)
    modify_etd(dest,on)
    modify_syd(dest,typ)
    nvc={s:sum(patch_id(x,y,typ)==s for x,y in ACTIVE) for s in (1,2,3)}
    assert sum(nvc.values())==405
    meta={"type":typ,"rain_mm_h":rain,"canopy_on":on,"n":405,
      "active_m2":6480,"extent_m2":7888,"nvc_oak":nvc[1],
      "nvc_miscanthus":nvc[2],"nvc_bare":nvc[3],
      "tmax_hr":dt,"initial_DLS_mm":10.0,
      "groundcover_category":{"bare":0.0,"miscanthus":0.55,"oak":0.12},
      "species_parameters_not_field_calibrated":True,
      "physical_engine":"upstream SHETRAN Fortran unchanged; only diagnostic outputs"}
    (dest/"scenario_metadata.json").write_text(json.dumps(meta,indent=2))
    return meta

def execute(exe,source,root,typ,rain,on,dt):
    name=f"{typ}_{rain}mmph_"+("on" if on else "off")
    dest=root/name
    m=setup(source,dest,typ,rain,on,dt)
    # No huge stdout buffers; process stream while retaining only compact QA.
    proc=subprocess.Popen([str(exe.resolve()),"-f","rundata_cob.txt"],
          cwd=dest,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
          text=True,bufsize=1,errors="replace")
    records={}
    budget=[]
    logs=[]
    for raw in proc.stdout:
        x=raw.find("QA_FINAL_CELL")
        if x>=0:
            a=raw[x:].split()
            assert len(a)==8,(name,a)
            _,sx,sy,*values=a
            vals=list(map(float,values))
            cx,cy=int(sx),int(sy)
            assert (cx,cy) in ACTIVE
            time,erode,dls,pls,area=vals
            assert all(math.isfinite(v) for v in vals)
            records[(cx,cy)]={"time_hr":time,"substrate_eroded_mm":erode*1000,
                "loose_change_mm":(dls-.01)*1000,
                "delta_z_mm":(dls-.01-erode)*1000,
                "mobile_layer_mm_final":dls*1000,"PLS":pls,"cell_area_m2":area}
        elif "QA_SED_MASS" in raw:
            t=raw[raw.index("QA_SED_MASS"):].split()
            assert len(t)==7,(name,t)
            budget.append(list(map(float,t[1:])))
        elif len(logs)<30 and any(w in raw for w in ["ERROR","Error","FATAL","Warning"]):
            logs.append(raw.strip()[:240])
    rc=proc.wait(timeout=300)
    (dest/"simulation_diagnostics.txt").write_text("\n".join(logs))
    assert rc==0,(name,rc,logs)
    assert len(records)==405,(name,"active cells",len(records))
    assert len(budget)>30,(name,"budget",len(budget))
    arr=np.asarray(budget)
    residual=(arr[-1,3]-arr[0,1]-np.sum(arr[:,2])+np.sum(arr[:,4]))
    source_vol=float(np.sum(arr[:,2]))
    relative_mass=abs(residual)/max(source_vol,1e-14)
    assert relative_mass<.001,(name,relative_mass)
    z=np.array([r["delta_z_mm"] for r in records.values()])
    ero=np.array([r["substrate_eroded_mm"] for r in records.values()])
    threshold=.001
    output={**m,"source_detachment_solid_m3":source_vol,
        "native_mass_residual_m3":float(residual),
        "relative_sediment_mass_error":float(relative_mass),
        "n_native_sediment_substeps":len(budget),
        "mean_original_soil_erosion_mm":float(ero.mean()),
        "max_original_soil_erosion_mm":float(ero.max()),
        "mean_net_event_z_mm":float(z.mean()),
        "net_elevation_gain_cells":int((z>threshold).sum()),
        "net_elevation_loss_cells":int((z< -threshold).sum()),
        "max_net_deposition_mm":float(z.max()),
        "max_net_erosion_mm":float(z.min()),
        "avg_mobile_layer_mm_final":float(np.mean([r["mobile_layer_mm_final"] for r in records.values()])),
        "closed_boundary_no_outlet":True,
        "simulated_true_surface_z_feedback":False,
        "test_completed":True}
    (dest/"summary.json").write_text(json.dumps(output,indent=2))
    with (dest/"cells.csv").open("w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["x","y","species","substrate_eroded_mm","loose_change_mm","delta_z_mm","mobile_layer_mm_final"])
        for (x,y),r in sorted(records.items()):
            w.writerow([x,y,patch_id(x,y,typ),r["substrate_eroded_mm"],
                        r["loose_change_mm"],r["delta_z_mm"],r["mobile_layer_mm_final"]])
    print("QA_LARGE_PATCH_CASE "+json.dumps(output),flush=True)
    return output,records

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--original-model",type=Path,required=True)
    p.add_argument("--exe",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--tmax-hr",type=float,default=.015625)
    p.add_argument("--one-case",nargs=3,metavar=("VEGETATION","RAINFALL","CANOPY"),help="smoke case then exit")
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    if a.one_case:
        typ,rain,canopy=a.one_case
        execute(a.exe,a.original_model,a.out,typ,int(rain),canopy=="on",a.tmax_hr)
        return
    out=[];cache={}
    for intensity in RAIN_CASES:
        for typ in VEG_CASES:
            for on in ([True] if typ=="bare" else [True,False]):
                row,grid=execute(a.exe,a.original_model,a.out,typ,intensity,on,a.tmax_hr)
                out.append(row);cache[(typ,intensity,on)]=grid
    comparisons=[]
    for intensity in RAIN_CASES:
        baseline=next(r for r in out if r["type"]=="bare" and r["rain_mm_h"]==intensity)
        for typ in ("grass","oak_sparse","mixed"):
            z_on=next(r for r in out if r["type"]==typ and r["rain_mm_h"]==intensity and r["canopy_on"])
            z_off=next(r for r in out if r["type"]==typ and r["rain_mm_h"]==intensity and not r["canopy_on"])
            oncells=cache[(typ,intensity,True)]
            offcells=cache[(typ,intensity,False)]
            dz=[oncells[k]["delta_z_mm"]-offcells[k]["delta_z_mm"] for k in oncells]
            comparisons.append({"rain_mm_h":intensity,"landscape":typ,
                "bulk_erosion_source_ratio_on_vs_bare":z_on["source_detachment_solid_m3"]/max(baseline["source_detachment_solid_m3"],1e-9),
                "canopy_effect_source_solid_m3":z_on["source_detachment_solid_m3"]-z_off["source_detachment_solid_m3"],
                "canopy_effect_avg_net_z_mm":z_on["mean_net_event_z_mm"]-z_off["mean_net_event_z_mm"],
                "canopy_effect_max_abs_local_z_mm":max(abs(v) for v in dz),
                "on_positive_deposition_cells":z_on["net_elevation_gain_cells"],
                "off_positive_deposition_cells":z_off["net_elevation_gain_cells"]})
    report={"synthetic":True,"n_native_scenarios":len(out),
            "same_4m_0.648ha_active_land_and_slope":True,
            "all_physics_upstream_shETRAN":True,
            "no_open_outlet":True,"no_Gounsa_observed_vegetation_parameters":True,
            "scenarios":out,"contrasts":comparisons}
    (a.out/"full_factorial_results.json").write_text(json.dumps(report,indent=2))
    with (a.out/"summary_matrix.csv").open("w",newline="") as fp:
        fields=["type","rain_mm_h","canopy_on","source_detachment_solid_m3",
          "mean_original_soil_erosion_mm","mean_net_event_z_mm",
          "net_elevation_gain_cells","net_elevation_loss_cells","max_net_deposition_mm",
          "max_net_erosion_mm","relative_sediment_mass_error"]
        w=csv.DictWriter(fp,fieldnames=fields);w.writeheader()
        for d in out:w.writerow({k:d.get(k) for k in fields})
    print("QA_LARGE_PATCH_COMPLETE "+json.dumps({"n_cases":len(out),
      "max_mass_residual":max(z["relative_sediment_mass_error"] for z in out),
      "contrasts":comparisons}),flush=True)
if __name__=="__main__":main()
