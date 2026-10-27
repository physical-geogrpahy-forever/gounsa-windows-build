#!/usr/bin/env python3
"""Add pure logging statements to the already instrumented SYMAIN source.
Logs (x,y) native sediment intercell transfer, native original-soil source,
and final/current loose+suspended storage. Does NOT alter solver variables.
"""
from pathlib import Path
import sys
p=Path(sys.argv[1]);s=p.read_text()
original="      INTEGER :: QA_EL, QA_SED, QA_FACE"
changed="      INTEGER :: QA_EL, QA_SED, QA_FACE, QA_XX, QA_YY\n      DOUBLE PRECISION :: QA_TRANSFER_CELL, QA_SOURCE_CELL, QA_LOOSE_CELL, QA_SUSP_CELL"
assert s.count(original)==1,s.count(original)
s=s.replace(original,changed,1)
marker="            ! Store Old-time Values & Update Timer"
assert s.count(marker)==1,s.count(marker)
insert="""            ! QA_SPATIAL: positive QA_TRANSFER_CELL means net imported from
            ! neighbouring cells; negative means net exported. This is NOT
            ! identical to gross local deposition, which must exclude
            ! transient suspended storage. Exact native signed QSED used.
            IF (NLF == 0) THEN
               DO QA_YY=1,NY
                  DO QA_XX=1,NX
                     QA_EL=ICMXY(QA_XX,QA_YY)
                     IF (QA_EL <= NLF) CYCLE
                     QA_TRANSFER_CELL=-SUM(QSED(QA_EL,1:NSED,1:4))*DTSY
                     QA_SOURCE_CELL=(ONE-PLS(QA_EL))*AREA(QA_EL)* &
                          FETA_symain(QA_EL)*GNU(QA_EL)*DTSY
                     QA_LOOSE_CELL=(ONE-PLS(QA_EL))*AREA(QA_EL)*DLS(QA_EL)
                     QA_SUSP_CELL=(ONE-PLS(QA_EL))*AREA(QA_EL)* &
                          SUM(FDEL(QA_EL,1:NSED))*DWAT1(QA_EL)
                     WRITE(*,'(A,1X,2(I4,1X),5(ES23.14,1X))') &
                         'QA_SPATIAL',QA_XX,QA_YY,UZNOW,QA_TRANSFER_CELL, &
                         QA_SOURCE_CELL,QA_LOOSE_CELL,QA_SUSP_CELL
                  END DO
               END DO
            END IF

"""
s=s.replace(marker,insert+marker,1);p.write_text(s)
print("QA_SPATIAL_INSTRUMENT_SOURCE_WRITE_ONLY")
