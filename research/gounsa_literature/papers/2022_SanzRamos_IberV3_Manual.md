# 서지정보
Sanz-Ramos, M., Cea, L., Bladé, E., López-Gómez, D., Sañudo, E., Corestein, G., García-Alén, G., & Aragón-Hernández, J. L. (2022). *Iber v3: Manual de referencia e interfaz de usuario de las nuevas implementaciones*. CIMNE. https://doi.org/10.23967/iber.2022.01

# 이 자료를 찾은 이유
Iber soil-erosion module의 실제 사용자 입력/결과 구조, multiclass sediment mass, loose-layer shielding 및 non-uniform sediment module의 구현 범위를 확인하기 위해 검토했다.

# 자료 유형
- official model reference/user manual

# 공간 구조
- 2D finite-volume Iber
- soil erosion module
- separate non-uniform sediment-mixture module

# 핵심 과정
soil erosion module:
- distributed 2D erosion
- original cohesive layer
- eroded/non-cohesive loose layer
- rainfall and flow erosion
- per-class mass conservation

non-uniform sediment module:
- active layer
- multiple substrate strata
- per-class bed-material fractions
- hiding and differential transport

# 핵심 확인
soil erosion module에서:
- 각 sediment class별 soil mass conservation
- loose layer M_s,k [kg m^-2]
- erosion shielding epsilon
- flow-driven detachability K_k
- critical shear stress tau_cr
등이 explicit input/state로 정의됨.

non-uniform sediment module에서는 active layer 및 substrate strata의 class proportions를 저장하고 결과에서도 layer별 grading을 조회할 수 있다.

# 고운사에 직접 사용할 수 있는 부분
- Iber에 이미 multiclass, shielding, active-layer/strata concepts가 구현된 계보가 있다는 근거
- event output을 class별로 관리할 수 있는 공식 implementation documentation

# 중요한 제한
공식 문서에서 soil-erosion module과 river-bed non-uniform-mixture module이 **고운사 hillslope에서 하나의 multilayer soil-profile module로 완전히 통합되어 동작한다고 확인되지는 않았다.**
따라서 두 모듈을 결합해 SSSPAM을 대체한다고 주장하지 않는다.

# 최종 판정
- Iber+ event multiclass erosion interface의 공식 구현근거
- deep hillslope profile은 SSSPAM/mARM 계보를 유지

# 참고 링크 / DOI
https://doi.org/10.23967/iber.2022.01
