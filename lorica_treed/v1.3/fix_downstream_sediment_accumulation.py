#!/usr/bin/env python3
"""Fix one audited sediment routing mass-loss bug in native daily LORICA.

The deposition branch previously overwrote the downstream receiver's mineral
sediment in transport via '='. It must add the newly routed flux via '+='
because multiple upstream contributors can share the same receiver.
No erosion capacity, vegetation protection, transport exponent, hillslope
routing, hydrology or TREED equations are altered.
Run after v1.1 formula patch and v1.2 export instrumentation.
"""
from pathlib import Path
import sys

root=Path(sys.argv[1])
p=root/"LORICA/Functions/geomorph.cs"
s=p.read_text(encoding="utf-8")
start=s.find("        void calculate_sediment_dynamics(")
end=s.find("        void calculate_water_ero_sed_daily()",start)
if start<0 or end<0 or end<=start:
    raise RuntimeError("Cannot locate daily sediment dynamics function")
part=s[start:end]
old="sediment_in_transport_kg[row_sd + i_sd, col_sd + j_sd, size] = potential_transported_amount_kg;"
new="""// v1.3 conservation fix: accumulate incoming transport from all
                        // donors instead of erasing sediment already received.
                        sediment_in_transport_kg[row_sd + i_sd, col_sd + j_sd, size] += potential_transported_amount_kg;"""
if part.count(old)!=1:
    raise RuntimeError(f"Expected exactly one destructive downstream assignment; found {part.count(old)}")
part=part.replace(old,new,1)
p.write_text(s[:start]+part+s[end:],encoding="utf-8")
print("LORICA_V13_DOWNSTREAM_SEDIMENT_ACCUMULATION_PATCH_APPLIED")
