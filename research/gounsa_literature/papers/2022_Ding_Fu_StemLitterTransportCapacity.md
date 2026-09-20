# 서지정보
Ding, L., & Fu, S. (2022). Sediment transport capacity as affected by different combinations of vegetation litter and stem cover. *CATENA, 211*, 106021.

# 이 논문을 찾은 이유
stem과 litter가 같은 vegetation cover로 묶여도 hydraulic effect가 다른지 확인하기 위해 검토했다.

# 연구 유형
- 실험 + 예측식

# 공간 구조
- flume/plot

# 적용 환경
- shrub-stem/litter 모사

# 핵심 과정
- flow velocity
- sediment transport capacity

# 식생 입력
- litter cover
- stem cover

# 핵심 식
이 채팅 정리에는 stem decay coefficient가 litter보다 velocity에서 약 2배, `T_c`에서 약 2.5배 강하다고 기록됨.

# 파라미터와 단위
litter cover 0-70%, stem cover 0-30%.

# 원 논문의 구현 범위
stem과 litter의 hydraulic/sediment-transport 효과를 분리.

# 고운사에 직접 사용할 수 있는 부분
Stem drag와 litter resistance를 별도 과정으로 둘 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS woody structure와 litter pool을 stem cover/litter geometry로 변환하는 것은 새로운 coupling.

# 한계
수치 지형발달모델이 아님.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2022.106021
