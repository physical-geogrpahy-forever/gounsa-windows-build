#!/usr/bin/env python3
"""Independent re-check of the v1.6 report numbers from raw committed files.
Uses only ASC rasters, annual_state.csv, ledgers, jld2 bytes and the
user's original v1.5 artifact. Does not import the v1.6 verifier.

Inputs: ./res = clone of branch lorica-treed-v1.6-landslide-recovery-results;
BUNDLE_B2 = unzipped gounsa_v15_open30_beta2.zip (from the handoff bundle,
sha256 3257ad9a...6dfd13). Run: python3 recheck.py > recheck.json"""
import csv, hashlib, json, math, sys
from pathlib import Path

RES = Path("res/runs")
AB = RES / "43790582202_ab"
CC = RES / "43795357866_c"
BUNDLE_B2 = Path("/home/claude/bundle/pkg/b2")
out = {}


def asc(p):
    L = Path(p).read_text().splitlines()
    return [[float(v) for v in l.split()] for l in L[6:] if l.strip()]


def rcsv(p):
    with open(p, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def run(cond):
    base = AB if cond in ("A_no_landslide", "B_landslide_original", "R_v15_regression") else CC
    return base / ("lorica-v16-" + cond) / "run"


A, B = run("A_no_landslide"), run("B_landslide_original")
C4, C8, C0 = run("C_rec_tau4_k032"), run("C_rec_tau8_k018"), run("C_null_module_no_landslide")
R = run("R_v15_regression")
Y = lambda d, y: d / ("year_%02d" % y)
EY = 4

# 1. event table from pre/post ASC
pre = {k: asc(Y(B, EY) / "pre_slide" / (k + ".asc")) for k in ["soildepth_m", "crrain_m_d", "root_cohesion_kPa", "effective_fpc_lorica", "soil_mass_kg"]}
post = {k: asc(Y(B, EY) / "post_slide" / (k + ".asc")) for k in ["soildepth_m", "ero_slid_m", "sed_slid_m", "paw_mm", "soil_mass_kg", "persistent_landslide_mass_kg", "transient_transport_mass_kg"]}
ev = []
for r in range(5):
    for c in range(5):
        if post["ero_slid_m"][r][c] < -1e-12 or post["sed_slid_m"][r][c] > 1e-12:
            ev.append({"cell": (r, c), "pre_sd": pre["soildepth_m"][r][c], "post_sd": post["soildepth_m"][r][c],
                       "ero": post["ero_slid_m"][r][c], "sed": post["sed_slid_m"][r][c], "crr": pre["crrain_m_d"][r][c],
                       "Cr": pre["root_cohesion_kPa"][r][c], "effF": pre["effective_fpc_lorica"][r][c], "paw": post["paw_mm"][r][c]})
out["event_cells"] = ev
out["event_soil_mass_pre_post"] = (sum(map(sum, pre["soil_mass_kg"])), sum(map(sum, post["soil_mass_kg"])),
                                   sum(map(sum, post["persistent_landslide_mass_kg"])), sum(map(sum, post["transient_transport_mass_kg"])))

# 2. annual closures and initiations
ann = {}
for nm, d in [("A", A), ("B", B), ("C4", C4), ("C8", C8), ("C0", C0)]:
    ann[nm] = {int(r["year"]): r for r in rcsv(d / "annual_state.csv")}
out["max_mass_closure"] = {nm: max(float(r["mass_closure"]) for r in D.values()) for nm, D in ann.items()}
out["max_exchange_err"] = {nm: max(max(float(r["treed_input_DTM_error_m"]), float(r["treed_input_soildepth_error_m"])) for r in D.values()) for nm, D in ann.items()}
out["initiations_by_year_nonzero"] = {nm: {y: r["landslide_initiations"] for y, r in D.items() if r["landslide_initiations"] != "0"} for nm, D in ann.items()}
out["years"] = {nm: len(D) for nm, D in ann.items()}

# 3. byte-level raster identity
RASTERS = ["TREED_FPC", "TREED_LAI", "TREED_rootC_gC_m2", "TREED_NPP", "TREED_effective_FPC", "TREED_effective_rootC_gC_m2",
           "TREED_input_PAW_mm", "TREED_input_soil_depth_m", "root_cohesion_kPa", "water_erosion_m", "soil_depth_m", "dtm_m"]
def same_bytes(d1, d2, y, names):
    return [n for n in names if (Y(d1, y) / (n + ".asc")).read_bytes() != (Y(d2, y) / (n + ".asc")).read_bytes()]
out["A_vs_B_diff_rasters_by_year"] = {y: same_bytes(A, B, y, RASTERS) for y in range(1, 7)}
treed_ev = ["TREED_FPC", "TREED_LAI", "TREED_rootC_gC_m2", "TREED_NPP", "TREED_input_PAW_mm", "TREED_input_soil_depth_m", "root_cohesion_kPa", "water_erosion_m"]
out["event_year_A_vs_B_TREED_diffs"] = same_bytes(A, B, EY, treed_ev)
out["C0_vs_A_any_diff"] = sorted({(y, n) for y in range(1, 35) for n in same_bytes(C0, A, y, RASTERS)})
out["C4_vs_B_diff_upto_event"] = sorted({(y, n) for y in range(1, EY + 1) for n in same_bytes(C4, B, y, RASTERS)})
out["C8_vs_B_diff_upto_event"] = sorted({(y, n) for y in range(1, EY + 1) for n in same_bytes(C8, B, y, RASTERS)})
apre = asc(Y(A, EY) / "soil_depth_m.asc")
out["B_pre_slide_vs_A_end_soil_maxdiff"] = max(abs(apre[r][c] - pre["soildepth_m"][r][c]) for r in range(5) for c in range(5))

# 4. restart hashes from the actual jld2 bytes
h = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
first = None
for y in range(1, 35):
    if h(Y(A, y) / "traits_restart.jld2") != h(Y(B, y) / "traits_restart.jld2"):
        first = y; break
out["restart_first_differing_year"] = first
out["restart_sha_matches_annual_csv"] = all(h(Y(B, y) / "traits_restart.jld2") == ann["B"][y]["traits_restart_sha256"] for y in range(1, 35))

# 5. year-after input differences
def g(d, y, n): return asc(Y(d, y) / (n + ".asc"))
dis = [e["cell"] for e in ev]
und = [(r, c) for r in range(5) for c in range(5) if (r, c) not in dis]
out["y5_max_dsoil"] = max(abs(g(B, 5, "TREED_input_soil_depth_m")[r][c] - g(A, 5, "TREED_input_soil_depth_m")[r][c]) for r, c in dis)
out["y5_max_dpaw"] = max(abs(g(B, 5, "TREED_input_PAW_mm")[r][c] - g(A, 5, "TREED_input_PAW_mm")[r][c]) for r, c in dis)

# 6. horizon tables from ASC
groups = {"partial": [(1, 1), (1, 3)], "full": [(1, 2)], "deposit": [(2, 1), (2, 2), (2, 3)]}
H = [0, 1, 2, 3, 5, 10, 20, 30]
hz = {}
for gname, cells in groups.items():
    for var in ["TREED_effective_FPC", "root_cohesion_kPa", "TREED_FPC"]:
        for nm, d in [("A", A), ("B", B), ("C4", C4), ("C8", C8)]:
            hz[f"{gname}|{var}|{nm}"] = [round(sum(g(d, EY + k, var)[r][c] for r, c in cells) / len(cells), 3) for k in H]
out["horizons"] = hz

# 7. B-A mean deltas yrs 5-34
dl = {}
for cell in dis:
    for var in ["TREED_FPC", "TREED_LAI", "TREED_rootC_gC_m2", "TREED_NPP"]:
        d = [g(B, y, var)[cell[0]][cell[1]] - g(A, y, var)[cell[0]][cell[1]] for y in range(5, 35)]
        base = [g(A, y, var)[cell[0]][cell[1]] for y in range(5, 35)]
        dl[f"{cell}|{var}"] = (round(sum(d) / len(d), 4), round(100 * sum(d) / sum(base), 2))
    dl[f"{cell}|dPAW"] = round(g(B, 6, "TREED_input_PAW_mm")[cell[0]][cell[1]] - g(A, 6, "TREED_input_PAW_mm")[cell[0]][cell[1]], 1)
out["delta_means"] = dl
out["undisturbed_max_dFPC"] = max(abs(g(B, y, "TREED_FPC")[r][c] - g(A, y, "TREED_FPC")[r][c]) for y in range(1, 35) for r, c in und)
out["undisturbed_max_dPAW"] = max(abs(g(B, y, "TREED_input_PAW_mm")[r][c] - g(A, y, "TREED_input_PAW_mm")[r][c]) for y in range(1, 35) for r, c in und)
out["full_cell_rawFPC_range_B_y5_34"] = (min(g(B, y, "TREED_FPC")[1][2] for y in range(5, 35)), max(g(B, y, "TREED_FPC")[1][2] for y in range(5, 35)))

# 8. exports
out["post_event_export_kg"] = {nm: round(sum(float(D[y]["explicit_water_export_kg"]) for y in range(EY + 1, 35)), 3) for nm, D in ann.items()}

# 9. restart traits dump
TA = {(int(r["year"]), int(r["row"]), int(r["col"])): r for r in rcsv(CC / "lorica-v16-dump-ab/A_no_landslide/treed_restart_traits_by_cell.csv")}
TB = {(int(r["year"]), int(r["row"]), int(r["col"])): r for r in rcsv(CC / "lorica-v16-dump-ab/B_landslide_original/treed_restart_traits_by_cell.csv")}
out["trait_fields"] = [k for k in next(iter(TA.values())) if k not in ("year", "row", "col")]
out["H_full_cell"] = {y: (TA[(y, 1, 2)]["H"], TB[(y, 1, 2)]["H"]) for y in (4, 5, 6, 34)}
out["Cleaf_full_cell_y34"] = (TA[(34, 1, 2)]["C_leaf"], TB[(34, 1, 2)]["C_leaf"])
out["H_full_cell_B_range_y5_34"] = (min(float(TB[(y, 1, 2)]["H"]) for y in range(5, 35)), max(float(TB[(y, 1, 2)]["H"]) for y in range(5, 35)))

# 10. regression vs the user's ORIGINAL v1.5 beta2 artifact (not the repo copy)
rr = {int(r["year"]): r for r in rcsv(R / "annual_state.csv")}
orig = {int(r["year"]): r for r in rcsv(BUNDLE_B2 / "annual_state.csv")}
out["R_rows_identical_to_original_artifact"] = sum(rr[y] == orig[y] for y in range(1, 14))
bad = []
for y in range(1, 14):
    for n in ["TREED_FPC", "TREED_LAI", "TREED_rootC_gC_m2", "soil_depth_m", "dtm_m", "root_cohesion_kPa", "water_erosion_m", "TREED_effective_FPC", "ET_m", "Ks_topsoil_m_h"]:
        if (Y(R, y) / (n + ".asc")).read_bytes() != (BUNDLE_B2 / ("year_%02d" % y) / (n + ".asc")).read_bytes():
            bad.append((y, n))
    if h(Y(R, y) / "traits_restart.jld2") != h(BUNDLE_B2 / ("year_%02d" % y) / "traits_restart.jld2"):
        bad.append((y, "traits_restart.jld2"))
out["R_vs_original_byte_mismatches"] = bad

# 11. probes
p1 = rcsv(RES / "43789221109_probe/probe_summary.csv")
p2 = rcsv(RES / "43790023979_probe/probe_summary.csv")
out["probe1_runs_fail"] = (len(p1), sum(r["status"] != "PASS" for r in p1))
out["probe2_runs_fail"] = (len(p2), sum(r["status"] != "PASS" for r in p2))
le38 = [r for r in p1 if r["family"] != "v15_open_hillslope" and float(r["scarp_deg"]) <= 38]
out["probe1_le38_all_stable"] = all(r["n_always_stable"] == "25" for r in le38)
fin = [float(r["min_finite_crrain_m_d"]) for r in p1 if r["min_finite_crrain_m_d"] not in ("NaN", "") and 40 <= float(r["scarp_deg"]) <= 50]
out["probe1_40_50_min_finite_crrain_range"] = (min(fin), max(fin))
by = {}
for r in p1:
    by.setdefault(r["dem_id"], set()).add((r["initiations"], r["erosion_sum_m"], r["deposition_sum_m"]))
out["probe1_dems_where_storm_changed_outcome"] = [k for k, v in by.items() if len(v) > 1]
out["probe2_hollow_36_42_46"] = [(r["dem_id"], r["storm_mm_6h"], r["initiations"], r["min_finite_crrain_m_d"]) for r in p2 if "36_42_46" in r["dem_id"]]
cells2 = rcsv(RES / "43790023979_probe/probe_cells.csv")
out["probe_cells_columns_ok"] = "crrain_m_d" in cells2[0]
print(json.dumps(out, indent=1, default=str))
