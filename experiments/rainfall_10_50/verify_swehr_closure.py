#!/usr/bin/env python3
"""Native SWEHR scientific verification, with explicitly documented initialization/boundary fixes.
Physical SWE, Green-Ampt, Hairsine-Rose equations are otherwise unchanged.
"""
import argparse, pathlib, subprocess, json, re, os, math
ROOT=pathlib.Path(__file__).resolve().parent
def call(cmd,cwd=None,timeout=500):
    p=subprocess.run(cmd,cwd=cwd,text=True,encoding="latin1",stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT,timeout=timeout)
    return p.returncode,p.stdout
def replace_once(s,old,new):
    assert s.count(old)==1, (old[:120], s.count(old))
    return s.replace(old,new,1)
def add_patch(src,rain_mm_h,ks_m_s,erosion,onclosed,roughness=0.1):
    p=src
    # Original public code sets an initial water depth in DEPTHINIT but does not assign U[1].
    p=replace_once(p,
         "            DEPTHINIT[i][j]=1e-4;               // INITIAL FLOW DEPTH",
         "            DEPTHINIT[i][j]=1e-4;               // INITIAL FLOW DEPTH\n"
         "            U[1][i][j]=DEPTHINIT[i][j]; // QA: defined conserved depth\n"
         "            SOLID[i][j]=0; // QA: no internal solids in provided DEM\n"
         "            for (k=1;k<=sclass;k++) M[k][i][j]=0.0; // QA: empty initial loose layer")
    # The published input code contains an *unconditional* upstream sediment and water inflow
    # AFTER the BNDRY[4] wall/transmission logic; remove that block for rain-only simulations.
    before="        // Sediment and Water Inflow B.C. at j=ny"
    after="        // Topography B.C. at i=1 and i=nx"
    assert p.count(before)==1 and p.count(after)==1
    q1=p.index(before);q2=p.index(after,q1)
    p=p[:q1]+"        // QA: published imposed upstream hydrograph/sediment inflow DISABLED.\n\n"+p[q2:]
    p=replace_once(p,"            KS[i][j]=0;                         // SATURATED HYDRAULIC CONDUCTIVITY [m]/[s]",
       f"            KS[i][j]={ks_m_s:.12g}; // QA study infiltration Ksat [m/s]")
    p=replace_once(p,"            ROUGHNESS[i][j]=0.1;",f"            ROUGHNESS[i][j]={roughness:.10g}; // sensitivity parameter Manning base")
    p=replace_once(p,"             MANNING[i][j]=0.1;",f"             MANNING[i][j]={roughness:.10g}; // sensitivity parameter Manning initial") if "             MANNING[i][j]=0.1;" in p else p
    if onclosed:
        p=replace_once(p,"    BNDRY[2]=0;                                 // B.C. at j==1",
                       "    BNDRY[2]=1;                                 // B.C. at j==1; QA closed box")
    # Initialize all arrays subsequently read in source terms, before first time step.
    target="    // Remaining Set Up"
    init="""    // QA: well-defined original soil, sediment layer, and water before first flux.
    for (i=1;i<=nx;i++) for(j=1;j<=ny;j++) {
        TOTM[i][j]=0.0;
        DEP[i][j]=0.0;
        TOTSED[i][j]=0.0;
        TOPOOLD[i][j]=TOPO[i][j];
        H[i][j]=0.0;
        TRACER[i][j]=0.0;
    }

"""
    p=replace_once(p,target,init+target)
    # Running-integral diagnostics, in SI units and integrated across cell area.
    p=replace_once(p,"    idum=-2999;",
         """    double qa_w0=0,qa_wf=0,qa_rain=0,qa_infil=0,qa_wboundary=0,qa_sboundary=0;
    double qa_susp=0,qa_bed=0,qa_sed_vol=0,qa_min_depth=1e200,qa_min_sed=1e200;
    double qa_loose=0,qa_bed_down=0,qa_bed_up=0,qa_original_detach=0;
    idum=-2999;""")
    afterinit="    // Remaining Set Up"
    p=replace_once(p,afterinit,"""    for (i=1;i<=nx;i++) for (j=1;j<=ny;j++) qa_w0+=U[1][i][j]*dx*dx;
    
"""+afterinit)
    # Integrate finite volume fluxes AFTER adaptive timestep finalized but BEFORE state update.
    anchor="        // Time Update\n        //#pragma omp parallel for private(j,k,chtemp,redetach,beta)"
    diag="""        // QA finite-volume boundary fluxes, positive = net outward volume or mass.
        qa_rain+=dt*R*(nx*ny)*dx*dx;
        for(i=1;i<=nx;i++) for(j=1;j<=ny;j++) if(SOLID[i][j]==0)
            for(k=1;k<=sclass;k++) qa_original_detach+=dt*dx*dx*(E[1][k][i][j]+E[3][k][i][j]);
        for (j=1;j<=ny;j++) {
           qa_wboundary+=dt*dx*(FLUXX[1][nx+1][j]-FLUXX[1][1][j]);
           for (k=4;k<=nn;k++)
             qa_sboundary+=dt*dx*(FLUXX[k][nx+1][j]-FLUXX[k][1][j]);
        }
        for (i=1;i<=nx;i++) {
           qa_wboundary+=dt*dx*(FLUXY[1][i][ny+1]-FLUXY[1][i][1]);
           for (k=4;k<=nn;k++)
             qa_sboundary+=dt*dx*(FLUXY[k][i][ny+1]-FLUXY[k][i][1]);
        }
        // Time Update
        //#pragma omp parallel for private(j,k,chtemp,redetach,beta)"""
    p=replace_once(p,anchor,diag)
    p=replace_once(p,"                        U[1][i][j] = U[1][i][j]+(U[k][i][j]-chtemp)/(rhos*(1-phi));",
       """                        // QA: SWEHR compensates water-column depth for solids volume; ledger it.
                        qa_sed_vol += (U[k][i][j]-chtemp)/(rhos*(1-phi))*dx*dx;
                        U[1][i][j] = U[1][i][j]+(U[k][i][j]-chtemp)/(rhos*(1-phi));""")
    p=replace_once(p,"        t+=dt;",
       """        for (i=1;i<=nx;i++) for(j=1;j<=ny;j++) qa_infil+=INFL[i][j]*dx*dx;
        t+=dt;""")
    before_end="    time_t t1 = time(NULL);"
    conclusion="""    for (i=1;i<=nx;i++) for(j=1;j<=ny;j++) {
       double zdelta=TOPO[i][j]-TOPOINIT[i][j];
       qa_wf+=U[1][i][j]*dx*dx;
       if (U[1][i][j]<qa_min_depth) qa_min_depth=U[1][i][j];
       qa_bed += rhos*(1-phi)*zdelta*dx*dx;
       qa_bed_down += fmax(0,-zdelta)*dx*dx;
       qa_bed_up += fmax(0,zdelta)*dx*dx;
       qa_loose+=TOTM[i][j]*dx*dx;
       for(k=4;k<=nn;k++) {
          qa_susp+=U[k][i][j]*dx*dx;
          if (U[k][i][j]<qa_min_sed)qa_min_sed=U[k][i][j];
       }
    }
    double qa_wres=(qa_wf-qa_w0) - qa_rain + qa_infil + qa_wboundary - qa_sed_vol;
    double qa_sres=qa_bed+qa_susp+qa_sboundary;
    double qa_orig_res=qa_original_detach-qa_loose-qa_susp-qa_sboundary;
    double qa_geom_res=qa_bed-qa_loose+qa_original_detach;
    printf("QA_JSON {\\\"initial_water_m3\\\":%.15g,\\\"final_water_m3\\\":%.15g,"
      "\\\"rain_m3\\\":%.15g,\\\"infil_m3\\\":%.15g,\\\"net_boundary_water_out_m3\\\":%.15g,"
      "\\\"sediment_volume_correction_m3\\\":%.15g,\\\"water_residual_m3\\\":%.15g,"
      "\\\"bed_mass_delta_kg\\\":%.15g,\\\"suspended_sediment_kg\\\":%.15g,"
      "\\\"net_boundary_sediment_out_kg\\\":%.15g,\\\"sediment_residual_kg\\\":%.15g,"
      "\\\"gross_bed_lowering_m3\\\":%.15g,\\\"gross_bed_rise_m3\\\":%.15g,"
      "\\\"deposited_layer_mass_kg\\\":%.15g,\\\"min_water_depth_m\\\":%.15g,"
      "\\\"min_suspended_mass_kg_m2\\\":%.15g}\\n",
      qa_w0,qa_wf,qa_rain,qa_infil,qa_wboundary,qa_sed_vol,qa_wres,
      qa_bed,qa_susp,qa_sboundary,qa_sres,qa_bed_down,qa_bed_up,qa_loose,
      qa_min_depth,qa_min_sed);
    printf("QA_LAYER {\\"original_soil_detachment_kg\\":%.15g,\\"deposited_layer_kg\\":%.15g,\\"original_layer_residual_kg\\":%.15g,\\"geometry_layer_residual_kg\\":%.15g}\\n",
       qa_original_detach, qa_loose, qa_orig_res, qa_geom_res);
"""
    p=replace_once(p,before_end,conclusion+"\n"+before_end)
    return p

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--rain",type=int,required=True)
    parser.add_argument("--tag",default="baseline")
    parser.add_argument("--roughness",type=float,default=0.1)
    parser.add_argument("--a",type=float,default=0.25)
    parser.add_argument("--ad",type=float,default=0.25)
    parser.add_argument("--f",type=float,default=0.004)
    parser.add_argument("--canopy-loss-mm",type=float,default=0.0,
                        help="Removed from gross event depth over first 1h; input to original model is resulting homogeneous net precipitation")

    parser.add_argument("--seconds",type=int,default=3600)
    parser.add_argument("--ks",type=float,default=2e-6)
    parser.add_argument("--erosion",choices=["off","on"],default="off")
    parser.add_argument("--boundary",choices=["closed","open"],default="open")
    args=parser.parse_args()
    assert 0<=args.canopy_loss_mm<=args.rain
    work=ROOT/"runtime"/f"{args.tag}_{args.rain:02d}_{args.seconds}_{args.erosion}_{args.boundary}_{args.ks:.1g}"
    work.mkdir(parents=True,exist_ok=True)
    src=ROOT/"source_swehr"
    if not src.exists():
        p=subprocess.run(["git","clone","--depth","1","https://github.com/csdms-contrib/swehr.git",str(src)],text=True,
                         capture_output=True)
        if p.returncode:raise RuntimeError(p.stderr[-4000:])
    sha=call(["git","rev-parse","HEAD"],src)[1].strip()
    s=(src/"SWEHR.c").read_text()
    patched=add_patch(s,args.rain,args.ks,args.erosion,args.boundary=="closed",args.roughness)
    c=work/"SWEHR_QA.c"
    c.write_text(patched)
    (work/"original_source_sha.txt").write_text(sha+"\n")
    vals=[float(x) for x in (src/"input.txt").read_text().split()]
    assert len(vals)==14 and int(vals[0])==3 and int(vals[1])==51
    vals[5]=args.seconds
    vals[6]=0 if args.erosion=="off" else args.a
    vals[7]=0 if args.erosion=="off" else args.ad
    vals[3]=0 if args.erosion=="off" else args.f # original F=0.004
    vals[10]=math.ceil(args.seconds/60)
    vals[11]=60
    (work/"input.txt").write_text("\n".join(str(v) for v in vals)+"\n")
    net_rain=args.rain-args.canopy_loss_mm*3600/args.seconds
    assert net_rain>=0
    (work/"rain.txt").write_text("\n".join([f"{net_rain/3600000:.16g}"]*int(vals[10]))+"\n")
    for n in ("topoin.txt","particlesizein.txt","particlepercentin.txt"):
        (work/n).write_bytes((src/n).read_bytes())
    cmd=["gcc","-O2","-std=gnu99","-Wall","-o",str(work/"qaengine"),str(c),"-lm"]
    rc,output=call(cmd,work,timeout=60)
    (work/"build.log").write_text(output)
    if rc: raise RuntimeError(output[-6000:])
    try:rc,output=call([str(work/"qaengine")],work,timeout=440)
    except subprocess.TimeoutExpired:raise RuntimeError("Native C run exceeded 440 seconds")
    (work/"run.log").write_text(output)
    matches=re.findall(r"QA_JSON (\{[^\n]*\})",output)
    layer_matches=re.findall(r"QA_LAYER (\{[^\n]*\})",output)
    result=dict(source_sha=sha,scenario=vars(args),effective_rain_mm_h=net_rain,run_exit=rc,qa_json_lines=len(matches))
    if matches:
        qa=json.loads(matches[-1])
        result.update(qa)
        if layer_matches:
            layer=json.loads(layer_matches[-1]);result.update(layer)
            lscale=max(layer["original_soil_detachment_kg"], 1e-8)
            result["original_layer_relative_residual"]=abs(layer["original_layer_residual_kg"])/lscale
            result["geometry_layer_relative_residual"]=abs(layer["geometry_layer_residual_kg"])/lscale
            result["independent_layer_pass"]=bool(result["original_layer_relative_residual"]<1e-2 and result["geometry_layer_relative_residual"]<1e-2)
        else:result["independent_layer_pass"]=False
        # Strict residual validation on total water and net solid ledger, incl sediment volume displacement.
        wscale=max(qa["rain_m3"]+qa["initial_water_m3"]+abs(qa["net_boundary_water_out_m3"]),1e-8)
        sscale=max(abs(qa["bed_mass_delta_kg"])+abs(qa["suspended_sediment_kg"])+abs(qa["net_boundary_sediment_out_kg"]),1e-8)
        result["water_relative_residual"]=abs(qa["water_residual_m3"])/wscale
        result["solid_relative_residual"]=abs(qa["sediment_residual_kg"])/sscale
        result["water_pass"]=bool(result["water_relative_residual"] < 1e-3)
        result["sediment_pass"]=bool(result["solid_relative_residual"] < 1e-2)
        result["nonnegative_pass"]=bool(qa["min_water_depth_m"]>=-1e-9 and qa["min_suspended_mass_kg_m2"]>=-1e-8)
        result["zero_sediment_pass"]=bool(args.erosion!="off" or 
          (abs(qa["bed_mass_delta_kg"])+abs(qa["suspended_sediment_kg"]))<1e-5)
        result["pass"]=bool(rc==0 and result["water_pass"] and result["sediment_pass"] and
                            result["nonnegative_pass"] and result["zero_sediment_pass"] and result["independent_layer_pass"])
    else: result["pass"]=False
    (work/"qa_result.json").write_text(json.dumps(result,indent=2,ensure_ascii=False))
    print("FINAL_QA "+json.dumps(result,ensure_ascii=False))
    if not result["pass"]: raise SystemExit(2)
if __name__=="__main__":main()
