# 서지정보
Kim, J. K., Yang, D. Y., Kim, M. S., & Onda, Y. (2009). Evaluation of interrill erosion under forest canopy. *Hydrological Research Letters, 3*, 36–40. https://doi.org/10.3178/hrl.3.36. Original J-STAGE https://www.jstage.jst.go.jp/article/hrl/3/0/3_0_36/_article.

# 이 논문을 검색한 이유
고운사 산불 후 산지사면과 가장 지리적으로 가까운 **한국 산림의 수관 아래 침식 및 나지 비교의 실측자료**와 식생 차단을 통한 강우 운동에너지 변화를 확인. *모델 원본 논문을 찾기 위한 조사 중 발견한 검증 연구*이며 해당 논문을 수치모델로 잘못 분류하지 않음. 조사 전 `INDEX.md`에서 DOI 및 2009 Kim 동일논문 미등재.

# 연구 유형
**현장 관측 및 통계 분석**, 수치모델 개발/2D 해석기 실증 아님. J-STAGE 공식 article page와 공개 indexed full-text 요약 참조. 2006-03-30부터 2006-10-12까지 자연강우.

# 공간 구조
경기도 안성 산지사면에서 수관 아래와 비피복(open) 장소 총 **6개 0.45m×0.40m (0.18m²)** 플롯, 각 10°, 20°, 30° 경사 조건. 원자료 현장 침식구 크기는 **5~10cm native numerical grid가 아니며** 계산격자/해석시간간격 없음.

# 적용 환경
한반도 중부 안성, 산림사면. 조사지는 USCS SP 표토로 실트/점토 약4%, 모래76%, 자갈20%, 기반암 편마암(banded gneiss); 고운사 사암과 입도 차이 보정 필수.

# 핵심 과정 및 실험 방법
개방 지표와 수관 아래 지표에서 자연강우 동안 상부 강우와 수관통과우 관찰, 플롯 침식토를 수거해 실트/모래/자갈 기반의 interrill soil loss 측정. 수관 아래 침식은 개방지보다 작았고, 3시간 최대강우강도 및 총강우량과 유의하게 관련되었으며, 해당 조건에서 경사각과의 관계는 상대적으로 약했음. 강우강도 증가에 수관통과우 비율이 접근하는 점근적 경향; 침식 개시 강우강도가 그 변곡 구간과 유사하다는 기작 해석.

# 식생 입력
**실제 수관 유무(under vs open)** 및 수관통과 강우의 관측. LAI 기반 저류공간 격자식과 식생 온오프를 수치적으로 푼 모델은 없음. 수관통과강우와 수관저류 영향에 관한 인과해석은 observational treatment differences와 기상요인이 중첩 가능.

# 핵심 식 및 파라미터 단위
3h max rainfall intensity [mm h^-1], total precipitation [mm], throughfall rate [% or ratio], soil loss [g m^-2], slopes [deg], plot area0.18m². Original regression formula/threshold numeric coefficients not captured in accessible publisher abstract, do not invent.

# 원 논문의 구현 범위 / 고운사에 직접 사용할 수 있는 부분
**고운사 canopy ON/OFF의 물리기작과 침식 방향성**에 대한 국내 자연강우 관측 선례. 억새/참나무 맹아 원종별 매개변수 직접 측정 결과가 아니며 published numerical free 2D erosion model 증거는 아님. Candidate benchmark for plot sediment magnitude and threshold, not source engine.

# 필요한 새로운 coupling / 한계
No simulation source, no hydrodynamic PDE, no sediment 2D transport, no 5cm cell. Additional model writing required to convert into predictive simulator; user requests original already-used model so do not propose as main engine.

# 최종 판정
**국내 현장 검증 및 연구가설 뒷받침 보조근거**, native original high-res 2D 모델 선정 증거 **NO**.

# 참고
https://doi.org/10.3178/hrl.3.36
https://www.jstage.jst.go.jp/article/hrl/3/0/3_0_36/_article
