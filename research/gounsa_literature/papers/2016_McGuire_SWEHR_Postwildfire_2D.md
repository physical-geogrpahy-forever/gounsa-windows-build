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
