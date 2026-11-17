#!/usr/bin/env python3
"""Consistency of the exported layered PAW profile against LORICA's own totals.
usage: check_paw_profile.py <TREED_exchange.zip> <label>
For every year: node 0 is 0, the profile never decreases, and for cells whose soil is
no deeper than the last node the final value equals paw_mm.asc (treed_paw_mm).
Prints the mean ratio profile(min(0.5 m, soil)) / uniform storage at 0.5 m.
Exit 1 on a violation.
"""
import re
import sys
import zipfile

import numpy as np

z = zipfile.ZipFile(sys.argv[1]); label = sys.argv[2]
names = z.namelist()


def asc(n):
    rows = []
    for l in z.read(n).decode().split("\n"):
        w = l.split()
        if len(w) == 2 and re.match(r"^[A-Za-z_]+$", w[0]):
            continue
        if w:
            rows.append([float(x) for x in w])
    return np.array(rows)


years = sorted({m.group(1) for n in names for m in [re.search(r"/(\d{4})/input/paw_profile_mm\.csv$", n)] if m})
bad = 0; worst = 0.0; ratios = []
for y in years:
    pf = [n for n in names if "/%s/input/paw_profile_mm.csv" % y in n][0]
    lines = z.read(pf).decode().strip().split("\n")
    step = float(lines[0].split()[1].split("=")[1]); K = int(lines[0].split()[2].split("=")[1]) - 1
    paw = asc([n for n in names if "/%s/input/paw_mm.asc" % y in n][0])
    sd = asc([n for n in names if "/%s/input/soildepth.asc" % y in n][0])
    for ln in lines[1:]:
        f = ln.split(","); r, c = int(f[0]), int(f[1]); v = np.array([float(x) for x in f[2:]])
        if v[0] != 0.0 or (np.diff(v) < -1e-9).any():
            bad += 1; print("  year", y, "cell", r, c, "profile not starting at 0 or decreasing")
        if sd[r, c] <= K * step and paw[r, c] > 0:
            d = abs(v[-1] - paw[r, c]) / paw[r, c]; worst = max(worst, d)
            if d > 1e-9:
                bad += 1; print("  year", y, "cell", r, c, "end value", v[-1], "paw_mm", paw[r, c])
        if sd[r, c] > 0 and paw[r, c] > 0:
            zz = min(0.5, sd[r, c]); k = int(zz / step); fr = zz / step - k
            lay = v[k] + (fr * (v[min(k + 1, K)] - v[k]) if k < K else 0.0)
            ratios.append(lay / (paw[r, c] * zz / sd[r, c]))
print("%s: %d years, max relative end-value deviation %.2e, violations %d, layered/uniform storage at <=0.5 m: mean %.3f [%.3f, %.3f]" % (
    label, len(years), worst, bad, np.mean(ratios) if ratios else float("nan"),
    min(ratios) if ratios else float("nan"), max(ratios) if ratios else float("nan")))
sys.exit(1 if bad or not years else 0)
