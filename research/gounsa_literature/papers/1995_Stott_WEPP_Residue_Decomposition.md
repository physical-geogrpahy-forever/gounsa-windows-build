# 서지정보
Stott et al. (1995). Chapter 9, Residue Decomposition and Management, USDA WEPP Documentation.

# 이 논문을 찾은 이유
WEPP의 식물 잔재와 뿌리 잔재 상태변수를 확인하기 위해 검토.

# 연구 유형
- 공식 모델 문서

# 공간 구조
- WEPP hillslope

# 적용 환경
- cropland
- rangeland

# 핵심 과정
- residue pools
- root residue pools
- rill/interrill surface protection

# 식생 입력
- standing residue
- flat residue
- buried residue
- root residue
- litter
- woody biomass

# 핵심 식
여러 residue pool을 별도로 갱신하고 surface coarse fragments도 별도 상태로 둔다.

# 파라미터와 단위
주요 mass 변수는 kg m^-2.

# 원 논문의 구현 범위
WEPP residue state의 시간변화.

# 고운사에 직접 사용할 수 있는 부분
LitterC, root residue, coarse fragments를 단일 식생항으로 합치지 않는 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS carbon pool과 WEPP mass pool 사이 변환은 새로운 coupling.

# 한계
농업관리 루틴 비중이 큼.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
USDA-ARS WEPP Documentation, Chapter 9.
