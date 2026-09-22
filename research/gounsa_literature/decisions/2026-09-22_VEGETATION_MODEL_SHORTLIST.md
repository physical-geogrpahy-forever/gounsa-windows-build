# 고운사 식생모델 재검토

날짜: 2026-09-22

## 재검토 이유
기존 LANDIS-II + NECN 잠정안에서:
- landscape spatial succession은 강하지만 geomorph model과의 시간교환이 연 단위 이상으로 제한되고
- 고운사 지형모델은 storm/event 또는 hourly scale로 작동한다.

기존 LPJ-GUESS는:
- daily physiology와 root/litter state는 강하지만
- standard patches/cells 사이가 공간적으로 명시적이지 않다.

iLand는:
- 개체목/stand process는 강하지만
- 고운사 30 m geomorph feedback에 필요한 공간단위와 직접 일치하지 않는 문제가 있었다.

따라서 다음 조건을 동시에 재검색했다.

## 필수 조건
1. explicit landscape space 또는 30 m 이하의 실제 spatial structure
2. wildfire 후 succession/recruitment
3. root biomass 또는 root-related quantitative state
4. litter/dead biomass state
5. geomorph model과 교환 가능한 1년 이하 식생 update
6. code availability와 실제 구현가능성

## 후보 비교

| Model | 공간 | 시간 | 산불 후 천이 | root | litter | 현재 판정 |
|---|---|---|---|---|---|---|
| LPJ-GM | grid-cell seed exchange 명시 | physiology daily, migration annual | LPJ-GUESS disturbance + seed limitation | 강함 | 강함 | 최우선 기술검증 |
| SEIB-DGVM | 30 m plot 내부 1 m explicit | daily/monthly/annual | O | 강함 | 강함 | 2순위, inter-plot 문제 |
| LANDIS-II NECN | landscape raster explicit | monthly internal, succession extension yearly+ | O | 강함 | 강함 | fallback 유지 |
| LAVESI-FIRE | individual x,y, 0.2 m env grid | annual vegetation | 매우 강함 | 약함 | layer height O | 보조후보 |
| FireBGCv2 | stand + representative plot | daily ecology, annual tree update | 강함 | 강함 | 강함 | stand aggregation 때문에 탈락 |
| SORTIE-ND | individual x,y | annual+ | disturbance 가능 | 약함 | substrate 중심 | root state 부족 |
| TreeMig | 25 m 이상 cells, intercell seed dispersal | annual | disturbance 제한 | 약함 | 약함 | root/litter 부족 |
| PICUS | 10 m patches, spatial seed/light | annual growth, monthly climate | 제한적 | 약함 | 약함 | root/litter 부족 |
| SIBBORK | individual trees on real terrain | long-term gap dynamics | fire applications 존재 | 약함 | forest-floor C 미추적 | root/litter 부족 |
| RHESSys-WMFire | spatial patch/catchment | daily ecohydrology | fire effects O | 강함 | 강함 | true succession/migration 약함 |
| ED2/FATES | subgrid patch/cohort | fine ecological timestep | disturbance O | 강함 | 강함 | horizontal patch placement 비명시 |

## 가장 중요한 새 결론

### 1. LPJ-GM을 우선 코드검증
LPJ-GM은 standard LPJ-GUESS의 문제를 정확히 겨냥한다.

standard:
```
cell A LPJ-GUESS    cell B LPJ-GUESS
      X no seed exchange X
```

LPJ-GM:
```
cell A
  -> annual seed production
  -> spatial dispersal kernel
  -> seed bank / establishment in cell B
cell B
```

따라서 기존 고운사 LPJ-GUESS root/litter physiology를 버리지 않고 landscape succession을 추가할 가능성이 있다.

### 2. 그러나 published 30 m model이라고 부르면 안 됨
LPJ-GM 1.0/1.1의 vegetation local dynamics는 1 km cells에서 검증되었다.
LPJ-GM 1.1의 100 m는 dispersal-kernel numerical resolution이다.

따라서:
```
LPJ-GM at 30 m
```
은 아직 새 implementation hypothesis이다.

### 3. SEIB-DGVM은 complementary alternative
30 m virtual forest와 1 m internal grid는 고운사 DEM scale에 매우 매력적이고 fine-root/litter까지 제공한다.

그러나 public base distribution은 single virtual forest point simulation이다.
catchment-wide inter-plot seed exchange가 standard published function인지 확인되지 않았다.

## 다음 작업
LPJ-GM 2.0 source를 직접 검사한다.

반드시 확인:
1. local cell area/spacing hard-coded 여부
2. 30 m spacing 설정 가능 여부
3. SEEDISP kernel이 arbitrary resolution을 허용하는지
4. corridor 없이 약 4454 cells 전부 local dynamics 실행 가능 여부
5. current Gounsa LPJ-GUESS branch와 root/litter output 호환성
6. fire disturbance 직후 seed source/establishment 처리
7. MPI/FFT requirements on Windows/Linux

이 검증에서 30 m implementation이 과도한 개조를 요구하면:
- SEIB-DGVM multi-plot + explicit interplot seed dispersal
- LANDIS-II NECN 1-year coupling
순으로 비교한다.

## 기존 결정과의 관계
`2026-09-22_LANDISII_GEOMORPH_ARCHITECTURE.md`의 LANDIS-II + NECN은 폐기하지 않는다.
다만 식생축은 provisional 상태로 되돌리고, LPJ-GM 기술검증 후 최종 확정한다.
