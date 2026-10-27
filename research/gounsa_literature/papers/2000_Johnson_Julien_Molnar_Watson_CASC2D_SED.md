# 서지정보
Johnson, B. E., Julien, P. Y., Molnar, D. K., & Watson, C. C. (2000). The two-dimensional upland erosion model CASC2D-SED. *Journal of the American Water Resources Association*, 36(1), 31–42. https://doi.org/10.1111/j.1752-1688.2000.tb04246.x

# 이 논문을 검색한 이유
Classic OpenLISEM 이외의 **진짜 원본 공개 C 코드**가 있는 강우사상별 2차원 지표유출과 다입경 침식/퇴적 모델의 실증 여부 확인.

# 연구 유형
기성 raster two-dimensional diffusive-wave runoff + erosion/sediment model 과 실제 Goodwin Creek 관측 유출/유사 비교를 포함한 모델 개발 및 검증 논문. 이번 세션에서는 FAO AGRIS의 논문 초록, CSU 공식 배포 설명과 공개 C 소스 직접 확인. 원문 전체 본문은 접근 미확보.

# 공간구조
격자기반 2D **diffusive wave**, full inertial shallow-water equations 아님. `OvrlRout.c::OvrlRout`에서 모든 내륙 정방격자 x/y 양 방향 인접 교환; `ovrl`은 격자 수면고도차 방향에 따라 양/음 부호가 바뀌는 유량을 반대 격자에 더하거나 뺌. D8은 아니지만 `RoutOutlet.c`는 **한 개 `jout,kout`** 출구 격자에서만 경계배출 처리하므로 **네 면 자유 개방 경계 요건 실패**.

# 적용환경
Goodwin Creek 농업유역, Mississippi, USA. 초고해상도 산지 숲 5–10cm 강우사상 실증 아님.

# 핵심과정
- 강우 분포 `rain.c`, `OvrlDepth.c`; Green-Ampt infiltration; 2D diffusive-wave overland.
- `Fcts_sed.c::KRcap` modified Kilinc-Richardson transport capacity, landuse USLE C/P, soil K, `RoutSedOvrl.c` suspended/deposited/parent soil volume, sand/silt/clay classes; `Settling.c` 침강과 `SedStats.c` 격자별 net erosion/deposition.
- `RoutSedOvrl` 내 원토양 박리는 유량이 있는 **흐름수송능력**에 결합. 직접 rainfall-drop splash detachment 별도 source term은 이번 원본 코드 경로에서 미발견.

# 식생입력과 수관차단
- `ReadControlFile.c` landuse별 `pman[i]` 거칠기, `retention[i]` 초기 차단저류량(mm), `cfactor[i]` USLE C, `pfactor[i]` USLE P.
- `InitializeVars.c` `ret[j][k]=retention[iman[j][k]]/1000`; `intercept.c`: 해당 초기 `ret`를 `wrint*dt`에서 소진할 때까지 차감하고 `ret=0`; **수관 LAI, 동적 canopy C(t) / Smax, leaf drip, drainage, stemflow 없음**. 식생별 고정 용량과 수관의 우량-시간 재분배는 다름.
- `cfactor`는 경험적 피복/관리계수이지 LAI 물수지나 뿌리저항량이 아님.

# 핵심식 및 단위
- `OvrlRout.c`: `sf=(z_i-z_j)/w - (h_j-h_i)/w` (signed water-surface gradient); `Q=sign(sf)*w*sqrt(abs(sf))/n*(h_upstream-Sdep)^1.667`. w[m], Q[m3/s], n Manning.
- `Fcts_sed.c::KRcap`: `KRcoeff*abs(sf)^1.66*(abs(Q)/width)^2.035 * USLE_C * soil_K * USLE_P * width * dt` as code. Formula parameters from original control input, literature calibration cannot be reused blindly.
- interception `ret` in m initially and `wrint` m/s, `dt` s.
- Original source routine `InitializeVars.c` initializes `ssoil` to 0 and `RoutSedOvrl` erodes parent material by subtracting `TransferSed` without a clearly bounded layer stock; finite initial soil thickness not encoded by that variable in verified path.

# 원 논문의 구현 범위
FAO AGRIS 초록: Goodwin Creek example peak flow and peak timing within ±20%, sediment rates -50% to +200% of observations. These are case results, not per-cell 5cm sediment/DEM validation.

# 고운사에 직접 사용할 수 있는 부분
독립 소스 기반 2D diffusive hydraulic and overland sediment/deposition counterexample; 원본 연구부터 공개되어 연구방법 재현 확인의 좋은 대조자료.

# 새로운 coupling이 필요한 부분
LAI-Rutter/Gash 동적 저류 및 leaf-drip kinetic energy, separate raindrop detach, arbitrary all-sides open boundary, finite soil stock, sub10cm timestep/mesh convergence가 전부 현 소스 원본의 확인된 기능이 아님. 새로 추가하면 **새로운 coupling/patched model**, user 요청 원본 검증모델은 아님.

# 한계
GitHub clone README는 CSU 원본 배포 site에서 옮기며 `rint` 이름을 `wrint`로 바꾼 수정 사항 기재. **CSU의 원 binary와 byte-identical이라고 주장하지 말 것**. 이전 v1.0 연구용 코드는 공개되었으나 Linux native 컴파일/실험은 이번 문헌 조사에서 수행 안 함. 5cm published precedent 미발견.

# 최종 판정
**원본 코드 확인 PASS, 고운사 원본 단일엔진 NO-GO.** LAI 동적 canopy/leafdrop 박리, 네 면 개방 경계, 5–10cm 실증 근거 부족. 문헌상 진정 2D diffusive-wave erosion/deposition 존재는 확인.

# 참고 링크 / DOI
https://doi.org/10.1111/j.1752-1688.2000.tb04246.x
https://agris.fao.org/search/en/providers/122535/records/65defa137c7033e84bec47bd
https://www.engr.colostate.edu/~pierre/ce_old/Projects/CASC2D-SED%20Web%20site%20082506/CASC2D-SED-Home.htm
https://github.com/wy7980/CASC2D-SED
