# 서지정보
Long, M. (Mansheng), & He, D. (Dongjian). (2009). Simulation of rill evolution based on finite volume method. *Journal of Information and Computational Science, 6*(6), 2349–2356. DOI 확인되지 않음.
초록·서지: https://www.researchgate.net/publication/289634136_Simulation_of_rill_evolution_based_on_finite_volume_method

# 이 논문을 찾은 이유
5–10cm 사면에 적용하려는 **수관차단 + 자유 2D SWE + 직접 강우사상 세류침식/퇴적 + 원본 프로그램** 조합을 단일 published model에서 실현한 다른 연구를 찾기 위해.

# 연구 유형
2D 유동 및 입자이동 수치모델, 방법론 논문. 현재 검증 범위는 제목·저널 서지·공개 초록이며 전체 원문 PDF를 입수하여 식/격자/수치결과까지 전수 판독한 것이 아님.

# 공간 구조
**2D shallow-water equations / Godunov-type finite volume shock-capturing**; intercell sediment and eroded-bed change. Slope planform XY model이지 LDD kinematic 1D가 아님.

# 적용 환경
주로 강우사상 사면에서 세류(rill)의 발생/발달을 수치실험. **참나무 산림/억새 패치 5–10cm 선행사례는 확인되지 않음**.

# 핵심 과정
- Modified Gash **interception** component.
- Green–Ampt infiltration.
- 2D shallow-water runoff momentum and continuity.
- Non-capacity sediment transport equation with separately parameterized **erosion and deposition**.
- Sediment exchange and dynamic rill evolution on the slope.
- Godunov shock-capturing finite-volume numerical hydrodynamics.

# 식생 입력
Modified Gash canopy interception is explicitly named in abstract. **논문 초록만으로 LAI 실제 입력, vegetation species-specific storage/drainage, leaf-drip kinetic energy, oak/grass field validation이라고 주장 불가**. 식생 모듈의 정확 source and parameter values require the full paper.

# 핵심 식
2D SWE + non-capacity sediment conservation + erosion/deposition empirical source terms + Green-Ampt + modified Gash, but coefficient-level equations and exact units **full text not yet obtained**. 임의로 식을 보충하거나 기존 Gash 일반형을 저자 native 식인 것처럼 제시하지 않음.

# 파라미터와 단위
실제 격자폭 [m], 시간간격 [s], 수관저류 매개변수 [mm], 지형변화 검증 오차 **공개 초록에서 미확인**. 5cm or 10cm published RUN evidence 없음.

# 원 논문의 구현 범위
Methods explicitly integrate canopy-interception and 2D erosion/deposition with rill change in one original numerical model **at equation/paper level**. Matching executable SHA, published source tarball, full test case, reproducible input maps, native numeric stability not found in search.

# 고운사에 직접 사용할 수 있는 부분
Very strong **architectural precedent** against claim that no published 2D SWE + canopy interception + morphodynamics study exists. Does **not** satisfy user's publicly available, 5–10cm, LAI-specific, reproducible existing original model constraints.

# 필요한 새로운 coupling
배포된 단일 원본 코드를 확보하지 못했으므로 본 논문을 바탕으로 새 해석기를 직접 작성하는 것은 **새 구현**이며 사용자가 요구한 타인 원본코드 실행이 아니다.

# 한계 및 최종 판정
**보조근거/원본 확보 실패로 채택 보류**. 조건 ① published same-model canopy+SWE+erosion yes at abstract level; ② real ≤10cm grid unknown; ③ LAI-dependent active interception/drip impact unknown; ④ matching open source unknown; ⑤ 5cm/native stability unknown.

# 원문 접근
https://www.researchgate.net/publication/289634136_Simulation_of_rill_evolution_based_on_finite_volume_method
https://www.china-simulation.com/CN/abstract/abstract1200.shtml (2017 후속 논문의 2010 선행인용).
