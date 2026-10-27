# 서지정보
Li, Z., & Tian, F. (2025). Derivation and validation of a theoretical canopy interception model based on raindrop microphysical processes. *Water Resources Research*, 61, e2024WR038296. https://doi.org/10.1029/2024WR038296

# 이 논문을 찾은 이유
고운사 드론 식생구조에서 LAI와 잎 기울기, 식생 피복이 강우 중 수관저류/수관통과를 어떻게 바꾸는지 학술 원식과 **완전 공개 Python 소스** 있는 연구를 찾기 위해. 침식모형 자체 대신 물리적 수관모형 선례로 구분.

# 연구 유형
- 수관-물방울 충돌, splash/bounce/attachment의 microphysical model derivation.
- 실험실 강우모사에 의한 수관 저류와 물방울 분포 검증.
- 저널 원문 HTML 방법론, 수식(5–13,16,18), 표6–7, Zenodo 공식 데이터/소스 항목 검색 확인.

# 공간 구조
- 격자 2D/3D 지표수 유동 모형 아님.
- 수관 식생 면적분율 gamma(FVC), LAI, leaf projection ratio G로 평균 다층 수관수지 계산.
- 층수 n≈LAI×G/gamma; 각 층별 물방울 부착/체류와 잔여 강우를 시간별 계산.
- **가로 5–10cm 해상도 검증 사례 아님**.

# 적용 환경
- 식물 수관 충돌 현상의 실험실 강우모사, 실험자료를 이용한 모델 비교.
- 고운사 억새 또는 참나무 어린 맹아의 종별 beta/p를 그대로 사용한다는 증거 없음.

# 핵심 과정
- 직접 수관통과 (1-gamma), 수관 충돌 후 splash/bounce/attachment, 시간별 저장고 포화.
- stemflow, evaporation of attached/splashed droplets는 extended formulations에 존재.
- 지표수 overland flow, Green-Ampt infiltration, rill/interrill detachment, sediment transport/deposition **없음**.

# 식생 입력
- LAI, gamma fractional vegetation cover(-), G projection ratio(-), leaf inclination angle distribution, beta attachment retention(-), p pinning fraction(-), per-layer Y_i(mm).
- 구조 변수는 관측과 LiDAR로 물리적 추정이 가능한 것을 저자들이 강조.

# 핵심 식
논문 Eq.(5–7): 
```
I_1 = gamma I_0
dw_i/dt = I_i beta p max(0, 1-w_i/Y_i)
I_(i+1) = I_i - dw_i/dt
```
I in mm/h, w_i and Y_i in mm, time h.
논문 Eq.(13), 건조 수관 시작 간소형: `w(t)=Y[1-exp(-I_bar K t/Y)]`; `K=gamma {1-[1-beta p]^(LAI G/gamma)}` (논문 Table 6).
가변 강우에 대해서는 layer-by-layer discretization Eq10 사용.
논문 Appendix C stemflow fraction proposal: `p_t=SAI/(LAI+SAI)`; 실제 어린 참나무 calibration evidence 아님.

# 파라미터와 단위
- Rainfall comparison 20/80mm/h, original splash drop experiments include 10/80mm/h.
- Model validation Table7, 20mm/h: basic R² .958 RMSE .060, simplified R² .964 RMSE .055. 80mm/h: basic R² .972 RMSE .046, simplified R² .943 RMSE .066. **해당 실험 출력과 RMSE units 원문 비교 기준에 한정**; 산지 침식 정확도 아님.
- beta,p etc field/site values require separate observed determination. Table6 K example .572 model, .112 Aston, .103 DeRoo, .7 Wang, 1 Merriam for authors' specific laboratory dataset.

# 원 논문의 구현 범위
- basic model transient multi-layer rainfall and storage, simplified average intensity.
- original lab model shows early-stage infiltration rate? NO: interception only, infiltration/soil erosion not calculated.
- 논문은 고해상도 LiDAR 기반 수관구조 입력 가능성 언급하지만 **LiDAR 기반 5cm 산림사면 침식 실증이 수행된 연구는 아님**.

# 고운사에 직접 사용할 수 있는 부분
- 단순 LAI to fixed Smax 가정보다 물방울 충돌과 포화과정을 설명하는 published canopy equation.
- canopy dynamics만 독립 검증할 경우 공개 Python 모델과 표7을 벤치마크로 활용 가능. 단일 침식 엔진이라고 할 수 없음.

# 실제 소스 코드 확인
- 공식 Zenodo release **DOI https://doi.org/10.5281/zenodo.15045577** ; version v2 published 2025-03-18.
- 공개 파일 목록에 `model_runrun_basic.py` (5.0kB), `model_runrun_simplified.py` (5.7kB), `data_share.xlsx`, `read_me.txt`, 영상 .rar 확인.
- **이번 조사에서 실제 Python 파일 내용을 내려받아 실행한 것은 아님.** 파일 목록 공개는 확인되지만 native reproducibility PASS 아님.

# 새로운 coupling이 필요한 부분
- canopy water budget -> overland rain supply; canopy drop energy -> actual soil splash; lateral drip localization; species-specific beta/p.
- 이 모델을 단일 2D soil erosion engine의 일부로 결합하면 **새로운 coupling**이며 user requirement 단일 발표 원본 만족 아님.

# 한계
- 식생 피복률 자체가 뿌리/생물량 대체변수라는 해석 금지.
- leaf-drop splash water particle distribution을 모형이 다룬다고 지표 토사박리 계산까지 하는 것으로 해석 금지.
- 기존 지형 연구 다른 모델과 결합된 원저 검증 실적 아님.

# 최종 판정
**보조근거(독립 수관차단 물리+실제 공개 원본 Python).** 주모델로는 탈락.

# 참고 링크 / DOI
https://doi.org/10.1029/2024WR038296
https://zenodo.org/records/15045577
https://doi.org/10.5281/zenodo.15045577
