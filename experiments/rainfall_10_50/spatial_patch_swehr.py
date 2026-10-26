#!/usr/bin/env python3
"""Spatial 2D hypothesis experiment with the *original* SWEHR solver equations.

Native C source from csdms-contrib/swehr. Prior validated initialization, inflow
suppression, and conservation ledger from verify_swehr_closure.add_patch.
New coupling: deterministic vegetation/stem positions -> spatial Ksat, n, a, ad,
J and canopy water/raindrop input. This coupling is NOT native published SWEHR.
NO field Gounsa DTM or vegetation polygons are present. ALL spatial parameters
and stemflow fractions are hypothetical: not calibrated oak or Miscanthus data.
"""
from pathlib import Path
from math import sin,pi,hypot
import argparse,sys,json,subprocess,re,random,math,csv
from verify_swehr_closure import add_patch,replace_once
ROOT=Path(__file__).resolve().parent
NX,NY,DX=13,25,0.5
AREA=NX*NY*DX*DX
CENTER=(NX-1)*DX/2
SCENARIOS=("grass_dense","oak_sparse","barrier_equal","island_equal")
def frac_positions(name):
    if name=="grass_dense":
        return [(x,y) for x in (0.6,1.9,3.2,4.5,5.8) for y in (0.7,2.0,3.3,4.6,5.9,7.2,8.5,9.8,11.1)]
    if name=="oak_sparse":
        return [(1.1,2.0),(5.1,4.0),(2.6,6.8),(4.8,9.7),(1.6,11.5)]
    if name=="island_equal":
        return [(1.0,2.0),(5.3,3.7),(2.4,6.3),(5.2,9.3),(1.0,10.9)]
    return [(x,y) for y in (1.5,4.0,6.5,9.0,11.5) for x in (0.5,2.5,4.5,6.0)]
def generate(name,rain,stemflow):
    points=frac_positions(name)
    cells=[]
    for i in range(NX):
        for j in range(NY):
            x=i*DX;y=j*DX
            d=min(hypot(x-a,y-b) for a,b in points)
            cells.append(dict(i=i,j=j,x=x,y=y,d=d))
    if name=="grass_dense": 
        for z in cells:z["veg"]=int(z["d"]<=0.86)
    elif name=="oak_sparse":
        for z in cells:z["veg"]=int(z["d"]<=0.66)
    elif name=="barrier_equal":
        rows={2,3,7,8,12,13,17,18,22,23}
        for z in cells:z["veg"]=int(z["j"] in rows)
    elif name=="island_equal":
        target=NX*10
        scored=sorted(cells,key=lambda z:(z["d"],z["i"],z["j"]))
        picks={(z["i"],z["j"]) for z in scored[:target]}
        for z in cells:z["veg"]=int((z["i"],z["j"]) in picks)
    assert name not in ("barrier_equal","island_equal") or sum(x["veg"] for x in cells)==NX*10
    lookup={(z["i"],z["j"]):z for z in cells}
    donors={k:0. for k in lookup}
    sftotal=0.
    for z in cells:
        z["int_mm"]= min(.8, rain*.25) if z["veg"] else 0.
        z["sf_donor_mm"]=rain*.10 if (z["veg"] and stemflow) else 0.
        sftotal+=z["sf_donor_mm"]
        z["drop_mm"]=rain-z["int_mm"]-z["sf_donor_mm"]
        assert z["drop_mm"]>=0
        if z["sf_donor_mm"]:
            a,b=min(points,key=lambda q:(z["x"]-q[0])**2+(z["y"]-q[1])**2)
            ii=min(range(NX),key=lambda i:abs(i*DX-a))
            jj=min(range(NY),key=lambda j:abs(j*DX-b))
            donors[(ii,jj)]+=z["sf_donor_mm"]
    fields=[]
    for z in cells:
        i=z["i"];j=z["j"];v=z["veg"]
        z["source_mm"]=z["drop_mm"]+donors[(i,j)]
        z["Ks"]=4.0e-6 if v else 1e-6       # HYPOTHETICAL, not species-fitted
        z["roughness"]=.18 if v else .08     # HYPOTHETICAL
        z["rain_a"]=.07 if v else .25        # HYPOTHETICAL
        z["rain_ad"]=.10 if v else .25       # HYPOTHETICAL
        z["J"]=90 if v else 30              # HYPOTHETICAL
        z["topo"]=4+.25*j*DX+.009*(i*DX-CENTER)**2
        fields.append(z)
    # A structural source conservation test, independent from SWEHR.
    gross_mm=rain*NX*NY
    infil_I=sum(z["int_mm"] for z in fields)
    delivered=sum(z["source_mm"] for z in fields)
    discrepancy=gross_mm-infil_I-delivered
    assert abs(discrepancy)<1e-8,(discrepancy,name,rain)
    assert abs(sum(donors.values())-sftotal)<1e-10
    # Bare-ground downslope continuity (j decreases toward outlet j=0);
    # structural indicator, NOT physically routed flowlength.
    runs=[]
    for i in range(NX):
        length=0
        for j in reversed(range(NY)):
            if lookup[(i,j)]["veg"]:length=0
            else:
                length+=DX
                runs.append(length)
    return fields,dict(n_cells=NX*NY,area_m2=AREA,
         vegetation_fraction=sum(z["veg"] for z in fields)/(NX*NY),
         bare_fraction=sum(not z["veg"] for z in fields)/(NX*NY),
         max_uninterrupted_bare_column_length_m=max(runs) if runs else 0,
         mean_bare_column_run_length_m=sum(runs)/len(runs) if runs else 0,
         storm_input_mm=rain,interception_volume_m3=infil_I*DX*DX/1000,
         stemflow_relocated_m3=sftotal*DX*DX/1000,
         effective_rain_volume_m3=delivered*DX*DX/1000,
         canopy_mass_error_m3=discrepancy*DX*DX/1000,
         note="Column flowlength is a directional structural proxy, not the 2D simulated runoff network.")

def spatial_patch(source):
    # Native SWEHR H-R/Hairsine–Rose and 2D shallow-water terms remain in C.
    source=replace_once(source,
       "    idum=-2999;",
       """    double **QA_WFACTOR, **QA_DFACTOR;
    QA_WFACTOR=matrix(1,nx,1,ny);
    QA_DFACTOR=matrix(1,nx,1,ny);
    idum=-2999;""")
    # After original parameter masks initialized in Remaining Set Up.
    hook="""            JSMASK[i][j]=Jentrain;
        }
    """
    assert source.count(hook)==1,source.count(hook)
    patch="""            JSMASK[i][j]=Jentrain;
        }

    // NEW COUPLING (not native SWEHR): spatial canopy/stemflow/hydraulic fields.
    FILE *fpspatial=fopen("./spatial_fields.txt","r");
    if (!fpspatial) {fprintf(stderr,"Cannot open spatial fields");exit(3);}
    for(i=1;i<=nx;i++) for(j=1;j<=ny;j++) {
        int n=fscanf(fpspatial,"%lf %lf %lf %lf %lf %lf %lf",
             &QA_WFACTOR[i][j],&QA_DFACTOR[i][j],
             &KS[i][j],&ROUGHNESS[i][j],&ASMASK[i][j],
             &ADSMASK[i][j],&JSMASK[i][j]);
        if(n!=7 || QA_WFACTOR[i][j]<0 || QA_DFACTOR[i][j]<0 ||
           KS[i][j]<0 || JSMASK[i][j]<=0) {
           fprintf(stderr,"Invalid map cell %d %d fields %d",i,j,n);exit(4);
        }
        MANNING[i][j]=ROUGHNESS[i][j];
    }
    fclose(fpspatial);
    """
    source=source.replace(hook,patch,1)
    # Native rainfall source is spatial, and only drop component can splash detach.
    source=replace_once(source,
        "E[1][k][i][j]=(1-H[i][j])*P[k][i][j]*ASMASK[i][j]*R;",
        "E[1][k][i][j]=(1-H[i][j])*P[k][i][j]*ASMASK[i][j]*R*QA_DFACTOR[i][j];")
    source=replace_once(source,
        "E[2][k][i][j]=H[i][j]*M[k][i][j]/TOTM[i][j]*ADSMASK[i][j]*R;",
        "E[2][k][i][j]=H[i][j]*M[k][i][j]/TOTM[i][j]*ADSMASK[i][j]*R*QA_DFACTOR[i][j];")
    source=replace_once(source,"                            + dt*R;",
       "                            + dt*R*QA_WFACTOR[i][j];")
    # Prior native QA ledger must now sum local rainfall, not global scalar R.
    source=replace_once(source,
       "        qa_rain+=dt*R*(nx*ny)*dx*dx;",
       """        for(i=1;i<=nx;i++) for(j=1;j<=ny;j++)
            qa_rain+=dt*R*QA_WFACTOR[i][j]*dx*dx;""")
    return source

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--scenario",choices=SCENARIOS,required=True)
    ap.add_argument("--rain",type=int,choices=[0,10,20,30,40,50],required=True)
    ap.add_argument("--stemflow",choices=["off","on"],default="off")
    ap.add_argument("--seconds",type=int,default=3600)
    x=ap.parse_args()
    name=f"{x.scenario}_p{x.rain:02d}_sf{x.stemflow}_{x.seconds}s"
    wd=ROOT/"spatial_patch_experiments"/"runs"/name
    wd.mkdir(parents=True,exist_ok=True)
    fields,info=generate(x.scenario,x.rain,x.stemflow=="on")
    # Source original DEM raster input expects x(i) OUTER, y(j) INNER.
    (wd/"spatial_fields.txt").write_text("\n".join(
       " ".join(f"{v:.15g}" for v in [z["source_mm"]/x.rain if x.rain else 0,
          z["drop_mm"]/x.rain if x.rain else 0,z["Ks"],z["roughness"],
          z["rain_a"],z["rain_ad"],z["J"]]) for z in fields)+"\n")
    (wd/"topoin.txt").write_text("\n".join(f"{z['topo']:.12g}" for z in fields)+"\n")
    (wd/"vegetation_map.csv").write_text("i,j,x_m,y_m,veg,topo_m,ks_m_s,manning,soil_a,soil_J,rain_source_mm,rain_drop_mm\n"+
        "\n".join(",".join(str(z[y]) for y in ("i","j","x","y","veg","topo","Ks","roughness","rain_a","J","source_mm","drop_mm")) for z in fields)+"\n")
    from verify_swehr_closure import call
    src=ROOT/"source_swehr"
    if not src.exists():
        p=subprocess.run(["git","clone","--depth","1","https://github.com/csdms-contrib/swehr.git",str(src)],capture_output=True,text=True)
        if p.returncode:raise RuntimeError(p.stderr[-3000:])
    source_sha=call(["git","rev-parse","HEAD"],src)[1].strip()
    original=(src/"SWEHR.c").read_text()
    source=add_patch(original,x.rain,1e-6,True,False,.08)
    # Diagnostic probes in original C target y=50, outside the 25-row grid.
    # Change only output sample positions; do not modify physical equations.
    for old,new in [("YPOINT[2]=10;","YPOINT[2]=7;"),
                    ("YPOINT[3]=20;","YPOINT[3]=12;"),
                    ("YPOINT[4]=30;","YPOINT[4]=17;"),
                    ("YPOINT[5]=40;","YPOINT[5]=21;"),
                    ("YPOINT[6]=50;","YPOINT[6]=24;")]:
        assert source.count(old)==1,(old,source.count(old))
        source=source.replace(old,new,1)
    source=spatial_patch(source)
    (wd/"SWEHR_spatial_coupling.c").write_text(source)
    inputvals=list(map(float,(src/"input.txt").read_text().split()))
    assert len(inputvals)==14
    inputvals[0]=NX;inputvals[1]=NY;inputvals[2]=DX
    inputvals[5]=x.seconds;inputvals[6]=.25;inputvals[7]=.25;inputvals[3]=.004
    inputvals[10]=math.ceil(x.seconds/60);inputvals[11]=60
    (wd/"input.txt").write_text("\n".join(map(str,inputvals))+"\n")
    (wd/"rain.txt").write_text("\n".join([f"{x.rain/3600000:.16g}"]*int(inputvals[10]))+"\n")
    for p in ("particlesizein.txt","particlepercentin.txt"):
        (wd/p).write_bytes((src/p).read_bytes())
    cc,build=call(["gcc","-O2","-std=gnu99","-o",str(wd/"native"),str(wd/"SWEHR_spatial_coupling.c"),"-lm"],wd,60)
    (wd/"build.log").write_text(build)
    if cc:raise RuntimeError(build[-5000:])
    try:rc,out=call([str(wd/"native")],wd,300)
    except subprocess.TimeoutExpired as e:rc=124;out="NATIVE TIMEOUT "+repr(e)
    (wd/"run.log").write_text(out[-100000:])
    r=dict(scenario=x.scenario,intensity_mm_h=x.rain,stemflow=x.stemflow,seconds=x.seconds,
           native_source_sha=source_sha,engine_exit_code=rc,**info)
    j=re.findall(r"QA_JSON (\{[^\n]*\})",out)
    y=re.findall(r"QA_LAYER (\{[^\n]*\})",out)
    if j:
        d=json.loads(j[-1]);r.update(d)
        sc=max(1e-8,abs(d["rain_m3"])+abs(d["initial_water_m3"])+abs(d["net_boundary_water_out_m3"]))
        r["water_relative_residual"]=abs(d["water_residual_m3"])/sc
        if y:
            q=json.loads(y[-1]);r.update(q)
            den=max(1e-8,q["original_soil_detachment_kg"])
            r["original_soil_relative_residual"]=abs(q["original_layer_residual_kg"])/den
            r["bed_geometry_relative_residual"]=abs(q["geometry_layer_residual_kg"])/den
        r["sediment_export_t_ha"]=d["net_boundary_sediment_out_kg"]/AREA*10
        r["gross_detachment_t_ha"]=r.get("original_soil_detachment_kg",0)/AREA*10
        r["outflow_mm"]=d["net_boundary_water_out_m3"]/AREA*1000
    else:r["error_last_lines"]=out[-2400:]
    r["qa_pass"]=bool(rc==0 and r.get("water_relative_residual",1)<.001 and
         r.get("original_soil_relative_residual",1)<.01 and
         r.get("bed_geometry_relative_residual",1)<.01 and
         r.get("min_water_depth_m",-1e10)>=-1e-8 and
         r.get("min_suspended_mass_kg_m2",-1e10)>=-1e-8 and
         abs(r.get("rain_m3",0)-info["effective_rain_volume_m3"])<.000001)
    (wd/"qa_result.json").write_text(json.dumps(r,ensure_ascii=False,indent=2))
    print("SPATIAL_QA "+json.dumps(r,ensure_ascii=False),flush=True)
    if not r["qa_pass"]:sys.exit(2)
if __name__=="__main__":main()
