#!/usr/bin/env python3
"""Log original-native OC boundary water discharge from original QOC at each
sediment substep, read-only. Apply AFTER mass-ledger instrumentation.
Water face conversion is identical to SYMAIN source QWAT=SIGN(1,2-FACE)*QOC.
"""
import sys
from pathlib import Path
p=Path(sys.argv[1]);s=p.read_text()
old="      INTEGER :: QA_EL, QA_SED, QA_FACE"
new="      INTEGER :: QA_EL, QA_SED, QA_FACE\n      DOUBLE PRECISION :: QA_WATER_BDRY"
assert s.count(old)==1
s=s.replace(old,new,1)
old="""            QA_RESID = QA_AFTER-QA_BEFORE-QA_SOURCE+QA_BOUNDARY
            WRITE(*,'(A,1X,6(ES24.15,1X))')"""
new="""            QA_RESID = QA_AFTER-QA_BEFORE-QA_SOURCE+QA_BOUNDARY
            QA_WATER_BDRY = ZERO
            DO QA_EL = NLF+1,NEL
               DO QA_FACE=1,4
                  IF (ICMREF(QA_EL,QA_FACE,2)==0) THEN
                     QA_WATER_BDRY = QA_WATER_BDRY + &
                      SIGN(ONE,DBLE(2-QA_FACE))*QOC(QA_EL,QA_FACE)*DTSY
                  END IF
               END DO
            END DO
            WRITE(*,'(A,1X,3(ES24.15,1X))') 'QA_OPEN_EXPORT', &
                           UZNOW, QA_WATER_BDRY, QA_BOUNDARY
            WRITE(*,'(A,1X,6(ES24.15,1X))')"""
assert s.count(old)==1
s=s.replace(old,new,1)
p.write_text(s)
print("QA_OPEN_WATER_EXPORT_LOGGING_ONLY",p)
