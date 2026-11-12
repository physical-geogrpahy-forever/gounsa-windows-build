#!/usr/bin/env python3
"""
Generate an explicit event-scale Hwang root-cohesion calibration for LORICA-TREED.

This utility does not modify the model equations and does not recalibrate each
scenario. It takes ONE baseline TREED root-C raster, ONE literature cohesion
benchmark, and ONE template coupling cfg; it writes a new cfg with a fixed
manual effective tensile strength (Tr_eff). Reuse that generated cfg (or its
Tr_eff) across the scenario matrix.
"""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

PROFILES_KPA = {
    # Hales et al. (2009), Coweeta Hydrologic Laboratory, vertically integrated means.
    "hales2009_fbm_mean": 3.4,
    "hales2009_wu_mean": 7.6,
    # Kim et al. (KSFE-FETEC 2025), reduction-corrected Wu estimates after
    # comparison with direct shear for major Korean tree species.
    "korea2025_larix_kaempferi": 4.3,
    "korea2025_pinus_densiflora": 9.0,
    "korea2025_pinus_koraiensis": 9.1,
    "korea2025_quercus_mongolica": 12.9,
}

DEFAULT_FC = 0.47
DEFAULT_RHO = 435.3
DEFAULT_K = 1.2


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read_cfg(path):
    text = Path(path).read_text(encoding="utf-8")
    cfg = {}
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or "=" not in s:
            continue
        k, v = s.split("=", 1)
        cfg[k.strip()] = v.strip()
    return text, cfg


def cfg_float(cfg, key, default):
    try:
        return float(cfg.get(key, default))
    except Exception:
        return float(default)


def read_esri_ascii(path):
    lines = Path(path).read_text(encoding="utf-8").strip().splitlines()
    if len(lines) < 7:
        raise ValueError("Invalid ESRI ASCII raster")
    nodata = -9999.0
    for line in lines[:6]:
        p = line.split()
        if p and p[0].lower() == "nodata_value":
            nodata = float(p[-1])
    vals = []
    for line in lines[6:]:
        for tok in line.split():
            v = float(tok)
            if math.isfinite(v) and v != nodata:
                vals.append(v)
    if not vals:
        raise ValueError("No valid root-C cells")
    return vals


def target_from_args(profile, manual_target):
    if profile == "manual":
        if manual_target is None or manual_target <= 0:
            raise ValueError("--manual-target-kpa must be >0 with profile=manual")
        return float(manual_target), "manual"
    if profile not in PROFILES_KPA:
        raise ValueError("Unknown profile: " + profile)
    return PROFILES_KPA[profile], profile


def effective_tr_mpa(mean_rootc_gc_m2, target_cr_kpa, f_c, rho_root, k_hwang):
    mean_br = mean_rootc_gc_m2 / (1000.0 * f_c)
    if mean_br <= 0 or rho_root <= 0 or k_hwang <= 0:
        raise ValueError("Invalid baseline biomass or Hwang constants")
    return target_cr_kpa * 1000.0 * rho_root / (k_hwang * mean_br) / 1.0e6


def replace_or_append(text, key, value):
    lines = text.splitlines()
    prefix = key + "="
    found = False
    out = []
    for line in lines:
        if line.strip().startswith(prefix):
            out.append(prefix + str(value))
            found = True
        else:
            out.append(line)
    if not found:
        out.append(prefix + str(value))
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("baseline_rootc_asc")
    ap.add_argument("template_cfg")
    ap.add_argument("profile", choices=sorted(list(PROFILES_KPA) + ["manual"]))
    ap.add_argument("output_cfg")
    ap.add_argument("output_json")
    ap.add_argument("--manual-target-kpa", type=float, default=None)
    args = ap.parse_args()

    cfg_text, cfg = read_cfg(args.template_cfg)
    vals = read_esri_ascii(args.baseline_rootc_asc)
    mean_rootc = sum(vals) / len(vals)

    f_c = cfg_float(cfg, "hwang_root_carbon_fraction", DEFAULT_FC)
    rho = cfg_float(cfg, "hwang_root_density_kg_m3", DEFAULT_RHO)
    k = cfg_float(cfg, "hwang_K_m_inv", DEFAULT_K)
    if f_c <= 0:
        raise ValueError("hwang_root_carbon_fraction must be >0")

    target, source_profile = target_from_args(args.profile, args.manual_target_kpa)
    tr_eff = effective_tr_mpa(mean_rootc, target, f_c, rho, k)
    mean_br = mean_rootc / (1000.0 * f_c)

    header = (
        "# EVENT-SCALE ROOT COHESION CALIBRATION -- GENERATED, NOT MEASURED Tr\n"
        "# baseline_rootC_sha256=" + sha256(args.baseline_rootc_asc) + "\n"
        "# template_cfg_sha256=" + sha256(args.template_cfg) + "\n"
        "# calibration_profile=" + source_profile + "\n"
        "# target_mean_root_cohesion_kPa=" + format(target, ".12g") + "\n"
        "# baseline_mean_rootC_gC_m2=" + format(mean_rootc, ".12g") + "\n"
        "# baseline_mean_root_biomass_kgDM_m2=" + format(mean_br, ".12g") + "\n"
        "# inferred_effective_event_Tr_MPa=" + format(tr_eff, ".12g") + "\n"
        "# Reuse this fixed Tr_eff across scenarios; do NOT recalibrate each scenario.\n\n"
    )

    out = cfg_text
    out = replace_or_append(out, "hwang_root_tensile_profile", "manual")
    out = replace_or_append(out, "hwang_root_tensile_strength_MPa", format(tr_eff, ".15g"))
    out = replace_or_append(out, "hwang_root_cohesion_reduction_factor", "1.0")
    out = replace_or_append(out, "hwang_root_cohesion_multiplier", "1.0")
    Path(args.output_cfg).write_text(header + out, encoding="utf-8")

    # Verify algebraically that the generated Tr returns the requested mean Cr.
    reconstructed = k * (tr_eff * 1.0e6) * (mean_br / rho) / 1000.0
    record = {
        "mode": "baseline_target_cohesion_to_fixed_event_Tr",
        "profile": source_profile,
        "target_mean_root_cohesion_kPa": target,
        "baseline_cells": len(vals),
        "baseline_mean_rootC_gC_m2": mean_rootc,
        "baseline_mean_root_biomass_kgDM_m2": mean_br,
        "hwang_root_carbon_fraction": f_c,
        "hwang_root_density_kg_m3": rho,
        "hwang_K_m_inv": k,
        "effective_event_Tr_MPa": tr_eff,
        "reconstructed_mean_root_cohesion_kPa": reconstructed,
        "baseline_rootC_sha256": sha256(args.baseline_rootc_asc),
        "template_cfg_sha256": sha256(args.template_cfg),
        "warning": "Tr_eff is an inverse-calibration parameter, not a measured tensile strength.",
    }
    Path(args.output_json).write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
