#!/usr/bin/env python3
"""Independent verification of the v1.6 landslide-response runs.

Reads only the files written by the native runs (no model code is imported):

    COLLECTED/lorica-v16-<CONDITION>/run/...        (A, B, optional C runs)
    COLLECTED/lorica-v16-R_v15_regression/run/...    (v1.5 regression rerun)

and writes VERIFY_DIR/landslide_verification.json, recovery tables and a
short markdown summary. Every check is recomputed from the raw outputs.
"""
import csv
import json
import math
import sys
from pathlib import Path

COLLECTED = Path(sys.argv[1])
OUT = Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)
REPO = Path(__file__).resolve().parents[2]
REF = REPO / "lorica_treed/v1.6/reference"

checks = []


def check(name, ok, detail):
    status = "NOT_RUN" if ok is None else ("PASS" if ok else "FAIL")
    checks.append({"check": name, "status": status, "detail": detail})


def read_csv(p):
    with open(p, newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def fnum(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return float("nan")


def read_asc(p):
    lines = Path(p).read_text().splitlines()
    return [[float(v) for v in ln.split()] for ln in lines[6:] if ln.strip()]


def run_dir(cond):
    d = COLLECTED / ("lorica-v16-" + cond) / "run"
    return d if d.is_dir() else None


def mean(xs):
    xs = [x for x in xs if not math.isnan(x)]
    return sum(xs) / len(xs) if xs else float("nan")


# ---------------------------------------------------------------- regression
R = run_dir("R_v15_regression")
if R is not None and (R / "annual_state.csv").exists():
    new = read_csv(R / "annual_state.csv")
    ref = read_csv(REF / "v15_open30_beta2_annual_state.csv")
    n = min(len(new), 13)
    maxdiff = {}
    exact_rows = 0
    for i in range(n):
        same_row = True
        for k in ref[i].keys():
            if k not in new[i]:
                continue
            a, b = fnum(new[i][k]), fnum(ref[i][k])
            if math.isnan(a) and math.isnan(b):
                continue
            d = abs(a - b)
            maxdiff[k] = max(maxdiff.get(k, 0.0), d)
            if new[i][k] != ref[i][k]:
                same_row = False
        exact_rows += same_row
    worst = max(maxdiff.values()) if maxdiff else float("nan")
    check("R_v15_regression_annual_state_years_1_13_reproduced",
          n == 13 and worst <= 1e-12,
          {"years_compared": n, "bitwise_identical_rows": exact_rows, "max_abs_diff_any_column": worst,
           "max_abs_diff_by_column": {k: v for k, v in maxdiff.items() if v > 0}})
    # per-cell rasters of years 1-13
    refcells = read_csv(REF / "v15_open30_beta2_cells_years01_13.csv")
    names = ["TREED_FPC", "TREED_LAI", "TREED_rootC_gC_m2", "soil_depth_m", "dtm_m", "root_cohesion_kPa", "water_erosion_m"]
    worst_cell = {}
    for y in range(1, 14):
        yd = R / ("year_%02d" % y)
        if not yd.is_dir():
            continue
        grids = {nm: read_asc(yd / (nm + ".asc")) for nm in names}
        for row in refcells:
            if int(row["year"]) != y:
                continue
            r, c = int(row["row"]), int(row["col"])
            for nm in names:
                d = abs(grids[nm][r][c] - float(row[nm]))
                worst_cell[nm] = max(worst_cell.get(nm, 0.0), d)
    check("R_v15_regression_cell_rasters_years_1_13_reproduced",
          bool(worst_cell) and max(worst_cell.values()) <= 1e-12,
          {"max_abs_diff_by_raster": worst_cell})
else:
    check("R_v15_regression_present", None, "regression run not part of this workflow run")

# ---------------------------------------------------------------- A / B / C
conds = {}
names = ["A_no_landslide", "B_landslide_original"] + sorted(
    p.name[len("lorica-v16-"):] for p in COLLECTED.glob("lorica-v16-C_*") if p.is_dir())
for cond in names:
    d = run_dir(cond)
    if d is not None and (d / "annual_state.csv").exists():
        conds[cond] = {
            "dir": d,
            "annual": read_csv(d / "annual_state.csv"),
            "cells": read_csv(d / "cell_timeseries.csv"),
            "status": dict(l.split("=", 1) for l in (d / "run_status.txt").read_text().splitlines() if "=" in l)
            if (d / "run_status.txt").exists() else {},
        }

for cond, D in conds.items():
    an = D["annual"]
    mc = max(fnum(r["mass_closure"]) for r in an)
    sc = max(fnum(r["slide_stage_mass_closure"]) for r in an)
    ex = max(max(fnum(r["treed_input_DTM_error_m"]), fnum(r["treed_input_soildepth_error_m"])) for r in an)
    le = max(fnum(r["layer_depth_error_m"]) for r in an)
    check(cond + "_mass_closure_le_1e-6", mc <= 1e-6 and sc <= 1e-6,
          {"max_annual_export_adjusted_closure": mc, "max_slide_stage_closure": sc, "years": len(an)})
    check(cond + "_treed_exchange_le_5.1e-7_m", ex <= 5.1e-7, {"max_exchange_error_m": ex})
    check(cond + "_layer_depth_consistency_le_1e-5_m", le <= 1e-5, {"max_layer_depth_error_m": le})
    check(cond + "_native_run_status", D["status"].get("status") == "PASS", D["status"])

A = conds.get("A_no_landslide")
B = conds.get("B_landslide_original")
event_year = int(B["status"]["event_year"]) if B and "event_year" in B["status"] else None

if A:
    tot = sum(int(r["landslide_initiations"]) for r in A["annual"])
    check("A_has_no_landslide", tot == 0, {"total_initiations": tot})

if B and event_year:
    ev = [r for r in B["annual"] if int(r["year"]) == event_year][0]
    init = int(ev["landslide_initiations"])
    other = sum(int(r["landslide_initiations"]) for r in B["annual"] if int(r["year"]) != event_year)
    check("B_event_year_actual_native_initiation_1_to_6_cells", 1 <= init <= 6,
          {"event_year": event_year, "initiations": init, "eroded_cells": int(ev["slide_eroded_cells"]),
           "deposit_cells": int(ev["slide_deposit_cells"]), "erosion_sum_m": fnum(ev["landslide_erosion_sum_m"]),
           "deposition_sum_m": fnum(ev["landslide_deposition_sum_m"]),
           "persistent_after_kg": fnum(ev["persistent_after_kg"]), "initiations_other_years": other})

# A vs B identical before the slide
CELL_KEYS = ["input_dtm_m", "input_soildepth_m", "input_paw_mm", "raw_fpc", "raw_lai", "raw_rootC_gC_m2", "npp",
             "effective_fpc", "effective_rootC_gC_m2", "root_cohesion_kPa", "water_erosion_m", "water_deposition_m",
             "end_dtm_m", "end_soildepth_m", "ET_m"]
if A and B and event_year:
    def cell_index(D):
        return {(int(r["year"]), int(r["row"]), int(r["col"])): r for r in D["cells"]}
    ia, ib = cell_index(A), cell_index(B)
    pre_diff = 0.0
    for (y, r, c), ra in ia.items():
        if y >= event_year:
            continue
        rb = ib[(y, r, c)]
        for k in CELL_KEYS:
            pre_diff = max(pre_diff, abs(fnum(ra[k]) - fnum(rb[k])))
    check("A_B_identical_before_event_year_(tol_1e-9)", pre_diff <= 1e-9, {"max_abs_cell_difference": pre_diff})
    # TREED of the event year ran BEFORE the slide: raw outputs must still agree
    treed_keys = ["input_dtm_m", "input_soildepth_m", "input_paw_mm", "raw_fpc", "raw_lai", "raw_rootC_gC_m2", "npp",
                  "effective_fpc", "root_cohesion_kPa", "water_erosion_m"]
    ev_diff = 0.0
    for (y, r, c), ra in ia.items():
        if y != event_year:
            continue
        rb = ib[(y, r, c)]
        for k in treed_keys:
            ev_diff = max(ev_diff, abs(fnum(ra[k]) - fnum(rb[k])))
    check("event_year_TREED_and_water_erosion_identical_A_B_(TREED_precedes_slide,tol_1e-9)", ev_diff <= 1e-9,
          {"max_abs_cell_difference": ev_diff})
    # B pre-slide state equals A end-of-year state in the event year
    pd = 0.0
    for (y, r, c), rb in ib.items():
        if y != event_year:
            continue
        ra = ia[(y, r, c)]
        pd = max(pd, abs(fnum(rb["pre_slide_soildepth_m"]) - fnum(ra["end_soildepth_m"])))
    check("B_pre_slide_soil_equals_A_end_of_event_year", pd <= 1e-12, {"max_abs_diff_m": pd})
    # Restart SHA: identical up to and including event year
    sa = {int(r["year"]): r["traits_restart_sha256"] for r in A["annual"]}
    sb = {int(r["year"]): r["traits_restart_sha256"] for r in B["annual"]}
    same_until = max([y for y in sorted(sa) if all(sa[k] == sb.get(k) for k in range(1, y + 1))] or [0])
    first_diff = next((y for y in sorted(sa) if sa[y] != sb.get(y)), None)
    check("traits_restart_identical_through_event_year", same_until >= event_year,
          {"identical_through_year": same_until, "first_differing_year": first_diff})

    # ------------------------------------------------ recovery time series
    mask = {}
    for (y, r, c), rb in ib.items():
        if y == event_year:
            mask[(r, c)] = int(rb["event_mask"])
    groups = {"scar_only(1)": [k for k, v in mask.items() if v == 1],
              "deposit_only(2)": [k for k, v in mask.items() if v == 2],
              "scar_and_deposit(3)": [k for k, v in mask.items() if v == 3],
              "undisturbed(0)": [k for k, v in mask.items() if v == 0]}
    vars_ = ["input_soildepth_m", "input_paw_mm", "raw_fpc", "effective_fpc", "raw_lai", "raw_rootC_gC_m2",
             "effective_rootC_gC_m2", "root_cohesion_kPa", "npp", "water_erosion_m", "end_soildepth_m"]
    years = sorted({y for (y, _, _) in ib})
    rows = []
    for y in years:
        for g, cells in groups.items():
            if not cells:
                continue
            out = {"year": y, "years_since_event": y - event_year, "group": g, "n_cells": len(cells)}
            for v in vars_:
                b = mean([fnum(ib[(y, r, c)][v]) for r, c in cells])
                a = mean([fnum(ia[(y, r, c)][v]) for r, c in cells])
                out["B_" + v] = b
                out["A_" + v] = a
                out["BminusA_" + v] = b - a
            rows.append(out)
    with open(OUT / "recovery_by_group.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # per-cell B-A at key horizons
    horizons = [0, 1, 2, 3, 5, 10, 20, 30]
    cell_rows = []
    for h in horizons:
        y = event_year + h
        if y not in years:
            continue
        for (r, c), code in sorted(mask.items()):
            ra, rb = ia[(y, r, c)], ib[(y, r, c)]
            d = {"years_since_event": h, "year": y, "row": r, "col": c, "event_mask": code}
            for v in vars_:
                d["A_" + v] = fnum(ra[v])
                d["B_" + v] = fnum(rb[v])
            cell_rows.append(d)
    with open(OUT / "cells_at_horizons.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(cell_rows[0].keys()))
        w.writeheader()
        w.writerows(cell_rows)

    # Key diagnostics in the year after the slide
    y1 = event_year + 1
    disturbed = [k for k, v in mask.items() if v != 0]
    undist = [k for k, v in mask.items() if v == 0]
    def dmax(cells, v, y):
        return max([abs(fnum(ib[(y, r, c)][v]) - fnum(ia[(y, r, c)][v])) for r, c in cells] or [0.0])
    diag = {
        "event_year": event_year,
        "disturbed_cells": [list(k) + [mask[k]] for k in disturbed],
        "year_after": y1,
        "max_abs_BminusA_input_soildepth_disturbed": dmax(disturbed, "input_soildepth_m", y1),
        "max_abs_BminusA_input_paw_disturbed": dmax(disturbed, "input_paw_mm", y1),
        "max_abs_BminusA_raw_fpc_disturbed": dmax(disturbed, "raw_fpc", y1),
        "max_abs_BminusA_raw_fpc_undisturbed": dmax(undist, "raw_fpc", y1),
        "max_abs_BminusA_effective_fpc_disturbed": dmax(disturbed, "effective_fpc", y1),
        "max_abs_BminusA_raw_rootC_disturbed": dmax(disturbed, "raw_rootC_gC_m2", y1),
        "max_abs_BminusA_root_cohesion_disturbed": dmax(disturbed, "root_cohesion_kPa", y1),
    }
    soilfree_after = [list(k) for k in disturbed if fnum(ib[(y1, k[0], k[1])]["input_soildepth_m"]) <= 1e-6]
    diag["soilfree_cells_entering_year_after"] = soilfree_after
    check("year_after_event_TREED_receives_post_slide_soil_state",
          diag["max_abs_BminusA_input_soildepth_disturbed"] > 0.0, diag)

    # TREED restart traits
    ta = Path(A["dir"]) / "treed_restart_traits_by_cell.csv"
    tb = Path(B["dir"]) / "treed_restart_traits_by_cell.csv"
    TA = {(int(r["year"]), int(r["row"]), int(r["col"])): r for r in read_csv(ta)} if ta.exists() else {}
    TB = {(int(r["year"]), int(r["row"]), int(r["col"])): r for r in read_csv(tb)} if tb.exists() else {}
    if not TA or not TB:
        check("restart_traits_dumped", None, "treed_restart_traits_by_cell.csv missing or empty")
    else:
        fields = [k for k in next(iter(TA.values())).keys() if k not in ("year", "row", "col")]
        trait_rows = []
        for h in horizons:
            y = event_year + h
            for (r, c), code in sorted(mask.items()):
                if (y, r, c) not in TA:
                    continue
                d = {"years_since_event": h, "year": y, "row": r, "col": c, "event_mask": code}
                for fld in fields:
                    d["A_" + fld] = fnum(TA[(y, r, c)][fld])
                    d["B_" + fld] = fnum(TB[(y, r, c)][fld])
                trait_rows.append(d)
        if trait_rows:
            with open(OUT / "restart_traits_at_horizons.csv", "w", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=list(trait_rows[0].keys()))
                w.writeheader()
                w.writerows(trait_rows)
        check("restart_contains_only_trait_fields_no_disturbance_state",
              sorted(fields) == sorted(["H", "a_ll", "C_leaf", "seasonality", "r_s_r", "Tave_optim", "Tmax_optim",
                                        "Tmin_optim", "Pave_optim"]),
              {"fields": fields})

    # Water/sediment export after the event
    ea = sum(fnum(r["explicit_water_export_kg"]) for r in A["annual"] if int(r["year"]) > event_year)
    eb = sum(fnum(r["explicit_water_export_kg"]) for r in B["annual"] if int(r["year"]) > event_year)
    check("post_event_outlet_water_sediment_export_recorded", True,
          {"A_kg": ea, "B_kg": eb, "B_minus_A_kg": eb - ea})

# ---------------------------------------------------------------- C module
def cidx(D):
    return {(int(r["year"]), int(r["row"]), int(r["col"])): r for r in D["cells"]}
c_rows = []
for cname, D in conds.items():
    if not cname.startswith("C_"):
        continue
    ctype = D["status"].get("condition", "")
    ic = cidx(D)
    if ctype == "C_null_module_no_landslide" and A:
        ia = cidx(A)
        worst = max(abs(fnum(r[k]) - fnum(ia[key][k])) for key, r in ic.items() for k in CELL_KEYS)
        check(cname + "_module_on_without_landslide_reproduces_A_exactly", worst == 0.0,
              {"max_abs_cell_difference": worst})
    if ctype == "C_landslide_recovery_module" and B and event_year:
        ib = cidx(B)
        worst_pre = max([abs(fnum(r[k]) - fnum(ib[key][k])) for key, r in ic.items() if key[0] <= event_year
                         for k in CELL_KEYS] or [0.0])
        check(cname + "_identical_to_B_through_event_year", worst_pre == 0.0, {"max_abs_cell_difference": worst_pre})
        # undisturbed cells: C differs from B only through landscape feedback, record magnitude
        maskC = {(key[1], key[2]): int(r["event_mask"]) for key, r in ic.items() if key[0] == event_year}
        for y in sorted({k[0] for k in ic}):
            for g, sel in (("scar", lambda m: m in (1, 3)), ("deposit_only", lambda m: m == 2), ("undisturbed", lambda m: m == 0)):
                cells = [k for k, m in maskC.items() if sel(m)]
                if not cells:
                    continue
                row = {"run": cname, "year": y, "years_since_event": y - event_year, "group": g, "n": len(cells)}
                for v in ["raw_fpc", "effective_fpc", "raw_rootC_gC_m2", "effective_rootC_gC_m2", "root_cohesion_kPa",
                          "input_soildepth_m", "water_erosion_m", "end_soildepth_m"]:
                    row["C_" + v] = mean([fnum(ic[(y, r, c)][v]) for r, c in cells])
                    row["B_" + v] = mean([fnum(ib[(y, r, c)][v]) for r, c in cells])
                c_rows.append(row)
if c_rows:
    with open(OUT / "C_vs_B_by_group.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(c_rows[0].keys()))
        w.writeheader()
        w.writerows(c_rows)

summary = {"checks": checks,
           "n_pass": sum(c["status"] == "PASS" for c in checks),
           "n_fail": sum(c["status"] == "FAIL" for c in checks),
           "conditions_found": sorted(conds.keys()) + (["R_v15_regression"] if R is not None else []),
           "note": "Synthetic 5x5 open-scarp hillslope; not a Gounsa field validation."}
(OUT / "landslide_verification.json").write_text(json.dumps(summary, indent=2, default=str))
for c in checks:
    print(c["status"], c["check"])
print("PASS" if summary["n_fail"] == 0 else "FAIL", summary["n_pass"], "passed,", summary["n_fail"], "failed")
sys.exit(0 if summary["n_fail"] == 0 else 1)
