# 서지정보
Cooper, J. R., Wainwright, J., Parsons, A. J., Onda, Y., Fukuwara, T., Obana, E., Kitchener, B., Long, E. J., & Hargrave, G. H. (2012). A new approach for simulating the redistribution of soil particles by water erosion: A marker-in-cell model. *Journal of Geophysical Research: Earth Surface, 117*, F04027. https://doi.org/10.1029/2012JF002499

# 검색 이유
식생 강우차단, 수관통과, 수관적하 충격에너지와 공간별 유사 재배분이 함께 들어가는 매우 세밀한 모델의 논문 및 원본 확보.

# 연구 유형
MAHLERAN에 marker-in-cell 입자별 운반/재퇴적 구조를 결합하여 137Cs 표지입자 토양 재분배를 강우모사 실험과 비교함.

# 공간구조
**13.75m×6.5m** 인공 사면을 0.3m 그리드로 측량하고 **MAHLERAN-MiC 0.3m 셀**로 실제 실행(원문 §4.1 L390–414). 20분, 60mm/h 인공강우. 유동은 2D 래스터 공간이지만 **각 격자 경사 최대감소방향의 한 cardinal direction으로 운동파 라우팅**(원문 §2 L? 및 원문 본문 §2). genuine 2D SWE 자유유동과 다름.

# 적용환경
식생이 없는 모래 시험사면에서 얕은 세류와 입자 재분배 확인. **현장 실험에서 식생 수관차단까지 실제 활성 검증한 것은 아님**.

# 핵심과정
Smith-Parlange 침투, 운동파 지표유출, Darcy-Weisbach 마찰, 빗방울 및 흐름에 의한 입자박리, marker transport and deposition, 137Cs tracer spatial reconstruction.

# 식생입력
저자는 식생이 있는 경우 interception loss, throughfall, leaf drip에 의한 빗방울 운동에너지 변화를 scaling하는 모듈이 있다고 설명(본문 §3.1). LAI 기반 시간별 수관저류 방정식의 구체 구현 및 **0.3m 실험에서 식생이 있는 경우 검증**은 확인되지 않음.

# 핵심식
Kinematic-wave finite-difference routing, Smith-Parlange infiltration, direct/drop KE sediment detachment, probabilistic marker redistribution. 단일 셀에서 가장 가파른 정방향 이동.

# 파라미터와 단위
Δx=0.3m, 강우강도 60mm/h, 기간20분, 비탈면 13.75×6.5m, 경사 3°~5°, 셀당 marker 1200개 최적 기준.

# 고운사 활용
수관통과/수관적하별 충격에너지 개념과 유사 입자 이동 정량, 공간 퇴적 패턴 연구의 선행문헌.

# 필요한 새로운 coupling
10cm 이하 원본 실행 및 자유로운 4방향 SWE, 실제 억새/참나무 동적 canopy storage와 source version 공개를 모두 확인해야 함.

# 한계
실제 실험 Δx=0.3m, 단일경사방향 운동파, canopy scenario 검증 안됨. 개발자 공식 https://draem.webspace.durham.ac.uk/software/ 에서 이벤트 버전 원본 다운로드 파일 제공 대신 John Wainwright에 연락하라고 명시. 2026 현재 즉시 다운로드 가능한 matching code 미확인.

# 최종 판정
식생/유사이송 프로세스 참고용으로 유력, **<=10cm 및 공개 완전 단일 2D 모델 조건 불충족**으로 주모델 기각.

# 참고자료
https://doi.org/10.1029/2012JF002499
https://draem.webspace.durham.ac.uk/software/


## 2026-10-27 원문 전체 재확인: 수관 에너지 보정은 존재하나 실제 검증판은 나지

**Original journal accessible full text** https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2012JF002499:
- §2: underlying `Mahleran` hydrodynamic overland is **kinematic wave + cardinal-direction steepest-descent single flow outlet per cell**, NOT free XY 2D SWE. §3.1: when vegetation is present, **the impact KE of rain is scaled for interception losses, throughfall and leafdrip** following Wainwright et al. (1999), but no explicit event Rutter/Gash LAI-dependent water-storage solver from this sentence.
- §4.1: bare **13.75m×6.5m** synthetic sandy slope, 3° and 5°, 60mm/h for 20 min; survey 0.30m map, actual numerical **0.30m grid**. Artificial sediment layers include 0.05m upper loose sand **SOIL DEPTH, not computational 5cm**. Spatial tracer mapping 0.30m with `137Cs` soil. **No vegetation canopy active in published calibration/validation runs**.
- §5: observed water runoff534L vs model580L (reported 9% difference), outlet hydrograph NSE0.93; `137Cs` cell-level tracer redistribution spatial NSE0.98. Authors run 20 stochastic repeats and cell-wise 137Cs distribution. **Strong deposition validation**, but at 30cm in bare soil only.
- Other original documentation https://draem.webspace.durham.ac.uk/software/ offers authors/contact route, not independently downloadable same-matching 2012 exact compiler source in this audit.
- This evidence rules out promotion to **native 5–10cm, dynamic canopy-active, free XY 2D hydrodynamics**, regardless of marker positions calculated continuously within each grid. Stochastic subcell particle movement is **not equivalent to native free two-dimensional hydrodynamic grid solving**.
