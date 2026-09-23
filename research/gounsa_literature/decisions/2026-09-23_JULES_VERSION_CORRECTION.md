# JULES public documentation version correction

업데이트: 2026-09-23

`2026-09-23_VEGETATION_ENGINE_DEEP_AUDIT.md`의 다음 문구를 정정한다.

기존 문구:
- public latest JULES documentation이 v7.9라고 기록

정정:
- 2026-09-23 현재 Met Office 공식 `latest` JULES User Guide는 **v8.1**이다.
- `red_parms.nml`에 RED의 `mclass`, `mass0`, `massi`, `height0`, `crwn_area0`, `alpha_recrt`, `mort_base`, `dom_order` 등이 정식 문서화되어 있다.
- `dom_order`: 3 tree, 2 shrub, 1 grass.
- `jules_vegetation.nml`의 `l_red`가 Robust Ecosystem Demography 사용 switch로 정식 문서화되어 있다.

따라서 `models/JULES_RED.md`에서 사용한 v8.1 기준 설명을 유지한다.

이 정정은 JULES-RED의 고운사 최종 순위를 높이는 결정은 아니다. 표준 JULES `dzsoil_io`가 domain 전체에서 constant soil-layer thickness/total depth를 사용한다는 dynamic-soil-geometry 한계는 여전히 남는다.
