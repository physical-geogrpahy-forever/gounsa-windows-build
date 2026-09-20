# 서지정보
Wang, J., Yang, Y., Wang, B., Liu, G., & Li, J. (2022). Soil detachment caused by flowing water erosion in six typical herbaceous plant root systems on the Loess Plateau, China. *Biosystems Engineering, 217*, 56-67.

# 이 논문을 찾은 이유
천이단계와 root architecture가 flowing-water detachment에 미치는 효과를 확인하기 위해 검토했다.

# 연구 유형
- 실험 + 예측관계

# 공간 구조
- plot/flume

# 적용 환경
- Loess Plateau 초본군락

# 핵심 과정
- soil detachment by flowing water

# 식생 입력
- RLD
- RSAD
- root area ratio
- RMD

# 핵심 식
`D_c`가 RLD, RSAD, root area ratio, RMD 증가와 함께 지수적으로 감소한다고 정리됨.

# 파라미터와 단위
RLD, RSAD, RAR, RMD.

# 원 논문의 구현 범위
6개 초본종과 root architecture 차이를 비교.

# 고운사에 직접 사용할 수 있는 부분
초본 PFT의 root architecture별 erosion resistance 차등화 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC를 각 root-trait 지표로 변환하는 것은 새로운 coupling.

# 한계
수치 landscape model이 아님.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.biosystemseng.2022.03.001
