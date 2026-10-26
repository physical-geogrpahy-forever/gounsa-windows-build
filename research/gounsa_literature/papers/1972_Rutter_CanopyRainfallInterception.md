# 서지정보
Rutter, A. J., Kershaw, K. A., Robins, P. C., & Morton, A. J. (1972). A predictive model of rainfall interception in forests, 1. Derivation of the model from observations in a plantation of Corsican pine. *Agricultural Meteorology, 9*, 367–384. https://doi.org/10.1016/0002-1571(71)90034-3

# 이 논문을 찾은 이유
SWEHR McGuire et al. 2016 논문의 수관차단식(§3.5, 24–26)이 참조한 Rutter 원 모형의 물수지 구조를 확인하기 위함.

# 연구 유형
수관 수문모형과 관측 검증. [A: 출판된 원문 초록 확인, 본문 전체 미확보]

# 공간 구조
시간별 수관 저류 수지. 일반적인 genuine 2D 지표유동 또는 2D 유사이송 모형이 아님.

# 적용 환경
Corsican pine(Pinus nigra) 조림지. 화재 후 고운사 억새와 참나무 맹아의 실측 수관구조 아님.

# 핵심 과정
강우 일부가 직접 수관 통과, 잎/줄기에 임시 저류, 증발, 배수/적하로 돌아가는 시간 변화. Drainage and evaporation depend on time-varying canopy water amount, not fixed annual fraction.

# 식생 입력
수관 저장용량 및 임분구조, 직접 수관 통과 비율 등.

# 핵심식
수지의 일반형은 dC/dt=(1-p)P-D-E. 이는 해석용 요약이며, 확장 모형에서 수간/줄기저류 분기와 수관피복 분율은 별도 고려. `D` is dynamically dependent on canopy storage; generic Rutter drainage law often exponential `D=D_s exp[b(C-S)]`, but original exact functional implementation should be audited from the full text when using as original source.

# 파라미터와 단위
P,D,E [mm h^-1], canopy store C and capacity S [mm], p [0,1]; SI consistency before SWEHR integration required.

# 원 논문 구현 범위
수관 강우차단 수지. 수관 적하의 물방울 운동에너지와 지표 침식량 직접 모의하지 않음.

# 고운사에 직접 사용할 수 있는 부분
SWEHR의 2D SWE water source를 입사강우 P가 아니라 일시저류와 배수에 따른 시간별 지표도달 강우로 변경할 때 원본 계보.

# 새로운 coupling
C(t), D(t) and E(t) by patch and plant → original SWEHR Pwater spatial forcing, separate impact energy.

# 한계
소나무 조림 관측 및 수관 구조가 다른 계절/종; 직접 species coefficient 이식 금지.

# 최종 판정
Rutter 수관수문방정식의 원전 보조근거, 결합부 필요.

# 참고 링크
https://www.sciencedirect.com/science/article/pii/0002157171900343
