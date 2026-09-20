# 서지정보
Hwang et al. (2015). JGR Biogeosciences. DOI: 10.1002/2014JG002824. 정확한 제목과 전체 저자목록은 원문 재검증 필요.

# 이 논문을 찾은 이유
belowground biomass를 root cohesion과 factor of safety로 연결한 published model precedent 확인.

# 연구 유형
- 수치모델 + 공간자료

# 공간 구조
- distributed hillslope/watershed
- infinite-slope framework

# 적용 환경
- 산림 산지

# 핵심 과정
- root cohesion
- shallow landslide stability

# 식생 입력
- total belowground biomass
- root tissue density
- root tensile strength
- root depth distribution

# 핵심 식
BGB를 root area/geometry로 변환하고 tensile strength를 결합하여 root cohesion Cr을 계산한 뒤 factor of safety에 넣는다.

# 파라미터와 단위
BGB는 kg m-2 계열, Cr은 kPa 계열. 세부식 원문 재검증 필요.

# 원 논문의 구현 범위
산림의 공간적으로 변하는 root biomass를 slope stability에 연결.

# 고운사에 직접 사용할 수 있는 부분
FineRootC/BGB -> root cohesion -> FS bridge.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC를 BGB 및 depth distribution으로 변환하는 부분은 새로운 coupling.

# 한계
DGVM과 직접 결합된 모델은 아님.

# 최종 판정
- 채택: slope-stability bridge
