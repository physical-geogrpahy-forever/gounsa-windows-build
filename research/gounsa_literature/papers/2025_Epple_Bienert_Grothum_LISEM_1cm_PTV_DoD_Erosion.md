# 서지정보
Epple, L., Bienert, A., Grothum, O., Lenz, J., & Eltner, A. (2025). Uncovering fine-scale surface flow dynamics with particle tracking velocimetry: A new benchmark for soil erosion modelling. *Earth Surface Processes and Landforms*, 50(9), e70127. https://doi.org/10.1002/esp.70127

# 이 논문을 찾은 이유
초고해상도 cm급 강우사상/DEM 갱신/지표 유속/침식 및 퇴적 실측 비교의 **동일 LISEM 모델 계보** 최근 선례 확인.

# 연구 유형
독일 작물재배 시험포 강우모사, SfM before/after, PTV 표면 유속, 2개 공개 수문/침식 모델(FullSWOF_2D과 LISEM) 비교.

# 공간 구조
4개 실험포 각 약 폭0.85–0.95m × 길이2.93–2.96m (각 <3m²). SfM 1cm DEM을 생성. LISEM 계산 해상도 **0.01m, 0.025m, 0.05m, 0.075m, 0.1m** 비교, 나머지 3개 포는 1cm. 면적이 고운사 약0.648ha보다 훨씬 작음. LISEM 내 수리 routing method 정확버전은 논문 표기로 확인 안 됨; 2022 Maggioli의 kinematic-wave를 자동 전가하지 않음.

# 적용 환경
독일 작물경작지, 경운선과 소규모 세류, 경사 8.3–14.8%, 강우모사 0.6–0.8mm/min; 일부 포에 초기 무경운/멀칭 잔존, 대다수 경운 나지. 참나무 및 억새 수관 실증은 아님.

# 핵심 과정
격자별 실측 유속(PTV), SfM DoD(LoD) 산출, LISEM의 시간별 DEM 갱신 및 세류 심화에 따른 유로 변화, FullSWOF_2D는 정적 DEM. 1cm→10cm 재격자화 시 미세 세류 유로 소실과 국지 유속/저류 변화. 실제 모델 DoD와 SfM DoD 비교했으나 LISEM 모의 고도변화는 주요 흐름길에 치우치고 실측에서 나타나는 일부 분산 hotspot은 누락.

# 식생 입력
논문 실험은 수관차단 LAI에 대해 입력/검증값 제시하지 않음. 같은 LISEM 소프트웨어 계열은 interception 모듈 보유하나 **이 논문 자체가 1cm에서 식생 수관차단을 활성화하고 유사물리까지 공동 검증했다는 증거는 없음.**

# 핵심 식
SfM 차분과 M3C2-PM LoD, PTV 유속 산출, LISEM/FullSWOF 강우 침투+지표 유동 및 LISEM DEM 연동 지형변화. 구체 source numerical integrator 코드 비교 검증은 원문 외 추가 수행하지 않음.

# 파라미터와 단위
DEM 격자 0.01, .025, .05, .075, .1 m. 1cm에서 raster plot_A 약85×294, plot_B95×293, plot_C93×294, plot_D91×296 cells. 이 격자는 2~3만 셀 수준. 모의 유량 누적 및 일부 유속비교; 독립 sediment budget/timestep convergence는 논문에서 확인되지 않음.

# 원 논문의 구현 범위
**LISEM 1cm 실제 실행과 동적 DEM 업데이트, 공간유속/DoD 비교는 입증**. 전체 식생 수관차단/수관적하 계산 및 격자별 유사수지 정량 검증은 없음. 논문에 'LISEM (L,2024)'로 기술, 실행 가능한 정확한 소스 태그/SHA 미기재.

# 고운사에 직접 사용할 수 있는 부분
두 시기 LiDAR/SfM DoD+LoD와 모델 지형변화 비교, 1cm 유로 추적, 모의 유속과 영상기반 PTV 검증, 원본 코드의 강우 중 지형변화 피드백 여부 평가.

# 새로운 coupling이 필요한 부분
같은 실행버전에서 LAI/수관저류와 동적 지형변화 및 4방향 2D 흐름이 동시에 켜지는지 확인, 나지 아닌 혼재식생, 원본 numerical sediment convergence, 깊이 제한 조건.

# 한계
극히 작은 포(3m² 미만), 관측 유속 검증과 침식/퇴적량 실증 강도 동일하지 않음. 기존 OpenLISEM7.5.2 native NO-GO는 자동 해제되지 않음.

# 최종 판정
**채택: LISEM 1cm 모의와 시간별 DEM 피드백/DoD 검증 선례. 고운사 단일모델 선정은 원본 동일버전+canopy+2D 유사수지 검증 전 보류**.

# 참고 링크 / DOI
https://doi.org/10.1002/esp.70127

## 2026-10-27 모델 계보 확인: **신형 LISEM, classic OpenLISEM 7.5.2가 아님**
논문 전문 https://onlinelibrary.wiley.com/doi/10.1002/esp.70127?af=R §2.2.3은 모델을 `LISEM (L, 2024)`로 표기하고, 이 `L`의 **scripting capability**를 강조한다. 참고문헌의 `LISEM (2024) https://lisemmodel.com/`은 Bastian van den Bout의 **신형 LISEM (Lisem Integrated Spatial Earth Modeller)** 공식 홈이다. 게다가 Acknowledgments에 **Bastian van den Bout의 LISEM 지원**을 명시한다. 개발자 공식 설명 https://lisemmodel.com/docs/home/ 는 LISEM Classic과 신형 LISEM이 서로 다른 소프트웨어임을 분명하게 명시한다.
**결론:** 논문이 사용하는 모델은 신형 LISEM 계열이라고 판정할 근거가 매우 강하며, 적어도 Victor Jetten의 OpenLISEM v7.5.2 바이너리와 동등하다고 보아서는 안 된다. 정확한 신형 LISEM git tag, SHA, 패치/스크립트 내용은 논문에서 미확인이다. **과거 Gounsa OpenLISEM v7.5.2 native NO-GO를 신형 LISEM에 전가하는 것은 부정확**하며, 1cm 선행연구의 효과를 Classic 7.5.2가 직접 구현·검증했다고 해석하는 것도 부정확함.
