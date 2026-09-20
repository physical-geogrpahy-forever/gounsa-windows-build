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

# 2026-09-21 FineRootC -> RLD 업데이트

이 연결의 **수식/단위 구조는 해결됨**.

Dantas de Paula et al. 2025 LPJ-GUESS-NTD는 carbon-based SRL을 사용한다:

```
SRL_C [m root kg C^-1]
C_root [kg C m^-2]
```

따라서 PFT p, soil layer i에서:

```
RLD_p,i
=
C_root,p
* SRL_C,p
* f_p,i
/ Dz_i
```

- `f_p,i`: LPJ-GUESS PFT-specific root fraction in layer i
- `Dz_i`: soil-layer thickness

현재 LPJ-GUESS는 15 x 0.1 m layer 구조와 PFT별 vertical root fraction을 제공한다.
따라서 `SRL_C`를 사용하면 별도 임의 carbon-to-dry-mass 변환은 필요 없다.

한국 산림 근거:
- Huh et al. 2025: Korean pine vs oak에서 비슷한 총 fine-root biomass에도 SRL과 0-10 cm 분배가 크게 다름
- Kim et al. 2017: Pinus densiflora seedling SRL도 국내 토양조건에 따라 변함

따라서 이제 unresolved gap은:
```
FineRootC -> RLD equation
```
자체가 아니라:

1. 고운사 PFT/species별 `SRL_C`
2. exact Gounsa FineRootC output normalization
3. surface erosion에 사용할 effective depth
4. postfire live/dead root persistence
5. RLD -> erosion resistance parameter calibration

이다.

세부 구현:
- `models/LPJ_GUESS_Root_Erosion_Interface.md`

# 아직 해결되지 않은 문제
- PFT별 SRL_C parameterization
- live/dead root postfire persistence
- WoodC/cohort state -> tree throw 및 CWD
- NPP/root respiration -> chemical weathering rate
