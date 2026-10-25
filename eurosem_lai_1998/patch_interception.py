#!/usr/bin/env python3
"""Minimal single-executable LAI interception experiment for EUROSEM 1998.

Source equations:
  Phillips et al. (1997/1998) canopy capacity S = S_leaf * LAI;
  LISFLOOD/De Roo formulation k = 0.046*LAI (user-calibratable k_leaf).
Replaces ONLY interception storage inside EUROSEM INTERC, preserving original
free throughfall, geometry-based drip/stemflow, KE, infiltration and sediment
routing. LAI.PAR: element_id LAI S_leaf_mm_per_LAI k_per_LAI.
All coefficients shown in the test cases are examples, not Gounsa estimates.
"""
from pathlib import Path

p=Path("eurseml.for")
s=p.read_text()
declarations="      DIMENSION vegsto(100),dinter(100),dripst(100)"
assert s.count(declarations)==1
s=s.replace(declarations,declarations+"""
      REAL LAIV,SLEAF,KLAI,SCAP,SKLAI
      INTEGER IOSLA,IDL
""")
init="""      DICMAX=DINTR(J)
      CUINT(J)=0.0"""
assert s.count(init)==1
s=s.replace(init,"""      DICMAX=DINTR(J)
C     OPTIONAL LAI FORCING WITHIN THE SAME EUROSEM EXECUTABLE.
C     LAI.PAR: ELEMENT, ONE-SIDED GROUND LAI, SLEAF(mm/LAI), K/LAI.
C     IF ABSENT, ORIGINAL 1998 STORAGE EQUATION IS UNCHANGED.
      LAIV=-1.
      OPEN(UNIT=77,FILE='LAI.PAR',STATUS='OLD',IOSTAT=IOSLA)
      IF(IOSLA.EQ.0) THEN
  870 READ(77,*,IOSTAT=IOSLA) IDL,LAIV,SLEAF,KLAI
      IF(IOSLA.NE.0) THEN
        LAIV=-1.
        GOTO 880
      ENDIF
      IF(IDL.NE.J) GOTO 870
  880 CLOSE(77)
      ENDIF
      IF(LAIV.GE.0.) THEN
        SCAP=MAX(0.0,SLEAF*LAIV)
        SKLAI=MIN(COVER(J),MAX(0.0,KLAI*LAIV))
      ENDIF
      CUINT(J)=0.0""")
target="       vegsto(K)=COVER(J)*DICMAX*(1-EXP(-cumd(ige,k)))"
assert s.count(target)==1
s=s.replace(target,"""       IF(LAIV.GE.0.) THEN
         VEGSTO(K)=0.0
         IF(SCAP.GT.1.0E-8) VEGSTO(K)=
     1   SCAP*(1.0-EXP(-SKLAI*CUMD(IGE,K)/SCAP))
       ELSE
         vegsto(K)=COVER(J)*DICMAX*(1-EXP(-cumd(ige,k)))
       ENDIF""")
p.write_text(s)
print("PATCHED EUROSEM INTERC with optional LAI water storage; original fallback retained")
