#!/usr/bin/env python3
"""Native, unmodified OpenLISEM 7.5.2: 5cm/10cm + canopy + 2D erosion.
NOT a model endorsement. Generated maps and runs are synthetic.
This is deliberately on the prior OpenLISEM experiment branch.
"""
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
ORIGINAL = REPO / "openlisem_virtual_trial" / "generate_inputs.py"
assert ORIGINAL.is_file(), ORIGINAL

CASES = {
    "Oak_sprouts_sparse": (.40, 1.2, 1.8, .343, .12),
    "Miscanthus_dense": (.85, 3.0, 1.3, 1.551, .20),
}
def source_for_grid(n: int, dx: float) -> str:
    src = ORIGINAL.read_text(encoding="utf-8")
    assert src.count("R,C,DX=25,15,1.0") == 1
    src = src.replace("R,C,DX=25,15,1.0", f"R,C,DX={n},{n},{dx}")
    start = src.index("cases={")
    end = src.index("\ndef write_map", start)
    src = src[:start] + "cases=" + repr(CASES) + "\n" + src[end:]
    assert src.count("for intensity in (5,10,20):") == 2
    src = src.replace("for intensity in (5,10,20):", "for intensity in (20,):")
    assert src.count("001:0060  0") == 1
    assert src.count("001:0120  0") == 1
    src = src.replace("001:0060  0", "001:0010  0")
    src = src.replace("001:0120  0", "001:0015  0")
    assert src.count('"End time":"001:0120"') == 1
    src = src.replace('"End time":"001:0120"', '"End time":"001:0015"')
    assert src.count('"Timestep":"10"') == 1
    src = src.replace('"Timestep":"10"', '"Timestep":"1"')
    return src

all_runs = []
for resolution_cm, n, dx in ((10, 20, 0.10), (5, 40, 0.05)):
    base = ROOT / f"grid_{resolution_cm}cm"
    base.mkdir(parents=True, exist_ok=True)
    code = source_for_grid(n, dx)
    filename = base / "generator_from_prior_native_inputs.py"
    filename.write_text(code, encoding="utf8")
    scope = {"__name__": "__main__", "__file__": str(filename)}
    exec(compile(code, str(filename), "exec"), scope)
    run_dir = base / "runs"
    result_dir = base / "results"
    for p in sorted(run_dir.glob("*.run")):
        original = p.read_text(encoding="utf8")
        assert "Routing Kin Wave 2D=2" in original, p
        assert "Include Interception=1" in original, p
        assert "Include Erosion simulation=1" in original, p
        assert "End time=001:0015" in original, p
        assert "Timestep=1" in original, p
        for dt in (1, 2):
            label = f"{resolution_cm}cm_{p.stem}_dt{dt}"
            if dt == 1:
                text = original
            else:
                text = original.replace("Timestep=1", "Timestep=2")
            dest = result_dir / label
            dest.mkdir(parents=True, exist_ok=True)
            text = re.sub(r"(?m)^Result Directory=.*$",
                          lambda m: "Result Directory=" + str(dest.resolve()) + "\\",
                          text)
            # Preserve original runfile keys including native sediment controls.
            new = run_dir / (label + ".run")
            new.write_text(text, encoding="utf8")
            all_runs.append({"name": label, "resolution_cm": resolution_cm,
                             "dx_m": dx, "cells": n*n,
                             "storm_mm_h": 20, "storm_minutes": 10,
                             "end_minutes": 15, "user_dt_s": dt,
                             "runfile": str(new), "outdir": str(dest)})
        p.unlink()
manifest = {"code": "official unmodified 7.5.2 Windows lisem.exe",
            "not_the_Maggioli_2022_exact_binary": True,
            "not_a_published_5cm_dynamic_wave_precedent": True,
            "compare_fixed_2m_x_2m_domain": True,
            "cases": all_runs}
(ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf8")
with (ROOT / "runs.csv").open("w", encoding="utf8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(all_runs[0]))
    writer.writeheader()
    writer.writerows(all_runs)
print("NATIVE_CM_GENERATED", len(all_runs), "5/10cm actual PCRaster grid cases")
