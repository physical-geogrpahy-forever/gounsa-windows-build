#!/usr/bin/env python3
"""Increase ONLY compiled fixed-size table bound for >20 boundary conditions.
Original SHETRAN upstream build uses NOCTAB=20, but 15x27 active hillslope
produces 54 OC boundary faces. NO PHYSICAL EQUATIONS OR BOUNDARY TYPES CHANGED.
This is a transparent compilation-capacity patch, not an untouched binary.
"""
from pathlib import Path
import sys
p=Path(sys.argv[1]);s=p.read_text()
before="INTEGER(KIND=I_P), PARAMETER :: NOCTAB = 20"
after="INTEGER(KIND=I_P), PARAMETER :: NOCTAB = 80"
assert s.count(before)==1,s.count(before)
p.write_text(s.replace(before,after))
print("QA_CAPACITY_ONLY_PATCH from NOCTAB 20 to 80; original equations untouched",p)
