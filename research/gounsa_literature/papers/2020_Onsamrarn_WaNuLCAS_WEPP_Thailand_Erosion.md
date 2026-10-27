# 서지정보
Onsamrarn, W., Chittamart, N., & Tawornpruek, S. (2020). Performances of the WEPP and WaNuLCAS models on soil erosion simulation in a tropical hillslope, Thailand. *PLOS ONE, 15*(11), e0241689. https://doi.org/10.1371/journal.pone.0241689

# 찾은 이유
산림/농림복합식생의 LAI, 수관차단 및 뿌리 입력이 유수침식/토사 유출량에 영향을 주는 **단일모델 선례**인지 확인.

# 연구 유형 / 적용 환경
태국 Ratchaburi Province Suan Phueng 열대 사면의 옥수수 단작과 간작-생울타리 혼합 농경지에서 관측 강우사상에 대한 WEPP, WaNuLCAS 유출량/유사량 대조. 자연 참나무 맹아 및 억새 산지 선례는 아님.

# 공간 구조 / 시간
WaNuLCAS 원모형의 지상부 수관과 토양층 및 구획(zone) 구조. Genuine XY 2D SWE 유사이동 수치모형이 아닌 수평 구획 사면계산. Published 0.05–0.1m 계산격자 실증 없음. 관측 강우사상의 유사량/유출량을 평가하지만 WaNuLCAS 내부 강우/유출-침식에 자유로운 2D 격자 time-step 증거 없음.

# 핵심 과정 및 식생 상태
- LAI 등 leaf area, plant canopy, root length density, canopy interception, crop cover efficiency가 유사량 민감도에 영향을 줬다고 보고.
- Rose-type erosion / runoff-sediment relationship. 침식/퇴적 및 구획별 토양 변화 여부는 old v3 technical manual에 설명, 실측 5cm DoD 아님.
- 관측 결과: 간작의 토양손실 예측에서 WaNuLCAS 상대적으로 유리, 단작 수문예측에서 WEPP 상대적 강점. 환경과 매개변수에 대한 모델별 성능차, 보편 우열 아님.

# 핵심 식/단위
일별 soil loss를 runoff Q와 sediment concentration E를 통해 계산하는 Rose equation 유도, 식의 정확 단위는 기술매뉴얼과 논문 구획별 표로 확인. 본 연구가 LAI 자체를 침식률로 직접 동일시한 것은 아님.

# 고운사 적용 가능 / 새 coupling
식생 생체량 및 canopy 입력의 침식 모형 민감도와 현장 비교의 보조증거. 5–10cm 자유 2D 유사수송 결합은 사용자 단일 원본 조건 밖의 새로운 개발.

# 한계 / 최종 판정
**보조근거 (식생 상태-침식), 모델 자체는 탈락**: 하위 시간규모 및 자유 2D 라우팅, 완전 공개 실행원본 재현성 미충족.

# 링크
https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0241689
https://pmc.ncbi.nlm.nih.gov/articles/PMC7641452/
