# 서지정보
Long, M. (Mansheng), & He, D. (Dongjian). (2010). Simulation of soil erosion and rill evolution for overland flow [坡面水蚀与细沟发育过程模拟研究]. *Journal of System Simulation (系统仿真学报), 22*(2), 348–352. ISSN 1004-731X. DOI 공개 검색에서 미확인.
1차 재확인 (중국 저널 2017 인용): https://www.china-simulation.com/CN/abstract/abstract1200.shtml
연구 초록: https://eurekamag.com/research/099/685/099685317.php
https://www.researchgate.net/publication/289633996_Simulation_of_soil_erosion_and_rill_evolution_for_overland_flow

# 이 논문을 찾은 이유
고운사 엄격 5–10cm single model + LAI canopy + true 2D SWE + separate erosion and deposition + DEM feedback + public original search. 기존 Gounsa `INDEX.md` 470편에 같은 논문 없음 확인 후 새 canonical 기록.

# 연구 유형
Published numerical slope erosion model, computational FVM. **현재 원문 전체 PDF 및 실행코드가 아닌 공개 초록과 후속 원본 저널의 참고문헌으로 교차 확인**.

# 공간 구조
2D shallow-water equations with finite volume numerical method; sediment transport equation; erodible topography updated to track rill evolution. **2D momentum-based hydraulics가 명시되어 D8 routing과 다름**.

# 적용 환경
실험사면의 강우 침식 및 세류 발달. Forested steep sandstone hill and LAI measured patches not shown.

# 핵심 과정
- **Modified Gash rainfall interception** explicitly included.
- Green-Ampt infiltration.
- Rain-generated overland runoff 2D SWE.
- Erosion and deposition functions in sediment mass transport.
- Morphodynamic updates and dynamic rill development.
- Point-implicit friction slope to deal with near dry bed, per 2010 abstract.

# 식생 입력
'Modified Gash interception' 존재는 초록에서 확인. **LAI, species-specific canopy storage, throughfall routing, leaf-drip energy active** 여부는 본문·코드 미확인. Modified Gash에서 LAI를 수관최대저류량과 연결할 수 있다는 개념적 가능성을 저자가 직접 그 매개변수를 구현했다고 주장 금지.

# 핵심 식 / 파라미터와 단위
2D SWEs coupled with sediment transport and bed elevation feedback, Green–Ampt and Gash; empirical erosion/deposition source formulas, actual resolution and numeric coefficients were **not extractable from abstract**. Do not invent precise equations, mesh width, timestep or validation performance.

# 원 논문의 구현 범위
Published complete paper-level model combination definitely more aligned with user's physics than Maggioli2022 kinematic 5cm. No source-level audit is possible without original code; 5cm computational validation not evidenced.

# 고운사에 직접 사용할 수 있는 부분
Physical precedent for **same paper physics** of canopy interception + freely 2D + erosion/deposition + rill topographic update.

# 새로운 coupling
Original source not found. Any contemporary numerical re-implementation of the equations is user-unwanted **new model**, not validated original application.

# 한계 / 최종 판정
**Strong physical reference only. No immediate reproducible model.** Missing published 0.05–0.10m computational grid, original complete open-source code, exact canopy LAI/stem/leaf drip energy treatment, matching executable, source and sediment mass QA. Thus **not recommended as operational Gounsa main engine**.

# 참고 링크
https://eurekamag.com/research/099/685/099685317.php
https://www.researchgate.net/publication/289633996_Simulation_of_soil_erosion_and_rill_evolution_for_overland_flow
https://www.china-simulation.com/CN/abstract/abstract1200.shtml
