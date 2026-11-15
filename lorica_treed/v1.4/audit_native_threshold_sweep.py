#!/usr/bin/env python3
"""Independent audit of fresh 64-case native LORICA threshold/landslide outputs."""
import csv
import json
import math
import pathlib
import sys

source=pathlib.Path(sys.argv[1])
out=pathlib.Path(sys.argv[2])
out.mkdir(parents=True,exist_ok=True)
with source.open(encoding="utf-8-sig",newline="") as f:
    rows=list(csv.DictReader(f))
alerts=[]
if len(rows)!=64: alerts.append(f"Expected 64 rows, got {len(rows)}")
if any(r["status"]!="PASS" for r in rows):
    alerts.extend(f"Native failed case: {r}" for r in rows if r["status"]!="PASS")
for r in rows:
    if r["status"]!="PASS": continue
    if float(r["mass_closure"])>1e-6: alerts.append("Mass closure "+str(r))
    if float(r["event_mm"])==0 and int(r["initiations"])!=0: alerts.append("No-rain landslide "+str(r))
    if not (0<=float(r["actual_slope_deg"])<=90): alerts.append("Invalid computed slope "+str(r))
def locate(s,root,p):
    return next((r for r in rows if float(r["slope_deg"])==s
                 and float(r["root_kPa"])==root and float(r["event_mm"])==p),None)
count_anomalies=[]
threshold_anomalies=[]
for s in (10.,20.,30.,40.):
    for p in (0.,10.,30.,60.):
        rs=[locate(s,c,p) for c in (0.,2.,5.,8.)]
        if any(r is None or r["status"]!="PASS" for r in rs): continue
        counts=[int(r["initiations"]) for r in rs]
        if any(b>a for a,b in zip(counts,counts[1:])):
            count_anomalies.append({"type":"cohesion_more_landslides","slope":s,"storm":p,"counts":counts})
        values=[float(r["critical_rain_m_day"]) for r in rs]
        adjusted=[math.inf if v < -1000 else v for v in values]
        if any(b+1e-9<a for a,b in zip(adjusted,adjusted[1:])):
            threshold_anomalies.append({"type":"cohesion_lowered_critical_rain","slope":s,"storm":p,"values":values})
    for c in (0.,2.,5.,8.):
        rs=[locate(s,c,p) for p in (0.,10.,30.,60.)]
        if any(r is None or r["status"]!="PASS" for r in rs): continue
        counts=[int(r["initiations"]) for r in rs]
        if any(b<a for a,b in zip(counts,counts[1:])):
            count_anomalies.append({"type":"more_rain_fewer_landslides","slope":s,"cohesion":c,"counts":counts})
summary={
    "n_cases":len(rows),
    "native_calculation":"actual patched LORICA calc_and_write_ls_rasters and calculate_slide_new",
    "grid":"five 10m cells on monotonic slope",
    "event_duration_h":6,
    "critical_rain_sentinel_always_stable":-9999,
    "mass_closure_max":max((float(r["mass_closure"]) for r in rows if r["status"]=="PASS"),default=None),
    "positive_slide_cases":sum(int(r["initiations"])>0 for r in rows if r["status"]=="PASS"),
    "sample_thresholds":[{"slope_deg":s,"root_kPa":c,"storm_mm":60,
                         "critical_rain_m_day":locate(s,c,60.)["critical_rain_m_day"],
                         "initiations":locate(s,c,60.)["initiations"]}
                         for s in (10.,20.,30.,40.) for c in (0.,2.,5.,8.)
                         if locate(s,c,60.) and locate(s,c,60.)["status"]=="PASS"],
    "count_monotonicity_anomalies":count_anomalies,
    "threshold_monotonicity_anomalies":threshold_anomalies,
    "execution_errors":alerts,
}
summary["status"]="PASS" if not (alerts or count_anomalies or threshold_anomalies) else "INVESTIGATE"
(out/"native_threshold_audit.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(summary,ensure_ascii=False,indent=2))
if alerts or count_anomalies or threshold_anomalies:
    raise SystemExit("NATIVE_THRESHOLD_AUDIT_NEEDS_INVESTIGATION")
print("GOUNSA_V14_64_NATIVE_SENSITIVITY_AUDIT_PASS")
