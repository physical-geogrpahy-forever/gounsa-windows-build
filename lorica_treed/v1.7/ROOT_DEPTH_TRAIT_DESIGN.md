# v1.7 설계안: TREED 뿌리 깊이 형질

작성일 2026-11-16. 상태: 구현됨(`root_depth_mode`, 기본 `off`). 아래 3.3, 3.4, 4절은 설계 당시 안이고, 실제 구현은 바로 다음 박스와 같이 바뀌었다.

이 문서는 TREED에 뿌리 깊이를 10번째 형질로 넣는 방법을 정리한다. 모든 식과 매개변수에는 출처와 확인 수준을 붙였다. 확인 수준은 세 가지다.

- **확인**: 논문 본문이나 초록, 저자 자료에서 이번 작업 중 직접 읽은 것
- **부분 확인**: 2차 인용이나 발표자료로만 본 것. 구현 전에 원문 식 번호 대조 필요
- **가정**: 문헌 근거 없이 이 설계에서 새로 정한 것

> **구현에서 바뀐 점 (2026-11-16)**
>
> - **비용**: 3.3의 수송뿌리 비용(`SA * z_mean * WD`)은 쓰지 않았다. Guswa(2008) 식 1의 `C = γr * RLD / SRL` 꼴로, 깊이에 비례하는 세근 유지비를 `cost * z_eff`(g C m-2 yr-1)로 회전율 항에 더했다. 계수는 표 1(사바나)에서 14.0, 표 2에서 146.1이 나오며, 한국 실측이 아니므로 둘 다 민감도로 돌린다.
> - **최적화**: 3.4의 `x[4]` 방식(ECA 4차원)은 쓰지 않았다. 시험해 보니 씨앗마다 `z_opt`가 0.1에서 2.8 m까지 흩어졌다. 기존 3차원 ECA([a_ll, C_leaf, H])는 그대로 두고, 그 뒤에 `z_r`만 0.05 m 간격 격자로 결정론적으로 탐색한다. 동률이면 가장 얕은 깊이를 고른다.
> - **물 공급**: 월별 강우일 비율 α와 평균 강우량 λ(LORICA가 `rain_event_stats_monthly.csv`로 내보냄)로 Guswa 식 12 꼴의 평균 증산을 계산한다(`milly_stochastic`). 저장 용량은 `PAW * z_eff / 토심`이다. 월 단위 정상 상태를 가정하므로 달을 넘는 이월은 없다. `bucket_monthly`는 비교용이다.
> - **입력**: 층별 누적 PAW는 쓰지 않았다. PAW가 토심 전체에 균일하다고 가정했다.
> - **상태**: `z_r`은 `rootdepth_restart.jld2`에 저장한다. 분산 블록(`run_TREED_ecology`)에는 아직 넣지 않았다(2단계에서 한다).
> - **LORICA 쪽 물 수지에는 되먹임하지 않는다.** `z_r`은 TREED의 증산 공급과 탄소 비용에만 들어간다. LORICA의 토양수 계산을 통일하는 일은 3단계 과제다.

## 1. 왜 새로 정의해야 하는가

upstream TREED(julrogger/TREED, 커밋 03ac783)를 직접 읽은 결과다.

| 항목 | upstream 코드 | 의미 |
|---|---|---|
| 물 공급 | `Esupply = min.(Emax, precip_monthly*1000)`, Emax = 5 mm/day (`TREED_physiological_functions.jl` 188-189행) | 토양 저장이 없다. 그 달 강수만 쓴다 |
| 뿌리 형질 | 최적화에서 `r_s_r = 1` 고정 (509행), `r_s_r_optimized = 1.` (561행) | 뿌리는 변하지 않는다 |
| 뿌리 비용 | 세근 호흡과 회전, 굵은뿌리 회전(1/15). 굵은뿌리 호흡 계수는 0 | 뿌리는 비용만 있고 편익이 없다 |
| 뿌리 깊이 | 없음 | |

따라서 뿌리 깊이 형질을 넣으려면 편익 항을 새로 만들어야 한다. 고운사 번들이 추가한 PAW 항(`strength * r_s_r/(r_s_r+halfsat) * PAW/365`)은 저장량을 365일로 나눠 매달 똑같이 더하는 방식이라 물수지가 닫히지 않고 깊이 개념도 없다. 이 설계는 그 항을 대체한다.

## 2. 문헌에서 확인한 것

### 2.1 뿌리 깊이는 비용과 편익의 균형으로 정해진다

- Guswa (2008, WRR 44, W02427): 깊은 뿌리의 한계 탄소 비용과 한계 편익이 같아지는 깊이가 최적 깊이다. 비용은 `C = γr * RLD / SRL * Zr`(뿌리 호흡률, 뿌리길이밀도, 비근장), 편익은 `B = WUE * T(Zr)`. 토양수분은 확률적 강우로 구동된다. 수분 제한 환경에서는 강우 빈도보다 강우 사상의 크기에 더 민감하다. **확인**(초록, 저자 발표자료). 닫힌 해의 정확한 꼴은 **부분 확인**.
- Kleidon & Heimann (1998, GCB 4:275-286): 지구 식생모델에서 NPP를 최대로 하는 뿌리 깊이를 찾았다. 뿌리 깊이는 토양 저장고 크기를 정하는 매개변수로 들어간다. 이 논문은 뿌리 비용을 명시적으로 넣지 않았다는 점을 스스로 밝힌다. **확인**.
- Schymanski et al. (2008, HESS 12:913): 수요를 충족하면서 뿌리 비용을 최소화하는 뿌리 분포. **부분 확인**.
- Speich et al. (2018, HESS 22:4097): Guswa 모델을 온대 15개 지점에 적용. 뿌리권 저장용량 `Sr = κ * Ze`. **부분 확인**.

### 2.2 토심이 뿌리 깊이의 상한이다

- Sakschewski et al. (2021, BG 18:4091), LPJmL4.0-VR: Jackson 분포를 토심에서 잘라 재정규화한다. `rootdist(z) = (1 - β^z) / (1 - β^z_bottom)`, z는 cm. 격자별 토심이 최대 뿌리 깊이를 제한한다. 뿌리 깊이는 나무 키의 로지스틱 함수로 자라고, 굵은뿌리(뿌리 변재)는 파이프 모델로 계산한다. 논문은 뿌리가 깊어질수록 굵은뿌리 비용이 크게 늘어난다고 적는다. **확인**(식 A1, A2, A3, A5). 층별 뿌리 변재 탄소식은 읽지 못했다.
- Jackson et al. (1996): `Y = 1 - β^d`, d는 cm. 온대 침엽수림 β = 0.976, 온대 낙엽수림 β = 0.966. **확인**(이전 단계).
- Schenk & Jackson (2002): 뿌리 프로파일의 90% 이상에서 뿌리의 절반이 상부 0.3 m 안에, 95%가 상부 2 m 안에 있다. **확인**(이전 단계).
- Fan et al. (2017, PNAS 114:10572): 배수가 좋은 고지대에서 뿌리 깊이는 강수 침투 깊이를 따른다. 저지대에서는 지하수면 위에 머문다. **확인**(초록). Pierret & Lacombe (2018)가 관측 편향 문제를 제기했고 저자들도 인정했다.
- Schwinning (2010, Ecohydrology 3:238): 얕은 토양 아래 풍화암이나 균열에서도 식물이 물을 쓴다. 다만 이런 기질은 접근 가능한 저장량을 줄이는 경향이 있다. **확인**(초록, 학회 초록).

### 2.3 뿌리 보강은 미끄럼면을 가로지르는 뿌리로 정해진다

- Cohen & Schwarz (2017, ESurf 5:451): 뿌리 보강은 기저, 측면, 토체 강성 증가의 세 가지다. 기저 보강이 있으면 가장 효율적이지만 파괴면이 뿌리권보다 깊으면 없다. **확인**.
- Giadrossich et al. (preprint): 기저 보강은 얕은 토양과 균열 암반 조건에서 나타난다. 측면 보강은 산사태 면적이 커질수록 비중이 줄어든다. **확인**.
- Wu/Waldron 모델은 모든 뿌리가 동시에 끊어진다고 가정해 과대평가한다. 섬유다발 모델 보정계수 k'' 는 0.3에서 1.0 범위로 보고된다(Pollen & Simon 2005, Mao et al. 2012, Bischetti et al. 2009를 인용한 2차 문헌). 과대평가가 최대 3배라는 보고도 있다(Hales 2017이 Cohen et al. 2011, Schwarz et al. 2010을 인용). **부분 확인**.
- Hwang et al. (2015, JGR-BG 120:361-378): Coweeta 토양 단면 실측에서 지하부 생물량과 뿌리 응집력 관계를 만들었다. **확인**(서지, 초록). 현재 코드의 `Cr = K * Tr * Br / ρr` 식 번호와 K = 1.2, ρr = 435.3은 번들 주석 기준이며 원문 대조는 하지 못했다.
- 국내 자료: Oh et al. (2011) 평균 뿌리 인장강도. 소나무 176.25, 신갈나무 224.19 kgf/cm². **확인**(초록). 현재 코드 값과 일치한다. Kim et al. (2011): 일본잎갈나무와 잣나무에서 뿌리 단면적이 깊이에 따라 지수적으로 감소, 평균 RAR 0.03%와 0.10%, Wu 모델 응집력 4.04와 12.26 kPa. **확인**(초록). 소나무와 신갈나무의 깊이별 RAR 실측값은 찾지 못했다.

## 3. 설계

### 3.1 형질 정의

`z_r` [m]: 잠재 뿌리 깊이. 뿌리의 95%가 들어가는 깊이(D95)로 정의한다.

- Jackson β로 환산: `β = 0.05^(1 / (100 * z_r))`
- 검산: β = 0.976이면 D95 = 1.23 m, β = 0.966이면 D95 = 0.87 m
- 실현 깊이: `z_eff = min(z_r, z_soil + f_rock * (z_r - z_soil))`. `f_rock`은 풍화암 침투 비율로 기본값 0. **가정**(Schwinning 2010의 정성적 근거만 있음)
- 뿌리 분포는 LPJmL4.0-VR과 같이 `z_eff`에서 잘라 재정규화한다

형질 범위는 [0.05, 3.0] m로 제안한다. **가정**. 상한 3 m는 Schenk & Jackson의 "95%가 2 m 안" 범위를 조금 넘는 값이다.

### 3.2 편익: 뿌리권 물 저장

뿌리권 저장용량:

`S_r [mm] = Σ_layer PAW_layer(z) (지표부터 z_eff까지)`

PAW는 LORICA가 이미 Saxton & Rawls 식으로 층별 계산한다(`treed_paw_mm`). 지금은 전체 합만 넘기므로 층별 누적값을 넘기도록 교환 파일을 바꾼다.

물 공급은 두 방식을 옵션으로 둔다.

**방식 A, 월 버킷** (`root_depth_mode = bucket_monthly`)

```
W[m+1] = clamp(W[m] + P[m]*days - AET[m]*days, 0, S_r)
Esupply[m] = min(Emax, P[m] + W[m]/days)
AET[m] = min(Esupply[m], Edemand[m])
```

12개월을 2회 순환해 주기 정상상태를 만든다. 단순하고 물수지가 닫힌다. 한계는 월 합계만 보기 때문에 달 안의 건조 기간을 못 본다는 점이다.

**방식 B, 확률적 저장** (`root_depth_mode = milly_stochastic`), 권장

달마다 평균 강우 사상 크기 α [mm]와 빈도 λ [1/day]를 쓴다. LORICA는 일 강우를 갖고 있으므로 월별 α, λ를 계산해 넘길 수 있다.

```
γ = S_r / α
W = α * λ / Edemand
E/P = (exp(γ*(1-W)) - 1) / (exp(γ*(1-W)) - W)
Esupply[m] = min(Emax, (E/P) * α * λ)
```

이 식은 Milly (1993) 저장 모델의 꼴이며 Guswa (2008)가 쓴 것과 같은 계열이다. **부분 확인**. 원문 식 번호는 대조하지 못했다. 극한값은 직접 검산했다. γ가 무한대이고 W가 1보다 작으면 E/P = 1(유출 없음), W가 1보다 크면 E = Edemand, W가 0으로 가면 E/P = 1 - exp(-γ)(저장용량을 넘는 강우만 손실).

방식 B를 권하는 이유는 연구 질문과 직접 닿기 때문이다. 같은 월 강수량이라도 강우가 몇 번의 큰 사상으로 몰리면 얕은 토양에서는 쓸 수 있는 물이 줄어든다. 집중호우 시나리오가 산사태뿐 아니라 식생의 물 이용에도 영향을 주게 된다.

예시 계산이다. 아래 기후값은 설명용 **가정**이며 고운사 관측값이 아니다. PAW 0.12 m/m 가정.

| 조건 | 토심 0.1 m | 0.3 m | 1.0 m |
|---|---|---|---|
| 5월 80 mm, 강우일 8, 수요 3.5 mm/day | 0.43 | 0.63 | 0.73 |
| 7월 230 mm, 강우일 14, 수요 4.0 mm/day | 0.65 | 0.92 | 1.00 |
| 5월 80 mm, 강우일 12 | 0.51 | 0.68 | 0.74 |
| 5월 80 mm, 강우일 4 | 0.29 | 0.51 | 0.69 |
| 5월 80 mm, 강우일 2 | 0.18 | 0.37 | 0.60 |

값은 증산 충족률(T/Tpot)이다. 0.3 m보다 깊어지면 편익 증가가 빠르게 줄어든다. 강우가 몰릴수록 깊은 뿌리의 상대적 이점이 커진다.

### 3.3 비용

**수송뿌리(굵은뿌리) 비용**. TREED는 변재를 `C_sapwood = SA * H * WD_sapwood`로 계산한다. 같은 파이프 논리를 지하로 연장한다.

`C_root_transport = SA * z_mean * WD_sapwood`

`z_mean`은 잘린 Jackson 분포의 평균 뿌리 깊이다. 잘리지 않은 경우 `z_mean = -1/ln(β)` cm이고 β = 0.976이면 0.41 m다. LPJmL4.0-VR의 뿌리 변재 처리(첫 층에서 줄기 변재 단면적과 같고 아래로 갈수록 위쪽 세근 누적 비율만큼 감소)를 깊이 적분하면 이 꼴이 된다. 유도는 이 설계에서 한 것이므로 **가정**으로 분류한다. 회전율은 기존 `f_coarseroot = 1/15`를 쓴다.

**주의할 점**. 이 비용은 작다. z_mean 0.4 m는 나무 키 20 m에 비해 2%다. 따라서 최적화는 대부분 "토양을 다 채운다"로 수렴할 가능성이 높다. 이는 Schenk & Jackson의 관측(얕은 토양에서 뿌리가 토층 전체를 차지)과 어긋나지 않지만, 형질 변이가 토심 상한에 묶여 버릴 수 있다. 두 가지 보완을 민감도 옵션으로 둔다.

- 세근 밀도 조건: Guswa처럼 세근 질량이 깊이에 비례하도록 `C_fineroot = ρ_fr * z_eff * CA`로 바꾸는 방식. `ρ_fr = RLD/SRL`. 이 경우 `r_s_r`은 결과값이 되고 고운사 번들의 `adaptive_experimental` 모드는 필요 없어진다. Guswa의 무차원 비용 A = 5e-5 mm⁻¹ 값은 발표자료에서만 봤다. **부분 확인**. upstream의 `r_s_r = 1` 가정을 바꾸므로 기본값으로 쓰지 않는다
- 굵은뿌리 호흡: upstream은 계수가 0이다. 그대로 둔다

### 3.4 최적화와 진화

- 최적화 변수에 `x[4] = z_r` 추가. 경계 [0.05, 3.0]
- 목적함수는 그대로다(순탄소이득이 0이 되는 최대 키). 뿌리 깊이는 GPP(물)와 비용 양쪽으로 들어간다
- 진화: `z_r_new = z_r + evorate * (z_r_opt - z_r)`. 다른 형질과 같은 규칙
- 분산 선택 블록(`run_TREED_ecology`)에 `z_r`을 추가한다. 2단계에서 분산을 켤 때 필요하다

### 3.5 시간 불일치가 나타나는 지점

- 산사태로 토양이 벗겨지면 `z_soil`이 즉시 줄어든다. `z_r`은 `evorate` 속도로만 따라온다
- 토양이 다시 두꺼워지는 쪽(퇴적부, 토양 생성 회복)에서는 형질이 얕은 채 남아 물을 덜 쓴다. 지형 변화가 형질 적응보다 빠를 때의 손실이 여기서 나온다
- `z_r > z_soil`인 군집은 뿌리가 토양과 암반 경계에 몰린다. 4단계에서 이 부분이 기저 보강으로 연결된다

### 3.6 뿌리 보강과의 연결 (4단계 예고, 이번 구현 범위 밖)

미끄럼면 깊이 z에서의 뿌리 면적비:

`RAR(z) ≈ (Br/ρr) * (-100 * ln β) * β^(100z)`

`Cr_basal = k' * k'' * Tr * RAR(z_slip)`

k' = 1.2(Wu), k''는 0.3에서 1.0. 현재 코드의 0.447 "stress forcing"은 k'' 범위 안에 들어간다. 4단계에서 이 계수를 섬유다발 보정계수로 재해석할 수 있는지 검토한다. 측면 보강은 격자 크기와 산사태 면적에 의존하므로 별도로 다룬다.

## 4. 코드 삽입 지점

upstream 행 번호 기준이다. 고운사 번들은 PAW 항 때문에 몇 행씩 밀려 있다.

| 파일 | 위치 | 변경 |
|---|---|---|
| `TREED_model_functions.jl` | 28행 traits 구조체, 142행 초기화 | `z_r` 래스터 추가 |
| `TREED_physiological_functions.jl` | `plant_allometry` (10-78행) | `z_eff`, `z_mean`, `C_root_transport` 계산 |
| 같은 파일 | 188-189행 Esupply | 모드별 분기. `off`면 기존 식 그대로 |
| 같은 파일 | 회전 함수 422-455행 | 수송뿌리 회전 추가 |
| 같은 파일 | 최적화 500-512행, 549-551행 | `x[4]`, 경계 |
| 같은 파일 | `trait_evolution` 580행 부근 | `new_z_r` |
| `TREED_model_functions.jl` | `run_TREED_ecology` | 분산 블록에 `z_r` |
| `TREEDlocalstep.jl`, `treed_lorica_driver.jl` | 입력 | 층별 누적 PAW, 월별 α와 λ |
| `treed_coupling.cs` | `treed_paw_mm` 부근 | 깊이별 누적 PAW 출력, 월별 강우 통계 출력, 재시작 파일에 `z_r` |

원칙은 v1.6과 같다. 기본값 `root_depth_mode = off`에서 v1.5, v1.6 결과와 바이트 단위로 같아야 한다. upstream 생리 함수는 지우지 않고 분기로 추가한다.

## 5. 검증 계획

1. **회귀**: `off` 모드에서 v1.5 회귀와 v1.6 A/B 결과가 바이트 동일
2. **물수지 폐합**: 방식 A에서 연간 `ΣP = ΣAET + Σ유출 + ΔW`, 오차 1e-6 mm 이하
3. **극한 검사**: 방식 B에서 S_r이 0이면 Esupply가 0에 수렴, S_r이 매우 크면 `min(P, Edemand)`에 수렴
4. **단조성**: 다른 조건이 같을 때 토심이 깊을수록 GPP가 줄지 않는다
5. **토심 기울기 실험**: 토심 0.05, 0.1, 0.3, 0.6, 1.0, 2.0 m에서 최적 `z_r`과 H. 최적 `z_r`이 전 구간에서 토심 상한에 붙는지 확인한다. 붙으면 3.3의 보완 옵션을 평가한다
6. **강우 집중도 실험**: 월 강수량 고정, 강우일수만 바꿔 최적 `z_r` 변화 확인
7. **지연 실험**: 평형 후 토심을 1.0에서 0.3 m로 줄였다가 되돌리고 `evorate` 0.01, 0.1, 1.0에서 `z_r` 궤적 비교
8. **현실성 점검**: 고운사 조건에서 나온 최적 `z_r`을 Jackson의 온대림 D95(0.87에서 1.23 m)와 비교. 맞추기 위한 보정은 하지 않고 차이를 그대로 보고한다

## 6. 매개변수 표

| 매개변수 | 값 | 출처 | 확인 수준 |
|---|---|---|---|
| β 온대 침엽수 / 낙엽수 | 0.976 / 0.966 | Jackson et al. 1996 | 확인 |
| 분포 절단과 재정규화 | 식 A2 | Sakschewski et al. 2021 | 확인 |
| Emax | 5 mm/day | upstream TREED | 확인 |
| PAW | Saxton & Rawls, LORICA 기존 함수 | 번들 코드 | 확인(코드) |
| 저장 모델 E/P 식 | 3.2절 | Milly 1993, Guswa 2008 | 부분 확인 |
| f_coarseroot | 1/15 | upstream TREED | 확인 |
| WD_sapwood, SA | upstream 값 | upstream TREED | 확인 |
| 수송뿌리 식 | SA * z_mean * WD | 이 설계 | 가정 |
| z_r 범위 | 0.05 - 3.0 m | 이 설계 | 가정 |
| f_rock | 0 | 이 설계 | 가정 |
| k' | 1.2 | Wu 계열, Preti et al. 2010 인용 | 부분 확인 |
| k'' | 0.3 - 1.0 | Pollen & Simon 2005 등 | 부분 확인 |
| Tr 소나무 / 신갈나무 | 17.28 / 21.99 MPa | Oh et al. 2011 | 확인 |

## 7. 구현 전에 남은 확인 사항

- Guswa (2008) 본문의 T(Zr) 식과 비용 매개변수 값을 원문에서 옮겨 적기
- Milly (1993) 원문 식 대조
- Hwang et al. (2015) 식 5의 K와 ρr 값 원문 대조
- 소나무, 신갈나무의 깊이별 뿌리 분포 실측 자료(Cha et al. 2002, 한국임학회지 91:71-78이 후보)
- v1.6 보고서 정정: "번들 원본 기준"이라고 적은 TREED 행 번호는 이미 고운사 수정이 들어간 파일 기준이다. 진짜 upstream과는 다르다

## 참고문헌

- Cohen, D., Schwarz, M. (2017). Tree-root control of shallow landslides. Earth Surf. Dynam. 5:451-477. doi:10.5194/esurf-5-451-2017
- Fan, Y. et al. (2017). Hydrologic regulation of plant rooting depth. PNAS 114:10572-10577. doi:10.1073/pnas.1712381114
- Guswa, A.J. (2008). The influence of climate on root depth: A carbon cost-benefit analysis. WRR 44:W02427. doi:10.1029/2007WR006384
- Hwang, T. et al. (2015). Simulating vegetation controls on hurricane-induced shallow landslides with a distributed ecohydrological model. JGR-Biogeosciences 120:361-378. doi:10.1002/2014JG002824
- Jackson, R.B. et al. (1996). A global analysis of root distributions for terrestrial biomes. Oecologia 108:389-411
- Kim, D., Lee, S.H., Im, S. (2011). 뿌리의 공간분포를 고려한 수목 뿌리의 토양보강 효과에 대한 분석. 한국환경복원기술학회지
- Kleidon, A., Heimann, M. (1998). A method of determining rooting depth from a terrestrial biosphere model. GCB 4:275-286. doi:10.1046/j.1365-2486.1998.00152.x
- Oh, J.H., Hwang, J.S., Cha, D.S. (2011). 교목류 뿌리의 비탈면 안정효과 분석. 한국환경생태학회지 25(1):31-36
- Rogger, J. et al. (2026). TREED. GMD 19:4931
- Sakschewski, B. et al. (2021). Variable tree rooting strategies are key for modelling the distribution, productivity and evapotranspiration of tropical evergreen forests. Biogeosciences 18:4091-4116. doi:10.5194/bg-18-4091-2021
- Schenk, H.J., Jackson, R.B. (2002). The global biogeography of roots. Ecol. Monogr. 72:311-328
- Schwarz, M., Lehmann, P., Or, D. (2010). Quantifying lateral root reinforcement in steep slopes. ESPL 35:354-367. doi:10.1002/esp.1927
- Schwinning, S. (2010). The ecohydrology of roots in rocks. Ecohydrology 3:238-245. doi:10.1002/eco.134
- Speich, M.J.R. et al. (2018). HESS 22:4097
