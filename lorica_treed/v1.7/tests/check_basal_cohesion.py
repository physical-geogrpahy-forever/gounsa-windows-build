#!/usr/bin/env python3
"""Independent recomputation of the stage-4 basal root cohesion from published outputs.
usage: check_basal_cohesion.py <TREED_exchange.zip> <label>

For every year and cell it rebuilds the cohesion that LORICA (treed_coupling.cs) wrote to
treed_rootcohesion_Hwang2015_kPa.asc from the rasters of the same year (root carbon, rooting
depth z_r, soil depth) and the parameters in treed_rootcohesion_parameters.txt, using the
Jackson (1996) profile of the stage-4 design. This checks that the C# implements the formula
as written; it does not validate the formula. The self test first checks the profile maths
(integral of f is 1, zero below the rooted depth, truncation modes) by numerical quadrature.
Exit 1 on any violation.
"""
import math
import re
import sys
import zipfile

import numpy as np


def density(z_slip, d95, soil, trunc):
    if z_slip <= 0 or d95 <= 1e-6 or soil <= 1e-6:
        return 0.0
    lnb = math.log(0.05) / (100.0 * d95)
    z_end = soil if trunc == "soil_bottom" else min(d95, soil)
    if z_slip > z_end + 1e-12:
        return 0.0
    y_end = 1.0 - math.exp(100.0 * z_end * lnb)
    if y_end <= 1e-12:
        return 0.0
    return -100.0 * lnb * math.exp(100.0 * z_slip * lnb) / y_end


def selftest():
    bad = 0
    for d95 in (0.2, 0.5, 0.87, 1.5, 3.0):
        for soil in (0.05, 0.3, 0.5, 0.87, 1.2, 2.0):
            for trunc in ("module", "soil_bottom"):
                z_end = soil if trunc == "soil_bottom" else min(d95, soil)
                n = 20000
                zs = (np.arange(n) + 0.5) * z_end / n
                f = np.array([density(z, d95, soil, trunc) for z in zs])
                integral = float(f.sum() * z_end / n)
                if abs(integral - 1.0) > 1e-4:
                    bad += 1
                    print("selftest: integral %.6f d95 %.2f soil %.2f %s" % (integral, d95, soil, trunc))
                # density at the slip plane = soil depth
                fs = density(soil, d95, soil, trunc)
                if trunc == "module" and soil > d95 + 1e-12 and fs != 0.0:
                    bad += 1; print("selftest: module truncation should give 0 below z_r", d95, soil)
                if trunc == "soil_bottom" and fs <= 0.0:
                    bad += 1; print("selftest: soil_bottom should give a positive density", d95, soil)
    # 95 percent of the unbounded profile lies above d95
    d95 = 0.87; lnb = math.log(0.05) / (100 * d95)
    if abs((1 - math.exp(100 * d95 * lnb)) - 0.95) > 1e-12:
        bad += 1; print("selftest: D95 definition")
    # a very thin soil holds all roots: f -> 1/soil
    if abs(density(0.01, 3.0, 0.01, "soil_bottom") * 0.01 - 1.0) > 0.01:
        bad += 1; print("selftest: thin soil limit")
    return bad


def main():
    bad = selftest()
    if len(sys.argv) < 3:
        print("selftest violations:", bad)
        sys.exit(1 if bad else 0)
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

    years = sorted({m.group(1) for n in names for m in [re.search(r"/(\d{4})/output/treed_rootcohesion_parameters\.txt$", n)] if m})
    worst = 0.0; n_cells = 0; zero_density = 0; mode_seen = set()
    for y in years:
        pre = [n for n in names if "/%s/output/treed_rootcohesion_parameters.txt" % y in n][0].split("/%s/" % y)[0]
        par = dict((k.strip(), v.strip()) for k, v in (l.split("=", 1) for l in z.read("%s/%s/output/treed_rootcohesion_parameters.txt" % (pre, y)).decode().split("\n") if "=" in l))
        mode = par.get("root_reinforcement_mode", "hwang_mean")
        mode_seen.add(mode)
        if mode != "basal_profile":
            continue
        Tr = float(par["Tr_used_MPa"]); red = float(par["reduction_factor"]); rho = float(par["rho_root_kg_m3"])
        kp = float(par["root_k_prime"]); kdp = float(par["root_k_double_prime"]); trunc = par["root_profile_truncation"]
        fC = 0.47
        out = "%s/%s/output/" % (pre, y)
        rootC = asc(out + "treed_rootC_areanorm_gC_m2.asc")
        zr = asc(out + "treed_root_depth_m.asc")
        soil = asc("%s/%s/input/soildepth.asc" % (pre, y))
        coh = asc(out + "treed_rootcohesion_Hwang2015_kPa.asc")
        dens = asc(out + "treed_rootprofile_density_slip_per_m.asc")
        for r in range(coh.shape[0]):
            for c in range(coh.shape[1]):
                rc = rootC[r, c] if soil[r, c] > 1e-6 else 0.0
                f = density(soil[r, c], max(zr[r, c], 0.0), soil[r, c], trunc)
                v = red * kdp * kp * Tr * 1000.0 * (rc / (1000.0 * fC) / rho) * f if rc > 0 else 0.0
                d = abs(v - coh[r, c]); tol = 1e-5 + 1e-5 * abs(v)
                worst = max(worst, d)
                n_cells += 1
                if f == 0.0 and rc > 0:
                    zero_density += 1
                if d > tol:
                    bad += 1
                    if bad <= 10:
                        print("  year", y, "cell", r, c, "recomputed", v, "written", coh[r, c])
                if abs(f - dens[r, c]) > 1e-5 * max(1.0, f) and rc > 0:
                    bad += 1
                    if bad <= 10:
                        print("  year", y, "cell", r, c, "density recomputed", f, "written", dens[r, c])
    print("%s: modes %s, %d years, %d cell-years rebuilt, max abs deviation %.2e kPa, cell-years with no root at the slip plane %d, violations %d" % (
        label, sorted(mode_seen), len(years), n_cells, worst, zero_density, bad))
    sys.exit(1 if bad or not years or n_cells == 0 else 0)


main()
