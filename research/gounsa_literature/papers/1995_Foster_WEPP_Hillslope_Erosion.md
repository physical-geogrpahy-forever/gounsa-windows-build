# 서지정보
Foster et al. (1995). Chapter 11, Hillslope Erosion Component, USDA WEPP Documentation.

# 이 논문을 찾은 이유
WEPP가 interrill과 rill erosion을 어떻게 분리하는지 확인하기 위해 검토.

# 연구 유형
- 공식 수치모델 문서

# 공간 구조
- 1D hillslope profile

# 적용 환경
- hillslope

# 핵심 과정
- interrill sediment delivery
- rill detachment
- deposition
- sediment transport capacity

# 식생 입력
Chapter 7에서 조정된 Ki와 Kr가 전달된다.

# 핵심 식
Sediment continuity는 rill term과 interrill term의 합으로 구성된다. Rill detachment는 Kr, flow shear, critical shear, transport capacity를 사용하며 interrill term은 Ki, rainfall intensity, runoff를 사용한다.

# 파라미터와 단위
Ki는 kg s m^-4 계열, Kr는 s m^-1, shear stress는 Pa.

# 원 논문의 구현 범위
분리된 rill/interrill hillslope erosion.

# 고운사에 직접 사용할 수 있는 부분
root-adjusted Ki와 Kr를 erosion physics에 전달하는 원 구조.

# 새로운 coupling이 필요한 부분
genuine 2D engine으로 옮기는 것은 새로운 coupling.

# 한계
1D이며 spatial rill-network evolution이 없다.

# 최종 판정
- 채택: process structure
- 미채택: final 2D engine

# 참고 링크 / DOI
USDA-ARS WEPP Documentation, Chapter 11.
