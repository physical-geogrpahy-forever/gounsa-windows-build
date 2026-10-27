# 2026-10-27 21:00 신규 Long–He 2009–2010 2D 수관차단 침식모델의 학술선례와 원본코드 공개 여부 판정

## 작업 출발
`research/gounsa_literature/SYSTEM.md`, 최신 `MASTER.md`, 470 papers / 96 models `INDEX.md`, Maggioli2022 원본 소스 판정, Iber+, ASTERIX, HydroPol2D strict code audits를 **검색 전에 먼저 읽음**. 이미 제외된 SHETRAN 무선례 5cm 확대, OpenLISEM7.5.2 native failing build, SWEHR, TREX, GSSHA, LISEM 계보를 처음 찾는 모델로 재추천하지 않음.

## 새로 확인한 3편의 Long–He 연구
1. **Long & He (2009)**, `Simulation of rill evolution based on finite volume method`, *Journal of Information and Computational Science 6(6), 2349–2356*. https://www.researchgate.net/publication/289634136_Simulation_of_rill_evolution_based_on_finite_volume_method : 2D SWE (Godunov FVM), modified Gash interception, Green–Ampt infiltration, non-capacity erosion/deposition, fine-scale rill evolution in original abstract. **One-architecture physics precedent**.
2. **Long & He (2010)**, `Simulation of soil erosion and rill evolution for overland flow` [坡面水蚀与细沟发育过程模拟研究], *Journal of System Simulation, 22(2)*, 348–352. Original journal citation verified by subsequent Long(2017) https://www.china-simulation.com/CN/abstract/abstract1200.shtml; study abstract https://eurekamag.com/research/099/685/099685317.php . **2D SWE + modified Gash interception + Green–Ampt + empirical erosion/deposition + bed morphodynamics + point-implicit friction**. More direct to Gounsa whole physics than previously cited Maggioli 5cm kinematic version, but **no cm mesh proof**.
3. **Long & He (2009)** `Hydraulic Erosion Simulation Using Finite Volume Method on Graphics Processing Unit` ICIECS DOI 10.1109/ICIECS.2009.5363863: GPU 2D SWE HLLC + sediment + evolving bed; **canopy/Gash not mentioned in THIS paper's abstract**, do not automatically conflate the published GPU code with modified Gash study.

## 공개 코드 검증
- Connected GitHub global repository name/description search precise authors, paper title terms, `modified Gash` and code searches; **no matching complete solver repository found**. Nor peer-reviewed sources provide publicly linked matching source tarball, SHA, installation package, full 5cm input DEM or runfile.
- This is a **bounded search result**, not proof that source never existed or code could not be requested. No attempt to infer grid size from laser DEM or screenshots.
- Exact numerical grid width, native time step, full material stock limit, and 5cm local deposit DoD comparison cannot be determined from the available abstracts. **No cm-resolution published verification claim.**
- Modified Gash `interception` is verified at model abstract level. **Specific LAI-driven storage, preferential leafdrip kinetic energy, RLD and crown geometry not separately confirmed.**
- Numeric code for 2009/2010 **not compiled or run**; equations in journal abstract not a downloadable production-grade model.

## Additional new nonqualifying current literature
- **Perrini et al. (2024)** *WRR* DOI 10.1029/2023WR036421, existing archive paper `papers/2024_Perrini_RunoffOnGrid_DREAM_Iber.md`. Hydrological model DREAM computes explicit LAI-and-canopy fraction bucket plus 2D Iber hydraulic routing, but original **two-model coupling** does NOT publish the 2024 Iber+ active sediment+canopy+5cm exact same executable. No compliant new all-in-one.
- **Cea et al. (2024)** Iber+ rainfall and runoff detachment 2D finite-volume erosion DOI 10.1016/j.envsoft.2024.106098: Gounsa `models/Iber.md` prior audit says missing proven LAI interception and full C++/CUDA source accessible only collaborators. Strong physics, no original public source. Not revisit as new.
- **Heng et al. (2009)** *WRR*, DOI 10.1029/2008WR007502 has 0.05m numerical space step for a **1D comparison of Saint-Venant and kinematic-wave solution on 5m slope**, 2D full canopy+erosion at 5cm cannot be inferred. No interception keyword in original paper.

## Immediate reproducible Gounsa selection
**NO newly verified, openly executable exact source satisfying five hard conditions** (published native 5–10cm, LAI native canopy storage/drip, freely XY SWE, raindrop/flow detachment and local deposition, matching public complete code/stable mass).
New Long–He model is meaningful **academic equation-level precedent** but **not a runnable recommendation**. Continuing model name searches without code may not yield an immediate engine; source path/size availability remains blocker.

## Records
- [2009 Long & He FVM with canopy](../papers/2009_Long_He_Rill_Evolution_FVM_Modified_Gash.md)
- [2010 Long & He physics](../papers/2010_Long_He_2D_Gash_Rill_Erosion_Morphodynamics.md)
- [2009 GPU implementation](../papers/2009_Long_He_GPU_2D_SWE_Hydraulic_Erosion.md)
- [source lineage audit](../models/Long_He_2D_Gash_Morphodynamics_Code_Audit.md)

## Next concrete action if research resumes
Search **same source and same version executable/download only**, particularly Long & He full paper supplements or institutional published research software, while never silently relax 5–10cm or default to SHETRAN extension. If obtaining exact code requires asking authors, label not currently available without user pretending we can receive it automatically. New published 5cm model still most direct Maggioli2022 but kinematic and 7.5.2 separate source failed.
