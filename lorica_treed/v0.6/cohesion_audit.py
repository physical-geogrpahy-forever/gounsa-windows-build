#!/usr/bin/env python3
import csv
import math
import pathlib
import sys

# LORICA-TREED v0.6 cohesion audit.
# This script does NOT alter the coupled model. It diagnoses the consequence of
# applying Hwang et al. (2015) Eq. (5) to TREED area-normalized root carbon.

K_HWANG = 1.2
RHO_ROOT_KG_M3 = 435.3
ROOT_C_FRACTION = 0.47

# Literature comparison anchors.
# Kim et al. (KSFE-FETEC 2025): reduction-corrected Wu-model cohesion after
# comparison with direct-shear tests.
COHESION_TARGETS_KPA = {
    "Korea2025_Larix_kaempferi": 4.3,
    "Korea2025_Pinus_densiflora": 9.0,
    "Korea2025_Pinus_koraiensis": 9.1,
    "Korea2025_Quercus_mongolica": 12.9,
    # Hwang et al. (2015) spatially uniform Wu-method comparison case.
    "Hwang2015_uniform_Wu_comparison": 21.6,
}

TR_OH2011_PINUS_DENSIFLORA_MPA = 176.25 * 0.0980665
TR_KIM2025_PINUS_DENSIFLORA_MPA = 15.9
# Hales & Miniat (2017): 40% decline in tensile strength between 20-40%
# and 80-100% root moisture, across their laboratory species.
WET_STRENGTH_RETAINED_FRACTION = 0.60
# Kim et al. (2025): Wu-model cohesion was 1.5-5.1 times direct shear.
WU_REDUCTION_MIN = 1.0 / 5.1
WU_REDUCTION_MAX = 1.0 / 1.5


def read_esri_ascii(path):
    lines = pathlib.Path(path).read_text(encoding="utf-8").strip().splitlines()
    if len(lines) < 7:
        raise ValueError(f"Invalid ESRI ASCII: {path}")
    nodata = -9999.0
    for line in lines[:6]:
        p = line.split()
        if p and p[0].lower() == "nodata_value":
            nodata = float(p[-1])
    vals = []
    for line in lines[6:]:
        for token in line.split():
            v = float(token)
            if v != nodata and math.isfinite(v):
                vals.append(v)
    if not vals:
        raise ValueError("No valid root-carbon cells")
    return vals


def hwang_cr_kpa(root_c_gc_m2, tr_mpa, reduction=1.0):
    br = root_c_gc_m2 / (1000.0 * ROOT_C_FRACTION)
    return K_HWANG * (tr_mpa * 1.0e6) * (br / RHO_ROOT_KG_M3) / 1000.0 * reduction


def required_effective_tr_mpa(root_c_gc_m2, target_cr_kpa):
    br = root_c_gc_m2 / (1000.0 * ROOT_C_FRACTION)
    return target_cr_kpa * 1000.0 * RHO_ROOT_KG_M3 / (K_HWANG * br) / 1.0e6


def main(rootc_path, out_csv, out_txt):
    vals = read_esri_ascii(rootc_path)
    mean_rootc = sum(vals) / len(vals)
    mean_br = mean_rootc / (1000.0 * ROOT_C_FRACTION)

    rows = []

    for label, tr in [
        ("diagnostic_Oh2011_Pinus_densiflora_mean", TR_OH2011_PINUS_DENSIFLORA_MPA),
        ("diagnostic_Kim2025_Pinus_densiflora_mean", TR_KIM2025_PINUS_DENSIFLORA_MPA),
    ]:
        cr = hwang_cr_kpa(mean_rootc, tr)
        rows.append([label, "", tr, 1.0, cr, cr / 21.6])

    wet_tr = TR_KIM2025_PINUS_DENSIFLORA_MPA * WET_STRENGTH_RETAINED_FRACTION
    for reduction, label in [
        (WU_REDUCTION_MIN, "wet40pct_plus_Korea2025_inverse5p1"),
        (WU_REDUCTION_MAX, "wet40pct_plus_Korea2025_inverse1p5"),
    ]:
        cr = hwang_cr_kpa(mean_rootc, wet_tr, reduction)
        rows.append([label, "", wet_tr, reduction, cr, cr / 21.6])

    raw_kim = hwang_cr_kpa(mean_rootc, TR_KIM2025_PINUS_DENSIFLORA_MPA)
    for name, target in COHESION_TARGETS_KPA.items():
        tr_eff = required_effective_tr_mpa(mean_rootc, target)
        combined_scale = target / raw_kim
        rows.append([name, target, tr_eff, combined_scale, target, target / 21.6])

    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([
            "case",
            "target_Cr_kPa",
            "effective_Tr_MPa",
            "combined_scale_vs_Kim2025_raw15p9",
            "result_Cr_kPa",
            "ratio_to_Hwang21p6",
        ])
        w.writerows(rows)

    summary = [
        "LORICA-TREED v0.6 COHESION AUDIT",
        f"n_cells={len(vals)}",
        f"mean_rootC_gC_m2={mean_rootc:.9f}",
        f"mean_root_biomass_kgDM_m2={mean_br:.9f}",
        f"raw_Cr_Oh2011_17p284MPa_kPa={hwang_cr_kpa(mean_rootc, TR_OH2011_PINUS_DENSIFLORA_MPA):.9f}",
        f"raw_Cr_Kim2025_15p9MPa_kPa={raw_kim:.9f}",
        f"wet40pct_inverse5p1_Cr_kPa={hwang_cr_kpa(mean_rootc, wet_tr, WU_REDUCTION_MIN):.9f}",
        f"wet40pct_inverse1p5_Cr_kPa={hwang_cr_kpa(mean_rootc, wet_tr, WU_REDUCTION_MAX):.9f}",
        f"effective_Tr_for_Pinus_densiflora_9kPa_MPa={required_effective_tr_mpa(mean_rootc, 9.0):.9f}",
        "NOTE=Audit only; no value is automatically written back into LORICA-TREED.",
    ]
    pathlib.Path(out_txt).write_text("\n".join(summary) + "\n", encoding="utf-8")

    print("\n".join(summary))
    for row in rows:
        print(",".join(map(str, row)))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit("usage: cohesion_audit.py ROOTC_ASC OUT_CSV OUT_TXT")
    main(sys.argv[1], sys.argv[2], sys.argv[3])
