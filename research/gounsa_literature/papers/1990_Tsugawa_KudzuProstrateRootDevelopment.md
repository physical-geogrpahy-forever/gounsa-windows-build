# 서지정보
Tsugawa, H., Sasek, T. W., Komatsu, N., & Nishikawa, K. (1990). Development of prostrate stems and root systems of first year stands of kudzu-vine (*Pueraria lobata* Ohwi) differing in spacing. *Japanese Journal of Grassland Science, 36*(1), 9-19.

# 이 논문을 찾은 이유
칡이 seedling establishment 이후 어떤 방식으로 지표를 따라 확장하고 rooting network를 형성하는지, 그리고 고운사에서 nearby clonal source의 존재를 별도 상태로 둘 필요가 있는지 확인하기 위해 검토했다.

# 연구 유형
- first-year growth experiment

# 공간 구조
- stand/plant spacing experiment
- prostrate stem and root-system network

# 적용 환경
- kudzu stand development

# 핵심 과정
- prostrate stem expansion
- node/root development
- clonal spatial spread
- first-year establishment

# 식생 입력
- Pueraria lobata
- planting spacing

# 핵심 식
보편적 경쟁방정식보다 시간에 따른 stem length와 root-system development를 추적한다.
first-year kudzu가 빠르게 긴 prostrate stems를 만들고 공간을 점유하며 root system을 발달시키는 구조가 핵심이다.

# 파라미터와 단위
- plant spacing
- total stem length per area
- root-system distribution
- seasonal time

# 원 논문의 구현 범위
칡의 빠른 공간확장이 단순 local biomass growth가 아니라 포복경과 절/뿌리 형성을 통한 clonal network process임을 보여준다.

# 고운사에 직접 사용할 수 있는 부분
- kudzu를 일반 herbaceous PFT와 동일한 local establishment/growth만으로 처리하면 안 될 근거
- nearby kudzu patch에서의 clonal access 또는 lateral spread state를 별도로 둘 근거

# 새로운 coupling이 필요한 부분
LPJ-GUESS grid/cell 사이의 kudzu clonal spread를 구현하면 **새로운 coupling**이다.

# 한계
산불 및 stony-armour 조건을 직접 다루지 않는다.

# 최종 판정
- 보조근거
- kudzu propagule/clonal-access state의 근거

# 참고 링크 / DOI
Journal of Japanese Society of Grassland Science 36(1): 9-19. DOI 미확인.
