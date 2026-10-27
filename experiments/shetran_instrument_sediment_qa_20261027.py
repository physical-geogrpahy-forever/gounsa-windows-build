#!/usr/bin/env python3
"""Diagnostic-only instrumentation of a COPY of SHETRAN's original SYMAIN.
No sediment/water transport, detachment or deposition equation is modified.
Diagnostic compilation must never be described as pristine unmodified executable.
"""
from pathlib import Path
import sys

def replace_once(s,old,new):
    assert s.count(old)==1,(old[:120],s.count(old))
    return s.replace(old,new,1)

p=Path(sys.argv[1]);s=p.read_text()
s=replace_once(s,"      DOUBLE PRECISION :: DTSY\n      DOUBLE PRECISION :: CONCIE",
"""      DOUBLE PRECISION :: DTSY
      ! QA instrumentation only; no physical process changed.
      DOUBLE PRECISION :: QA_BEFORE, QA_AFTER, QA_SOURCE, QA_BOUNDARY, QA_RESID
      INTEGER :: QA_EL, QA_SED, QA_FACE
      DOUBLE PRECISION :: CONCIE""")
s=replace_once(s,
"""         DTSY = DTUZ/NEPS_symain
         DO N = 1, NEPS_symain

            ! Initialization""",
"""         DTSY = DTUZ/NEPS_symain
         DO N = 1, NEPS_symain
            QA_BEFORE = ZERO
            QA_SOURCE = ZERO
            DO QA_EL = NLF+1, NEL
               QA_BEFORE = QA_BEFORE + (ONE-PLS(QA_EL))*AREA(QA_EL)* &
                  (DLS(QA_EL)+SUM(FDEL(QA_EL,1:NSED))*DWATOL_symain(QA_EL))
               QA_SOURCE = QA_SOURCE + (ONE-PLS(QA_EL))*AREA(QA_EL)* &
                  FETA_symain(QA_EL)*GNU(QA_EL)*DTSY
            END DO

            ! Initialization""")
s=replace_once(s,
"""            ! Store Old-time Values & Update Timer
            ! ------------------------------------
            CALL DCOPY(NEL - NLF""",
"""            ! Independent QA of native four-face and storage material budget.
            ! Valid as an overland-only budget when NLF==0; includes sediment
            ! outlet and net imported sediment flux with signed QSED on boundaries.
            QA_AFTER = ZERO
            QA_BOUNDARY = ZERO
            DO QA_EL = NLF+1, NEL
               QA_AFTER = QA_AFTER + (ONE-PLS(QA_EL))*AREA(QA_EL)* &
                  (DLS(QA_EL)+SUM(FDEL(QA_EL,1:NSED))*DWAT1(QA_EL))
               DO QA_FACE = 1, 4
                  IF (ICMREF(QA_EL,QA_FACE,2) == 0) THEN
                     DO QA_SED = 1,NSED
                        QA_BOUNDARY = QA_BOUNDARY + &
                           QSED(QA_EL,QA_SED,QA_FACE)*DTSY
                     END DO
                  END IF
               END DO
            END DO
            QA_RESID = QA_AFTER-QA_BEFORE-QA_SOURCE+QA_BOUNDARY
            WRITE(*,'(A,1X,6(ES24.15,1X))') 'QA_SED_MASS', &
                     UZNOW, QA_BEFORE, QA_SOURCE, QA_AFTER, QA_BOUNDARY, QA_RESID

            ! Store Old-time Values & Update Timer
            ! ------------------------------------
            CALL DCOPY(NEL - NLF""")
p.write_text(s)
print(f"QA_PATCH_ONLY applied {p}, no physical solver equations changed")
