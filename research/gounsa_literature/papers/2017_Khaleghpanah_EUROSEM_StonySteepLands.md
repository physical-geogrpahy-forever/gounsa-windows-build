# 서지정보
Khaleghpanah, N., Shorafa, M., Asadi, H., Gorji, M., & Davari, M. (2017). Modeling soil loss at plot scale with EUROSEM and RUSLE2 at stony soils of Khamesan watershed, Iran. *CATENA, 153*, 170-181. https://doi.org/10.1016/j.catena.2016.08.039

# 이 논문을 찾은 이유
EUROSEM의 rock-fragment treatment가 실제 stony steep lands에서 runoff 및 soil loss를 재현한 적용 선례가 있는지 확인하기 위해 검토했다.

# 연구 유형
- field validation
- numerical model comparison

# 공간 구조
- 24 m x 1.8 m erosion plots
- hillslope/event scale

# 적용 환경
- stony steep rangeland hillslopes
- natural rainfall events

# 핵심 과정
- runoff
- soil loss
- rock-fragment effects
- event erosion

# 식생 입력
- rangeland surface condition
- 세부 식생상태는 EUROSEM input structure 사용

# 핵심 식
EUROSEM의 기존 ROC, PAVE, ISTONE structure를 사용한다. 본 연구의 핵심은 새 식이 아니라 stony steep land에서의 validation이다.

# 파라미터와 단위
- ROC
- PAVE
- saturated hydraulic conductivity
- rainfall/runoff/soil loss
정확한 calibration 값은 원문 적용 시 재검증한다.

# 원 논문의 구현 범위
24개 자연강우 사건을 이용해 EUROSEM과 RUSLE2를 비교하였다.
EUROSEM validation에서 runoff와 soil loss에 대해 각각 R² 약 0.70, 0.85가 보고되었고, rock-fragment cover가 simulation output에 영향을 주었다.

# 고운사에 직접 사용할 수 있는 부분
- steep + stony hillslope에 EUROSEM을 실제 적용한 선례
- rock-fragment interface가 농경지에만 한정되지 않는다는 근거

# 새로운 coupling이 필요한 부분
- 산림 PFT/root/litter dynamic state
- fire-spall-driven dynamic armour
- 2D flow coupling

# 한계
- rangeland
- plot/event scale
- 고운사 사암 산림과 직접 동일하지 않음

# 최종 판정
- 핵심 보조근거
- EUROSEM stony-steep applicability validation

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2016.08.039
