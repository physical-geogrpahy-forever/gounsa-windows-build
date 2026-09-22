# LPJ-GM model lineage

## 목적
LPJ-GUESS의 local vegetation dynamics를 유지하면서 grid cell 사이의 seed production, dispersal, seed bank, establishment를 명시적으로 연결한다.

## 계보
### LPJ-GM 1.0
Lehsten et al. 2019.
- LPJ-GUESS migration coupling
- MPI cell communication
- annual seed redistribution
- published simulation cell 1 km x 1 km
- corridor option and FFT method for computational reduction

### LPJ-GM 1.1
Zani et al. 2022.
- improved dispersal kernels
- explicit seed production, seed bank, germination
- 1 km vegetation-dynamics cells
- dispersal kernel computed at 100 m and aggregated to 1 km
- species-level migration evaluation

### LPJ-GM 2.0 archive
Zenodo 2023, DOI 10.5281/zenodo.8434850.
- LPJ-GUESS v4.0 base
- SEEDISP: explicit seed production, dispersal, soil seed bank
- FIXSPEED: time-delay approximation to migration

## 공간 구조
LPJ-GUESS의 비공간 replicate patches를 그대로 여러 개 두는 대신 명시적으로 위치한 simulation cells 사이에 seed exchange를 수행한다.

중요:
- published 1.0/1.1 experiments: 1 km local vegetation cells
- 1.1의 100 m는 dispersal kernel numerical resolution
- 이것을 30 m local vegetation resolution 검증으로 오해하면 안 됨

## 시간 구조
- LPJ-GUESS physiology: 기존 daily process
- seed production/dispersal/seed bank/establishment exchange: annual

## 고운사 장점
1. 기존 LPJ-GUESS FineRootC, leaf, litter, NPP, LAI, hydrology 출력 계보를 유지할 수 있음.
2. LPJ-GUESS의 가장 큰 문제였던 cell-to-cell migration 부재를 직접 해결함.
3. 산불 후 주변 미연소림에서 seed source가 들어오는 공간적 회복을 표현할 수 있음.
4. 기존 고운사 LPJ-GUESS 초기화와 출력 코드를 가장 많이 재활용 가능.

## 고운사 핵심 미검증
1. 30 m x 30 m local vegetation cell을 코드가 허용하는가.
2. 4454개 고운사 cell 모두에서 local LPJ dynamics를 실행했을 때 계산량이 현실적인가.
3. FFTM/dispersal kernel을 30 m spacing으로 재이산화해도 parameter meaning이 유지되는가.
4. slope/ridge/rock/burn severity를 dispersal barrier로 어떻게 줄 것인가.
5. current LPJ-GUESS release와 archived LPJ-GM 2.0 code의 차이를 어떻게 병합할 것인가.

## 판정
현재 식생모델 재검토에서 최우선 기술검증 후보.

단, 30 m 고운사 적용은 published implementation 그대로가 아니라 해상도 변경 및 검증이 필요한 새 implementation이다.

## 관련 논문
- papers/2019_Lehsten_LPJ_GM_1_0.md
- papers/2022_Zani_LPJ_GM_1_1.md
