# 서지정보
Neumann, M. (2022). *SMODERP – Implementation of sediment transport* [Doctoral dissertation, Czech Technical University in Prague]. http://hdl.handle.net/10467/104997

# 이 논문을 찾은 이유
2019/2022 SMODERP2D 연구에서 'erosion model'이라고 부르나 저장소의 active full source가 water+rill only여서 실제 유사원/퇴적 엔진을 별도 개발했는지 저자 연구 원문을 확인.

# 연구 유형
PhD original research thesis, **peer-reviewed journal paper와 구분**. Official CTU record/English-Czech abstracts verify experimental process and implementation objective. Full thesis PDF downloadable via university service, not read completely / all equations in this session.

# 공간 구조
Published thesis focuses choosing **unit discharge and slope based sediment-transport empirical equation** to attach to SMODERP event-based runoff engine, not same exact raster spatial multiface SWE+sediment.

# 적용 환경
CTU rainfall simulator >450 experiments in 2015–2021, slope4°–34°, rain40–160mm/h, agricultural soil/crop categories. Forest oak coppice vs Miscanthus and 5cm full-field simulation not verified.

# 핵심 과정
Comparison 10 candidate sediment transport/soil loss formulas against rainfall simulation. Kilinc & Richardson family formula chosen for integration, driven by unit surface discharge, gradient, USLE K erodibility and vegetation CS protection factor. **This is primarily an experimental identification and integration proposal**, not evidence 2026 GitHub distributed Python version includes finished sediment continuity and mass conservation modules.

# 식생 입력
Crop protective CS-factor by basic crop categories, not LAI-throughfall-capacity and rain drop KE of oak/grass individual crowns, no quantitative root biomass.

# 핵심 식
Unit discharge q and gradient S as predictors of KR-style soil loss capacity with crop CS and soil K; **exact parameter exponents and units not transcribed** because 2022 dissertation full Eq/table not verified.

# 파라미터와 단위
Rain mm/h 40–160; slope4–34 degrees, >450 experiments; relevant to user 10–50mm/h partly overlaps (40–50). No published 5cm executed morphology + sediment convergence.

# 원 논문의 구현 범위
Official abstract states contemporaneous SMODERP program only computed rain-runoff and target is to include erosion modeling. It provides academic method selection and calibrations, not direct proof runnable published 2D sediment engine merged into current public repo. Author implementation study may include code fragments in thesis which were not separately fetched; evidence cannot be broadened.

# 고운사에 직접 사용할 수 있는 부분
Independent physical constraint on runoff-erosion mapping in strong rain and steep slopes, but has vegetation by empirical CS; not a model program meeting user constraint.

# 필요한 새로운 coupling
Any new sediment module merged into SMODERP would be **new coupling**, user explicitly asks to avoid building replacement from formulas. No guarantee originally released runnable source exists.

# 한계
Doctoral study is research thesis, not independently proven code version with GitHub tag or site input, no sub10cm forest application, rain KE and deposition unverified.

# 최종 판정
**Supplementary observational/theoretical evidence, not standalone native 2D sediment source PASS**.

# 공식출처
https://dspace.cvut.cz/entities/publication/3155d66e-c8c2-463b-9e5a-72539e77c103
https://dspace.cvut.cz/server/api/core/bitstreams/178fb264-75e0-4835-a4fd-54a90ec359bf/content
http://hdl.handle.net/10467/104997
