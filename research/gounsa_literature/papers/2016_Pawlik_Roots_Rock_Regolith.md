# 서지정보
Pawlik, Ł., Phillips, J. D., & Šamonil, P. (2016). Roots, rock, and regolith: Biomechanical and biochemical weathering by trees and its impact on hillslopes—A critical literature review. *Earth-Science Reviews, 159*, 142–159. https://doi.org/10.1016/j.earscirev.2016.06.002

# 이 논문을 찾은 이유
고운사에서 C/Cr까지 침투하는 뿌리가 기반물질의 물리풍화와 화학풍화에 미치는 영향을 정리하기 위해 검토했다.

# 연구 유형
- 리뷰

# 공간 구조
- 특정 수치격자 없음

# 적용 환경
- 산림
- 기반암과 레골리스
- tree-root weathering

# 핵심 과정
- biomechanical weathering
- biochemical weathering
- root wedging
- tree uprooting
- rhizosphere weathering

# 식생 입력
- tree roots
- root system architecture
- tree uprooting

# 핵심 식
단일한 범용 root-weathering 수치식을 제안하는 논문이 아니라 기존 기작과 관측을 종합한 리뷰다.

# 파라미터와 단위
범용 단일계수 없음.

# 원 논문의 구현 범위
나무뿌리가 암석과 레골리스에 가하는 기계적, 생화학적 풍화과정을 정리한다.

# 고운사에 직접 사용할 수 있는 부분
고운사에서 뿌리가 C/Cr까지 접근할 수 있고, 토양층 아래에서도 풍화와 물리적 파쇄에 기여할 수 있다는 과정적 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC 또는 cohort 정보를 실제 root fracture rate로 변환하는 식은 리뷰에서 제공되지 않으며 새로운 coupling이다.

# 한계
- 리뷰이므로 직접 실행 가능한 수치모델이 아님
- root biomass에서 풍화율로 가는 범용 함수가 없음

# 최종 판정
- 과정근거로 채택
- 수치 매개변수 근거로는 보조적

# 참고 링크 / DOI
https://doi.org/10.1016/j.earscirev.2016.06.002
