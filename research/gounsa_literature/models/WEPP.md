# WEPP model lineage

## 확인된 역할
- interrill과 rill을 분리
- Ki, Kr, critical shear stress 사용
- live/dead root biomass와 residue가 erodibility adjustment에 들어감
- 기본 hillslope routing은 genuine 2D가 아님

## 고운사 판정
root-dependent erosion parameterization의 핵심 근거로 채택하되 최종 2D engine으로는 미채택.

## 새로운 coupling
LPJ-GUESS vegetation state를 WEPP parameter에 연결하거나, WEPP parameter를 Wu/Iber 계열 2D engine으로 넘기는 것은 새로운 coupling.

## 관련 문헌
- ../papers/1995_Alberts_WEPP_Soil_Component.md
- ../papers/1995_Arnold_WEPP_Plant_Growth_Component.md
- ../papers/1995_Stott_WEPP_Residue_Decomposition.md
- ../papers/1995_Foster_WEPP_Hillslope_Erosion.md
- ../papers/2022_Lee_WEPP_Erodibility_Critical_Shear.md
