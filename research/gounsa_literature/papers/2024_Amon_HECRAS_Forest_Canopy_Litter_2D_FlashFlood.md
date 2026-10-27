# 서지정보
Ámon, G., Bene, K., Ray, R. P., Gribovszki, Z., & Kalicz, P. (2024). Improving flash flood hydrodynamic simulations by integrating leaf litter and interception processes in steep-sloped natural watersheds. *Water, 16*(5), 750. https://doi.org/10.3390/w16050750

# 이 논문을 검색한 이유
**급경사 산림에서 canopy + litter + genuinely 2D hydrodynamic**을 실제 관측 강우사상에 적용한 연구가 있는지 검증. 다만 지표유출 모델만으로 침식 주모델을 판단하지 않음.

# 연구 유형과 적용 환경
헝가리 Hidegvíz 산림계곡의 계측 유역 강우사상 두 개(2010-07-15, 2012-06-07)를 대상으로 HEC-RAS 2D 유동 계산과 수관차단 및 낙엽저류 처리 방식 두 개를 비교한 동료심사 논문.

# 공간 구조 및 시간
HEC-RAS 2D의 FVM 기반 SWE hydrodynamics. 적응 계산격자 크기 산지 및 수로에서 **4×4m에서 20×20m**. 강우사상 1일 규모이며 별도의 5–10cm 침식 계산 없음.

# 핵심 과정
- 방법 A: 수관 및 낙엽 차단/저류량을 강우시계열에서 선공제하고 지면에 남는 유효강우로 유동을 계산.
- 방법 B: 수관차단 후 낙엽층은 가상 높은 공극률과 투수성의 토양층으로 표현.
- `h_eff = h - I_c - I_l - S_d - F_s`(방법 A: 같은 간격 수심 단위 mm), 방법 B는 litter infiltration `F_l`을 사용. 모델 내 강우/침투/유동 처리와 **수관차단은 전처리 또는 별도 산정의 결합**이므로 HEC-RAS 원본 native dynamic LAI canopy bucket이라고 주장 금지.
- peak discharge/event model fit reported, 침식모듈 및 국지 퇴적고 **연구에서 검증 안함**.

# 식생 입력 및 고운사 적용
수관차단과 낙엽층 저류를 산림 급경사 2D 수리모델에 반영했다는 관측강우 기반 적용 근거. LAI 계산 경로는 본문 상세식을 추가 확인해야 하며 현재 자료만으로 특정 LAI식 동작 판정 금지. 억새/참나무/나지 cm급 식생 패치와 구분.

# 핵심 매개변수와 단위
격자폭 4–20m, 강우/차단/저류/침투는 mm; 유량 m3/s. 모의 홍수첨두는 event hydrograph를 대조. 수관 및 낙엽 저류는 각각 별도 물리적 경로.

# 원 논문의 구현 범위와 한계
두 사상에서 수문 hydrograph 검증만 수행. 구획별 sediment detachment/transport/deposition 2D field calculation 자료 없음. HEC-RAS 본체의 별도 2D sediment capability 존재와 해당 canopy+sediment 같은 실행사상 실증을 혼동하면 안 됨.

# 필요한 새로운 coupling
고운사 침식/퇴적/강우타격 등 신규 계산을 추가하는 것은 새 모델 결합으로 취급, 단일 원본 배포기능이 아님.

# 최종 판정
**보조근거: 급경사 산림+2D SWE+수관 및 낙엽처리**, **주모델 탈락: 5–10cm과 직접 유수침식/국지 퇴적 same-run 확인되지 않음**.

# 링크
https://doi.org/10.3390/w16050750
https://www.mdpi.com/2073-4441/16/5/750
