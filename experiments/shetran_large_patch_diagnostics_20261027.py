#!/usr/bin/env python3
"""Add read-only accumulated original soil erosion and final native DLS per grid.
Apply only AFTER the native mass ledger instrumentation. Zero changes to all
hydrologic/erosion/transport equations. Counts a separate diagnostic state.
"""
from pathlib import Path
import sys
p=Path(sys.argv[1]);s=p.read_text()
def sub(old,new):
    global s
    n=s.count(old)
    assert n==1,(n,old[:160])
    s=s.replace(old,new,1)
sub("      DOUBLE PRECISION :: DTSY\n      ! QA instrumentation only;",
"""      DOUBLE PRECISION :: DTSY
      DOUBLE PRECISION, ALLOCATABLE, SAVE :: QA_GROSS_SOIL_ACC(:)
      INTEGER :: QA_LX, QA_LY, QA_LE
      ! QA instrumentation only;""")
sub("      PASS_symain = PASS_symain + 1\n      IF (PASS_symain == 1) THEN",
"""      PASS_symain = PASS_symain + 1
      IF (.NOT. ALLOCATED(QA_GROSS_SOIL_ACC)) THEN
         ALLOCATE(QA_GROSS_SOIL_ACC(NEL))
         QA_GROSS_SOIL_ACC = 0.0D0
      END IF
      IF (PASS_symain == 1) THEN""")
sub("NVC, GNU, DUMMY, DLS, DLSMAX_symain)\n\n         ! * Erosion rates for all link elements",
"""NVC, GNU, DUMMY, DLS, DLSMAX_symain)
         QA_GROSS_SOIL_ACC(NLF+1:NEL) = QA_GROSS_SOIL_ACC(NLF+1:NEL) + &
                         GNU(NLF+1:NEL)*DTUZ

         ! * Erosion rates for all link elements""")
sub("""            SYNOW_symain = SYNOW_symain + DTSY/3600.0D0

         END DO

         !--------------------- End of simulation step""",
"""            SYNOW_symain = SYNOW_symain + DTSY/3600.0D0

         END DO

         ! Diagnostic-only final surface elevations; 12h event end.
         IF (UZNOW >= 11.999999D0) THEN
            DO QA_LY=1,NY
               DO QA_LX=1,NX
                  QA_LE=ICMXY(QA_LX,QA_LY)
                  IF (QA_LE<=NLF) CYCLE
                  WRITE(*,'(A,1X,2(I4,1X),5(ES23.14,1X))') &
                       'QA_FINAL_CELL', QA_LX, QA_LY, UZNOW, &
                       QA_GROSS_SOIL_ACC(QA_LE), DLS(QA_LE), &
                       PLS(QA_LE), AREA(QA_LE)
               END DO
            END DO
         END IF

         !--------------------- End of simulation step""")
p.write_text(s)
print("QA_GROSS_INTEGRATED_FINAL_MAP_WRITE_ONLY",p)
