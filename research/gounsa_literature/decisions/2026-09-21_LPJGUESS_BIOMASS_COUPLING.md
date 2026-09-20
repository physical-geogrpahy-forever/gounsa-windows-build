# 결정 내용
고운사 식생-지형 coupling의 기본 상태변수는 단일 vegetation cover가 아니라 LPJ-GUESS의 PFT/cohort별 quantitative vegetation state로 둔다.

최소 보존변수:
- FineRootC_i
- LeafC_i
- WoodC_i
- SurfaceLitC
- NPP_i
- 가능하면 DBH, height, density, rooting-depth profile

# 왜 결정했는가
LPJ-GUESS에서는 상층 교목과 하층 초본이 같은 cell에서 수직적으로 겹치고 천이가 일어난다. 단일 cover fraction으로 합치면 PFT별 기능차이와 기관별 효과가 사라진다.

# 근거 논문
- Tan et al. 2022: PFT-specific root effect
- Gabet et al. 2003: root mass, turnover, depth에 따른 biogenic transport
- Ma et al. 2022, 2023: herb/shrub/tree root effects 차이
- Zeng et al. 2024: grass/shrub/forest의 Dc, Kr, tau_c 차이
- Zhou et al. 2024: aboveground와 belowground 경로 분리
- Parhizkar et al. 2024: overstory-understory competition 문제
- Pawlik 2023/2024, Osorio-Leon 2025: deep woody-root weathering

# 새로운 coupling
LPJ-GUESS carbon pools를 RMD/RLD/RSAD, erodibility, tree-throw probability, weathering rate로 변환하는 단계는 기존 단일 published model이 아니며 모두 **새로운 coupling**으로 표기한다.

# 아직 해결되지 않은 문제
- FineRootC -> RLD/RSAD의 PFT별 변환계수
- WoodC/cohort state -> tree throw 및 CWD
- NPP/root respiration -> chemical weathering rate
