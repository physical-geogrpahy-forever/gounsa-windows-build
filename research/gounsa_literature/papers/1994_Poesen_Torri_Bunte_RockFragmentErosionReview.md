# 서지정보
Poesen, J. W., Torri, D., & Bunte, K. (1994). Effects of rock fragments on soil erosion by water at different spatial scales: a review. *CATENA, 23*(1-2), 141-166. https://doi.org/10.1016/0341-8162(94)90058-2

# 이 논문을 찾은 이유
고운사에서 fire spall 및 기존 석력이 surface armour를 만들 때 토양 유실을 항상 감소시키는지, 그리고 그 효과가 공간규모, 입도, 경사, 매립상태에 따라 달라지는지 확인하기 위해 검토했다.

# 연구 유형
- 리뷰
- 과정 종합

# 공간 구조
- microplot
- mesoplot
- macroplot

# 적용 환경
- stony soils
- 다양한 자연 및 실험 사면

# 핵심 과정
- interrill erosion
- rill erosion
- rock-fragment shielding
- horseshoe-vortex erosion
- surface stabilization

# 식생 입력
- 없음

# 핵심 식
macroplot scale에서 상대 sediment yield와 rock-fragment cover 사이에 exponential decay 관계를 정리한다.
다만 mesoplot/interrill scale에서는 rock fragments가 sediment yield를 증가 또는 감소시킬 수 있으며 효과 방향은 fine-earth porosity, slope, fragment vertical position, size와 horseshoe-vortex erosion에 좌우된다.

# 파라미터와 단위
- rock-fragment cover [- 또는 %]
- sediment yield
- fragment size
- slope
세부 경험계수는 원문 사용 시 재검증한다.

# 원 논문의 구현 범위
석력의 erosion-control 효과가 단일 cover factor가 아니라 규모와 배치 및 입도에 의존함을 종합한다.

# 고운사에 직접 사용할 수 있는 부분
- armour shielding을 interrill/rill detachment 감소항으로 둘 근거
- armour 효과를 fragment cover 하나로만 결정하지 않을 근거
- 큰 spall과 작은 spall을 동일한 보호효율로 처리하지 않을 근거

# 새로운 coupling이 필요한 부분
fire-spall size distribution과 고운사 2D erosion engine의 detachment/transport parameter를 연결하는 것은 **새로운 coupling**이다.

# 한계
리뷰이며 고운사 산림 또는 산불 후 사암사면에 직접 보정된 수치모델이 아니다.

# 최종 판정
- 핵심 보조근거
- dynamic armour parameterization의 기본 문헌

# 참고 링크 / DOI
https://doi.org/10.1016/0341-8162(94)90058-2
