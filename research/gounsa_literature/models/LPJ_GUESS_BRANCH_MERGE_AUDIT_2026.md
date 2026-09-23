# LPJ-GUESS branch merge audit: SEC/PPA, RE, LSM

업데이트: 2026-09-23

## 목적
고운사 production architecture 후보인 LPJ-GUESS 계열에서 최신 canopy, soil hydrology, subdaily land-surface branch가 실제로 얼마나 독립적인지 평가한다.

현재 별도 published branches:
- SEC/PPA canopy revision 13221: Stoebke et al. 2026
- LPJ-GUESS-RE v1.0: Verbruggen et al. 2025
- LPJ-GUESS/LSM v1.0: Martín Belda et al. 2022

이 셋이 하나의 공개 통합판으로 검증된 것은 아니다.

## 1. SEC/PPA branch
Stoebke et al. 2026, revision 13221.

주요 수정 영역:
- cohort crown area와 canopy position
- vertical/horizontal light sections
- forest-floor irradiance
- establishment light filtering
- PPA canopy layer promotion/demotion
- SEC persistent gaps
- self-thinning / crown competition 관련 구조

즉 핵심 수정 영역은 `canopy geometry + radiative/light competition + establishment`이다.

Published code archive: Zenodo DOI 10.5281/zenodo.18133363.

## 2. LPJ-GUESS-RE v1.0
Verbruggen et al. 2025.
Base: LPJ-GUESS v4.1.1, revision 10118.

주요 수정 영역:
- 15-layer soil profile
- user-adjustable layer thickness
- configurable total soil depth
- Richards-equation vertical water movement
- adaptive subdaily ODE integration inside daily ecosystem step
- free drainage / bedrock / aquifer bottom boundary

중요한 저자 진술:
논문은 RE 코드가 `relatively simple and easy to transfer to other branches of LPJ-GUESS`라고 명시한다.

따라서 SEC/PPA와 RE는 서로 완전히 다른 모델 coupling이라기보다 동일 코드베이스의 canopy branch와 soil-hydrology branch merge 문제에 가깝다.

### 예상 충돌도
**LOW-MODERATE relative to other combinations.**

이유:
- SEC/PPA: canopy/light/establishment 중심
- RE: soil-water transport/soil layers 중심

공유 접점은 root water uptake와 water-stress state이므로 integration testing은 필요하지만, 핵심 수정 파일/개념영역이 상당히 분리된다.

## 3. LPJ-GUESS/LSM v1.0
Martín Belda et al. 2022.
Base: LPJ-GUESS v4.0 lineage.

주요 수정:
- land surface processes subdaily, evaluation runs 1 h forcing/timestep
- energy balance closure
- cohort sunlit/shaded leaf representation
- new canopy radiative transfer
- direct/diffuse shortwave partitioning
- stomatal/latent/sensible heat coupling
- nine soil layers, total 3 m
- subdaily soil heat and water transport

### 중요한 충돌
LSM은 단순히 `시간간격만 짧게 만든 branch`가 아니다.
**radiative transfer와 cohort canopy energy exchange를 크게 다시 구현했다.**

SEC/PPA 역시 canopy geometry와 light transfer를 크게 수정한다.

따라서:
```text
SEC/PPA + LSM
```
은 두 독립 모듈을 단순 결합하는 문제가 아니다.

예상 충돌 영역:
- cohort ordering/layering
- absorbed PAR
- sunlit/shaded partition
- canopy horizontal sections
- forest-floor light
- establishment light
- energy-balance coupling

### 예상 충돌도
**HIGH relative to SEC+RE.**

SEC/PPA spatial canopy geometry를 LSM의 subdaily radiative-transfer equations 안에 다시 표현해야 한다.

## 4. 고운사 시간구조에 대한 결론
고운사는 storm-scale geomorphology가 1 h 또는 그 이하로 돌아갈 수 있지만, 식생 biomass/demography 자체가 반드시 hourly일 필요는 없다.

가장 현실적인 구조:
```text
external hydrology / geomorphology
  hourly or event timestep
       |
       | daily state aggregation / exchange
       v
LPJ-GUESS SEC/PPA
  daily physiology
  slower demographic update
       |
       v
root biomass / LAI / litter / uptake demand
       |
       +--> external hydrology / geomorphology
```

RE를 내부 vertical soil solver로 쓰거나 PF-LPJG식 external 3-D hydrology overwrite를 사용할 수 있다.

폭우 직후 필요한 즉시 반응은 별도의 event hook으로:
- soil depth change
- root truncation/exposure
- plant damage/mortality flag
- soil water redistribution
을 갱신하면 된다.

따라서 LSM branch의 full subdaily canopy physiology를 합치는 것은 필수사항이 아니다.

## 5. 현재 구현 우선순위
### Route A, 가장 현실적
```text
SEC/PPA r13221
+ RE soil hydrology port
+ external geomorph state remapping
```

장점:
- canopy/understory 가장 강함
- variable soil depth와 bedrock
- merge conflict가 상대적으로 작음

한계:
- native lateral catchment water routing 없음

### Route B, 고운사 요구에 가장 강하지만 더 큰 coupling
```text
SEC/PPA r13221
+ PF-LPJG-style external ParFlow exchange
+ geomorph engine
```

장점:
- actual 3-D lateral hydrology
- hourly hydrology / daily vegetation 분리 가능

한계:
- PF-LPJG는 older LPJ-GUESS base이므로 coupling interface를 r13221로 port해야 함

### Route C, 현재 비추천
```text
SEC/PPA
+ LPJ-GUESS/LSM
+ RE/ParFlow
```

이유:
- canopy/radiation 코드 중복 수정
- 필요 이상 복잡
- 고운사 100-year postfire 목적에서는 hourly canopy energy balance가 핵심 병목이 아님

## 최종 판정
현재 기술적으로 가장 합리적인 LPJ-GUESS 방향은 **SEC/PPA + RE 또는 PF-style external hydrology**이다.

특히 RE 논문의 `easy to transfer to other branches` 진술 때문에 SEC+RE는 단순 추측보다 강한 구현 가능성 근거가 있다.

아직 주장하면 안 되는 것:
- SEC/PPA + RE가 이미 공식 통합되어 있다
- SEC/PPA + PF-LPJG가 이미 공개 실행판이다
- storm erosion 뒤 soil/root/C/N conservative remapping이 native 기능이다

이 세 부분은 고운사에서 새로 구현/검증해야 한다.

## 핵심 근거
- Stoebke et al. 2026. GMD 19, 3595-3615. DOI 10.5194/gmd-19-3595-2026.
- Verbruggen et al. 2025. GMD 18, 6623-. DOI 10.5194/gmd-18-6623-2025. Code DOI 10.5281/zenodo.15024130.
- Martín Belda et al. 2022. GMD 15, 6709-6745. DOI 10.5194/gmd-15-6709-2022.
