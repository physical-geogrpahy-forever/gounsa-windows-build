# 서지정보
Apip, Tachikawa, Y., Sayama, T., & Takara, K. (2008). Lumping a physically-based distributed sediment runoff model with embedding river channel sediment transport mechanism. Annuals of Disaster Prevention Research Institute, Kyoto University, 51B, 103–118. 기관 연구보고서.

# 이 논문을 찾은 이유
차단-수관통과우-수간유하우-침투/유출-침식 전 과정이 동일한 발표 모형에 연결되어 있는지 확인.

# 연구 유형
수치모형 방법론 / 기관 보고서. 일반 심사 학술지 논문과 구분.

# 공간 구조
CDRMV3 기반 격자별 사면과 하천의 유출 및 토사량, 기초 수문은 1D kinematic wave; 250 m×250 m 격자. Genuine 2D 아님. lumped 버전과 원 distributed 버전 구별 필요.

# 적용 환경
인도네시아 Lesti River 유역. 한국의 산불 산지에 직접 검증되지 않음.

# 핵심 과정
강우: 직접 수관통과우 DT, 수관차단 저류 ICstore, 일시적 차단 후 유입 TIF, 수간유하 SF, 잎 배수 LD.
지표 도달 유효강우 = DT + SF + LD. 수문: 불포화/포화 사면유출 및 지표유출. 침식: 강우박리 DR, 흐름에 의한 박리/퇴적 DF, 유사연속식 및 수송.

# 식생 입력
식생 피복 COV, 저장용량 ICmax, 줄기 각도 PA, 식생유형. 정량 biomass 기반 생태동태는 아님.

# 핵심 식
논문 Figure 1 강우분배 과정, Figure 3 격자별 유사 연속. 식 (3): ∂(h_s C)/∂t + ∂(q_s C)/∂x = DR + DF. 기초 1D 흐름과 격자간 routing.
중요: 세 성분은 net rainfall로 합산되므로 실제 개체목 기부 국지 집중을 보존하는 구현이라고 단정하면 안 됨.

# 파라미터와 단위
q_s [m³/s], C [kg/m³], h_s [m], DR/DF [kg/m²/hr] (원문); 공간격자 250 m.

# 원 논문의 구현 범위
강우분배와 지표유출-유사수송이 연결된 출판된 모형. 국지적 수간유하우 침투경로와 자유로운 2D 유수흐름은 해당하지 않음.

# 고운사에 직접 사용할 수 있는 부분
하나의 모형에서 3성분 강우분배와 분리된 강우박리/유수박리를 연계한 발표 선례.

# 새로운 coupling이 필요한 부분
개체별 수간유하 국지 분배, high-res 2D shallow water, coarse fragments 및 root-biomass 영향.

# 한계
수간유하를 합산 후 공간 집중 손실; 다수 과정은 식생 피복 계수. 발표 범주 보고서.

# 최종 판정
보조근거. 통합 구조 선례, 고운사 최종 엔진 아님.

# 참고 링크 / DOI
https://www.dpri.kyoto-u.ac.jp/nenpo/no51/ronbunB/a51b0p10.pdf
