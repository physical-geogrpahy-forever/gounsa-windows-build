# 서지정보
Long, M. (Mansheng), & He, D. (Dongjian). (2009). Hydraulic erosion simulation using finite volume method on graphics processing unit. In *Proceedings of the International Conference on Information Engineering and Computer Science (ICIECS)*. https://doi.org/10.1109/ICIECS.2009.5363863
검색 원문 메타·초록: https://www.researchgate.net/publication/251912530_Hydraulic_Erosion_Simulation_Using_Finite_Volume_Method_on_Graphics_Processing_Unit

# 이 논문을 찾은 이유
Long & He 2009/2010 Gash canopy and true 2D rill erosion lineage's GPU executable/source release and ultra-fine computation evidence search.

# 연구 유형 / 공간 구조 / 환경
GPU numerical implementation: full 2D shallow-water equations with HLLC first-order explicit Godunov finite-volume scheme + non-equilibrium sediment transport + bed topography evolution; dry/wet boundaries and dynamic time-step GPU reduction. Synthetic numerical sediment-fluvial model (physical soil erosion case validation unclear).

# 핵심 과정
2D shallow-water routing, sediment transport, erosion/bed evolution, flexible boundary textures. This paper's abstract **does not specifically mention canopy interception, LAI, modified Gash nor vegetation treatment**. Do not treat this implementation as demonstrably same source/version with the 2009 JICS or 2010 Journal of System Simulation canopy studies.

# 핵심 식/파라미터 단위
HLLC 2D SWE, finite-volume conservative flux, sediment source terms, evolving bed, dynamic CFL dt. Exact 0.05m/0.1m mesh, canopy retention [mm], sediment test mass residual not found in paper abstract.

# 고운사 직접 활용 및 필요한 새로운 coupling
Demonstrates numerical implementation of 2D high-performance morphodynamics under same authors, not an openly available code lineage with proven native canopy. Linking 2010 Gash interception would require verified SAME executable or would be an undesired new coupling.

# 한계 및 최종판정
**Separate code lineage support, not an operational candidate.** Exact full source/commit, 5–10cm benchmark, canopy active in this GPU code unknown.

# 링크
https://doi.org/10.1109/ICIECS.2009.5363863
