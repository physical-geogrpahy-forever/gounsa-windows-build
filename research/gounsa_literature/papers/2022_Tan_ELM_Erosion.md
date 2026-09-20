# 서지정보
Tan, Z., Leung, L. R., Li, H.-Y., & Cohen, S. (2022). Representing global soil erosion and sediment flux in Earth System Models. *Journal of Advances in Modeling Earth Systems, 14*, e2021MS002756. https://doi.org/10.1029/2021MS002756

# 이 논문을 찾은 이유
PFT별 quantitative root biomass가 rainfall-driven 및 runoff-driven erosion에 직접 들어가는 published model을 확인하고, LPJ-GUESS FineRootC를 유수침식 저항으로 연결할 근거를 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- Earth System Model soil erosion module
- erosion and sediment-flux model

# 공간 구조
- ELM grid
- catchment/upland erosion parameterization
- global regionalized calibration

# 적용 환경
- 전지구 land cover
- 산림
- 농경지
- 기타 육상 PFT

# 핵심 과정
- rainfall-driven erosion
- runoff-driven erosion
- overland-flow transport capacity
- residue protection
- root protection
- surface roughness

# 식생 입력
- topsoil root biomass density BR
- plant residue biomass Br
- LAI
- canopy cover
- canopy height
- PFT

# 핵심 식
ground-cover/root protection:

```
GC = exp[-bC * max(Cr, C_LAI) - bR * BR]
```

강우 및 유출침식에 대해 각각 `bC1, bC2, bR1, bR2`를 둔다.

residue biomass에서 cover:

```
Cr = 1 - exp(-a * Br)
```

surface roughness:

```
n = 0.03 + 0.05 * max(Cr, C_LAI)
```

원문에서 root effect는 rainfall-driven erosion과 runoff-driven erosion에 서로 다른 coefficient를 사용하며, roots가 runoff-driven erosion 억제에 더 효과적이라는 구조를 둔다.

# 파라미터와 단위
- BR: 논문에서는 topsoil root biomass density, kg m-3
- Br: kg m-2
- bR: PFT-specific root-effectiveness parameter
- bC: PFT-specific surface-cover effectiveness parameter
- a: residue-to-cover regression coefficient, 논문 구현에서 6.680
- c1, c2, c3, bC1, bC2, bR1, bR2: calibration parameters

# 원 논문의 구현 범위
ELM이 photosynthesis, respiration, phenology, carbon allocation으로 residue와 root biomass를 갱신하고, ELM-Erosion이 이를 rainfall-driven/runoff-driven erosion 및 transport-capacity 계산에 사용한다.

제공된 `SedYieldMod.F90` 검토에서 root biomass는 fine root뿐 아니라 live/dead coarse-root carbon과 PFT 면적비를 사용해 topsoil `Broot`를 구성하는 구현이 확인되었다.

# 고운사에 직접 사용할 수 있는 부분
- 절대 root biomass density를 쓰는 구조
- PFT별 root effectiveness
- rainfall-driven과 runoff-driven root effect를 분리하는 구조
- residue/LAI와 root effect를 별도의 항으로 두는 구조

# 새로운 coupling이 필요한 부분
고운사에서는 mixed-PFT를 다음처럼 PFT별로 분리합산하는 방안을 검토했다.

```
R_root = sum_i (bR_i * BR_i)
GC_root = exp(-R_root)
```

이 형태는 ELM-Erosion의 실제 mixed-PFT 코드 구현과 동일하다고 확인되지 않았으므로 반드시 `새로운 coupling`으로 기록한다.

또한 LPJ-GUESS FineRootC를 topsoil root dry-mass density 또는 carbon-mass density로 바꾸는 변환도 새로운 coupling이다.

# 한계
- bR는 보편 물성값이 아니라 calibration parameter
- 실제 ELM 코드에서는 PFT별 root biomass를 먼저 합친 column-level Broot에 PFT coefficient를 적용하는 것으로 보이는 구현이 있어 개념식과 mixed-PFT 처리에 주의가 필요
- 코드 주석은 Broot를 kgC m-3로 표시하는 반면 논문은 root biomass density kg m-3로 기술하므로 단위 변환 재검증 필요
- 제공 코드의 root term이 `- -gcbr_* * Broot` 형태로 보여 부호 확인이 필요하며, `pftvarcon`의 실제 parameter 값이 없으므로 현재는 오류라고 단정하지 않는다
- 산지 genuine 2D concentrated-flow 전용모델은 아니다

# 최종 판정
- 채택
- 역할: FineRootC/topsoil root biomass -> runoff detachment protection의 핵심 근거

# 참고 링크 / DOI
https://doi.org/10.1029/2021MS002756

# 복구 메모
- 업로드된 원문과 제공된 ELM-Erosion Fortran 코드를 현재 채팅에서 직접 확인했다.

## 2026-09-21 현재 채팅 최종 보정
- **수치모델 연구로서 채택 유지.** topsoil root biomass density가 rainfall-driven 및 runoff-driven erosion 저감항에 직접 들어간다는 점이 핵심이다.
- 다만 이 모델은 고운사의 genuine 2D 산지 surface-flow routing을 제공하지 않는다.
- 따라서 `FineRootC -> topsoil root biomass density -> erodibility/detachment modifier`만 가져오고, HighLand 또는 별도 2D flow solver에 연결하는 부분은 **새로운 coupling**이다.
- interrill과 rill을 WEPP/Wu 방식으로 분리할 경우 ELM-Erosion의 rainfall/runoff 구분과 일대일 대응한다고 가정하지 않는다.
