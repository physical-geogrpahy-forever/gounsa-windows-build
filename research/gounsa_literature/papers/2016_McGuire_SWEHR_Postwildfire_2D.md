# 서지정보
McGuire, L. A., Kean, J. W., Staley, D. M., Rengers, F. K., & Wasklewicz, T. A. (2016). Constraining the relative importance of raindrop- and flow-driven sediment transport mechanisms in postwildfire environments and implications for recovery time scales. *Journal of Geophysical Research: Earth Surface, 121*(11), 2211–2237. https://doi.org/10.1002/2016JF003867

# 이 논문을 찾은 이유
산불 후 환경에서 2D shallow-water와 morphodynamics를 함께 계산하는 모델을 찾기 위해 검토했다.

# 연구 유형
- 수치모델
- postwildfire erosion

# 공간 구조
- 2D shallow-water 계열

# 적용 환경
- postwildfire hillslope/catchment

# 핵심 과정
- canopy interception
- infiltration
- 2D runoff
- Hairsine-Rose 계열 sediment/morphodynamics

# 식생 입력
- 주로 vegetation cover fraction
- quantitative root biomass 직접입력은 확인되지 않음

# 핵심 식
이번 세션에서 원식 전체는 복구되지 않았다. **원문 재검증 필요**.

# 파라미터와 단위
원문 재검증 필요.

# 원 논문의 구현 범위
산불 후 2D runoff-erosion-morphodynamics.

# 고운사에 직접 사용할 수 있는 부분
postfire 2D 모델이라는 점의 구조적 선례.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC/LitterC를 직접 연결하려면 **새로운 coupling**.

# 한계
vegetation effect가 cover 중심이므로 고운사의 strict quantitative-vegetation 조건을 충족하지 않는다.

# 최종 판정
**보조근거.** 산불 후 2D 적용 선례지만 최종 vegetation coupling 후보에서는 우선순위 낮음.


# 2026-10-26 원 논문 및 공개코드 대조 정정

- 원 논문은 Southern California 2009 Station Fire 후 Arroyo Seco의 0.01 km² 유역을 연구하고, 37.5 cm TLS DEM과 고해상도 관측자료로 공간적인 침식/퇴적 패턴을 검증했다. 2009-11-12 약 1시간 폭우의 5분 최대강도 약 80 mm/h.
- 원 논문의 해당 11월 사건 수치모의는 약 64 m³의 침식체적을 제시하며, 흐름박리 항을 끈 F=0 비교는 약 17 m³였다. 면적은 원 전체 유역과 실제 계산 process domains를 혼동하면 안 되므로 이를 임의로 t/ha로 환산하지 않는다.
- 복구된 공개 코드: https://github.com/csdms-contrib/swehr , 출처 커밋 4e6f783f335ac6dc1c116ef0d516c2f3d1b911e2 . 해당 example "input.txt" 는 nx=3, ny=51, dx=0.25m, F=0.004, a=0, ad=0, 600초로 제공. "rain.txt"에는 0이 입력되어 있으므로 **논문 검증실험의 시나리오 입력이 아니라 영강우 공개 테스트**. Hairsine–Rose 원토양 / 퇴적층 분리 및 다입경 계산은 원 논문 구현이지만 고운사 현장 입력은 별도로 정해야 한다.
- 공개 코드 initialcondition 함수에서 KS[i][j]=0; U[1] 초기값과 SOLID/M 초기화가 명시적으로 확인되지 않는다. 단, C/C++ 메모리 초기화의 우연한 동작 등 실제 런타임 문제는 별도 테스트로 단정해야 한다.
- GitHub 원본 C를 그대로 10–50 mm/h, 1시간으로 변경한 테스트에서는 all five return code=0이었으나 출력의 좌표정렬을 올바르게 맞춘 뒤 gross erosion ≈0.01907m³ vs gross deposition ≈0.549–0.553m³으로 나타났다. 10~50mm/h 강우 차이에 거의 반응하지 않고, 토사 경계유입과 모델 초기지형 전처리 변화를 설명하지 못했다. 재현가능한 침식 민감도로 **기각**. 원론적 SWEHR 이론이 불가능하다는 뜻 아님.
- 공개 코드의 경계조건은 i=1/nx 및 j=ny solid, j=1 transmissive. 초기조건 함수의 작동과 boundary flux를 추적하지 않으면 h를 직접 강우 유출량으로 오판할 수 있다. 유수박리 F=0.004는 0이 아니므로 a=ad=0이라고 total erosion=0이라는 주장도 잘못.
- 원 논문은 수관저류 등 요소를 기술하나 공개 예제는 수간유하우의 나무별 공간 집중 입력을 포함하지 않음.
- 본 논문 결과의 현장값과 독립적 원본 공개 코드의 불안정한 예제 출력을 엄격히 분리한다.

원 논문: https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2016JF003867
실험 QA: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40252527690

## 2026-10-26 Rutter 수관차단과 별도의 강우박리 저감 원문-소스 대조 확정

앞의 `# 핵심 식`에 적었던 "원문 재검증 필요"는 이 항목에 대해 해결됨. 정확한 원문: [McGuire et al. 2016 full text](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2016JF003867), §3.2 식(3)–(7), §3.5 식(24)–(26), §4.3 및 §5. 공개 C: [SWEHR.c](https://github.com/csdms-contrib/swehr/blob/master/SWEHR.c).

**논문에 포함된 두 개의 독립적인 수관 관련 과정**:
1. Rutter canopy interception: 시간별 수관 저류 C, throughfall coefficient Tc, drainage D, canopy capacity S, Kc, gc. 짧은 사건에서 E=0으로 간략화, 지표 도달 유효강우의 시간변화. 논문의 수관저류 식24, drainage 식25, 지표도달 강우 식26.
2. 직접 빗방울 강우박리 및 퇴적층 재박리에 적용한 별도 canopy impact shielding 계수 `(1−Cv)+Tc Cv`. 식생 피복 Cv는 부분 차폐, Tc는 canopy에 닿지 않은 직접 강우 비율. 강우량 차단(수관 물 저장)과 다른 기계적 효과. 단, 수관 적하의 새로운 방울 크기·유효 낙하높이·운동에너지는 별도 명시적 kinetic-energy 계산이 없고, 이 간략계수로 표현.

**식생과 다른 저감항**:
- 같은 §3.2 수심 h가 h0보다 클 때 rainfall detachment multiplier `(h0/h_vertical)^b` (b=1) 적용, 원본 공개 코드 L1348–1352 확인.
- 떨어진 퇴적층의 원토양 보호 `H=min(1,TOTM/mtstar)`와 `1−H`, 공개 C L1331–1343 및 L1365–1372 확인.
- roughness-Manning은 수심 의존하지만 실제 식생 Cv와 자동 결합되지 않음. 논문 §5 에 vegetation recovery→roughness 반영을 미구현 사항으로 명시.

**소스 코드 직접 감사 결과**:
- `SWEHR.c` 전체 검색에서 독립 `Cv`, `Tc`, `Kc`, `gc`, `Rutter`, `canopy storage C` 및 stemflow 저장고/함수가 없음. `R=RAIN[rind]` L814.
- 강우박리 `E[1]=(1-H)*P[k]*ASMASK*R` L1338, 재박리 `E[2]=H*M[k]/TOTM*ADSMASK*R` L1343; 유수량 `U[1]+=dt*R` L1427. 물과 강우충격이 동일 R을 사용하므로 식생 shielding이 입력된 것이 아님.
- `SF` 변수 L1360은 *Manning friction slope*, 수간유하우가 절대 아님.
- 원논문은 실제 2009년 11월 및 12월 산불 직후 사건에서는 수관이 거의 완전 소실되어 interception을 의도적으로 생략(§3.8), 식생 회복 20×5 m 가상사면에서는 Cv0.05–0.95, Ks2–11mm/h, Tc0.35, S2.2mm, gc3.9mm⁻¹, Kc5×10⁻⁵mm/s 사용. 30분 높은 강우사상에서 raindrop-only erosion은 Cv 변화에 따라 ~5배 이상 감소, flow-only erosion은 Ks 영향이 크며 Cv 영향은 2배 미만. 이는 **원문 모형 시뮬레이션 결과이지 공개 C 및 고운사 현장 재현 결과는 아님**.

**고운사 결정**: 원본 SWEHR 이론에는 두 과정이 들어가 있으나 공개 C에는 둘 다 없음. 기존 공간형 38회 유효강우차감/강우충격 계수는 별도 신규 coupling이지만 원래 Rutter 동적수지 및 수관방울 에너지 구현은 아님. 새 수관 C(t), D(t), SF 기부 공급, 독립 `P_water`와 `P_impact`, 실제 leaf-drip KE 및 강우 종료 후 배수까지 구현 후 물/유사수지 재검증 필요.

참조 [model SWEHR code audit](../models/SWEHR.md), [2026-10-26 결정](../decisions/2026-10-26_SWEHR_RUTTER_CANOPY_SHIELDING_SOURCE_AUDIT.md).

## 2026-10-27 2025 개발자 공개자료와 2017 SWEHR1.0 계보 추가대조
- 2016 published field model의 DEM 관측해상도 **2.5cm**, 실제 2D 모의격자 **37.5cm**. 본문의 수관차단 Rutter 식과 2D Hairsine-Rose 과정은 published, 그러나 실제 산불 직후 Nov/Dec 관측 재현은 수관차단 OFF. 5–10cm canopy ON validated 단일 모델로 제시 불가.
- 2017 CSDMS GitHub [SWEHR.c](https://github.com/csdms-contrib/swehr/blob/master/SWEHR.c) blob `e8505221a37d245ebb387b3304d8f325addd9ada` 1785행 전체 원본 `canop/intercep/rutter/leaf/lai` 없음 재확인. 정적 기능감사는 이전과 동일하므로 신규 개발 주장 금지.
- 2025-12-10 개발자 Luke McGuire & Aiza Kabeer HydroShare [프로필](https://hydroshare.cuahsi.org/user/8128/)에서 northern Arizona Pipeline Fire 관련 모델 및 자료 게시 확인. **압축물/UUID/실제 코드 미열람**이어서 2017 source에서 Rutter가 추가됐거나 5–10cm canopy 모델이라고 해석 금지. 상세 [새 단서 판정](../decisions/2026-10-27_SWEHR_2025_HYDROSHARE_CODE_PROVENANCE_FOLLOWUP.md).
