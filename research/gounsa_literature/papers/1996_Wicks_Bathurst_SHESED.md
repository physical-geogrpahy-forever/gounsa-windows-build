# 서지정보
Wicks, J. M., & Bathurst, J. C. (1996). SHESED: A physically based, distributed erosion and sediment yield component for the SHE hydrological modelling system. *Journal of Hydrology, 175*(1–4), 213–238. https://doi.org/10.1016/S0022-1694(96)80012-6

# 찾은 이유
SWEHR 공개코드에는 원논문 수관 저감항이 없어 완전 공개된 다른 원본 SWEHR 대체 후보에서 산림 수관적하, 물과 유수박리를 분리하고 있는지, rill 형성까지 가능한지 검증하기 위함.

# 연구 유형
[A] 저널 원문 초록 및 출판정보 확인; 수치모형 개발 및 농업 소유역 실증.

# 공간 구조
SHE hydrological grid network distributed hillslope erosion with sheet overland flow, catchment sediment routes; **논문은 explicitly without rilling**이라고 명시. 2D cell routing 논문 내용만으로는 full dynamic 2D shallow-water SWE라고 단정 금지. 현재 SHETRAN 소스는 4-face overland QOC finite differences.

# 적용환경
미국 아이오와 농업 유역 두 곳 5.1ha 및 6.4ha에서 시간별 토사량 비교, Wyoming East Fork River 3.3km 37일 사건 sediment discharge 비교. 직접 고운사 산불급경사 실증 아님.

# 핵심과정
raindrop detachment + canopy leaf drip momentum + sheet overland flow detachment/transport, channel bank/bed sediment, multi size and bed armouring.

# 식생입력
overstory canopy and understory cover with leaf-drip mechanisms, not dynamic roots RLD.

# 핵심식
Actual source equations (SHETRAN 2026 version `src/sediment/SYmod.f90/SYOVER`): `DR=GKR*Fw*(1-FCG-FCROCK)*(GMR+GMD)` and `DF=GKF*(1-FCROCK)*max(0,tau/tauc-1)`. `GMD` canopy drip momentum depends on fall height, drop diameter and drip fraction. Code version has explicit complete implementation, independently verified. Publication exact numerical parameters, input data not used yet.

# 파라미터와 단위
GKR soils raindrop erodibility, GKF flow detachment parameter, XDRIP[m], DRDRIP[m], FDRIP dimensionless, FCG/FCROCK [0–1], SWE hydrological state, soil density kg/m3.

# 고운사 직접 적용
Both canopy drip kinetic energy and separate near-ground vegetation and coarse rock armor factor already in OPEN ORIGINAL Fortran `SYOVER`, unlike public SWEHR 1.0. Existing vegetation and soil parameter records may be mapped to dense Miscanthus vs sparse Quercus structure, but need actual plant parameters and spatial maps.

# 필요한 새로운 coupling
per-plant location stemflow, dynamic roots/litter physics and RLD, fire-spall rock weathering, rill morphodynamics NOT in original. All changes separately labelled if applied.

# 한계
Default sheet flow no rills, original 1996 field data arable, latest SHETRAN source quality/mass QA untested here, current BALSED function stub.

# 판정
**핵심 원본 식생 침식 과정 근거**.

# 링크
https://eprints.ncl.ac.uk/57743


## 2026-10-27 SHETRAN 주모델 선정 이후 판정 정정
- SHETRAN 4.7.2는 [이번 결정문](../decisions/2026-10-27_SHETRAN_SELECTED_AS_GOUNSA_SINGLE_STORM_EROSION_ENGINE.md)에 따라 **고운사 단일강우 유수침식 주모델로 선정 완료**. 이 논문의 예전 '최종 모델 채택 보류' 서술은 당시 연구 상황을 기록한 과거 판정이며, 새 결정 이후 모델 미선정의 근거로 사용할 수 없다.
- 이 논문의 실제 검증범위(실험사면/유역 외부 유사량 또는 격자 내 퇴적, 예전 SHESED 및 당대 SHETRAN 버전)는 유지하고, SHETRAN 4.7.2 고운사 현장 검증 완료라는 주장으로 확대하지 않는다.
