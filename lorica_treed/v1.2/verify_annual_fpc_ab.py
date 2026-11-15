#!/usr/bin/env python3
"""Compare two actual native every_timestep TREED-LORICA runs (beta=0 vs beta=2).

The sole treatment is the scalar erosion vegetation-protection coefficient.
K=1e-4 is an explicit sensitivity setting, not a field calibration.
'water_erosion_sum_m' sums cellwise positive erosion thicknesses; it is
not water/sediment mass or volume.
"""
import csv
import json
import math
import pathlib
import sys


def table(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def raster(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    meta = dict(line.split()[:2] for line in lines[:6])
    ncol, nrow = int(meta["ncols"]), int(meta["nrows"])
    data = [float(v) for line in lines[6:6+nrow] for v in line.split()]
    assert len(data) == ncol * nrow, (path, ncol, nrow, len(data))
    return data


def nearly(a, b, atol=1e-9, rtol=1e-9):
    return abs(a-b) <= atol + rtol * max(abs(a), abs(b))


def main(root, out):
    a = root / "lorica-v12-ab-beta0"
    b = root / "lorica-v12-ab-beta2"
    out.mkdir(parents=True, exist_ok=True)
    for name, dir_ in [("beta0", a), ("beta2", b)]:
        assert dir_.is_dir(), (name, dir_)
    A = table(a / "annual_state.csv")
    B = table(b / "annual_state.csv")
    assert len(A) == len(B) == 3, (len(A), len(B))
    compare_rows = []
    for i, (x, y) in enumerate(zip(A, B), 1):
        assert int(x["year"]) == int(y["year"]) == i
        for field in ("annual_precip_mm", "mean_temperature_C"):
            assert nearly(float(x[field]), float(y[field]), atol=0.0, rtol=0.0), (i, field)
        for row in (x, y):
            assert float(row["mass_closure"]) < 1e-6, (i, "mass", row["mass_closure"])
            assert float(row["treed_input_DTM_error_m"]) <= 5.1e-7
            assert float(row["treed_input_soildepth_error_m"]) <= 5.1e-7
            assert float(row["layer_depth_error_m"]) < 1e-5
        erosion_a = float(x["water_erosion_sum_m"])
        erosion_b = float(y["water_erosion_sum_m"])
        compare_rows.append(dict(
            year=i, FPC_beta0=x["FPC_mean"], FPC_beta2=y["FPC_mean"],
            runoff_beta0=x["runoff_sum_m"], runoff_beta2=y["runoff_sum_m"],
            water_erosion_beta0_m=erosion_a,
            water_erosion_beta2_m=erosion_b,
            water_erosion_reduction_pct=100*(1-erosion_b/erosion_a) if erosion_a > 0 else None,
            soil_depth_beta0_m=x["mean_soil_depth_m"],
            soil_depth_beta2_m=y["mean_soil_depth_m"],
            max_mass_closure=max(float(x["mass_closure"]), float(y["mass_closure"]))
        ))
    # Treatment must not change the first-year TREED vegetation and hydrology,
    # because the difference is solely in downstream sediment dynamics.
    for key in ("FPC_mean", "LAI_mean", "rootC_mean_gC_m2",
                "runoff_sum_m", "root_cohesion_mean_kPa"):
        assert nearly(float(A[0][key]),float(B[0][key]),atol=1e-7,rtol=1e-9), ("initial forcing not identical",key)
    assert float(A[0]["FPC_mean"]) > 0.01, "No actual vegetation in first year"
    assert float(B[0]["water_erosion_sum_m"]) < float(A[0]["water_erosion_sum_m"]) - 1e-10, (
        "No measurable reduction in first-year LORICA water erosion",
        A[0]["water_erosion_sum_m"], B[0]["water_erosion_sum_m"])
    first_fpc_0 = raster(a / "year_01" / "TREED_FPC.asc")
    first_fpc_2 = raster(b / "year_01" / "TREED_FPC.asc")
    assert all(nearly(x,y,atol=1e-7,rtol=1e-9) for x,y in zip(first_fpc_0,first_fpc_2)), "First year TREED FPC fields differ"
    first_ero_a = raster(a / "year_01" / "water_erosion_m.asc")
    first_ero_b = raster(b / "year_01" / "water_erosion_m.asc")
    changed_cells = sum(abs(x-y)>1e-10 for x,y in zip(first_ero_a,first_ero_b))
    assert changed_cells > 0, "No change in real per-cell erosion raster"
    for d in (a, b):
        layers = table(d/"soil_layers.csv")
        assert len(layers) == 3*5*5*10, len(layers)
        audit = table(d/"TREED_driver_audit.csv")
        assert len(audit) == 3 and audit[0]["restart_present_before"] == "false"
        assert all(x["restart_present_after"] == "true" for x in audit)
        assert all(x["restart_present_before"] == "true" for x in audit[1:])
        assert (d/"LORICA_TREED_V1_2_ANNUAL_SENSITIVITY_PASS.txt").is_file()
    audits = [table(d/"TREED_driver_audit.csv") for d in (a,b)]
    assert [x["seed"] for x in audits[0]] == [x["seed"] for x in audits[1]], "TREED seeds mismatch"

    with (out/"annual_fpc_ab_comparison.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(compare_rows[0]))
        w.writeheader()
        w.writerows(compare_rows)
    info = {
        "status": "PASS",
        "years":3,
        "grid":"5x5 @ 10 m; original synthetic convergent case",
        "test_scope":"Actual patched LORICA every_timestep with annual TREED Julia coupling",
        "only_treatment":"bio_protection_configured beta=0 versus beta=2",
        "controlled_erodibility_K":0.0001,
        "first_year_FPC_mean":float(A[0]["FPC_mean"]),
        "year1_erosion_beta0_sum_thickness_m":float(A[0]["water_erosion_sum_m"]),
        "year1_erosion_beta2_sum_thickness_m":float(B[0]["water_erosion_sum_m"]),
        "year1_reduction_pct":compare_rows[0]["water_erosion_reduction_pct"],
        "year1_changed_erosion_cells":changed_cells,
        "total_erosion_beta0_sum_thickness_m":sum(float(x["water_erosion_sum_m"]) for x in A),
        "total_erosion_beta2_sum_thickness_m":sum(float(x["water_erosion_sum_m"]) for x in B),
        "max_mass_closure":max(float(x["mass_closure"]) for x in A+B),
        "caveats":["K=1e-4 selected for sensitivity, not empirical calibration",
                   "Erosion metric sums cellwise thickness: not mass or volume",
                   "Synthetic 5x5 domain and 3-year validation only",
                   "Not a 30-year treatment evaluation or field prediction"]
    }
    (out/"annual_fpc_ab_verification.json").write_text(json.dumps(info,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps(info,indent=2))
    print("GOUNSA_LORICA_V12_ANNUAL_FPC_AB_PASS")


if __name__ == "__main__":
    main(pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]))
