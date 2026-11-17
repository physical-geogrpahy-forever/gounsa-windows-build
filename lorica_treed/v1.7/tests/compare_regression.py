#!/usr/bin/env python3
"""Byte-level regression check: stage-2 patch with mortality_mode=off versus the
unpatched v1.7 seasonal run (same seed, same weather).

usage: compare_regression.py <new TREED_exchange.zip> <old TREED_exchange.zip> <label>
Compares every .asc file under <year>/input and <year>/output after removing the
run-number directory. The NetCDF files are not compared (binary container).
Exit code 1 on any difference or on a differing file set.
"""
import re
import sys
import zipfile


def table(path):
    z = zipfile.ZipFile(path)
    out = {}
    for n in z.namelist():
        if not n.endswith(".asc"):
            continue
        m = re.match(r"^[^/]+/(\d{4}/(?:input|output)/.+)$", n)
        if m:
            out[m.group(1)] = z.read(n)
    return out


new, old, label = table(sys.argv[1]), table(sys.argv[2]), sys.argv[3]
only_new = sorted(set(new) - set(old))
only_old = sorted(set(old) - set(new))
diff = sorted(k for k in set(new) & set(old) if new[k] != old[k])
print("%s: %d files compared, %d identical, %d differ, %d only in new, %d only in old" % (
    label, len(set(new) & set(old)), len(set(new) & set(old)) - len(diff), len(diff), len(only_new), len(only_old)))
for k in diff[:15]:
    print("  DIFF", k)
for k in only_new[:15]:
    print("  ONLY_NEW", k)
for k in only_old[:15]:
    print("  ONLY_OLD", k)
if len(set(new) & set(old)) == 0:
    print("  NO COMMON FILES: comparison is void")
    sys.exit(1)
sys.exit(1 if (diff or only_new or only_old) else 0)
