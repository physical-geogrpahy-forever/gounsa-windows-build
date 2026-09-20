# ELM-Erosion model lineage

## 범위
고운사 문헌아카이브에서 ELM-Erosion 계열을 통합 관리한다.

## 확인된 핵심
Tan et al. (2022)에서 rainfall-driven erosion과 runoff-driven erosion을 분리하고, topsoil root biomass density와 PFT별 root-effectiveness coefficient를 ground-cover/root protection factor에 사용한다.

`GC = exp[-bC * max(Cr, C_LAI) - bR * BR]`

## vegetation state
- topsoil root biomass density
- residue biomass
- LAI
- canopy cover/height
- PFT

## 고운사 적용
FineRootC -> topsoil root biomass density -> runoff detachment protection 경로의 핵심 published precedent로 채택한다.

## 새로운 coupling
고운사에서 `sum_i bR_i * BR_i`로 PFT별 root effect를 합산하는 방식과 LPJ-GUESS FineRootC 단위변환은 원 구현과 동일하지 않으므로 새로운 coupling이다.

## 미해결
- bR calibration
- kgC m-3 대 dry biomass kg m-3 단위
- provided Fortran의 root-term 부호
- mixed-PFT 실제 구현

## 관련 논문
- ../papers/2022_Tan_ELM_Erosion.md
