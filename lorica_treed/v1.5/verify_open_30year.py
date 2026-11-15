#!/usr/bin/env python3
"""Validate 30 years of actual native TREED-LORICA on synthetic open hillslope."""
import csv, json, math, pathlib, sys
root=pathlib.Path(sys.argv[1]);out=pathlib.Path(sys.argv[2])
out.mkdir(parents=True,exist_ok=True)
errors=[];data={}; N=30
for name,beta in (("beta0",0),("beta2",2)):
    folder=root/("lorica-v15-open30-"+name)
    f=folder/"annual_state.csv";m=folder/"LORICA_TREED_V1_2_ANNUAL_SENSITIVITY_PASS.txt"
    if not f.is_file() or not m.is_file():
        errors.append(name+" missing output or marker");continue
    marker=m.read_text(encoding="utf-8-sig")
    if "topology=open_hillslope" not in marker or "years=30" not in marker or "beta="+str(beta) not in marker:
        errors.append(name+" invalid completion marker")
    with f.open(newline="",encoding="utf-8-sig") as fh: rows=list(csv.DictReader(fh))
    if len(rows)!=N: errors.append(name+": incorrect annual count "+str(len(rows)))
    if (folder/"soil_layers.csv").is_file():
        with (folder/"soil_layers.csv").open(newline="",encoding="utf-8-sig") as fh: lay=list(csv.DictReader(fh))
        if len(lay)!=N*25*10:errors.append(name+": incorrect layer rows")
    else: errors.append(name+": soil layers missing")
    if (folder/"TREED_driver_audit.csv").is_file():
        with (folder/"TREED_driver_audit.csv").open(newline="",encoding="utf-8-sig") as fh: audit=list(csv.DictReader(fh))
        if len(audit)!=N or any(r["restart_present_after"]!="true" for r in audit):
            errors.append(name+": TREED restart continuity")
    else:errors.append(name+": TREED restart audit missing")
    for y,r in enumerate(rows,1):
        if int(r["year"])!=y:errors.append(name+": year mismatch "+str(y))
        if float(r["mass_closure"])>1e-6:errors.append(name+": mass balance year "+str(y))
        if float(r["treed_input_DTM_error_m"])>5.1e-7 or float(r["treed_input_soildepth_error_m"])>5.1e-7:
            errors.append(name+": state exchange year "+str(y))
        if float(r["explicit_water_export_kg"])<0 or float(r["water_erosion_sum_m"])<0:
            errors.append(name+": negative sediment output year "+str(y))
        if abs(float(r["unclassified_transient_kg"]))>1e-5:errors.append(name+": untracked transport "+str(y))
        if y>1:
            before=float(rows[y-2]["soil_mass_kg"]);after=float(r["soil_mass_kg"])
            # no landslides or active soil production expected in this test
            if int(r["landslide_initiations"])==0 and abs((before-after)-float(r["explicit_water_export_kg"]))>1e-4:
                errors.append(name+": annual soil mass loss != exported flux year "+str(y))
    if len(list(folder.glob("year_??/dtm_m.asc")))!=N:errors.append(name+": missing yearly DEM rasters")
    if len(list(folder.glob("year_??/TREED_FPC.asc")))!=N:errors.append(name+": missing yearly FPC rasters")
    data[name]=rows
if len(data)==2 and len(data["beta0"])==N and len(data["beta2"])==N:
    for y,(a,b) in enumerate(zip(data["beta0"],data["beta2"]),1):
        for key in ("annual_precip_mm","mean_temperature_C"):
            if float(a[key])!=float(b[key]):errors.append("Forcing mismatch "+str(y)+" "+key)
    for key in ("FPC_mean","LAI_mean","rootC_mean_gC_m2","runoff_sum_m","root_cohesion_mean_kPa"):
        if abs(float(data["beta0"][0][key])-float(data["beta2"][0][key]))>1e-7:
            errors.append("Different initial conditions "+key)
totals={}
for name,rows in data.items():
    totals[name]={
      "gross_erosion_sum_cell_depth_m":sum(float(r["water_erosion_sum_m"]) for r in rows),
      "deposition_sum_cell_depth_m":sum(float(r["water_deposition_sum_m"]) for r in rows),
      "external_export_kg":sum(float(r["explicit_water_export_kg"]) for r in rows),
      "max_mass_closure":max(float(r["mass_closure"]) for r in rows),
      "landslide_initiations":sum(int(r["landslide_initiations"]) for r in rows)
    }
    if totals[name]["external_export_kg"]<=1e-9:errors.append(name+": open-outlet external sediment export absent")
blocks=[]
if len(data)==2:
    for i in range(0,N,5):
        a=data["beta0"][i:i+5];b=data["beta2"][i:i+5]
        ea=sum(float(r["explicit_water_export_kg"]) for r in a)
        eb=sum(float(r["explicit_water_export_kg"]) for r in b)
        ba=sum(float(r["water_erosion_sum_m"]) for r in a)
        bb=sum(float(r["water_erosion_sum_m"]) for r in b)
        blocks.append({"years":str(i+1)+"-"+str(i+len(a)),"export_beta0_kg":ea,"export_beta2_kg":eb,
                       "export_reduction_pct":100*(1-eb/ea) if ea>0 else None,
                       "erosion_beta0_sum_cell_depth_m":ba,"erosion_beta2_sum_cell_depth_m":bb,
                       "FPC_beta0_last":a[-1]["FPC_mean"],"FPC_beta2_last":b[-1]["FPC_mean"],
                       "max_mass_closure":max(float(r["mass_closure"]) for r in a+b)})
    with (out/"open_30year_five_year_blocks.csv").open("w",newline="",encoding="utf8") as fh:
        w=csv.DictWriter(fh,fieldnames=list(blocks[0]));w.writeheader();w.writerows(blocks)
summary={"status":"PASS" if not errors else "NEEDS_INVESTIGATION","years":30,
         "domain":"5x5 @ 10m synthetic open hillslope, not actual Gounsa",
         "only_erosion_treatment":"FPC beta=0 versus beta=2",
         "soil_water_coupling_strength":1.0,
         "totals":totals,"five_year_blocks":blocks,"errors":errors}
(out/"open_30year_verification.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
print(json.dumps(summary,indent=2,ensure_ascii=False))
if errors: raise SystemExit("GOUNSA_V15_OPEN_30YEAR_VERIFICATION_FAILED")
print("GOUNSA_V15_OPEN_30YEAR_PASS")
