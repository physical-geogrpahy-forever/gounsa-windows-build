# 서지정보
Li, Z., & Tian, F. (2026). Derivation and validation of estimation model of rainfall kinetic energy under the canopy. Hydrology and Earth System Sciences, 30, 3203–3219. https://doi.org/10.5194/hess-30-3203-2026

# 이 논문을 찾은 이유
자유 수관통과우와 수관적하우의 운동에너지 구분을 기존 강우박리 모듈과 물리적으로 연결할 근거 확인.

# 연구 유형
수관하 강우 운동에너지 계산모형 유도 및 검증.

# 공간 구조
수관하 강우 구성성분 단위. 2D erosion solver는 아님.

# 적용 환경
수목 수관하 강우 특성; 산불 후 사암사면에 직접 검증 아님.

# 핵심 과정
직접 통과 빗방울, 튀김방울, 수관적하의 크기/속도와 운동에너지 분리. 잎 각도, LAI, 수관높이, 표면 접촉각의 효과.

# 식생 입력
LAI, leaf inclination/contact angle, branch height, canopy traits, rainfall drop-size distribution.

# 핵심 식
원문 §2: 성분별 방울 질량과 속도로 KE 산정한 뒤 free throughfall, splash, drip KE를 합산. 지표유출/유사수송 방정식은 미포함.

# 파라미터와 단위
KE flux [J m-2 h-1], 개별 에너지 [J], drop diameter [m], velocity [m/s].

# 원 논문의 구현 범위
수관하 KE 모형 검증, 침식량 산정/수간유하 runoff 미구현.

# 고운사에 직접 사용할 수 있는 부분
수관차단이 단순히 지표 박리에너지를 비례 감소시킨다는 가정을 피할 근거.

# 새로운 coupling이 필요한 부분
시간별/공간별 TF 구성성분 KE를 SWEHR rainfall detachment에 전달하되 원래 계수 및 단위 재검토 필요.

# 한계
수관적하 KE 증폭을 모든 식생에 일반화할 수 없으며 자체 침식모델이 아님.

# 최종 판정
핵심 보조근거(수관→강우박리 에너지 경계조건).

# 참고 링크 / DOI
https://hess.copernicus.org/articles/30/3203/2026/hess-30-3203-2026.html
