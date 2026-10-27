#!/usr/bin/env python3
"""Increase ONLY static SHETRAN boundary-array extent for 54+80 BC.
No original hydrologic or sediment equations changed.
"""
from pathlib import Path
import sys
p=Path(sys.argv[1])
s=p.read_text()
old="INTEGER(KIND=I_P), PARAMETER :: NOCTAB = 20"
new="INTEGER(KIND=I_P), PARAMETER :: NOCTAB = 180"
assert s.count(old)==1
p.write_text(s.replace(old,new))
print("QA_ONLY_STATIC_BOUNDARY_ARRAY_EXTENT 20 -> 180",p)
