# SWEHR 원본 논문과 공개 코드의 생태수문 및 강우박리 저감항 대조

## 핵심
McGuire et al. (2016, DOI 10.1002/2016JF003867) **논문 수식에는 Rutter 수관차단(§3.5 식24–26)과 수관의 직접 빗방울 충격 차폐(§3.2 식3–4)가 각각 포함**된다. 그러나 CSDMS github.com/csdms-contrib/swehr 공개 단일 `SWEHR.c` 파일에는 시간별 Rutter 수관저류/배수 `C, Tc, Kc, gc, S, Cv` 계산과 직접 수관차폐 계수가 모두 **없다**. 논문상 수식 ≠ 해당 공개 구현. 원논문은 Rutter로 수관저류와 유효강우를 산출하나 실제 Nov/Dec wildfire 관측 재현에서는 수관이 완전 연소해 interception을 제외(§3.8). 재생 민감도 모의에서는 Cv 0.05–0.95, Ks 2–11mm/h와 Tc=0.35, S=2.2mm, gc=3.9mm^-1, Kc=5e-5mm/s 사용(§4.3).

## 논문이 고려한 5개 별도 저감 또는 조절과정
1. **Rutter interception and drainage** (§3.5, 식24–26): 시간에 따라 canopy C 증가/배수 D, 지표 유효강우의 시간변화를 계산. 증발 E는 짧은 강우사상 조건이어서 논문 구현에서 생략. 빗물의 일시 저장을 증발 손실로 해석하면 안 됨. Source water budget와 canopy storage를 함께 적산해야 함.
2. **Canopy shielding of rainfall splash** (§3.2, 식3–4): 강우 박리와 재박리에만 별도 인자 `f_shield=(1-Cv)+Tc Cv`. Cv=식생 피복 비율, Tc=수관을 접촉하지 않고 통과하는 강우 비율. 이 인자는 수관차단에 따른 유효강우 변화와 물리적으로 다르며, 강우박리의 직접 충격효과를 감소시킨다. 수관 배수가 원래 빗방울 운동에너지를 그대로 갖는다고 보지 않음. SWEHR 논문 자체는 leaf-drip size/height-dependent kinetic energy model을 독립 구현하지 않음.
3. **Flow depth splash damping** (§3.2, 식5–6): h_perp>h0일 때 박리/재박리 계수에 `(h0/h_perp)^b`, h0 critical depth, b=1. 이는 물깊이에 의한 완화, 식생 계수가 아님. C code SWEHR.c 1348–1352 lines.
4. **Deposited sediment shielding** (§3.2, HR): `H=min(1, m_t/m_t*)`; original soil splash and flow detachment multiplied by 1-H, loose sediment redetachment affected by H. C code L1331–1338, L1365–1372. 식생 낙엽 또는 뿌리 피복 자체가 아님.
5. **Manning friction** (§3.3/§5): water-depth-dependent hydraulic roughness exists, but paper explicitly says dynamic vegetation cover→roughness coupling **not included** (§5 end). Code L1356–1360 and L1556–1560. Source `SF[i][j]` is *friction slope*, NOT stemflow.

## 공개코드 직접 정량 감사
https://github.com/csdms-contrib/swehr/blob/master/SWEHR.c
- 본 리포지토리 7개 파일: `SWEHR.c`, `input.txt`, `rain.txt`, `topoin.txt`, 입경 파일 2개, 라이선스; 별도 Rutter 함수/헤더 없음.
- `R=RAIN[rind]` L814, `E[1]=(1-H)*P[k]*ASMASK*R` L1338, `E[2]=H*M[k]/TOTM*ADSMASK*R` L1343, `U[1]+=dt*R` L1427; 같은 R로 물공급과 빗방울 충격 박리를 계산하므로 canopy water vs impact split 미구현.
- `ASMASK[i][j]=a`, `ADSMASK[i][j]=ad` L662–663; CV,Tc 처리 없음.
- `KS[i][j]=0` 기본 L239; 별도 Green-Ampt 침투 식 L1450 있음. 논문 관측 검증 시 사용한 ks는 별도로 보정, 공개 demo zero rainfall 시험설정과 다름.
- `SF[i][j] = MANNING²·q²/h^(10/3)` L1360 = 마찰경사. 이름만 보고 SF=stemflow라고 판단 금지.

## 실제 기존 고운사 spatial SWEHR 결합부 판정
- `spatial-vegetation-runoff-erosion-20261026` 브랜치의 `spatial_patch_swehr.py`: 신규 개발 `QA_WFACTOR(x,y)` (물공급), `QA_DFACTOR(x,y)` (원래 비방울 충격 박리 공급) 2항을 분리. 38개 QA pass; **원본 Rutter 모델을 구현한 것이 아니라 식생격자 저류량을 사건별 고정 최대 0.8mm로 단순화**, 수간유하우 공급위치에는 가정 10%를 이동함. 수관내 시간별 C(t), D(t), 증발 E(t), canopy balance over recession 등이 **없음**. SF 재배분은 출구 유사량 미세 차이, leaf drip size/impact energy 계산 없음. 이 인터페이스는 published SWEHR 기능이 아닌 새 coupling.
- source engineering: strong 2D sediment conservation does not validate site vegetation state. Need distinct `P_total` canopy storage, `P_water` and `P_impact` source ledgers plus stem base, no accidental double-counting of rain reduction.
- 1975 Rutter **원 모형**에는 stemflow / trunk compartment 확장. 그러나 McGuire 논문 2016 §3.5에 기술된 간략형에서는 별도 per-tree stemflow or trunk footprint source unspecified. Published Rutter capability ≠ SWEHR paper adaptation ≠ public C.

## 고운사 핵심 우선 순위
1. Original Rutter 1975/1972 (or independently verified canopy equations)를 실제 1h and recession/time-step C(t), D(t), E(t) 상태변수와 물수지로 구현하는 **new coupling**, 필요 시 leaf-on vs leafless species state.
2. `P_water(x,y,t)`: direct throughfall + drip + spatial stemflow (from observed oak stump/tussock geometry); `P_impact(x,y,t)`: free high KE rain and additional measured/published modeled leaf-drip kinetic energy. Throughfall ratio Tc and total water reaching soil are not interchangeable.
3. 별도 impact reduction `f_shield=(1-Cv)+TcCv`는 논문 계열 원형임. 다만 이미 high-energy direct TF 분율로 `P_impact`를 정의했다면 동일 shield 인자를 **또 곱하지 않음**. Leaf drip KE가 있으면 독립 impact contribution 산출하고 canopy factor 중복 적용 금지.
4. Vegetation rooting/litter, soil Ksat, surface roughness and source connectivity must be independent spatial variables, not a scalar C_v or hypothetical species multiplier.
5. Water balance: gross rainfall = surface inflow + atmospheric evaporation + delta canopy storage + boundary vapor/export where applicable. Direct rain/rain-energy impact and soil erosion tracked separately.
6. Validate numerical conservation (including canopy) against rainfall 10-50mm/h, 1h + rainfall cessation drainage before reporting grass vs oak sediment differences.

## 핵심 문헌
McGuire et al. (2016), JGR: Earth Surface 121(11), 2211–2237 https://doi.org/10.1002/2016JF003867
Rutter et al. (1972), Agricultural Meteorology 9, 367–384 https://doi.org/10.1016/0002-1571(71)90034-3
Rutter, Morton & Robins (1975), J Appl Ecology 12, 367–380 https://doi.org/10.2307/2401739
Source code https://github.com/csdms-contrib/swehr/blob/master/SWEHR.c
