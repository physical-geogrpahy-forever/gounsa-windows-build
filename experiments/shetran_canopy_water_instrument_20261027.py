#!/usr/bin/env python3
"""Insert read-only ETIN canopy mass flux diagnostics into SHETRAN upstream.
Physics/equations unmodified. Uses native precip, CSTORE, PNETTO, EINTA.
"""
import sys
from pathlib import Path
p=Path(sys.argv[1]);s=p.read_text()
a="      DOUBLE PRECISION :: EDUM !! Potential evaporation not supplied by initial surface water (m/s)."
assert s.count(a)==1
s=s.replace(a,a+"\n      DOUBLE PRECISION :: QA_CSTORE_BEFORE",1)
a="      CPLAI = MIN(CLAI(N), ONE)*PLAI(N)"
assert s.count(a)==1
s=s.replace(a,a+"\n      QA_CSTORE_BEFORE = CSTORE(IEL)",1)
a="      S(top_cell_no) = S(top_cell_no) + ESOILA(IEL)/DELTAZ(top_cell_no, IEL)"
assert s.count(a)==1
s=s.replace(a,a+"""
      WRITE(*,'(A,1X,I7,1X,10(ES23.14,1X))') 'QA_CANOPY', IEL, TIMEUZ, &
        DTUZ, precip_m_per_s(IEL), QA_CSTORE_BEFORE, CSTORE(IEL), &
        PNETTO(IEL), EINTA(IEL), ERZA(IEL), ESOILA(IEL), EEVAP(IEL)
""",1)
p.write_text(s)
print("QA_CANOPY_WRITE_ONLY no native hydrologic equations changed")
