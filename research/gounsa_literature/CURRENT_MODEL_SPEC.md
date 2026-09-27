# Gounsa CURRENT MODEL SPEC

업데이트: 2026-09-28

이 문서는 고운사 산불 후 식생-지형 상호작용 모델의 **현재 canonical specification**이다.

채팅 기록보다 이 파일을 우선한다. 새 문헌을 찾았다고 기존 결론을 자동으로 바꾸지 않는다. 기존안을 변경할 때에는 `decisions/`에 변경 이유와 근거를 기록한 뒤 이 파일을 갱신한다.

현재 모델은 하나의 기존 published model이 아니다. LPJ-GUESS와 여러 published process equations를 연결하는 **새로운 coupling**이다.

---

# 1. 연구 목표

고운사 산불 이후 약 100년 동안 다음 상호작용을 공간적으로 모의한다.

```text
외부 기후강제력 + 산불 교란
        ↓
식생 소실과 회복
        ↕
토양수분, 유출, 침식
        ↕
사면 물질이동
        ↕
풍화와 토양생산
        ↕
토심, 석력, 표면 암편, 지형 변화
        ↕
식생 성장과 천이
```

핵심은 식생을 단일 cover로 환원하지 않고, LPJ-GUESS의 PFT/cohort별 식생 상태와 토양 및 지형 상태를 상호 연결하는 것이다.

---

# 2. 외부 입력과 외부 교란

## 2.1 기후강제력

- 강우
- 기온
- CO2
- 태양복사

## 2.2 외부 교란

- 산불

산불은 독립된 내부 모듈이 아니라 외부 교란으로 취급한다.

산불은 최소한 다음 내부 상태에 영향을 준다.

- 상층 목본
- 하층 목본 및 초본
- 잎, 줄기, 뿌리 biomass
- 고사목
- 낙엽과 토양 유기물
- 토양 표면 상태
- 노출 기반암의 fire spalling

---

# 3. 식생 동태

## 현재 판정: 채택

식생 엔진은 **LPJ-GUESS**를 사용한다.

식생을 하나의 `vegetation cover`로 합치지 않는다.

최소 보존 상태변수:

- PFT/cohort별 `FineRootC_i`
- `LeafC_i`
- `WoodC_i`
- `SurfaceLitC`
- `NPP_i`
- 가능한 경우 DBH
- height
- density
- rooting-depth profile

개념적으로는 적어도 다음 식생층을 구별한다.

- 상층 목본
- 하층 목본
- 초본

LPJ-GUESS가 담당하는 핵심 과정:

- 활착
- 생장
- 번식
- 고사
- 경쟁
- 촉진
- 천이

## 새로운 coupling

다음 변환은 기존 단일 published model의 원래 기능이 아니므로 반드시 새로운 coupling이라고 표기한다.

```text
FineRootC_i -> root mass density / RLD / RSAD
FineRootC_i -> erosion resistance
FineRootC_i -> biogenic hillslope transport
WoodC/cohort state -> tree throw / CWD
NPP / root respiration -> chemical weathering effect
```

---

# 4. 핵심 토양 및 지표 상태변수

이 항목은 앞으로 모든 다이어그램과 코드에서 같은 정의를 사용한다.

## 4.1 토심 H

토양층의 물리적 두께.

주요 연결:

```text
풍화와 토양생산 -> H 증가
침식 -> H 감소
퇴적 -> H 증가
H -> 토양수분 저장능
H -> 식생 이용가능 토양량
H -> 뿌리 가용 공간
```

## 4.2 토성 texture

**2 mm 미만 fine-earth fraction**의 sand, silt, clay 구성.

토성과 석력비율은 같은 변수가 아니다.

주요 연결:

```text
texture -> 침투 및 수리특성
texture -> 수분보유
texture -> 침식성
texture -> 식생 수분이용
```

동적 토성 변화의 정량식은 아직 확정하지 않는다.

## 4.3 토양 내 석력비율 F_g

토양층 내부의 2 mm 이상 coarse-fragment fraction.

표면 암편량과 구별한다.

주요 연결:

```text
F_g + H -> 실제 fine-earth volume
F_g -> 토양수분 저장공간 및 수리특성
F_g -> 이동 가능한 세토량
F_g -> 뿌리가 이용 가능한 토양량
```

개념적으로 사용할 수 있는 파생량:

```text
H_fine ≈ H (1 - F_g)
```

단, 이 식을 production equation으로 채택한 것은 아니다. 상태변수 간 물리적 관계를 나타내기 위한 작업식이다.

## 4.4 표면 암편 저장량 또는 표면 암편 피복 R_s

토양 내부 석력비율과 별도의 지표 상태변수로 둔다.

증가 경로:

```text
fire spalling -> 새로운 암편 공급 -> R_s
세토 선택적 제거 -> 기존 석력 노출 -> R_s
상부사면 암편 이동 -> 재퇴적 -> R_s
```

감소 경로:

```text
중력성 암편 이동
유수에 의한 암편 운반
매몰 또는 토양 내 혼합
```

주요 효과:

```text
R_s -> 빗방울 충격 차단
R_s -> 침투 및 지표유출 변화
R_s -> 면상침식과 집중류침식 변화
R_s -> armour effect
```

### 중요한 금지 연결

```text
Fire spalling -> 토양 석력비율
```

을 직접 연결하지 않는다.

올바른 구조는 다음과 같다.

```text
Fire spalling
 -> 암편 공급
 -> 표면 암편 저장 R_s
 -> 이동 / 재퇴적 / 매몰 / 혼합
 -> 필요한 경우 토양 내 F_g 변화
```

## 4.5 토양 유기물 및 litter

- LPJ-GUESS의 고사와 litter flux에서 공급
- 수분저장, 침투, 표면보호, 침식저항에 영향
- 산불 후 급격히 감소할 수 있음

---

# 5. 수문

## 현재 판정: 과정은 필수, 최종 엔진 미확정

최소 상태와 flux:

- 침투
- 토양수분
- 증발산
- 지표유출

필수 연결:

```text
강우 -> 차단/throughfall -> 침투 또는 지표유출
토심 + 토성 + 석력비율 + 유기물 -> 토양수분 및 침투
식생 -> 차단, 증발산, 뿌리 수분이용
지형 -> 유출경로와 집수
지표유출 -> 유수침식
```

LPJ-GUESS 내부 수분상태와 storm-scale 2D surface hydraulics를 동일한 것으로 취급하지 않는다.

---

# 6. 유수침식

## 현재 판정: 구조 확정, 최종 2D engine 미확정

반드시 다음 두 과정을 분리한다.

```text
interrill / rainfall-driven detachment
rill 또는 flow-driven detachment
```

## 6.1 quantitative vegetation bridge

문헌에서 직접 확인된 강한 근거:

- WEPP: live/dead root biomass -> interrill `Ki` adjustment
- WEPP: live/dead root biomass + buried residue -> rill `Kr` adjustment
- Mao et al. 2010: dynamic vegetation/root/residue -> WEPP erosion parameter adjustment
- Gould et al. 2016: wildfire mountain watershed application
- PROMET/Waldmann: vegetation -> RLD -> erosion resistance
- ELM-Erosion: PFT-specific root biomass -> erosion resistance

LPJ-GUESS `FineRootC`를 이 변수들로 변환하는 것은 새로운 coupling이다.

## 6.2 genuine 2D erosion-engine 후보

현재 핵심 비교군:

- Wu et al. 2020
- Iber+ 2024
- PSEM_2D
- SERGHEI-SE
- McGuire lineage는 rill-network benchmark
- OpenLISEM은 postfire 비교 및 검증 계보

현재까지 다음 네 조건을 동시에 만족하는 단일 published model은 확인되지 않았다.

```text
genuine 2D
+ mountain / steep forest or postfire
+ quantitative vegetation state
+ rainfall/interrill vs flow/rill separation
```

따라서 2D hydraulic-erosion skeleton과 LPJ-GUESS vegetation bridge를 결합하면 새로운 coupling이다.

## 6.3 금지

- MUSLE을 최종 산지 유수침식식으로 사용하지 않는다.
- vegetation cover 하나를 root biomass와 동일시하지 않는다.
- field regression을 이미 검증된 numerical model이라고 쓰지 않는다.

---

# 7. 사면 물질이동

## 현재 판정: 구조 확정, 각 항의 최종 parameterization 일부 미확정

사면 이동은 하나의 단순 diffusion coefficient로 합치지 않는다.

작업 구조:

```text
q_hill
 = q_background
 + q_biogenic
 + q_dryravel
```

`q_biogenic` 안에서는 필요에 따라 다음을 구분한다.

```text
root growth / decay
+ tree throw
+ organismal transport
```

## 7.1 background transport

토심이 매우 얕은 고운사 조건을 반영할 수 있는 **depth-dependent transport** 계열을 우선한다.

현재 유력한 구현 계보:

- Landlab `DepthDependentDiffuser`
- Johnstone and Hilley 계열 토심 의존 transport

작업 형태:

```text
q_bg = -K H* (1 - exp(-H/H*)) grad(z)
```

얕은 토양에서는 대략 `q_bg ∝ H grad(z)`가 되어 soil availability limitation을 반영한다.

최종 parameter 값은 미확정이다.

## 7.2 biogenic transport

핵심 근거 계보:

- Gabet et al. 2003
- Gabet and Mudd 2010

LPJ-GUESS의 root mass, turnover, rooting depth와 연결하는 방향을 유지한다.

이 coupling의 계수는 아직 확정하지 않는다.

## 7.3 postfire dry ravel

Lamb et al. 2011의 vegetation sediment-storage loss/recovery를 독립과정으로 유지한다.

산불 후 식생이 사라지면서 저장되어 있던 loose sediment가 방출되는 과정을 의미한다.

## 7.4 표면 암편 이동

표면 암편은 단순히 `석력비율`로 흡수하지 않는다.

필수 구조:

```text
R_s
 -> 정지/저장
 또는
 -> 중력성 이동
 -> 하부사면 재퇴적 또는 하천 도달
```

암편 이동거리와 routing을 어떤 published particle-transport equation으로 계산할지는 아직 canonical하게 확정하지 않았다.

이 항은 현재 우선 미해결 문제이다.

---

# 8. 풍화와 토양생산

## 현재 판정: 구조는 있음, 최종 production equation 미확정

현재 작업 구조:

```text
W_total
 = W_hydroclimatic
 + W_deep_root_chemical
 + W_woody_mechanical
```

중요 원칙:

- root-access depth를 A/B horizon 두께와 동일시하지 않는다.
- 뿌리는 C/Cr까지 접근할 수 있다.
- 식생 영향 없는 단순 토심-풍화식 하나로 전체 과정을 끝내지 않는다.

토양생산은 개념적으로 다음 상태를 변화시킨다.

```text
기반암 -> regolith / soil
H 증가
암편 및 fine-earth 생산
```

## 석력 풍화와 토성 변화

석력과 암편이 풍화될 수 있다는 과정은 인정하지만, 고운사 production model에서 다음 변환의 정량식은 아직 확정하지 않았다.

```text
coarse fragment (>2 mm)
 -> weathering / fragmentation
 -> fine earth (<2 mm)
 -> sand / silt / clay composition change
```

따라서 현 단계에서 `석력비율 -> 토성`을 직접 화살표 하나로 연결하지 않는다.

필요한 경우 별도 `coarse-fragment weathering` flux를 정의한다.

---

# 9. Fire spalling과 coarse-fragment supply

## 현재 판정: source process 채택, 정량 production equation 미확정

Fire spalling은 dry ravel과 다른 과정이다.

```text
산불 외부 교란
 -> 노출 암반 열충격
 -> fire spalling
 -> 새로운 coarse-fragment supply
 -> 표면 암편 저장 R_s
```

그 이후에는 별도 transport process가 작동한다.

```text
R_s
 -> dry ravel / particle transport
 -> 재퇴적 또는 channel delivery
```

현재 unresolved gap:

- fire-spall fragment production rate
- fragment size distribution
- 표면 암편의 이동거리 및 routing
- 표면 암편의 매몰/혼합률
- coarse-fragment weathering rate

---

# 10. 지형 변화와 되먹임

지형 변화는 침식, 퇴적, 사면이동, 토양생산의 결과이다.

필수 상태:

- 고도 z
- 경사
- 곡률
- 집수면적 또는 drainage structure
- 토심 H

핵심 feedback:

```text
침식 / 퇴적 / 사면이동 / 토양생산
 -> z, slope, contributing area, H 변화
 -> 유출경로와 토양수분 변화
 -> 식생 성장과 경쟁 변화
 -> 다시 침식과 사면이동 변화
```

이 feedback이 고운사 모델의 핵심이다.

---

# 11. shallow landslide

## 현재 판정: 별도 과정으로 유지, core v1에서는 우선순위 낮음

유수침식의 root erodibility와 같은 parameter로 처리하지 않는다.

구조:

```text
FineRootC
 -> root distribution / architecture
 -> root reinforcement or c_r
 -> factor of safety
 -> shallow landslide
```

주요 근거 계보:

- Hales 2018
- Istanbulluoglu lineage

---

# 12. vertical soil mixing

## 현재 판정: lateral hillslope transport와 분리

MILESD, LORICA, HydroLorica, ChronoLorica 계열의 vertical profile mixing은 사면방향 sediment flux와 동일시하지 않는다.

core v1에서 반드시 필요한지 여부는 아직 미정이다.

---

# 13. 현재 canonical 상태변수 목록

## 외부 입력

- precipitation
- temperature
- CO2
- solar radiation
- fire disturbance

## 식생

- PFT/cohort identity
- FineRootC
- LeafC
- WoodC
- SurfaceLitC
- NPP
- optional DBH, height, density
- optional rooting-depth profile

## 토양 및 지표

- soil depth H
- soil texture of fine earth
- subsurface coarse-fragment fraction F_g
- surface rock-fragment storage or cover R_s
- soil organic matter / litter
- soil moisture

## 지형

- elevation z
- slope
- curvature
- contributing area / drainage structure

## sediment / material flux

- interrill detachment
- rill/flow-driven detachment
- deposition
- background hillslope transport
- biogenic hillslope transport
- dry ravel
- coarse-fragment transport
- weathering / soil production
- fire-spall fragment supply

---

# 14. 현재 확정도 표

| 항목 | 현재 상태 | canonical 판정 |
|---|---|---|
| 식생 엔진 | LPJ-GUESS | 채택 |
| 식생 상태 | PFT/cohort별 biomass와 root state | 채택 |
| 산불 | 외부 교란 | 채택 |
| 토심 | 동적 상태변수 | 채택 |
| 토성 | fine-earth texture, 석력과 분리 | 채택 |
| 토양 내 석력비율 | 독립 상태변수 | 채택 |
| 표면 암편 | 석력비율과 분리한 독립 상태 | 채택 |
| 유수침식 구조 | rainfall/interrill + flow/rill 분리 | 채택 |
| 유수침식 최종 2D engine | Wu/Iber+/기타 비교 중 | 미확정 |
| vegetation -> erosion bridge | WEPP/PROMET/ELM 계보 활용 | 구조 채택, coupling 미보정 |
| background hillslope transport | depth-dependent 구조 | 유력 |
| root-driven transport | Gabet 계보 | 유력 |
| tree throw | Gabet and Mudd 계보 | 유력, 필요도 재검토 |
| postfire dry ravel | Lamb 2011 | 채택 계보 |
| 표면 암편 routing | 별도 transport 필요 | 미확정 |
| fire-spall production | 독립 source process | 구조 채택, 식 미확정 |
| 풍화/토양생산 | 식생 영향을 포함한 구조 | 미확정 |
| 석력 풍화 -> fine earth | 가능 과정 | 정량식 미확정 |
| shallow landslide | 별도 root-reinforcement 과정 | 2단계 |
| vertical soil mixing | lateral flux와 분리 | 보류 |

---

# 15. 현재 우선 해결 문제

새로운 식생모델을 더 찾는 작업은 중단한다.

다음 미해결 사항만 우선 조사한다.

1. **유수침식 최종 2D engine 확정**
   - Wu et al. 2020
   - Iber+ 2024
   - 기타 strict 후보 비교

2. **표면 암편의 이동과 routing 식 확정**
   - slope
   - grain size
   - roughness
   - vegetation obstruction
   - deposition / channel delivery

3. **fire-spall fragment production 식 또는 parameterization 확보**

4. **풍화 및 soil/regolith production 최종식 확정**
   - hydroclimatic
   - deep-root chemical
   - woody mechanical

5. **FineRootC -> RMD/RLD/RSAD 변환계수 확정**

6. **토양 내 석력과 표면 암편의 exchange**
   - fines removal and exhumation
   - burial
   - mixing
   - coarse-fragment weathering

---

# 16. 다시 열지 않을 갈림길

- LPJ-GUESS 대신 새로운 식생모델을 처음부터 다시 찾지 않는다.
- COPLAS를 최종 모델 근거로 사용하지 않는다.
- MUSLE를 최종 산지 유수침식식으로 사용하지 않는다.
- Wu와 WEPP를 둘 중 하나만 고르는 문제로 되돌아가지 않는다. 역할이 다르다.
- vegetation cover 하나로 모든 식생효과를 처리하지 않는다.
- 토성, 토양 내 석력비율, 표면 암편량을 하나의 변수로 합치지 않는다.
- fire spalling을 dry ravel 자체로 취급하지 않는다.
- fire spalling이 토양 석력비율을 즉시 바꾼다고 가정하지 않는다.
- root-dependent erosion resistance와 landslide root cohesion을 같은 parameter로 사용하지 않는다.

---

# 17. 단일 개념도에서의 최소 연결

```text
기온, CO2, 태양복사 ----------------------> 상층식생 / 하층식생 / 초본
강우 ------------------------------------> 침투 / 토양수분 / 지표유출
토양수분 <------------------------------> 식생

식생 -> FineRootC / litter / woody state
FineRootC -------------------------------> 유수침식 저항
FineRootC -------------------------------> biogenic hillslope transport
litter ----------------------------------> 지표보호 / 토양유기물
woody state -----------------------------> tree throw / CWD

지표유출 ---------------------------------> 면상 및 집중류침식
토양 -------------------------------------> 이동 가능한 sediment
토심 + 석력비율 --------------------------> fine-earth availability

기반암 -----------------------------------> 풍화 및 토양생산 -> 토심 / 토양
산불 -------------------------------------> 식생 소실
산불 -------------------------------------> fire spalling -> 표면 암편 공급

표면 암편 -------------------------------> 유출 및 침식 조절
표면 암편 -------------------------------> 중력성 이동 / 재퇴적 / 하천도달
세토 선택적 제거 -------------------------> 기존 석력 노출 -> 표면 암편 증가
표면 암편의 매몰/혼합 --------------------> 토양 내 석력비율 변화

침식 + 퇴적 + 사면이동 + 토양생산
 -> 고도 / 경사 / 집수면적 / 토심 변화
 -> 유출 / 토양수분 / 식생 변화
 -> 다시 침식과 사면이동 변화
```

---

# 18. 근거가 되는 현재 결정 파일

- `decisions/2026-09-21_PROCESS_ARCHITECTURE.md`
- `decisions/2026-09-21_THREE_PROCESS_GEOMORPH_STRUCTURE.md`
- `decisions/2026-09-21_LPJGUESS_BIOMASS_COUPLING.md`
- `decisions/2026-09-21_COUPLING_BOUNDARY.md`
- `decisions/2026-09-21_STRICT_2D_QUANTITATIVE_VEGETATION.md`
- `decisions/2026-09-21_EXCLUSIONS.md`

세부 근거는 `MASTER.md`, `models/`, `papers/`를 따른다.
