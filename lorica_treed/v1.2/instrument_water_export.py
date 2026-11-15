#!/usr/bin/env python3
"""Expose LORICA's existing daily sediment boundary export as a diagnostic field.

This does not change runoff, erosion, routing, transport, deposition, root
cohesion or mass fluxes. It only copies the existing local mass_export ledger
into a stable class field for annual LORICA-TREED conservation diagnostics.
Run after apply_v11_formula_patch.py.
"""
from pathlib import Path
import sys

ROOT = Path(sys.argv[1])
cp = ROOT / "LORICA/Functions/treed_coupling.cs"
text = cp.read_text(encoding="utf-8-sig")
anchor = "        bool treed_refresh_ks_each_year = false;"
if text.count(anchor) != 1:
    raise RuntimeError("Cannot uniquely locate TREED annual field anchor")
text = text.replace(anchor, anchor + """
        // v1.2 mass audit only: mass exported by daily water sediment routing
        // (kg), as already calculated in LORICA geomorph.cs's mass_export.
        double treed_water_sediment_export_kg = 0.0;""", 1)
cp.write_text(text, encoding="utf-8")

geo = ROOT / "LORICA/Functions/geomorph.cs"
src = geo.read_text(encoding="utf-8-sig")
start = src.find("        void calculate_water_ero_sed_daily()")
end = src.find("        void calculate_water_ero_sed()", start)
if start < 0 or end < 0:
    raise RuntimeError("Could not locate complete original daily erosion method")
piece = src[start:end]
init = "Decimal mass_before = total_catchment_mass_decimal(), mass_after, mass_export = 0;"
if piece.count(init) != 1:
    raise RuntimeError("Expected one water mass_export initializer")
piece = piece.replace(init, init + """
            treed_water_sediment_export_kg = 0.0;""", 1)
record = "mass_after = total_catchment_mass_decimal();"
if piece.count(record) != 1:
    raise RuntimeError("Expected exactly one daily erosion mass_after statement")
piece = piece.replace(record, """
                // Audit the already-computed local sediment export before the
                // transient transport arrays are later reused by landsliding.
                treed_water_sediment_export_kg = (double)mass_export;
                mass_after = total_catchment_mass_decimal();""", 1)
src=src[:start]+piece+src[end:]
geo.write_text(src,encoding="utf-8")
print("LORICA_DAILY_WATER_EXPORT_INSTRUMENTED_NO_PHYSICS_CHANGE")
