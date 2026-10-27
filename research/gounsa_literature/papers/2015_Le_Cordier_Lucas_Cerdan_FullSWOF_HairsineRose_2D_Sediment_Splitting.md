# 서지정보
Le, M.-H., Cordier, S., Lucas, C., & Cerdan, O. (2015). A faster numerical scheme for a coupled system modeling soil erosion and sediment transport. *Water Resources Research*, 51(2), 987–1005. https://doi.org/10.1002/2014WR015690

# 이 논문을 찾은 이유
고운사 단일 강우사상 5–10cm의 진정 2차원 유수침식 과정에 필요한 **수치적 안정성, 격자별 국지 박리 및 퇴적, 질량 보존, 건습경계에서 유사농도의 비음수성**을 실제 증명한 기성 모델의 학술 선례와 공개 계산코드가 일치하는지 확인하기 위해. Classic OpenLISEM 코드 수정은 별도 Work 담당으로 유지.

# 연구 유형
- 2차원 천수방정식 + Hairsine–Rose(HR) 다입경 토사침식의 유한체적법 및 수치적 시간분할 개발.
- 1차원 해석해/수치해 벤치마크, 2차원 실험지형 입력에 대한 계산시간 및 수치 안정성 비교.
- **논문 본문 전체 Wiley 공개 HTML(방법론 §2–4.3, 결론)을 직접 검증**. DOI와 출판일 2015-01-12 확인.
- 물리식 논문은 완전 공개지만 **2015년 연구용 최종 HR 수정 C++ 파일과 테스트 runfile의 일치하는 공개 소스 SHA는 찾지 못함**. 공개 FullSWOF_2D 원형은 물리적으로 별개 버전.

# 공간 구조
- 원본 발표 수치해법: 자유 x/y 2차원 비선형 shallow-water flow, finite-volume conservative formulation, hydrostatic reconstruction+MUSCL, 다입경 침식과 물질농도 수송.
- 상태변수: 수심 h, 2차원 유속 u,v, 지표고도 z_b, 입경별 부유사농도 c_i [M/L³], 지표 퇴적층의 입경별 질량 m_i [M/L²].
- 수면마찰 Manning 또는 Darcy-Weisbach, 침투 Green-Ampt, 다입경별 침강속도.
- 2D 검증 지형: 세네갈 Thiès 시험구 **10m×4m**, 종방향과 횡방향 경사 각각 1%인 V자형 지표. **실제 숫자 계산격자 dx/dy는 현재 확인한 Wiley HTML 본문에서 직접 특정하지 못해 5cm 검증이라 주장 금지**.

# 적용 환경
세네갈 농경지 흙 사면 강우 모사; sand-dominant 실험구 (clay1%, silt7%, fine sand43%, coarse sand49%). 강우 **70mm/h, 2시간**. 현장 수관 및 참나무 맹아/억새 혼합피복 연구가 아님.

# 핵심 과정
1. 수리: 비선형 2D SWEs wet/dry positivity-preserving finite volume, Green–Ampt infiltration, dynamic rainfall input.
2. HR 원토양 박리: 비에 의한 splash detachment e_i와 유수전단에 의한 entrainment 분리.
3. 퇴적층 재박리 및 재유입 e_ri, 기존 퇴적층에 의한 원토양 보호, 입경별 침전과 퇴적층 m_i, 유사농도 c_i 수송 및 지형변화.
4. **핵심 수치 차별성**: 기존 Heng (2009) 및 Kim (2013) 방식이 shallow water의 CFL 이외에 유사농도 음수 방지를 위한 **추가 제한 시간간격** 요구. Le et al.은 침전 과정의 해석적 적분과 침식 과정의 양수보존 처리, Strang 분할로 extra limit 없이 **물 흐름 CFL 조건만으로 sediment nonnegative**를 보장하도록 설계.
5. 2D 시험에서 연구진은 흐름이 대부분 얕아 유수 흐름의 stream power가 critical threshold 미달하여 **실제 계산된 flow-induced sediment entrainment 기여가 거의 없다고 명시** (§4.3 Figure6). 결과는 **강우충격에 의한 침식 및 유사퇴적 우세**. 이 시험을 강우박리+세류/유수박리 모두 정량 검증된 증거로 인용 금지.
6. 시간간격 수치 효율: 종전 추가 제한 대비 약 100배 이상의 시간간격 성능개선, 저자 2D case에서 계산시간 100배 이상 단축; **고운사 5cm 구현의 안정성이나 실제 벤치마크 속도와 동치 아님**.

# 식생 입력
- 본 2015 버전의 강우 공급 R과 침식 source는 기술되지만 LAI, canopy storage Smax, dynamic canopy C(t), throughfall, stemflow, interception/drainage, **leaf-drop impact energy**는 논문 모델의 state/input 또는 소스에서 확인되지 않음.
- Manning roughness constant in this paper is not a vegetation canopy water budget.
- Site bare / raked soil. Thus canopy-on vs off young oak/Miscanthus test unperformed.

# 핵심 식
- 2D 수문-유사 결합: 물 연속방정식 + xy momentum + 종별 advection–reaction(sediment) + deposited layer m_i. 정확 source term e_i flow splash + deposition d_i, shield m_i, spatial bed evolution z_b.
- Transport code numerical physical restriction: volume sediment fraction <10% so sediments treated as passive species in water dynamics. High solid concentration is outside the tested coupling regime.
- Sediment positivity: wet/dry-aware well-balanced hydrodynamics with local two-stage analytical settling; Strang splitting (deposition half-step, erosion full-step, deposition half-step).
- Final paper Eq1–7 and Eq20–26 are formally published, but Wiley HTML text hides TeX formula source for many expressions; **do not manufacture coefficients or duplicate equations from unrelated references**.

# 파라미터와 단위
- Model plot 10m×4m, 1% longitudinal/1% transverse slope, 70mm/h 2h.
- Grain size classes 10, 20, 50, 100, 150, 200, 250, 500, 750, 1000 μm; sand-dominated fractions Table1.
- Intrinsic horizontal Δx/dy, water timestep, actual 4-edge free boundary config, sediment stock finite soil depth: **unverified**.

# 원 논문의 구현 범위
A **published actual integrated same study** 2D FullSWOF hydraulic + HR sediment, numerical solver benchmark and morphodynamics. Its central contribution is numerical time-step stability and positivity, not vegetation inter-event processes. The chosen 2D benchmark itself had negligible overland **flow detachment** due to low stream power; only rain detachment and transport dominated. User needs both contributions demonstrable.

# 정확한 소스 검증
- Baseline FullSWOF_2D original 2016 CeCILL version **publicly available**: https://github.com/BUCEA/FullSWOF_Rif branch master `README.txt` lists version 1.07.00 dated 2016-03-14. `Makefile` compiles `librain_infiltration`, `libschemes`, `libflux`, `libboundaryconditions` etc, **NO sediment/erosion/HR library**.
- The study explicitly states 2015 researchers **added an erosion component onto FullSWOF**, so it is an **altered experimental research edition distinct from public baseline**.
- University official FullSWOF releases confirm hydraulic original, mention some later **1D transfer additions** (July2021), but did not confirm release of 2015 Le et al. **same full 2D erosion C++**. Sourcecode trace/DOI artifact unknown. Peer-reviewed method does not satisfy exact public complete executable source.
- Baseline FullSWOF clone 2016 is not the paper's same version nor the Le modifications; do not turn it into model original by hypothetical implementation.

# 고운사에 직접 사용할 수 있는 부분
- Strong physical and numerical **independent benchmark** for local 2D erosion and deposition, material nonnegative and wet/dry fronts, (if exact code found) numerical mass testing. Well suited in concept for cm-scale solver design, but no published 5cm same source nor LAI interception.
- Investigates exactly the kind of timestep sediment numerical instability that invalidated Classic OpenLISEM7.5.2 before. This is **methodological information for assessing** a solver, not proof code patches elsewhere are already published or stable.

# 새로운 coupling이 필요한 부분
- LAI-driven canopy reservoir and throughfall/dynamic drip KE, species-specific oak and Miscanthus calibration, physically linked rainfall erodibility; would be **new coupling**.
- Exact paper HR sediment source must be obtained before any attempt to run the same published model; reconstructing Eq as a new fork is development not native original.
- 5–10cm and 6h steep multi-direction/open four boundaries physical sediment convergence not established.

# 한계
No source-code complete matching study public and no canopy, exact 2015 plot numerical cell size unverified, 2D experiment flow entrainment negligible. Not an immediately suitable original single model.

# 최종 판정
**보조근거: 매우 유용한 2D sediment numerical stability peer-reviewed paper; native 공개 검증가능 5cm canopy model = NO-GO.**

# 참고 링크 / DOI
https://doi.org/10.1002/2014WR015690
https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2014WR015690
https://github.com/BUCEA/FullSWOF_Rif
https://www.idpoisson.fr/en/fullswof/
