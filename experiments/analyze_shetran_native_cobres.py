#!/usr/bin/env python3
"""Diagnostics for an ACTUALLY EXECUTED upstream SHETRAN Cobres HDF5 result.

Computes descriptive data checks only. Does not claim exact sediment mass
conservation or that hourly HDF5 rates integrate native GNU substeps exactly.
"""
from pathlib import Path
import csv
import json
import sys
import numpy as np
import h5py

root = Path(sys.argv[1]) if len(sys.argv)>1 else Path("/tmp/shetran-native-cobres")
path = root / "output_cob_shegraph.h5"
assert path.is_file(), str(path)

def stats(a):
    a=np.asarray(a,dtype=np.float64)
    ok=np.isfinite(a)&(np.abs(a)<1e10)
    v=a[ok]
    return dict(valid_count=int(v.size),min=float(v.min()) if v.size else None,
                max=float(v.max()) if v.size else None,
                nonzero=int(np.count_nonzero(v)) if v.size else 0)

with h5py.File(path) as f:
    v=f["VARIABLES"]
    items={}
    for name,group in v.items():
        label=name.strip().split(" ",1)[-1].strip()
        if not isinstance(group,h5py.Group) or "value" not in group or "time" not in group:
            continue
        items.setdefault(label,[]).append((name,group))
    rate_candidates=items.get("s_v_er",[])
    loose_candidates=items.get("s_t_dp",[])
    assert rate_candidates, f"No original s_v_er in {list(items)}"
    rate_name, rate_g=max(rate_candidates,key=lambda ng:np.prod(ng[1]["value"].shape))
    loose_name, loose_g=max(loose_candidates,key=lambda ng:np.prod(ng[1]["value"].shape))
    rate=np.asarray(rate_g["value"],dtype=np.float64)
    loose=np.asarray(loose_g["value"],dtype=np.float64)
    times=np.asarray(rate_g["time"],dtype=np.float64)
    times_d=np.asarray(loose_g["time"],dtype=np.float64)
    assert rate.shape==loose.shape and rate.ndim==3,(rate.shape,loose.shape)
    assert np.allclose(times,times_d) and np.all(np.diff(times)>0)
    assert rate.shape[-1]==times.size and times.size>=3
    active=np.isfinite(rate).all(axis=-1) & np.isfinite(loose).all(axis=-1)
    active &= (np.abs(rate)<1e10).all(axis=-1) & (np.abs(loose)<1e10).all(axis=-1)
    active &= (loose>=0).all(axis=-1)
    rate_a=rate[active]
    loose_a=loose[active]
    assert rate_a.size>0
    dt=np.diff(times)*3600.0
    # Rate in mm/day -> metres of source material eroded per record interval.
    # Right-endpoint and trapezoid are two *approximations* from snapshots.
    right=np.sum(rate_a[:,1:]*dt[np.newaxis,:],axis=-1)/86400000.0
    trap=np.sum(0.5*(rate_a[:,1:]+rate_a[:,:-1])*dt[np.newaxis,:],axis=-1)/86400000.0
    net_dls=(loose_a[:,-1]-loose_a[:,0])/1000.0
    outcome={
        "source":"native SHETRAN 4.7.2.0 pinned SHA cf9cd540add78ad3accbaf62b4199d2032887f6b",
        "native_shetran_executed":True,
        "modified_inputs_only":"shortened Cobres simulation to 48 hours; sediment began at first time",
        "hdf5":path.name,
        "rate_dataset":rate_name,
        "loose_dataset":loose_name,
        "time_hours_first_last":[float(times[0]),float(times[-1])],
        "number_recorded_times":int(times.size),
        "grid_shape":[int(x) for x in rate.shape[:2]],
        "num_cells_with_finite_nonnegative_loose_depth":int(active.sum()),
        "rate_mm_day":stats(rate_a),
        "loose_depth_mm":stats(loose_a),
        "right_endpoint_sampled_erosion_m":stats(right),
        "trapezoid_sampled_erosion_m":stats(trap),
        "sampled_integral_difference_m":stats(right-trap),
        "net_dls_change_m":stats(net_dls),
        "cells_nonzero_erosion_right_endpoint":int(np.count_nonzero(right>0)),
        "cells_nonzero_dls_delta":int(np.count_nonzero(net_dls!=0)),
        "blockers":[
            "HDF5 hourly source-rate integration is NOT exact native GNU*DTUZ",
            "native SYMAIN first-call initialization and missing first step not repaired",
            "no original sediment mass conservation audit yet",
            "no completed SY52 FBETA / SY53 FDEL + water hotstart continuity",
            "no FR37/OC35/VS08 coupled next-event native rerun yet"
        ],
    }
    for label,groups in items.items():
        if label.startswith("s_dis"):
            for name,g in groups:
                outcome["outlet_"+label+"_kg_s"]=stats(g["value"][()])
    for ext in ["output_cob_mb.csv","output_cob_sediment_all.csv","output_cob_sediment_fine.csv"]:
        fcsv=root/ext
        if fcsv.exists():
            with fcsv.open(newline="") as fd:
                rows=list(csv.reader(fd))
            outcome[ext]={"num_rows":len(rows),"header":rows[0][:15] if rows else [],
                          "last_row":rows[-1][:15] if rows else []}
out=root/"native_cobres_48h_diagnostics.json"
out.write_text(json.dumps(outcome,indent=2,ensure_ascii=False,allow_nan=False))
print("NATIVE_COBRES_DIAGNOSTICS_JSON")
print(out.read_text())
