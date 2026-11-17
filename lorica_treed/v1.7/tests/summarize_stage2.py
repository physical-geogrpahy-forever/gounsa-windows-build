#!/usr/bin/env python3
"""Per-year summary of a stage-2 run from the published results.
usage: summarize_stage2.py <runs/<id>_v17stage2 directory> [years comma list]
Reads TREED_exchange.zip of every lorica-v17s2-* condition.
Quantities: occupied cells, killed and recolonised cells (from the stage-2 summary),
mean FPC and mean area-normalised root carbon over all 25 cells, mean phi of occupied
cells. Synthetic weather and a 5 x 5 synthetic hillslope: not field data.
"""
import glob
import os
import re
import sys
import zipfile

import numpy as np

base = sys.argv[1]
years = [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 else [1, 3, 4, 5, 6, 8, 10, 15, 20, 30, 34]


def asc(z, name):
    t = z.read(name).decode().split("\n")
    nd = -9999.0
    rows = []
    for l in t:
        w = l.split()
        if len(w) == 2 and re.match(r"^[A-Za-z_]+$", w[0]):
            if w[0].lower() == "nodata_value":
                nd = float(w[1])
            continue
        if w:
            rows.append([float(x) for x in w])
    a = np.array(rows)
    a[a == nd] = np.nan
    return a


for c in sorted(glob.glob(os.path.join(base, "lorica-v17s2-*"))):
    zp = os.path.join(c, "TREED_exchange.zip")
    if not os.path.exists(zp):
        print("==", os.path.basename(c), "no exchange zip")
        continue
    z = zipfile.ZipFile(zp)
    names = z.namelist()
    print("==", os.path.basename(c))
    print(" year  occ  killed recol  FPC_mean  rootC_mean  phi_mean(occ)  soil0cells")
    for y in years:
        ys = "%04d" % y
        f = lambda k: [n for n in names if "/%s/" % ys in n and n.endswith(k)]
        fpc = f("output/treed_fpc.asc")
        if not fpc:
            continue
        fpc_a = asc(z, fpc[0])
        root_a = asc(z, f("output/treed_rootC_areanorm_gC_m2.asc")[0])
        sd = asc(z, f("input/soildepth.asc")[0])
        occ = f("output/treed_stage2_occupied.asc")
        if occ:
            o = asc(z, occ[0]); ph = asc(z, f("output/treed_stage2_phi.asc")[0])
            summ = z.read(f("output/treed_stage2_summary.csv")[0]).decode().strip().split("\n")[1].split(",")
            print(" %4d %4d %6s %5s  %8.3f  %10.1f  %12.3f  %5d" % (
                y, int(np.nansum(o)), summ[1], summ[2], np.nanmean(fpc_a), np.nanmean(root_a),
                np.nanmean(ph[o > 0.5]) if (o > 0.5).any() else float("nan"), int((sd <= 1e-6).sum())))
        else:
            print(" %4d %4s %6s %5s  %8.3f  %10.1f  %12s  %5d" % (
                y, "-", "-", "-", np.nanmean(fpc_a), np.nanmean(root_a), "-", int((sd <= 1e-6).sum())))
