# 서지정보
Arnold et al. (1995). Chapter 8, Plant Growth Component, USDA WEPP Documentation, NSERL Report No. 10.

# 이 논문을 찾은 이유
WEPP의 식생 생체량과 뿌리 상태변수 정의를 확인하기 위해 검토.

# 연구 유형
- 공식 수치모델 문서

# 공간 구조
- WEPP 1D hillslope component

# 적용 환경
- cropland
- rangeland

# 핵심 과정
- plant growth
- biomass
- root growth
- root depth
- senescence

# 식생 입력
- above-ground biomass
- root mass
- root depth
- LAI
- canopy height

# 핵심 식
Brt(i) = Brt(i-1) + ΔBi Rsr.
Root mass를 여러 토심대로 분배한다.

# 파라미터와 단위
Brt와 RTMMAX는 kg m^-2, Rd는 m.

# 원 논문의 구현 범위
WEPP 내부 식생과 뿌리 생체량의 시간변화.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS 출력을 erosion parameter로 전달할 때 WEPP가 기대하는 변수 정의 참고.

# 새로운 coupling이 필요한 부분
LPJ-GUESS와 WEPP 변수 연결은 새로운 coupling.

# 한계
WEPP 식생모델 자체를 고운사에 채택하는 것은 아님.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
USDA-ARS WEPP Documentation, Chapter 8.
