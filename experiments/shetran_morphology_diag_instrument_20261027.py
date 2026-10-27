#!/usr/bin/env python3
"""Add TWO native geomorphic diagnostic scalars to existing QA_SPATIAL.
Apply AFTER shetran_instrument_sediment_qa and shetran_spatial_flux_instrument.
No native process equations or prognostic state variables are modified.
"""
from pathlib import Path
import sys
p=Path(sys.argv[1]);s=p.read_text()
old="WRITE(*,'(A,1X,2(I4,1X),5(ES23.14,1X))')"
new="WRITE(*,'(A,1X,2(I4,1X),7(ES23.14,1X))')"
assert s.count(old)==1,(old,s.count(old))
s=s.replace(old,new)
oldline="QA_SOURCE_CELL,QA_LOOSE_CELL,QA_SUSP_CELL"
newline="QA_SOURCE_CELL,QA_LOOSE_CELL,QA_SUSP_CELL, &\n                         GNU(QA_EL)*DTSY, FETA_symain(QA_EL)"
assert s.count(oldline)==1
s=s.replace(oldline,newline)
p.write_text(s)
print("QA_MORPH_DIAGNOSTIC_APPLIED, physical source unchanged")
