# 서지정보
Guignabert, A., Ponette, Q., André, F., Messier, C., Nolet, P., & Jonard, M. (2023). Validation of a new spatially explicit process-based model (HETEROFOR) to simulate structurally and compositionally complex forest stands in eastern North America. Geoscientific Model Development, 16, 1661-1683. DOI: 10.5194/gmd-16-1661-2023

# 이 논문을 찾은 이유
HETEROFOR가 특정 유럽 활엽수 몇 종에만 국한된 모델인지, 다종 온대림과 장기 천이에 실제 검증됐는지 확인했다.

# 연구 유형
- 모델 검증
- 공간명시적 개체목 forest dynamics

# 공간 구조
- individual trees with x,y,z and crown dimensions
- regeneration cohorts on spatial cells
- saplings spatialized after recruitment threshold

# 적용 환경
- eastern North America temperate forests
- mixed and uneven-aged stands
- 23 tree species
- 5-16 year short-term and 120-year long-term tests

# 핵심 과정
- growth
- competition
- mortality
- regeneration
- water/light limitation

# 식생 입력
- tree coordinates and dimensions
- soil horizons and fine-root proportion
- hourly meteorology

# 핵심 식
기본 HETEROFOR 1.0 탄소수지 및 수문식을 23종으로 parameterize한다.

# 파라미터와 단위
- short-term validation: 5-16 yr
- long-term simulation: 120 yr
- stand-scale mixed species

# 원 논문의 구현 범위
복잡한 온대 산림에서 개체목 성장과 사망, 장기 임분동태를 평가한다.

# 고운사에 직접 사용할 수 있는 부분
- 100년 시간범위와 직접 맞음
- 혼효림, 다종, 불균일 연령 구조
- LiDAR tree inventory 초기화 구조

# 새로운 coupling이 필요한 부분
- Korean species parameterization
- postfire tissue mortality
- geomorph feedback

# 한계
한국 온대림 수종으로 검증된 것은 아니다. native wildfire 과정은 이 검증의 핵심 모듈이 아니다.

# 최종 판정
- 채택 후보
- HETEROFOR의 100년 온대 혼효림 적용가능성 근거

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-16-1661-2023
