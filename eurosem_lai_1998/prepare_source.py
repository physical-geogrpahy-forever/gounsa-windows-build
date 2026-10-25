#!/usr/bin/env python3
"""Prepare original 1998 EUROSEM for modern gfortran. No hydrology/erosion
formula is changed except the separately applied optional LAI extension."""
from pathlib import Path
root=Path("eu")
assert (root/"eurseml.for").exists(),root
for p in root.glob("*.for"):
    p.write_bytes(p.read_bytes().replace(bytes([26]),b""))
p=root/"eplanel.for"
s=p.read_text()
for old,new in (
 ("      INTRT = 0\n      LCH = 0\n      contrib = 1.",
  "      INTRT = 0\n      LCH = 0\n      NKIR = 0\n      contrib = 1."),
 ("        MM=NB(JJ)-1","        MM=NB(JJ)-1\n        MB=NI+1")
):
    assert s.count(old)==1,old
    s=s.replace(old,new)
p.write_text(s)
p=root/"test.par"
s=p.read_text()
lines=s.splitlines()
m=[i for i,x in enumerate(lines) if x.split()==["2","0","0","0","0","0","0"]]
assert len(m)==1,m
lines[m[0]]=" 2      1         0        0        0        0       0"
p.write_text("\n".join(lines)+"\n")
print("Prepared source and fixed sample topology")
