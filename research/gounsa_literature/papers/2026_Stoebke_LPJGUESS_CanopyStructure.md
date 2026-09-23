# 서지정보
Stoebke, J. E., Wårlind, D., Olin, S., Eckes-Shephard, A., Brzeziecki, B., Peltoniemi, M., & Pugh, T. A. M. (2026). Representing canopy structure dynamics within the LPJ-GUESS dynamic global vegetation model (revision 13221). Geoscientific Model Development, 19, 3595–3615. https://doi.org/10.5194/gmd-19-3595-2026

# 이 논문을 찾은 이유
고운사 식생엔진 후보의 핵심 조건인 `공간명시 cohort + 명시적 하층식생/천이 + 짧은 생리 시간단위`를 LPJ-GUESS 최신 계보가 얼마나 충족하는지 확인하기 위해 검토했다. 특히 기존 LPJ-GUESS의 약점이었던 patch 내부 수관 공간구조와 understory 표현이 2026년에 개선되었는지 확인했다.

# 연구 유형
- 수치모델 개발 및 검증
- cohort 기반 동적식생모델의 수관 구조 확장

# 공간 구조
세 가지 수관 구조를 비교한다.
- standard LPJ-GUESS: patch 내부 수관이 수평적으로 균질
- SEC (spatially explicit canopy): cohort의 aggregated crown area centroid를 patch 내부 고정 위치에 배치
- PPA: cohort를 높이순으로 수관층과 understory layer에 배치

SEC는 완전 개별목 모델은 아니지만 cohort에 patch 내부 공간위치를 부여해 gap이 시간에 따라 유지되도록 한다. 이는 고운사의 `개별목보다 단순하지만 실제 공간구조를 갖는 cohort-hybrid` 조건에 매우 잘 맞는다.

# 적용 환경
- boreal, temperate, tropical forest의 23개 이상 장기 관측지
- BCI 등 forest dynamics plots
- harvesting 이후 woody understory 재정착 평가

# 핵심 과정
- cohort별 crown area, height, bole height
- vertical/horizontal light competition
- persistent canopy gap
- PFT-specific sapling establishment
- woody understory/recruitment layer
- herbaceous understory light response
- growth-efficiency mortality
- self-thinning

# 식생 입력
- tree cohort biomass and density
- cohort height and crown area
- PFT-specific establishment traits
- herbaceous layer LAI
- standard LPJ-GUESS carbon, nitrogen, water state

# 핵심식/구조
Lambert-Beer 광감쇠로 각 수직 구간의 fPAR를 계산한다.

SEC에서는 forest floor를 여러 horizontal section으로 나누고 각 section의 연간 PAR를 계산한다. 각 PFT의 `PAR_est,min`을 넘는 영역비율 `f_est`가 정착 가능면적을 결정한다.

새 sapling 수가 충분하면 새로운 cohort를 생성하며, 논문 설정에서는 PFT당 연간 최대 4개 신규 cohort를 만들 수 있다.

# 하층식생 관련 핵심 발견
- 수관 아래 남은 PAR가 herbaceous understory에 전달된다.
- SEC에서는 forest-floor horizontal section별로 herbaceous understory leaf area가 동적으로 조절된다.
- tree cohort는 overstory와 여러 understory layer를 형성할 수 있다.
- disturbance/harvest 이후 gap이 유지되면서 recruitment layer가 형성된다.
- standard LPJ보다 SEC가 장기간 woody recruitment layer를 더 잘 유지했다.

따라서 LPJ-GUESS 계열은 2026 revision 13221 기준으로 `하층식생을 단순 ground-cover correction으로만 처리한다`고 평가하면 안 된다.

# 시간 구조
이 논문은 수관구조 개선에 초점을 두며 생리 시간간격을 새로 바꾸지는 않는다. LPJ-GUESS의 기존 일별 생리/토양수문 계산과 연별 demographic scheduling을 그대로 사용한다.

# 원 논문의 구현 범위
- 실제 지형 유역 수문과의 결합 논문은 아님
- patch 내부 canopy spatial structure를 개선
- fire는 평가실험에서 껐지만 LPJ-GUESS 계보의 fire capability 자체는 유지

# 고운사에 직접 사용할 수 있는 부분
1. 개별목보다 가벼운 공간명시 cohort-hybrid
2. 수목 overstory/understory와 gap dynamics
3. forest floor 광환경에 따른 herbaceous understory 동태
4. 산불/교란 후 recruitment layer를 명시적으로 계산할 수 있는 구조
5. 기존 LPJ-GUESS의 root, litter, soil-water state와 결합 가능

# 새로운 coupling이 필요한 부분
이 revision을 다음 계보와 동시에 쓰는 것은 현재 확인된 published single implementation이 아니다.
- PF-LPJG 2026의 ParFlow coupling
- LPJ-DH/WHyMe-TFM의 50 m catchment routing
- LPJ-GUESS-RE의 15-layer Richards soil hydrology

즉 `revision 13221 SEC/PPA + PF-LPJG 또는 LPJ-GUESS-RE`는 고운사에서 매우 유망하지만 현 시점에서는 **새로운 code merge/coupling**으로 분류해야 한다.

# 한계
- SEC의 cohort 위치는 실제 2-D x-y 좌표라기보다 원형 1-D 공간좌표로 단순화된 patch 내부 위치
- herbaceous layer는 수목처럼 age/size cohort demography가 동일 수준으로 세분된 것은 아님
- 유역 측방수문은 이 논문에 없음
- canopy refinement는 standard LPJ보다 계산비용 증가

# 최종 판정
- 채택 후보의 핵심 근거
- **LPJ-GUESS 계열의 criterion 1과 2를 이전 평가보다 상향**
- SEC는 고운사에서 `완전 개별목보다 단순한 공간 cohort` 구조로 특히 유망
- 주 유역/토양지형 coupling은 별도 계보(PF-LPJG, LPJ-DH, LPJ-GUESS-RE)와 결합해야 함

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-19-3595-2026
